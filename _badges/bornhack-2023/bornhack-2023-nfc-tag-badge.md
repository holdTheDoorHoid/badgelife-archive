---
title: BornHack 2023 NFC Tag Badge
id: bornhack-2023-bornhack-2023-nfc-tag-badge
layout: badge
parent: BornHack 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2023
year: 2023
makers:
- name: BornHack
summary: 'The passive half of the BornHack 2023 two-board NFC badge set: a small NFC Forum Type 2 tag board built around an NXP NTAG I2C Plus chip, with no MCU of its own, designed to pair with the companion RP2040/PN7150 NFC reader badge.'
functions: Acts as a passive NFC tag that the reader badge (or any NFC Forum Type 2 reader, such as a phone) can read from and write to over the NTAG I2C Plus chip's RF and I2C interfaces.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - nfc
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Handed out alongside the matching NFC reader badge to BornHack 2023 attendees.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2023
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bornhack/badge2023/blob/main/README.md
  url: https://github.com/bornhack/badge2023/blob/main/README.md
  kind: repo
- label: github.com/bornhack/badge2023
  url: https://github.com/bornhack/badge2023
  kind: repo
images:
- file: assets/images/badges/bornhack-2023/bornhack-2023-nfc-tag-badge/63e3cac77b.jpg
  source: "https://github.com/bornhack/badge2023"
  credit: "BornHack"
  caption: "The BornHack 2023 NFC tag badge (right) paired with the NFC reader badge"
- file: assets/images/badges/bornhack-2023/bornhack-2023-nfc-tag-badge/4726c5c38c.jpg
  source: "https://github.com/bornhack/badge2023"
  credit: "BornHack"
  caption: "Back of the BornHack 2023 NFC badge pair showing the tag and reader boards"
contact: {}
notes:
- The passive half of the 2023 NFC badge pair, built around an NXP NTAG I2C Plus chip (part NT3H2211W0FTT) with no active MCU, distinct from the companion reader badge which uses an RP2040 and PN7150 NFC controller. Found by the event-year sweep, task bornhack-2023.
- The maker's repo and README treat the reader and tag as one combined "BornHack 2023 NFC Badges" project/README rather than naming the tag board separately; this entry covers the tag board specifically.
- This item substantially duplicates the archive's existing combined entry bornhack-2023-bornhack-2023-badge, which already documents both halves of the pair from the same repository.
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2023/blob/main/README.md
  title: BornHack 2023 NFC Tag Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bornhack-2023); event read as ''bornhack-2023''.'
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2023/main/README.md
  title: bornhack/badge2023 README.md
  accessed: '2026-09-08'
  note: Confirmed the tag board uses the NXP NT3H2211W0FTT (NTAG I2C Plus 2K, NFC Forum Type 2 Tag with I2C interface), has no MCU, is designed in KiCad v7, and that the hardware is released under CC BY-SA 4.0.
- kind: url
  url: https://api.github.com/repos/bornhack/badge2023/contents/IMAGES
  title: bornhack/badge2023 IMAGES directory listing
  accessed: '2026-09-08'
  note: Located the badge photo files used for the images below.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'The maker''s repo confirms this board exists and gives its chip (NXP NT3H2211W0FTT / NTAG I2C Plus 2K). No price, production quantity, or a photo of the tag board in isolation were found; all photos in the repo show the tag and reader boards together. This entry is essentially the same underlying project as bornhack-2023-bornhack-2023-badge (same repo, same maker, same event), which already documents both halves; kept as a separate entry per the sweep''s split but flagged as a likely duplicate.'
last_modified_date: '2026-09-08'
---

The BornHack 2023 NFC tag badge is the passive half of that year's two-board conference badge set. Where the companion badge carries an RP2040 microcontroller and an NXP PN7150 NFC reader/controller, the tag badge has no MCU at all: it is built around a single NXP NT3H2211W0FTT chip, part of the NTAG I2C Plus 2K family, an NFC Forum Type 2 tag that exposes both an RF interface and an I2C interface. Any NFC Forum Type 2 reader, including a phone or the matching reader badge, can read from and write to it.

BornHack designed the pair together and released the hardware for both boards, under the CC BY-SA 4.0 license, in a single GitHub repository (bornhack/badge2023), with schematics as KiCad v7 projects and PDFs. The repository's README and photos describe and depict the tag and reader as a connected pair rather than documenting the tag board on its own, and no price, production quantity, or independent product photo of the tag board was found in the sources checked.

This entry substantially overlaps the archive's existing combined entry for the BornHack 2023 badge (bornhack-2023-bornhack-2023-badge), which already covers both halves of the pair from the same source material.
