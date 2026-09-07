---
title: IDK SAO
id: dc32-idk-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: p0ns/idk
  url: https://idk.bz/
summary: A small SAO built around the new ATtiny Series 0/1 chips, with four SK6812-mini LEDs and a button, made in a first batch of 24.
functions: 'LED lighting effects driven by the ATtiny chip, triggered/controlled by the onboard button.'
look:
  colors: []
  shape: rectangle
  themes:
  - minimalist
tech:
  mcu: ATtiny404
  leds:
    count: 4
    type: SK6812-mini
    note: First batch used an ATtiny404; the maker noted later batches might use a different ATtiny 0/1-series chip.
  display: none
  connectivity:
  - uart
  battery: powered by host badge
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: 24
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://idk.bz/idk-sao.ino
  eda_tool: null
links:
- kind: website
  label: IDK (p0ns) project site
  url: https://idk.bz/
  archived: false
- kind: website
  label: IDK SAO - IDK
  url: https://idk.bz/idksao/
  archived: false
images:
  - file: assets/images/badges/dc32/idk-sao/994c5695f1.png
    source: "https://idk.bz/idksao/"
    credit: "p0ns/idk"
    caption: "IDK SAO, front"
  - file: assets/images/badges/dc32/idk-sao/e7c74863d6.jpg
    source: "https://idk.bz/idksao/"
    credit: "p0ns/idk"
    caption: "IDK SAO, back"
contact: {}
notes:
- 'Maker''s post title is simply "IDK SAO"; the community sheet used the same title, so no rewording was needed.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: >-
    Confirmed directly on the maker's own site (idk.bz/idksao/, posted 2024-05-16, ahead of
    DEF CON 32 that August): ATtiny404 (first batch of 24; the maker says later batches might
    use a different ATtiny 0/1-series chip), 4x SK6812-mini LEDs, one button, 6-pin SAO
    connector wired so pin 1 doubles as the ATtiny's UPDI programming pin. Firmware is
    published as a downloadable .ino sketch; no hardware/Gerber files or EDA tool are named,
    so open_source is "partial" rather than "yes". No price, sale channel, or post-con
    availability is stated anywhere on the maker's site, GitHub, or social accounts (checked
    against the same maker's other dc32 entries in this archive — Battery SAO, 420 Bud SAO,
    Disappointing Badge — which cross-referenced the same site), so price/availability/where
    are left unfilled rather than guessed. Colors are not shown clearly enough in the
    (grayscale-toned) product photos to call with confidence, so look.colors is left empty.
last_modified_date: '2026-09-06'
---

In May 2024, ahead of DEF CON 32, p0ns (of idk.bz) posted a small SAO built around the then-new ATtiny Series 0/1 microcontroller family. The board carries four SK6812-mini addressable LEDs and a single button, connects through a 6-pin SAO header, and is powered from the host badge. A deliberate detail: pin 1 of the SAO connector doubles as the chip's UPDI programming pin, so the whole board can be reflashed in place with a modified USB-UART adapter, with no separate programming header needed.

The first batch ran 24 units on an ATtiny404; the maker noted that later batches might switch to a different chip in the same ATtiny 0/1 family. The maker published the firmware as a downloadable Arduino sketch (`idk-sao.ino`) and posted the schematic and pinout as images, but did not publish hardware design files or name a CAD tool, and gave no price or sale channel — this looks like a maker's personal give-away/trade SAO from that year rather than a storefront item, consistent with idk.bz's other DC31/DC32-era SAOs.

## Make your own

Firmware is available directly from the maker: [idk-sao.ino](https://idk.bz/idk-sao.ino). To reprogram a unit, build a UPDI programmer from any USB-UART converter (a diode and resistor, per [SpenceKonde's guide](https://github.com/SpenceKonde/AVR-Guidance/blob/master/UPDI/jtag2updi.md)) and connect to pin 1 of the SAO header, which is wired to the ATtiny's UPDI pin.
