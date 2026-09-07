---
title: MCH2022 Badge
id: dc32-mch2022-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Badge.team
  url: https://badge.team/
summary: The official badge for May Contain Hackers 2022 (MCH2022) in the Netherlands, a Game Boy Advance-shaped handheld built around an ESP32, an RP2040, and a Lattice iCE40UP5K FPGA, listed on the DC32 sheet as an out-of-band group buy rather than a DEF CON badge.
functions: It's got an ICE40UP5K FPGA that can control the display, it plays Doom, Out of This World and Gameboy games. You can publish apps at mch2022.badge.team which can then be downloaded via the badge itself.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - console
  - hardware tool
tech:
  mcu: ESP32 WROVER-E + RP2040 + iCE40UP5K FPGA
  leds:
    count: null
    type: SK6812-EC15
    note: Addressable RGB (Neopixel-compatible), driven by the RP2040.
  display: 2.4" ILI9341 TFT (Z240IT008 panel)
  connectivity:
  - wifi
  - usb
  battery: LiPo via JST S2B-ZR-SM4A-TF connector (capacity not specified by the maker)
  sao_version: v2
  sao_ports: 1
get_one:
  price: €80.00
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold/preordered directly through Badge.team ahead of the MCH2022 event in the Netherlands; shipping was from the Netherlands and priced in euros.
make_your_own:
  open_source: true
  hardware_url: https://github.com/badgeteam/mch2022-badge-hardware
  firmware_url: https://github.com/badgeteam/mch2022-firmware-esp32
  eda_tool: null
  license: CERN-OHL-P
  notes: Hardware repo is archived (read-only) as of March 2026. ESP32 and RP2040 firmware are maintained in separate repos.
links:
- label: badge.team/docs/badges/mch2022
  url: https://badge.team/docs/badges/mch2022/
  kind: website
  archived: https://web.archive.org/web/20260725092331/https://badge.team/docs/badges/mch2022/
- label: github.com/badgeteam/mch2022-badge-hardware
  url: https://github.com/badgeteam/mch2022-badge-hardware
  kind: repo
  archived: https://web.archive.org/web/20260122054412/https://github.com/badgeteam/mch2022-badge-hardware
images:
- file: assets/images/badges/dc32/mch2022-badge/8ac8f9c368.jpg
  source: https://badge.team/docs/badges/mch2022/
  credit: Badge.team
  caption: MCH2022 badge overview
  archived: https://web.archive.org/web/20260725092331/https://badge.team/docs/badges/mch2022/
contact:
  emails:
  - defcon32@badge.team
notes:
- Pay attention to the currency. This price is in Euros and shipping from the Netherlands will need to be included (I will be buying one and I will list the total amount when it goes through). You may buy as many badges at once that you wish.
status: released
sources:
- kind: sheet
  event: dc32
  row: 15
  updated: '2024-06-03'
- kind: url
  url: https://badge.team/docs/badges/mch2022/
  title: MCH2022 badge - badge.team docs
  accessed: '2026-09-06'
  note: Maker/team, form factor, display and LED chip references, price context, overview photo.
  archived: https://web.archive.org/web/20260725092331/https://badge.team/docs/badges/mch2022/
- kind: url
  url: https://github.com/badgeteam/mch2022-badge-hardware
  title: badgeteam/mch2022-badge-hardware
  accessed: '2026-09-06'
  note: MCUs, SAOv2 support, license, credits for artwork and electronics design; repo now archived.
  archived: https://web.archive.org/web/20260122054412/https://github.com/badgeteam/mch2022-badge-hardware
- kind: url
  url: https://hackaday.com/2022/05/04/the-mch2022-badge-has-landed/
  title: The MCH2022 Badge Has Landed - Hackaday
  accessed: '2026-09-06'
  note: Confirms large color TFT, addressable LEDs, Game Boy Advance-style form factor, joystick/buttons, Bosch sensors, stereo audio with onboard speaker.
  archived: https://web.archive.org/web/20260309100410/https://hackaday.com/2022/05/04/the-mch2022-badge-has-landed/
- kind: url
  url: https://badge.team/docs/badges/mch2022/hardware/
  title: MCH2022 badge hardware - badge.team docs
  accessed: '2026-09-06'
  note: Display panel (ILI9341/Z240IT008) and LED part number (SK6812-EC15); confirms SAO connector I/O broken out from the RP2040.
  archived: https://web.archive.org/web/20260513010609/https://badge.team/docs/badges/mch2022/hardware/
- kind: url
  url: https://badge.team/docs/badges/mch2022/hardware/battery/
  title: MCH2022 badge battery - badge.team docs
  accessed: '2026-09-06'
  note: Confirms LiPo connector type (JST S2B-ZR-SM4A-TF); capacity not stated.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: This entry is not a DEF CON 32 badge; it was a Badge.team group-buy listing that ended up on the DC32 community sheet (note in the sheet explains the buyer was arranging a bulk EU order). Exact LED count and battery capacity are not published by the maker. Quantity made/sold and current availability were not found; hardware repo is archived as of March 2026 so it is likely no longer sold new. PCB colors/shape not confirmed from a source describing them explicitly (photo shows a Game Boy Advance-style handheld shell, but front matter "look" fields were left conservative pending a clearer source).
last_modified_date: '2026-09-06'
---

The MCH2022 badge was the official conference badge for May Contain Hackers 2022, a Dutch outdoor hacker camp held in August 2022, produced by the volunteer collective Badge.team. It appeared on the DEF CON 32 community badge sheet not because it was a DEF CON badge, but because someone was organizing a bulk overseas order for interested DEF CON attendees — the sheet row explicitly flags the price as euros and mentions arranging shipping from the Netherlands.

Physically it takes the form of a Game Boy Advance-style handheld: a joystick and buttons flank a 2.4" ILI9341 color TFT display, backed by SK6812-EC15 addressable RGB LEDs. Under the hood it combines three processors — an Espressif ESP32 WROVER-E (16MB flash, 8MB PSRAM) for WiFi and applications, a Raspberry Pi RP2040 for USB and board management, and a Lattice iCE40UP5K FPGA for hardware-accelerated graphics — plus Bosch environmental/motion sensors and a stereo audio path with an onboard speaker. It exposes a single SAOv2 connector wired to RP2040 I/O. Badge.team's companion web app store, the Hatchery, let attendees publish and download apps (including Doom, Out of This World, and Game Boy ports) directly to the badge.

Hardware and firmware are open source: the hardware repository is licensed CERN-OHL-P, with artwork credited to Nikolett S. of tilde.industries and electronics engineering credited to Renze Nicolai of Nicolai Electronics, alongside a larger volunteer debugging/routing team. As of research time the hardware repo has been archived (read-only) on GitHub, and no current storefront listing or production-quantity figure could be found.
