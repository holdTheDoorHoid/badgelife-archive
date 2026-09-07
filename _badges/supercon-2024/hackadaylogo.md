---
title: hackadayLogo
id: supercon-2024-hackadaylogo
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: A tiny "SAOAO" (SAO for an SAO) carrying Hackaday's Jolly Wrencher skull-and-wrenches
  mascot, part of davedarko's YoDawgSAO / "Yo Dawg SAO" project for the 2024 Hackaday
  Supercon SAO contest.
functions: Two RGB LEDs light up when the SAOAO is plugged into a Yo Dawg SAO baseplate
  (or otherwise powered), fading through colors on their own with no driver chip or
  microcontroller on board.
look:
  colors:
  - black
  - yellow
  shape: rectangle
  themes:
  - skull
  - logo
  - hardware tool
  - meme
  form_factor: pcb sao
tech:
  mcu: none
  leds:
    count: 2
    type: RGB
    note: Self-fading (color-cycling) RGB LEDs; the schematic shows no separate driver
      IC, matching the project notes that these boards "will receive the RGB LED
      faders."
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '100 (ordered for Supercon 8, 2024)'
  availability: unknown
  distribution:
  - kit
  where: Handed out as build-your-own boards at Hackaday Supercon 8 (2024) as part
    of the SAOAO / Yo Dawg SAO project.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/hackadayLogo
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/YoDawgSAO/tree/master/badges/hackadayLogo
  url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/hackadayLogo
  kind: repo
- label: 'Yo Dawg SAO - introducing SAOAO (hackaday.io)'
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  kind: hackaday
- label: '"2024 SAO Contest: We''ve Got SAOs For Your SAOs" (Hackaday)'
  url: https://hackaday.com/2024/10/01/2024-sao-contest-weve-got-saos-for-your-saos/
  kind: article
images:
- file: assets/images/badges/supercon-2024/hackadaylogo/9c82b683d8.jpg
  source: "https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao"
  credit: "davedarko / hackaday.io"
  caption: "hackadayLogo SAOAO (Jolly Wrencher skull-and-wrenches artwork) mounted on a badge, lit from below"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/hackadayLogo
  title: hackadayLogo
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''supercon-2024''.'
- kind: url
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  title: Yo Dawg SAO - introducing SAOAO
  accessed: '2026-09-07'
  note: Maker's own project page; confirms the SAOAO standard (19x19mm, 1.27mm 3-pin
    GND-VCC-GND header), that davedarko ordered "100 hackaday logo boards" among
    the initial production run for Supercon 8 (2024), and that these boards "will
    receive the RGB LED faders."
- kind: url
  url: https://hackaday.com/2024/10/01/2024-sao-contest-weve-got-saos-for-your-saos/
  title: '2024 SAO Contest: We''ve Got SAOs For Your SAOs'
  accessed: '2026-09-07'
  note: Hackaday.com writeup of the SAOAO project by davedarko for the 2024 Supercon
    SAO contest; corroborates specs and quantities.
- kind: url
  url: https://github.com/davedarko/YoDawgSAO/blob/main/badges/hackadayLogo/hackadayLogo.kicad_sch
  title: hackadayLogo.kicad_sch
  accessed: '2026-09-07'
  note: Schematic shows a 3-pin GND-VCC-GND connector and two generic "LED" symbols,
    no MCU or driver chip.
- kind: url
  url: https://cdn.hackaday.io/images/1360201727734239235.jpg
  title: hackadayLogo SAOAO photo
  accessed: '2026-09-07'
  note: Photo from the maker's hackaday.io project gallery, used for the saved image.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: This is a "SAOAO" (an SAO-sized add-on for an SAO baseplate, not a stand-alone
    badge or a normal SAO), part of davedarko's YoDawgSAO / "Yo Dawg SAO" standard
    made for the Hackaday Supercon 8 (2024) SAO contest. Event corrected from generic
    "other" to supercon-2024 based on the maker's own hackaday.io project page and
    the matching Hackaday.com article. Could not find a specific LED part number,
    exact price (these appear to have been given out to be self-assembled rather
    than sold), or a photo of the bare unpopulated board. Marc Merlin is credited
    as a collaborator on the broader SAOAO project on hackaday.io, but nothing found
    ties him specifically to the hackadayLogo variant, so only davedarko is listed
    as maker.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/hackadaylogo/
---

The hackadayLogo board is one of several small add-ons davedarko designed for his "Yo Dawg SAO" project, introduced for the 2024 Hackaday Supercon SAO contest. The project's joke is right there in the name: it is an "SAOAO," a Simple Add-On Add-On that plugs into its own miniature baseplate (the "Yo Dawg SAO"), which in turn plugs into a badge's normal SAO header — badges for your badges for your badges. Every SAOAO shares a tiny 19mm x 19mm footprint and a 1.27mm three-pin GND-VCC-GND header designed so the board can't be plugged in backwards.

This particular variant carries Hackaday's own mascot, the "Jolly Wrencher" skull-and-crossed-wrenches logo, printed on a black board. It carries two RGB LEDs that fade through colors on their own once powered, with no microcontroller or driver chip on the board — the schematic is just the connector and two LEDs. davedarko ordered 100 of these hackaday logo boards alongside 100 SAOAO baseplates and 100 "Iron Man" boards for Supercon 8, where attendees built and swapped them as part of the show's badge-hacking scene.

## Make your own

KiCad source files (schematic, PCB, and the JLCPCB "fabrication toolkit" production files) are published in the YoDawgSAO GitHub repository, alongside a reference SVG of the Jolly Wrencher artwork used for the silkscreen/soldermask design.
