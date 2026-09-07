---
title: 'Biogotchi (BioHacking Village Tamagotchi Badge)'
id: dc27-biohacking-village-tamagotchi-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Biohacking Village
  url: https://www.villageb.io/
summary: A DIY electronic pet badge for the DEF CON 27 (2019) Biohacking Village, styled after the Bandai Tamagotchi but themed around raising microscopic organisms instead of fictional creatures.
functions: Simulates caring for a microscopic organism (feeding, cleanliness, aging, "eggs"/achievements) on an onboard touchscreen, tracking stats like age, last meal, size, and poop count in firmware.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - learn to solder
  - hardware tool
tech:
  mcu: ESP32 WROOM
  leds: null
  display: 1.8" TFT (ILI9163, resistive touch)
  connectivity:
  - wifi
  - bluetooth
  - usb
  battery: LiPo, USB (microUSB) charging
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed at the Biohacking Village at DEF CON 27 (2019); exact distribution method not stated in available sources.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/biohacking-village/tamagotchi
  eda_tool: null
links:
- label: github.com/biohacking-village/tamagotchi
  url: https://github.com/biohacking-village/tamagotchi
  kind: repo
- label: Biohacking Village
  url: https://www.villageb.io/
  kind: website
images: []
contact: {}
notes:
- Name suggests a tamagotchi-style electronic badge/toy; year needs verification.
- 'Repo confirms this is the "Biogotchi", the Biohacking Village badge for DEF CON 27 (2019); event corrected from "other" to dc27.'
status: released
sources:
- kind: url
  url: https://github.com/biohacking-village/tamagotchi
  title: BioHacking Village Tamagotchi Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON, BioHacking Village - year not confirmed (API rate-limited before repo inspection)''.'
- kind: url
  url: https://raw.githubusercontent.com/biohacking-village/tamagotchi/master/README.md
  title: 'Biogotchi! README'
  accessed: '2026-09-07'
  note: 'Confirms name "Biogotchi", event "Biohacking Village 2019", ESP32 WROOM MCU, 1.8" TFT ILI9163 touch display, LiPo/USB charging, reprogrammable WiFi/BT dev board built on the Adafruit ESP32 Feather design.'
- kind: url
  url: https://raw.githubusercontent.com/biohacking-village/tamagotchi/master/biogotchi/README.md
  title: 'Biogotchi firmware README (Reflashing / Dev Notes)'
  accessed: '2026-09-07'
  note: 'Describes gameplay states (boot, live, menu, screen-saver, sleep), stats struct (age, last_meal, size, poops), biogotchi struct (name, biotype, hosts, points, eggs, luck), and SPIFFS-based save/status system.'
- kind: url
  url: https://raw.githubusercontent.com/biohacking-village/tamagotchi/master/prototype/README.md
  title: Biogotchi prototype hardware README
  accessed: '2026-09-07'
  note: 'Prototype built on Adafruit ESP32 Feather + 1.8" resistive-touch TFT breakout; lists exact display-to-ESP32 pin wiring and Arduino/TFT_eSPI toolchain setup; contains a wiring-diagram photo of the display breakout (not the badge itself, not saved).'
- kind: url
  url: https://www.villageb.io/
  title: Biohacking Village
  accessed: '2026-09-07'
  note: 'Confirms Biohacking Village as the maker/org (GitHub org blog link); no separate credited individual designer found.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No maker photos of the assembled badge were found (repo contains only a wiring-diagram photo of the display breakout, and a PDF datasheet, no photos of the finished device), so images remain empty. Price, quantity produced, and current availability are not stated anywhere in the repo or on the Biohacking Village site; get_one fields left empty/unknown. No individual designer credited beyond the Biohacking Village organization. LED info not mentioned in any source (display-only device), so tech.leds left null.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/biohacking-village-tamagotchi-badge/
---

The Biogotchi is the Biohacking Village's badge for DEF CON 27 (2019): a reprogrammable electronic pet built around an Espressif ESP32 WROOM module and a 1.8" resistive-touch TFT display (ILI9163 controller), wired and powered like an Adafruit ESP32 Feather with USB-rechargeable LiPo. Like a Tamagotchi, it runs firmware that tracks an onboard creature's age, feeding, cleanliness, and achievements, but themes it around real microscopic organisms rather than the original toy's fictional pets, fitting the village's biology-education focus.

Because the board doubles as a full ESP32 dev board (WiFi, Bluetooth, USB-to-UART), badge holders can reflash it with their own firmware after the con. The project's GitHub repo publishes the firmware source, gameplay state machine, and prototype hardware notes (including exact display wiring and Arduino/TFT_eSPI library setup), though no board schematics, PCB Gerbers, bill of materials, price, or production-quantity figures are published, so those fields are left blank rather than guessed.

## Make your own

1. Build or obtain an ESP32 Feather-compatible board (the prototype used an Adafruit HUZZAH32 ESP32 Feather).
2. Wire a 1.8" resistive-touch TFT display (ILI9163 controller) to the ESP32 per the pinout in the repo's `prototype/README.md`.
3. Install the Arduino IDE with ESP32 board support and the `TFT_eSPI` library (Bodmer), editing `User_Setup.h` to match the wiring.
4. Run the `SPIFFS_Test` sketch to initialize the filesystem, then flash the Biogotchi firmware from the `biogotchi` folder.
