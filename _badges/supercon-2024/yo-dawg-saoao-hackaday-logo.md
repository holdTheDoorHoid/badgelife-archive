---
title: Hackaday Logo SAOAO
id: supercon-2024-yo-dawg-saoao-hackaday-logo
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: supercon-2024
year: 2024
series: Yo Dawg SAOAO
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: A 19x19 mm Hackaday "jolly wrencher" logo Simple Add-on Add-on (SAOAO) for the Yo Dawg SAO baseplate, made for the Supercon 2024 SAO contest; one of 100 boards ordered in this variant.
functions: Single LED lights up the Hackaday jolly-wrencher logo cutout/silkscreen when powered through the SAOAO header.
look:
  colors: []
  shape: rectangle
  themes:
  - logo
  - hardware tool
  - minimalist
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single through-hole/SMD LED (schematic ref D1); not addressable.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '100'
  availability: unknown
  distribution:
  - free_drop
  where: Handed out at Supercon 2024 alongside the other Yo Dawg SAOAO boards; davedarko brought "100 SAOs and 200 SAOAOs" to the con, including 100 of this hackaday-logo variant.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/davedarko/YoDawgSAO/tree/main/badges/hackadayLogo
  firmware_url: null
  eda_tool: KiCad
  gerbers_url: https://github.com/davedarko/YoDawgSAO/tree/main/badges/hackadayLogo/production
  license: MIT
  notes: KiCad source (schematic, PCB, and JLCPCB fabrication-toolkit production files) lives in the badges/hackadayLogo folder of the YoDawgSAO repo, alongside sibling SAOAO designs (Iron Man, xHain logo, an LED super-cluster).
links:
- label: github.com/davedarko/YoDawgSAO
  url: https://github.com/davedarko/YoDawgSAO
  kind: repo
- label: hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  kind: hackaday
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
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/main/README.md
  title: YoDawgSAO README
  accessed: '2026-09-07'
  note: 'Design brief: 19x19mm SAOAO concept for the Supercon 2024 add-on contest, 1.27mm GND-VCC-GND 3-pin header, MIT license.'
- kind: url
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  title: 'Yo Dawg SAO -- introducing SAOAO! - Hackaday.io'
  accessed: '2026-09-07'
  note: Team (davedarko, Marc MERLIN), Supercon 2024 contest entry, and mention of "100 hackaday logo boards" ordered plus "100 SAOs and 200 SAOAOs" brought to Supercon.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/main/badges/hackadayLogo/hackadayLogo.kicad_sch
  title: hackadayLogo.kicad_sch
  accessed: '2026-09-07'
  note: Schematic confirms a single discrete LED (D1) and the standard 3-pin SAOAO connector; no MCU present.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No photo of the assembled/soldered board was found anywhere in the repo or on the Hackaday.io project page -- only KiCad source files and a reference SVG of the Hackaday jolly-wrencher artwork (the design source, not a picture of the item), so images is left empty. Price and current availability were not stated anywhere; these were free giveaways at Supercon rather than a sold item, so price/price_usd are left blank and availability is unknown post-event. The repo folder for this variant is named "hackadayLogo" but the board is officially called a "SAOAO" (Simple Add-on Add-on); series field added since the repo documents several sibling SAOAO designs (Iron Man, xHain logo, LED super-cluster) under the same Yo Dawg concept.'
last_modified_date: '2026-09-07'
---

The Hackaday Logo SAOAO is a tiny "add-on for your add-on" board that plugs into the Yo Dawg SAO baseplate, one of several SAOAO designs davedarko (with Marc MERLIN) created for the Hackaday Supercon 2024 SAO contest. The whole SAOAO concept keeps to a strict 19mm x 19mm footprint with a simplified 3-pin (GND-VCC-GND) 1.27mm header, deliberately skipping I2C so makers could slap a small meme or a blinking LED onto their contest entry without it counting as a full standalone add-on. This particular variant carries the Hackaday "jolly wrencher" logo with a single LED behind it.

Davedarko had 100 of the hackaday-logo boards fabricated (alongside 100 red-ENIG Iron Man boards, 100 plain SAOAO baseplates, and a run of self-blinking "super cluster" LED boards) and brought roughly 200 SAOAOs total to Supercon 2024 to hand out. Hardware is open source under the MIT license, with KiCad schematic, PCB, and JLCPCB-ready production files in the `badges/hackadayLogo` folder of the YoDawgSAO GitHub repo.

## Make your own

The `badges/hackadayLogo` folder in [davedarko/YoDawgSAO](https://github.com/davedarko/YoDawgSAO/tree/main/badges/hackadayLogo) has the full KiCad project (schematic, PCB, and a `production/` folder with a ready-to-order `hackadayLogo.zip` fabrication package plus an IPC netlist) needed to order your own boards from a fab like JLCPCB.
