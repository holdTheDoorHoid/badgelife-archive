---
title: DCZia's dumb DC32 badge (winner for most unique name lol)
id: dc32-dczia-s-dumb-dc32-badge-winner-for-most-unique-name-lol
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
series: DCZia
makers:
- name: DCZIA
  url: https://dczia.net
summary: The DCZia "Ziatron" is DCZia's 2024 DEF CON 32 badge, an homage to the Sony
  Trinitron TV with a 1.9" full-color LCD screen and mic-reactive LEDs.
functions: Light patterns, a sound-reactive "rave" mode (a knob sets microphone
  sensitivity), and raw image display from an SD card. An SSTV encode/decode mode
  was planned but not finished in time for the con.
look:
  colors: []
  shape: rectangle
  themes: []
  form_factor: pcb badge
tech:
  mcu: RP2040 (Raspberry Pi Pico W)
  leds: 
    count: 18
    type: RGB
    note: up to 18 full-color LEDs
  display: 1.9" full-color LCD
  connectivity:
  - wifi
  - audio
  inputs:
  - rotary encoder
  - microphone
  battery: 3x AAA
  sao_version: null
get_one:
  price: $130.00
  price_usd: 130.0
  quantity: ''
  availability: unknown
  distribution: []
  where: TBD
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/dczia/Defcon32-Badge/tree/main/Hardware
  firmware_url: https://github.com/dczia/Defcon32-Badge/tree/main/Software
  eda_tool: KiCad
  fab_url: null
  bom_url: https://github.com/dczia/Defcon32-Badge/blob/main/Hardware/DCZIA%20DC32%20BADGE%20BOM.xlsx
  notes: Repo includes KiCad schematics/PCB, a BOM spreadsheet, 3D-printed case
    STLs, and a BuildGuide.md covering assembly and firmware flashing.
links:
- kind: repo
  label: DCZia/Defcon32-Badge on GitHub
  url: https://github.com/dczia/Defcon32-Badge
- kind: website
  label: DCZia badge history
  url: https://dczia.net
images:
- file: assets/images/badges/dc32/dczia-s-dumb-dc32-badge-winner-for-most-unique-name-lol/93601d2403.jpg
  source: "https://dczia.net/"
  credit: "DCZia"
  caption: "The DCZia Ziatron, DCZia's DEF CON 32 badge"
contact:
  handles:
  - '@dczia505'
  raw:
  - on twitter/ dczia.bsky.social on bluesky
notes:
- Info on sales pending. Also, the price is approximate at this time.
- The community sheet's title uses a joking name ("winner for most unique name
  lol"); DCZia's own site and GitHub repo call this badge the "Ziatron."
status: released
sources:
- kind: sheet
  event: dc32
  row: 51
  updated: '2024-07-30'
- kind: url
  url: https://github.com/dczia/Defcon32-Badge
  title: dczia/Defcon32-Badge - GitHub
  accessed: '2026-09-06'
  note: Primary source for badge name (Ziatron), specs, BOM, KiCad hardware files,
    firmware, and BuildGuide.
- kind: url
  url: https://dczia.net
  title: DCZia
  accessed: '2026-09-06'
  note: Maker's own badge history page; confirms the Ziatron description and links
    to the GitHub repo; source of the badge photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Confirmed via the maker's own GitHub repo and website that this is the
    "DCZia Ziatron," a Raspberry Pi Pico W badge with an LCD, up to 18 LEDs, a mic,
    and a speaker, styled as a Sony Trinitron homage. Could not find any storefront,
    listing, or social post confirming price, quantity made, or public availability
    for DC32 (2024) specifically -- the sheet's ~$130 price is left as-is but
    unconfirmed. No GitHub release/firmware binary was found, though firmware
    source exists under Software/. DCZia appears to be a maker crew that
    distributes badges mainly within their own group rather than a public
    storefront, based on later-year (DC33/DC34) social posts about crew
    pickups/preorders.
last_modified_date: '2026-09-06'
---

DCZia's 2024 DEF CON 32 badge, the "Ziatron," is an homage to the Sony Trinitron
television: a 1.9" full-color LCD screen sits behind a dye-sublimated, dual-PCB
front panel, backed by up to 18 full-color LEDs. A single clickable rotary encoder
is the only physical control, paired with a micro mechanical microphone (TDK) and
a small 0.3" speaker. It runs on a Raspberry Pi Pico W (RP2040 with Wi-Fi) and is
powered by three AAA batteries.

The badge's stock firmware includes several LED light patterns, a sound-reactive
"rave" mode where the encoder sets microphone sensitivity, and the ability to
display raw formatted images from an SD card. The team had planned an SSTV
(slow-scan television) encode/decode feature to match the TV theme but ran out of
time before the con. Hardware (KiCad schematics and PCB, a BOM, and 3D-printed
case files) and firmware source are published on GitHub, along with a build guide
covering rotary-encoder and battery-pack assembly and firmware flashing via the
Pico's USB mass-storage bootloader.

No public storefront, price confirmation, or production-quantity figure for this
specific badge could be found; DCZia's later badges (2025 Zippy, 2026 MK9) were
sold via preorder and crew pickup at the con rather than open retail, and the same
may have been true here.
