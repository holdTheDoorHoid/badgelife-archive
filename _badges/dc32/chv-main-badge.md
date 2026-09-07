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
summary: The Car Hacking Village's DEF CON 32 badge, a 150mm RP2040 board built around four onboard CAN networks with a dry CAN connector for tapping real vehicle buses, and four SAO headers for CHV's CAN-based add-on ecosystem.
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
  - radio
  - hardware tool
  - ctf
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
- label: 'linted/CHV_SAO_Specification (GitHub)'
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
  note: 'Confirms CHV maintains a CAN-based SAO standard ("we''ve updated the SAO
    standard to include CAN TX/RX"); no DC32-specific badge page or price/quantity
    was found on the current site.'
- kind: url
  url: https://github.com/linted/CHV_SAO_Specification
  title: linted/CHV_SAO_Specification
  accessed: '2026-09-06'
  note: 'CHV''s CAN-based SAO spec (labeled DC31 in the repo): SAO headers carry
    3.3V/GND plus CAN TX/RX instead of I2C, CAN 2.0B, based on the SAO bis v1.69
    design guide. Confirms the CAN-SAO concept referenced in the DC32 sheet entry
    but is documented for DC31, not DC32 specifically.'
- kind: url
  url: https://github.com/linted
  title: linted (Mike Merrill) GitHub profile
  accessed: '2026-09-06'
  note: 'Maintainer of CHV''s badge repos (CHV_SAO_Specification, CHV_badge_board,
    CHV_Badge_Firmware, and a can2040 fork for software CAN on RP2040). No repo
    specifically for a DC32/2024 badge was found among their public repositories.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: >-
    Could not find a dedicated page, storefront listing, GitHub repo, or photo
    for this specific DC32 (2024) badge. Car Hacking Village's own site currently
    has no badge page for 2024 and its swag store does not list a badge. CHV's
    known GitHub maintainer (linted / Mike Merrill) publishes CHV badge hardware
    and the CAN-based SAO specification, but the only repos found (CHV_badge_board,
    CHV_SAO_Specification) are explicitly labeled DC31 (three SAO connectors),
    one generation earlier than the four-connector, four-CAN-network board
    described on the DC32 sheet, so I did not attach them as this badge's own
    design files. Set type to "badge" (from "sao") since the sheet's own
    functions field describes it as a 150mm board with SAO connectors and a
    CAN connector for tapping vehicle buses, i.e. a host badge rather than a
    plug-in SAO. tech.mcu (RP2040) is taken from the sheet's own functions
    field, which is consistent with CHV's prior-year badges using can2040
    (software CAN for RP2040). No image of the actual DC32 badge was found on
    the sites checked (carhackingvillage.com, swag.carhackingvillage.com,
    GitHub). Price ($100) and event association were already correct in the
    imported sheet data. Web search access was unavailable during this
    research pass, which limited coverage of press, forum, and social posts.
last_modified_date: '2026-09-06'
---

The CHV Main Badge is the Car Hacking Village's badge for DEF CON 32 (2024): a 150mm-wide board built around an RP2040 microcontroller with four onboard CAN networks and a "dry" CAN connector, letting attendees tap into real automotive bus traffic as part of the village's CTF challenges. It carries four SAO headers using CHV's own CAN-based add-on standard, which repurposes the usual I2C SAO pins for CAN TX/RX so that add-ons can talk CAN directly to the badge rather than I2C.

CHV has published hardware and a CAN-SAO specification for its badges on GitHub under the maintainer "linted" (Mike Merrill), including a CAN 2.0B-based SAO spec and board files explicitly labeled for the prior year's badge (DC31), which used three SAO connectors rather than this badge's four. No repository, storefront listing, or photo specific to the DC32 board was located, so this entry describes it using only the sheet's own listed specs plus the general CHV CAN-SAO context; the design files, exact quantity made, and current availability remain unconfirmed.
