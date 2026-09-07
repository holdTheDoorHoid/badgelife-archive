---
title: Free-WiLi Whale Tail Badge
id: dc32-ics-village-unnamed-badge-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: FreeWili
  url: https://freewili.com/
summary: A RP2040-based badge from FreeWili highlighting industrial and automotive
  digital protocols, sold through the ICS Village at DEF CON 32.
functions: Works as a USB-to-10BASE-T1L interface and a CAN FD interface for talking
  to industrial and automotive networks; includes an RS485 Modbus interface, a
  4-20mA sensor simulator, capacitive touch buttons, and an expansion plug that
  adds a FreeWili's display, power, and wireless modules.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - measurement
  - radio
tech:
  mcu: RP2040
  leds:
    count: 6
    type: RGB
    note: 6x serial RGB color programmable LED
  display: null
  connectivity:
  - i2c
  - none
get_one:
  price: $60/$70
  price_usd: 60.0
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Sold at the ICS Village booth at DEF CON 32, 2024.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/freewili/whaletail-examples
  eda_tool: null
links:
- label: x.com/ICS_Village
  url: https://x.com/ICS_Village
  kind: social
- kind: url
  url: https://web.archive.org/web/20240809175354/https://www.icsvillage.com/defconevents/def-con-32
  title: 'ICS Village: DEF CON 32 (archived)'
  accessed: '2026-09-06'
  note: Confirms the item is the "Free-WiLi Whale Tail Badge," sold at the ICS
    Village booth to support ICS Village events.
- kind: url
  url: https://web.archive.org/web/20241014122935/https://freewili.com/products/whale-tail/
  title: 'Whale Tail - FreeWili (archived product page)'
  accessed: '2026-09-06'
  note: Maker's own product page - description, features, chip, LEDs, interfaces.
- kind: repo
  url: https://github.com/freewili/whaletail-examples
  title: freewili/whaletail-examples
  accessed: '2026-09-06'
  note: Example firmware for 10BASE-T1L and the Sensor Loop Drive; no hardware
    design files found in the freewili GitHub org for this specific board.
images:
  - file: assets/images/badges/dc32/ics-village-unnamed-badge-sao/28c07b663b.jpg
    source: "https://freewili.com/products/whale-tail/"
    credit: "FreeWili"
    caption: "Free-WiLi Whale Tail Badge, front"
contact: {}
notes:
- Sheet listed this only as "ICS Village (unnamed badge/SAO)"; identified via
  ICS Village's own DEF CON 32 event page as the "Free-WiLi Whale Tail Badge."
status: released
sources:
- kind: sheet
  event: dc32
  row: 69
  updated: '2024-07-30'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The maker's freewili.com site is now offline (returns 404); all detail
    comes from Wayback Machine snapshots. Could not confirm quantity made, exact
    price breakdown (kit vs. assembled, the sheet's "$60/$70" is unconfirmed
    elsewhere), or whether hardware design files (KiCad/Gerbers) were ever
    published for this specific board - only firmware examples were found.
    Not to be confused with "DEFCON32_FREEWiLi," FreeWili's separate re-flash
    of the official DEF CON 32 human badge, which is a different product from
    the same maker.
last_modified_date: '2026-09-06'
---

The Free-WiLi Whale Tail Badge was sold through the ICS Village booth at DEF CON 32
(2024) to help fund ICS Village's programming. It was made by FreeWili, the team
behind the FREE-WiLi handheld hacking platform, and is built around a Raspberry Pi
RP2040 microcontroller. Rather than being a typical blinky con badge, it is pitched
as a learning and bench tool for protocols used in industrial and automotive
settings: it carries an Analog Devices ADIN1110-based 10BASE-T1L interface (so it
can act as a USB-to-10BASE-T1L adapter), a Microchip MCP2518FD-based CAN FD
interface compatible with the CANIS Labs CANPICO, and an RS485 Modbus interface,
alongside a 4-20mA industrial sensor simulator.

Beyond the industrial-protocol hardware, the badge has six serial RGB LEDs, two
capacitive-touch buttons, and an expansion plug that lets it take FreeWili display,
power, and wireless add-on modules. FreeWili's GitHub org publishes example
firmware for the board's 10BASE-T1L and "Sensor Loop Drive" features
(`whaletail-examples`) and a Docusaurus-based documentation site, but no hardware
design files (KiCad project or Gerbers) specific to this board were found, so it is
recorded here as only partially open source.

It should not be confused with "DEFCON32_FREEWiLi," a separate FreeWili product
that is a from-scratch firmware re-flash for the official DEF CON 32 conference
badge itself (of which almost 30,000 were made) - a different item from the same
maker, also documented on freewili.com.
