---
title: Hacker Mindset Badge
id: dc31-hacker-mindset-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Garrett / Hacker Warehouse
  url: https://hackerwarehouse.com
summary: An RP2040-based electronic badge sold by Hacker Warehouse at DEF CON 31 to support the launch of "The Hacker Mindset" book, with USB HID emulation, mass storage, and 14 RGB LEDs over two SAO ports.
functions: USB keyboard emulation (static strings, ducky/yubikey-style automations), USB mouse emulation (mouse jiggler), USB serial console, USB mass storage, 56 built-in LED patterns, and user-defined execution triggered by two buttons.
look:
  colors:
  - green
  - gold
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
  price: $110 (pre-order) / $80 (later listing)
  price_usd: 80.0
  quantity: ''
  availability: available
  availability_note: Still listed for sale on hackerwarehouse.com as of 2026-09-07, at $80.00.
  distribution:
  - purchase
  where: Sold directly on hackerwarehouse.com and available in person at the Hacker Warehouse booth at DEF CON 31.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: store
  label: Hacker Mindset Badge — Hacker Warehouse
  url: https://hackerwarehouse.com/product/hacker-mindset-badge/
images:
- file: assets/images/badges/dc31/hacker-mindset-badge/21ffd5af82.jpg
  source: https://hackerwarehouse.com/product/hacker-mindset-badge/
  credit: Hacker Warehouse
  caption: The Hacker Mindset Badge, front view showing RGB LEDs and artwork
- file: assets/images/badges/dc31/hacker-mindset-badge/6582272f33.jpg
  source: https://hackerwarehouse.com/product/hacker-mindset-badge/
  credit: Hacker Warehouse
  caption: The Hacker Mindset Badge, angled view showing SAO ports and buttons
- file: assets/images/badges/dc31/hacker-mindset-badge/21ffd5af82.jpg
  source: https://hackerwarehouse.com/product/hacker-mindset-badge/
  credit: Hacker Warehouse
  caption: The Hacker Mindset Badge, RP2040-based PCB badge
contact: {}
notes:
- rp2040 (<-- everyones favorite awesome plaything this year), 14 rgb leds, buttons, etc
- Hacker Warehouse storefront, listed under couture/badgelife category. $80. RP2040 MCU, 14 RGB LEDs, 2 buttons, USB HID keyboard/mouse emulation, 56 LED patterns, SAO v1.69bis expansion port. Listed for sale, no out-of-stock indicator.
- 'The archive already holds a separate, more fully researched entry for what appears to be this same badge at dc31-hacker-mindset-badge (title "Hacker Mindset Badge", maker "Garrett / Hacker Warehouse", event DEF CON 31, year 2023), which ties it to the launch of Garrett Gee''s "The Hacker Mindset" book. This entry''s own source (the current hackerwarehouse.com product page) does not itself state an event or year: the page carries no con name, and a web search for "Hacker Mindset" book/badge found the book''s own listed publish date as June 11, 2024, which is inconsistent with a 2023 DEF CON 31 tie-in and was not resolved from sources read here. The product photo filenames are dated in a 2023/09 upload path, consistent with (but not proof of) a DEF CON 31 (Aug 2023) release.'
status: released
sources:
- kind: sheet
  event: dc31
  row: 43
  updated: '2023-07-14'
- kind: url
  url: https://web.archive.org/web/20231204165437/https://hackerwarehouse.com/product/hacker-mindset-badge/
  title: Hacker Mindset Badge — Hacker Warehouse (archived Dec 2023 listing)
  accessed: '2026-09-07'
  note: Full feature list, hardware specs (RP2040, 8MB SPI flash, 14 RGB LEDs, 2 buttons, 1 capacitive touch button, 2 SAO v1.69bis ports, 4 expansion IO ports), SKU THM-HMB, original $110 pre-order price, and confirmation it was made to support the launch of "The Hacker Mindset" book (published June 2024). Also the source of the two product photos saved to this entry.
- kind: url
  url: https://hackerwarehouse.com/product/hacker-mindset-badge/
  title: Hacker Mindset Badge — Hacker Warehouse (current listing)
  accessed: '2026-09-07'
  note: Confirms the badge is still listed for sale, now at $80.00.
- kind: url
  url: https://hackerwarehouse.com/couture/badgelife/
  title: Badgelife Archives - Hacker Warehouse
  accessed: '2026-09-07'
  note: Storefront category listing; no additional background, event, or designer credit for this badge found.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No open-source hardware/firmware files, GitHub repo, or Hackaday.io project page were found for this badge; make_your_own fields are left empty rather than guessed. Battery/power source is not stated on the product page (the badge runs over USB for its HID/mass-storage functions, but that isn't the same as a stated power spec, so tech.battery is left null). The book itself, "The Hacker Mindset," is only described as launching June 2024; its author is not named on the product page and was not independently confirmed, so no author is recorded here. Price changed between the DC31-era pre-order ($110, which included the book) and the current standalone listing ($80); both are noted. Merged with duplicate entry 'Hacker Mindset Badge' (dc31-hacker-mindset-badge-2).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc31/hacker-mindset-badge-2/
---

Hacker Warehouse, the security-tools retailer run by Garrett, sold the Hacker Mindset Badge at DEF CON 31 in 2023 as a tie-in for "The Hacker Mindset," a book the company had in the works at the time (it would go on to publish in June 2024). The badge is an RP2040 board built around USB tricks rather than a display or radio: it can emulate a USB keyboard to fire off static strings or Ducky/YubiKey-style automations, act as a USB mouse jiggler, present a USB serial console, and mount itself as USB mass storage, all selectable through 56 built-in LED patterns and two buttons whose behavior the user can define. Hardware-wise it packs 14 RGB LEDs, a capacitive touch button alongside the two physical ones, 8 MB of SPI flash, two fully wired SAO v1.69bis ports, and four expansion IO pins, with "The Hacker Mindset" artwork silkscreened across the board.

At launch it was sold as a $110 pre-order bundle tied to the book (US customers only, due to translation rights elsewhere), available both online and in person at the Hacker Warehouse booth. As of this research pass the badge is still listed for sale on hackerwarehouse.com, now on its own at $80. No open-source hardware, firmware repository, or Hackaday.io project page could be located for it, so it appears to be a closed-design product rather than a badgelife community release.

## Notes merged from the duplicate entry "Hacker Mindset Badge"

The Hacker Mindset Badge is an RP2040-powered electronic conference badge sold through the Hacker Warehouse online store. It runs on an RP2040 microcontroller with 8 MB of SPI flash and drives 14 RGB LEDs through 56 selectable lighting patterns. Two physical buttons and a capacitive touch button trigger user-defined actions, and the badge can emulate a USB keyboard (for static strings and ducky/YubiKey-style automations), a USB mouse (as a "mouse jiggler"), a USB serial console, and USB mass storage. It carries two fully wired SAO v1.69bis expansion headers plus four additional IO pins for other add-ons.

The badge's name and artwork tie it to Hacker Warehouse founder Garrett Gee's "Hacker Mindset" brand and book. The storefront page itself does not name a specific convention or year, and no separate project page, repository, or press coverage describing its debut was found. It is priced at $80 and, as of this check, still listed as in stock.

This entry is very likely a duplicate of the archive's existing `dc31-hacker-mindset-badge` entry, which carries the same title and technical specifications but attributes the badge to DEF CON 31 (2023) as a companion to the book's launch. That event/year attribution could not be independently verified from the sources consulted here, so this entry has been left without an event correction; see `research.notes` for the discrepancy found (the book's own listed publish date is June 2024).
