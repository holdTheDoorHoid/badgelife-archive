---
title: SecKC DC26 Daughter board (GPS/screen/buttons/sensors)
id: dc26-seckc-dc26-daughter-board-gps-screen-buttons-sensors
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc26
year: 2018
makers:
- name: BadgePirates / SecKC
  url: https://badgepirates.com/
summary: An add-on expansion board for the BadgePirates/SecKC DEF CON 26 badge, split into three sections (GPS, screen + buttons, and sensors) that plug into the main badge.
functions: Extends the SecKC DC26 main badge with GPS positioning, a small screen with buttons for input/navigation, and onboard sensors.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - gps
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Gerbers
  firmware_url: null
  eda_tool: null
links:
- label: github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Gerbers
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Gerbers
  kind: repo
- label: github.com/BadgePiratesLLC/DefCon_SecKC_26 (repo root)
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26
  kind: repo
- label: SecKC DC26 Badge on Tindie (main badge this board plugs into)
  url: https://www.tindie.com/products/badgepirates/seckc-dc26-badge/
  kind: store
images:
- file: assets/images/badges/dc26/seckc-dc26-daughter-board-gps-screen-buttons-sensors/4401b0281e.jpg
  source: "https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Photos"
  credit: "BadgePirates/SecKC"
  caption: "GPS module section of the SecKC DC26 daughter board"
- file: assets/images/badges/dc26/seckc-dc26-daughter-board-gps-screen-buttons-sensors/ef887b2113.jpg
  source: "https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Photos"
  credit: "BadgePirates/SecKC"
  caption: "Screen and buttons section of the SecKC DC26 daughter board"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: listed
sources:
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Gerbers
  title: SecKC DC26 Daughter board (GPS/screen/buttons/sensors)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc26''.'
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26
  title: 'GitHub - BadgePiratesLLC/DefCon_SecKC_26: SECKC DC26 Defcon Badge'
  accessed: '2026-09-07'
  note: 'Repo root; confirms maker (Badge Pirates LLC), contains Photos folder with Daughter_GPS.JPG, Daughter_Screen&Buttons.JPG, Daughter_Sensors.JPG showing the three sections of the daughter board; gerber files dated 2018-06-27, consistent with DEF CON 26 (August 2018).'
- kind: url
  url: https://www.tindie.com/products/badgepirates/seckc-dc26-badge/
  title: SecKC DC26 Badge from BadgePirates on Tindie
  accessed: '2026-09-07'
  note: 'Listing for the main SecKC DC26 badge this daughter board attaches to via its SAO/header connector: ESP32-WROOM-32, 42 charlieplexed LEDs, "BadgeLife Shitty Add-On Connector" for daughter boards, 2x AAA power. Listing is retired/no longer for sale; no separate listing found for the daughter board itself.'
- kind: url
  url: https://raw.githubusercontent.com/BadgePiratesLLC/DefCon_SecKC_26/master/Gerbers/Project-Moe-BOM--Final.csv
  title: Project-Moe-BOM--Final.csv
  accessed: '2026-09-07'
  note: 'Bill of materials in the same Gerbers folder as the daughter board files; it is for the main badge (ESP-WROOM-32, tact switches, charlieplexed LEDs, DC26 Shitty Addon Connector), not a separate BOM for the daughter board itself. No BOM/schematic specific to the daughter board (GPS module, screen, or sensor part numbers) was found.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    This is an accessory daughter board for the BadgePirates/SecKC DEF CON 26 badge (2018), not
    a standalone badge. The repo's Photos folder confirms it has three physical sections
    matching the title -- a GPS module, a screen-plus-buttons module, and a sensors module --
    but no README, schematic, or BOM specific to the daughter board was found, so the exact
    GPS chip, screen part/size, sensor types, and button count could not be confirmed. The
    Gerbers folder's BOM (Project-Moe-BOM--Final.csv) documents the main badge only. No price,
    quantity, or distribution details were found for the daughter board; it does not appear to
    have had its own separate storefront listing (only the main badge was listed on Tindie, and
    that listing is retired). Left tech.mcu, tech.leds, tech.battery, tech.sao_version, and all
    get_one fields empty/unknown rather than guess from the main badge's specs, since they may
    differ on the daughter board itself.
last_modified_date: '2026-09-07'
---

This is an expansion "daughter board" that plugs into the main SecKC DC26 badge, a DEF CON 26 (2018) badge made by BadgePirates for the Kansas City hacker group SecKC. The main badge itself is built around an ESP32-WROOM-32 with 42 charlie-plexed LEDs and a "BadgeLife Shitty Add-On Connector" meant for exactly this kind of attachment; it was briefly sold on Tindie but that listing has since been retired.

Photos in the project's GitHub repository show the daughter board split into three distinct physical sections: a GPS module, a small screen paired with buttons, and a block of onboard sensors -- matching the board's working title. Gerber files for the daughter board are dated June 27, 2018, consistent with a DEF CON 26 timeline. Beyond the photos and gerbers, no README, schematic, or bill of materials specific to the daughter board was published, so its exact GPS chip, screen part, sensor types, and how many units (if any) were made or distributed remain undocumented.

## Make your own

Gerber files for the daughter board are published as `Daughter_gerber.zip` in the repository's `Gerbers` folder, alongside the main badge's BOM, drill charts, and firmware (`BadgeCode`, a PlatformIO/Arduino project). No separate schematic or component list for the daughter board itself was found, so building one from scratch would require reverse-engineering the gerbers.
