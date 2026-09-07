---
title: Iron Man SAOAO
id: supercon-2024-yo-dawg-saoao-iron-man
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: supercon-2024
year: 2024
series: Yo Dawg SAO
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
summary: A 19x19 mm Iron Man themed Simple Add-on Add-on (red PCB with ENIG finish and a backlit gold Iron Man helmet mask) that plugs into the Yo Dawg SAO baseplate via a 1.27 mm 3-pin header; KiCad files live in the repo's badges/IronMan folder.
functions: 'Backlit LED graphic (Iron Man helmet face lights up amber/gold); nests onto the Yo Dawg SAO mainboard alongside other SAOAOs (hackaday logo, skull-and-wrenches, LED matrix, etc).'
look:
  colors:
  - red
  - gold
  shape: mask
  themes:
  - pop culture
  - movie
  - meme
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: '100'
  availability: sold_out
  distribution:
  - free_drop
  - swap
  where: Given away/traded at Supercon 2024 (Supercon 8) by davedarko; one was donated to Marc Merlin, who documented soldering it.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/YoDawgSAO/tree/master/badges/IronMan
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/YoDawgSAO
  url: https://github.com/davedarko/YoDawgSAO
  kind: repo
- label: hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  kind: hackaday
- label: "Marc Merlin: Pasadena Hackaday Supercon 2024 Yo Dawg Micro SAO and SMD Soldering"
  url: https://marc.merlins.org/perso/electronics/post_2024-11-02_Pasadena-Hackaday-Supercon-2024-Yo-Dawg-Micro-SAO-and-SMD-Soldering.html
  kind: article
images:
- file: assets/images/badges/supercon-2024/yo-dawg-saoao-iron-man/81423ef002.jpg
  source: "https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao"
  credit: "davedarko"
  caption: "Assembled Iron Man SAOAO lit up, alongside other SAOAO designs from the Yo Dawg SAO project"
- file: assets/images/badges/supercon-2024/yo-dawg-saoao-iron-man/79e728088a.png
  source: "https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao"
  credit: "davedarko"
  caption: "Bare red ENIG Iron Man SAOAO PCBs fresh from the panel, alongside other Yo Dawg SAOAO designs"
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
  url: https://hackaday.io/project/198060-yo-dawg-sao-introducing-saoao
  title: "Yo Dawg SAO - introducing SAOAO"
  accessed: '2026-09-07'
  note: "Project logs confirm davedarko ordered 100 red Iron Man SAOAO boards with ENIG finish from JLCPCB for Supercon 2024 (Supercon 8), alongside 100 Yo Dawg SAO baseplates and 100 hackaday-logo SAOAOs; brought 100 SAOs and 200 SAOAOs total to give away/trade at the con. Source of both saved images."
- kind: url
  url: https://raw.githubusercontent.com/davedarko/YoDawgSAO/master/README.md
  title: "YoDawgSAO README"
  accessed: '2026-09-07'
  note: "Confirms 19x19mm size, 1.27mm 3-pin GND-VCC-GND header standard, and that the project was made for the 2024 Hackaday Supercon add-on contest."
- kind: url
  url: https://api.github.com/repos/davedarko/YoDawgSAO/commits?path=badges/IronMan
  title: "Commit history for badges/IronMan"
  accessed: '2026-09-07'
  note: "Single commit by davedarko (2024-10-11) confirms he authored the Iron Man board files (KiCad project, netlist, production zip)."
- kind: url
  url: https://marc.merlins.org/perso/electronics/post_2024-11-02_Pasadena-Hackaday-Supercon-2024-Yo-Dawg-Micro-SAO-and-SMD-Soldering.html
  title: "Pasadena Hackaday Supercon 2024 Yo Dawg Micro SAO and SMD Soldering"
  accessed: '2026-09-07'
  note: "Marc Merlin's comment on the Hackaday.io project thanks davedarko for donating him one of the SAOAOs and confirms it was received at Supercon 2024; his blog post documents soldering a Yo Dawg micro SAO (theme of the specific unit he soldered is not confirmed as Iron Man in the post's surviving text)."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'MCU/LED chip type not stated anywhere found; davedarko himself noted in the 09/30/2024 log that he was not sure he had "the LEDs" for all 100 Iron Man boards, suggesting a simple discrete LED behind the mask rather than an addressable chip -- left tech.leds empty rather than guessing. Price is inferred as free from the give-away/trade framing in the project logs (no listed sale price found). Quantity of 100 is the number of bare PCBs ordered; unclear how many were actually assembled and handed out. No separate storefront or listing exists -- this was a con giveaway/trade item, not sold.'
last_modified_date: '2026-09-07'
---

The Iron Man SAOAO is one of several tiny "add-on for an add-on" boards davedarko designed for his Yo Dawg SAO project, made for the 2024 Hackaday Supercon badge add-on contest. Constrained to 19x19 mm with a 1.27 mm 3-pin header, it plugs into the Yo Dawg baseplate (itself a standard Simple Add-On) alongside slots for two more SAOAOs. The board is a red PCB with ENIG (gold) plating, with a cutout/mask silkscreen forming Iron Man's helmet face; a backlit LED behind the mask lights the eyes and face gold/amber when powered from the host badge.

davedarko had 100 of the red Iron Man boards panelized and fabricated by JLCPCB in September 2024, alongside 100 Yo Dawg baseplates, 100 Hackaday-logo SAOAOs, and other designs (an LED-matrix "Super Cluster" and a hackspace-logo board). He brought roughly 100 SAOs and 200 SAOAOs total to Supercon 2024 to give away and trade with other attendees who wanted to build their own SAOAO onto the standard. One of the Iron Man units was given to Marc Merlin, who documented using it to learn SMD soldering with solder paste and a heat gun.

## Make your own

KiCad source files (schematic, PCB, and a production folder with a netlist and gerber zip) are in the `badges/IronMan` folder of the [YoDawgSAO GitHub repo](https://github.com/davedarko/YoDawgSAO/tree/master/badges/IronMan). The board follows the SAOAO connector standard defined by the same repo: 19x19 mm max size, 1.27 mm pitch, 3-pin GND-VCC-GND header.

## History

Part of the "Yo Dawg SAO" series -- a set of nested Simple Add-on Add-ons davedarko created as a lighthearted response to the seriousness of the 2024 Supercon SAO contest, alongside a Hackaday-logo SAOAO, a "Super Cluster" LED matrix, and a hackspace-logo board.
