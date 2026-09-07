---
title: 2025 Utahtastic BSides Badge — BSides Lora Badge
id: bsides-2025-2025-utahtastic-bsides-badge-bsides-lora-badge
layout: badge
parent: BSides 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-2025
year: 2025
makers:
- name: distinctm1nd
  url: https://github.com/distinctm1nd
summary: A LoRa mesh-networking badge made for BSides Utah 2025, running a custom Meshtastic firmware over Bluetooth-paired phone control.
functions: Sends and receives text messages over a LoRa mesh network (Meshtastic), navigated with a 5-way joystick and shown on a TFT screen; pairs to the Meshtastic phone app over Bluetooth to change settings such as ambient LED color and brightness. Holds 3 minibadges on expansion headers.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - wearable
tech:
  mcu: ESP32-S3-WROOM
  leds:
    count: 25
    type: addressable
    note: Includes moon-shaped LEDs behind a 3D-printed diffuser on the back of the badge.
  display: TFT display
  connectivity:
  - lora
  - ble
  - uart
  battery: Micro USB or 3x AA batteries, regulated to 3.3V
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees at BSides Utah 2025; not sold as a standalone product.
make_your_own:
  open_source: true
  hardware_url: https://github.com/distinctm1nd/2025_utahtastic_bsides_badge/tree/functional/hardware
  firmware_url: https://github.com/distinctm1nd/2025_utahtastic_bsides_badge/tree/functional/software
  eda_tool: null
links:
- label: github.com/distinctm1nd/2025_utahtastic_bsides_badge
  url: https://github.com/distinctm1nd/2025_utahtastic_bsides_badge
  kind: repo
  archived: https://web.archive.org/web/20260907104757/https://github.com/distinctm1nd/2025_utahtastic_bsides_badge
- label: Joystick Button Cap (Printables)
  url: https://www.printables.com/model/1166931-joystick-cap-for-b-sides-utah-2025-badge
  kind: fab
- label: Moon LED Diffuser (Printables)
  url: https://www.printables.com/model/1166783-moon-led-diffuser-for-b-sides-utah-2025-badge
  kind: fab
images:
- file: assets/images/badges/bsides-2025/2025-utahtastic-bsides-badge-bsides-lora-badge/26ace32ddb.png
  source: https://github.com/distinctm1nd/2025_utahtastic_bsides_badge
  credit: distinctm1nd
  caption: Front of the BSides Utah 2025 LoRa badge, showing the TFT display, 5-way joystick, and minibadge headers
- file: assets/images/badges/bsides-2025/2025-utahtastic-bsides-badge-bsides-lora-badge/4f421e05a3.png
  source: https://github.com/distinctm1nd/2025_utahtastic_bsides_badge
  credit: distinctm1nd
  caption: Back of the BSides Utah 2025 LoRa badge, showing the moon LED diffuser and lanyard post
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/distinctm1nd/2025_utahtastic_bsides_badge
  title: 2025_utahtastic_bsides_badge — BSides Lora Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides 2025 (Utah)''.'
  archived: https://web.archive.org/web/20260907104757/https://github.com/distinctm1nd/2025_utahtastic_bsides_badge
- kind: url
  url: https://github.com/distinctm1nd/2025_utahtastic_bsides_badge
  title: 2025_utahtastic_bsides_badge README
  accessed: '2026-09-07'
  note: README and hardware/software folders read for specs, assembly instructions, and image files (utah_bsides_front.png, utah_bsides_back.png).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Made for BSides Utah 2025 (no bsides-utah event id exists in events.yml, so the entry stays under the generic bsides-2025 id; noted here per research guide). Repository is the maker's own project page and is the primary source; no independent press coverage, storefront, or price/quantity information was found. Availability set to unknown since this appears to have been a conference giveaway/build, not a sale; get_one.where reflects that. Hardware/firmware are both published (Meshtastic-based custom firmware, KiCad-style hardware folder not explicitly labeled with an EDA tool), so open_source is yes though the specific EDA tool used was not stated.
last_modified_date: '2026-09-07'
model:
  file: assets/models/bsides-2025/2025-utahtastic-bsides-badge-bsides-lora-badge.glb
  method: gerber
  source_file: hardware/2025_bsides_badge_v2.kicad_pcb
  generated: '2026-09-07'
  bytes: 361544
  size_mm:
  - 138.2
  - 111.8
---

The 2025 Utahtastic BSides Badge is a LoRa mesh-networking badge made by distinctm1nd for BSides Utah 2025. Built around an ESP32-S3-WROOM with a LoRa radio, it runs a custom Meshtastic firmware, letting attendees send and receive short text messages across a mesh network using a 5-way joystick to navigate a TFT display, or by pairing the badge to the official Meshtastic phone app over Bluetooth. The badge carries 25 addressable LEDs, including moon-shaped LEDs on the back lit through a 3D-printed diffuser whose color and brightness can be tuned from the app's ambient lighting settings.

The badge can run off Micro USB or three AA batteries (regulated down to 3.3V), and exposes a UART header, reset/flash buttons, and 4 general-purpose GPIO pins for hacking. It also carries three minibadge expansion slots; the repository includes a matching solder-your-own minibadge kit (resistors and LEDs) as a badge-assembly activity. STL files for a custom joystick cap and the moon diffuser are shared separately on Printables.

## Make your own

Hardware and firmware are both published in the GitHub repository, split into `hardware` and `software` directories, with a `doc/datasheets` folder for component references. The README walks through badge and minibadge assembly (soldering headers, the battery holder, and the moon diffuser) and documents the joystick's five functions (send, backspace, cursor left/right, and screen switch). No price, production quantity, or resale availability is stated; the badge appears to have been distributed to attendees rather than sold.
