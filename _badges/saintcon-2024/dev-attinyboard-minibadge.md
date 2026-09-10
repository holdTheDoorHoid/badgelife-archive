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
functions: None documented; the board exposes the ATtiny1614's pins on two 7-pin headers for programming/prototyping. No LEDs, sensors, or games are present in the design.
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
- The sweep's title matches the repo folder name; no separate maker-given title was found.
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
  note: 'Confirms the design: one ATtiny1614-SS (SOIC-14), two SMD capacitors (C1, C2), and two 1x07 pin headers (J1, J2). No LEDs, display, or battery in the schematic.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: 'utahsaint-org/MiniBadges2024: Minibadges for SAINTCON 2024'
  accessed: '2026-09-10'
  note: Repo root listing confirms DEV-AttinyBoard sits alongside dozens of other named SAINTCON 2024 minibadge/community-badge KiCad folders.
- kind: url
  url: https://api.github.com/repos/utahsaint-org/MiniBadges2024/commits?path=DEV-AttinyBoard
  title: Commit history for DEV-AttinyBoard
  accessed: '2026-09-10'
  note: Single commit, author "Jup1t3r" (GitHub user tjhiker), message "Attendee" (2024-07-24). No real name given (profile bio is a non-identifying one-liner, location listed as Utah/US); not confident enough to attribute.
- kind: url
  url: https://github.com/utahsaint-org/saintcon.zip.files/blob/main/2024/2024-SAINTCON-MiniBadge-Guide-v3.0-10.20.2024-1.pdf
  title: 2024 SAINTCON MiniBadge Guide v3.0
  accessed: '2026-09-10'
  note: Full text of the official 2024 minibadge guide does not mention "AttinyBoard," "DEV-AttinyBoard," or an ATtiny1614 minibadge, so it is unconfirmed whether this design was ever fabricated or handed out to attendees.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Fact-check pass (2026-09-10): the researcher''s schematic source note and body text originally said the board had "one SMD capacitor" and "a 1x07 header" (singular). Re-fetched the raw KiCad schematic directly and confirmed by grepping component reference designators: it actually instantiates two capacitors (C1, C2) and two 1x07 headers (J1, J2) alongside the single ATtiny1614-SS (U1). Corrected the source note, functions field, research notes, and body to say "two" throughout. Also downloaded the 2024 SAINTCON MiniBadge Guide PDF directly (GitHub''s file-preview page does not render 38MB PDFs, so the earlier "full-text searched" claim could not be verified from the page alone) and ran a real full-text search for "AttinyBoard" and "1614": no hits. The guide''s only ATtiny mentions are three unrelated badges (ATtiny84a, ATtiny814, ATtiny412), so it is confirmed that DEV-AttinyBoard does not appear in the official guide, supporting the "distribution unconfirmed" framing. Checked
    the commit-author''s GitHub profile (tjhiker): it has no real name, but does have a short non-identifying bio ("I''m Living the Dream!") and lists "Utah/US" as location, so the "no name or bio" wording was slightly overstated; softened to "no real name given." All other cited facts (repo contents, folder list, single commit, MCU/package identification) checked out against their sources. With the component-count error fixed, everything remaining in the entry is supported by a source that was actually read.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2024/dev-attinyboard-minibadge.glb
  method: kicad
  source_file: DEV-AttinyBoard/AttinyBoard.kicad_pcb
  generated: '2026-09-10'
  bytes: 38180
---

DEV-AttinyBoard is a small KiCad hardware design checked into the SAINTCON 2024 community minibadge repository (`utahsaint-org/MiniBadges2024`) alongside that year's other minibadges. The schematic shows a single ATtiny1614-SS microcontroller (SOIC-14 package), two SMD decoupling capacitors, and two 1x07-pin headers breaking out the chip's pins — no LEDs, display, battery, or other components. It reads as a bare-bones ATtiny1614 breakout or programming jig rather than a badge with its own blinky or game functions.

Whether this design was ever fabricated and handed out to attendees is unconfirmed: it does not appear anywhere in the official "2024 SAINTCON MiniBadge Guide," which lists that year's released minibadges with their descriptions. It may instead have been an internal test board used by the badge-design community while developing other ATtiny-based minibadges, committed to the shared repo for reference rather than as a standalone released item.

The single commit that added the files is authored by the GitHub account "Jup1t3r" (username tjhiker), whose profile gives no real name — only a generic one-line bio and "Utah/US" as location — so the maker is recorded as unconfirmed. No photos of an assembled board, price, quantity, or distribution details were found anywhere online.
