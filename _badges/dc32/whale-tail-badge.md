---
title: Whale Tail Badge
id: dc32-whale-tail-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: FREE-WILi
  url: https://freewili.com/
  role: hardware
- name: DEF CON ICS Village
  url: https://www.icsvillage.com/
  role: partner/distribution
summary: A programmable industrial-control-systems badge built by FREE-WILi with DEF CON's ICS Village for DEF CON 32, exposing CAN FD, 10BASE-T1L, and RS485 Modbus interfaces alongside RGB LEDs and touch sensors.
functions: Lets attendees experiment with ICS/industrial fieldbus protocols (CAN FD, 10BASE-T1L, RS485 Modbus, 4-20mA sensor simulation); drives 6 programmable RGB LEDs via 2 capacitive touch sensors; expansion plug accepts other FREE-WILi modules (display, power, wireless).
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - radio
tech:
  mcu: RP2040
  leds:
    count: 6
    type: RGB
    note: Programmable, touch-controlled.
  display: none
  connectivity:
  - usb
  battery: USB-C
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed via DEF CON 32 ICS Village (badgelife/DC32, 2024); a related "WhaleTail Badge Orca" module is later listed for sale on the FREE-WILi storefront.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'The GitHub repo linked from the docs site (freewili/whaletale_webdocs) is the Docusaurus documentation site itself, not a hardware/firmware repo; no KiCad files, gerbers, or firmware source were found.'
links:
- label: whaletail.freewili.com/introduction-and-overview
  url: https://whaletail.freewili.com/introduction-and-overview/
  kind: website
- label: FREE-WILi
  url: https://freewili.com/
  kind: website
- label: WhaleTail Badge Orca (FREE-WILi store)
  url: https://freewili.com/products/orca-modules/whaletail-badge-orca/
  kind: store
- label: 'FREE-WiLi on X: badge announcement'
  url: https://twitter.com/FREE_WiLi_/status/1822056672027898010
  kind: social
images:
- file: assets/images/badges/dc32/whale-tail-badge/d48c11a94c.png
  source: "https://whaletail.freewili.com/introduction-and-overview/"
  credit: "FREE-WILi"
  caption: "Whale Tail Badge, front view"
- file: assets/images/badges/dc32/whale-tail-badge/f2cfa06108.jpg
  source: "https://whaletail.freewili.com/introduction-and-overview/"
  credit: "FREE-WILi"
  caption: "Whale Tail Badge, back view"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'A successor badge, "icsvillage-badge-defcon33", extends this design for DEF CON 33 (2025) with a full-color PCB by artist Kyle Irving, per freewili/FreeWili_WebDocs; that is a separate item and not covered by this entry.'
status: released
sources:
- kind: url
  url: https://whaletail.freewili.com/introduction-and-overview/
  title: Whale Tail Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''unknown''.'
- kind: url
  url: https://freewili.com/
  title: FREE-WILi
  accessed: '2026-09-07'
  note: Confirmed maker identity and site.
- kind: url
  url: https://twitter.com/FREE_WiLi_/status/1822056672027898010
  title: 'FREE-WiLi on X: Whale Tail Badge announcement'
  accessed: '2026-09-07'
  note: Confirms DEF CON 32 / ICS Village / badgelife / 2024 (#defcon32, #df32, #icsvillage).
- kind: url
  url: https://github.com/freewili/FreeWili_WebDocs/blob/main/docs/defcon-badges/icsvillage-badge-defcon33.md
  title: ICS Village Badge for DEF CON 33 docs
  accessed: '2026-09-07'
  note: Confirms this Whale Tail badge was the DEF CON 32 (2024) predecessor to a DEF CON 33 successor badge.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'No price, quantity, or open-source hardware/firmware files could be confirmed. The GitHub repo linked from the docs site is documentation-only. A related product, "WhaleTail Badge Orca," is later sold on the FREE-WILi storefront but its relationship to the free DEF CON 32 badge (same hardware vs. a commercial follow-on) is not stated by sources, so get_one/where notes this without asserting a sale price for the original badge.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/whale-tail-badge/
---

The Whale Tail Badge is a programmable industrial control systems (ICS) badge that FREE-WILi built together with DEF CON's ICS Village for DEF CON 32 in 2024. Rather than a typical blinky electronic badge, it doubles as a hands-on tool for exploring fieldbus and industrial networking protocols: it exposes a CAN FD interface (via a Microchip MCP2518FD controller), a 10BASE-T1L interface for long-distance low-speed Ethernet, an RS485 Modbus interface, and a 4-20mA current-loop sensor simulator, alongside six programmable RGB LEDs driven by two capacitive touch pads. An RP2040 microcontroller runs the show, and an expansion plug lets the badge take other FREE-WILi modules such as displays, power boards, or wireless add-ons. It shipped with a USB-C cable, RF-controlled LED bracelets, and a compatibility connector for other FREE-WILi devices.

The badge was sponsored by Microchip and Analog Devices as part of ICS Village's presence at DEF CON 32, and FREE-WILi promoted it on social media under the badgelife and #df32 tags. Full hardware design files, gerbers, and firmware source were not found; the GitHub repository linked from the badge's documentation site is the Docusaurus-based documentation site itself rather than a hardware repo, so open-source status is only partial pending further files being published.

## History

FREE-WILi and ICS Village followed this badge with a second-generation "ICS Village Badge" for DEF CON 33 (2025), which expands on the Whale Tail's ICS/fieldbus focus with an emphasis on physical and environmental exploitation, and features a full-color PCB designed by Detroit artist Kyle Irving. That DEF CON 33 badge is a distinct item and would need its own archive entry.
