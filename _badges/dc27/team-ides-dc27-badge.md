---
title: da Bomb! (Team Ides DC27 Badge)
id: dc27-team-ides-dc27-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: John Adams / Team Ides
  url: https://github.com/netik
  role: lead / hardware / project owner
- name: Bill Paul
  role: firmware and Bluetooth implementation
summary: Team Ides' independent DEF CON 27 badge, a bomb-shaped board with BLE multiplayer games, an RGB LED matrix, and stereo audio, built as a follow-up to their DC25 'Ides of DEF CON' badge.
functions: Runs a real-time multiplayer sea-battle game with a physics engine over Bluetooth Low Energy, plus about 27 built-in applications; seven programmable buttons support a Konami-code easter egg; stereo audio playback; SD card slot with free space for user content; SAO connector for add-ons.
look:
  colors: []
  shape: bomb
  themes:
  - security
  - radio
  - ctf
tech:
  mcu: nRF52840 (BMD340)
  leds:
    count: null
    type: RGB
    note: Driven by an IS3736 I2C matrix LED driver (32x8).
  display: LED matrix
  connectivity:
  - ble
  - uart
  - i2c
  battery: LiPo, rechargeable, with fuel-gauge circuit
  sao_version: null
get_one:
  price: $120-$150 depending on payment method (Kickstarter)
  price_usd: 120
  quantity: '500'
  availability: sold_out
  distribution:
  - crowdfunding
  - purchase
  where: Funded via Kickstarter (exceeded a $25k goal); badges were also sold at troupeit.com/badge. 500 units were manufactured (496 functional), with about 160 shipped via USPS pre-event and the rest distributed at DEF CON 27 pickup windows.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/netik/dc27_badge
  firmware_url: https://github.com/netik/dc27_badge
  eda_tool: null
  license: Apache 2.0
  notes: Firmware runs ChibiOS; repo includes both PCB hardware design and firmware/game source (5,500+ lines of game code, custom drivers for 15+ onboard devices).
links:
- label: hackaday.io/project/161163-team-ides-dc27-badge
  url: https://hackaday.io/project/161163-team-ides-dc27-badge
  kind: hackaday
- label: 'GitHub: netik/dc27_badge'
  url: https://github.com/netik/dc27_badge
  kind: repo
- label: 'Kickstarter: it''s da Bomb! - An Indie DEF CON badge for DC27'
  url: https://www.kickstarter.com/projects/1887776662/its-da-bomb-an-indie-def-con-badge-for-dc27
  kind: store
- label: 'Team Ides: da Bomb Badge Post-Mortem'
  url: https://ides.team/dabomb/badge-post-mortem/
  kind: article
images:
- file: assets/images/badges/dc27/team-ides-dc27-badge/20ab33f703.jpg
  source: https://hackaday.io/project/161163-team-ides-dc27-badge
  credit: John Adams / Team Ides
  caption: The da Bomb! badge for DEF CON 27
- file: assets/images/badges/dc27/team-ides-dc27-badge/b6c85434a1.jpg
  source: https://hackaday.io/project/161163-team-ides-dc27-badge
  credit: John Adams / Team Ides
  caption: da Bomb! badge, DC27 (2019)
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://hackaday.io/project/161163-team-ides-dc27-badge
  title: Team Ides DC27 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27 (check if it exists in events.yml)''.'
- kind: url
  url: https://github.com/netik/dc27_badge
  title: netik/dc27_badge (GitHub)
  accessed: '2026-09-07'
  note: Confirmed Apache 2.0 open-source hardware and firmware for the DC27 'DaBomb!' badge.
- kind: url
  url: https://www.kickstarter.com/projects/1887776662/its-da-bomb-an-indie-def-con-badge-for-dc27
  title: it's da Bomb! - An Indie DEF CON badge for DC27 by John Adams — Kickstarter
  accessed: '2026-09-07'
  note: Confirmed crowdfunding, price tiers, that this is a follow-up to the DC25 'Ides of DEF CON' badge (225 units), and general feature description.
- kind: url
  url: https://ides.team/dabomb/badge-post-mortem/
  title: da Bomb - Badge Post-Mortem - Team Ides
  accessed: '2026-09-07'
  note: Source for production quantity/yield (500 made, 496 functional), BOM cost, distribution logistics, and known hardware/firmware issues.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own GitHub repo, Kickstarter page, and post-mortem write-up all corroborate. LED count and exact SAO header version were not stated in any source and are left empty. Price recorded as the Kickstarter reward range; no single confirmed retail price was found for troupeit.com/badge sales.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc27/team-ides-dc27-badge.glb
  method: kicad
  source_file: hardware/dc27_badge_kicad/DC27-badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 670752
---

Team Ides' "da Bomb!" was John Adams (netik)'s follow-up to the group's DC25 "Ides of DEF CON" badge, built for DEF CON 27 in 2019 with firmware and Bluetooth work by Bill Paul. It is a bomb-shaped, independently produced (non-official) badge built around a Nordic nRF52840 running ChibiOS, with an IS3736-driven RGB LED matrix, stereo audio via a Cirrus Logic DAC, seven buttons (including a Konami-code easter egg), a rechargeable LiPo battery with fuel gauge, an SD card slot, and an SAO connector for add-ons. Its headline feature was a real-time multiplayer "sea battle" game with a physics engine, playable over BLE between badges, alongside roughly 27 built-in applications.

The project was funded on Kickstarter, comfortably clearing its goal, with badges going for $120-$150 depending on payment method. Team Ides built 500 units (496 functional, a 99.4% yield) at an estimated BOM cost of about $93 each. Around 160 were mailed out via USPS ahead of the con, with the rest handed out at DEF CON 27 pickup windows; the team's own post-mortem describes that pickup process as chaotic, and also notes a late, largely untested redesign of the power-management circuit, I2C bus contention between the LED controller and SAO devices, and some joystick and silkscreen issues.

## Make your own

Hardware and firmware are fully open source (Apache 2.0) in the `netik/dc27_badge` GitHub repository, which includes the PCB design files alongside the ChibiOS-based firmware and game code (over 5,500 lines, with custom drivers for 15+ onboard devices).

## History

"da Bomb!" is the second badge in the Team Ides line, following the 225-unit "Ides of DEF CON" badge made for DC25 (2017).
