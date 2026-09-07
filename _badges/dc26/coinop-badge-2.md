---
title: CoinOp Badge
id: dc26-coinop-badge-2
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Mike Szczys
  url: https://hackaday.io/mike
summary: A white pixel-art PCB badge shaped like the Galaga spaceship, driven by an ATmega48 with 18 red and 4 blue charlieplexed LEDs, two buttons and a CR2032 cell; 59 were hand-assembled in summer 2018 and packed with lanyards and batteries for DEF CON 26.
functions: 'Interactive LED animations, including a "laser fire" effect, with buttons cycling through display modes; a sleep mode (about 4.3 microamp) and a full off mode (about 0.1 microamp) to preserve the coin cell between uses.'
look:
  colors:
  - white
  shape: spaceship
  themes:
  - arcade
  - retro computer
  - pop culture
tech:
  mcu: ATmega48
  leds:
    count: 22
    type: discrete
    note: 18 red + 4 blue 0603 LEDs, charlieplexed
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '59'
  availability: unknown
  distribution: []
  where: Hand-assembled and packed with a lanyard and battery for distribution at DEF CON 26; sources do not say whether it was given away free or sold.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/szczys/coinop-badge/tree/master/board
  firmware_url: https://github.com/szczys/coinop-badge/tree/master/firmware
  eda_tool: KiCad
links:
- label: hackaday.io/project/159302-coinop-badge
  url: https://hackaday.io/project/159302-coinop-badge
  kind: hackaday
- label: github.com/szczys/coinop-badge
  url: https://github.com/szczys/coinop-badge
  kind: repo
- label: www.youtube.com/watch?v=faJSoZDbjUw
  url: https://www.youtube.com/watch?v=faJSoZDbjUw
  kind: video
images:
  - file: assets/images/badges/dc26/coinop-badge-2/25bfcd3599.jpg
    source: "https://hackaday.io/project/159302-coinop-badge"
    credit: "Mike Szczys"
    caption: "The finished CoinOp Badge, a white pixel-art PCB shaped like the Galaga spaceship"
  - file: assets/images/badges/dc26/coinop-badge-2/22d16e6d68.jpg
    source: "https://hackaday.io/project/159302-coinop-badge"
    credit: "Mike Szczys"
    caption: "Assembled CoinOp Badge PCBs packed with lanyard and battery"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159302-coinop-badge
  title: CoinOp Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/159302-coinop-badge
  title: CoinOp Badge
  accessed: '2026-09-07'
  note: Confirmed MCU (ATmega48), LED count/color split, buttons, CR2032 battery, sleep-current figures, quantity (59 assembled), and pulled gallery photos.
- kind: url
  url: https://github.com/szczys/coinop-badge
  title: szczys/coinop-badge
  accessed: '2026-09-07'
  note: Confirmed hardware (KiCad, /board) and firmware (/firmware) are both published in the repo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    Maker's own Hackaday.io project log and GitHub repo confirm the core hardware facts (chip, LED
    split, battery, button count, 59 units assembled). Neither source states a price or explicitly
    says the badges were given away free vs. sold; a commenter on the project log asked if extras
    would be listed on Tindie but the maker did not answer publicly. Left get_one.price,
    get_one.availability, and get_one.distribution unfilled rather than guess. No license file was
    found in the repo, so make_your_own.license is left empty. Event/year already matched DEF CON 26
    (2018) correctly; no correction needed.
last_modified_date: '2026-09-07'
---

The CoinOp Badge is Mike Szczys's homage to the Galaga arcade spaceship: a white, pixel-art-styled PCB cut into the ship's silhouette. An ATmega48 drives 18 red and 4 blue charlieplexed LEDs to produce animations, including a laser-fire effect, with two buttons letting the wearer cycle through modes. Careful power management — roughly 4.3 microamps asleep and 0.1 microamps fully off — was built in to stretch the life of the single CR2032 coin cell running the board.

Szczys documented the build through several revisions on Hackaday.io, reaching a v2.1 board before hand-assembling and packing 59 finished units, each with a lanyard and battery, ahead of DEF CON 26 in the summer of 2018. Both the KiCad hardware design and the AVR firmware are published in his `szczys/coinop-badge` GitHub repository, though no license file accompanies them and no price or free-vs-sold distribution detail is stated in either the project log or the repo.

## Make your own

Hardware files (KiCad schematic and PCB layout) live in the repo's `board` folder, and the ATmega48 firmware source is in `firmware`. The project depends on KiCad library files and MacroFab's EDALibraries for parts; assembly notes and a full build log are in the Hackaday.io project's logs.
