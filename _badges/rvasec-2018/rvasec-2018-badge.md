---
title: RVAsec 2018 Badge
id: rvasec-2018-rvasec-2018-badge
layout: badge
parent: RVAsec 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2018
year: 2018
makers:
- name: HackRVA
  url: https://www.hackrva.org/badge/
summary: An open, hackable electronic conference badge built by HackRVA for RVAsec 2018, with games, puzzles, and two-channel audio meant to get attendees talking to each other.
functions: Includes buttons, two-channel audio/speaker output, and games/puzzles that tied into a conference badge-hacking CTF room.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - ctf
tech:
  mcu: PIC32
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '300+'
  availability: unknown
  distribution:
  - free_drop
  where: Given to RVAsec 2018 attendees (Richmond Marriott, June 7-8, 2018).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HackRVA/badge18-public
  eda_tool: null
links:
- label: badge.gallery/badges/rvasec-2018-badge
  url: https://badge.gallery/badges/rvasec-2018-badge
  kind: website
- label: HackRVA wiki - RVAsec Badge Build 2018
  url: https://wiki.hackrva.org/index.php/RVAsec_Badge_Build_2018
  kind: doc
- label: GitHub - HackRVA/badge18-public (firmware)
  url: https://github.com/HackRVA/badge18-public
  kind: repo
- label: hack.RVA badge page
  url: https://www.hackrva.org/badge/
  kind: website
images: []
contact: {}
notes:
- HackRVA electronic badge for RVAsec 2018, also documented on the HackRVA wiki's badge-builds page. Confirmed on badge.gallery and the HackRVA wiki/GitHub. Sweep's one-line summary matches confirmed sources. Found by the event-year sweep, task con-rvasec.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/rvasec-2018-badge
  title: RVAsec 2018 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2018''.'
- kind: url
  url: https://badge.gallery/badges/rvasec-2018-badge
  title: RVAsec 2018 Badge - badge.gallery summary
  accessed: '2026-09-10'
  note: Confirms games/puzzles/two-channel audio, HackRVA build contacts Morgan and Paul, RVAsec 2018 dates (June 7-8, Richmond Marriott), and that over 300 badges were produced; no schematic/BOM/manufacturing archive recovered by that project.
- kind: url
  url: https://wiki.hackrva.org/index.php/RVAsec_Badge_Build_2018
  title: RVAsec Badge Build 2018 - HackRVA wiki
  accessed: '2026-09-10'
  note: Describes the badge as "open and completely hackable" hardware with games/puzzles for attendee-attendee interaction; names Morgan and Paul as build contacts; links to a HackRVA GitLab repo not independently checked.
- kind: url
  url: https://github.com/HackRVA/badge18-public
  title: 'GitHub - HackRVA/badge18-public: firmware for the RVASec 2018 badges'
  accessed: '2026-09-10'
  note: Firmware repo confirms a PIC32 MCU (Microchip Harmony v1.09 + FreeRTOS, MPLAB X/XC32), an RGB LED used as a bootloader-mode indicator, and a physical button used to enter programming mode. No display, battery, or BOM details found in the excerpt read.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Existence and core facts (maker, event, games/puzzles/audio, PIC32 MCU) confirmed by HackRVA''s own wiki and firmware repo, so this is not just a search snippet. Could not confirm: LED count/type beyond a single status RGB LED noted in the firmware repo, display (likely none, but not stated), battery/power source, exact price (badges were given to attendees, not sold), and a rights-cleared photo of the actual badge - hackrva.org/badge/ has undated photos spanning many badge years and none could be confidently tied to 2018 specifically, so no image was saved. The firmware README''s hardware-repo link (github.com/HackRVA/Harmony-Badge-2018) now 404s, so hardware_url was left null and open_source set to partial (firmware only, confirmed reachable).'
last_modified_date: '2026-09-10'
---

HackRVA, the Richmond, Virginia hackerspace, built the electronic badges given to attendees of RVAsec 2018, a security conference held June 7-8, 2018 at the Richmond Marriott. As with HackRVA's other RVAsec badge builds, the 2018 badge was designed to be "open and completely hackable," built around games and puzzles meant to get attendees talking to and hacking on each other's badges, plus a two-channel audio/speaker feature. It tied into a badge-hacking CTF run during the conference. HackRVA's build team, with Morgan and Paul serving as primary contacts, reported producing more than 300 badges representing hundreds of person-hours of work.

The badge runs on a PIC32 microcontroller, programmed with Microchip's MPLAB Harmony v1.09 framework and FreeRTOS, built in MPLAB X with the XC32 compiler. The firmware repository documents an RGB LED used as a status indicator during bootloader/programming mode and a physical button used to enter that mode, but does not spell out the full LED count, display, or battery details for the badge itself.

## Make your own

Firmware source is public at github.com/HackRVA/badge18-public, which documents the MPLAB X/Harmony/XC32 toolchain setup. The README points to a separate hardware repository (Harmony-Badge-2018) for the PCB design, but that repository no longer resolves, so the hardware side is not currently available.
