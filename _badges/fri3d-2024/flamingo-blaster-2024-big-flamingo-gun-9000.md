---
title: Flamingo (Blaster 2024 / "Big Flamingo Gun 9000")
id: fri3d-2024-flamingo-blaster-2024-big-flamingo-gun-9000
layout: badge
parent: Fri3D 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: fri3d-2024
year: 2024
makers:
- name: Fri3d Camp
  url: https://github.com/Fri3dCamp
summary: 'An infrared blaster gun accessory for the Fri3d Camp 2024 badge: players shoot an IR beam and use two IR receivers to detect hits from other players.'
functions: 'IR "shoot the other team" game: trigger pushbutton fires an IR pulse from the front-mounted IR LED, two IR receivers detect incoming hits, a team-selector switch sets faction, four WS2812 LEDs give color feedback, and a buzzer sounds on hits. Connects to the main Fri3d 2024 badge over the badge-link cable.'
look:
  colors: []
  shape: null
  themes:
  - game
  - hardware tool
tech:
  mcu: CH32V203G6U6 (via LANA-TNY-01 module)
  leds:
    count: 4
    type: WS2812
    note: RGB status/feedback LEDs
  display: none
  connectivity:
  - ir
  - uart
  battery: powered by host badge (badge-link cable)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/Fri3dCamp/blaster_2024
  firmware_url: https://github.com/Fri3dCamp/blaster_2024
  eda_tool: null
  license: Apache 2.0
  notes: Repo contains design files, production files and firmware sources for both the 2024 and earlier 2022 blaster hardware. Firmware is C, buildable with PlatformIO, Embeetle IDE, or MounRiver Studio.
links:
- label: fri3dcamp.github.io/badge_2024/en/flamingo
  url: https://fri3dcamp.github.io/badge_2024/en/flamingo/
  kind: website
- label: Fri3dCamp/blaster_2024
  url: https://github.com/Fri3dCamp/blaster_2024
  kind: repo
images:
- file: assets/images/badges/fri3d-2024/flamingo-blaster-2024-big-flamingo-gun-9000/27531723a0.jpg
  source: https://fri3dcamp.github.io/badge_2024/en/flamingo/
  credit: Fri3d Camp
  caption: Fully assembled Big Flamingo Gun 9000 blaster
- file: assets/images/badges/fri3d-2024/flamingo-blaster-2024-big-flamingo-gun-9000/a788ed4c14.jpg
  source: https://fri3dcamp.github.io/badge_2024/en/flamingo/
  credit: Fri3d Camp
  caption: Blaster kit parts before assembly
contact: {}
notes:
- IR blaster-gun add-on for the Fri3d Camp 2024 badge, built with badge-link cable, IR receivers and WS2812 LEDs. Found by the event-year sweep, task fri3d.
- Maker's own assembly guide names it "Big Flamingo Gun 9000" and files it under the "Flamingo" section of the 2024 badge docs; the sheet's title matches, kept as-is.
status: listed
sources:
- kind: url
  url: https://fri3dcamp.github.io/badge_2024/en/flamingo/
  title: Flamingo (Blaster 2024 / "Big Flamingo Gun 9000")
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:fri3d); event read as ''fri3d-2024''.'
- kind: url
  url: https://fri3dcamp.github.io/badge_2024/en/flamingo/
  title: Flamingo assembly guide
  accessed: '2026-09-08'
  note: Confirmed item exists, name, chip (LANA-TNY module / CH32V203), LED count (4x WS2812), IR LED + 2 IR receivers, buzzer, team switch, trigger; images fetched from this page.
- kind: url
  url: https://github.com/Fri3dCamp/blaster_2024
  title: Fri3dCamp/blaster_2024
  accessed: '2026-09-08'
  note: Confirmed open-source hardware+firmware (Apache 2.0), repo covers both 2024 and 2022 blaster hardware revisions, MCU is CH32V203G6U6 via the LANA-TNY-01 module.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker's own build page and GitHub repo confirm the item, its function, and hardware/firmware openness. Price, quantity made, and availability were not stated anywhere found and are left empty. PCB colors/shape were not described on the pages seen (only assembly photos of populated boards, not a clean top-down shot with color info called out) and are left empty rather than guessed.
last_modified_date: '2026-09-10'
model:
  file: assets/models/fri3d-2024/flamingo-blaster-2024-big-flamingo-gun-9000.glb
  method: gerber
  source_file: Hardware/Fri3d_2024_Blaster_00/OUTPUT/Gerber
  generated: '2026-09-10'
  bytes: 209228
  size_mm:
  - 131.2
  - 140.1
  note: The published files have no board outline, so the model is shown on a rectangular board.
---

The Big Flamingo Gun 9000, listed on the Fri3d Camp 2024 badge site as "Flamingo," is an infrared blaster accessory built to plug into the Fri3d Camp 2024 main badge over its badge-link cable. Players use the trigger pushbutton to fire an IR pulse at opponents; two onboard IR receivers detect incoming hits from other blasters, a team-selector switch sets which faction a player belongs to, and four WS2812 RGB LEDs plus a buzzer give visual and audio feedback on hits and game state.

The blaster is built around a LANA-TNY-01 module carrying a CH32V203G6U6 RISC-V microcontroller from WCH. Fri3d Camp publishes the hardware design files, production files, and firmware source for the 2024 blaster (alongside an earlier 2022 hardware revision) in the `Fri3dCamp/blaster_2024` GitHub repository under the Apache 2.0 license; the firmware is written in C and can be built with PlatformIO, Embeetle IDE, or MounRiver Studio, with badge-side control available through a MicroPython driver.

No pricing, production quantity, or storefront availability was found on the maker's build page or in the repository, so those fields are left blank rather than guessed.
