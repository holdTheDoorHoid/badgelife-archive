---
title: xHain Logo SAOAO
id: supercon-2024-yo-dawg-saoao-xhain-logo
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: A 19x19 mm Simple Add-on Add-on carrying the logo of the xHain hackspace (davedarko's favorite hackspace) for the Yo Dawg SAO baseplate; KiCad files are in the repo's badges/xHainLogo folder.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - logo
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - free_drop
  where: Hand-soldered by davedarko and brought to Supercon 2024 for people to trade onto their Yo Dawg SAO baseplate; not sold.
make_your_own:
  open_source: true
  hardware_url: https://github.com/davedarko/YoDawgSAO/tree/main/badges/xHainLogo
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/YoDawgSAO
  url: https://github.com/davedarko/YoDawgSAO
  kind: repo
- label: hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  kind: hackaday
  archived: https://web.archive.org/web/20260219013204/https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/YoDawgSAO
  title: davedarko/YoDawgSAO - Simple Add-on Add-ons
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/davedarko/YoDawgSAO/tree/main/badges/xHainLogo
  title: badges/xHainLogo folder in davedarko/YoDawgSAO
  accessed: '2026-09-07'
  note: Confirms the xHainLogo SAOAO has its own KiCad PCB, production Gerber zip, and reference SVG artwork (xHainLogo.svg, silkscreen and soldermask-stop variants) in the repo; no photo of the assembled board is present.
- kind: url
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  title: Yo Dawg SAO - introducing SAOAO (Hackaday.io project 198060)
  accessed: '2026-09-07'
  note: 'Project description, dimensions/pinout, and a 09/30/2024 log entry: "100 yo-dawg baseplates ... 100 iron man add-ons ... and some with the logo of my favorite hackspace on it" and a 09/25/2024 log stating "I''m bringing 100 SAOs and 200 SAOAOs to supercon."'
  archived: https://web.archive.org/web/20260219013204/https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The Hackaday.io project page and repo confirm the xHain-logo variant exists among the SAOAO batch davedarko brought to Supercon 8 (2024), but neither source gives it a named quantity the way the Iron Man and Hackaday-logo variants got ("100" each) — the log only says "some with the logo of my favorite hackspace on it," so quantity is left blank rather than guessed. No LED/chip is mentioned for this specific variant (only the Iron Man and Hackaday-logo boards are described as getting RGB LEDs/faders), so tech fields are set to none/null. No photo of the assembled xHainLogo board was found — the repo's xHainLogo.svg/xHainLogoSilk.svg/xHainLogoStop.svg are vector artwork sources for the PCB, not photos, and the project's cover photo (showing Super Cluster, Iron Man, and a skull-and-wrenches badge) does not include the xHain logo design, so no image was saved. PCB color/finish for this specific variant is not stated (only the Iron Man boards are noted as ordered in red with ENIG), so
    look.colors is left empty.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2024/yo-dawg-saoao-xhain-logo.glb
  method: kicad
  source_file: badges/xHainLogo/xHainLogo.kicad_pcb
  generated: '2026-09-10'
  bytes: 30192
---

This is one of the SAOAO ("Simple Add-on Add-on") designs davedarko produced alongside the Yo Dawg SAO baseplate for Hackaday Supercon 8's SAO contest in 2024. SAOAOs are 19x19 mm mini-boards with a mirroring-protected 3-pin (GND-VCC-GND) 1.27 mm header, meant to plug into a small carrier baseplate that itself is a full-size Simple Add-On — "badges for your badges for your badges," in the maker's words, inspired partly by the SAINTCON-style minibadge standard.

This variant carries the logo of xHain, davedarko's favorite hackerspace, in place of the Iron Man, Hackaday-logo, or "Super Cluster" artwork used on the other SAOAOs from the same batch. According to the maker's Hackaday.io project log, the PCBs for the batch (100 Yo Dawg baseplates, 100 Iron Man add-ons, a run of Hackaday-logo boards, and "some with the logo of my favorite hackspace") arrived together in late September 2024, and davedarko brought roughly 100 SAOs and 200 SAOAOs to Supercon for attendees to build and trade. No exact production count or LED/chip detail specific to the xHain design was stated in the sources found.

## Make your own

KiCad source (`xHainLogo.kicad_pcb`), reference SVG artwork (front, silkscreen, and soldermask-stop layers), and a production Gerber/BOM zip are published under `badges/xHainLogo/` in the [YoDawgSAO GitHub repo](https://github.com/davedarko/YoDawgSAO/tree/main/badges/xHainLogo), alongside the general SAOAO footprint file (`squareSAOAO.kicad_mod`) used by every design in the project.
