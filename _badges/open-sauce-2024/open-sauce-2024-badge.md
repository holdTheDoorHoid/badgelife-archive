---
title: Open Sauce 2024 Badge
id: open-sauce-2024-open-sauce-2024-badge
layout: badge
parent: Open Sauce 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: open-sauce-2024
year: 2024
makers:
- name: DC Punks
  url: https://pawprintprototyping.org/tags/opensauce/
  role: designer (member of Pawprint Prototyping)
summary: 'The official festival badge for Open Sauce 2024 in San Francisco: a through-hole PCB cut into the shape of the Open Sauce robot mascot, with a pair of LED "blinking eyes" driven by a simple analog flasher circuit.'
functions: 'Two LEDs blink as the robot''s eyes, driven by an astable multivibrator (two-transistor oscillator) rather than a microcontroller.'
look:
  colors: []
  shape: robot
  themes:
  - robot
  - mascot
  form_factor: pcb badge
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 5mm through-hole LEDs (builder's choice of color; UV purple used in the DigiKey assembly writeup), blinked by a two-transistor astable multivibrator, not a microcontroller
  display: none
  connectivity: []
  battery: 9V battery with clip connector
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  availability_note: 'Checked 2026-09-08: this was an event giveaway, not a storefront item; no listing found.'
  distribution:
  - free_drop
  where: Given out to Open Sauce 2024 attendees in San Francisco.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  gerbers_url: null
  bom_url: https://www.digikey.com/en/maker/tutorials/2024/building-better-badges-assembling-the-open-sauce-2024-pcb-badge
  eda_tool: null
  fab_url: https://www.pcbway.com/project/share/Open_Sauce_Badge_Project_0af58b9b.html
  license: null
  notes: 'DigiKey published a full assembly tutorial with bill of materials and step-by-step through-hole soldering instructions; PCBWay hosts the project as a "shared project" (order page for the bare board), but no schematic, firmware repo, or Gerber download was found.'
links:
- label: www.digikey.com/en/maker/tutorials/2024/building-better-badges-assembling-the-open-sauce-2024-pcb-badge
  url: https://www.digikey.com/en/maker/tutorials/2024/building-better-badges-assembling-the-open-sauce-2024-pcb-badge
  kind: article
- label: www.pcbway.com/project/share/Open_Sauce_Badge_Project_0af58b9b.html
  url: https://www.pcbway.com/project/share/Open_Sauce_Badge_Project_0af58b9b.html
  kind: fab
- label: pawprintprototyping.org/tags/opensauce
  url: https://pawprintprototyping.org/tags/opensauce/
  kind: website
images: []
contact: {}
notes:
- 'Sweep-imported entry originally titled "Open Sauce 2024 Badge" with makers listed as "DC Punks (Pawprint Prototyping)"; research confirms DC Punks is an individual member of the Pawprint Prototyping group who is credited with designing the badge, so the maker field was split into name + affiliation.'
status: released
sources:
- kind: url
  url: https://www.digikey.com/en/maker/tutorials/2024/building-better-badges-assembling-the-open-sauce-2024-pcb-badge
  title: 'Building Better Badges: Assembling the Open Sauce 2024 PCB Badge'
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-open-sauce); event read as ''Open Sauce 2024''.'
- kind: url
  url: https://www.digikey.com/en/maker/tutorials/2024/building-better-badges-assembling-the-open-sauce-2024-pcb-badge
  title: 'Building Better Badges: Assembling the Open Sauce 2024 PCB Badge'
  accessed: '2026-09-08'
  note: 'Confirms analog (no-MCU) LED flasher circuit, through-hole BOM (2x 47K and 2x 470R resistors, 2x PN2222 transistors, 2x 47uF caps, 5mm LEDs), 9V battery power, and that it was distributed as an event badge in San Francisco.'
- kind: url
  url: https://pawprintprototyping.org/tags/opensauce/
  title: Pawprint Prototyping — Open Sauce tag
  accessed: '2026-09-08'
  note: 'Names DC Punks, a member of the Pawprint Prototyping group, as the badge''s designer; describes the astable-multivibrator eye-blink circuit.'
- kind: url
  url: https://www.pcbway.com/project/share/Open_Sauce_Badge_Project_0af58b9b.html
  title: Open Sauce Badge Project — PCBWay shared project
  accessed: '2026-09-08'
  note: 'Confirms the badge was fabricated through PCBWay (project posted Sep 7, 2024); page carries no schematic, BOM, or photos beyond the bare order form.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08) re-fetched all three cited pages and confirmed every non-empty field and body sentence: DigiKey confirms robot-face shape, 2x 5mm through-hole LEDs (UV purple in their build), astable multivibrator (no MCU), 9V battery, exact BOM (2x 47k, 2x 470R, 2x PN2222, 2x 47uF), and free distribution at the SF event. Pawprint Prototyping''s tag page confirms DC Punks as designer and the astable-multivibrator description. PCBWay share page confirms the project exists (posted 2024-09-07) and confirms the negative — no schematic/BOM/photos on that page, matching make_your_own.notes. No contradictions found. Still not found: PCB color/solder-mask, quantity made, whether ever offered for sale, and any photo of the assembled badge.'
last_modified_date: '2026-09-08'
---

The Open Sauce 2024 badge was the official festival badge for Open Sauce, the maker/creator convention held in San Francisco. Rather than a microcontroller-driven board, it is a simple through-hole PCB cut into the shape of the event's robot mascot, with a pair of LEDs standing in for the robot's eyes. The eyes blink courtesy of a classic two-transistor astable multivibrator — "a few extra jellybean components," as the designer's team put it — so the whole badge runs on a single 9V battery with no firmware at all.

The badge was designed by DC Punks, a member of the maker collective Pawprint Prototyping, who was credited by name in the group's own recap of the event. The bare boards were fabricated through PCBWay, which lists the design as a shared community project. DigiKey later published a full assembly tutorial and bill of materials for the badge as part of a "Building Better Badges" series, walking through soldering the resistors, transistors, capacitors, and LEDs by hand — useful for anyone who picked one up unassembled or wants to build a replica after the fact.

No listing, price, or production-quantity information was found; it appears to have been handed out to attendees rather than sold, consistent with it being a con badge rather than a storefront product.
