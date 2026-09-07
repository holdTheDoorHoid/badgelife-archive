---
title: Peanut Butter SAO
id: dc27-peanut-butter-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/twinkletwinkie
summary: A peanut-butter-jar shaped SAO on a 4-layer PCB with six white 1204 side-view LEDs and one 10-15 ohm resistor, riffing on the GIF-versus-Jif pronunciation debate under the tagline "Choosy moms choose Gif".
functions: 'Backlights the word "Gif" (styled after the Jif peanut butter logo) with white LEDs; no interactive or game functions.'
look:
  colors: [white]
  shape: null
  themes: [meme, food, text, logo]
tech:
  mcu: none
  leds:
    count: 6
    type: 1204 side-view (white)
    note: 10-15 ohm series resistor; second revision moved to a 4-layer board using the two inner copper layers to mask light bleed around the "Gif" lettering.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/174028-peanut-butter-sao
  firmware_url: null
  eda_tool: null
  notes: 'Hardware files (Gerbers for the 4-layer revision) are downloadable from the Hackaday.io project page as "GIF_4L_2019-07-23-0017.zip". No firmware exists since the board is passive (LEDs + resistor, no MCU).'
links:
- label: hackaday.io/project/174028-peanut-butter-sao
  url: https://hackaday.io/project/174028-peanut-butter-sao
  kind: hackaday
- label: hackaday.io/twinkletwinkie
  url: https://hackaday.io/twinkletwinkie
  kind: hackaday
images:
- file: assets/images/badges/dc27/peanut-butter-sao/83979c4025.jpg
  source: "https://hackaday.io/project/174028-peanut-butter-sao"
  credit: "TwinkleTwinkie"
  caption: "Peanut Butter SAO, styled after a Jif peanut butter jar label"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/174028-peanut-butter-sao
  title: Peanut Butter SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/174028-peanut-butter-sao
  title: Peanut Butter SAO
  accessed: '2026-09-07'
  note: 'Confirmed design story, LED count/type, resistor value, and the two-revision history (6-LED v1 with light bleed, 4-layer v2 with copper masking); source of the saved image.'
- kind: url
  url: https://hackaday.io/twinkletwinkie
  title: TwinkleTwinkie's Profile
  accessed: '2026-09-07'
  note: Confirmed maker identity, that Peanut Butter SAO was made in 2019, and the DEF CON badge/SAO community context of other TwinkleTwinkie projects.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No maker page or third-party source states a price, quantity made, or whether it was sold, given away, or is still available, so get_one fields are left empty/unknown. No MCU is present (passive LED board); tech.sao_version and sao_ports were never specified by the maker and are left null. Event/year (DC27, 2019) match between the Hackaday project's file date (2019-07-23) and the maker's own profile description.
last_modified_date: '2026-09-07'
---

The Peanut Butter SAO is a shitty add-on (SAO) by TwinkleTwinkie made for DEF CON 27 in 2019, built to settle a friendly argument about how to pronounce "GIF." The board renders the word "Gif" in the visual style of the Jif peanut butter logo, with a giraffe motif filling the background — a deliberate attempt to let both sides of the pronunciation debate feel vindicated.

The first revision used six white 1204 side-view LEDs pointed inward at the cut-out lettering, but suffered from heavy light bleed that spread well past the intended letterforms. TwinkleTwinkie corrected this in a second revision by moving to a 4-layer PCB, using the two inner copper layers as a light mask so only the "Gif" cutouts glow. The board runs off a single ~10-15 ohm series resistor and has no microcontroller, drawing power from its host badge.

## Make your own

Gerber files for the 4-layer revision are posted on the project's Hackaday.io page as a downloadable zip (`GIF_4L_2019-07-23-0017.zip`). No firmware is needed since the SAO is a passive LED board.
