---
title: Helgatchi
id: dc34-helgatchi
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: DC801 + 801 Labs
  url: https://dc801.store
summary: A pocket-sized BLE and WiFi scanner from DC801/801 Labs that passively hunts for beacons and alerts on matching devices, built around a XIAO ESP32-S3 with a 1.69" color screen.
functions: |-
  A portable, hand-held BLE beacon and WiFi AP scanner/hunter, with built-in alerting, 1.69” full-color screen, and external SMA-RP antenna all powered by the XIAO ESP32-S3.

  The Helgatchi will passively scan for BLE devices and WiFi SSIDs/APs, and alert when specific Manufacturers, naming schemes, or services are discovered.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - security
  - radio
  - hardware tool
  - wearable
tech:
  mcu: XIAO ESP32-S3
  leds:
    count: 6
    type: RGB
    note: For customizable visual alerts; individual LED chip part not confirmed by the maker.
  display: 1.69" LCD (240x280, Waveshare)
  connectivity:
  - wifi
  - ble
  battery: 400mAh 3.7V LiPo (rechargeable)
  sao_version: null
get_one:
  price: $120 (regular $801)
  price_usd: 120.0
  quantity: ''
  availability: available
  availability_note: Listed as in-stock on dc801.store as of 2026-09-06.
  distribution:
  - purchase
  where: Sold directly through the DC801 storefront (dc801.store), with local pickup at 801 Labs or remote shipping.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Pips801/Helgatchi/tree/main/Hardware
  firmware_url: https://github.com/Pips801/Helgatchi/tree/main/Software
  eda_tool: KiCad
  gerbers_url: null
  bom_url: null
  license: null
  fab_url: null
  notes: Repo also includes a WebFlasher tool and a hardware test jig. Firmware is built on PlatformIO + Arduino, using LVGL for graphics, NimBLE for BLE, and FastLED for the RGB LEDs.
links:
- label: dc801.store
  url: https://dc801.store
  kind: store
- label: github.com/Pips801/Helgatchi
  url: https://github.com/Pips801/Helgatchi
  kind: repo
- label: DC801 Helgatchi Badge (product page)
  url: https://dc801.store/products/helgatchi
  kind: store
  note: Full description, specs, price, and images.
images:
- file: assets/images/badges/dc34/helgatchi/ec7fce1fb9.jpg
  source: https://dc801.store/products/helgatchi
  credit: DC801 / 801 Labs
  caption: Helgatchi handheld BLE/WiFi scanner badge, front view with 1.69in screen
- file: assets/images/badges/dc34/helgatchi/854002afb5.jpg
  source: https://dc801.store/products/helgatchi
  credit: DC801 / 801 Labs
  caption: Helgatchi badge, alternate angle showing antenna and enclosure
contact:
  discord: Pips801
  emails:
  - pips@801labs.org
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 24
  updated: 6/23/2026 12:45:55
  listing: New
- kind: url
  url: https://dc801.store/products/helgatchi
  title: DC801 Helgatchi Badge
  accessed: '2026-09-06'
  note: Full product description, specs table (MCU, battery, screen, antenna, size), price ($120, regular $801), shipping timeline, and product photos.
- kind: url
  url: https://github.com/Pips801/Helgatchi
  title: Pips801/Helgatchi on GitHub
  accessed: '2026-09-06'
  note: Confirms repo structure (Hardware, Software, WebFlasher folders) and project site helga.pet.
- kind: url
  url: https://github.com/Pips801/Helgatchi/tree/main/Hardware/Helgatchi%20front%20PCB
  title: Helgatchi front PCB directory listing
  accessed: '2026-09-06'
  note: Confirms KiCad design files (.kicad_pcb, .kicad_sch, .kicad_pro) for the hardware.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core facts (chip, display, LEDs, battery, price, availability, open-source hardware/firmware) confirmed directly from the maker''s storefront listing and GitHub repo. Could not confirm: quantity made, individual RGB LED chip part number, PCB solder-mask/silkscreen color (product photos suggest a dark enclosure but this was not stated in text), gerbers/BOM download links, and any software license for the repo (no LICENSE file found). The repo also references a project site at helga.pet which was not fetched.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/helgatchi.glb
  method: kicad
  source_file: Hardware/Helgatchi front PCB/Helgatchi front PCB.kicad_pcb
  generated: '2026-09-07'
  bytes: 241948
---

The Helgatchi is a pocket-sized BLE and WiFi scanner made by DC801 and 801 Labs for DEF CON 34, sold through the DC801 storefront for $120 (marked down from a joke "regular price" of $801). Built around a Seeed XIAO ESP32-S3 with 8MB of flash, it drives a 1.69" rounded color LCD, six RGB LEDs, and a vibration motor, and connects to an external SMA-RP antenna for extra 2.4 GHz range. It runs on a 400mAh rechargeable LiPo and fits in a pocket.

Functionally, it passively scans for BLE beacons and WiFi access points in the background, waking to actively scan and alert when it spots something matching a user-defined rule — by MAC address, manufacturer/OUI, device name or SSID, or BLE service. The maker's listing suggests using it to flag ALPR and other surveillance gear, tactical equipment, hidden cameras, fitness wearables, and other 2.4 GHz devices, with configurable alert behavior (vibrate, LED, screen wake) and adjustable sleep/scan durations.

Both hardware and firmware are published on GitHub (Pips801/Helgatchi): the Hardware folder holds KiCad source for the front and back PCBs, a spacer, and a test jig, while the Software folder holds PlatformIO/Arduino firmware built on LVGL (graphics), NimBLE (BLE), and FastLED (the RGB LEDs). The repo also includes a browser-based WebFlasher for reflashing units without a full toolchain install.

## Make your own

The KiCad hardware source (front PCB, back PCB, spacer, test jig) and PlatformIO/Arduino firmware are both in the GitHub repo linked above. No separate Gerber export, BOM, or license file was found in the repository at the time of this research; anyone building their own would need to export fabrication files from the KiCad projects directly.
