---
title: SecKC Badge (PCB devboard)
id: dc25-seckc-badge-pcb-devboard
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: SecKC (Kansas City infosec meetup)
  url: https://seckc.org/
summary: A dev-board-style hardware badge built by SecKC (the Kansas City infosec meetup) for DEF CON 25, based around an nRF module from SparkFun.
functions: 'Intended as a hackable devboard; attendees built on top of it, including one build that turned it into a rotary-dial "cellphone."'
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'preordered 50, ~60 built'
  availability: unknown
  distribution:
  - preorder
  where: Preordered by SecKC members ahead of DEF CON 25; demand exceeded supply, so the group also handed out edge-lit acrylic badges as a backup.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  kind: website
images:
  - file: assets/images/badges/dc25/seckc-badge-pcb-devboard/9c3e170f57.jpg
    source: "https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/"
    credit: "Hackaday"
    caption: "SecKC devboard badge, front"
  - file: assets/images/badges/dc25/seckc-badge-pcb-devboard/14699c1bea.jpg
    source: "https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/"
    credit: "Hackaday"
    caption: "SecKC devboard badge, back"
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- This appears to be a duplicate of dc25-seckc-badge, which already carries fuller, sourced detail (ESP32/OLED, GitHub repo, distribution) confirmed against the same Hackaday article and the SecKC GitHub org. Left as a stub-level duplicate rather than merged, per the one-entry-per-task rule.
status: listed
sources:
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: SecKC Badge (PCB devboard)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: All The Hardware Badges Of DEF CON 25 (Hackaday)
  accessed: '2026-09-10'
  note: Confirmed SecKC devboard exists, maker, nRF/SparkFun basis, preorder/build quantities (50 preordered, ~60 built), and the acrylic-badge fallback. Source of the two images.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Only source found is the same Hackaday article already on the sheet; no maker storefront, repo link, or separate confirmation page was located for this specific entry. Likely the same physical badge as dc25-seckc-badge (see duplicate_of), which has a GitHub repo and more complete tech specs sourced separately — those were not copied into this entry since they weren't independently re-verified here. tech.mcu/leds/display and make_your_own fields left empty because this entry's own sources (the Hackaday article) don't spell out the chip or LED/display specifics precisely enough to state with confidence.
last_modified_date: '2026-09-10'
---

SecKC, the Kansas City infosec meetup, built this devboard-style badge for DEF CON 25 (2017), designing it around an nRF module from SparkFun. The group took preorders for 50 boards and ended up building around 60, but demand outstripped supply; when they couldn't get additional boards built in time, they handed out edge-lit acrylic badges as a stopgap for members who missed out on the PCB (see the separate SecKC Acrylic Badge entry).

The badge was built to be hacked on, and Hackaday's DEF CON 25 badge roundup notes that attendees took it further, with one build reworking it into a rotary-dial "cellphone."

This entry appears to describe the same physical badge as `dc25-seckc-badge`, which carries a fuller, independently-sourced write-up (SparkFun ESP32 Thing, OLED display, GitHub repo). That detail was not copied over here since it wasn't re-confirmed against this entry's own sources.
