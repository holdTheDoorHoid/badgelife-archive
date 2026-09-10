---
title: HITB Minibadge
id: saintcon-2017-hitbutt-minibadge
layout: badge
parent: Saintcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2017
year: 2017
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: A SAINTCON-format trading minibadge with two touch pads that drive two APA102 RGB LEDs, themed around "Hak-In-The-Box".
functions: 'Touching either of two exposed capacitive pads changes the color shown on two onboard RGB LEDs (red/green/blue combinations depending on which pad, or both, are touched).'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - minimalist
tech:
  mcu: ATtiny45
  leds:
    count: 2
    type: APA102
    note: 5050 package, bit-banged over two GPIO pins
  display: none
  connectivity: []
  inputs:
  - touch
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/compukidmike/Saintcon2017/tree/master/HITBUTT_Minibadge
  firmware_url: https://github.com/compukidmike/Saintcon2017/blob/master/HITBUTT_Minibadge/HITB_Test.ino
  eda_tool: Eagle
links:
- label: github.com/compukidmike/Saintcon2017
  url: https://github.com/compukidmike/Saintcon2017
  kind: repo
- label: HITBUTT_Minibadge design files
  url: https://github.com/compukidmike/Saintcon2017/tree/master/HITBUTT_Minibadge
  kind: repo
images: []
contact: {}
notes:
- Minibadge project (HITBUTT_Minibadge folder) by compukidmike for SAINTCON 2017; details limited on repo listing. Found by the event-year sweep, task saintcon-2017.
- 'The repo folder is named "HITBUTT_Minibadge" but the maker''s own README titles the project "HITB Minibadge 2017" and describes it as "the design files for the Hak-In-The-Box minibadge for Saintcon 2017" — title corrected to match the README.'
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2017
  title: HITBUTT Minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2017); event read as ''saintcon-2017''.'
- kind: url
  url: https://github.com/compukidmike/Saintcon2017/tree/master/HITBUTT_Minibadge
  title: HITBUTT_Minibadge folder (Saintcon2017 repo)
  accessed: '2026-09-10'
  note: Folder listing (Base-Rev0 Eagle schematic/board/gerbers, HITB_Test.ino, README.md).
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2017/master/HITBUTT_Minibadge/README.md
  title: HITB Minibadge 2017 README
  accessed: '2026-09-10'
  note: 'Maker''s own description: "the design files for the Hak-In-The-Box minibadge for Saintcon 2017"; libraries used (APA102 by Pololu, ADCTouch by martin2250).'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2017/master/HITBUTT_Minibadge/HITB_Test.ino
  title: HITB_Test.ino firmware
  accessed: '2026-09-10'
  note: Confirms 2 APA102 LEDs and 2 ADCTouch pads; touching either pad switches the LED color (red/green/blue logic).
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2017/master/HITBUTT_Minibadge/Base-Rev0.sch
  title: Base-Rev0.sch (Eagle schematic)
  accessed: '2026-09-10'
  note: 'Part list confirms MCU is an ATtiny45 (SparkFun-Retired library, TINY45-20-SMT), two APA102 5050 LEDs, two TP06R touch pads, and an AVR SPI programming header; built on the shared "MiniBadge" BADGE64 base library.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed as a real, built minibadge via the maker''s own GitHub repo (schematic, board, gerbers, and working firmware are all present), so this is not just a search-snippet rumor. No press coverage, storefront, price, quantity, or photo of the assembled badge was found anywhere online — likely a small trade-only run typical of SAINTCON minibadges, but that could not be confirmed. Confidence held at medium rather than high because availability/quantity/pricing and an image remain unknown.'
last_modified_date: '2026-09-10'
---

The HITB Minibadge is a SAINTCON-format trading minibadge that compukidmike built for SAINTCON 2017, on the community's shared "MiniBadge" base board. Its own README describes it plainly as "the design files for the Hak-In-The-Box minibadge for Saintcon 2017," which is likely the source of the folder name "HITBUTT_Minibadge" in the repo (the two appear to be the same project, just named a bit differently in the folder vs. the README).

Electrically it's a simple, minibadge-scale interactive board: an ATtiny45 microcontroller reads two exposed capacitive touch pads (via the ADCTouch library) and drives two APA102 RGB LEDs (via Pololu's APA102 library) in response. In the maker's own test firmware, touching one pad turns the LEDs red, touching the other turns them blue, touching neither leaves them green, and touching both turns off green and shows the combined color — a straightforward touch-reactive light toy in minibadge form.

No pricing, production quantity, distribution details, or photos of the finished badge turned up in any search; the only documentation found is the maker's own repository (schematic, board, Gerbers, and firmware), which is enough to confirm the badge was designed and built, but not enough to say how it was distributed at SAINTCON 2017.

## Make your own

The Eagle schematic (`Base-Rev0.sch`), board (`Base-Rev0.brd`), and Gerbers (`Base-Rev0-Gerbers.zip`) are in the `HITBUTT_Minibadge` folder of compukidmike's `Saintcon2017` repo, alongside `HITB_Test.ino`, the Arduino firmware. Building one requires the APA102 library (Pololu) and ADCTouch library (martin2250), both installable from the Arduino Library Manager, and an AVR ISP programmer (there's a dedicated 3x2 SPI programming header on the board).

