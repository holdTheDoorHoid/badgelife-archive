---
title: Flandre Scarlet 3D-Printed Wings hexpansion
id: emf-camp-2024-flandre-scarlet-3d-printed-wings-hexpansion
layout: badge
parent: EMF Camp 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: emf-camp-2024
year: 2024
makers:
- name: DanNixon
  url: https://github.com/DanNixon
summary: A 3D-printed hexpansion for the EMF Camp 2024 Tildagon badge shaped like the wings of Touhou character Flandre Scarlet.
functions: Purely decorative; clips into a Tildagon hexpansion slot with no electronics.
look:
  colors: []
  shape: wings
  themes:
  - anime
  - pop culture
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: available
  distribution: []
  where: Not sold; download the files and 3D-print your own hexpansion shell.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/DanNixon/hexpansions/tree/main/flan-wings-3dprinted
  firmware_url: null
  eda_tool: null
links:
- label: github.com/DanNixon/hexpansions/tree/main/flan-wings-3dprinted
  url: https://github.com/DanNixon/hexpansions/tree/main/flan-wings-3dprinted
  kind: repo
images: []
contact: {}
notes:
- One of several open-source Tildagon hexpansions in DanNixon's public repo; a novelty 3D-printed wing add-on. Found by the event-year sweep, task emf-addons.
- The sweep's snippet is confirmed by the repo itself; the entry is not a rumor.
status: released
sources:
- kind: url
  url: https://github.com/DanNixon/hexpansions/tree/main/flan-wings-3dprinted
  title: Flandre Scarlet 3D-Printed Wings hexpansion
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''EMF Camp 2024''.'
- kind: url
  url: https://raw.githubusercontent.com/DanNixon/hexpansions/main/README.md
  title: DanNixon/hexpansions README
  accessed: '2026-09-10'
  note: Confirms this is one of several Tildagon hexpansion designs (alongside Le Carnard de Bleu, Maker Space badge, Rabbit) in the same repo, for the EMF Camp 2024 Tildagon badge.
- kind: url
  url: https://api.github.com/repos/DanNixon/hexpansions/contents/flan-wings-3dprinted
  title: flan-wings-3dprinted directory listing
  accessed: '2026-09-10'
  note: Folder contains only design files (outline.dxf, volume.scad, volume.stl) — no electronics, no README, no photos.
- kind: url
  url: https://api.github.com/repos/DanNixon/hexpansions/commits?path=flan-wings-3dprinted
  title: Commit history for flan-wings-3dprinted
  accessed: '2026-09-10'
  note: Commits dated May 2024, consistent with EMF Camp 2024 (held that June).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: "Confirmed real via the maker's own GitHub repo (not just a search snippet) — folder contains outline.dxf, volume.scad, and volume.stl, with a May 2024 commit fixing a rotation issue. No README, no photos, and no pricing/quantity/distribution info exist because this was never sold: it is a self-printable STL/DXF design, not a manufactured item. Left tech.leds, price, and quantity empty since nothing supports a value. Shape/theme tags (wings, anime) inferred from the name (Flandre Scarlet is a Touhou character) since no image could be found to confirm colors or exact form."
last_modified_date: '2026-09-10'
---

DanNixon's Flandre Scarlet 3D-Printed Wings is a hexpansion — a plug-in expansion module for the Tildagon badge issued at EMF Camp 2024 — shaped as a pair of wings referencing Flandre Scarlet, a character from the Touhou Project game series. It is one of four Tildagon hexpansion designs DanNixon published in a single GitHub repository alongside "Le Carnard de Bleu," a "Maker Space badge," and a "Rabbit" hexpansion.

Unlike most entries in this archive, this is not a manufactured or sold item: the repository holds only the design files needed to make one yourself (an `outline.dxf`, an OpenSCAD source `volume.scad`, and a compiled `volume.stl`), with no electronics, no listed price, and no storefront. A May 2024 commit rotating the hexpansion adapter by 30 degrees to fix a fitment issue is the only development history visible, and it lines up with EMF Camp 2024's June 2024 dates. No photos of a printed unit were found, so its exact size and color are unconfirmed.

## Make your own

The files are published openly at https://github.com/DanNixon/hexpansions/tree/main/flan-wings-3dprinted. `outline.dxf` and `volume.scad` define the wing geometry (editable in OpenSCAD), and `volume.stl` is a ready-to-slice mesh; combined with a standard Tildagon hexpansion PCB adapter, printing `volume.stl` reproduces the part.
