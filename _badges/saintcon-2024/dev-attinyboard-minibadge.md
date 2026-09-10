---
title: DEV-AttinyBoard minibadge
id: saintcon-2024-dev-attinyboard-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: unconfirmed
summary: A bare-bones ATtiny1614 breakout design submitted to the SAINTCON 2024 community minibadge KiCad repository.
functions: 'None documented; the board exposes the ATtiny1614''s pins on a 7-pin header for programming/prototyping. No LEDs, sensors, or games are present in the design.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: ATtiny1614
  leds: null
  display: none
  connectivity: []
  battery: null
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
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/DEV-AttinyBoard
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/DEV-AttinyBoard
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/DEV-AttinyBoard
  kind: repo
images: []
contact: {}
notes:
- ATtiny developer/dev-board style minibadge submitted for SAINTCON 2024. Found by the event-year sweep, task saintcon-2024.
- 'The sweep''s title matches the repo folder name; no separate maker-given title was found.'
status: unknown
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/DEV-AttinyBoard
  title: DEV-AttinyBoard minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/utahsaint-org/MiniBadges2024/main/DEV-AttinyBoard/AttinyBoard.kicad_sch
  title: AttinyBoard.kicad_sch (raw schematic)
  accessed: '2026-09-10'
  note: 'Confirms the design: one ATtiny1614-SS (SOIC-14), one SMD capacitor, and a 1x07 pin header. No LEDs, display, or battery in the schematic.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: 'utahsaint-org/MiniBadges2024: Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: 'Repo root listing confirms DEV-AttinyBoard sits alongside dozens of other named SAINTCON 2024 minibadge/community-badge KiCad folders.'
- kind: url
  url: https://api.github.com/repos/utahsaint-org/MiniBadges2024/commits?path=DEV-AttinyBoard
  title: Commit history for DEV-AttinyBoard
  accessed: '2026-09-10'
  note: 'Single commit, author "Jup1t3r", message "Attendee" (2024-07-24). No maker name or description given; not confident enough to attribute.'
- kind: url
  url: https://github.com/utahsaint-org/saintcon.zip.files/blob/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  title: 2024 SAINTCON MiniBadge Guide v3.0
  accessed: '2026-09-10'
  note: 'Full text of the official 2024 minibadge guide does not mention "AttinyBoard," "DEV-AttinyBoard," or an ATtiny1614 minibadge, so it is unconfirmed whether this design was ever fabricated or handed out to attendees.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-10'
  notes: >-
    The GitHub repo and raw KiCad schematic confirm the design is real: an ATtiny1614-SS
    in SOIC-14, one decoupling capacitor, and a 1x07 header, with no LEDs, display, or
    onboard battery. It reads as a bare developer/prototyping breakout rather than a
    playable minibadge. It does not appear in the official 2024 SAINTCON MiniBadge Guide
    (searched the full text for "AttinyBoard" and "1614"), so I could not confirm it was
    fabricated in quantity or distributed to attendees; it may have been an internal
    design-team test board checked into the shared community repo alongside the actual
    released minibadges. The single commit adding it is authored by GitHub user
    "Jup1t3r" with no name or bio, so the maker remains unconfirmed. No photo of an
    assembled board was found. Price, quantity, and availability are unknown.
last_modified_date: '2026-09-10'
---

DEV-AttinyBoard is a small KiCad hardware design checked into the SAINTCON 2024 community minibadge repository (`utahsaint-org/MiniBadges2024`) alongside that year's other minibadges. The schematic shows a single ATtiny1614-SS microcontroller (SOIC-14 package), one SMD decoupling capacitor, and a 1x07-pin header breaking out the chip's pins — no LEDs, display, battery, or other components. It reads as a bare-bones ATtiny1614 breakout or programming jig rather than a badge with its own blinky or game functions.

Whether this design was ever fabricated and handed out to attendees is unconfirmed: it does not appear anywhere in the official "2024 SAINTCON MiniBadge Guide," which lists that year's released minibadges with their descriptions. It may instead have been an internal test board used by the badge-design community while developing other ATtiny-based minibadges, committed to the shared repo for reference rather than as a standalone released item.

The single commit that added the files is authored by the GitHub account "Jup1t3r," which has no public name, bio, or other identifying information, so the maker is recorded as unconfirmed. No photos of an assembled board, price, quantity, or distribution details were found anywhere online.
