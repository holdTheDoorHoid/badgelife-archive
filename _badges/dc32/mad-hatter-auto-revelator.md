---
title: Mad Hatter Auto Revelator
id: dc32-mad-hatter-auto-revelator
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: The Mad Hatters
  url: https://madhatters.lol
summary: "A satirical DEF CON 32 badge from a Utah group, billed as a 'celestial intelligencer' that parodies seer stones and e-meters: a 3D-printed top hat sits over a small OLED you peer into, four capacitive 'handshake' pads drive a menu of Truth, Revelation, Magic 8 Ball and a Mad Hatter Meter, and 47 LEDs run 13 light modes."
functions: "Menu of Truth, Revelation and Magic 8 Ball (each with a hidden NSFW mode unlocked by a secret handshake and password); Mad Hatter Meter, a parody e-meter that reads the capacitive touch pads and reports TEST, SET, RISE or FALL; 13 LED modes (Mad Hatter, Celestial Clouds, Gone to Hell, Secret Combination, The Salamander, Tapir Joyride, Suppressive Badge, Thetan Possession, Seer Stones, Drunk as Hell, Gone Clear, American Jesus, DC 32); Display Handle, which stores your handle persistently in the 'Akashic Record'; hidden puzzles; About screen. Navigation is by four capacitive handshake pads (menu/exit, up, down, select)."
look:
  colors:
  - black
  shape: circle
  themes:
  - meme
  - puzzle
  form_factor: pcb badge
tech:
  mcu: ESP32-S2-SOLO-2
  leds:
    count: 47
    type: SK6812
    note: "Maker lists 9 regular LEDs and 38 addressable LEDs. The BOM shows SK6812MINI on the main board and SK6812-SIDE-A side-firing LEDs on the upper and lower boards, plus discrete red and yellow LEDs and a UV power indicator."
  display: 0.96" OLED
  connectivity:
  - usb
  - i2c
  - uart
  inputs:
  - capacitive
  - buttons
  power: "Micro USB or 3x AA, regulated to 3.3 V, with a slide switch to pick USB or battery"
  battery: 3x AA
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: $100.00
  price_usd: 100.0
  quantity: '100'
  availability: unknown
  availability_note: "The maker's page and repository README say the badge was available at Hacker Warehouse during DC32. A hackerwarehouse.com product search on 2026-09-06 returned only HackRF One listings, so current availability is unknown."
  distribution:
  - purchase
  where: Hacker Warehouse at DEF CON 32 (Las Vegas, August 2024), per the maker's page.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/the-mad-hatters/defcon2024badge/tree/main/hardware
  firmware_url: https://github.com/the-mad-hatters/defcon2024badge/tree/main/firmware
  bom_url: https://github.com/the-mad-hatters/defcon2024badge/blob/main/hardware/mad_hatter_bom.xlsx
  gerbers_url: https://github.com/the-mad-hatters/defcon2024badge/tree/main/hardware
  eda_tool: KiCad
  license: MIT
  notes: "Three KiCad boards (main board, upper 'top text' board, lower 'bottom text' board) with schematics, a spreadsheet BOM and a v3 zip per board containing Gerber and drill files (files dated 2024-05-30 for the two text boards and 2024-06-08 for the main board). Firmware is a PlatformIO project on the Arduino framework using FastLED and U8g2; prebuilt bootloader/partitions/firmware/spiffs binaries are on the GitHub releases page with esptool offsets. STLs for the top hat and a twist-lock hat adapter are in stl/ (remixes, CC BY 4.0 and CC BY-SA 4.0)."
links:
- label: madhatters.lol
  url: https://madhatters.lol
  kind: website
- label: GitHub repo (hardware, firmware, STLs)
  url: https://github.com/the-mad-hatters/defcon2024badge
  kind: repo
- label: Firmware releases (v1.3.2, v1.3.3)
  url: https://github.com/the-mad-hatters/defcon2024badge/releases
  kind: repo
- label: Flashing instructions (docs/firmware.md)
  url: https://github.com/the-mad-hatters/defcon2024badge/blob/main/docs/firmware.md
  kind: doc
- label: BoardRepo mirror of the KiCad project
  url: https://boardrepo.com/the-mad-hatters/defcon2024badge
  kind: website
- label: Top hats for the badge and SAO (Printables, by Brucifer)
  url: https://www.printables.com/model/935801-top-hats-for-the-mad-hatters-badge-and-sao-at-def
  kind: website
- label: Twist-lock hat adapters (Printables, by Brucifer)
  url: https://www.printables.com/model/964691-twist-lock-adapters-for-swapping-top-hats-for-the
  kind: website
images:
- file: assets/images/badges/dc32/mad-hatter-auto-revelator/ef53e95434.png
  source: "https://madhatters.lol/"
  credit: "The Mad Hatters"
  caption: "Front of the lit badge on its DC32 lanyard, with the OLED showing the three seer stones"
- file: assets/images/badges/dc32/mad-hatter-auto-revelator/907061bf8d.png
  source: "https://madhatters.lol/"
  credit: "The Mad Hatters"
  caption: "Angled view showing the 3D-printed top hat mounted over the OLED and the side-firing LEDs"
- file: assets/images/badges/dc32/mad-hatter-auto-revelator/d3294733c8.png
  source: "https://madhatters.lol/"
  credit: "The Mad Hatters"
  caption: "Badge in a blue LED mode, hat and handshake touch pads visible"
contact: {}
notes:
- https://madhatters.lol/ for information. Will be available at Hacker Warehouse at DC32
- "The maker's page styles the full name as 'Mad Hatter Auto Revelator, or Celestial Intelligencer'. A companion SAO, the Madragrammaton, was offered alongside it at Hacker Warehouse."
status: released
sources:
- kind: sheet
  event: dc32
  row: 107
  updated: '2024-07-06'
- kind: url
  url: https://madhatters.lol/
  title: Mad Hatter Auto Revelator (The Mad Hatters)
  accessed: '2026-09-06'
  note: "Maker's own page: description, navigation, menu, LED modes, specifications, GPIO map, Madragrammaton SAO, Hacker Warehouse availability, photos."
- kind: url
  url: https://github.com/the-mad-hatters/defcon2024badge
  title: GitHub - the-mad-hatters/defcon2024badge
  accessed: '2026-09-06'
  note: "Repository layout (hardware, firmware, docs, stl), MIT license, created December 2023, last pushed 2024-08-06."
- kind: url
  url: https://github.com/the-mad-hatters/defcon2024badge/releases
  title: Releases - the-mad-hatters/defcon2024badge
  accessed: '2026-09-06'
  note: "v1.3.2 'Seemingly stable' (2024-07-10) and v1.3.3 'Pre DefCon' (2024-08-06) with prebuilt binaries and flashing notes."
- kind: url
  url: https://github.com/the-mad-hatters/defcon2024badge/blob/main/hardware/mad_hatter_bom.xlsx
  title: mad_hatter_bom.xlsx (hardware BOM)
  accessed: '2026-09-06'
  note: "ESP32-S2-SOLO-2-N4R2 module, SK6812MINI and SK6812-SIDE-A LEDs, 128x64 I2C 0.96 inch OLED, 3xAA holder, micro USB, SAO connector, JLCPCB boards, 3D-printed hat."
- kind: url
  url: https://github.com/the-mad-hatters/defcon2024badge/blob/main/firmware/platformio.ini
  title: firmware/platformio.ini
  accessed: '2026-09-06'
  note: "PlatformIO, espressif32 platform, esp32-s2-saola-1 board, Arduino framework, FastLED and U8g2 libraries."
- kind: url
  url: https://github.com/the-mad-hatters/defcon2024badge/blob/main/docs/firmware.md
  title: docs/firmware.md
  accessed: '2026-09-06'
  note: "How the binaries are built and flashed with esptool or a web serial flasher; FLASH and RESET buttons for download mode."
- kind: url
  url: https://github.com/the-mad-hatters/defcon2024badge/blob/main/stl/README.md
  title: stl/README.md
  accessed: '2026-09-06'
  note: "Top hat and twist-lock adapter STLs, their Printables pages, and CC BY / CC BY-SA licenses with remix attribution."
- kind: url
  url: https://boardrepo.com/the-mad-hatters/defcon2024badge
  title: defcon2024badge - BoardRepo
  accessed: '2026-09-06'
  note: "Mirror of the KiCad project: 2 copper layers, 1.6 mm, MIT."
- kind: url
  url: https://github.com/the-mad-hatters
  title: the-mad-hatters (TheMadHatters) - GitHub
  accessed: '2026-09-06'
  note: "User account (not an organization) with a single public repository; no bio, location or names published."
- kind: url
  url: https://hackerwarehouse.com/?s=mad+hatter&post_type=product
  title: You searched for mad hatter - Hacker Warehouse
  accessed: '2026-09-06'
  note: "The store search for 'mad hatter' returns three results, all HackRF One listings (HackRF One (No Case) 35828, HackRF One 7088, HackRF One Bundle 262); there is no Mad Hatter or Madragrammaton product, so current availability is unknown."
- kind: url
  url: https://www.printables.com/model/935801-top-hats-for-the-mad-hatters-badge-and-sao-at-def
  title: Top Hats for The Mad Hatters Badge and SAO at DEF CON 32 by Brucifer (Printables)
  accessed: '2026-09-06'
  note: "Page is behind a Cloudflare check (HTTP 403); only the search-result title was readable, which supports the link label and the author name Brucifer."
- kind: url
  url: https://www.printables.com/model/964691-twist-lock-adapters-for-swapping-top-hats-for-the
  title: Twist-Lock Adapters for Swapping Top Hats for The Mad Hatters Badge and SAO at DEF CON 32 by Brucifer (Printables)
  accessed: '2026-09-06'
  note: "Page is behind a Cloudflare check (HTTP 403); only the search-result title was readable, which supports the link label and the author name Brucifer."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: "Fact-checked 2026-09-06 against every cited source. Name, Utah origin, navigation, menus, LED modes, specifications, SAO headers, the Madragrammaton SAO and Hacker Warehouse availability are confirmed on the maker's own page; LED part types, the OLED, power parts and JLCPCB fabrication by the repo BOM; build and flash steps by docs/firmware.md and the release notes; the three photos are the maker's own (pixel-identical to madhatters.lol images 1, 2 and 6). Price ($100) and quantity (100) come only from the community sheet row updated 2024-07-06; the maker gives neither. status: released is inferred rather than directly sourced: the maker says the badge was available at Hacker Warehouse during DC32, the final firmware was tagged 'Pre DefCon' on 2024-08-06 and the photos show finished badges on DC32 lanyards, but no post-con sales report, press coverage or owner posts were found. Individual maker names are not published (the GitHub account is a user account with no bio; the licence copyright reads 'TheMadHatters'). PCB colour and shape are judged from the maker's photos. The two Printables pages are behind a Cloudflare check; their titles and the author name Brucifer come only from search-result titles plus the repo's stl/README, and Brucifer's relationship to the maker group is unknown. Hacker Warehouse's online search for 'mad hatter' returns only three HackRF One listings, so the badge is not in the online store. No Reddit, Bluesky, X or Hackaday coverage turned up."
last_modified_date: '2026-09-06'
---

The Mad Hatter Auto Revelator is a DEF CON 32 badge from a Utah group calling themselves The Mad Hatters. Its own manual is laid out as a mock antique title page ("Mad Hatter Auto Revelator, or Celestial Intelligencer, being a complete system in one badge") and the whole design is a running joke about seer stones, hats, e-meters and "celestial intelligence". A 3D-printed top hat sits over a 0.96" OLED; you are meant to press your eye to the hat, shut out the light, and read the glowing stones. The makers warn that the badge is "unapologetically heathen" and that its Truth, Revelation and Magic 8 Ball modes each hide an NSFW version behind a secret handshake and password.

Under the parody the hardware is straightforward. An ESP32-S2-SOLO-2 module drives 38 addressable LEDs (SK6812 mini parts on the main board and side-firing SK6812 parts on the upper and lower text boards) plus nine discrete LEDs, with 13 named light modes including a DC 32 mode. Four capacitive touch pads styled as "handshakes" replace buttons for menu navigation, and they double as the sensor for the Mad Hatter Meter, a tongue-in-cheek e-meter that interprets the readings as TEST, SET, RISE or FALL. A Display Handle mode etches your handle permanently into the "Akashic Record", so it is shown again on later boots. Power is a micro USB port or three AA cells behind a regulator, selected by a slide switch, and there are two keyed SAO v1.69bis headers with I2C available by bridging pads, plus broken-out UART and JTAG.

The badge and a companion SAO, the Madragrammaton (16 LEDs, a potentiometer for flash rate, powered from the badge or a CR2032), were sold through Hacker Warehouse at DC32, according to the maker's page and repository README. The community sheet listed it at $100 with 100 made. Brucifer published printable top hats and twist-lock adapters for swapping hats on both the badge and the SAO on Printables; the same STLs, with their Creative Commons licences, are in the repository's stl/ directory.

## Make your own

Everything is in the `the-mad-hatters/defcon2024badge` repository under an MIT license. The `hardware/` directory has KiCad schematics and PCB files for the main board and the upper and lower "text" boards, a spreadsheet BOM with supplier links (boards were fabbed at JLCPCB), and v3 zip archives for each board. The `firmware/` directory is a PlatformIO project (espressif32 platform, Arduino framework, FastLED and U8g2); build it in VS Code with PlatformIO, or grab the prebuilt `bootloader.bin`, `partitions.bin`, `firmware.bin` and `spiffs.bin` from the firmware.tar.gz archive on the v1.3.3 release and flash them with `esptool.py --chip esp32s2` at offsets 0x1000, 0x8000, 0x10000 and 0x290000 (or a web serial flasher). Hold FLASH while pressing RESET if the badge does not enumerate. Print `tophat_dc32_badge.stl` from `stl/` for the hat, and the two adapter STLs if you want swappable hats.
