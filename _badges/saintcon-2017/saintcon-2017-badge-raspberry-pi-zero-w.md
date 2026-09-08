---
title: SAINTCON 2017 Badge (Raspberry Pi Zero W)
id: saintcon-2017-saintcon-2017-badge-raspberry-pi-zero-w
layout: badge
parent: Saintcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2017
year: 2017
makers:
- name: lukejenkins / SAINTCON
  url: https://github.com/lukejenkins
summary: The official SAINTCON 2017 attendee badge, built around a Raspberry Pi Zero W with a 2.8" TFT touchscreen and SNES-style controls.
functions: Boots a custom badge OS image off a microSD card; doubles as a general-purpose Linux/Pi handheld, and the official docs note it can be re-flashed into a RetroPie emulation handheld after the con.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - console
tech:
  mcu: Raspberry Pi Zero W
  leds:
    count: 2
    type: null
    note: Two status LEDs, reserved (per the official badge spec page).
  display: 2.8" TFT LCD, 320x240 (Adafruit PiTFT Plus style)
  connectivity:
  - wifi
  - bluetooth
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
  where: Distributed to SAINTCON 2017 attendees (Provo, Utah, October 10-13, 2017); the official page describes stock as limited to the organizers' attendance forecast, with early registration recommended to secure one.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/lukejenkins/SAINTCON-2017-Badge
  firmware_url: http://badge2017.saintcon.org/images/latest.img.xz
  eda_tool: null
links:
- label: github.com/lukejenkins/SAINTCON-2017-Badge
  url: https://github.com/lukejenkins/SAINTCON-2017-Badge
  kind: repo
- label: saintcon.gitlab.io/Badge2017
  url: http://saintcon.gitlab.io/Badge2017/
  kind: doc
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2017/badge
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2017/badge/
  kind: website
- label: badge.gallery/badges/saintcon-2017-raspberry-pi-badge
  url: https://badge.gallery/badges/saintcon-2017-raspberry-pi-badge
  kind: website
- label: github.com/lukejenkins/minibadge (MiniBadge spec)
  url: https://github.com/lukejenkins/minibadge
  kind: repo
images:
- file: assets/images/badges/saintcon-2017/saintcon-2017-badge-raspberry-pi-zero-w/80624e1fb3.jpg
  source: "http://saintcon.gitlab.io/Badge2017/"
  credit: "SAINTCON / lukejenkins"
  caption: "Assembled SAINTCON 2017 badge (screen not yet attached)"
- file: assets/images/badges/saintcon-2017/saintcon-2017-badge-raspberry-pi-zero-w/e5b8226b97.jpg
  source: "http://saintcon.gitlab.io/Badge2017/"
  credit: "SAINTCON / lukejenkins"
  caption: "SAINTCON 2017 badge assembly step"
contact: {}
notes:
- Official SAINTCON 2017 attendee badge built around a Raspberry Pi Zero W, 2.8-inch TFT display, SNES-style buttons and MiniBadge support; hardware files by lukejenkins, not yet in the archive. Found by the event-year sweep, task saintcon-2017.
status: listed
sources:
- kind: url
  url: https://github.com/lukejenkins/SAINTCON-2017-Badge
  title: SAINTCON 2017 Badge (Raspberry Pi Zero W)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2017); event read as ''saintcon-2017''.'
- kind: url
  url: https://github.com/lukejenkins/SAINTCON-2017-Badge
  title: lukejenkins/SAINTCON-2017-Badge
  accessed: '2026-09-08'
  note: 'Confirms maker (Luke Jenkins), MiniBadge-spec compatibility, and that Eagle schematic/board files (.sch/.brd) and a PDF schematic are published in the repo.'
- kind: url
  url: http://saintcon.gitlab.io/Badge2017/
  title: SaintCon 2017 Badge assembly guide
  accessed: '2026-09-08'
  note: 'Official assembly instructions: Raspberry Pi + PiTFT orientation, ~20 minute build time, badge OS image (latest.img.xz) flashed with Etcher, and a note that the badge could be converted to RetroPie after the con.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2017/badge/
  title: SAINTCON 2017 official badge page (archived)
  accessed: '2026-09-08'
  note: 'Archived organizer copy: Raspberry Pi Zero W, 1GHz single-core CPU, 512MB RAM, 16GB microSD, 2.8" 240x320 color display, SNES-style buttons, 2 reserved status LEDs, 802.11b/g/n + Bluetooth 4.1 LE, USB port, PCB 5.7"x5"; notes stock was limited to expected attendance.'
- kind: url
  url: https://badge.gallery/badges/saintcon-2017-raspberry-pi-badge
  title: badge.gallery — SAINTCON 2017 Raspberry Pi Badge
  accessed: '2026-09-08'
  note: 'Third-party catalog entry; credits design to "Jup1t3r" rather than lukejenkins and could not find a public source repo (unaware of the lukejenkins GitHub repo). Treated as lower-confidence than the primary sources above.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: >-
    Fact-check pass 2026-09-08: re-fetched all four cited sources
    (lukejenkins/SAINTCON-2017-Badge repo, saintcon.gitlab.io/Badge2017
    assembly guide, the archived official saintcon.zip badge page, and
    badge.gallery) plus both saved photos. Every non-empty field and every
    factual sentence in the summary/functions/body/tech/get_one/make_your_own
    fields checked out against these sources: Pi Zero W + 2.8" 320x240 TFT +
    SNES buttons + 2 reserved LEDs + wifi/BLE 4.1/USB + ~5.7"x5" PCB, Eagle
    schematic/board files and PDF schematic in the GitHub repo, MiniBadge
    spec compatibility, Etcher-flashed latest.img.xz image, the board-
    orientation warning quote, the RetroPie-after-the-con note, and the
    limited-stock/attendance-forecast distribution note. Both saved photos
    show the actual yellow SAINTCON badge PCB with Pi Zero W and SNES-style
    buttons, matching their captions and source page. Price and quantity
    made were never published anywhere found; get_one.quantity/price left
    empty, correctly. badge.gallery attributes the design to "Jup1t3r"
    instead of lukejenkins/SAINTCON, but the GitHub repo and SAINTCON's own
    gitlab.io docs consistently credit lukejenkins, so that name is kept as
    primary maker and the discrepancy is noted here rather than guessed at.
    No corrections were needed. Confidence held at medium (not high) because
    whether the PCB design itself was fully custom versus built on an
    off-the-shelf carrier board was never independently confirmed beyond the
    repo's own files.
last_modified_date: '2026-09-08'
---

The SAINTCON 2017 badge was the official attendee badge for SAINTCON, the Utah-based security conference (SAINTCON 2017 ran October 10-13, 2017 in Provo). Rather than a typical PCB-with-blinkies badge, it was built around a Raspberry Pi Zero W paired with a 2.8" 320x240 TFT touchscreen (PiTFT Plus style) and a SNES-style D-pad and button layout, turning the badge into a small handheld computer running a custom Linux image off a microSD card. The design work is credited to Luke Jenkins (lukejenkins) working with the SAINTCON organizing team, and the badge doubled as a platform for on-site challenges while attendees registered.

Attendees flashed or received the official badge OS image (`latest.img.xz`, distributed via Etcher across Windows/Mac/Linux) and followed a documented assembly process pairing the Pi Zero W with the display and controller board; the official guide warns that getting the board orientation wrong "will mean your badge will not function without a lot of pain and suffering." After the conference, organizers noted the hardware could be repurposed into a RetroPie emulation handheld. Stock was described as limited to the organizers' attendance forecast, with early registration encouraged to guarantee one; no price or exact production quantity was found in the sources checked.

## Make your own

Hardware files (Eagle schematic and board layout, plus a PDF schematic) are published in lukejenkins' `SAINTCON-2017-Badge` GitHub repository, and the badge follows the MiniBadge header spec documented in the companion `lukejenkins/minibadge` repo, meaning third-party minibadges built to that spec could plug into it. The badge OS image itself is linked from the official SAINTCON 2017 badge site rather than bundled in the hardware repo.
