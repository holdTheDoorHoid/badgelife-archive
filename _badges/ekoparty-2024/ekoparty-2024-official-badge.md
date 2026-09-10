---
title: Ekoparty 2024 Official Badge
id: ekoparty-2024-ekoparty-2024-official-badge
layout: badge
parent: Ekoparty 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: ekoparty-2024
year: 2024
makers:
- name: Electronic Cats
  url: https://electroniccats.com/
summary: The official electronic badge for Ekoparty 2024, built by Electronic Cats around an ESP32-C6 with an RFM95 LoRa radio, a small OLED display, addressable NeoPixel LEDs, a buzzer, and USB, decorated with a pixel-sunglasses llama graphic.
functions: Boots to a serial terminal over USB (115200 baud) showing badge text/UI; drives the OLED display and NeoPixel LEDs; communicates over the onboard LoRa radio.
look:
  colors: []
  shape: null
  themes:
  - animal
  - radio
  - meme
tech:
  mcu: ESP32-C6
  leds:
    count: null
    type: NeoPixel
    note: Addressable RGB NeoPixel LEDs; exact count not stated in the repo.
  display: OLED
  connectivity:
  - lora
  - usb
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution: []
  where: Distributed at Ekoparty 2024 in Buenos Aires; an Electronic Cats social post described it as a limited-run electronic badge for the event, but no price or exact quantity is published.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/ElectronicCats/badge-EKOParty-2024/tree/main/hardware
  firmware_url: https://github.com/ElectronicCats/badge-EKOParty-2024/tree/main/firmware
  eda_tool: KiCad
  notes: Hardware released under the CERN Open Hardware Licence v1.2 (see LICENSE_HARDWARE.md). Firmware build instructions are in firmware/README.md.
links:
- label: github.com/ElectronicCats/badge-EKOParty-2024
  url: https://github.com/ElectronicCats/badge-EKOParty-2024
  kind: repo
- label: Electronic Cats (maker site)
  url: https://electroniccats.com/
  kind: website
images:
- file: assets/images/badges/ekoparty-2024/ekoparty-2024-official-badge/db0a1481ca.jpg
  source: https://github.com/ElectronicCats/badge-EKOParty-2024
  credit: Electronic Cats
  caption: 'Badge board outline / silkscreen artwork (3D render): a llama wearing pixel sunglasses'
contact: {}
notes:
- ESP32-C6 badge with RFM95 LoRa radio, OLED display and NeoPixels, designed by Electronic Cats for Ekoparty 2024. Found by the event-year sweep, task con-ekoparty.
- 'Research 2026-09-08: confirmed via the maker''s own GitHub repo (README, LICENSE_HARDWARE.md) and file tree. The repo does not include a photo of the assembled/soldered badge; the saved image is a KiCad 3D-viewport render of the board outline and llama-in-sunglasses artwork found in hardware/Eko2024.pretty/, used here as the best available depiction of the design. Price and exact production quantity are not published anywhere found; a search snippet of an Electronic Cats social post (Instagram) called it a limited-edition electronic badge for the event but could not be fully fetched to confirm numbers, so those fields were left empty rather than guessed. LED count is not stated. A search result surfaced a third-party site (badge.gallery) with a page titled to look like it discusses "image provenance" for this exact entry; it was not opened since it appears aimed at an automated researcher rather than at documenting the badge, and none of its claims were used here.'
status: released
sources:
- kind: url
  url: https://github.com/ElectronicCats/badge-EKOParty-2024
  title: Ekoparty 2024 Official Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''Ekoparty 2024''.'
- kind: url
  url: https://raw.githubusercontent.com/ElectronicCats/badge-EKOParty-2024/main/README.md
  title: ElectronicCats/badge-EKOParty-2024 README
  accessed: '2026-09-08'
  note: Confirmed MCU (ESP32-C6), LoRa/OLED/NeoPixel/buzzer/USB hardware, open-hardware CERN OHL v1.2 licensing, and serial-terminal usage.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Core hardware facts (MCU, radio, display, LEDs, open-source status) confirmed from the maker's own repository. Price, exact LED count, production quantity, and distribution mechanics are not published in any source found and are left empty. No production/assembled-badge photo was found; the saved image is board-outline artwork from the KiCad footprint library, not a photo of the physical item.
last_modified_date: '2026-09-10'
model:
  file: assets/models/ekoparty-2024/ekoparty-2024-official-badge.glb
  method: kicad
  source_file: hardware/eko-badge-2024/eko-badge-2024.kicad_pcb
  generated: '2026-09-10'
  bytes: 310132
---

The Ekoparty 2024 Official Badge is an electronic conference badge Electronic Cats designed for Ekoparty, the long-running Buenos Aires security conference. It is built around an ESP32-C6 microcontroller paired with an RFM95 LoRa radio, a small OLED display, addressable NeoPixel RGB LEDs, a buzzer, and USB connectivity; out of the box it boots to a serial terminal at 115200 baud that shows badge text and UI. The board carries a pixel-art llama-in-sunglasses graphic as its main artwork.

Electronic Cats published both the hardware (KiCad design files, released under the CERN Open Hardware Licence v1.2) and the firmware for the badge on GitHub, continuing their pattern of releasing conference badges as open hardware. No price, exact LED count, or production quantity is published; a company social-media post around the badge's release described it as a limited-edition badge made for the event, but the specifics were not confirmed in any source that could be fully verified for this entry.

## Make your own

The hardware design lives in the `hardware/` directory of the GitHub repo (KiCad project, including the PCB outline/silkscreen artwork), and the firmware lives in `firmware/`, with build instructions in `firmware/README.md`. The hardware is licensed under CERN OHL v1.2.
