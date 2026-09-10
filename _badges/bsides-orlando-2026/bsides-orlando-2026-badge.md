---
title: BSides Orlando 2026 Badge
id: bsides-orlando-2026-bsides-orlando-2026-badge
layout: badge
parent: BSides Orlando 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-orlando-2026
year: 2026
makers:
- name: BSides Orlando
summary: An electronic conference badge for BSides Orlando 2026, styled as a retro-futuristic "clearance verified" multipass with a UV-reactive Orlando skyline illustration, built around a CH32V003 RISC-V microcontroller and an SAO port.
functions: Addressable RGB LEDs plus a single 3mm indicator LED; exposes a Simple Add-On (SAO) v2 header for plugging in other badgelife hardware; has mounting holes for a lanyard and an SAO tether.
look:
  colors:
  - blue
  - purple
  - orange
  - teal
  - gold
  shape: card
  themes:
  - space
  - sci-fi
  - mascot
  - pop culture
tech:
  mcu: CH32V003
  leds:
    count: null
    type: SK6812MINI-E
    note: Addressable RGB LED(s) plus one discrete 3mm through-hole LED; exact count not confirmed from the schematic.
  display: none
  connectivity:
  - i2c
  battery: single-cell (AAA holder) boosted to 3.3V via a TPS61021A boost converter
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/bsidesorlando/2026-badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bsidesorlando/2026-badge
  url: https://github.com/bsidesorlando/2026-badge
  kind: repo
images:
- file: assets/images/badges/bsides-orlando-2026/bsides-orlando-2026-badge/93795978a0.jpg
  source: https://github.com/bsidesorlando/2026-badge
  credit: BSides Orlando
  caption: UV-reactive artwork design for the 2026 badge PCB
contact: {}
notes:
- Originally found by the event-year sweep (task bsides-bsides-orlando) as a search snippet naming the repo 'bsidesorlando/2026-badge', with the design/maker/content unconfirmed at that time. Since confirmed real and active by reading the repo's own commit history and hardware files; see research.notes.
- Sweep title matched the maker's own repo name; no title change needed.
status: announced
sources:
- kind: url
  url: https://github.com/bsidesorlando/2026-badge
  title: BSides Orlando 2026 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-orlando); event read as ''bsides-orlando-2026''.'
- kind: url
  url: https://raw.githubusercontent.com/bsidesorlando/2026-badge/main/hardware/bsidesorl-v1.kicad_sch
  title: hardware/bsidesorl-v1.kicad_sch (KiCad schematic, commit 45fabc1)
  accessed: '2026-09-10'
  note: Confirmed MCU (CH32V003), LEDs (SK6812MINI-E addressable + 3mm discrete), SAO v2 header (Simple_Addon_v2), single-cell battery boosted via TPS61021A, and I2C pull-ups on the SAO bus.
- kind: url
  url: https://api.github.com/repos/bsidesorlando/2026-badge/commits
  title: Commit history for bsidesorlando/2026-badge
  accessed: '2026-09-10'
  note: Repo is an active, real project (14 commits Aug 4 - Sep 1, 2026 by Kevin Colley); latest commits "Final schematic, ready to order" and "Generate production files for JLCPCB" show the board was finalized and sent to fab. No firmware folder is present, only hardware/.
- kind: url
  url: https://bsidesorlando.org/event/
  title: Event Activites - Security BSides Orlando
  accessed: '2026-09-10'
  note: Official event page confirms a Soldering Village ("Bring your badge to life!") implying an electronic badge, but gives no badge specifics itself.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The GitHub repo is real and actively developed (not just a search-snippet rumor): KiCad schematic and PCB files, plus JLCPCB production-file generation, confirm a CH32V003-based badge with an SAO v2 port, addressable LEDs, and single-cell battery power via a boost converter. Repo commits are authored by Kevin Colley (kjcolley7@gmail.com); the org account is bsidesorlando, so makers is kept as "BSides Orlando" per the org''s own repo, with Kevin Colley noted here as the apparent hardware designer. No README, price, quantity, or distribution details were published anywhere found. Firmware does not appear to be in the repo (hardware/ only), so open_source is "partial" rather than "yes". The badge has not been distributed yet (con is Sept 25-26, 2026), hence availability: not_released and status: announced rather than released.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-orlando-2026/bsides-orlando-2026-badge.glb
  method: kicad
  source_file: hardware/bsidesorl-v1.kicad_pcb
  generated: '2026-09-10'
  bytes: 238380
---

The 2026 BSides Orlando badge is a retro-futuristic "clearance verified" ID card, complete with a UV-reactive Orlando skyline illustration (theme-park spires, a monorail, and a mascot creature riding a rocket sled) styled after a sci-fi movie multipass. Under the art is a real PCB: a CH32V003 RISC-V microcontroller drives SK6812MINI-E addressable RGB LEDs alongside a single discrete 3mm LED, power comes from a single cell (an AAA holder feeding a TPS61021A boost converter up to 3.3V), and the board carries a 6-pin SAO v2 header with I2C pull-ups and ESD protection so it can host other badgelife add-ons. Mounting holes are provided for both a lanyard and an SAO tether.

The hardware is being developed in the open on GitHub (`bsidesorlando/2026-badge`), with the schematic, PCB layout, and KiCad project files all committed publicly; as of September 1, 2026 the repo shows a "final schematic, ready to order" commit followed immediately by generated JLCPCB production files, indicating the board has been sent to fabrication ahead of the conference on September 25-26, 2026. No firmware repository has surfaced alongside the hardware, and the con's own site does not publish pricing, quantity, or distribution details, though its Soldering Village description ("Bring your badge to life!") corroborates that attendees receive an electronic badge meant to be soldered/assembled or extended.
