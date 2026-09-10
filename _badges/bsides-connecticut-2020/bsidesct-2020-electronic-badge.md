---
title: BSidesCT 2020 Electronic Badge
id: bsides-connecticut-2020-bsidesct-2020-electronic-badge
layout: badge
parent: BSides Connecticut 2020
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-connecticut-2020
year: 2020
makers:
- name: BSides-CT community team
summary: An electronic conference badge for BSidesCT 2020 built around an Atmel SAM D11 MCU, with programmable LEDs and an onboard CR95HF NFC reader.
functions: Programmable LED blink patterns; an onboard NFC reader (non-functional as shipped due to unresolved initialization bugs); USB-C for power/programming.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: SAM D11 D14AM
  leds:
    count: null
    type: null
    note: Multiple programmable LEDs with working blink-pattern firmware.
  display: null
  connectivity:
  - nfc
  - usb
  battery: USB-C (powered/programmed via USB-C)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Distributed to BSidesCT 2020 conference attendees.
make_your_own:
  open_source: true
  hardware_url: https://github.com/BSides-CT/2020-Badge
  firmware_url: https://github.com/BSides-CT/2020-Badge
  eda_tool: null
links:
- label: github.com/BSides-CT/2020-Badge
  url: https://github.com/BSides-CT/2020-Badge
  kind: repo
images:
- file: assets/images/badges/bsides-connecticut-2020/bsidesct-2020-electronic-badge/17699e109c.jpg
  source: https://github.com/BSides-CT/2020-Badge
  credit: BSides-CT
  caption: Assembled 2020 BSidesCT badge PCB showing the SAM D11 MCU, CR95HF NFC reader, and USB-C port
contact: {}
notes:
- Electronic badge for BSides Connecticut 2020 with an NFC reader (SAM D11 + CR95HF), distributed despite unresolved USB/NFC bugs. Found by the event-year sweep, task general-2020.
- The GitHub repo says the badge was originally designed for BSidesCT 2019 but the release was delayed, with the 2020 team completing and distributing it that year.
status: released
sources:
- kind: url
  url: https://github.com/BSides-CT/2020-Badge
  title: BSidesCT 2020 Electronic Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2020); event read as ''BSides Connecticut 2020''.'
- kind: url
  url: https://github.com/BSides-CT/2020-Badge
  title: BSides-CT/2020-Badge README
  accessed: '2026-09-10'
  note: Confirmed maker, MCU (SAM D11 D14AM), NFC chip (CR95HF), USB-C, GPL-3.0 open hardware/firmware, distribution to attendees, and that NFC/USB code was non-functional as released.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Only source found is the maker's own GitHub repo (no press coverage, storefront, or photos of the fully assembled/worn badge — only component/schematic images in the repo, one of which is used above). Repo says the badge was originally designed for BSidesCT 2019 and delayed to 2020; kept the event as bsides-connecticut-2020 since that is when it was actually distributed. Exact quantity made and LED count/type not stated anywhere found.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsides-connecticut-2020/bsidesct-2020-electronic-badge.glb
  method: kicad
  source_file: Hardware/Schematics/bsidesct2019.kicad_pcb
  generated: '2026-09-10'
  bytes: 318588
---

The 2020 BSidesCT electronic badge is a conference badge built around an Atmel SAM D11 D14AM microcontroller, given out to attendees of BSides Connecticut. According to its GitHub repository, the design was originally started for the 2019 event but wasn't finished in time, so the BSides-CT team completed and distributed it in 2020 instead.

The badge features programmable LEDs with working blink-pattern firmware, a CR95HF-based NFC reader, and a USB-C port used for power and programming. The NFC reader and USB serial communication reportedly had unresolved initialization bugs and did not work reliably in the units that went out, but the team released the hardware schematics and firmware source under GPL-3.0 anyway, along with notes for community members interested in debugging or extending it.

## Make your own

Hardware schematics and firmware source are published at [github.com/BSides-CT/2020-Badge](https://github.com/BSides-CT/2020-Badge) under GPL-3.0. The repo includes MCU and NFC pinout diagrams and an SWD programming header layout for anyone who wants to build or repair one.
