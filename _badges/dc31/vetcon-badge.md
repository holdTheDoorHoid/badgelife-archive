---
title: VetCON Badge
id: dc31-vetcon-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: VetCON
  url: https://shop.threathunter.ai/collections/vetcon
summary: 'A crayon-box "SAO Totem" for VetCON at DEF CON 31: a green battery-powered base holds five swappable crayon-shaped SAOs, each silkscreened with a joke military-unit name and lit by one LED, plus a sixth standalone crayon SAO.'
functions: Six crayon-shaped SAOs each light a single colored LED when plugged into the totem's female headers; the totem and crayons carry engraved ciphers/puzzles for solvers to decode.
look:
  colors:
  - green
  - gold
  - yellow
  - blue
  - red
  - orange
  shape: rectangle
  themes:
  - military
  - puzzle
  - ctf
  - kit
  - learn to solder
tech:
  mcu: none
  leds:
    count: 6
    type: discrete
    note: One through-hole LED per crayon SAO (green, blue, red, yellow, white/black, orange), driven directly off the totem's battery pack through current-limiting resistors; no MCU.
  display: none
  connectivity:
  - i2c
  battery: 2x AA (NiMH rechargeable pack pictured)
  sao_version: v1.69bis
  sao_ports: 5
get_one:
  price: $60, later marked down to $40
  price_usd: 40
  quantity: First batch of 50 units (per a later restock listing)
  availability: sold_out
  availability_note: 'Checked via Wayback Machine snapshot from 2025-05-13; the product page was pulled from the live VetCON shop collection by 2026-09-06 and no 2023 badge listing remains.'
  distribution:
  - purchase
  - preorder
  - charity
  where: Pre-ordered online through the VetCON collection on shop.threathunter.ai (Milton Security Group's Shopify store), for in-person pickup only at VetCON at DEF CON 31 in Las Vegas; net profits went to fund VetCON certification tests and training materials.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  gerbers_url: null
  bom_url: https://github.com/wery67564/Vetcon_Badge_2023
  eda_tool: null
  license: null
  fab_url: null
  notes: The linked GitHub repo (the badge's own assembly guide) is a through-hole assembly/BOM writeup with soldering instructions and puzzle hints, not published board design files (no schematic, PCB, or firmware source found).
links:
- label: t.co/woIuy0ruPv
  url: https://t.co/woIuy0ruPv
  kind: website
- label: VetCON 2023 Badge product listing (Wayback Machine)
  url: http://web.archive.org/web/20250513000025/https://shop.threathunter.ai/collections/vetcon/products/preorder-vetcon-2023-badge-in-person-pickup-at-vetcon-only
  kind: store
- label: 'VetCON Badge 2023: assembly guide and puzzle hints (GitHub)'
  url: https://github.com/wery67564/Vetcon_Badge_2023
  kind: repo
images:
- file: assets/images/badges/dc31/vetcon-badge/2ffcb4bbb9.jpg
  source: "https://shop.threathunter.ai/collections/vetcon/products/preorder-vetcon-2023-badge-in-person-pickup-at-vetcon-only"
  credit: "VetCON / ThreatHunter.ai"
  caption: "VetCON 2023 SAO Totem badge with crayon-themed SAOs"
- file: assets/images/badges/dc31/vetcon-badge/b5fcfad762.jpg
  source: "https://shop.threathunter.ai/collections/vetcon/products/preorder-vetcon-2023-badge-in-person-pickup-at-vetcon-only"
  credit: "VetCON / ThreatHunter.ai"
  caption: "VetCON 2023 badge totem back side showing puzzle traces"
contact: {}
notes:
- Get them now before the Marines see them!!! Damn Jarheads will try and eat them all.
- 'The community sheet listed only a shortlink; the product itself (and its title) came from the archived Shopify listing, not the sheet.'
status: released
sources:
- kind: sheet
  event: dc31
  row: 85
  updated: '2023-07-21'
- kind: url
  url: http://web.archive.org/web/20250513000025/https://shop.threathunter.ai/collections/vetcon/products/preorder-vetcon-2023-badge-in-person-pickup-at-vetcon-only
  title: 'ONSITE ORDER FOR VETCON 2023 Badge **in-person pickup at VETCON ONLY**'
  accessed: '2026-09-07'
  note: Product description, price history ($60 -> $40 sale), quantity (first 50 units), pickup-only distribution, and the "SAO Totem plus 6 SAOs" concept; also links to the GitHub assembly guide.
- kind: url
  url: https://github.com/wery67564/Vetcon_Badge_2023
  title: Vetcon_Badge_2023 (GitHub)
  accessed: '2026-09-07'
  note: Assembly/BOM details -- 2x AA battery pack, six LED colors, 2x3 male/female SAO headers, resistor values -- and confirmed no board design files are published, only an assembly guide.
- kind: url
  url: https://shop.threathunter.ai/collections/vetcon
  title: Vetcon – ThreatHunter.ai
  accessed: '2026-09-07'
  note: Confirmed the 2023 badge listing is no longer live on the current VetCON storefront (only a 2025 badge and wall flags remain), supporting sold_out/no-longer-listed status.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own product listing (via Wayback Machine, since removed from the live store) and the badge''s own GitHub assembly guide confirm the concept, price, and BOM. No MCU is used (LEDs are directly wired), so tech.mcu is "none" despite the badge having GPIO/SDA/SCL-labeled SAO headers on the totem PCB (visible in the battery-side photo) -- those appear to be pass-through SAO signal pins, not a controller on the totem itself. Could not confirm exact total quantity produced for the original 2023 run (only a later restock mentions "first 50 units"), nor a firmware/hardware source repo beyond the assembly-guide repo. No maker page beyond the Shopify store was found.'
last_modified_date: '2026-09-07'
---

VetCON is a hacker-veteran community track that runs alongside DEF CON, and its 2023 electronic badge for DEF CON 31 took the form of a crayon box. A green PCB "totem," silkscreened with VetCON's skull-and-circuitry logo and powered by two AA batteries, holds five female SAO headers arranged like the flap of a crayon box. Five crayon-shaped SAO boards click into those headers, each printed with a tongue-in-cheek "crayon name" riffing on a military branch or unit stereotype (seen in maker photos: Canoe Club, Chair Force, Seal Please, Marin Crops, and The Army), and each lighting a single colored LED (green, blue, red, yellow/white, and orange) when plugged in. A sixth crayon SAO ships loose. The badge doubled as a running gag and a puzzle: traces and engravings on the totem and crayons carried ciphers for attendees to decode, alongside knowing jabs at "Intel Weenies" needing DIRNSA's blessing to solve them.

The badge was sold as an online preorder through VetCON's storefront on Milton Security Group's Shopify site (shop.threathunter.ai), strictly for in-person pickup at VetCON during DEF CON 31 in Las Vegas -- no shipping, no refunds if you didn't show up. Net profits funded VetCON's certification tests and training materials for its members. A later listing on the same store, marking the badge down from $60 to $40, mentions the first 50 units of a restock; the original 2023 run's total quantity isn't stated anywhere found. By September 2026 the listing had been pulled from VetCON's live collection entirely.

## Make your own

No schematic, PCB, or firmware files were found published for this badge -- what exists is an assembly guide on GitHub (linked from the badge itself as `tinyurl.com/vetcon-badge-guide`) covering through-hole soldering steps, a bill of materials (six LEDs in six colors, a 2x AA battery holder, 0/120/330 ohm and 10k resistors, keyed 2x3 male/female SAO headers), and hints for the badge's cryptographic puzzles. Anyone wanting to build a similar totem-and-SAO-crayon badge would need to reverse the PCB layout from photos, since no Gerbers or CAD source are linked.
