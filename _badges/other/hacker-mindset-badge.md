---
title: Hacker Mindset Badge
id: other-hacker-mindset-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: Hacker Warehouse / Godai Group LLC (specific badge designer not credited on page)
  url: https://hackerwarehouse.com
summary: An RP2040-based electronic badge sold by Hacker Warehouse, tying into founder Garrett Gee's "Hacker Mindset" book/brand, with USB HID emulation, mass storage, and 14 RGB LEDs over two SAO ports.
functions: USB keyboard emulation (static strings, ducky/yubikey-style automations), USB mouse emulation (mouse jiggler), USB serial console, USB mass storage, 56 built-in LED patterns, and user-defined execution triggered by two buttons plus a capacitive touch button.
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - hardware tool
  - text
tech:
  mcu: RP2040
  leds:
    count: 14
    type: RGB
    note: 56 selectable LED patterns.
  display: none
  connectivity:
  - usb
  inputs:
  - buttons
  - capacitive
  battery: null
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: $80
  price_usd: 80.0
  quantity: ''
  availability: available
  availability_note: 'In stock on hackerwarehouse.com as of 2026-09-07.'
  distribution:
  - purchase
  where: Sold directly through the Hacker Warehouse online store.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackerwarehouse.com/product/hacker-mindset-badge
  url: https://hackerwarehouse.com/product/hacker-mindset-badge/
  kind: website
images:
  - file: assets/images/badges/other/hacker-mindset-badge/21ffd5af82.jpg
    source: "https://hackerwarehouse.com/product/hacker-mindset-badge/"
    credit: "Hacker Warehouse"
    caption: "The Hacker Mindset Badge, RP2040-based PCB badge"
contact: {}
notes:
- Hacker Warehouse storefront, listed under couture/badgelife category. $80. RP2040 MCU, 14 RGB LEDs, 2 buttons, USB HID keyboard/mouse emulation, 56 LED patterns, SAO v1.69bis expansion port. Listed for sale, no out-of-stock indicator.
- 'The archive already holds a separate, more fully researched entry for what appears to be this same badge at dc31-hacker-mindset-badge (title "Hacker Mindset Badge", maker "Garrett / Hacker Warehouse", event DEF CON 31, year 2023), which ties it to the launch of Garrett Gee''s "The Hacker Mindset" book. This entry''s own source (the current hackerwarehouse.com product page) does not itself state an event or year: the page carries no con name, and a web search for "Hacker Mindset" book/badge found the book''s own listed publish date as June 11, 2024, which is inconsistent with a 2023 DEF CON 31 tie-in and was not resolved from sources read here. The product photo filenames are dated in a 2023/09 upload path, consistent with (but not proof of) a DEF CON 31 (Aug 2023) release.'
status: listed
sources:
- kind: url
  url: https://hackerwarehouse.com/product/hacker-mindset-badge/
  title: Hacker Mindset Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://hackerwarehouse.com/product/hacker-mindset-badge/
  title: Hacker Mindset Badge - Hacker Warehouse
  accessed: '2026-09-07'
  note: 'Confirmed specs (RP2040, 8MB flash, 14 RGB LEDs, 56 patterns, 2 buttons + capacitive touch, 2x SAO v1.69bis + 4 IO, USB HID/mass storage), price $80, in-stock status, and image URLs. No event/year stated on the page.'
- kind: url
  url: https://hackerwarehouse.com/couture/badgelife/
  title: Badgelife Archives - Hacker Warehouse
  accessed: '2026-09-07'
  note: 'Storefront category listing; no additional background, event, or designer credit for this badge found.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'The current hackerwarehouse.com product page gives full hardware specs but names no specific convention, year, or individual designer (page only reads "Hacker Warehouse / Godai Group LLC"). A likely duplicate exists at dc31-hacker-mindset-badge with the same title and specs, attributing it to DEF CON 31 (2023) and Garrett Gee''s "Hacker Mindset" book launch; that attribution was not independently confirmed from the sources read for this entry (the book''s own page gives a 2024 publish date), so event/year were left as-is here rather than copied. Quantity made and any open-source design files were not found. Flagging as duplicate rather than merging per instructions.'
last_modified_date: '2026-09-07'
---

The Hacker Mindset Badge is an RP2040-powered electronic conference badge sold through the Hacker Warehouse online store. It runs on an RP2040 microcontroller with 8 MB of SPI flash and drives 14 RGB LEDs through 56 selectable lighting patterns. Two physical buttons and a capacitive touch button trigger user-defined actions, and the badge can emulate a USB keyboard (for static strings and ducky/YubiKey-style automations), a USB mouse (as a "mouse jiggler"), a USB serial console, and USB mass storage. It carries two fully wired SAO v1.69bis expansion headers plus four additional IO pins for other add-ons.

The badge's name and artwork tie it to Hacker Warehouse founder Garrett Gee's "Hacker Mindset" brand and book. The storefront page itself does not name a specific convention or year, and no separate project page, repository, or press coverage describing its debut was found. It is priced at $80 and, as of this check, still listed as in stock.

This entry is very likely a duplicate of the archive's existing `dc31-hacker-mindset-badge` entry, which carries the same title and technical specifications but attributes the badge to DEF CON 31 (2023) as a companion to the book's launch. That event/year attribution could not be independently verified from the sources consulted here, so this entry has been left without an event correction; see `research.notes` for the discrepancy found (the book's own listed publish date is June 2024).
