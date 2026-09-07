---
title: STORE BADGE
id: saintcon-2021-store-badge
layout: badge
parent: Saintcon 2021
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2021
year: 2021
makers:
- name: Jup1t3r
summary: A beginner-level SAINTCON minibadge with two LEDs and a jumper-selectable blink or solid-on mode.
functions: 'Lights two LEDs (D1, D2); a solder jumper on the back selects blinking (middle+bottom pads) or solid-on (middle+top pads).'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds:
    count: 2
    type: null
    note: 'Two through-hole LEDs (D1, D2); orient with the green dot toward the right of the board.'
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: "SAINTCON's own badge store, per the minibadge.wiki community record."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=STORE%20BADGE&year=2021
  url: https://minibadge.wiki/?search=STORE%20BADGE&year=2021
  kind: store
images:
  - file: assets/images/badges/saintcon-2021/store-badge/8e1bbe65d3.jpg
    source: "https://minibadge.wiki/2021.json"
    credit: "Jup1t3r"
    caption: "STORE BADGE minibadge, front, showing two LEDs and jumper pads"
  - file: assets/images/badges/saintcon-2021/store-badge/e1b4a495f9.jpg
    source: "https://minibadge.wiki/2021.json"
    credit: "Jup1t3r"
    caption: "STORE BADGE minibadge, back, showing resistor and soldering instructions"
contact: {}
notes:
- 'Community sheet lists quantityMade as 0 and leaves category, boardHouse, howToAcquire, and rarity blank; treated here as not stated rather than "zero made."'
status: listed
sources:
- kind: url
  url: https://minibadge.wiki/?search=STORE%20BADGE&year=2021
  title: STORE BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2021''.'
- kind: url
  url: https://minibadge.wiki/2021.json
  title: 'MiniBadge Wiki 2021 data (STORE BADGE record)'
  accessed: '2026-09-07'
  note: 'Underlying JSON record behind the minibadge.wiki listing page: soldering instructions, LED count/orientation, jumper behavior, and front/back images.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'The minibadge.wiki listing page itself is a JS search UI with no static content; the actual record lives in its underlying 2021.json data file, which supplied the soldering/LED/jumper details and both images. No maker page, storefront, or press coverage for "Jup1t3r" or this specific badge was found beyond that community record, so price, quantity, chip (there is none — it is a passive LED board), colors, and shape remain unknown. Web search was unavailable for this task (session search budget exhausted), so only the existing link and its data file were checked.'
last_modified_date: '2026-09-07'
---

The STORE BADGE is a beginner-friendly SAINTCON 2021 minibadge made by Jup1t3r, sold through SAINTCON's own badge store rather than distributed as a village or vendor giveaway. It's a simple soldering-practice board: two through-hole LEDs (D1 and D2) and a single resistor, with no microcontroller.

A three-pad jumper on the back sets the badge's behavior after assembly — bridging the middle and bottom pads makes the LEDs blink, while bridging the middle and top pads holds them solid on. The listing warns builders not to bridge all three pads at once, since that can short the badge and cause problems for the whole board.

Beyond the assembly instructions and the two photos captured here, little else about this badge is documented publicly: quantity made, price, and exact release details were not found in any source checked for this entry.
