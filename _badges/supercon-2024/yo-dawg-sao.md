---
title: Yo Dawg SAO
id: supercon-2024-yo-dawg-sao
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
summary: A Supercon 2024 add-on-contest SAO baseplate with room for three tiny 19x19 mm 'Simple Add-on Add-ons' (SAOAOs) on 1.27 mm GND-VCC-GND 3-pin headers, riffing on the 'Yo Dawg, I heard you like add-ons on your badges' meme; davedarko brought about 100 baseplates to Supercon.
functions: Baseplate for mounting up to three tiny SAOAO modules; individual SAOAO modules are typically simple LED add-ons (blinky/meme boards), with no I2C requirement.
look:
  colors: []
  shape: null
  themes:
  - meme
  - pop culture
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: davedarko brought about 100 Yo Dawg SAO baseplates and 200 SAOAOs to Supercon 2024
  availability: free
  distribution:
  - contest
  - free_drop
  where: Handed out / built at Hackaday Supercon 2024 as part of the SAO add-on contest; open design so others can also fab their own.
make_your_own:
  open_source: true
  hardware_url: https://github.com/davedarko/YoDawgSAO
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
- label: hackaday.com/2024/10/01/2024-sao-contest-weve-got-saos-for-your-saos
  url: https://hackaday.com/2024/10/01/2024-sao-contest-weve-got-saos-for-your-saos/
  kind: article
  archived: https://web.archive.org/web/20260307052723/https://hackaday.com/2024/10/01/2024-sao-contest-weve-got-saos-for-your-saos/
- label: marc.merlins.org/perso/electronics/post_2024-11-02_Pasadena-Hackaday-Supercon-2024-Yo-Dawg-Micro-SAO-and-SMD-Soldering.html
  url: https://marc.merlins.org/perso/electronics/post_2024-11-02_Pasadena-Hackaday-Supercon-2024-Yo-Dawg-Micro-SAO-and-SMD-Soldering.html
  kind: website
images:
- file: assets/images/badges/supercon-2024/yo-dawg-sao/873acad980.png
  source: https://hackaday.com/2024/10/01/2024-sao-contest-weve-got-saos-for-your-saos/
  credit: davedarko / Hackaday
  caption: Supercon Add-On Add-Ons (SAOAOs) in production
  archived: https://web.archive.org/web/20260307052723/https://hackaday.com/2024/10/01/2024-sao-contest-weve-got-saos-for-your-saos/
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
  url: https://github.com/davedarko/YoDawgSAO
  title: davedarko/YoDawgSAO - Simple Add-on Add-ons
  accessed: '2026-09-07'
  note: Confirmed dimensions (19x19mm), 1.27mm GND-VCC-GND header, MIT-licensed KiCad hardware files.
- kind: url
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  title: Yo Dawg SAO - introducing SAOAO
  accessed: '2026-09-07'
  note: 'Maker project page: team includes Marc MERLIN, pinout description (VCC middle, GND outer pins for mirror-protection), 100 baseplates / 200 SAOAOs brought to Supercon, PCBs ordered from JLCPCB, multiple SAOAO variants (Iron Man, Hackaday logo) made by contributors.'
  archived: https://web.archive.org/web/20260219013204/https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
- kind: url
  url: https://hackaday.com/2024/10/01/2024-sao-contest-weve-got-saos-for-your-saos/
  title: '2024 SAO Contest: We''ve Got SAOs For Your SAOs'
  accessed: '2026-09-07'
  note: Hackaday coverage of the 2024 Supercon SAO contest confirming quantities brought and that the standard is open for anyone to fabricate their own; source of the production photo used here.
  archived: https://web.archive.org/web/20260307052723/https://hackaday.com/2024/10/01/2024-sao-contest-weve-got-saos-for-your-saos/
- kind: url
  url: https://marc.merlins.org/perso/electronics/post_2024-11-02_Pasadena-Hackaday-Supercon-2024-Yo-Dawg-Micro-SAO-and-SMD-Soldering.html
  title: 'Pasadena Hackaday Supercon 2024: Yo Dawg Micro SAO and SMD Soldering'
  accessed: '2026-09-07'
  note: A builder's account of soldering a Yo Dawg Micro SAO/SAOAO by hand; confirms the tiny modules were fiddly SMD work and lacked clear polarity marking on some units.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price is not stated anywhere found - these were given out/self-assembled at Supercon rather than sold, so get_one.price is left empty and availability set to free. No LED count/type or specific SAOAO circuit details found since SAOAO is an open standard for third-party add-on modules rather than a fixed product; tech.leds left null accordingly. No dedicated storefront exists.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2024/yo-dawg-sao.glb
  method: kicad
  source_file: dawg/dawg.kicad_pcb
  generated: '2026-09-10'
  bytes: 112956
---

The Yo Dawg SAO is a baseplate that davedarko designed for Hackaday Supercon 2024's SAO add-on contest, built around a joke: "Yo Dawg, I heard you like add-ons on your badges, so I put an add-on on your add-on." Rather than being a single fixed circuit, it defines the "SAOAO" (Simple Add-on Add-on) standard - a tiny 19x19 mm module format on a 1.27 mm 3-pin GND-VCC-GND header, with VCC in the middle so the header can't be plugged in backwards. The baseplate itself holds up to three of these micro add-ons at once, and the design (credited to davedarko with Marc Merlin as a collaborator) was shared openly enough that other attendees produced their own SAOAO variants, including an Iron Man design and a Hackaday-logo board.

davedarko brought roughly 100 Yo Dawg SAO baseplates and 200 SAOAOs to Supercon 2024, ordering the PCB panels from JLCPCB and giving them out to badge-hacking attendees rather than selling them. Because the pins on the tiny SAOAO modules were not always clearly marked for polarity, several builders (including at least one who wrote up the soldering experience) had to test boards and LEDs by hand to determine orientation before assembling them - a fiddly bit of SMD work that became part of the badge's charm at the con.

## Make your own

Hardware files (KiCad, MIT-licensed) are published at github.com/davedarko/YoDawgSAO, including the baseplate and the SAOAO footprint/module reference design, so anyone can fabricate their own baseplates or design compatible SAOAO add-ons using the same 19x19 mm / 1.27 mm 3-pin header standard.
