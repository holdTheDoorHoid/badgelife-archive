---
title: Hack ‘em Crack ‘em Robots
id: dc33-hack-em-crack-em-robots
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: NilbinSec
summary: A boxing-themed DEF CON 33 badge ("The Ring") bundled with two included robot-boxer SAOs ("Red" and "Blue" Fighters) that plug in and track match data.
functions: Runs interactive boxer-vs-boxer gameplay on the main badge; the two included SAOs store match data via I2C EEPROM and contain hidden interactions with other badges and CTFs around the con.
look:
  colors: []
  shape: null
  themes:
  - robot
  - retro computer
  - arcade
  - game
tech:
  mcu: Raspberry Pi Pico
  leds: null
  display: 0.96" OLED
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: $79.99
  price_usd: 79.99
  quantity: ''
  availability: unknown
  distribution:
  - preorder
  where: Pre-order via the maker's RENXCHANGE storefront, for pickup in person at DEF CON 33 (no shipping); drops announced on NilbinSec's social channels.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: renxchange.com/products/hack-em-crack-em-robots-limited-badge-release-for-def-con-33-by-nilbinsec
  url: https://renxchange.com/products/hack-em-crack-em-robots-limited-badge-release-for-def-con-33-by-nilbinsec
  kind: website
images:
- file: assets/images/badges/dc33/hack-em-crack-em-robots/da8946e3f8.jpg
  source: "https://web.archive.org/web/20250716001015/https://renxchange.com/products/hack-em-crack-em-robots-limited-badge-release-for-def-con-33-by-nilbinsec"
  credit: "NilbinSec / RENXCHANGE"
  caption: "Hack 'Em Crack 'Em Robots badge and SAOs, product photo"
- file: assets/images/badges/dc33/hack-em-crack-em-robots/45e04c68b7.jpg
  source: "https://web.archive.org/web/20250716001015/https://renxchange.com/products/hack-em-crack-em-robots-limited-badge-release-for-def-con-33-by-nilbinsec"
  credit: "NilbinSec / RENXCHANGE"
  caption: "Hack 'Em Crack 'Em Robots badge and SAOs, additional product photo"
contact:
  emails:
  - Nilbinsec@gmail.com
notes:
- Our Linktr.ee/nilbinsec has our socials where drops will be announced. This badge supports giving away 800 SAOs to attendees this year!
status: listed
sources:
- kind: sheet
  event: dc33
  row: 11
  updated: 6/20/2025 20:39:49
- kind: url
  url: https://web.archive.org/web/20250716001015/https://renxchange.com/products/hack-em-crack-em-robots-limited-badge-release-for-def-con-33-by-nilbinsec
  title: "Hack 'Em Crack 'Em Robots Limited Badge Release for DC33 By NilbinSec – RENXCHANGE (archived)"
  accessed: '2026-09-06'
  note: Live storefront listing at renxchange.com now returns a Shopify "store unavailable" page; used the Wayback Machine capture from 2025-07-16, which is the maker's own product description, price, contents, and photos. Also source for MCU, display, EEPROM/SAO details, quantity of free giveaway SAOs, and pickup terms.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    The renxchange.com storefront is now dead (Shopify "store unavailable"); all technical
    and pricing details come from a Wayback Machine capture of the original product page
    (2025-07-16). The community sheet listed this as an SAO ($80, row functions text about
    "SAOs"), but the maker's own page describes the $79.99 purchase as a bundle: a main
    badge called "The Ring" (Raspberry Pi Pico, OLED display, game controls) plus two
    included SAOs, "Red" and "Blue" Fighters, so type was changed from sao to badge to
    match. Could not find a Hackaday.io page, GitHub repo, or open-source hardware/firmware
    for this project, nor confirm actual unit quantity, LED count/type, battery, or
    SAO header version — left empty rather than guessed. Could not confirm whether it
    was actually released/sold at DEF CON 33 versus only pre-ordered; sources found only
    cover the pre-order listing, so `status` is left as `listed` and `get_one.availability`
    as `unknown`.
last_modified_date: '2026-09-06'
---

NilbinSec's first for-sale badge at DEF CON 33 was a boxing-themed set called "Hack 'Em Crack 'Em Robots" — a nod to the classic Rock 'Em Sock 'Em Robots toy. The $79.99 bundle centered on a main badge, "The Ring," built around a Raspberry Pi Pico with an OLED display and onboard game controls, sold fully assembled with no soldering required. Every purchase included two SAOs, "Red" and "Blue" Fighters, styled as retro robot boxers; they plugged into the Ring and stored per-match data on I2C EEPROMs, with hidden interactions tied to other badges and CTFs around the con.

The listing was a pre-order for in-person pickup only at DEF CON 33 (no shipping), with drop timing announced through NilbinSec's social channels and the Badgemakers Community. According to the maker, proceeds from the badge helped fund an unrelated free giveaway of over 800 SAOs to attendees that year. The original storefront listing (renxchange.com) is no longer live; this entry is reconstructed from an archived copy of that page, so it is not confirmed whether the badge actually shipped, how many were made, or what happened after the pre-order period.
