---
title: AND!XOR DC30 Badge "Chomper"
id: dc30-awesome-badge-aka-watch
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: AND!XOR
  url: https://andnxor.com/
summary: A DEF CON 30 badge built by re-flashing a LilyGo T-Watch 2020 V3 smartwatch with a custom MicroPython build, worn on a lanyard instead of a wrist strap in most cases; the listing researched here is the "Philanthropist" fundraising tier that sold spare badges for donation.
functions: Digital/binary/analog watch faces, TV-B-Gone, a BLE scanner, a proximity-based "Ninja" attack game, the B.E.N.D.E.R. text-adventure CTF, full-screen RGB/GIF "bling" playback, an on-device RTFM manual, and an over-the-air "Upgrayedd" updater.
look:
  colors:
  - black
  - purple
  shape: rectangle
  themes:
  - wearable
  - ctf
  - hardware tool
  form_factor: wearable
tech:
  mcu: ESP32
  leds: null
  display: 1.54" 240x240 color LCD with capacitive touch
  connectivity:
  - wifi
  - bluetooth
  - ir
  battery: LiPo, rechargeable via Micro USB, ~24 hours
  sao_version: none
get_one:
  price: $150
  price_usd: 150.0
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - free_drop
  - contest
  - raffle
  where: 'Philanthropist sale at shop.andnxor.com: a $150 donation tier that set aside
    a spare badge for the buyer. The badges themselves were not generally sold; AND!XOR
    says most were given away for hacking challenges or at random at DEF CON 30.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HughMungis/ANDnXOR_DC30_Badge
  eda_tool: null
  notes: The hardware is an off-the-shelf LilyGo T-Watch 2020 V3 (no custom PCB this
    year, per the maker); only the firmware/software is AND!XOR's own work and is
    published under the MIT license.
links:
- label: shop.andnxor.com/products/and-xor-dc30-philanthropist-badge
  url: https://shop.andnxor.com/products/and-xor-dc30-philanthropist-badge
  kind: store
- label: HughMungis/ANDnXOR_DC30_Badge (firmware repo)
  url: https://github.com/HughMungis/ANDnXOR_DC30_Badge
  kind: repo
images:
- file: assets/images/badges/dc30/awesome-badge-aka-watch/7e5c97eda2.png
  source: "https://shop.andnxor.com/products/and-xor-dc30-philanthropist-badge"
  credit: "AND!XOR"
  caption: "AND!XOR DC30 badge (Chomper), a modified LilyGo T-Watch, worn on the
    wrist in the shop listing's promotional photo"
contact: {}
notes:
- <Sold Out>
- 'Sheet listed it only as "Awesome Badge (aka watch)"; the maker''s own name for
  it, found in the firmware repo, is "Chomper."'
status: released
sources:
- kind: sheet
  event: dc30
  row: 6
  updated: '2022-07-31'
- kind: url
  url: https://shop.andnxor.com/products/and-xor-dc30-philanthropist-badge
  title: AND!XOR DC30 Philanthropist Badge
  accessed: '2026-09-06'
  note: Live page now 404s; content retrieved via Wayback Machine snapshot (2023-09-28).
    Confirms $150 price, sold-out status, that it is not a custom-PCB badge this
    year but a re-flashed consumer device worn on a lanyard, hackable via MicroPython,
    with radios; badges mostly given away for challenges/randomly rather than generally
    sold.
- kind: url
  url: https://github.com/HughMungis/ANDnXOR_DC30_Badge
  title: HughMungis/ANDnXOR_DC30_Badge - "Chomper!"
  accessed: '2026-09-06'
  note: Firmware repo README and rtfm/docs/index.md confirm the hardware is a LilyGo
    T-WATCH 2020V3 (ESP32, 16MB flash, 4MB RAM, 240x240 capacitive touch display,
    wifi/BT, IR LED, vibration motor, ~24h battery, Micro USB charging), the codename
    "Chomper," MIT-licensed MicroPython 1.18 firmware, and the full app list (watch
    faces, TV-B-Gone, BLE scanner, Ninja, B.E.N.D.E.R CTF, Bling, RTFM, Upgrayedd).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts (hardware, firmware, features, price, distribution) confirmed
    by the maker's own shop listing (via Wayback Machine, since the live page 404s)
    and firmware repo. Exact production quantity not stated anywhere found. The
    $150 "Philanthropist" listing was a donation tier for spare badges, not the
    normal way most attendees got one; get_one.where reflects that nuance. No LED
    count is documented for the watch itself (the T-Watch case has no separate
    addressable LEDs beyond the display/vibration motor), so tech.leds is left null.
    No additional maker photos of the badge itself were found beyond the shop's
    promotional (partially obscured) image.
last_modified_date: '2026-09-06'
---

The DEF CON 30 (2022) AND!XOR badge, nicknamed "Chomper" by its makers, departed from the group's usual custom-PCB badges: facing supply-chain shortages, AND!XOR instead took an off-the-shelf LilyGo T-Watch 2020 V3 smartwatch and rewrote its firmware from scratch, building a semi-custom MicroPython 1.18 port for its ESP32 (16MB flash, 4MB RAM). The watch keeps its 240x240 capacitive touchscreen, Wi-Fi and Bluetooth radios, an infrared LED, a vibration motor, and roughly 24 hours of battery life on its LiPo cell, charged over Micro USB. Rather than a wrist badge, most attendees wore it on a lanyard.

On top of digital/binary/analog watch faces, the badge shipped with a TV-B-Gone app, a BLE scanner, a proximity-based "Ninja" dueling game, full-screen RGB/GIF "bling" video playback, an on-device RTFM manual, and an OTA updater called "Upgrayedd." As in past years, the centerpiece was AND!XOR's B.E.N.D.E.R. CTF, a text-adventure hacking challenge accessed over a serial console, tied into a side challenge called "Snackey."

The entry researched here corresponds to the shop's "Philanthropist" listing: a $150 donation tier, now sold out, through which buyers helped fund extra badges for the con rather than buying a badge for themselves outright. AND!XOR's own listing says most Chomper badges were given away for hacking challenges or handed out at random at DEF CON 30, rather than sold in the ordinary sense.

## Make your own

The firmware, provisioning scripts, and an in-progress manual are published under the MIT license at [HughMungis/ANDnXOR_DC30_Badge](https://github.com/HughMungis/ANDnXOR_DC30_Badge). Building it means cloning ESP-IDF v4.2, installing `adafruit-ampy`/`mpremote`, and running the repo's `provision/provision.sh` against a LilyGo T-Watch 2020 V3 over serial; the hardware itself is the stock commercial T-Watch, not a custom AND!XOR PCB, so no Gerbers or BOM are published for this year's badge.
