---
title: Flipper Zero to Minibadge add-on
id: saintcon-2025-flipper-zero-to-minibadge-add-on
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: Pips
summary: 'An adapter that lets a Flipper Zero drive a SAINTCON minibadge, and bridges I2C so the Flipper can talk to minibadges that use I2C.'
functions: 'Connects a Flipper Zero to a standard minibadge socket so the Flipper can display/drive the minibadge, and exposes I2C (SDA/SCL) for reading I2C communication from minibadges that use it.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '0 (per maker''s listing)'
  availability: unknown
  distribution:
  - swap
  where: 'Trade directly with the maker (Pips); not sold.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Flipper%20Zero%20to%20Minibadge%20add-on&year=2025
  url: https://minibadge.wiki/?search=Flipper%20Zero%20to%20Minibadge%20add-on&year=2025
  kind: website
images:
- file: assets/images/badges/saintcon-2025/flipper-zero-to-minibadge-add-on/9f002c19e9.jpg
  source: "https://minibadge.wiki/?search=Flipper%20Zero%20to%20Minibadge%20add-on&year=2025"
  credit: "Pips"
  caption: "Front of the Flipper Zero to Minibadge add-on"
- file: assets/images/badges/saintcon-2025/flipper-zero-to-minibadge-add-on/bc8729ba0e.jpg
  source: "https://minibadge.wiki/?search=Flipper%20Zero%20to%20Minibadge%20add-on&year=2025"
  credit: "Pips"
  caption: "Back of the Flipper Zero to Minibadge add-on"
contact: {}
notes:
- 'category: Other; rarity: Rare'
- 'Soldering instructions (maker, minibadge.wiki): solder the 1x10 pin header row downwards; solder the two 1x8 pin sockets facing upwards. Optionally bridge the SDA and SCL pads to use a Flipper Zero app that can read I2C communications. Do not bridge the CLK pad — it does not work correctly for badges that use CLK for alternating light patterns.'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=Flipper%20Zero%20to%20Minibadge%20add-on&year=2025
  title: Flipper Zero to Minibadge add-on
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2025''.'
- kind: url
  url: https://minibadge.wiki/2025.json
  title: MiniBadge Wiki 2025 data feed (Flipper Zero to Minibadge add-on entry)
  accessed: '2026-09-07'
  note: 'The wiki page renders from this JSON feed; used it to get the maker''s own description, soldering instructions/difficulty, category, quantity made (0), rarity, acquisition method ("Trade with me!"), and front/back image URLs.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched https://minibadge.wiki/2025.json directly and confirmed every non-empty field (quantityMade: 0, category: Other, rarity: Rare, howToAcquire: "Trade with me!", the full soldering-instructions text) against the maker''s own JSON record. Confirmed both saved images (9f002c19e9.jpg front, bc8729ba0e.jpg back) are byte-for-byte the same artwork as frontImageUrl/backImageUrl on that record. Removed the "minibadge" look.theme tag: not in the guide''s shared vocabulary and redundant with type: minibadge. Only source is the maker''s own listing on the community minibadge.wiki database; no separate maker page, repo, or store listing was found. Chip/MCU, LEDs, display, power/battery, price, and open-source/design-file status are not stated anywhere and remain empty. "Quantity made" is listed as 0 on the source, which likely means the maker did not report a count rather than that none exist (it is a physical, tradeable minibadge per the listing); recorded as given rather than guessed.'
last_modified_date: '2026-09-07'
---

Pips made this SAINTCON 2025 minibadge as an adapter rather than a display piece: it plugs a Flipper Zero into the standard minibadge socket so the Flipper can drive whatever minibadge is attached, and it breaks out I2C (SDA/SCL) so the Flipper can listen in on minibadges that communicate over I2C. Assembly is a single 1x10 pin header soldered facing down plus two 1x8 pin sockets facing up, rated beginner difficulty; the maker notes the SDA/CLK bridge pads can optionally be shorted to use a Flipper Zero app that reads I2C traffic, but warns against bridging the CLK pad since it breaks minibadges that use CLK for alternating light patterns.

It is filed as "Other" category and "Rare" on the community minibadge.wiki listing, and the maker's own note on how to get one is simply "Trade with me!" — it was not sold or dropped freely, only swapped in person.
