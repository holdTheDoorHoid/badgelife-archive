---
title: Cult of Cthulhu
id: dc34-cult-of-cthulhu
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Elliot Pfarr
  url: https://github.com/sqearl
summary: A BLE-based RPG badge shaped like a Cthulhu head, worn at DEF CON 34, where wearers connect to other "acolyte" badges to grow their cult, find glyphs, and progress a 13-chapter main quest plus an unlockable side quest.
functions: 'Badge-to-badge BLE connections to level up and unlock story chapters; a 13-chapter main quest and a 6-chapter unlockable side quest; unlockable modes including a battle arena ("R''lyeh Arena"), a second RNG battle mode, screen/LED "Bling" pattern unlocks, an "Exploit" beacon mode, and a "Séance" mode where four badges together trigger a mass beacon; tracks connected "Cult Members"; adjustable LED brightness and a screen-flip option for neck wear.'
look:
  colors:
  - black
  - gold
  - multicolor
  shape: cthulhu head
  themes:
  - horror
  - fantasy
  - wearable
tech:
  mcu: ESP32
  leds:
    count: 10
    type: null
    note: 10 addressable LEDs used for progress/level indication and unlockable patterns; exact LED part not stated by the maker.
  display: OLED
  connectivity:
  - ble
  battery: LiPo, rechargeable, capacity not stated
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/sqearl/cult_of_cthulhu_badge/blob/main/cthulhu_badge_schematic.pdf
  firmware_url: https://github.com/sqearl/cult_of_cthulhu_badge/tree/main/firmware
  eda_tool: null
  gerbers_url: null
  bom_url: https://github.com/sqearl/cult_of_cthulhu_badge/blob/main/cthulhu_badge_BOM.csv
  license: MIT
  fab_url: null
  notes: Schematic is a PDF, not source EDA files; no Gerbers published. Firmware is flashed in-browser via esptool-js (Web Serial, Chrome/Edge only).
links:
- label: www.instagram.com/reel/DZVt7tYx8yt
  url: https://www.instagram.com/reel/DZVt7tYx8yt/
  kind: website
- label: GitHub - sqearl/cult_of_cthulhu_badge
  url: https://github.com/sqearl/cult_of_cthulhu_badge
  kind: repo
- label: 'TikTok: @pfarrsidecreations badge reel'
  url: https://www.tiktok.com/@pfarrsidecreations/video/7651278106916932877
  kind: social
images:
- file: assets/images/badges/dc34/cult-of-cthulhu/c6fe09e191.jpg
  source: "https://www.instagram.com/reel/DZVt7tYx8yt/"
  credit: "Elliot Pfarr"
  caption: "Reel thumbnail of the Cult of Cthulhu badge, lit up, showing its Cthulhu-head PCB outline, OLED display, and single button"
contact: {}
notes:
- BLE-based indie RPG badge where wearers connect to other 'acolyte' badges to grow a cult and solve challenges, with SAO prizes for early quest completers, debuted as the maker's first indie DEF CON 34 badge. Found by the event-year sweep, task dc34-indie.
- 'The maker''s GitHub handle "sqearl" matches "sqearlsalazar," who has several earlier DC26/DC27/DC30 SAO entries in this archive under that handle; Elliot Pfarr appears to be the same person''s real name, confirmed via the linked Instagram/TikTok accounts (elliotpfarr / pfarrsidecreations).'
status: listed
sources:
- kind: url
  url: https://www.instagram.com/reel/DZVt7tYx8yt/
  title: Cult of Cthulhu
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc34-indie); event read as ''dc34''.'
- kind: url
  url: https://github.com/sqearl/cult_of_cthulhu_badge
  title: 'GitHub: sqearl/cult_of_cthulhu_badge'
  accessed: '2026-09-08'
  note: Maker's own repo; confirmed hardware (ESP32, USB-C, LiPo, 10 addressable LEDs, screen, one button), gameplay mechanics, MIT license, and open hardware/firmware files.
- kind: url
  url: https://www.tiktok.com/@pfarrsidecreations/video/7651278106916932877
  title: Cult of Cthulhu badge DEF CON 34 BLE RPG scavenger hunt
  accessed: '2026-09-08'
  note: Corroborates the maker's own description of the badge and links the pfarrsidecreations/elliotpfarr identity to the project.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own GitHub repo and social posts, so core facts (chip, power, gameplay, open-source status) are solid. Not found anywhere: price, quantity made, and availability/where it was distributed (likely free/worn by the maker and collaborators rather than sold, but no source states this). Exact LED part number and OLED size are not given by the maker. The badge does not appear to carry an SAO header itself; the entry''s original notes mention "SAO prizes for early quest completers" but no source describes a separate prize SAO in detail, so that is not otherwise documented here. DEF CON forum badgelife-list thread (https://forum.defcon.org/node/255780) was found via search but could not be fetched to check for a listing.'
last_modified_date: '2026-09-08'
---

Cult of Cthulhu is a BLE-based RPG badge that Elliot Pfarr (GitHub/Instagram/TikTok handle sqearl / sqearlsalazar / elliotpfarr / pfarrsidecreations) built for DEF CON 34, described as his first indie badge after ten years of following badgelife. The badge is cut in the shape of a Cthulhu head, built around an ESP32 with a small onboard screen, ten addressable LEDs, a single button, and a rechargeable Li-Po battery charged over USB-C.

Wearers ("Acolytes") use Bluetooth Low Energy to connect to other badges in the wild — including "Glyph" badges seeded around villages and vendor booths and "Elder God" badges held by DEF CON staff — to level up and progress a 13-chapter main quest, "The Ritual." A six-chapter unlockable side quest ("The Corrupt Ritual") and several bonus modes follow: a "R'lyeh Arena" battle mode, a second RNG battle mode with a Rick and Morty-flavored story, a "Bling" mode with unlockable screen/LED patterns, a "Séance" mode that needs four badges together to trigger a mass BLE beacon, and joke "Exploit"/"Rick Roll" beacon modes. The badge tracks connected "Cult Members" and offers adjustable LED brightness and a screen-flip option for wearing it around the neck.

Hardware (schematic PDF and BOM) and firmware are published on GitHub under the MIT license; firmware updates are applied in-browser via esptool-js over Web Serial (Chrome/Edge only), and a full reflash at address 0x0 resets saved progress. No pricing, production quantity, or distribution details were found in any source — the badge does not appear to have been sold, and it is unclear whether it was given away or worn only by the maker's own circle.

## Make your own

- Hardware: schematic PDF and bill of materials in the [GitHub repo](https://github.com/sqearl/cult_of_cthulhu_badge) (no Gerbers published).
- Firmware: build files in the repo's `firmware` directory.
- Flashing: use [esptool-js](https://espressif.github.io/esptool-js/) over Web Serial (Chrome or Edge) — flash an `app_xxx.bin` at address `0x10000` to update while keeping saved progress, or `full_cult_v3.bin` at address `0x0` for a full reset.
