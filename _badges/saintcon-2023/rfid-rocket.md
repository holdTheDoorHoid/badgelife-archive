---
title: RFID Rocket
id: saintcon-2023-rfid-rocket
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: SHIFTY
summary: A red, rocket/arrow-shaped SAINTCON minibadge with "RFID" lettering and radio-wave arcs, lit by one always-on white LED and one blinking red LED.
functions: One white LED stays lit continuously; one red LED (mounted on the rocket's tail) blinks.
look:
  colors: [red, white, grey]
  shape: rocket
  themes: [radio, minimalist, text]
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Single-pad-soldered SMD LEDs; 1 white always-on, 1 blinking red on the rocket's tail.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: [swap]
  where: Traded or bartered in person at the Badge Life Community area at SAINTCON 2023; not sold.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=RFID%20Rocket&year=2023
  url: https://minibadge.wiki/?search=RFID%20Rocket&year=2023
  kind: website
- label: minibadge.wiki 2023 data export (JSON)
  url: https://minibadge.wiki/2023.json
  kind: doc
images:
  - file: assets/images/badges/saintcon-2023/rfid-rocket/c559feb3be.png
    source: "https://minibadge.wiki/data/"
    credit: "SHIFTY"
    caption: "RFID Rocket minibadge, front"
  - file: assets/images/badges/saintcon-2023/rfid-rocket/99c77eb1d5.png
    source: "https://minibadge.wiki/data/"
    credit: "SHIFTY"
    caption: "RFID Rocket minibadge, back"
contact: {}
notes:
- 'category: Personal; rarity: Super Rare'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=RFID%20Rocket&year=2023
  title: RFID Rocket
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2023''.'
- kind: url
  url: https://minibadge.wiki/2023.json
  title: MiniBadge Wiki 2023 data export
  accessed: '2026-09-07'
  note: The search page renders client-side from this JSON export; contains the actual submitted record (author, description, soldering instructions, category, rarity, quantityMade, howToAcquire, image filenames) for RFID Rocket by SHIFTY.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >
    Despite the name, the maker's own description and soldering instructions describe only two
    LEDs (one always-on white, one blinking red) with no RFID reading/tagging function mentioned
    or any MCU — "RFID" appears to be thematic (the artwork shows radio-wave arcs), not a real
    RFID feature, so tech.connectivity is left empty rather than guessed. quantityMade in the
    source record is 0, which the wiki appears to use as "not disclosed" rather than "none made";
    left get_one.quantity empty rather than reporting a false zero. No repo, storefront, or design
    files were found for this minibadge; it was distributed by trade/barter per the maker's own
    "how to acquire" text, not sold, so pricing fields are left empty.
last_modified_date: '2026-09-07'
---

RFID Rocket is a SAINTCON 2023 minibadge by SHIFTY: a red, arrow/rocket-shaped PCB stenciled with "RFID" lettering and a set of radio-wave arcs fanning off the nose. It is a simple, beginner-level build — SMD LEDs and resistors soldered using the single-pad method — with one white LED that stays on continuously and one red LED, mounted on the rocket's tail, that blinks. There is no microcontroller and no indication in the maker's own materials that it actually reads or emits RFID; the name and radio-wave graphic appear to be purely thematic.

The badge was not sold. Per the maker's own "how to acquire" note, it was handed out through in-person trading and bartering at the Badge Life Community area at SAINTCON 2023, and the community wiki lists it as "Super Rare" in the "Personal" category.
