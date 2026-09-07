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
  source: "https://hackerwarehouse.com/product/hacker-mindset-badge/"
  credit: "Hacker Warehouse"
  caption: "The Hacker Mindset Badge, front view showing RGB LEDs and artwork"
- file: assets/images/badges/dc31/hacker-mindset-badge/6582272f33.jpg
  source: "https://hackerwarehouse.com/product/hacker-mindset-badge/"
  credit: "Hacker Warehouse"
  caption: "The Hacker Mindset Badge, angled view showing SAO ports and buttons"
contact: {}
notes:
- rp2040 (<-- everyones favorite awesome plaything this year), 14 rgb leds, buttons, etc
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
  note: Full feature list, hardware specs (RP2040, 8MB SPI flash, 14 RGB LEDs, 2
    buttons, 1 capacitive touch button, 2 SAO v1.69bis ports, 4 expansion IO ports),
    SKU THM-HMB, original $110 pre-order price, and confirmation it was made to
    support the launch of "The Hacker Mindset" book (published June 2024). Also
    the source of the two product photos saved to this entry.
- kind: url
  url: https://hackerwarehouse.com/product/hacker-mindset-badge/
  title: Hacker Mindset Badge — Hacker Warehouse (current listing)
  accessed: '2026-09-07'
  note: Confirms the badge is still listed for sale, now at $80.00.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No open-source hardware/firmware files, GitHub repo, or Hackaday.io project
    page were found for this badge; make_your_own fields are left empty rather than
    guessed. Battery/power source is not stated on the product page (the badge runs
    over USB for its HID/mass-storage functions, but that isn't the same as a stated
    power spec, so tech.battery is left null). The book itself, "The Hacker Mindset,"
    is only described as launching June 2024; its author is not named on the
    product page and was not independently confirmed, so no author is recorded
    here. Price changed between the DC31-era pre-order ($110, which included the
    book) and the current standalone listing ($80); both are noted.
last_modified_date: '2026-09-07'
---

Hacker Warehouse, the security-tools retailer run by Garrett, sold the Hacker Mindset Badge at DEF CON 31 in 2023 as a tie-in for "The Hacker Mindset," a book the company had in the works at the time (it would go on to publish in June 2024). The badge is an RP2040 board built around USB tricks rather than a display or radio: it can emulate a USB keyboard to fire off static strings or Ducky/YubiKey-style automations, act as a USB mouse jiggler, present a USB serial console, and mount itself as USB mass storage, all selectable through 56 built-in LED patterns and two buttons whose behavior the user can define. Hardware-wise it packs 14 RGB LEDs, a capacitive touch button alongside the two physical ones, 8 MB of SPI flash, two fully wired SAO v1.69bis ports, and four expansion IO pins, with "The Hacker Mindset" artwork silkscreened across the board.

At launch it was sold as a $110 pre-order bundle tied to the book (US customers only, due to translation rights elsewhere), available both online and in person at the Hacker Warehouse booth. As of this research pass the badge is still listed for sale on hackerwarehouse.com, now on its own at $80. No open-source hardware, firmware repository, or Hackaday.io project page could be located for it, so it appears to be a closed-design product rather than a badgelife community release.
