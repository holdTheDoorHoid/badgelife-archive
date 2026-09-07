---
title: bsidesif-badge-2022
id: other-bsidesif-badge-2022
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2022
makers:
- name: wrigjl
  url: https://github.com/wrigjl
summary: 'A WiFi-connected electronic badge built for BSides Iowa 2022, with three NeoPixel LEDs whose colors can be set locally or synced from a network coordination service.'
functions: 'Cycles through random colors on three onboard NeoPixels, with a pushbutton input; polls a network API roughly every 30 seconds so LED colors can be driven centrally during a group/event activity rather than only locally.'
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
tech:
  mcu: null
  leds:
    count: 3
    type: NeoPixel
    note: 'Driven from Pin(4) via MicroPython neopixel module; brightness reduced in firmware.'
  display: none
  connectivity:
  - wifi
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
  firmware_url: https://github.com/wrigjl/bsidesif-badge-2022
  eda_tool: null
links:
- label: github.com/wrigjl/bsidesif-badge-2022
  url: https://github.com/wrigjl/bsidesif-badge-2022
  kind: repo
images: []
contact: {}
notes:
- "Made for BSides Iowa (event site says 'BSidesIowa'), held April 23, 2022 at Grand View University. No matching event id exists yet in _data/events.yml (only bsides-orlando, bsides-jacksonville, bsides-rochester, bsidesdfw, etc. are defined), so this entry stays filed under 'other'; a bsides-iowa-2022 event should be added."
status: listed
sources:
- kind: url
  url: https://github.com/wrigjl/bsidesif-badge-2022
  title: bsidesif-badge-2022
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides Iowa (IF) 2022''.'
- kind: url
  url: https://raw.githubusercontent.com/wrigjl/bsidesif-badge-2022/main/README.md
  title: 'bsidesif-badge-2022 README'
  accessed: '2026-09-07'
  note: 'Confirms the project is firmware for a WiFi-connected badge ("All the badge things"); MicroPython, requires SSID/PASSWORD secrets file, code pushed via push.sh.'
- kind: url
  url: https://raw.githubusercontent.com/wrigjl/bsidesif-badge-2022/main/pixel.py
  title: 'bsidesif-badge-2022 pixel.py'
  accessed: '2026-09-07'
  note: '3 NeoPixels on Pin(4); random-color cycling logic and color palette.'
- kind: url
  url: https://raw.githubusercontent.com/wrigjl/bsidesif-badge-2022/main/main.py
  title: 'bsidesif-badge-2022 main.py'
  accessed: '2026-09-07'
  note: 'uasyncio-based main loop; pushbutton class; polls a Coms/API object every 30s to sync LED state with a server, suggesting a group/event-wide synchronized light effect.'
- kind: url
  url: https://x.com/BSidesIowa/status/1511121618445213699
  title: 'BSidesIowa tweet'
  accessed: '2026-09-07'
  note: 'Confirmed as the BSides Iowa conference account; used to corroborate the "BSidesIF" name refers to BSides Iowa, not another BSides chapter.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo contains firmware only (MicroPython) — no schematic, PCB, gerbers, or BOM found, so mcu/battery/price/quantity/availability/colors/shape are left empty rather than guessed. The MicroPython network/neopixel/machine.Pin API stack implies an ESP32-class WiFi microcontroller, but no source states the exact chip, so tech.mcu is left null. No photos of the physical badge were found on GitHub, X/Twitter, or via web search.'
last_modified_date: '2026-09-07'
---

This badge was built for BSides Iowa 2022 (held April 23, 2022 at Grand View University) by GitHub user wrigjl. The published repository, named "bsidesif-badge-2022," holds only the badge's MicroPython firmware: boot and main loops built on `uasyncio`, a debounced pushbutton driver, and a `pixel.py` module that drives three NeoPixel LEDs wired to Pin 4.

The firmware connects to WiFi (credentials supplied via a local `secrets.py` file kept out of version control) and polls a small API roughly every 30 seconds to fetch shared LED-color state, alongside locally generated random colors. That structure — a badge that normally free-runs its own color pattern but can be overridden by an "event_active" signal from a network service — points to a coordinated group light show or similar shared activity rather than a purely standalone badge, though no announcement or write-up describing that activity was found.

No hardware files (schematic, PCB layout, BOM, or gerbers) are in the repository, and no photos of the assembled badge turned up on GitHub, the BSides Iowa social accounts, or general web search, so physical details (MCU part number, board shape/color, battery, price, and quantity made) could not be confirmed and are left blank. BSides Iowa does not yet have an entry in this archive's events list, so the record stays filed under "other" pending that addition.
