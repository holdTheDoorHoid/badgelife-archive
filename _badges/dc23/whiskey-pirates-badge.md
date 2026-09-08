---
title: Whiskey Pirates Badge
id: dc23-whiskey-pirates-badge
layout: badge
parent: DC23
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc23
year: 2015
makers:
- name: TrueControl
summary: An unofficial skull-and-bones badge TrueControl built for the Whiskey Pirate Crew at DEF CON 23, with RGB eye LEDs and a radio link back to the previous year's badge.
functions: Capacitive-touch spinner and select/back pads drive an RGB LED matrix in the skull's eyes; a 2.4GHz NRF24L01 radio detects nearby DC22 (2014) Whiskey Pirates badges and scrolls their owner's nickname when in range; a piezo element chirps different sounds depending on which badges are interacting.
look:
  colors:
  - black
  - copper
  shape: skull
  themes:
  - skull
  - pirate
tech:
  mcu: PSOC4
  leds:
    count: null
    type: RGB
    note: RGB LED pixels for the eyes, each on its own small PCB soldered to the back of the badge with cutouts for the light to show through; also described as a surface-mount LED matrix.
  display: none
  connectivity: []
  battery: 2x AA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  kind: article
images:
- file: assets/images/badges/dc23/whiskey-pirates-badge/ef6454becc.jpg
  source: "https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/"
  credit: "Hackaday"
  caption: "Front of the Whiskey Pirates DC23 badge, skull-and-bones design with RGB eye LEDs"
- file: assets/images/badges/dc23/whiskey-pirates-badge/f315930a03.jpg
  source: "https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/"
  credit: "Hackaday"
  caption: "Back of the badge showing the text treatment"
contact: {}
notes:
- Skull-and-bones unofficial badge with RGB LED eyes, PSOC4 chip, capacitive touch spinner controls and an NRF24L01 2.4GHz radio, made for the Whiskey Pirate Crew at DEF CON 23. Found by the event-year sweep, task dc23-all.
status: listed
sources:
- kind: url
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  title: Whiskey Pirates Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc23-all); event read as ''dc23''.'
- kind: url
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  title: All The Unofficial Electronic Badges Of DEF CON
  accessed: '2026-09-08'
  note: Confirmed the badge, maker (TrueControl), event (DEF CON 23, 2015), chip (PSOC4), LEDs, controls, radio and audio; supplied the two photos used above.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: "Only source found is the Hackaday roundup article; no maker-run page for this specific year's badge is reachable (whiskeypirates.com's dc23 subdomain link is dead/unresolvable, and trueControl's current site does not have an archived page for it). Price, quantity built and availability are not stated anywhere found, so those fields remain empty. LED count is not given, only 'a ton of LEDs' in an RGB matrix on the eyes. A companion accessory/addon or successor is not mentioned. A separate, unrelated entry already exists for the DC22 (2014) Whiskey Pirates badge (dc22-whiskey-pirates-dc22-badge) that this badge's radio talks to. tech.connectivity left empty: the badge's NRF24L01 2.4GHz link is a proprietary point-to-point radio, not a fit for any term in the controlled connectivity vocabulary; it is described under functions/tech instead."
last_modified_date: '2026-09-08'
---

The Whiskey Pirates Badge was an unofficial hardware badge designed by TrueControl for the Whiskey Pirate Crew at DEF CON 23 (2015), following up on a badge the same maker built for the crew the previous year. It keeps a skull-and-bones outline, with a matte black solder mask and copper showing through for accents, and a PSOC4 microcontroller drives an RGB LED matrix built into the skull's eyes, each eye its own small PCB soldered to the back of the badge with cutouts to let the light through. Two AA batteries power the board.

Interaction is entirely capacitive touch: a spinner wraps one eye, with separate select and back pads. A built-in NRF24L01 2.4GHz radio lets the badge talk to the crew's DC22 (2014) badges — when one of the older badges is nearby, the 2015 badge scrolls its owner's nickname on the display, and a piezo element chirps different sounds depending on which badges are interacting.

No pricing, production quantity, or open-source design files for this specific badge have turned up; it appears to have been a limited crew badge rather than a sold or widely distributed item, in keeping with the Whiskey Pirates' general practice of giving their badges away rather than selling them.
