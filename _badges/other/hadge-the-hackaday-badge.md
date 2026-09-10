---
title: Hadge, the Hackaday Badge
id: other-hadge-the-hackaday-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2014
makers:
- name: Anool Mahidharia
  url: https://hackaday.io/anool
- name: Michele Perla
  role: hardware design lead
- name: Hack-a-Day / Hackaday.io community (51-member collaborative team, incl. Mike Szczys, Benchoff)
summary: HaDge is a community-designed wearable badge built by Hackaday.io contributors as "a physical extension of the hackaday.io community," meant to form a mesh network (the "Sub-Etha network") between wearers at events.
functions: Displays user profile info and messages from the Hackaday community; mesh-networks with other HaDge badges over radio (with a planned internet gateway); IR transmit/receive; touch buttons for interaction.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - logo
tech:
  mcu: Atmel SAM D21 (later revised toward SAM R21 with integrated radio)
  leds:
    type: WS2812B
    note: multiple RGB LEDs
  display: 2.4" color TFT LCD (240x320)
  connectivity:
  - ir
  battery: 3.7V 2500mAh LiPo
  sao_version: null
get_one:
  price: ''
  price_usd: 35
  quantity: ''
  availability: unknown
  distribution: []
  where: Intended for distribution to Hackaday.io community members at conferences Hackaday attended; no evidence of general retail sale.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Hack-a-Day/HaDge_HW
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/3009-hadge-the-hackaday-badge
  url: https://hackaday.io/project/3009-hadge-the-hackaday-badge
  kind: hackaday
- label: HaDge_HW hardware repo (GitHub)
  url: https://github.com/Hack-a-Day/HaDge_HW
  kind: repo
- label: 'Developed on Hackaday: It''s a Badge. No, It''s the HaDge (Hackaday.com)'
  url: https://hackaday.com/2015/10/26/developed-on-hackaday-its-a-badge-no-its-the-hadge/
  kind: article
  archived: https://web.archive.org/web/20260420095651/https://hackaday.com/2015/10/26/developed-on-hackaday-its-a-badge-no-its-the-hadge/
images:
- file: assets/images/badges/other/hadge-the-hackaday-badge/dec7a912b9.png
  source: https://hackaday.io/project/3009-hadge-the-hackaday-badge
  credit: Anool Mahidharia / HaDge team
  caption: HaDge project render/photo
contact: {}
notes:
- 'Not tied to a single named convention: the project was designed as a general Hackaday-community badge meant to be deployed at "every event" Hackaday attended, so no single event id in _data/events.yml matches it. Left under event: other.'
status: announced
sources:
- kind: url
  url: https://hackaday.io/project/3009-hadge-the-hackaday-badge
  title: Hadge, the Hackaday Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/3009-hadge-the-hackaday-badge
  title: HaDge - The Hackaday Badge | Hackaday.io
  accessed: '2026-09-07'
  note: 'Project overview: maker, features (TFT display, WS2812B LEDs, touch, IR, mesh radio), SAM D21 MCU, $35 BOM target, LiPo battery, KiCad hardware/firmware/software repos.'
- kind: url
  url: https://hackaday.com/2015/10/26/developed-on-hackaday-its-a-badge-no-its-the-hadge/
  title: Developed On Hackaday – It's A Badge. No, It's The HaDge | Hackaday
  accessed: '2026-09-07'
  note: Confirms Michele Perla as hardware design lead and Anool Mahidharia coordinating; describes Sub-Etha mesh network concept and a SAM R21-based HACK dev kit; article dated Oct 2015, still in design/announcement stage.
  archived: https://web.archive.org/web/20260420095651/https://hackaday.com/2015/10/26/developed-on-hackaday-its-a-badge-no-its-the-hadge/
- kind: url
  url: https://github.com/Hack-a-Day/HaDge_HW
  title: 'GitHub - Hack-a-Day/HaDge_HW: A wearable thing for Hackaday folks.'
  accessed: '2026-09-07'
  note: 'Confirms hardware repo exists under the Hack-a-Day GitHub org, supporting open_source: yes for hardware.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, MCU, display, LEDs, battery, $35 BOM target, KiCad hardware files) confirmed on the maker's own Hackaday.io project page and a Hackaday.com "Developed on Hackaday" article. Could not find a firmware repo URL, a final production quantity, actual distribution event(s)/dates, or confirmation the badge was ever finished and handed out versus remaining a community design project (sources describe it as still in development as of late 2015). look.colors and look.shape left empty since no clear photo of a finished physical unit with colors was found beyond the project render. Price is a target BOM cost, not a retail/sale price, so get_one.price left blank and price_usd holds the $35 figure with that caveat in mind.
last_modified_date: '2026-09-07'
---

HaDge was a community-built electronic badge project run through Hackaday.io's "Developed on Hackaday" series, coordinated by Anool Mahidharia with Michele Perla leading hardware design, and built out by a roughly 51-person volunteer team that included Hackaday staff like Mike Szczys and Benchoff. The idea was to give the Hackaday.io community itself a badge: a 2.4" color TFT display, WS2812B RGB LEDs, capacitive touch buttons, IR transmit/receive, and a small speaker, built around an Atmel SAM D21 (later revisions moved toward the radio-integrated SAM R21). Badges were meant to form a "Sub-Etha" mesh network so wearers at the same event could exchange messages with each other, with a stretch goal of bridging that mesh to the wider internet.

The project targeted a $35 bill-of-materials cost per badge and a 3.7V 2500mAh LiPo for roughly a day of runtime, with hardware designed in KiCad and published on GitHub (Hack-a-Day/HaDge_HW). It was conceived as a badge for Hackaday community members generally, to be brought along to whichever conferences Hackaday attended, rather than as the official badge of one specific convention. As of the most detailed public writeup (October 2015), the project was still at the design/prototyping stage, including a separate SAM R21-based "HACK" development kit meant to let the software team start writing code before hardware was finalized. No source found confirms a final production run, a specific event where finished units were actually worn, or that firmware development was completed.

## Make your own

Hardware design files (KiCad) are published at https://github.com/Hack-a-Day/HaDge_HW. No firmware repository URL could be confirmed during this research pass, though the project page references companion HaDge_FW (firmware) and HaDge_SW (software) repositories under the same GitHub organization.
