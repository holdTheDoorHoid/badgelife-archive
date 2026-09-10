---
title: BABY YODA BADGE
id: saintcon-2022-baby-yoda-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Mr. & Mrs bfcoder
summary: 'A personal SAINTCON minibadge depicting Grogu ("Baby Yoda") eating a cookie and barfing, with two LEDs that can be jumpered to blink or stay solid.'
functions: 'Two LEDs light up the design; a solder jumper on the front selects between blink and solid illumination modes.'
look:
  colors:
  - green
  - gold
  shape: yoda
  themes:
  - tv
  - meme
  - pop culture
  - food
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two single-color LEDs (D1, D2); a solder jumper selects blink vs. solid illumination.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - swap
  where: Traded in person with the maker (bfcoder) at SAINTCON 2022; not sold.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
- label: Minibadge Wiki
  url: https://minibadge.wiki/
  kind: website
images:
- file: assets/images/badges/saintcon-2022/baby-yoda-badge/5597866edc.jpg
  source: "https://minibadge.wiki/"
  credit: "Mr. & Mrs bfcoder"
  caption: "Baby Yoda minibadge, front (bare PCB with R1, D1, D2 and jumper header)"
- file: assets/images/badges/saintcon-2022/baby-yoda-badge/2f8905329e.jpg
  source: "https://minibadge.wiki/"
  credit: "Mr. & Mrs bfcoder"
  caption: "Baby Yoda minibadge, back: printed Grogu artwork with \"COOKIES WE ACCEPT\""
contact: {}
notes:
- Personal Baby Yoda-themed minibadge by Mr. & Mrs bfcoder. Found by the event-year sweep, task saintcon-2022.
- 'The community-run Minibadge Wiki (minibadge.wiki, data from Pips801/minibadge-wiki on GitHub) lists this as category "Personal" with rarity "Rare" and a solder difficulty of "Beginner"; its "quantityMade" field is 0, which reads as unfilled rather than a confirmed count, so quantity is left blank here.'
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: BABY YODA BADGE
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON Minibadge Assembly Guide 2022 (official build guide, page 46)
  accessed: '2026-09-10'
  note: 'Confirmed the item is a real, official 2022 minibadge with description "Baby Yoda eating a cookie and barfing," beginner difficulty, rare rarity, trade-only acquisition, and assembly steps (resistor, LEDs, blink/solid jumper, 3x 2-position headers).'
- kind: url
  url: https://minibadge.wiki/
  title: Minibadge Wiki - community catalog of SAINTCON minibadges
  accessed: '2026-09-10'
  note: 'Structured record (2022.json, via github.com/Pips801/minibadge-wiki) matching the build guide, plus front and back photos of the actual badge used for the saved images.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Confirmed as a real, official SAINTCON 2022 minibadge (not just a sweep snippet): the build-guide PDF and the independent Minibadge Wiki catalog agree on the title, maker, description, and trade-only distribution. No chip/MCU is involved -- it is a passive LED board with a jumper-selectable blink/solid mode, powered from the host badge like other minibadges. No price, exact quantity, or design-file links were found; the maker does not appear to publish hardware/firmware sources for this one.'
last_modified_date: '2026-09-10'
---

The Baby Yoda Badge is a personal SAINTCON 2022 minibadge designed by Mr. & Mrs bfcoder, depicting Grogu ("Baby Yoda") from *The Mandalorian* eating a cookie -- and, per the maker's own description, barfing. The board carries the tagline "COOKIES WE ACCEPT" on its printed side and is cut to an ear-and-hood silhouette rather than a plain rectangle.

Electrically it is a simple, beginner-difficulty build: a single resistor (R1) and two LEDs (D1, D2), with a small solder jumper that lets the builder choose between a blinking or solid-on illumination mode. Like other SAINTCON minibadges, it draws power from the host conference badge rather than carrying its own battery or microcontroller.

The badge was not sold or distributed as a kit; it was made to trade in person with bfcoder at SAINTCON 2022, and the community-run Minibadge Wiki lists its rarity as "Rare." No design files, exact production quantity, or price have been published for it.
