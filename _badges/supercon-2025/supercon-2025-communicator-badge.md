---
title: Supercon 2025 Communicator Badge
id: supercon-2025-supercon-2025-communicator-badge
layout: badge
parent: Supercon 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2025
year: 2025
makers:
- name: Hackaday
  url: https://hackaday.com
summary: 'The official badge for Hackaday Supercon 2025, a two-board ESP32-S3 handheld with a color TFT, a physical keyboard, and a LoRa radio for badge-to-badge messaging.'
functions: 'Runs a MicroPython-based OS with an app system; a background network stack sends, receives, and repeats LoRa messages between badges (with a TTL-based repeat/mesh scheme) while apps built on top define chat and other messaging protocols. Attendees can also write and load their own apps.'
look:
  colors: [green]
  shape: rectangle
  themes: [radio, hardware tool, retro computer]
tech:
  mcu: ESP32-S3
  leds: null
  display: 2.79" color TFT
  connectivity: [lora, i2c]
  battery: LiPo (MCP73831 USB charge controller)
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: 'Distributed to attendees at Hackaday Supercon 2025 (Friday of the conference); not sold.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hack-a-Day/2025-Communicator_Badge/tree/main/hardware
  firmware_url: https://github.com/Hack-a-Day/2025-Communicator_Badge/tree/main/firmware
  eda_tool: KiCad
links:
- label: hackaday.com/2025/10/27/the-supercon-2025-badge-is-built-to-be-customized
  url: https://hackaday.com/2025/10/27/the-supercon-2025-badge-is-built-to-be-customized/
  kind: article
- label: github.com/Hack-a-Day/2025-Communicator_Badge
  url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2025/supercon-2025-communicator-badge/f1745ddb89.jpg
  source: "https://github.com/Hack-a-Day/2025-Communicator_Badge"
  credit: "Hackaday"
  caption: "Front render of the Communicator Badge with customizable front panel"
- file: assets/images/badges/supercon-2025/supercon-2025-communicator-badge/3598d44e59.png
  source: "https://github.com/Hack-a-Day/2025-Communicator_Badge"
  credit: "Hackaday"
  caption: "Close-up of the rear PCB showing the keyboard dome switches and electronics"
contact: {}
notes:
- Two-PCB design; purely decorative front board holds keyboard membrane, made for customization
- 'Firmware repo also carries a "2026_hackaday_europe_image.bin", suggesting the same platform was reused for Hackaday Europe 2026; not confirmed as a separate release and not researched here.'
status: released
sources:
- kind: url
  url: https://hackaday.com/2025/10/27/the-supercon-2025-badge-is-built-to-be-customized/
  title: Supercon 2025 Communicator Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''Hackaday Supercon 2025''.'
- kind: url
  url: https://github.com/Hack-a-Day/2025-Communicator_Badge
  title: Hack-a-Day/2025-Communicator_Badge (GitHub repo)
  accessed: '2026-09-07'
  note: 'Confirmed MIT license, open hardware and firmware; repo structure (hardware/firmware/documentation/images).'
- kind: url
  url: https://raw.githubusercontent.com/Hack-a-Day/2025-Communicator_Badge/main/firmware/README.md
  title: Communicator Badge firmware README
  accessed: '2026-09-07'
  note: 'MicroPython + LVGL + asyncio firmware architecture; LoRa network stack with TTL-based message repeating; SAO I2C bus and onboard keyboard/display API mentioned.'
- kind: url
  url: https://api.github.com/repos/Hack-a-Day/2025-Communicator_Badge/contents/documentation/datasheets
  title: Communicator Badge datasheets folder listing
  accessed: '2026-09-07'
  note: 'Datasheets confirm ESP32-S3-WROOM MCU, SX1262/Wio-SX1262 LoRa module, ER-TFT2.79 TFT display (NV3007 driver), TCA8418 keypad controller, and MCP73831 LiPo charge IC.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo datasheets confirm the hardware (ESP32-S3, SX1262 LoRa, 2.79" TFT, TCA8418 keypad matrix controller, MCP73831 LiPo charger) but no BOM or README states LED count/type, so tech.leds is left empty. No maker-stated price or production quantity found; badge was a free conference giveaway, not sold. SAO support is implied by a "sao_i2c" bus referenced in firmware but no sao_ports count was stated, so sao_ports is left empty. No individual badge designer is credited by name in the sources checked; makers is kept as "Hackaday" (the team/org).'
last_modified_date: '2026-09-07'
---

The Communicator Badge was the official hardware for Hackaday Supercon 2025, held at the Hackaday HQ in Pasadena. It is a two-board handheld: a rear PCB carries an ESP32-S3 microcontroller, a 2.79-inch color TFT display, a TCA8418-driven membrane keypad, a Semtech SX1262 LoRa radio (via a Wio-SX1262 module), and a LiPo battery with USB charging, while a front board is purely mechanical — it exists to hold the keyboard membrane against the rear board's dome switches and is deliberately left blank so attendees can redesign, laser-cut, 3D-print, or CNC their own faceplate for it.

Firmware runs MicroPython with LVGL for the UI and asyncio to keep the display and keyboard responsive while a background network stack manages the LoRa radio. That stack lets badges send, receive, and repeat short messages to each other over the air using a time-to-live counter so messages propagate hop-to-hop without flooding forever, and it exposes ports that attendees could claim (via pull request) to build their own message protocols and apps on top. The badges also expose an SAO-compatible I2C bus.

Hackaday published the full hardware (KiCad) and firmware sources under the MIT license on GitHub, along with the datasheets for its major components, at github.com/Hack-a-Day/2025-Communicator_Badge. The badge was given to Supercon attendees rather than sold, and the repository shows signs the same platform was carried forward for a subsequent Hackaday Europe event, though that has not been independently confirmed.
