---
title: 2024 Aerospace Village Badge
id: dc32-aerospace-village-unnamed-badge-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Aerospace Village
  url: https://www.aerospacevillage.org/dc32-badge
summary: A self-contained ADS-B receiver badge for DEF CON 32 that is also a full Linux single-board computer, natively decoding and displaying nearby aircraft from their 1090 MHz transmissions.
functions: Receives and displays live aircraft positions via ADS-B (1090 MHz) with GPS own-ship position on a moving map; exposes Dump1090 data over Wi-Fi or USB Ethernet; plays video and emulates retro video games; supports SSH and USB-keyboard terminal access; expandable via microSD; included a hidden CTF-style puzzle hunt.
look:
  colors: []
  shape: rectangle
  themes:
  - radio
  - security
  - hardware tool
tech:
  mcu: unknown (Linux SBC, dual-core, repurposed/reverse-engineered chip per maker and reviewer)
  leds: null
  display: null
  connectivity:
  - wifi
  - usb
  - uart
  - i2c
  - gps
  battery: 18650 (replaceable), USB-C PD fast charging
  sao_version: null
get_one:
  price: $160.00
  price_usd: 160.0
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing marked "Discontinued" as of 2026-09-06; badges were also sold in person at Aerospace Village during DEF CON 32.
  distribution:
  - purchase
  - village
  where: Sold during DEF CON 32 at the Aerospace Village and via the Aerospace Village's Tindie store (sales opened publicly on Tindie in October 2024 after the con).
make_your_own:
  open_source: yes
  hardware_url: https://github.com/AerospaceVillage/avBadge_2024
  firmware_url: https://github.com/AerospaceVillage/avBadge_2024
  eda_tool: null
  fab_url: null
  notes: Repo includes hardware files, WingletOS build instructions, a development tutorial, an FAQ, and links to community-made 3D-printed cases (stand, travel case, bumper, bezel).
links:
- kind: website
  label: DC32 Badge page (Aerospace Village)
  url: https://www.aerospacevillage.org/dc32-badge
- kind: repo
  label: avBadge_2024 (GitHub)
  url: https://github.com/AerospaceVillage/avBadge_2024
- kind: store
  label: 2024 Aerospace Village Badge (Tindie, discontinued)
  url: https://www.tindie.com/products/aero_village/2024-aerospace-village-badge/
- kind: article
  label: "Adafruit blog: The Aerospace Village badge for DEF CON 32 is an aircraft position display"
  url: https://blog.adafruit.com/2024/07/30/the-aerospace-village-badge-for-def-con-32-is-an-aircraft-position-display/
images:
- file: assets/images/badges/dc32/aerospace-village-unnamed-badge-sao/1cafb1eeee.jpg
  source: "https://www.tindie.com/products/aero_village/2024-aerospace-village-badge/"
  credit: "Aerospace Village"
  caption: "Front of the 2024 Aerospace Village DC32 badge, showing the ADS-B display"
- file: assets/images/badges/dc32/aerospace-village-unnamed-badge-sao/1602e5ec3c.jpg
  source: "https://www.tindie.com/products/aero_village/2024-aerospace-village-badge/"
  credit: "Aerospace Village"
  caption: "Back of the 2024 Aerospace Village DC32 badge"
contact: {}
notes:
- "Sheet listed this row only as an unnamed Aerospace Village item at $160; research identified it as the official 2024 Aerospace Village Badge (the village's main DC32 badge, not a separate SAO)."
status: released
sources:
- kind: sheet
  event: dc32
  row: 8
  updated: '2024-07-29'
- kind: url
  url: https://www.aerospacevillage.org/dc32-badge
  title: DC32 Badge | Aerospace Village
  accessed: '2026-09-06'
  note: Feature list, distribution context, and confirmation this is the main DC32 badge.
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2024
  title: "GitHub: AerospaceVillage/avBadge_2024"
  accessed: '2026-09-06'
  note: Open-source hardware/firmware repo, README description, case links, software release tags.
- kind: url
  url: https://www.tindie.com/products/aero_village/2024-aerospace-village-badge/
  title: 2024 Aerospace Village Badge (Tindie)
  accessed: '2026-09-06'
  note: Confirmed price ($160.00), discontinued/sold-out status, product images, and a buyer review.
- kind: url
  url: https://blog.adafruit.com/2024/07/30/the-aerospace-village-badge-for-def-con-32-is-an-aircraft-position-display/
  title: "Adafruit: The Aerospace Village badge for DEF CON 32 is an aircraft position display"
  accessed: '2026-09-06'
  note: Corroborating description of features and team involvement.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: >-
    The sheet row gave no title, only a $160 price and "Selling during DEFCON at the
    Aerospace Village." Cross-referencing the Aerospace Village's own DC32 badge page,
    their GitHub repo, and the Tindie store (which lists the exact same $160.00 price
    and DC32 description) confirms this is the "2024 Aerospace Village Badge" itself,
    not a separate unnamed SAO. Could not confirm exact quantity made, specific SoC part
    number, LED count/type, or display size/type from public sources; left those fields
    empty rather than guess. The Tindie listing is now marked discontinued.
last_modified_date: '2026-09-06'
---

The 2024 Aerospace Village Badge for DEF CON 32 is a self-contained ADS-B receiver: it decodes 1090 MHz transmissions that most aircraft broadcast and plots them on a live moving map alongside the badge's own GPS position, using ordinary components rather than a dedicated SDR front end. Beyond that headline feature, it is a full Linux single-board computer with Wi-Fi, a dual-core processor, 128MB of DDR3 RAM, and 8GB of eMMC storage, expandable with a user-supplied microSD card. Wearers could SSH in, plug a keyboard into its USB port for a terminal, expose the underlying Dump1090 data over Wi-Fi or USB Ethernet, play video, or run game emulators. It also carried an SAO connector supporting I2C, UART, and CAN bus, a replaceable 18650 battery with USB-C PD fast charging, and a hidden CTF-style puzzle hunt for attendees to find.

The badge was sold in person at the Aerospace Village during DEF CON 32 and later opened to the public on the village's Tindie store in October 2024 for $160, where it has since sold out and is now listed as discontinued. Hardware and firmware are both open-sourced on GitHub (`AerospaceVillage/avBadge_2024`), including a development tutorial, build instructions for its "WingletOS," and links to several community-designed 3D-printed cases. The same badge hardware was carried forward into DEF CON 33 with new software rather than a new board.

## Make your own

The hardware and firmware are published at https://github.com/AerospaceVillage/avBadge_2024, which includes the badge's hardware files, instructions for building its custom "WingletOS" Linux image, a widget-development tutorial, and an FAQ. Software releases are tagged v1.1 and v2.0 in the repo. Community members have also published separate 3D-printable case designs (a stand-equipped case, a travel case, a bumper case, and a bezel) linked from the repo's README.
