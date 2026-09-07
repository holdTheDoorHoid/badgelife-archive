---
title: xHain hackspace logo SAOAO
id: supercon-2024-xhain-hackspace-logo-saoao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A tiny simple add-on shaped like the xHain hackspace (Berlin) logo, with a single LED, made as part of davedarko's "YoDawgSAO" collection for the Hackaday Supercon 2024 add-on contest.
functions: 'Passive: a single LED lit by power from the host badge''s simple-add-on header. No microcontroller, no logic.'
look:
  colors: []
  shape: logo
  themes:
  - logo
  - hardware tool
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single through-hole/discrete LED (schematic ref D1); no specific color documented by the maker.
  display: none
  connectivity:
  - none
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/xHainLogo
  firmware_url: null
  eda_tool: KiCad
  license: MIT
  notes: "Part of the davedarko/YoDawgSAO repo, which holds KiCad source, fabrication outputs (Gerbers/BOM/CPL in production/xHainLogo.zip) and reference art (vector logo + silkscreen) for several small add-on shapes sharing one design: 19mm x 19mm, connected via a 1.27mm-pitch 3-pin GND-VCC-GND header rather than a standard SAO connector."
links:
- label: github.com/davedarko/YoDawgSAO/tree/master/badges/xHainLogo
  url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/xHainLogo
  kind: repo
- label: davedarko/YoDawgSAO (repo root README)
  url: https://github.com/davedarko/YoDawgSAO
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/xHainLogo
  title: xHain hackspace logo SAOAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''supercon-2024''.'
- kind: url
  url: https://github.com/davedarko/YoDawgSAO
  title: davedarko/YoDawgSAO
  accessed: '2026-09-07'
  note: Repo root README explains the project's origin (Hackaday Supercon 2024 add-on contest, as a "not smart, no I2C" alternative), the 19mm x 19mm size constraint, and the 1.27mm GND-VCC-GND header design choice. Also confirms MIT license and lists sibling variants (IronMan, hackadayLogo, super_computer_custer_0805, dawg).
- kind: url
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/main/badges/xHainLogo/xHainLogo.kicad_sch
  title: xHainLogo.kicad_sch (raw)
  accessed: '2026-09-07'
  note: Schematic shows one Device:LED (D1) and one Connector:Conn_01x03_Socket wired GND-VCC-GND; no MCU present.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three cited sources (repo file listing for badges/xHainLogo, the YoDawgSAO root README, and the raw xHainLogo.kicad_sch) plus the repo API for license and sibling folder names. Every non-empty field and sentence in this entry is supported by the maker''s own repo: xHainLogo folder contains xHainLogo.kicad_sch/.kicad_pcb/.kicad_pro plus a production/xHainLogo.zip and a reference/ folder; the schematic has exactly one Device:LED (ref D1) and one Connector:Conn_01x03_Socket (ref J1) wired to VCC/GND power symbols, with no MCU symbol anywhere in the file; the README confirms the Supercon 2024 add-on contest origin, the "not smart, no I2C" framing, the 19mm x 19mm size constraint, and the 1.27mm GND-VCC-GND header design ("a pain to solder... but it''s the standard now"); the GitHub API confirms an MIT license and sibling badge folders IronMan, hackadayLogo, super_computer_custer_0805 (plus a repo-root dawg/ folder for the Yo Dawg baseplate itself). No maker photo of the assembled/populated xHainLogo board was found in the repo, so images/colors/LED-color remain empty rather than guessed. Price, quantity made, and distribution method are not stated anywhere in the sources and remain empty. The connector is a non-standard "simple add-on" 1.27mm 3-pin GND-VCC-GND header (not a 4-pin SAO v1 or 6-pin SAO v1.69bis/v2 header), so tech.sao_version is correctly left null rather than forced into the existing vocabulary. No unsupported claims or contradicted values were found; nothing needed to be blanked, corrected, or removed. Note: a separate sibling entry (_badges/supercon-2024/yo-dawg-saoao-xhain-logo.md) covers what appears to be the same physical item from a different source angle (Hackaday.io project log, giving distribution/quantity context this entry lacks) — left untouched per the one-entry-per-task rule, but a future pass may want to reconcile or merge the two.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/xhain-hackspace-logo-saoao/
---

davedarko's "YoDawgSAO" is a small family of deliberately simple add-ons made for the Hackaday Supercon 2024 badge-add-on contest. Where the contest pushed toward smart, I2C-connected add-ons, davedarko built a set of passive boards for people who "just want to do a small meme or have some RGB LEDs blinking": each board is constrained to 19mm x 19mm and connects to the host badge through a 1.27mm-pitch 3-pin GND-VCC-GND header rather than a full SAO connector.

The xHain hackspace logo variant is one shape in that family, its outline cut to match the logo of xHain, a hackspace in Berlin. Its schematic shows nothing more than a single LED wired straight across power and ground, so it lights whenever the host badge powers the add-on header; there is no microcontroller or logic on board. The repository holds the full KiCad source (schematic, PCB, and fabrication output as a zipped Gerber/BOM/CPL package) alongside vector artwork for the logo shape and its silkscreen, published under the MIT license, but no photos of an assembled unit.

The same repo contains sibling shapes on the same 19mm add-on platform — an Iron Man logo, the Hackaday logo, and a "super computer" 0805-style piece — plus the "Yo Dawg" board the collection is named after, all sharing the same simple 3-pin power-only connector.
