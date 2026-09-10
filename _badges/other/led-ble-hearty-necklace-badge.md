---
title: LED BLE Hearty Necklace/Badge
id: other-led-ble-hearty-necklace-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: Nitesh Kadyan
  url: https://hackaday.io/nitesh-kadyan
summary: A heart-shaped wearable LED badge/necklace with an 8x16 matrix of 0603 LEDs that scrolls custom text sent over Bluetooth from an Android phone.
functions: Displays scrolling text messages sent wirelessly from an Android app over BLE; firmware updates later added simple games (Tetris and Snake) playable on the LED matrix.
look:
  colors:
  - red
  shape: heart
  themes:
  - wearable
  - jewelry
tech:
  mcu: ATmega328p
  leds:
    count: 128
    type: discrete
    note: 0603 SMD LEDs in an 8x16 matrix, driven by two daisy-chained 74HC595 shift registers and a ULN2803 sink driver
  display: LED matrix 8x16
  connectivity:
  - ble
  battery: LiPo 320 mAh
  sao_version: none
get_one:
  price: ~$30 (planned)
  price_usd: 30
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Creator planned to sell assembled kits on Tindie; hand-soldered first batch mentioned on the project page. No live Tindie listing found at time of research.
make_your_own:
  open_source: true
  hardware_url: https://github.com/niteshkadyan/Hearty-LED-Necklace-Badge
  firmware_url: https://github.com/niteshkadyan/Hearty-LED-Necklace-Badge
  eda_tool: KiCad
  license: MIT
  notes: Repo contains KiCad project files, Arduino firmware (Hearty-Arduino/HeartyBadge), a Bluetooth-Hearty-LED folder, and a companion Android app; no separate BOM or Gerber folder was found in the visible repo listing.
links:
- label: hackaday.io/project/114144-led-ble-hearty-necklacebadge
  url: https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
  kind: hackaday
  archived: https://web.archive.org/web/20251211204905/https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
- label: github.com/niteshkadyan/Hearty-LED-Necklace-Badge
  url: https://github.com/niteshkadyan/Hearty-LED-Necklace-Badge
  kind: repo
  archived: https://web.archive.org/web/20260311144109/https://github.com/niteshkadyan/Hearty-LED-Necklace-Badge
images:
- file: assets/images/badges/other/led-ble-hearty-necklace-badge/c660107425.jpg
  source: https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
  credit: Nitesh Kadyan
  caption: The Hearty LED necklace/badge, worn
  archived: https://web.archive.org/web/20251211204905/https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
- file: assets/images/badges/other/led-ble-hearty-necklace-badge/310fc13570.jpg
  source: https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
  credit: Nitesh Kadyan
  caption: Assembled Hearty LED board, heart-shaped LED matrix
  archived: https://web.archive.org/web/20251211204905/https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
  title: LED BLE Hearty Necklace/Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
  archived: https://web.archive.org/web/20251211204905/https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
- kind: url
  url: https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
  title: LED BLE Hearty Necklace/Badge
  accessed: '2026-09-07'
  note: Maker, event/year, functions, MCU, LED count/type, battery, connectivity, price, and open-source claim.
  archived: https://web.archive.org/web/20251211204905/https://hackaday.io/project/114144-led-ble-hearty-necklacebadge
- kind: url
  url: https://github.com/niteshkadyan/Hearty-LED-Necklace-Badge
  title: niteshkadyan/Hearty-LED-Necklace-Badge
  accessed: '2026-09-07'
  note: Repo contents (KiCad + Arduino firmware + Android app), MIT license.
  archived: https://web.archive.org/web/20260311144109/https://github.com/niteshkadyan/Hearty-LED-Necklace-Badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a 2018 Hackaday Prize entry, not a badge made for a specific hacker con, so there is no matching event id in events.yml; left as event "other". Originally described by the maker as a Valentine's Day gift project. No live storefront was found to confirm final price, quantity made, or current availability; repo's Gerbers/BOM were not directly inspected beyond the folder listing.
last_modified_date: '2026-09-07'
---

The Hearty LED Necklace/Badge is a heart-shaped wearable built by Nitesh Kadyan, entered in the 2018 Hackaday Prize. An 8x16 grid of 128 tiny 0603 LEDs, driven by two daisy-chained 74HC595 shift registers and a ULN2803 sink driver off an ATmega328p, forms a small heart-shaped matrix display. An HM-11 Bluetooth Low Energy module lets a companion Android app push custom scrolling text messages to the badge wirelessly; later firmware updates added simple games, including Tetris and Snake, playable on the same matrix. It runs off a 320 mAh LiPo battery with onboard charge management.

The project began as a Valentine's Day gift and was later opened up as a hardware and software project, with KiCad design files, Arduino firmware, and the Android app all published on GitHub under the MIT license. The maker mentioned hand-soldering an initial batch and floated selling assembled kits on Tindie for around $30, but no live storefront listing was found during this research, so final production numbers and current availability are unconfirmed.

## Make your own

Hardware and firmware are open source at the GitHub repo linked above: KiCad project files for the PCB, Arduino sketches under `Hearty-Arduino/HeartyBadge`, BLE-handling code under `Bluetooth-Hearty-LED`, and a separate Android app for sending messages over Bluetooth.
