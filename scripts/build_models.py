#!/usr/bin/env python3
"""Build an interactive 3D model (.glb) of a badge or SAO from the design files fetched by fetch_hardware.py.

Two methods, chosen automatically per entry:
  kicad   a real 3D export from the KiCad board (kicad-cli pcb export glb, Draco-compressed), used when the result is small
          enough; KiCad boards also get a gerber export so the second method can serve as the fallback
  gerber  a "textured slab": the top and bottom of the board rendered from the Gerber files with tracespace, wrapped onto a
          1.6 mm extrusion of the board outline (holes included). Small, uniform, works for any fabrication file set.

Writes assets/models/<event>/<slug>.glb and a `model:` block into the entry's front matter. Never overwrites an entry's
other fields. Run inside the project virtualenv: .venv/bin/python scripts/build_models.py [--id ID | --all] [--limit N]
"""
import argparse, glob, io, json, os, re, shutil, subprocess, sys, tempfile, datetime
import numpy as np, yaml
from PIL import Image
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HW = os.path.join(ROOT, "data", "hw"); MANIFEST = os.path.join(ROOT, "data", "hw_manifest.json")
MODELS = os.path.join(ROOT, "assets", "models"); REPORT = os.path.join(ROOT, "data", "models_report.json")
KICAD_CLI = ["flatpak", "run", "--filesystem=home", "--command=kicad-cli", "org.kicad.KiCad"]
KICAD_PY = ["flatpak", "run", "--filesystem=home", "--command=python3", "org.kicad.KiCad"]
THICK = 1.6; TEX_MAX = 1024; FULL_GLB_MAX = 6 * 1024 * 1024
BUILD_DIR = [None]  # set per entry so kicad exports stay out of assets/ until finished
GERBER_EXT = (".gbr", ".gtl", ".gbl", ".gko", ".gm1", ".gm2", ".gbs", ".gts", ".gbo", ".gto", ".gbp", ".gtp", ".drl", ".xln", ".txt", ".gml", ".gd1", ".g2", ".g3")

yaml.add_representer(OrderedDict, lambda d, x: d.represent_mapping("tag:yaml.org,2002:map", x.items()))
yaml.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None))

def log(*a): print(*a, flush=True)
def run(cmd, timeout=600, cwd=None):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd)
    return r.returncode, (r.stdout or "") + (r.stderr or "")

# ---------- locating inputs ----------
def gerber_dirs(root):
    """Directories under root that hold a plausible gerber set (an outer copper + an outline or mask layer)."""
    out = []
    for d, _, files in os.walk(root):
        if "_build" in d: continue
        low = [f.lower() for f in files]
        cu = any(f.endswith((".gtl", ".gbl")) or re.search(r"([fb][_.-]?cu|copper|top|bottom).*\.(gbr|ger|art|pho)$", f) for f in low)
        edge = any(f.endswith((".gko", ".gm1", ".gm2", ".gml")) or re.search(r"(edge|outline|profile|board|dimension|milling)", f) for f in low)
        mask = any(f.endswith((".gts", ".gbs")) or "mask" in f for f in low)
        if cu and (edge or mask): out.append((d, len([f for f in low if f.endswith(GERBER_EXT)])))
    return [d for d, n in sorted(out, key=lambda x: -x[1])]

def kicad_boards(root):
    return sorted([p for p in glob.glob(os.path.join(root, "**", "*.kicad_pcb"), recursive=True) if "_build" not in p and "backup" not in p.lower()], key=lambda p: (p.count("/"), -os.path.getsize(p)))

def eagle_boards(root):
    out = []
    for p in glob.glob(os.path.join(root, "**", "*.brd"), recursive=True):
        try: head = open(p, "rb").read(200)
        except Exception: continue
        if b"<?xml" in head or b"<eagle" in head: out.append(p)
    return out

# ---------- gerber -> slab ----------
def tracespace(gdir, outdir):
    files = [os.path.join(gdir, f) for f in os.listdir(gdir) if os.path.isfile(os.path.join(gdir, f)) and not f.lower().endswith((".png", ".jpg", ".pdf", ".md", ".csv", ".zip", ".html", ".json", ".step", ".stp"))]
    rc, out = run(node_bin("tracespace", "@tracespace/cli") + ["-L", "-q", "-o", outdir] + files, timeout=600)
    top = glob.glob(os.path.join(outdir, "*.top.svg")); bot = glob.glob(os.path.join(outdir, "*.bottom.svg"))
    if not top or not bot: raise RuntimeError("tracespace produced no board render: " + out[-300:])
    return top[0], bot[0]

def svg_size_mm(svg):
    head = open(svg, encoding="utf-8", errors="ignore").read(2000)
    def dim(name):
        m = re.search(r'(?<![-\w])' + name + r'="([\d.]+)(mm|in|cm)?"', head)
        if not m: return None
        v = float(m.group(1)); u = m.group(2) or "mm"
        return v * (25.4 if u == "in" else 10 if u == "cm" else 1)
    return dim("width"), dim("height")

TOOLS = os.path.join(ROOT, "tools")
def node_bin(name, pkg):
    local = os.path.join(TOOLS, "node_modules", ".bin", name)
    return [local] if os.path.exists(local) else ["npx", "--yes", pkg]

def rasterize(svg, width_px):
    """tracespace SVGs rely on CSS classes and <use>; resvg renders them faithfully (cairosvg draws nothing)."""
    out = svg + ".png"
    rc, msg = run(["node", os.path.join(TOOLS, "svg2png.js"), svg, out, str(width_px)], timeout=300)
    if rc != 0 or not os.path.exists(out): raise RuntimeError("resvg failed: " + msg[-200:])
    im = Image.open(out).convert("RGBA"); im.load(); os.remove(out)
    return im

def board_color(img):
    a = np.asarray(img); m = a[..., 3] > 200
    if m.sum() < 100: return (30, 90, 40)
    px = a[m][:, :3]
    med = np.median(px, axis=0)  # the solder mask dominates the opaque area on most boards
    return tuple(int(x) for x in med)

def contours_mm(mask, px_per_mm, h_px, min_hole_mm2=1.2):
    import cv2
    from shapely.geometry import Polygon
    from shapely.validation import make_valid
    cs, hier = cv2.findContours(mask.astype(np.uint8), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    if hier is None: raise RuntimeError("no board outline found in render")
    hier = hier[0]; polys = []
    areas = [cv2.contourArea(c) for c in cs]
    biggest = max(areas) if areas else 0
    for i, c in enumerate(cs):
        if hier[i][3] != -1 or areas[i] < 0.01 * biggest or len(c) < 3: continue
        holes = []
        j = hier[i][2]
        while j != -1:
            if areas[j] / (px_per_mm ** 2) >= min_hole_mm2 and len(cs[j]) >= 3:
                holes.append([((x) / px_per_mm, (h_px - y) / px_per_mm) for [[x, y]] in cs[j]])
            j = hier[j][0]
        outer = [((x) / px_per_mm, (h_px - y) / px_per_mm) for [[x, y]] in c]
        p = Polygon(outer, holes).simplify(0.08, preserve_topology=True)
        p = make_valid(p)
        if p.geom_type == "MultiPolygon": polys += [g for g in p.geoms if g.area > 1]
        elif p.geom_type == "Polygon": polys.append(p)
    if not polys: raise RuntimeError("outline polygon empty")
    return polys

def build_slab(top_svg, bot_svg, out_glb):
    import trimesh
    w_mm, h_mm = svg_size_mm(top_svg)
    if not w_mm or not h_mm: raise RuntimeError("svg without physical size")
    scale = TEX_MAX / max(w_mm, h_mm)           # px per mm
    w_px = int(round(w_mm * scale)); h_px = int(round(h_mm * scale))
    top = rasterize(top_svg, w_px).resize((w_px, h_px)); bot = rasterize(bot_svg, w_px).resize((w_px, h_px))
    mask = (np.asarray(top)[..., 3] > 40)
    if mask.mean() < 0.02: raise RuntimeError("render is empty")
    color = board_color(top)
    note = ""
    try:
        polys = contours_mm(mask, scale, h_px)
    except RuntimeError:
        from shapely.geometry import box
        ys, xs = np.where(mask)
        if len(xs) < 50: raise
        x0, x1, y0, y1 = xs.min() / scale, (xs.max() + 1) / scale, (h_px - ys.max() - 1) / scale, (h_px - ys.min()) / scale
        polys = [box(x0, y0, x1, y1)]; note = "The published files have no board outline, so the model is shown on a rectangular board."
    # atlas: top over bottom, transparent pixels filled with the board colour
    bg = Image.new("RGBA", (w_px, h_px), color + (255,))
    top_f = Image.alpha_composite(bg, top).convert("RGB"); bot_f = Image.alpha_composite(bg, bot).convert("RGB")
    atlas = Image.new("RGB", (w_px, 2 * h_px)); atlas.paste(top_f, (0, 0)); atlas.paste(bot_f, (0, h_px))
    if os.environ.get("MODEL_DEBUG"):
        dbg = os.path.join(os.path.dirname(top_svg), "debug"); os.makedirs(dbg, exist_ok=True)
        atlas.save(os.path.join(dbg, "atlas.jpg"), quality=80); Image.fromarray((mask * 255).astype(np.uint8)).save(os.path.join(dbg, "mask.png"))
        print("debug images in", dbg, flush=True)
    buf = io.BytesIO(); atlas.save(buf, "JPEG", quality=85, optimize=True); buf.seek(0); atlas_j = Image.open(buf); atlas_j.load()
    faces_mesh = []; side_mesh = []
    for poly in polys:
        m = trimesh.creation.extrude_polygon(poly, THICK)
        nz = m.face_normals[:, 2]
        tb = np.where(np.abs(nz) > 0.9)[0]; sd = np.where(np.abs(nz) <= 0.9)[0]
        if len(tb): faces_mesh.append(m.submesh([tb], append=True))
        if len(sd): side_mesh.append(m.submesh([sd], append=True))
    fm = trimesh.util.concatenate(faces_mesh); sm = trimesh.util.concatenate(side_mesh) if side_mesh else None
    v = fm.vertices; is_top = v[:, 2] > THICK / 2
    u = np.where(is_top, v[:, 0] / w_mm, 1 - v[:, 0] / w_mm)
    img_y = np.where(is_top, (1 - v[:, 1] / h_mm) * h_px, h_px + (1 - v[:, 1] / h_mm) * h_px)
    uv = np.column_stack([u, 1 - img_y / (2 * h_px)])
    fm.visual = trimesh.visual.TextureVisuals(uv=uv, material=trimesh.visual.material.PBRMaterial(baseColorTexture=atlas_j, metallicFactor=0.0, roughnessFactor=0.55, name="board"))
    scene = trimesh.Scene()
    scene.add_geometry(fm, node_name="faces")
    if sm is not None:
        sm.visual = trimesh.visual.TextureVisuals(material=trimesh.visual.material.PBRMaterial(baseColorFactor=list(color) + [255], metallicFactor=0.0, roughnessFactor=0.7, name="edge"))
        scene.add_geometry(sm, node_name="edges")
    # centre the board and convert mm -> m
    T = np.eye(4); T[:3, :3] *= 0.001; T[:3, 3] = [-w_mm / 2000, -h_mm / 2000, -THICK / 2000]
    scene.apply_transform(T)
    os.makedirs(os.path.dirname(out_glb), exist_ok=True)
    with open(out_glb, "wb") as f: f.write(scene.export(file_type="glb"))
    return {"size_mm": [round(w_mm, 1), round(h_mm, 1)], "board_color": "#%02x%02x%02x" % color, "pieces": len(polys), "note": note}

# ---------- kicad ----------
_kicad_help = {}
def kicad_flags(sub):
    if sub not in _kicad_help:
        rc, out = run(KICAD_CLI + ["pcb", "export", sub, "--help"], timeout=120); _kicad_help[sub] = out
    return _kicad_help[sub]

def kicad_gerbers(board, outdir):
    os.makedirs(outdir, exist_ok=True)
    rc, out = run(KICAD_CLI + ["pcb", "export", "gerbers", "-o", outdir + "/", "--layers", "F.Cu,B.Cu,F.Mask,B.Mask,F.SilkS,B.SilkS,Edge.Cuts", board], timeout=600)
    if rc != 0: raise RuntimeError("gerber export failed: " + out[-300:])
    run(KICAD_CLI + ["pcb", "export", "drill", "-o", outdir + "/", "--format", "excellon", board], timeout=300)
    return outdir

def kicad_glb(board, out_glb):
    help_ = kicad_flags("glb")
    want = ["--subst-models", "--include-tracks", "--include-pads", "--include-zones", "--include-silkscreen", "--include-soldermask", "--force"]
    flags = [f for f in want if f in help_]
    # export and compress inside the entry's _build folder; only the finished, compressed file lands in assets/models
    raw = os.path.join(os.path.dirname(board) if "_build" in board else os.path.join(os.path.dirname(os.path.dirname(out_glb)), "..", "..", "data", "hw"), "_raw_export.glb")
    raw = os.path.join(BUILD_DIR[0], "raw_export.glb") if BUILD_DIR[0] else raw
    rc, out = run(KICAD_CLI + ["pcb", "export", "glb", "-o", raw] + flags + [board], timeout=1200)
    if rc != 0 or not os.path.exists(raw): raise RuntimeError("glb export failed: " + out[-300:])
    tmp = raw + ".draco.glb"
    rc, out = run(node_bin("gltf-transform", "@gltf-transform/cli") + ["optimize", raw, tmp, "--compress", "draco", "--simplify", "false"], timeout=900)
    final = tmp if (rc == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 1000) else raw
    size = os.path.getsize(final)
    if size > FULL_GLB_MAX: raise RuntimeError(f"glb too large after compression ({size // 1024} KB)")
    os.makedirs(os.path.dirname(out_glb), exist_ok=True); shutil.copyfile(final, out_glb)
    return size

EAGLE_IMPORT_CODE = r"""
import pcbnew, sys
mgr = getattr(pcbnew, 'PCB_IO_MGR', None) or getattr(pcbnew, 'IO_MGR', None)
b = pcbnew.LoadBoard(sys.argv[1], mgr.EAGLE) if mgr is not None else pcbnew.LoadBoard(sys.argv[1])
# Eagle imports leave some items on undefined layers, which kicad-cli refuses to load. Removing them crashes the
# bindings, so park them on a comment layer that the 3D export ignores.
PARK = pcbnew.Cmts_User
def fix(it):
    try:
        if it.GetLayer() < 0 or it.GetLayer() == pcbnew.UNDEFINED_LAYER:
            it.SetLayer(PARK); return 1
    except Exception: pass
    return 0
def items(getter):
    try: return list(getter())
    except Exception: return []
moved = 0
for it in items(b.GetDrawings): moved += fix(it)
for it in items(b.GetTracks): moved += fix(it)
for z in items(b.Zones): moved += fix(z)
for fp in items(b.GetFootprints):
    for it in items(fp.GraphicalItems): moved += fix(it)
    for fld in items(getattr(fp, 'GetFields', lambda: [])): moved += fix(fld)
pcbnew.SaveBoard(sys.argv[2], b)
print('moved', moved)
"""

def eagle_to_kicad(brd, out_pcb):
    code = EAGLE_IMPORT_CODE
    rc, out = run(KICAD_PY + ["-c", code, brd, out_pcb], timeout=600)
    if rc != 0 or not os.path.exists(out_pcb): raise RuntimeError("eagle import failed: " + out[-300:])
    return out_pcb

# ---------- per entry ----------
def entry_path(eid):
    for p in glob.glob(os.path.join(ROOT, "_badges", "*", "*.md")):
        t = open(p, encoding="utf-8").read(200)
        if re.search(r"^id:\s*" + re.escape(eid) + r"\s*$", t, re.M): return p
    return None

def write_model(path, model):
    text = open(path, encoding="utf-8").read(); m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    fm = yaml.safe_load(m.group(1)) or {}; fm["model"] = model
    fm["last_modified_date"] = model["generated"]
    open(path, "w", encoding="utf-8").write("---\n" + yaml.dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---\n" + m.group(2))

def build_entry(eid, today, force=False, methods=("kicad", "gerber")):
    root = os.path.join(HW, eid)
    if not os.path.isdir(root): return {"status": "no_files"}
    path = entry_path(eid)
    if not path: return {"status": "no_entry"}
    ev, slug = os.path.basename(os.path.dirname(path)), os.path.basename(path)[:-3]
    out_glb = os.path.join(MODELS, ev, slug + ".glb")
    if os.path.exists(out_glb) and not force:
        fm_text = open(path, encoding="utf-8").read(3000)
        if os.path.relpath(out_glb, ROOT) in fm_text: return {"status": "exists"}
        os.remove(out_glb)  # orphan from an interrupted run: rebuild so the entry gets its model block
    build = os.path.join(root, "_build"); shutil.rmtree(build, ignore_errors=True); os.makedirs(build); BUILD_DIR[0] = build
    tried = []
    boards = kicad_boards(root)
    if not boards and "kicad" in methods:
        for brd in eagle_boards(root)[:1]:
            try: boards = [eagle_to_kicad(brd, os.path.join(build, "eagle_import.kicad_pcb"))]; tried.append("eagle->kicad ok")
            except Exception as e: tried.append(f"eagle: {str(e)[:120]}")
    gdirs = gerber_dirs(root)
    # prefer the gerber set whose folder name shares words with the entry slug (repos often hold several boards)
    words = set(w for w in re.split(r"[^a-z0-9]+", slug.lower()) if len(w) > 2)
    def affinity(d):
        name = set(re.split(r"[^a-z0-9]+", os.path.relpath(d, root).lower()))
        return -len(words & name)
    gdirs = sorted(gdirs, key=affinity)
    src = None; method = None; info = {}
    if boards and "kicad" in methods:
        board = boards[0]; src = os.path.relpath(board, root).replace("_build/eagle_import.kicad_pcb", os.path.basename(eagle_boards(root)[0]) if eagle_boards(root) else "board")
        try:
            size = kicad_glb(board, out_glb); method = "kicad"; info = {"bytes": size}
        except Exception as e:
            tried.append(f"kicad glb: {str(e)[:160]}")
            m_layer = re.search(r"undefined layers \(([^)]+)\)", str(e))
            if m_layer:
                # KiCad refuses boards that reference a layer missing from their layer table (typically "Rescue").
                # Re-point those items at a comment layer in a copy of the file and export that.
                try:
                    cleaned = os.path.join(build, "cleaned.kicad_pcb"); name = m_layer.group(1).strip()
                    text = open(board, encoding="utf-8", errors="ignore").read()
                    text = re.sub(r'\(layer "' + re.escape(name) + r'"\)', '(layer "Cmts.User")', text)
                    text = re.sub(r'\(layer ' + re.escape(name) + r'\)', '(layer Cmts.User)', text)
                    text = re.sub(r'"' + re.escape(name) + r'"', '"Cmts.User"', text)
                    open(cleaned, "w", encoding="utf-8").write(text)
                    size = kicad_glb(cleaned, out_glb); method = "kicad"; info = {"bytes": size}; tried.append(f"retried with layer {name} moved to Cmts.User")
                except Exception as e2: tried.append(f"cleanup retry: {str(e2)[:120]}")
        if not method:
            try: gdirs = [kicad_gerbers(board, os.path.join(build, "gerbers"))] + gdirs
            except Exception as e: tried.append(f"kicad gerbers: {str(e)[:160]}")
    if not method and "gerber" in methods:
        for gd in gdirs[:3]:
            try:
                rend = os.path.join(build, "render_" + str(abs(hash(gd)) % 10000)); os.makedirs(rend, exist_ok=True)
                top, bot = tracespace(gd, rend)
                info = build_slab(top, bot, out_glb); method = "gerber"
                src = src or os.path.relpath(gd, root).replace("_unz", ".zip")
                break
            except Exception as e: tried.append(f"gerber {os.path.basename(gd)}: {str(e)[:160]}")
    if not os.environ.get("MODEL_DEBUG"): shutil.rmtree(build, ignore_errors=True)
    if not method: return {"status": "failed", "tried": tried}
    model = OrderedDict([("file", os.path.relpath(out_glb, ROOT)), ("method", method), ("source_file", src or ""), ("generated", today), ("bytes", os.path.getsize(out_glb))])
    if info.get("size_mm"): model["size_mm"] = info["size_mm"]
    if info.get("note"): model["note"] = info["note"]
    write_model(path, dict(model))
    return {"status": "ok", "method": method, "bytes": model["bytes"], "tried": tried, "src": src}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--id"); ap.add_argument("--all", action="store_true"); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--force", action="store_true"); ap.add_argument("--methods", default="kicad,gerber"); ap.add_argument("--today", default=datetime.date.today().isoformat())
    ap.add_argument("--shard", default="", help="K/N: only process ids whose crc32 %% N == K; report goes to models_report.shardK.json")
    a = ap.parse_args()
    import zlib
    manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    shard_k, shard_n = (int(x) for x in a.shard.split("/")) if a.shard else (0, 1)
    report_path = REPORT.replace(".json", f".shard{shard_k}.json") if a.shard else REPORT
    done = {}
    for rp in glob.glob(os.path.join(ROOT, "data", "models_report*.json")):
        try: done.update({i: r for i, r in json.load(open(rp)).items() if r.get("status") in ("ok", "failed")})
        except Exception: pass
    report = json.load(open(report_path)) if os.path.exists(report_path) else {}
    ids = [a.id] if a.id else [k for k, v in manifest.items() if v.get("ok")]
    n = 0
    for eid in ids:
        if a.shard and zlib.crc32(eid.encode()) % shard_n != shard_k: continue
        if not a.id and eid in done and not a.force: continue
        try: r = build_entry(eid, a.today, force=a.force, methods=tuple(a.methods.split(",")))
        except Exception as e: r = {"status": "error", "error": str(e)[:200]}
        report[eid] = r; json.dump(report, open(report_path, "w"), indent=1)
        log(f"{r.get('status'):7s} {eid} {r.get('method','')} {r.get('bytes','')} {('| ' + '; '.join(r.get('tried', []))) if r.get('tried') else ''}"[:300])
        n += 1
        if a.limit and n >= a.limit: break
    ok = sum(1 for v in report.values() if v.get("status") == "ok"); log(f"report: {len(report)} tried, {ok} models")

if __name__ == "__main__":
    main()
