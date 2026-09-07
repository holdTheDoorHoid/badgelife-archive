---
title: Bug Bounty Village DC33 Badge (design by Abhinav Panda)
id: dc33-abhinav-panda-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Abhinav Panda
  url: https://hackerware.io
summary: A limited-edition green badge for DEF CON 33's Bug Bounty Village, designed
  by Abhinav Panda (Hackerware.io), with a Matrix-style falling "code rain" LED
  effect behind floated acrylic and an onboard CTF.
functions: An LED matrix behind the acrylic face chases downward like falling code;
  four tactile buttons let wearers enter binary flags from eight onboard CTF
  challenges, unlocking additional LED sequences (including a secret "anti-gravity"
  mode that reverses the falling-code animation).
look:
  colors:
  - green
  - black
  shape: rectangle
  themes:
  - security
  - hardware tool
  - ctf
tech:
  mcu: ATmega16A
  leds:
    count: 41
    type: SMD
    note: Full matrix behind floated acrylic, animated to simulate falling code (Matrix-style).
  display: none
  connectivity: []
  battery: 3x AAA (included)
  sao_version: null
get_one:
  price: $99.99
  price_usd: 99.99
  quantity: limited
  availability: sold_out
  availability_note: Checked 2026-09-06; storefront listing shows sold out.
  distribution:
  - preorder
  where: Pre-order only via shop.bugbountydefcon.com; pickup at DEF CON 33, no shipping.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: shop.bugbountydefcon.com
  url: https://shop.bugbountydefcon.com/
  kind: store
- label: DEF CON Forums - Limited Edition Bug Bounty Village Badge
  url: https://forum.defcon.org/node/253153
  kind: article
- label: Hackster.io - Bug Bounty Village 2025 Badge
  url: https://www.hackster.io/HacksFromPanda/bug-bounty-village-2025-badge-e1fe09
  kind: doc
images:
- file: assets/images/badges/dc33/abhinav-panda-listed-for-def-con-33-no-details/d122e621cf.jpg
  source: "https://shop.bugbountydefcon.com/"
  credit: "Bug Bounty Village"
  caption: "Bug Bounty Village DC33 badge, powered on, showing green LED matrix code-rain effect"
- file: assets/images/badges/dc33/abhinav-panda-listed-for-def-con-33-no-details/79c2bc0409.jpg
  source: "https://shop.bugbountydefcon.com/"
  credit: "Bug Bounty Village"
  caption: "Back side of the Bug Bounty Village DC33 badge showing battery compartment"
contact:
  emails:
  - contact@bugbountydefcon.com
notes:
- 'Sheet originally listed only the maker name with no badge details ("listed for DEF CON 33, no details"). Research found the badge: the DC33 Bug Bounty Village badge, designed by Abhinav Panda of Hackerware.io.'
- Sold pre-order only, pickup at DEF CON, no shipping.
status: released
sources:
- kind: sheet
  event: dc33
  row: 3
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://shop.bugbountydefcon.com/
  title: Bug Bounty Village Shop
  accessed: '2026-09-06'
  note: Price, chip, LED count, battery, buttons, CTF challenge count, sold-out status, and product photos.
- kind: url
  url: https://forum.defcon.org/node/253153
  title: Limited Edition Bug Bounty Village Badge - Available for Pre-Order
  accessed: '2026-09-06'
  note: Confirms limited green DC33 variant, pre-order-only distribution via forum post from Bug Bounty Village organizer.
- kind: url
  url: https://www.hackster.io/HacksFromPanda/bug-bounty-village-2025-badge-e1fe09
  title: Bug Bounty Village 2025 Badge - Hackster.io
  accessed: '2026-09-06'
  note: Confirms Abhinav Panda (HacksFromPanda) as designer of the 2025 badge; acrylic/LED-matrix design description.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: This entry is a duplicate of dc33-bug-bounty-village-dc33-badge, which
    already covers the same physical badge under the Bug Bounty Village maker
    name. This entry adds the individual designer credit (Abhinav Panda /
    Hackerware.io) plus specs (MCU, LED count, battery, availability) not yet
    filled in on the other entry. Open-source status, hardware/firmware files,
    and exact quantity produced were not found on any source checked.
last_modified_date: '2026-09-06'
---

The community sheet listed Abhinav Panda as an expected DEF CON 33 maker with no further detail. Panda, who designs hardware under Hackerware.io and has built several badges for DEF CON's Bug Bounty Village in prior years, was the designer behind the Village's DC33 badge: a limited green-PCB badge with acrylic artwork floated above a full matrix of 41 SMD LEDs driven by an ATmega16A. The LEDs animate a Matrix-style "falling code" effect behind the acrylic logo, with the hacker half of the logo lit from below.

Four tactile buttons let wearers enter binary flags tied to eight onboard CTF challenges; solving them unlocks additional LED sequences, including a secret code that reverses the falling-code animation into an "anti-gravity" mode. The badge ran on 3 AAA batteries (included) and sold for $99.99, pre-order only through the Bug Bounty Village's Shopify store, with pickup at DEF CON 33 and no shipping; it sold out.

This same badge is already tracked in the archive under `dc33-bug-bounty-village-dc33-badge` (maker credited there as "Bug Bounty Village"). This entry exists because the community sheet separately listed Panda by name; no evidence was found of a second, distinct item by him at DEF CON 33.
