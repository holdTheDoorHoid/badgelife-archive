---
title: KidsNight-Badge-2024
id: saintcon-2024-kidsnight-badge-2024
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: unconfirmed
summary: A SAINTCON 2024 minibadge made for the Kids Night event, with a blinky ATtiny85 circuit and three LEDs.
functions: Blinks its three LEDs; the ATtiny85 schematic firmware/logic itself was not published in the repo.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ATtiny85
  leds:
    count: 3
    type: discrete
    note: Generic "Device:LED" symbols in the schematic; not addressable/RGB.
  display: none
  connectivity:
  - none
  battery: coin cell (generic battery symbol in schematic; exact type not specified)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/KidsNight-Badge-2024
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/KidsNight-Badge-2024
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/KidsNight-Badge-2024
  kind: repo
- label: SAINTCON MiniBadges (saintcon.org)
  url: https://saintcon.org/minibadges/
  kind: website
images: []
contact: {}
notes:
- Kids' Night event minibadge for SAINTCON 2024. Found by the event-year sweep, task saintcon-2024.
- Sweep/sheet used the folder name "KidsNight-Badge-2024" as the title; the repo's own file names use "KidsNight" without the year suffix (e.g. 2023-KidsNight.kicad_pcb, a carried-over filename from a prior year's design). Kept the sheet's title since no maker-published name differs from it.
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/KidsNight-Badge-2024
  title: KidsNight-Badge-2024
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/KidsNight-Badge-2024/2023-KidsNight.kicad_sch
  title: 2023-KidsNight.kicad_sch (raw)
  accessed: '2026-09-10'
  note: Read schematic symbols directly to confirm MCU (ATtiny85), 3 discrete LEDs, a battery, and a MiniBadge connector part; no wireless connectivity or display present.
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: 'MiniBadges2024 (utahsaint-org): Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: Confirms this repo is the community collection of official SAINTCON 2024 minibadges, including the KidsNight folder.
- kind: url
  url: https://saintcon.org/minibadges/
  title: SAINTCON MiniBadges
  accessed: '2026-09-10'
  note: General background on how SAINTCON minibadges are distributed (trading/earning/building); no Kids Night-specific detail found there.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed via the maker''s own repo (utahsaint-org/MiniBadges2024) that this is a real minibadge made for the SAINTCON 2024 Kids Night event, part of the community''s official 2024 minibadge collection. The KiCad schematic shows an ATtiny85 MCU, three discrete (non-addressable) LEDs, a battery, and a resistor, driven off a SAINTCON "MiniBadge" connector part (not a standard SAO header) -- consistent with SAINTCON''s own klip-on minibadge system rather than the badge.life SAO standard. No firmware source was found in the repo (hardware/PCB files only: KiCad project, Gerbers, and vector art), so open_source is marked partial rather than yes. Could not confirm: an individual designer/maker name (the repo is published under the community org account, not a named person), colors/shape (no raster photos exist in the repo -- only SVG and Adobe Illustrator vector files, which the archive''s image tool cannot save as photos), price, quantity made, or how it was distributed at the event
    (SAINTCON minibadges are generally free/traded/earned per saintcon.org, but nothing ties that specifically to this badge). A 38MB official "2024 SAINTCON MiniBadge Guide" PDF in a companion repo likely documents this badge in more depth but was too large to fetch within budget.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2024/kidsnight-badge-2024.glb
  method: kicad
  source_file: KidsNight-Badge-2024/2023-KidsNight.kicad_pcb
  generated: '2026-09-10'
  bytes: 193068
---

This minibadge was made for SAINTCON 2024's Kids Night event, part of the annual community-built minibadge collection that SAINTCON attendees trade, earn, and build throughout the conference. Its design files live in the `utahsaint-org/MiniBadges2024` GitHub repository alongside dozens of other 2024 minibadges, in a folder that carries over a 2023-dated schematic and PCB filename (`2023-KidsNight`), suggesting the design was reused or only lightly updated from a prior year.

Electrically, it is a simple blinky board: an ATtiny85 microcontroller drives three individual (non-addressable) LEDs, powered by a coin-cell battery, with the whole thing wired into SAINTCON's own "MiniBadge" connector footprint rather than a badge.life-style SAO header. No display, wireless radio, or other inputs are present in the schematic.

The repository publishes the hardware design (KiCad schematic and PCB, Gerbers, and vector artwork for the silkscreen/solder mask) but no firmware source, so it is only partially open source. No photos of the finished board, price, production quantity, or distribution details were found; SAINTCON's own minibadge page describes minibadges generally as traded, earned through challenges, or built and brought to trade, but nothing specific to this badge's Kids Night distribution was located.
