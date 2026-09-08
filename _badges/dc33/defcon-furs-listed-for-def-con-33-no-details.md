---
title: DEFCON Furs 2025 Badge
id: dc33-defcon-furs-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: DEFCON Furs
  url: https://2025.dcfurs.com
summary: 'The 2025 #badgelife badge from DEFCON Furs, the furry-fandom meetup group that throws parties alongside DEF CON; it doubles as entry to their events and supports two Shitty Add-Ons.'
functions: LoRa radio "chirping", NFC, touch points including a "boop" sensor, MicroPython-scriptable RGB LED patterns.
look:
  colors:
  - black
  - white
  - copper
  shape: animal head
  themes:
  - animal
  - radio
tech:
  mcu: RP2040
  leds:
    count: 36
    type: RGB
    note: ''
  display: null
  connectivity:
  - lora
  - nfc
  battery: null
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: $150 assembled / $40 blank PCB (minimum donation)
  price_usd: 150
  quantity: ''
  availability: unknown
  availability_note: The 2025 site says "Pre-orders until August 3rd 2025"; badges were also sold onsite at the DEFCON Furs events and at the Hacker Warehouse booth in the DEF CON vendor space, subject to availability. Live 2025.dcfurs.com/register checked 2026-09-06; it no longer offers a way to buy, and no sold-out statement was found.
  distribution:
  - preorder
  - purchase
  where: Preordered via Stripe donation links on the DEFCON Furs 2025 site (assembled or blank-PCB tiers), picked up or bought onsite at their Gypsy/Piranha nightclub events, or purchased assembled at the Hacker Warehouse booth in the DEF CON vendor space.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: The maker said the badge software and parts list would be "posted publicly on GitHub soon"; no repository was found as of 2026-09-06.
links:
- kind: website
  label: DEFCON Furs 2025 registration/badge page
  url: https://2025.dcfurs.com/register
  archived: https://web.archive.org/web/20260908004248/https://2025.dcfurs.com/register
- kind: website
  label: DEFCON Furs main site
  url: https://dcfurs.com/
images:
- file: assets/images/badges/dc33/defcon-furs-listed-for-def-con-33-no-details/ec6a3ac825.jpg
  source: https://2025.dcfurs.com/register
  credit: DEFCON Furs
  caption: DEFCON Furs 2025 badge, blank PCB version
  archived: https://web.archive.org/web/20260908004248/https://2025.dcfurs.com/register
contact: {}
notes:
- Sheet listed only "DEFCON Furs" as an expected DC33 maker with no other details; retitled from the sheet placeholder once the 2025 badge details were found on the group's own site.
- This badge grants entry to DEFCON Furs' own party space (Gypsy/Piranha nightclubs), not to DEF CON itself; attendees still need an official DEF CON badge separately.
status: released
sources:
- kind: sheet
  event: dc33
  row: 38
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://2025.dcfurs.com/register
  title: DEFCON Furs | Registration
  accessed: '2026-09-06'
  note: 'Primary source: badge tiers/pricing ($150 assembled, $40 blank PCB), RP2040/36 RGB LED/LoRa/NFC/touch spec, SAO v1.69bis x2 support, distribution channels, and the badge photo (assets/img/dcfurs-badge-2025-blank.jpg, alt "Picture of DEFCON Furs 2025 Badge PCB blank"). Fetched live on 2026-09-06.'
  archived: https://web.archive.org/web/20260908004248/https://2025.dcfurs.com/register
- kind: url
  url: https://dcfurs.com/
  title: DEFCON Furs
  accessed: '2026-09-06'
  note: Background on the group (furry-fandom meetup at DEF CON) and link to the 2025 event site; no 2025-specific badge details on this page itself. Mentions the 2018 "Wrench Fox" boop badge as an earlier project.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core specs and pricing come from the maker''s own 2025 registration page and were re-checked against the live page on 2026-09-06. Not found: LED part number, battery/power, firmware/hardware repo (the page only promises a GitHub post), and quantity made. Fact-check removed unsupported references to earlier badge names ("Cereal Booper", "Vixy"), a "membership" distribution tag, and a "security" theme; colors/shape were set from the saved PCB photo.'
last_modified_date: '2026-09-06'
---

DEFCON Furs is a furry-fandom meetup group that throws parties alongside DEF CON each year, and their 2025 badge is described on their site as the next iteration of the group's #badgelife badge. The badge itself does not admit anyone to DEF CON; instead it grants entry to the group's own event space, which for 2025 for 2025 was the Gypsy and Piranha nightclubs in the Fruit Loop District, plus drink tickets and re-entry privileges.

The 2025 badge runs on an RP2040 with 36 RGB LEDs, LoRa "chirping," NFC, MicroPython-scriptable behavior, touch points (including a return of the "booping" interaction from earlier years), and two SAO v1.69bis ports for add-ons. It was offered as a $150 minimum-donation fully assembled badge or a $40 minimum-donation blank PCB, both preorderable via Stripe ahead of the event or purchased onsite; assembled units were also sold at the Hacker Warehouse booth in the DEF CON vendor space. The maker said firmware and a parts list would be posted to GitHub, but no such repository has surfaced yet.
