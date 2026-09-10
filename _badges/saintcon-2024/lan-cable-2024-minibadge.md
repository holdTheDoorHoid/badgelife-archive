---
title: Lan Cable Contest Minibadge
id: saintcon-2024-lan-cable-2024-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: Jup1t3r
summary: A SAINTCON 2024 official minibadge tied to the LAN Cable Contest, a simple two-LED board whose "gameplay" is crimping a network cable and looping it through the badge's own headers.
functions: Two LEDs light up when a hand-crimped LAN cable is looped through the badge's four 2-position headers, connecting the "crimp ends" side to the "loop cable" side.
look:
  colors:
  - green
  shape: circle
  themes:
  - hardware tool
  - ctf
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 1206 LEDs, single-pad hand-soldered
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Awarded for entering/completing SAINTCON 2024's LAN Cable Contest (build a network cable as fast as you can).
make_your_own:
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/LAN-Cable-2024
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/LAN-Cable-2024
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/LAN-Cable-2024
  kind: repo
- label: 2024 SAINTCON MiniBadge Guide (PDF, p.46)
  url: https://raw.githubusercontent.com/utahsaint-org/saintcon.zip.files/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  kind: doc
images:
- file: assets/images/badges/saintcon-2024/lan-cable-2024-minibadge/lan-cable-2024-front.jpg
  source: https://raw.githubusercontent.com/utahsaint-org/saintcon.zip.files/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  credit: SAINTCON MiniBadge Guide 2024
  caption: Front of the LAN Cable Contest minibadge, showing its two LEDs
- file: assets/images/badges/saintcon-2024/lan-cable-2024-minibadge/lan-cable-2024-back.jpg
  source: https://raw.githubusercontent.com/utahsaint-org/saintcon.zip.files/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  credit: SAINTCON MiniBadge Guide 2024
  caption: Back of the LAN Cable Contest minibadge, showing the crimp-ends and loop-cable pads
contact: {}
notes:
- The sweep filed this as "LAN-Cable-2024 minibadge" after its repo folder name; the maker/build-guide name is "Lan Cable Contest Minibadge."
- Listed as difficulty ADVANCED, rarity RARE in the official 2024 SAINTCON MiniBadge Guide.
status: released
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/LAN-Cable-2024
  title: LAN-Cable-2024 minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/saintcon.zip.files/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  title: 2024 SAINTCON MiniBadge Guide v3.0
  accessed: '2026-09-10'
  note: 'Page 46 entry for the "Lan Cable Contest Minibadge": maker (Jup1t3r), description, difficulty/rarity, assembly steps, parts list (1206 LED, 1206 resistor, FR4 PCB, 2-pin headers), and front/back board photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: The KiCad source repo has no README or firmware for this board; all descriptive detail comes from the official build guide's page 46 entry. No storefront, price, or quantity-made figure was found — it appears to have been earned through the LAN Cable Contest rather than sold or freely distributed. Board/LED-type diagram in the guide confirms "LED" discrete part markers rather than an addressable LED type.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2024/lan-cable-2024-minibadge.glb
  method: kicad
  source_file: LAN-Cable-2024/LAN-Cable-2024.kicad_pcb
  generated: '2026-09-10'
  bytes: 42152
---

The Lan Cable Contest Minibadge is one of the official minibadges from SAINTCON 2024, designed by community member Jup1t3r and tied to the conference's LAN Cable Contest. Rather than being sold or handed out freely, it was earned by trying the contest: build your own Cat5/Cat6 patch cable as fast as possible, crimping both RJ-45 ends.

The board itself is a small green PCB with two large silkscreen mounting/probe circles on front and back, silkscreened "LAN CABLE CONTEST" text and two discrete 1206 LEDs on the front, and "CRIMP ENDS" / "LOOP CABLE" labels flanking a 1206 resistor on the back. It has no microcontroller; assembly is limited to hand-soldering the two LEDs, a resistor, and four 2-position pin headers, after which the badge is completed by looping a hand-crimped cable through it — from the crimp-ends side to the loop-cable side, as short a loop as the builder can manage. The official build guide lists it at ADVANCED difficulty and RARE rarity.

The bare KiCad design files (schematic, PCB, project) are published in SAINTCON's MiniBadges2024 GitHub repository, but the repo carries no README, firmware, or bill-of-materials beyond what the printed guide documents, so this entry likely undercounts how the badge was actually distributed or priced.
