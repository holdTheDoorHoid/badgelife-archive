---
title: Tamper Evident Community Badge
id: saintcon-2023-tamper-evident-community-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: SHIFTY
summary: A red PCB minibadge for SAINTCON's Tamper Evident community, whose members practice bypassing tamper-evident seals and security devices without leaving a trace.
functions: 'Passive: two LEDs light when the badge is powered through its 2-pin header. No other electronic function.'
look:
  colors:
  - red
  - black
  - white
  shape: rectangle
  themes:
  - security
  - puzzle
  - village badge
  form_factor: pcb badge
tech:
  mcu: none
  leds:
    count: 2
    type: 1206 SMD
    note: Two 1206 LEDs (D1, D2), each with its own 1206 resistor; no microcontroller, so they simply light when powered.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - contest
  where: Awarded for taking part in the Tamper Evident community's challenge on the SAINTCON 2023 convention floor.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: website
images:
  - file: assets/images/badges/saintcon-2023/tamper-evident-community-badge/58c8984353.jpg
    source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
    credit: "SHIFTY / SAINTCON"
    caption: "Front of the badge: red PCB with a toothy jaw graphic around TAMPER EVIDENT text"
  - file: assets/images/badges/saintcon-2023/tamper-evident-community-badge/2910fc211b.jpg
    source: "https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf"
    credit: "SHIFTY / SAINTCON"
    caption: "Back of the badge showing the two LEDs, resistors, and 2023 SAINTCON / SHIFTY silkscreen"
contact: {}
notes:
- 2023 community minibadge for the Tamper Evident community (bypassing tamper-evident security devices). Found by the event-year sweep, task saintcon-2023.
- The sweep only captured the badge's title from a search snippet; the full listing in the official 2023 Minibadge Guide (p.21) confirms it as a real, designed-and-distributed minibadge rather than a rumor.
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: 2023 SAINTCON Minibadge Guide - Tamper Evident Community Badge (p.21)
  accessed: '2026-09-10'
  note: 'Full page entry: designer (SHIFTY), description, difficulty (beginner), rarity (common), how to get one (participate in the community''s challenge), parts list (1206 LED, 1206 resistor, FR4 PCB, 2-pin headers), and front/back board photos.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Confirmed directly from the official 2023 SAINTCON Minibadge Guide PDF (page 21), which is the maker/organizer''s own publication. No price is listed since the badge is earned by participating in the Tamper Evident community''s challenge rather than sold; exact quantity made is not stated in the guide. No separate storefront, repo, or design files were found for this minibadge, which is typical for SAINTCON community minibadges.'
last_modified_date: '2026-09-10'
---

The Tamper Evident Community Badge is a 2023 SAINTCON minibadge designed by SHIFTY for the con's "Tamper Evident" community, a group focused on bypassing tamper-evident seals and other physical security devices without leaving a trace, using techniques like heat, chemicals, brute force, and careful inspection for imperfections. The badge itself is a small red FR4 PCB shaped like an open, toothy jaw, with "TAMPER EVIDENT" lettered across the front in a matching bite-mark motif; the back repeats the graphic in mirrored silkscreen alongside "2023 SAINTCON" and the designer's name.

Electronically it is simple: two 1206 SMD LEDs (D1 and D2), each paired with its own 1206 resistor, wired through a 2-pin header so the badge lights up when powered from a host badge. There is no microcontroller, battery, or independent power source. SAINTCON's official 2023 Minibadge Guide rates it "beginner" difficulty to assemble and "common" rarity, and states it was not sold but given out to attendees who came and took part in the Tamper Evident community's on-site challenge.

No design files, repository, or storefront listing were found for this badge; like most SAINTCON community minibadges it appears to have been distributed only at the convention itself. A follow-up "Tamper Evident minibadge (v2)" was produced for SAINTCON 2024 and is cataloged separately.
