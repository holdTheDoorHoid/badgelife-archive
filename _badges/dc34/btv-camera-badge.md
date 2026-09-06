---
title: BTV Camera Badge
id: dc34-btv-camera-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Blue Team Village
  url: https://blueteamvillage.org
summary: A PCB badge shaped like a vintage SLR camera whose "lens" is a round display that lights up when it detects deauth packets or nearby Flipper Zeros.
functions: Detects and displays Wi-Fi deauth packets and nearby Flipper Zero devices on its lens-shaped display; runs on an ESP32 so further custom firmware is possible; maker hints at "other goodies hidden inside"
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
    note: 3x addressable LEDs, 5x discrete blue LEDs, and 1x bright white discrete LED per the kit BOM
  display: round display (camera lens)
  connectivity:
  - wifi
  inputs:
  - 3-pin switch
  battery: LiPo 3.7V 1200mAh
  sao_version: v2
  sao_ports: 1
get_one:
  price: $120 assembled; $60 kit (intermediate/advanced soldering)
  price_usd: 120.0
  quantity: ''
  availability: sold_out
  availability_note: Eventbrite listing showed "Event ended" / "Sales ended" as of 2026-09-06; badge was pickup-only during DEF CON 34 (Aug 7-9, 2026)
  distribution:
  - purchase
  - kit
  where: Sold via Eventbrite for in-person pickup at the Blue Team Village infobooth, Las Vegas Convention Center West Hall, 2nd Floor, W213-215, during DEF CON 34
make_your_own:
  open_source: yes
  hardware_url: https://github.com/blueteamvillage/btv_dc32_badge
  firmware_url: https://github.com/blueteamvillage/btv_dc32_badge
  eda_tool: KiCad
  license: MIT
  notes: The repo (btv_dc32_badge) and its documentation site describe this as the DEF CON 32 (2024) camera badge design; the DC34 Eventbrite listing for 2026 points to the same site for assembly instructions, so the DC34 sale appears to reuse or lightly update the DC32 hardware/firmware rather than being an all-new design.
links:
- label: www.eventbrite.com/e/1995859982936
  url: https://www.eventbrite.com/e/1995859982936
  kind: store
- label: discord.gg/blueteamvillage
  url: https://discord.gg/blueteamvillage
  kind: social
- label: camerabadge.blueteamvillage.org
  url: https://camerabadge.blueteamvillage.org
  kind: doc
- label: github.com/blueteamvillage/btv_dc32_badge
  url: https://github.com/blueteamvillage/btv_dc32_badge
  kind: repo
images:
- file: assets/images/badges/dc34/btv-camera-badge/fb0a135ffa.jpg
  source: "https://camerabadge.blueteamvillage.org"
  credit: "Blue Team Village / alt_bier"
  caption: "The BTV Camera Badge, front view"
contact:
  emails:
  - info@blueteamvillage.org
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 51
  updated: 7/29/2026 0:24:05
  listing: New
- kind: url
  url: https://www.eventbrite.com/e/1995859982936
  title: "The BTV Camera Badge - DEF CON 34 BTV Fundraiser - VEGAS PICKUP ONLY"
  accessed: '2026-09-06'
  note: Full description, BOM, pricing ($120 assembled / $60 kit), pickup location and dates, designer credit (alt_bier), and related items (BTV SAO, Sh1tty add-on)
- kind: url
  url: https://camerabadge.blueteamvillage.org
  title: BTV Camera Badge Documentation
  accessed: '2026-09-06'
  note: Confirms this design was originally made for DEFCON 32 (2024); links to GitHub repo and hero photo
- kind: url
  url: https://github.com/blueteamvillage/btv_dc32_badge
  title: blueteamvillage/btv_dc32_badge
  accessed: '2026-09-06'
  note: Confirms open hardware (KiCad, MIT license) with Art/Code/Docs/EDA directories
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Maker''s own Eventbrite listing and documentation site confirm the core facts. The DC34 listing directs buyers to camerabadge.blueteamvillage.org and the btv_dc32_badge GitHub repo, both of which describe the badge as designed for DEFCON 32 (2024) -- this appears to be the same camera badge design resold/rebuilt for DC34 in 2026 (see _badges/dc32/camera-badge.md, also currently a stub, for the earlier sale). Display type/size beyond "screen" is not specified anywhere found. Quantity made was not stated. Two related add-ons were also sold alongside this badge and are reported separately below (BTV SAO, Sh1tty add-on SAO) rather than filed here.'
last_modified_date: '2026-09-06'
---

The BTV Camera Badge is a PCB badge cut into the shape of a vintage SLR camera, made by Blue Team Village (BTV) for DEF CON 34 in August 2026 and designed by BTV badgelife team member alt_bier (with De-CERT and emilia). It doesn't take photos -- instead, the round display set into the "lens" lights up to show when Wi-Fi deauthentication packets are being sent nearby or when a Flipper Zero is detected in range. It runs on an ESP32, which the maker notes leaves room for custom firmware, and the listing hints that "other goodies" are hidden inside the badge as well.

BTV sold it two ways at DEF CON 34: fully assembled with a lanyard for $120, or as a $60 solder-it-yourself kit aimed at intermediate-to-advanced builders, with a BOM of top and bottom PCBs, a screen, an ESP32 dev board, three addressable LEDs, five discrete blue LEDs, a bright white LED, a 2x3 SAO connector, and a 3.7V 1200mAh LiPo battery. Proceeds benefited BTV as a 501(c)(3). Pickup was in person only, at the BTV infobooth in the Las Vegas Convention Center West Hall during village hours.

## Make your own

Hardware (KiCad, under `EDA/`) and firmware (under `Code/`) are published under the MIT license in the `blueteamvillage/btv_dc32_badge` GitHub repo, with an accompanying documentation and assembly-instructions site at camerabadge.blueteamvillage.org. Both describe the design as originating with the DEF CON 32 (2024) camera badge, which the DC34 sale appears to reuse.
