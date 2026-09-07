---
title: Camera Badge
id: dc32-camera-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Blue Team Village
  url: https://blueteamvillage.org
summary: A PCB badge shaped like a vintage SLR camera whose "lens" is a round display that lights up when it detects deauth packets or nearby Flipper Zeros.
functions: A wifi deauther along with other games; detects and displays nearby Wi-Fi deauth packets and Flipper Zero devices on its lens-shaped display; runs on an ESP32 so custom firmware is possible
look:
  colors:
  - black
  - blue
  - multicolor
  shape: camera
  themes:
  - security
  - radio
  - hardware tool
  - village badge
  - charity
tech:
  mcu: ESP32
  leds:
    count: 9
    type: mixed
    note: 3x addressable LEDs, 5x discrete blue LEDs, and 1x bright white discrete LED, per the later DC34 sale of the same design
  display: round display (camera lens)
  connectivity:
  - wifi
  battery: LiPo 3.7V 1200mAh
  sao_version: v2
  sao_ports: 1
get_one:
  price: $80 / $140
  price_usd: 80.0
  quantity: ''
  availability: unknown
  availability_note: Original DC32 Eventbrite sales page (btvcamerabadge.eventbrite.com) no longer resolves as of 2026-09-06; not found in the Wayback Machine either, so the sale's outcome could not be confirmed directly.
  distribution:
  - purchase
  where: Sold via an Eventbrite link posted by Blue Team Village, sales opening 29 July 2024 0900 Central Time; likely in-person pickup at the BTV village during DEF CON 32, Las Vegas, based on how the same design was later sold for DC34
make_your_own:
  open_source: true
  hardware_url: https://github.com/blueteamvillage/btv_dc32_badge
  firmware_url: https://github.com/blueteamvillage/btv_dc32_badge
  eda_tool: KiCad
  license: MIT
  notes: The repo is named btv_dc32_badge and its documentation site (camerabadge.blueteamvillage.org) states the design was made for DEF CON 32 in August 2024, confirming this entry as the badge's original release. The same design was resold/rebuilt for DEF CON 34 in 2026 (see dc34-btv-camera-badge).
links:
- label: t.co/WSAEdwdtY3
  url: https://t.co/WSAEdwdtY3
  kind: website
- label: camerabadge.blueteamvillage.org
  url: https://camerabadge.blueteamvillage.org
  kind: doc
- label: github.com/blueteamvillage/btv_dc32_badge
  url: https://github.com/blueteamvillage/btv_dc32_badge
  kind: repo
images:
- file: assets/images/badges/dc32/camera-badge/fb0a135ffa.jpg
  source: https://camerabadge.blueteamvillage.org
  credit: Blue Team Village
  caption: The BTV Camera Badge, front view
contact: {}
notes:
- The sales link goes live on 29 July 2024 at 0900 Central Time
status: released
sources:
- kind: sheet
  event: dc32
  row: 29
  updated: '2024-07-28'
- kind: url
  url: https://t.co/WSAEdwdtY3
  title: Redirects to btvcamerabadge.eventbrite.com (dead as of 2026)
  accessed: '2026-09-06'
  note: Confirmed the original t.co link's destination was the BTV Camera Badge Eventbrite sale; that Eventbrite page now 404s and has no Wayback snapshot.
- kind: url
  url: https://camerabadge.blueteamvillage.org
  title: BTV Camera Badge Documentation
  accessed: '2026-09-06'
  note: Confirms the badge was designed for DEF CON 32 (August 2024); provides the hero photo and links to the GitHub repo. Site states more detailed specs are "coming soon" and does not give price/quantity for the 2024 sale.
- kind: url
  url: https://github.com/blueteamvillage/btv_dc32_badge
  title: blueteamvillage/btv_dc32_badge
  accessed: '2026-09-06'
  note: Confirms open hardware (KiCad, MIT license) with art/code/docs/EDA directories; repo name itself ties the badge to DC32.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The maker's documentation site and GitHub repo (both discovered while researching the related dc34-btv-camera-badge entry, which reuses this same design) confirm this badge was designed for DEF CON 32. Chip, LED count/type, display size, battery and SAO details are taken from the later DC34 sale of the identical hardware (see dc34-btv-camera-badge sources) since no DC32-specific spec sheet was found; the original Eventbrite sales page is dead and has no Wayback snapshot, so DC32-specific quantity and final availability outcome (sold out vs cancelled) could not be confirmed. Price is as listed on the original community sheet ($80/$140, likely kit/assembled tiers, unconfirmed).
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc32/camera-badge.glb
  method: kicad
  source_file: eda/camera_badge/camera_badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 617648
---

The Camera Badge was made by Blue Team Village (BTV) for DEF CON 32 in Las Vegas in August 2024. It is a PCB cut into the shape of a vintage SLR camera; the round "lens" is actually a display that lights up to show nearby Wi-Fi deauthentication activity and other games, including a Flipper Zero detector. It runs on an ESP32, leaving room for custom firmware. BTV posted an Eventbrite link for sales that went live 29 July 2024 at 0900 Central Time, with the community sheet recording pricing around $80/$140 (likely kit vs. assembled tiers, though this was not directly confirmed).

BTV later reused this same hardware and firmware design for a DEF CON 34 sale in 2026 under the same repo name (`btv_dc32_badge`), where it was offered as a $120 assembled badge or $60 solder-it-yourself kit with an ESP32, a 2x3 SAO header, 9 LEDs (3 addressable, 5 discrete blue, 1 white), and a 3.7V 1200mAh LiPo battery — see the `dc34-btv-camera-badge` entry for that sale's full detail. Those specs are carried into this entry as the best available description of the DC32 hardware, since the original 2024 Eventbrite listing is no longer reachable and has no Wayback Machine snapshot.

## Make your own

Hardware (KiCad) and firmware are published under the MIT license at github.com/blueteamvillage/btv_dc32_badge, with an assembly-instructions site at camerabadge.blueteamvillage.org.
