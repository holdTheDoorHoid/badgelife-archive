---
title: DC435 Ultra
id: saintcon-2022-dc435-ultra
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Sh33pr0ck
summary: A super-rare DC435 minibadge with an RGB LED that cycles colors and broadcasts preloaded i2c messages, made to be traded rather than handed out freely.
functions: 'Right pad cycles LED colors; left pad cycles through preloaded messages sent over i2c, readable by previous years'' badges or anything else that can read them. The ICSP header is exposed for reprogramming.'
look:
  colors:
  - green
  - gold
  shape: rectangle
  themes:
  - security
  - text
tech:
  mcu: ATtiny841
  leds:
    count: 1
    type: RGB
    note: Common-anode RGB LED, driven from pins Red=2, Green=3, Blue=7 (Arduino/ATTiny Core numbering)
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: rumored
  distribution:
  - swap
  where: Not distributed through a normal line; the designer says to find him wandering the con and trade something cool and unique for it. "Very few available."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: SAINTCON MiniBadge Assembly Guide 2022 (PDF, p.85, "DC435 Ultra")
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: doc
images:
  - file: assets/images/badges/saintcon-2022/dc435-ultra/front.png
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "Sh33pr0ck"
    caption: "Front of the DC435 Ultra minibadge, DC435 silkscreened between two skull-and-crossbones icons"
  - file: assets/images/badges/saintcon-2022/dc435-ultra/back.png
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "Sh33pr0ck"
    caption: "Back of the DC435 Ultra minibadge, showing the ATtiny841, RGB LED, and resistor placements"
contact: {}
notes:
- The community sheet listed only the title and a few specs seen in a search snippet; this pass confirmed it against the official 2022 SAINTCON MiniBadge Assembly Guide PDF (page 85, printed as "PAGE 85"; the entry's original link mislabeled it as "page ~34").
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON MiniBadge Assembly Guide 2022 - DC435 Ultra (p.85)
  accessed: '2026-09-10'
  note: Primary source; confirmed maker, chip, LED type, i2c messaging function, pinout, rarity/difficulty rating, and distribution method ("find me wandering around and trade").
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Confirmed on the official SAINTCON 2022 MiniBadge Assembly Guide PDF, which is the maker/organizer's own document. No secondary coverage (Hackaday, Reddit, storefronts) was found for this item, which is expected for a small-run trade-only con minibadge. Quantity made and exact price are not stated anywhere in the source; distribution was purely by in-person trade with the designer, so get_one.price/quantity are left empty. No repo or design files were found, so make_your_own fields are left null/empty.
last_modified_date: '2026-09-10'
---

The DC435 Ultra is a SAINTCON 2022 minibadge designed by Sh33pr0ck for the DC435 (DEF CON Group 435, Salt Lake City) crowd, built around an ATtiny841 driving a single common-anode RGB LED. One capacitive-style pad cycles the LED through colors; a second pad steps through a set of preloaded messages that the badge broadcasts over i2c, readable by prior years' SAINTCON badges or any other device capable of listening on the bus. An exposed ICSP header lets an owner reflash it with their own firmware using the Arduino ATTiny Core (pin map: Red=2, Green=3, Blue=7, right pad=10, left pad=9, wire mode slave-only, counterclockwise pin map).

Unlike most minibadges on the sheet, the Ultra was not handed out at a booth or built from a kit table: the guide rates it "intermediate" difficulty and "super rare," notes the RGB LED and ATtiny came pre-soldered because both are difficult to hand-solder while keeping all colors functional, and says it was distributed only by finding the designer in person and trading him "something cool and unique" for it. It pairs with the more common "DC435 BUS" minibadge from the same year and designer, also part of the DC435 minibadge family for that SAINTCON.

No secondary write-ups, storefront listings, or a public repository for this badge were found; the assembly guide itself, published by SAINTCON, is the only confirmed source.
