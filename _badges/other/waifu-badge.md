---
title: Waifu Badge
id: other-waifu-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: Waifus4Lifu
summary: A Raspberry Pi-based electronic badge made by the Waifus4Lifu team for QuakeCon 2018, with a touchscreen, vibration motor, and a Bluetooth "hacking" game between badges.
functions: 'Displays looping waifu-themed video animations on an LCD; a touchscreen divided into quadrants drives menu navigation; a Bluetooth iBeacon scanner lets badges detect and "hack" each other, triggering a hack animation and vibration-motor feedback; also launches a RetroArch/EmulationStation front end for playing retro games, and can run an image/video slideshow.'
look:
  colors: []
  shape: null
  themes:
  - anime
  - pop culture
tech:
  mcu: Raspberry Pi
  leds: null
  display: LCD (touchscreen)
  connectivity:
  - bluetooth
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Waifus4Lifu/waifu-badge
  eda_tool: null
links:
- label: github.com/Waifus4Lifu/waifu-badge
  url: https://github.com/Waifus4Lifu/waifu-badge
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/Waifus4Lifu/waifu-badge
  title: Waifus4Lifu/waifu-badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/Waifus4Lifu/waifu-badge/master/README.md
  title: 'qc-badge-2018 README'
  accessed: '2026-09-07'
  note: 'Confirms the repo is for the "Waifus 4 Lifu QuakeCon 2018 badges," with lcd/ and scripts/ folders.'
- kind: url
  url: https://github.com/Waifus4Lifu/waifu-badge/blob/master/mcp.py
  title: mcp.py
  accessed: '2026-09-07'
  note: 'Main control script: reveals Raspberry Pi GPIO vibration motor, evdev touchscreen input, beacontools Bluetooth iBeacon scanning for a badge-hacking mechanic, and an EmulationStation game-launcher handler.'
- kind: url
  url: https://github.com/Waifus4Lifu/waifu-badge/tree/master/media
  title: 'waifu-badge media folder'
  accessed: '2026-09-07'
  note: 'Lists media assets (hacking.mp4, vibe.mp4, vibe_active.mp4, waifu_hack.mp4, waifus_animation.mp4) played on the badge screen; no static photos of the physical badge found.'
- kind: url
  url: https://github.com/Waifus4Lifu/waifu-badge/commits/master
  title: 'waifu-badge commit history'
  accessed: '2026-09-07'
  note: 'Commits run from April to August 2018, consistent with a QuakeCon 2018 (August) badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    This is the software/firmware repo for the "Waifus 4 Lifu" QuakeCon 2018 badge, run on a
    Raspberry Pi with a touchscreen LCD. No dedicated event id exists for QuakeCon in this
    archive's events.yml, so event is left as "other" — this was made for QuakeCon 2018, not a
    hacker con. Could not find price, quantity made, availability, a hardware/PCB repo (this repo
    is scripts and vendor LCD files only, marked "partial" open source), or any photo of the
    physical badge itself — the repo's media/ folder holds only mp4 animation clips, not static
    images, so no images were saved. No maker's own page (Twitter/Hackaday) was found beyond the
    GitHub repo.
last_modified_date: '2026-09-07'
---

The Waifu Badge is an electronic badge made by a team calling themselves "Waifus4Lifu" for QuakeCon 2018. Rather than a small standalone PCB, it runs on a Raspberry Pi driving a touchscreen LCD, playing looping anime-style ("waifu") video animations as its idle display.

Its standout feature is a Bluetooth-based social mechanic: the badge scans for iBeacon signals from other badges nearby and can be "hacked," which triggers a hack animation on screen along with feedback from an onboard vibration motor. The touchscreen is split into quadrants for menu navigation, and the badge can also launch an EmulationStation-based retro game front end or run an image/video slideshow, making it as much a small handheld console as a badge.

The public GitHub repository holds the control scripts (a Python daemon, `mcp.py`) and vendor-provided LCD driver files, but not a hardware/PCB design, so it is only partially open source. No information on price, quantity produced, or distribution was found; QuakeCon does not currently have a matching event entry in this archive, so the record is filed under "other" pending one being added.
