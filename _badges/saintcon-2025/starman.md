---
title: Starman
id: saintcon-2025-starman
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: ScalyOne
summary: 'A tribute minibadge to EarthBound''s Starman enemy, pairing pixel-art
  character art with a quote from the game.'
functions: 'A single LED behind the Starman figure that can be set, via a solder
  jumper, to either blink or stay solid.'
look:
  colors:
  - gold
  - black
  - white
  shape: robot
  themes:
  - retro computer
  - console
  - sci-fi
  - pop culture
tech:
  mcu: none
  leds:
    count: 1
    type: through-hole
    note: Single LED at D1 with a series resistor at R1; a jumper selects blink
      vs. solid.
  display: null
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - swap
  where: 'Not sold; the maker''s submission says "Trade with me."'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Starman&year=2025
  url: https://minibadge.wiki/?search=Starman&year=2025
  kind: website
- label: minibadge.wiki 2025 data export (JSON)
  url: https://minibadge.wiki/2025.json
  kind: doc
images:
  - file: assets/images/badges/saintcon-2025/starman/60adf59529.jpg
    source: "https://minibadge.wiki/2025.json"
    credit: "ScalyOne"
    caption: "Front of the Starman minibadge, pixel-art tribute to EarthBound's Starman enemy, with an LCD-style text box reading a Buzz Buzz quote"
  - file: assets/images/badges/saintcon-2025/starman/e1883f93d6.jpg
    source: "https://minibadge.wiki/2025.json"
    credit: "ScalyOne"
    caption: "Back of the Starman minibadge showing the through-hole LED, resistor, and jumper for the blink/solid mode"
contact: {}
notes:
- 'category: Personal; rarity: Rare'
- 'Maker''s soldering instructions describe the build as beginner difficulty: solder
  R1 (no orientation), place the D1 LED with its anode in the round through-hole
  bent behind the figure, split the 8-pin header into four 2-pin corner headers,
  and optionally bridge a jumper for blink mode.'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=Starman&year=2025
  title: Starman
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2025''.'
- kind: url
  url: https://minibadge.wiki/2025.json
  title: MiniBadge Wiki 2025 data export
  accessed: '2026-09-07'
  note: The search page itself is a client-rendered app with no server-side content;
    its underlying 2025.json data export (linked from minibadge.wiki/data/) carries
    the maker's own submission record for this badge, including description,
    soldering instructions, quantity made, category, rarity, how to acquire it,
    and the front/back image files used here.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: All facts come from the maker's (ScalyOne) own submission on the community
    minibadge.wiki sheet, so this is a primary source, but no independent
    corroboration (maker page, repo, storefront, press) was found. quantityMade
    is recorded as 0 in the source data, which likely means "not tracked" rather
    than zero actually made; left get_one.quantity empty rather than guess.
    No hardware/firmware files, price, or MCU were found or claimed; the badge
    appears to be a simple passive LED board with no microcontroller.
last_modified_date: '2026-09-07'
---

The Starman minibadge is ScalyOne's tribute to the Starman enemy from the SNES
role-playing game EarthBound. The front of the badge reproduces the character
in pixel art alongside a text box quoting the game's Buzz Buzz character
("It's been a long time, Buzz Buzz."), styled to look like the game's own
dialogue boxes.

Electronically it is a simple, beginner-friendly build: a single through-hole
LED sits behind the Starman figure, lit through one series resistor, with no
microcontroller on board. A solder jumper lets the builder choose whether the
LED blinks or stays solid. The eight-pin header is split into four two-pin
corner headers for mounting.

ScalyOne categorizes it as a "Personal" badge and marks it "Rare," made to
trade in person at SAINTCON rather than sold; the maker's own listing simply
says "Trade with me." No quantity, price, or design files were published.
