---
title: Golden Turd SAO
id: dc30-golden-turd-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: The Hebrew
summary: A gold-plated novelty SAO shaped like a pile of poop, sold as "The Ultimate S#!tty Add-on."
functions: 'A button cycles through 12 LED display modes, including Twinkle, Chase, and Marquee patterns, plus fixed brightness levels of 100%, 75%, 50%, 25%, or off.'
look:
  colors:
  - gold
  shape: null
  themes:
  - meme
  - jewelry
tech:
  mcu: ATtiny85
  leds:
    count: 10
    type: charlieplexed
    note: Driven via PWM through charlieplexing, using only four MCU pins for 10 LEDs.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: $30
  price_usd: 30.0
  quantity: ''
  availability: sold_out
  availability_note: 'Only 2 left as of checking the Tindie listing on 2026-09-06; sheet noted "Only 6 left as of 30Jun2022."'
  distribution:
  - purchase
  where: Tindie storefront (thehebrew)
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/thehebrew/golden-turd-sao
  url: https://www.tindie.com/products/thehebrew/golden-turd-sao/
  kind: store
images:
- file: assets/images/badges/dc30/golden-turd-sao/d4fa0a1cad.jpg
  source: "https://www.tindie.com/products/thehebrew/golden-turd-sao/"
  credit: "thehebrew"
  caption: "Golden Turd SAO, gold ENIG plated PCB"
contact: {}
notes:
- Only 6 left as of 30Jun2022
status: released
sources:
- kind: sheet
  event: dc30
  row: 44
  updated: '2022-06-30'
- kind: url
  url: https://www.tindie.com/products/thehebrew/golden-turd-sao/
  title: "Golden Turd SAO by thehebrew - Tindie"
  accessed: '2026-09-06'
  note: Confirmed maker, price, MCU, LED count/driving method, button-cycled display modes, ENIG gold finish, and stock level; source of the saved product photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Only source found was the maker''s own Tindie listing; no Hackaday.io project, GitHub repo, or press coverage located. Design files are not published there, so make_your_own is left null rather than guessed as closed/open. Exact quantity made is not stated anywhere. The Hebrew also has a stub entry for DEF CON 31 (dc31-the-hebrew-listed-for-def-con-31-no-details) that a future pass could try to fill in from this same Tindie account.'
last_modified_date: '2026-09-06'
---

The Golden Turd SAO is a novelty Shitty Add-On sold by maker "thehebrew" (based in Sterling, Virginia) for DEF CON 30 in 2022, billed as "The Ultimate S#!tty Add-on!" Shaped and plated to resemble a small pile of gold, the board uses ENIG (Electroless Nickel Immersion Gold) plating for an actual gold finish rather than paint or ink.

Under the hood it runs on an ATtiny85 microcontroller that charlieplexes 10 LEDs, driving them through PWM using only four of the chip's pins. A single button lets the wearer cycle through 12 display modes, ranging from animated patterns like Twinkle, Chase, and Marquee to fixed brightness steps (100%, 75%, 50%, 25%) and an off setting. It ships fully assembled with a pre-soldered 2x3 SAO header and sold for $30, with the community sheet noting only 6 remained by June 30, 2022 and the Tindie listing down to 2 units when checked.

No hardware or firmware files were found published for this design, so it appears to be sold assembled-only rather than open-sourced.
