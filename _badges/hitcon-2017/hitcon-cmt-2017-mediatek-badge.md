---
title: HITCON CMT 2017 MediaTek Badge
id: hitcon-2017-hitcon-cmt-2017-mediatek-badge
layout: badge
parent: Hitcon Cmt 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitcon-2017
year: 2017
makers:
- name: HITCON / MediaTek (HITCON Activity Team)
summary: An electronic conference badge built around a MediaTek MT7697 SoC, made for HITCON CMT 2017's "HITCON Badge Challenges."
functions: Two BLE-based challenges - a Pokemon-style "catch all the Hackermon" game and a Snake game (hold RIGHT + X + B to start, score above 249 to earn a reward) - plus a customizable Bluetooth name (up to 15 ASCII characters). Top scorers won tickets to HITCON CMT 2018.
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
  - wearable
tech:
  mcu: MediaTek MT7697 (ARM Cortex-M4)
  leds: null
  display: LED display
  connectivity:
  - wifi
  - ble
  - ir
  battery: batteries with power switch; microUSB usable as an alternate power source
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  - purchase
  where: Given to HITCON CMT 2017 Premium Pass holders as a deluxe badge, with additional units sold to attendees during the conference (Aug 25-26, 2017, Academia Sinica, Taipei).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/x43x61x69/HITCON-Badge
  eda_tool: null
links:
- label: badge.gallery/badges/hitcon-cmt-2017-mediatek-badge
  url: https://badge.gallery/badges/hitcon-cmt-2017-mediatek-badge
  kind: website
- label: HITCON CMT 2017 event page
  url: https://hitcon.org/2017/CMT/events
  kind: website
- label: 'GitHub: x43x61x69/HITCON-Badge (firmware/source)'
  url: https://github.com/x43x61x69/HITCON-Badge
  kind: repo
- label: 2017 HITCON Badge - Play Hackermon via BLE (demo video)
  url: https://www.youtube.com/watch?v=K_65732qKWM
  kind: video
images: []
contact: {}
notes:
- MediaTek-chipset electronic badge with Wi-Fi, BLE, joystick, IR and LED display used for the Hackermon/Snake badge challenges. Found by the event-year sweep, task con-hitcon.
- 'The maker''s own GitHub repo calls the hardware the "HITCON 2017 Electronic Badge (HEB)"; kept the sweep''s "HITCON CMT 2017 MediaTek Badge" title since that matches the badge.gallery entry and event branding.'
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/hitcon-cmt-2017-mediatek-badge
  title: HITCON CMT 2017 MediaTek Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-hitcon); event read as ''HITCON CMT 2017''.'
- kind: url
  url: https://hitcon.org/2017/CMT/events
  title: HITCON CMT 2017 - Mission Code - HITCON Badge Challenges
  accessed: '2026-09-08'
  note: 'Official event page (via search snippet, page itself blocked by Cloudflare): confirms MediaTek chipset, Wi-Fi/BLE/game-controller/IR/LED display, and that 2 badge challenges were run.'
- kind: url
  url: https://github.com/x43x61x69/HITCON-Badge
  title: 'GitHub - x43x61x69/HITCON-Badge: HITCON Badge Related Files'
  accessed: '2026-09-08'
  note: Maker's own repo - confirms MT7697 SoC, joystick/button layout, USR LED, BLE name config, Snake game trigger and score threshold, GPL v3 firmware/source.
- kind: url
  url: https://www.youtube.com/watch?v=K_65732qKWM
  title: 2017 HITCON Badge Challenges - Play Hackermon via BLE (DEMO)
  accessed: '2026-09-08'
  note: Demo video confirming the Hackermon-catching BLE challenge.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'No confirmed photo of the physical badge was found (badge.gallery and the GitHub repo carry no images of the hardware itself; only ASCII-art diagrams in the README), so images stayed empty. Exact LED count/type, display size/technology, hardware schematic/PCB files, price, and quantity made are not documented anywhere found. The official hitcon.org event page could not be fetched directly (Cloudflare challenge) - facts from it are via search-result snippets and are consistent with badge.gallery and the GitHub repo.'
last_modified_date: '2026-09-08'
---

The HITCON CMT 2017 MediaTek Badge - called the "HITCON 2017 Electronic Badge (HEB)" in its own firmware repo - was the electronic badge for HITCON Community 2017 (August 25-26, 2017, Academia Sinica, Taipei), built around a MediaTek MT7697 Wi-Fi/BLE SoC. It shipped as a deluxe item for Premium Pass holders, with extra units sold to other attendees during the event.

The badge drove that year's "HITCON Badge Challenges": a Pokemon-style game where players used Bluetooth Low Energy to "catch" Hackermon, and a built-in Snake game (started by holding RIGHT + X + B on the badge's directional joystick and action buttons) that rewarded scores over 249. High scorers in the challenges won tickets to the following year's HITCON CMT. The badge also let owners set a custom Bluetooth-advertised name of up to 15 ASCII characters, revealed along with a configuration prefix via a dedicated USR button. It ran on batteries (with a power switch) or microUSB power, and carried infrared alongside its Wi-Fi/BLE radios and an onboard LED display.

## Make your own

The firmware and related source/solution files were published on GitHub by developer x43x61x69 under GPL v3 (https://github.com/x43x61x69/HITCON-Badge). No hardware design files (schematic, PCB, BOM) were found alongside it, so the hardware side is not confirmed open source.
