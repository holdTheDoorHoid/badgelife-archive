---
title: LHC Meshtastic Badge
id: dc33-lhc-meshtastic-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Lonely Hackers Club
  url: https://lonelyhackers.club/
summary: A LoRa mesh-networking badge from Lonely Hackers Club for DEF CON 33, pre-configured to join the DEFCONnect Meshtastic network out of the box.
functions: ESP32-S3 with Lora radio, integrated antenna, runs meshtastic, 8x RGB leds, SAO
look:
  colors: []
  shape: null
  themes:
  - radio
  - mesh networking
tech:
  mcu: ESP32-S3-N16R8
  leds:
    count: 8
    type: RGB
    note: First 6 LEDs double as a color-coded PIN display for Bluetooth pairing (red=4, green=5, blue=6).
  display: none
  connectivity:
  - lora
  - meshtastic
  battery: LiPo 1000 mAh, USB-C charging
  sao_version: null
get_one:
  price: $100
  price_usd: 100.0
  quantity: '50'
  availability: sold_out
  availability_note: Maker's page shows a commented-out "SOLD OUT / more stock coming soon" buy button as of 2026-09-06; limited to 50 units.
  distribution:
  - purchase
  where: Purchased in advance via the maker's site (Stripe checkout), picked up in person starting August 7, 2025 at the LHC DEF CON meetup.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: Runs a custom build of Meshtastic firmware (badge control UI, RGB LED control) layered on stock Meshtastic; maker's page does not link a hardware or firmware repo.
links:
- label: lonelyhackers.club/badge
  url: https://lonelyhackers.club/badge
  kind: website
images:
- file: assets/images/badges/dc33/lhc-meshtastic-badge/c243c66a02.png
  source: "https://lonelyhackers.club/badge"
  credit: "Lonely Hackers Club"
  caption: "LHC Meshtastic Badge 2025, front"
- file: assets/images/badges/dc33/lhc-meshtastic-badge/d6c0063ee9.png
  source: "https://lonelyhackers.club/badge"
  credit: "Lonely Hackers Club"
  caption: "LHC Meshtastic Badge 2025, back"
contact:
  emails:
  - lhcbadge@grink.solutions
notes:
- Pickup starting wednesday at LHC meetup
status: released
sources:
- kind: sheet
  event: dc33
  row: 23
  updated: 7/11/2025 12:14:21
- kind: url
  url: https://lonelyhackers.club/badge
  title: "LHC Badge :: Lonely Hackers Club"
  accessed: '2026-09-06'
  note: "Maker's own product page: full specs, features, price/quantity (in a commented-out sold-out notice), pairing instructions, pickup logistics, and badge photos."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Maker''s own page confirms specs, price ($100, limited to 50, shown sold out), and distribution, so most fields are well supported. No hardware or firmware repository is linked anywhere on the page, and a search of the Lonely Hackers Club GitHub org (github.com/LonelyHackersClub) turned up only unrelated repos (lonely_hackers_news, a lobsters fork) — none for the badge. Could not find a Hackaday.io project page or press coverage; a general web search could not be run this session (search budget exhausted), so it is possible independent coverage exists that was not checked. sao_version and look.colors/shape left empty: no photo or text pinned down PCB color or an SAO header pinout. Confidence set to medium rather than high because availability/quantity comes from a commented-out block in the page HTML rather than visible text.'
last_modified_date: '2026-09-06'
---

The LHC Meshtastic Badge 2025 is a LoRa mesh-networking wearable that Lonely Hackers Club, a DEF CON-adjacent hacker community, made for its members at DEF CON 33. It pairs an ESP32-S3-N16R8 with a Semtech SX1262 LoRa radio and an integrated 915 MHz antenna (with a resistor-swap option to break out to an external SMA antenna), and ships pre-loaded with a custom Meshtastic build that adds a badge control interface and RGB LED effects on top of stock Meshtastic. Eight programmable RGB LEDs handle both decoration and a practical trick: the first six double as a color-coded PIN display (red=4, green=5, blue=6) so a badge can be Bluetooth-paired to the Meshtastic phone app without a screen. Power comes from a 1000 mAh Li-Ion cell charged over USB-C, and a SAO connector lets it host other badgelife add-ons.

The badge was sold in advance through the maker's own site for $100, limited to 50 units, with pickup only at DEF CON 33 starting August 7, 2025 at an LHC meetup; the listing on the maker's page is now marked sold out. Every unit came pre-configured with the DEFCONnect channel plus an LHC-only secondary channel, tuned for the size of mesh the convention floor creates. No hardware design files or a firmware repository are linked from the product page, so despite running an open-source base (Meshtastic itself), this specific badge's own board and firmware customizations do not appear to be published.
