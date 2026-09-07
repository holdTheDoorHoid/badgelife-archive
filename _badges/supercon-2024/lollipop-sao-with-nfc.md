---
title: Lollipop SAO with NFC
id: supercon-2024-lollipop-sao-with-nfc
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: TomKeddie
  url: https://hackaday.io/hacker/101574-tomkeddie
summary: A lollipop-shaped Simple Add-On with an NFC/RFID antenna in the candy head, built around the ST M24LR64E dual-interface EEPROM so the host badge can read the tag memory over I2C; it is derived from the Teardown 2019 badge design and was entered in the Supercon 8 SAO Contest.
functions: 'Exposes an NFC/RFID tag (ST M24LR64E-RMN6T-2 dual-interface EEPROM) to the host badge over I2C; the antenna coil is etched into the lollipop head so the SAO can be read wirelessly with an NFC reader/phone as well as queried over the wired I2C bus.'
look:
  colors: [red, white]
  shape: lollipop
  themes: [candy, nfc, security]
tech:
  mcu: none
  leds: null
  display: none
  connectivity: [nfc, rfid, i2c]
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: [contest]
  where: 'Entered as a project in the Supercon 8 SAO Contest at Supercon 2024; no storefront or sale found.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/TomKeddie/prj-pcb-experiments/tree/master/2024-rfid-sao
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/198256-lollipop-sao-with-nfc
  url: https://hackaday.io/project/198256-lollipop-sao-with-nfc
  kind: hackaday
- label: github.com/TomKeddie/prj-pcb-experiments/tree/master/2024-rfid-sao
  url: https://github.com/TomKeddie/prj-pcb-experiments/tree/master/2024-rfid-sao
  kind: repo
- label: upverter.com/design/gsteiert/teardown2019
  url: https://upverter.com/design/gsteiert/teardown2019/
  kind: website
images:
  - file: assets/images/badges/supercon-2024/lollipop-sao-with-nfc/1d16d12bb3.jpg
    source: "https://hackaday.io/project/198256-lollipop-sao-with-nfc"
    credit: "TomKeddie"
    caption: "The Lollipop SAO with NFC, a lollipop-shaped PCB SAO"
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/198256-lollipop-sao-with-nfc
  title: Lollipop SAO with NFC
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/TomKeddie/prj-pcb-experiments/tree/master/2024-rfid-sao
  title: TomKeddie/prj-pcb-experiments - 2024-rfid-sao
  accessed: '2026-09-07'
  note: Repo README ("Plan") confirms red solder mask/white silk, I2C to SAO with optional pullups, M24LR64E NFC/RFID chip, and derivation from the Teardown 2019 badge; contains KiCad source and gerbers, no firmware (passive device, no MCU).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Confirmed as a Supercon 8 SAO Contest entry by TomKeddie via the Hackaday.io project page and the linked GitHub repo (its README states the design plan directly). No pricing, quantity-made, or storefront information was found anywhere -- it reads as a one-off contest/personal project rather than something sold or widely distributed, so get_one fields are left mostly empty. No SAO connector pin-count (v1 vs v2) is stated on either page. No explicit open-source license is given for the repo, though the KiCad source, gerbers, and mechanical files are all published. The repo''s images/ folder holds only clip-art references (stock lollipop vector art, silkscreen reference) used while designing the silkscreen, not photos of the finished board, so only the one Hackaday.io hero photo was saved.'
last_modified_date: '2026-09-07'
---

The Lollipop SAO with NFC is a Simple Add-On by TomKeddie (Tom Keddie), built for the Supercon 8 SAO Contest at Supercon 2024. Its lollipop-shaped PCB carries an NFC/RFID antenna etched right into the candy head, wired to an ST M24LR64E-RMN6T-2 dual-interface EEPROM. That chip lets the host badge read and write the tag's memory over a standard I2C connection (with optional pull-ups on the SAO header), while the same tag can also be read wirelessly by an NFC-capable phone or reader -- giving the SAO two independent ways in. It has no microcontroller, LEDs, or display of its own; it is a passive add-on rather than a powered device.

The board follows a simple, stated design plan: red solder mask, white silkscreen, and a shape and antenna derived from a teardown of the 2019 Supercon badge (referenced via its Upverter design page). No pricing, unit count, or distribution channel beyond the SAO Contest entry itself was found, so it reads as a one-off project piece rather than a widely sold badge.

## Make your own

The full KiCad source (schematic and PCB), generated gerbers, a JLCPCB-ready BOM, and mechanical exports (DXF/PDF) are published in TomKeddie's `prj-pcb-experiments` GitHub repository under `2024-rfid-sao/`. No license is stated for the repository. Building one would mean fabricating the board from the provided gerbers, sourcing the M24LR64E-RMN6T-2 NFC/RFID EEPROM and passives per the BOM, and wiring the SAO header's I2C lines (with the optional pull-up resistors) to a host badge.
