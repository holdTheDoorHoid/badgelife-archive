---
title: RVAsec 2013 Badge
id: rvasec-2013-rvasec-2013-badge
layout: badge
parent: RVAsec 2013
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2013
year: 2013
makers:
- name: HackRVA
  url: https://www.hackrva.org/
summary: An electronic conference badge built by HackRVA for RVAsec 2013, with LEDs, infrared badge-to-badge play, a piezo speaker, and USB support.
functions: Badge-to-badge play over infrared, piezo speaker audio, USB connectivity (for firmware reflashing/audit), and a game/audit mode described in the firmware repo as a peripheral test bed.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - ir
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to RVAsec 2013 attendees in Richmond, VA.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HackRVA/rvasec-badge-2013
  eda_tool: null
links:
- label: badge.gallery/events/rvasec-2013
  url: https://badge.gallery/events/rvasec-2013
  kind: website
- label: github.com/HackRVA/rvasec-badge-2013
  url: https://github.com/HackRVA/rvasec-badge-2013
  kind: repo
- label: hack.RVA badge page
  url: https://www.hackrva.org/badge/
  kind: website
images:
  - file: assets/images/badges/rvasec-2013/rvasec-2013-badge/1449f0a904.jpg
    source: "https://github.com/HackRVA/rvasec-badge-2013"
    credit: "HackRVA"
    caption: "RVAsec 2013 badge PCB, from the HackRVA firmware repository"
contact: {}
notes:
- Electronic badge with LEDs, IR badge-to-badge play, piezo speaker, and USB support, built by HackRVA. Found by the event-year sweep, task con-rvasec.
status: listed
sources:
- kind: url
  url: https://badge.gallery/events/rvasec-2013
  title: RVAsec 2013 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2013''.'
- kind: url
  url: https://github.com/HackRVA/rvasec-badge-2013
  title: 'HackRVA/rvasec-badge-2013 - GitHub'
  accessed: '2026-09-08'
  note: 'Confirms the badge is a real hardware/firmware project ("the rvasec badge - 2013 edition"), an MPLAB X project with Badge.X and BadgeAudit.X folders; source of the saved photo (badge.png).'
- kind: url
  url: https://www.hackrva.org/badge/
  title: 'Badge - hack.RVA'
  accessed: '2026-09-08'
  note: 'Confirms HackRVA builds a badge every year for RVAsec; no 2013-specific technical detail found on this page.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: >-
    Existence confirmed by the maker's own GitHub repo (HackRVA/rvasec-badge-2013),
    which matches the sweep's description of LEDs/IR/piezo/USB. The repo is an
    MPLAB X project, implying a Microchip PIC-family MCU, but no specific part
    number is stated anywhere found, so tech.mcu is left null rather than guessed.
    Could not find price, quantity made, LED count/type, or display info from any
    source (badge.gallery, GitHub repo, hackrva.org, or the HackRVA wiki, which
    only lists builds from 2014 onward). The RVAsec badges page on rvasec.com only
    covers the 2016 badge, not 2013. Repo appears to be firmware/software only
    (no separate hardware/Gerber repo found), so make_your_own.open_source is
    'partial'.
last_modified_date: '2026-09-08'
---

The RVAsec 2013 badge was the second annual conference badge built by HackRVA, the Richmond, Virginia hacker/makerspace, for the RVAsec security conference held May 31–June 1, 2013. Like other early HackRVA badges, it was an electronic PCB badge rather than a passive one, giving attendees LEDs, a piezo speaker, and infrared badge-to-badge play, plus USB support that the accompanying firmware repository frames mainly around a "badge audit" test program used to verify each board's peripherals after fabrication.

HackRVA's firmware for the badge lives in the `rvasec-badge-2013` GitHub repository as an MPLAB X project (Badge.X and BadgeAudit.X), which points to a Microchip PIC-family microcontroller, though no specific part number is named in the repo. No hardware/Gerber files, pricing, or production-quantity information could be found; HackRVA's own wiki history of badge builds only goes back to 2014, and RVAsec's blog coverage of "the badges" only documents the 2016 edition. The badge appears to have been a free give-away to attendees rather than sold.

