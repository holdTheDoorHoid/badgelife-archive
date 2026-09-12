---
title: HeartyBadge
id: dc26-heartybadge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Ashwin K Whitchurch
  url: https://hackaday.io/whitchurch
- name: Archana Vijayan
  url: https://hackaday.io/Archie07
summary: A single-lead ECG and heart-rate-variability monitor built into a DEF CON 26 conference badge, based on ProtoCentral's HeartyPatch design.
functions: Records a single-lead ECG and derives heart-rate variability; pinching the two gold-plated electrode pads between thumb and forefinger triggers a heart-shaped animation on the LED matrix in time with the wearer's heartbeat.
look:
  colors:
  - black
  - gold
  shape: heart
  themes:
  - heart
  - health
  - wearable
tech:
  mcu: ESP32
  leds:
    count: 144
    type: APA102
    note: most of the LEDs are arranged in a matrix that displays a heart animation
  display: LED matrix
  connectivity:
  - wifi
  - ble
  - usb
  battery: Li-Ion, onboard charging
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '2'
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/Protocentral/HeartyBadge
  firmware_url: https://github.com/Protocentral/HeartyBadge
links:
- label: hackaday.io/project/160846-heartybadge
  url: https://hackaday.io/project/160846-heartybadge
  kind: hackaday
- label: github.com/Protocentral/HeartyBadge
  url: https://github.com/Protocentral/HeartyBadge
  kind: repo
- label: 'Hackaday: All The Badges Of DEF CON 26 (vol 3)'
  url: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  kind: article
images:
- file: assets/images/badges/dc26/heartybadge/efc40991c4.jpg
  source: https://hackaday.io/project/160846-heartybadge
  credit: Ashwin K Whitchurch / Protocentral
  caption: HeartyBadge PCB badge front
- file: assets/images/badges/dc26/heartybadge/2ce6e536b9.gif
  source: https://hackaday.io/project/160846-heartybadge
  credit: Ashwin K Whitchurch / Protocentral
  caption: HeartyBadge LED heart animation
contact: {}
notes:
- Sheet listed event as unknown; sources confirm it was built for DEF CON 26 (2018).
status: released
sources:
- kind: url
  url: https://hackaday.io/project/160846-heartybadge
  title: HeartyBadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://github.com/Protocentral/HeartyBadge
  title: Protocentral/HeartyBadge on GitHub
  accessed: '2026-09-07'
  note: Confirms open-source hardware and firmware (GPL-3.0), chip/LED/battery details.
- kind: url
  url: https://hackaday.com/2018/08/29/all-the-badges-of-def-con-26-vol-3/
  title: All The Badges Of DEF CON 26 (vol 3) | Hackaday
  accessed: '2026-09-07'
  note: Confirms only two badges were made, worn by the maker at DEF CON 26 Breakfast meetup, describes the pinch-to-detect-heartbeat interaction.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price and formal distribution not found; only two units were made by the maker for personal/demo use at DEF CON 26 rather than sold or given out widely, so availability is set to not_released. Repo does not state which EDA tool was used, left null. sao_version not applicable/unknown since this is a standalone badge, not confirmed to carry an SAO header.
last_modified_date: '2026-09-11'
redirect_from:
- /badges/other/heartybadge/
model:
  file: assets/models/dc26/heartybadge.glb
  method: kicad
  source_file: pc_badge_hrv.brd
  generated: '2026-09-11'
  bytes: 661132
---

HeartyBadge is a conference badge built by Ashwin K. Whitchurch of ProtoCentral (with Archana Vijayan) for DEF CON 26 in 2018, adapting the pair's existing HeartyPatch wearable ECG design into badge form just before the conference. It combines a MAX30003 single-lead ECG front end, an ESP32 with Wi-Fi and Bluetooth, and 144 APA102 RGB LEDs arranged mostly as a matrix. Two gold-plated pads etched into the PCB serve as electrodes: pinching them between thumb and forefinger lets the badge pick up the wearer's heartbeat and animate a heart shape on the LED matrix in time with it.

Only two HeartyBadges were built, and Whitchurch wore one himself at the DEF CON 26 "Breakfast at DEF CON" meetup while at the conference to present ProtoCentral's HealthyPi open-source patient monitor. The badge was not sold or distributed as a giveaway; it functioned as a personal demo piece and a showcase of the HeartyPatch technology in wearable-badge form.

## Make your own

Both the hardware design and firmware are published on GitHub under the GPL-3.0 license, in the `hardware` and `firmware/hrv_badge_ble` folders of the repository. The firmware targets the ESP32 and includes the ECG/HRV signal processing and LED-matrix animation logic; no separate BOM, Gerbers, or EDA-tool file format are called out on the repository's front page.
