---
title: CHV Main Badge
id: dc32-chv-main-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Car Hacking Village
  url: https://www.carhackingvillage.com
summary: The Car Hacking Village's DEF CON 32 badge, a 150mm-wide RP2040 board with four CAN networks, a dry CAN connector, four SAO headers using CHV's CAN-based SAO standard, and CTF challenges.
functions: |-
  150mm Wide
  CTF Challenges
  RP2040
  4 CAN Networks
  Dry CAN Connector
  4 SAO Connectors
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - ctf
  - village badge
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $100.00
  price_usd: 100.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  - village
  where: Available at the Car Hacking Village (CHV) at DEF CON 32
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.carhackingvillage.com
  url: https://www.carhackingvillage.com
  kind: website
  archived: https://web.archive.org/web/20260810193641/https://www.carhackingvillage.com/
- label: linted/CHV_SAO_Specification (GitHub)
  url: https://github.com/linted/CHV_SAO_Specification
  kind: repo
images: []
contact: {}
notes: []
status: listed
sources:
- kind: sheet
  event: dc32
  row: 35
  updated: '2024-07-17'
- kind: url
  url: https://www.carhackingvillage.com
  title: Car Hacking Village
  accessed: '2026-09-06'
  note: Confirms CHV maintains a CAN-based SAO standard ("we've updated the SAO standard to include CAN TX/RX"); no DC32-specific badge page or price/quantity was found on the current site.
  archived: https://web.archive.org/web/20260810193641/https://www.carhackingvillage.com/
- kind: url
  url: https://github.com/linted/CHV_SAO_Specification
  title: linted/CHV_SAO_Specification
  accessed: '2026-09-06'
  note: 'CHV''s CAN-based SAO spec (labeled DC31 in the repo): SAO headers carry 3.3V/GND plus CAN TX/RX instead of I2C, CAN 2.0B, based on the SAO bis v1.69 design guide. Confirms the CAN-SAO concept referenced in the DC32 sheet entry but is documented for DC31, not DC32 specifically.'
- kind: url
  url: https://github.com/linted?tab=repositories
  title: linted (Mike Merrill) GitHub repositories
  accessed: '2026-09-07'
  note: Repository list shows CHV_SAO_Specification, CHV_badge_board (KiCad files named CHV_DC31), CHV_Badge_Firmware ("firmware for emulating a car on a single PCB", no year stated) and a fork of KevinOConnor/can2040 (software CAN for RP2040). No repo specifically for a DC32/2024 badge was found.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Could not find a dedicated page, storefront listing, GitHub repo, or photo for this specific DC32 (2024) badge. Car Hacking Village''s own site currently has no badge page for 2024 and its swag store does not list a badge. CHV''s known GitHub maintainer (linted / Mike Merrill) publishes CHV badge hardware and the CAN-based SAO specification, but the only repos found (CHV_badge_board, CHV_SAO_Specification) are explicitly labeled DC31 (three SAO connectors), one generation earlier than the four-connector, four-CAN-network board described on the DC32 sheet, so I did not attach them as this badge''s own design files. Set type to "badge" (from "sao") since the sheet''s own functions field describes it as a 150mm board with SAO connectors and a CAN connector for tapping vehicle buses, i.e. a host badge rather than a plug-in SAO. tech.mcu (RP2040) is taken from the sheet''s own functions field; the maintainer also keeps a fork of can2040 (software CAN for RP2040), but no source ties
    that fork to this badge. No image of the actual DC32 badge was found on the sites checked (carhackingvillage.com, swag.carhackingvillage.com, GitHub). Price ($100) and event association were already correct in the imported sheet data. Web search access was unavailable during this research pass, which limited coverage of press, forum, and social posts. Fact-check 2026-09-07: all cited sources re-opened; corrected the body''s claim that CAN replaces the I2C pins (the CHV spec puts CAN TX/RX on the SAO GPIO1/GPIO2 pins and leaves I2C unconnected), removed the unsupported "tapping real vehicle buses" interpretation, and dropped the "radio" theme. Core specs (150mm, RP2040, 4 CAN networks, dry CAN connector, 4 SAO connectors, $100, CTF) rest on the community sheet only.'
last_modified_date: '2026-09-07'
---

The CHV Main Badge is the Car Hacking Village's badge for DEF CON 32 (2024). According to the community badge sheet it is a 150mm-wide board built around an RP2040 microcontroller with four CAN networks, a "dry" CAN connector, four SAO connectors, and CTF challenges, and it was sold at the village for $100. Its SAO headers follow CHV's own CAN-based SAO standard, which exposes CAN TX and RX on the pins that the standard SAO v1.69bis layout reserves for GPIO1 and GPIO2 and leaves the I2C pins unconnected, so add-ons talk CAN directly to the badge.

CHV's badge hardware and the CAN-SAO specification are published on GitHub by maintainer "linted" (Mike Merrill). The spec and board files found there are explicitly labeled for the prior year's badge (DC31), which had three SAO connectors rather than this badge's four. No repository, storefront listing, or photo specific to the DC32 board was located, so this entry describes it using only the sheet's own listed specs plus the general CHV CAN-SAO context; the design files, exact quantity made, and current availability remain unconfirmed.
