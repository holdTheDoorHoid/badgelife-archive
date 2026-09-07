---
title: Friend or Foe Badge
id: dc34-friend-or-foe-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: GameChangersAI
  url: https://github.com/lnxgod/friendorfoe
summary: A three-board ESP32-S3 handheld that passively listens for BLE/Wi-Fi evidence of drones, trackers, smart glasses, and surveillance gear, and can be converted from a worn badge into a fixed sensor node.
functions: Situational awareness of BLE/wlan devices that can affect wearer privacy. Can operate standalone, on android over usb-c, or at home/on networks over wifi. Passively detects Remote ID drones, drone Wi-Fi, smart glasses (Ray-Ban Meta, Snap Spectacles, etc.), Bluetooth trackers (AirTag, Tile, SmartTag), hidden cameras, Wi-Fi Pineapple/deauth tools, and Flock Safety/ALPR gear, surfacing the most relevant alerts on its own display.
look:
  colors: []
  shape: null
  themes:
  - privacy
  - security
  - radio
  - hardware tool
  form_factor: pcb badge
tech:
  mcu: ESP32-S3 (3x Seeed Studio XIAO ESP32-S3, one uplink + two scanner boards)
  leds: null
  display: 1.8" 128x160 color SPI module
  connectivity:
  - wifi
  - ble
  - usb
  battery: LiPo cell (JST-clone connector, polarity varies by batch)
  sao_version: null
get_one:
  price: "badge is free with a cash donation to our 501(c)(3) \namount $100"
  price_usd: 100.0
  quantity: 45 (DEF CON 34 run)
  availability: free
  availability_note: 'Checked 2026-09-06: no separate storefront; distributed at the Packet Hacking Village table for a donation.'
  distribution:
  - free_drop
  - village
  where: Packet Hacking Village at DEF CON 34, given for a cash donation to GameChangersAI's 501(c)(3)
make_your_own:
  open_source: true
  hardware_url: https://github.com/lnxgod/friendorfoe/tree/main/hardware/badge
  firmware_url: https://github.com/lnxgod/friendorfoe
  eda_tool: KiCad
  notes: Gerbers (single-board and a 5-badge/2-core OSH Park panel), BOM CSV, and a battery-cage STL are published under hardware/badge/. Direct component cost for the 45-badge run was about $80/badge (excludes labor and tools).
links:
- label: github.com/lnxgod/friendorfoe
  url: https://github.com/lnxgod/friendorfoe
  kind: repo
images: []
contact:
  discord: OhYou_
  emails:
  - info@userexport.zip
  raw:
  - '@ me in #linecon or something'
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 60
  updated: 8/5/2026 13:31:14
  listing: Update to Existing
- kind: url
  url: https://github.com/lnxgod/friendorfoe
  title: 'lnxgod/friendorfoe: Friend or Foe Badge'
  accessed: '2026-09-06'
  note: Primary source for what the badge is, its hardware (3x XIAO ESP32-S3, display, antennas, battery), functions, DEF CON 34 run size (45 badges), build cost (~$80/badge), and published hardware/firmware files.
- kind: url
  url: https://raw.githubusercontent.com/lnxgod/friendorfoe/main/hardware/badge/README.md
  title: Friend or Foe Badge Hardware
  accessed: '2026-09-06'
  note: Confirms fabrication files (Gerbers, panel, STL, BOM), KiCad board dimensions, and build/assembly notes (battery polarity, button footprint fit).
- kind: sheet
  event: dc34
  row: 47
  updated: 7/22/2026 10:52:12
  listing: New
- kind: url
  url: https://gamechangersai.org/
  title: GameChangers AI at DEF CON
  accessed: '2026-09-06'
  note: Maker's team site confirming the Friend or Foe badge as their DEF CON 34 hardware project (alongside a browser game and a badge-workbench tool, both software, not physical items).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: All hardware/software facts come from the maker's own GitHub repo (README and hardware/badge/README.md), which is a strong primary source, but no independent press, Hackaday, or storefront coverage was found to corroborate or add to it. No photos of the assembled badge were found anywhere in the repo (only unrelated aircraft-icon assets under android/app/src/main/assets/aircraft/), so images could not be filled in. No LED info given, so tech.leds is left null; the badge's awareness output appears to be entirely on its color display. look.colors/shape are unset since no photo or explicit description of the PCB art/colors was found. The maker's own sheet listed the same maker (GameChangersAI) with a second entry titled "TBD" (dc34-tbd-2); that is a different row and was not touched. Merged with duplicate entry 'Friend or Foe Badge' (dc34-tbd-2).
last_modified_date: '2026-09-06'
redirect_from:
- /badges/dc34/tbd-2/
---

Friend or Foe is a three-board ESP32-S3 handheld built by GameChangersAI for the DEF CON 34 Packet Hacking Village. One badge is really three Seeed Studio XIAO ESP32-S3 boards: an uplink board that drives a small 1.8" color display and handles USB-C control, plus two scanner boards (one BLE-primary, one Wi-Fi-primary) that run the same firmware image in different roles. Each radio has its own external 2.4 GHz patch antenna sitting over a copper ground-plane triangle worked into the badge's PCB art.

Worn passively, the badge listens for RF evidence already being broadcast around it and tries to label it conservatively: Remote ID and Wi-Fi signatures from consumer drones, BLE service UUIDs and manufacturer data from trackers (AirTag, Tile, SmartTag), smart glasses (Ray-Ban Meta, Snap Spectacles, Xreal, Vuzix), hidden cameras, Wi-Fi Pineapple-style rogue APs, and Flock Safety/ALPR gear. Plugging into an Android phone over USB-C unlocks a richer live view, display filters, and theming, but the badge works standalone with no cloud account or SIM required. The same hardware and firmware can be repurposed as a stationary sensor node given fixed power, a backend URL, and a mounted position instead of being worn.

GameChangersAI built 45 of these badges for the DEF CON 34 run at roughly $80 in components each, and gave them out at the Packet Hacking Village table for a cash donation to their 501(c)(3). The project is fully open: KiCad-derived Gerbers for both a single badge and an OSH Park panel of five, the original BOM, a 3D-printable battery cage, and the full Android/ESP32 firmware source are all published in the `lnxgod/friendorfoe` GitHub repo, along with build notes flagging battery-polarity and button-footprint quirks from the actual build run.

## Make your own

Gerbers and a BOM for the badge PCB are under [`hardware/badge/`](https://github.com/lnxgod/friendorfoe/tree/main/hardware/badge) in the repo: a single-board fabrication ZIP, a cost-optimized 5-badge/2-core OSH Park panel ZIP, and an STL for the rear battery cage. The board is a two-layer, 1.6 mm design at 160.05 x 138.6141 mm (single board) built from three Seeed Studio XIAO ESP32-S3 modules, Abracon APAGM2525-S2450 patch antennas, a 1.8" 128x160 SPI color display, and a small lithium-ion cell. Firmware for both the uplink and scanner roles builds from the repository root; the [hardware README](https://github.com/lnxgod/friendorfoe/blob/main/hardware/badge/README.md) documents assembly gotchas (battery connector polarity, button footprint fit, display carrier variance) worth reading before ordering boards.

## Notes merged from the duplicate entry "Friend or Foe Badge"

This entry is the same Friend or Foe badge documented at [dc34-friend-or-foe-badge](./friend-or-foe-badge.md); this sheet row is GameChangersAI's earlier, sparser submission for the identical item and is kept as a duplicate record rather than merged, per this archive's sourcing rules.

Friend or Foe is a three-board ESP32-S3 handheld built by GameChangersAI for the DEF CON 34 Packet Hacking Village. One badge is really three Seeed Studio XIAO ESP32-S3 boards: an uplink board that drives a small 1.8" color display and handles USB-C control, plus two scanner boards (one BLE-primary, one Wi-Fi-primary) running the same firmware image in different roles. Worn passively, it listens for RF evidence already being broadcast around it and labels it conservatively: Remote ID and Wi-Fi signatures from consumer drones, BLE data from trackers (AirTag, Tile, SmartTag), smart glasses, hidden cameras, Wi-Fi Pineapple-style rogue APs, and Flock Safety/ALPR gear. It works standalone with no cloud account, or over USB-C to an Android phone for a richer live view.

GameChangersAI built 45 of these for the DEF CON 34 run at roughly $80 in components each, and gave them out at the Packet Hacking Village table for a cash donation to their 501(c)(3). The project is fully open: KiCad-derived Gerbers, a BOM, a 3D-printable battery cage, and the full Android/ESP32 firmware are published in the `lnxgod/friendorfoe` GitHub repo.
