---
title: Metro-Addon (Vagoncito de Metro SAO)
id: bsides-cdmx-2025-metro-addon-vagoncito-de-metro-sao
layout: badge
parent: BSides Cdmx 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: bsides-cdmx-2025
year: 2025
makers:
- name: Electronic Cats
  url: https://electroniccats.com/
summary: A shitty-addon shaped like a Mexico City Metro train car, made to plug into Electronic Cats' BSides CDMX 2025 badge.
functions: Three discrete LEDs blink through scripted sequences (a light-up window sequence and a flashing "windows" pattern) driven directly by GPIO pins, no addressable LEDs involved.
look:
  colors: []
  shape: train
  themes:
  - transit
tech:
  mcu: Puya PY32F002A
  leds:
    count: 3
    type: discrete
    note: Driven directly by MCU GPIO pins (PA1, PA3, PA4) in hard-coded blink sequences, not addressable/Neopixel like the main badge.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ElectronicCats/Badge-bsides-cdmx-2025/tree/main/hardware/Metro-Addon
  firmware_url: https://github.com/ElectronicCats/Badge-bsides-cdmx-2025/tree/main/hardware/Metro-Addon/firmware
  eda_tool: KiCad
links:
- label: github.com/ElectronicCats/Badge-bsides-cdmx-2025/tree/main/hardware/Metro-Addon
  url: https://github.com/ElectronicCats/Badge-bsides-cdmx-2025/tree/main/hardware/Metro-Addon
  kind: repo
- label: Badge-bsides-cdmx-2025 root README
  url: https://github.com/ElectronicCats/Badge-bsides-cdmx-2025
  kind: repo
images: []
contact: {}
notes:
- Sweep's original wording ("Metro-Addon (Vagoncito de Metro SAO)") matches the repo folder name; no maker page uses a different title, so the title is unchanged.
status: released
sources:
- kind: url
  url: https://github.com/ElectronicCats/Badge-bsides-cdmx-2025/tree/main/hardware/Metro-Addon
  title: Metro-Addon (Vagoncito de Metro SAO)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://raw.githubusercontent.com/ElectronicCats/Badge-bsides-cdmx-2025/main/README.md
  title: Badge-bsides-cdmx-2025 root README
  accessed: '2026-09-10'
  note: Confirms the addon is a "Shitty Addon" for Electronic Cats' BSides CDMX 2025 badge; main badge chip/LED/display info (not this addon's).
- kind: url
  url: https://raw.githubusercontent.com/ElectronicCats/Badge-bsides-cdmx-2025/main/hardware/Metro-Addon/firmware/README.md
  title: Metro-Addon firmware README
  accessed: '2026-09-10'
  note: Gives the addon's own MCU (Puya PY32F002A) and notes it was designed for HackGDL.
- kind: url
  url: https://raw.githubusercontent.com/ElectronicCats/Badge-bsides-cdmx-2025/main/hardware/Metro-Addon/firmware/User/main.c
  title: Metro-Addon firmware main.c
  accessed: '2026-09-10'
  note: Shows 3 discrete LEDs on GPIO PA1/PA3/PA4 driven in hard-coded blink sequences (train-window-light effect); no display or wireless hardware referenced.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: No standalone README or product photo exists for the Metro-Addon folder itself; facts here come from the repo's file listing, the addon's own firmware/User/main.c source, and the parent badge's root README (which describes the main badge, not this addon). Price, quantity, and availability were not published anywhere found. The firmware README credits the design "for HackGDL" (a separate Guadalajara-area Electronic Cats event/meetup), suggesting the addon design may have originated there before being reused for BSides CDMX 2025; not confirmed further. No maker photo of the assembled addon was found, only KiCad-exported SVG/Gerber-style files, so no images were saved.
last_modified_date: '2026-09-10'
---

The Metro-Addon, nicknamed the "Vagoncito de Metro" (little metro car), is a shitty-addon (SAO) that Electronic Cats designed to plug into their BSides CDMX 2025 conference badge. Where the main badge runs a Puya PY32F030 with addressable Neopixels and an OLED display, the addon carries its own smaller Puya PY32F002A microcontroller and three plain (non-addressable) LEDs wired straight to GPIO pins, which the firmware blinks through scripted patterns meant to look like a train car's windows lighting up in sequence.

Hardware (KiCad schematic, PCB, and manufacturing files) and firmware source are both published in Electronic Cats' `Badge-bsides-cdmx-2025` GitHub repository under `hardware/Metro-Addon`, making the addon fully open source. No separate product page, price, or distribution details for the addon were found; it appears to have been bundled with or given out alongside the main BSides CDMX 2025 badge rather than sold on its own. The firmware's own README credits the design "for HackGDL," an Electronic Cats-affiliated Guadalajara event, which may mean the board started life there before being reused for BSides CDMX.

## Make your own

The full KiCad project (schematic, PCB layout, silkscreen and edge-cut exports, drill files) is in `hardware/Metro-Addon/` of the repo, and the firmware — a Puya PY32F0-series project built with the GNU Arm Embedded Toolchain and flashed via J-Link — is in `hardware/Metro-Addon/firmware/`, including its own build instructions.
