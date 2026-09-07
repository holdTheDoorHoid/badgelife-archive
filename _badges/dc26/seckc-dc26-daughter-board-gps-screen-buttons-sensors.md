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
  note: 'Repo root; confirms maker (Badge Pirates LLC), contains Photos folder with Daughter_GPS.JPG, Daughter_Screen&Buttons.JPG, Daughter_Sensors.JPG showing the three sections of the daughter board. Commit history shows the Gerbers folder was first added 2018-06-07 and Daughter_gerber.zip specifically was added/updated 2019-01-19 -- no evidence for a 2018-06-27 date (that earlier note was unsupported and has been corrected).'
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
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass (2026-09-07): re-fetched all three cited sources plus the GitHub API listing
    for Photos/ and Gerbers/, the BOM CSV, and the Daughter_gerber.zip contents. Confirmed: repo
    is BadgePiratesLLC/DefCon_SecKC_26 ("SECKC DC26 Defcon Badge"); Photos/ contains
    Daughter_GPS.JPG, Daughter_Screen&Buttons.JPG, Daughter_Sensors.JPG; Gerbers/ contains
    Daughter_gerber.zip alongside the main badge's BOM/drill chart/schematic; the BOM CSV
    documents only the main badge (ESP-WROOM-32, tact switches, LEDs, DC26 Shitty Addon
    Connector); badgepirates.com confirms the maker name/branding; the Tindie listing confirms
    the main badge's ESP32-WROOM-32 MCU, 42 charlie-plexed LEDs, "BadgeLife Shitty Add-On
    Connector," 2x AAA power, retired/no-longer-for-sale status, and that it does not itself
    describe the daughter board's contents. Viewed both saved images directly: one clearly shows
    a GPS module section (silkscreen "Shitty Add-On", labeled headers) with a u-blox NEO-6M GPS
    breakout and a ceramic patch antenna; the other shows a screen-and-buttons section with a
    small LCD and multiple tact switches -- both match their captions and source page. One
    unsupported factual claim was found and corrected: the body previously stated the daughter
    board's gerbers were "dated June 27, 2018" -- GitHub commit history instead shows the
    Gerbers folder was first committed 2018-06-07 and Daughter_gerber.zip specifically was
    added/updated 2019-01-19, so that sentence and the matching source note have been removed/
    corrected. Also corrected an imprecise "Make your own" sentence that implied the BadgeCode
    firmware lives in the Gerbers folder; it is actually a separate top-level folder in the same
    repo. This remains an accessory daughter board for the BadgePirates/SecKC DEF CON 26 badge
    (2018), not a standalone badge; no README, schematic, or BOM specific to the daughter board
    itself was found, so tech.mcu, tech.leds, tech.display, tech.battery, tech.sao_version, and
    all get_one fields are correctly left empty/unknown rather than guessed from the main badge's
    specs or from what is merely visible in the photos.
last_modified_date: '2026-09-07'
---

This is an expansion "daughter board" that plugs into the main SecKC DC26 badge, a DEF CON 26 (2018) badge made by BadgePirates for the Kansas City hacker group SecKC. The main badge itself is built around an ESP32-WROOM-32 with 42 charlie-plexed LEDs and a "BadgeLife Shitty Add-On Connector" meant for exactly this kind of attachment; it was briefly sold on Tindie but that listing has since been retired.

Photos in the project's GitHub repository show the daughter board split into three distinct physical sections: a GPS module, a small screen paired with buttons, and a block of onboard sensors -- matching the board's working title. Beyond the photos and gerbers, no README, schematic, or bill of materials specific to the daughter board was published, so its exact GPS chip, screen part, sensor types, and how many units (if any) were made or distributed remain undocumented.

## Make your own

Gerber files for the daughter board are published as `Daughter_gerber.zip` in the repository's `Gerbers` folder, alongside the main badge's BOM and drill charts. The main badge's firmware (`BadgeCode`, a PlatformIO/Arduino project) lives elsewhere in the same repository, not in the Gerbers folder itself. No separate schematic or component list for the daughter board itself was found, so building one from scratch would require reverse-engineering the gerbers.
