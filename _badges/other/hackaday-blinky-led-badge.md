---
title: Hackaday Blinky LED Badge
id: other-hackaday-blinky-led-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: Brian Benchoff
  url: https://github.com/bbenchoff
- name: Lutetium
  url: https://hackaday.io/lutetium
summary: A learn-to-solder wearable lapel pin with the Hackaday skull-and-wrenches (Jolly Wrencher) artwork, using two self-blinking slow-fade RGB LEDs, a slide switch and a CR1220 coin cell, derived from the earlier Tindie Blinky LED Badge circuit.
functions: 'Two self-blinking RGB LEDs slow-fade through colors for a "sparkly eyed" effect; a slide switch turns the badge on and off.'
look:
  colors: []
  shape: skull
  themes:
  - skull
  - learn to solder
  - kit
  - pin
tech:
  mcu: none
  leds:
    count: 2
    type: RGB
    note: Self-blinking/slow-fade RGB LEDs (no microcontroller; LEDs auto-cycle color internally)
  display: null
  connectivity: []
  battery: CR1220
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/bbenchoff/Hackaday-Pin
  firmware_url: null
  eda_tool: Eagle
links:
- label: github.com/bbenchoff/Hackaday-Pin
  url: https://github.com/bbenchoff/Hackaday-Pin
  kind: repo
- label: hackaday.io/project/161358-hackaday-blinky-led-badge
  url: https://hackaday.io/project/161358-hackaday-blinky-led-badge
  kind: hackaday
- label: hackaday.io/project/161358/instructions
  url: https://hackaday.io/project/161358/instructions
  kind: hackaday
- label: hackaday.io/project/26056-tindie-blinky-led-badge
  url: https://hackaday.io/project/26056-tindie-blinky-led-badge
  kind: hackaday
images:
- file: assets/images/badges/other/hackaday-blinky-led-badge/cbb9f7ac21.jpg
  source: "https://hackaday.io/project/161358-hackaday-blinky-led-badge"
  credit: "Brian Benchoff"
  caption: "Assembled Hackaday Blinky LED Badge lapel pin"
- file: assets/images/badges/other/hackaday-blinky-led-badge/9e173bde3e.jpg
  source: "https://hackaday.io/project/161358-hackaday-blinky-led-badge"
  credit: "Brian Benchoff"
  caption: "Hackaday Blinky LED Badge kit parts and assembly"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/bbenchoff/Hackaday-Pin
  title: bbenchoff/Hackaday-Pin - It's an LED blinky pin
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/161358-hackaday-blinky-led-badge
  title: Hackaday Blinky LED Badge | Hackaday.io
  accessed: '2026-09-07'
  note: Project overview - creators (Benchoff and Lutetium), creation date (09/19/2018), kit contents (slide switch, pin and clasp, battery holder, CR1220 battery), design derived from Tindie Blinky LED Badge; source of og:image photos.
- kind: url
  url: https://hackaday.io/project/161358/instructions
  title: Instructions | Hackaday Blinky LED Badge | Hackaday.io
  accessed: '2026-09-07'
  note: Assembly/soldering instructions; no event, price, or quantity mentioned.
- kind: url
  url: https://hackaday.io/project/26056-tindie-blinky-led-badge
  title: Tindie Blinky LED Badge | Hackaday.io
  accessed: '2026-09-07'
  note: Background on the earlier circuit this badge derives from - made by Tindie/Benchoff/Jasmine Brackett/Brandon Rexius for DEF CON 25 (2017), roughly 2,000 units produced across iterations.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No source ties this specific badge to a named conference or a distribution price/quantity - it reads as a general-purpose learn-to-solder kit sold/given out by Hackaday, created 09/19/2018, rather than a con-specific badge, so event was left as "other". Its circuit is a rebadged, Hackaday-themed version of the 2017 Tindie Blinky LED Badge (made for DEF CON 25). Hardware design files (Eagle schematic, board, BOM, Gerbers) are published in the linked GitHub repo; no firmware exists since the LEDs are self-blinking with no MCU.
last_modified_date: '2026-09-07'
---

The Hackaday Blinky LED Badge is a learn-to-solder kit in the shape of Hackaday's Jolly Wrencher skull-and-wrenches logo, published by Brian Benchoff (with contributor "Lutetium") on Hackaday.io on September 19, 2018. It reuses the circuit from the 2017 Tindie Blinky LED Badge - itself rushed together by Benchoff, Jasmine Brackett, and Brandon Rexius in about two weeks for DEF CON 25 - but redraws the board artwork around Hackaday's own mascot instead of Tindie's head logo.

Assembly is a mix of through-hole and surface-mount soldering: a slide switch, a pin-and-clasp fastener, a CR1220 coin-cell holder, and two RGB LEDs that self-blink and slow-fade through colors on their own, with no microcontroller driving them. Finished, it wears as a lapel pin with glowing "sparkly eyes." No source found ties this particular version to a specific conference, and no price, production quantity, or sales channel is documented - it reads as an open, general-audience soldering-practice kit rather than a con badge tied to one event or year of distribution.

## Make your own

Full hardware design files - Eagle schematic (HackadayPin.sch), board layout (HackadayPin.brd), bill of materials (HackadayPinBOM.csv), and Gerbers (HackadayPin_Gerbers.zip) - are published in Benchoff's GitHub repo at github.com/bbenchoff/Hackaday-Pin. No firmware is needed or provided, since the blinking effect comes from self-cycling RGB LEDs rather than a programmed microcontroller.
