---
title: Badge Tag NFC SAO
id: supercon-2024-badge-tag-nfc-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Thomas Flummer
  url: https://hackaday.io/tf
summary: A credential-card-shaped Simple Add-On built around an NXP NTAG I2C Plus 2K NFC chip that lets a badge show a name and share contact details, readable by a smartphone without power and accessible over I2C when mounted, entered in the Supercon 8 SAO Contest.
functions: Shares the wearer's name, contact details, and interests over NFC (tap with a phone, no power needed) or over I2C when plugged into a host badge.
look:
  colors: []
  shape: card
  themes:
  - security
  - nfc
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - nfc
  - i2c
  battery: null
  sao_version: v1.69bis
make_your_own:
  open_source: true
  hardware_url: https://github.com/flummer/badge-tag-sao
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/198165-badge-tag-nfc-sao
  url: https://hackaday.io/project/198165-badge-tag-nfc-sao
  kind: hackaday
  archived: https://web.archive.org/web/20251108163957/https://hackaday.io/project/198165-badge-tag-nfc-sao
- label: github.com/flummer/badge-tag-sao
  url: https://github.com/flummer/badge-tag-sao
  kind: repo
images:
- file: assets/images/badges/supercon-2024/badge-tag-nfc-sao/68996d3676.jpg
  source: https://hackaday.io/project/198165-badge-tag-nfc-sao
  credit: Thomas Flummer
  caption: Badge Tag NFC SAO card-shaped module
  archived: https://web.archive.org/web/20251108163957/https://hackaday.io/project/198165-badge-tag-nfc-sao
- file: assets/images/badges/supercon-2024/badge-tag-nfc-sao/482257adbd.jpg
  source: https://hackaday.io/project/198165-badge-tag-nfc-sao
  credit: Thomas Flummer
  caption: Badge Tag NFC SAO assembled board detail
  archived: https://web.archive.org/web/20251108163957/https://hackaday.io/project/198165-badge-tag-nfc-sao
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198165-badge-tag-nfc-sao
  title: Badge Tag NFC SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20251108163957/https://hackaday.io/project/198165-badge-tag-nfc-sao
- kind: url
  url: https://hackaday.io/project/198165-badge-tag-nfc-sao
  title: Badge Tag NFC SAO
  accessed: '2026-09-07'
  note: Confirmed maker, event (Supercon 8 SAO Contest, submitted 09/28/2024), NFC chip, form factor, SAO connector, and open-source status; source for both saved images.
  archived: https://web.archive.org/web/20251108163957/https://hackaday.io/project/198165-badge-tag-nfc-sao
- kind: url
  url: https://github.com/flummer/badge-tag-sao
  title: flummer/badge-tag-sao
  accessed: '2026-09-07'
  note: Confirmed exact NFC chip part number (NT3H2211W0FTT, NTAG I2C plus 2K), KiCad v8.99 design files, CC BY-SA 4.0 license, Gerbers and BOM present.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No price, quantity made, or distribution details found on either the Hackaday.io project page or the GitHub repo (this was a contest entry, not a sold item, so get_one fields are left empty). LED count/type and battery are not applicable since the SAO is a passive NFC tag with no MCU. sao_version is inferred as the standard 6-pin SAO (v1.69bis) since the repo describes a "through-hole SAO connector (2x3, keyed, 2.54mm spacing)" but this was not stated explicitly as a version number, so treat with light confidence.
last_modified_date: '2026-09-07'
---

The Badge Tag NFC SAO is a Simple Add-On by Thomas Flummer, submitted to the Supercon 8 SAO Contest in September 2024. Shaped and sized like a credential card, it centers on an NXP NT3H2211W0FTT (NTAG I2C plus, 2K memory) NFC chip, which lets anyone tap the tag with a smartphone to read a wearer's name, contact details, or interests without the SAO needing any power of its own — the chip harvests what it needs from the phone's NFC field. When mounted on a host badge through its 2x3 through-hole SAO connector, the same chip becomes readable over I2C as well.

The board is a simple, hand-assemblable design: just three SMD parts (a capacitor, a resistor, and the NFC chip itself) alongside the through-hole SAO header, plus a cutout for a lanyard. Hardware files — schematic, PCB layout, Gerbers, BOM, and an interactive assembly guide — are published on GitHub under KiCad (v8.99 nightly) and released under a CC BY-SA 4.0 license, making it straightforward for others to build or adapt.

No pricing, production quantity, or distribution details were found; the available sources describe it as a contest entry and open-source design rather than a badge sold or given away at scale.
