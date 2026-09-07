---
title: Friend or Foe Badge
id: dc34-tbd-2
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
summary: A three-board ESP32-S3 handheld that passively listens for BLE/Wi-Fi
  evidence of drones, trackers, smart glasses, and surveillance gear, and can be
  converted from a worn badge into a fixed sensor node.
functions: Situational awareness of nearby BLE/Wi-Fi devices that can affect
  wearer privacy. Works standalone, over USB-C to an Android phone, or on a
  network at home. Passively detects Remote ID drones and drone Wi-Fi, smart
  glasses (Ray-Ban Meta, Snap Spectacles, etc.), Bluetooth trackers (AirTag,
  Tile, SmartTag), hidden cameras, Wi-Fi Pineapple/deauth tools, and Flock
  Safety/ALPR gear, surfacing the most relevant alerts on its own display.
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
  price: "badge is free with a cash donation to our 501(c)(3) \namount tbd ~$100"
  price_usd: 100.0
  quantity: '45 (DEF CON 34 run)'
  availability: free
  availability_note: 'Checked 2026-09-06: no separate storefront; distributed at
    the Packet Hacking Village table for a donation.'
  distribution:
  - free_drop
  - village
  where: Packet Hacking Village at DEF CON 34, given for a cash donation to
    GameChangersAI's 501(c)(3)
make_your_own:
  open_source: yes
  hardware_url: https://github.com/lnxgod/friendorfoe/tree/main/hardware/badge
  firmware_url: https://github.com/lnxgod/friendorfoe
  eda_tool: KiCad
  notes: Gerbers (single-board and a 5-badge/2-core OSH Park panel), BOM CSV, and
    a battery-cage STL are published under hardware/badge/. Direct component cost
    for the 45-badge run was about $80/badge (excludes labor and tools).
links:
- label: github.com/lnxgod/friendorfoe
  url: https://github.com/lnxgod/friendorfoe
  kind: repo
images: []
contact:
  discord: OhYou_
  emails:
  - info@userexport.zip
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 47
  updated: 7/22/2026 10:52:12
  listing: New
- kind: url
  url: https://github.com/lnxgod/friendorfoe
  title: 'lnxgod/friendorfoe: Friend or Foe Badge'
  accessed: '2026-09-06'
  note: Confirms this is the same Friend or Foe badge as dc34-friend-or-foe-badge
    (hardware, 45-badge DEF CON 34 run, ~$80/badge cost, open-source MIT files).
- kind: url
  url: https://gamechangersai.org/
  title: GameChangers AI at DEF CON
  accessed: '2026-09-06'
  note: Maker's team site confirming the Friend or Foe badge as their DEF CON 34
    hardware project (alongside a browser game and a badge-workbench tool, both
    software, not physical items).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'This sheet row is a duplicate of dc34-friend-or-foe-badge: same maker
    (GameChangersAI), same near-identical donation-price text ("amount tbd ~$100"
    here vs "amount $100" on the other row), and no other physical badge or SAO
    from this maker turned up anywhere (GitHub org, team site, or web search) for
    DEF CON 34. Row 47 here is marked "New" on the sheet and row 60 on the other
    entry is marked "Update to Existing", so this row is almost certainly the
    maker''s first, less-filled-out sheet submission for the same badge, later
    updated in the other row. Filled in identically to dc34-friend-or-foe-badge
    per the research guide''s duplicate-handling rule rather than left as a stub.
    No new photos found beyond what the sister entry already lacks (repo has no
    assembled-badge photos, only unrelated aircraft-icon assets).'
last_modified_date: '2026-09-06'
duplicate_of: dc34-friend-or-foe-badge
---

This entry is the same Friend or Foe badge documented at [dc34-friend-or-foe-badge](./friend-or-foe-badge.md); this sheet row is GameChangersAI's earlier, sparser submission for the identical item and is kept as a duplicate record rather than merged, per this archive's sourcing rules.

Friend or Foe is a three-board ESP32-S3 handheld built by GameChangersAI for the DEF CON 34 Packet Hacking Village. One badge is really three Seeed Studio XIAO ESP32-S3 boards: an uplink board that drives a small 1.8" color display and handles USB-C control, plus two scanner boards (one BLE-primary, one Wi-Fi-primary) running the same firmware image in different roles. Worn passively, it listens for RF evidence already being broadcast around it and labels it conservatively: Remote ID and Wi-Fi signatures from consumer drones, BLE data from trackers (AirTag, Tile, SmartTag), smart glasses, hidden cameras, Wi-Fi Pineapple-style rogue APs, and Flock Safety/ALPR gear. It works standalone with no cloud account, or over USB-C to an Android phone for a richer live view.

GameChangersAI built 45 of these for the DEF CON 34 run at roughly $80 in components each, and gave them out at the Packet Hacking Village table for a cash donation to their 501(c)(3). The project is fully open: KiCad-derived Gerbers, a BOM, a 3D-printable battery cage, and the full Android/ESP32 firmware are published in the `lnxgod/friendorfoe` GitHub repo.
