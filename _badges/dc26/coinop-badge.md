---
title: CoinOp Badge
id: dc26-coinop-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Mike Szczys
  url: https://hackaday.io/szczys
summary: A Galaga-ship-shaped PCB badge by Mike Szczys with an ATmega48 driving 18 red and blue charlieplexed LEDs, two buttons, powered by a CR2032 coin cell; about 59 boards were hand-assembled and handed out at DEF CON 26 in 2018.
functions: Two buttons fire "lasers," cycle through LED visualizations, and put the badge to sleep. The ATmega48 charlieplexes the LEDs at a 1/6 duty cycle, 1kHz scan rate to keep power draw low; firmware sleep current is about 4.3 microamps (0.1 microamps when switched off).
look:
  colors:
  - red
  - blue
  shape: spaceship
  themes:
  - arcade
  - retro computer
tech:
  mcu: ATmega48
  leds:
    count: 22
    type: charlieplexed
    note: 18 red and either 3 or 4 blue 0603 diffuse LEDs (sources disagree on the exact blue count — see notes).
  display: none
  connectivity: []
  inputs:
  - buttons
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '59'
  availability: sold_out
  availability_note: 'Checked 2026-09-07: hand-made batch of 59 was given out at DEF CON 26 (2018); no ongoing storefront found.'
  distribution:
  - free_drop
  where: Handed out by the maker at DEF CON 26 in Las Vegas, 2018.
make_your_own:
  open_source: true
  hardware_url: https://github.com/szczys/coinop-badge
  firmware_url: https://github.com/szczys/coinop-badge
  gerbers_url: null
  bom_url: null
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: Hardware (KiCad board files) and firmware are both in the same GitHub repo, in board/ and firmware/ directories.
links:
- label: github.com/szczys/coinop-badge
  url: https://github.com/szczys/coinop-badge
  kind: repo
- label: hackaday.io/project/159302-coinop-badge
  url: https://hackaday.io/project/159302-coinop-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260216122653/https://hackaday.io/project/159302-coinop-badge
- label: hackaday.com/2018/09/05/all-the-badges-of-def-con-26-vol-4
  url: https://hackaday.com/2018/09/05/all-the-badges-of-def-con-26-vol-4/
  kind: article
  archived: https://web.archive.org/web/20260310212057/https://hackaday.com/2018/09/05/all-the-badges-of-def-con-26-vol-4/
- label: www.youtube.com/watch?v=faJSoZDbjUw
  url: https://www.youtube.com/watch?v=faJSoZDbjUw
  kind: video
  archived: https://web.archive.org/web/20260907115420/https://www.youtube.com/watch?v=faJSoZDbjUw
images:
- file: assets/images/badges/dc26/coinop-badge/25bfcd3599.jpg
  source: https://hackaday.io/project/159302-coinop-badge
  credit: Mike Szczys
  caption: CoinOp Badge, a Galaga-ship-shaped PCB badge with charlieplexed LEDs
  archived: https://web.archive.org/web/20260216122653/https://hackaday.io/project/159302-coinop-badge
- file: assets/images/badges/dc26/coinop-badge/25bfcd3599.jpg
  source: https://hackaday.io/project/159302-coinop-badge
  credit: Mike Szczys
  caption: The finished CoinOp Badge, a white pixel-art PCB shaped like the Galaga spaceship
  archived: https://web.archive.org/web/20260216122653/https://hackaday.io/project/159302-coinop-badge
- file: assets/images/badges/dc26/coinop-badge/22d16e6d68.jpg
  source: https://hackaday.io/project/159302-coinop-badge
  credit: Mike Szczys
  caption: Assembled CoinOp Badge PCBs packed with lanyard and battery
  archived: https://web.archive.org/web/20260216122653/https://hackaday.io/project/159302-coinop-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/szczys/coinop-badge
  title: szczys/coinop-badge — Hardware badge homage to my favorite coinop video game
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/159302-coinop-badge
  title: CoinOp Badge project page (Hackaday.io)
  accessed: '2026-09-07'
  note: Confirmed maker, event context, ATmega48/LED/button/battery specs, 59 units hand-assembled, and provided the badge photo used here. States 4 blue LEDs.
  archived: https://web.archive.org/web/20260216122653/https://hackaday.io/project/159302-coinop-badge
- kind: url
  url: https://hackaday.com/2018/09/05/all-the-badges-of-def-con-26-vol-4/
  title: 'All The Badges Of DEF CON 26: Vol. 4 (Hackaday)'
  accessed: '2026-09-07'
  note: Independent confirmation of DEF CON 26 (2018), ATmega48, CR2032, two buttons, and 59 hand-built boards. States 3 blue LEDs (not 4).
  archived: https://web.archive.org/web/20260310212057/https://hackaday.com/2018/09/05/all-the-badges-of-def-con-26-vol-4/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Blue LED count disagrees between sources — Hackaday.io project page says 4 blue LEDs (matching the earlier sheet import), the Hackaday.com DEF CON 26 roundup article says 3 blue LEDs. Left tech.leds.count at 22 total (18 red + 4 blue, the maker's own project page) and noted the discrepancy rather than guess which is correct. No Gerber-specific share link or BOM found; hardware/firmware are both in the GitHub repo. No evidence of any commercial sale — distributed free at DEF CON 26. Merged with duplicate entry 'CoinOp Badge' (dc26-coinop-badge-2).
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/coinop-badge.glb
  method: kicad
  source_file: board/coinop-badge.kicad_pcb
  generated: '2026-09-07'
  bytes: 205788
redirect_from:
- /badges/dc26/coinop-badge-2/
---

Mike Szczys built the CoinOp Badge as a personal tribute to the arcade game Galaga, shaping the PCB itself like the game's spaceship. An ATmega48 microcontroller charlieplexes 18 red and a handful of blue 0603 LEDs (sources differ on whether it's 3 or 4) across the board, scanning them at a 1kHz, 1/6 duty cycle to keep current draw low. Two momentary push buttons let the wearer fire "lasers," cycle through LED animation modes, and put the badge to sleep; a CR2032 coin cell powers the whole thing, with the firmware dropping to roughly 4.3 microamps in sleep and 0.1 microamps when switched fully off.

Szczys hand-assembled about 59 of these boards in his basement and handed them out at DEF CON 26 in Las Vegas in 2018. The badge was covered in Hackaday's "All The Badges Of DEF CON 26" roundup, and Szczys documented the build (including a time-lapse assembly video) on its Hackaday.io project page.

## Make your own

Both the KiCad hardware design and the AVR firmware are published together in the [szczys/coinop-badge GitHub repository](https://github.com/szczys/coinop-badge), split into `board/` and `firmware/` directories. The README notes the KiCad library dependencies (the standard KiCad library plus MacroFab's EDALibraries footprints and schematics) needed to open the board files; no separate Gerber share link or bill of materials was found.

## Notes merged from the duplicate entry "CoinOp Badge"

The CoinOp Badge is Mike Szczys's homage to the Galaga arcade spaceship: a white, pixel-art-styled PCB cut into the ship's silhouette. An ATmega48 drives 18 red and 4 blue charlieplexed LEDs to produce animations, including a laser-fire effect, with two buttons letting the wearer cycle through modes. Careful power management — roughly 4.3 microamps asleep and 0.1 microamps fully off — was built in to stretch the life of the single CR2032 coin cell running the board.

Szczys documented the build through several revisions on Hackaday.io, reaching a v2.1 board before hand-assembling and packing 59 finished units, each with a lanyard and battery, ahead of DEF CON 26 in the summer of 2018. Both the KiCad hardware design and the AVR firmware are published in his `szczys/coinop-badge` GitHub repository, though no license file accompanies them and no price or free-vs-sold distribution detail is stated in either the project log or the repo.

## Make your own

Hardware files (KiCad schematic and PCB layout) live in the repo's `board` folder, and the ATmega48 firmware source is in `firmware`. The project depends on KiCad library files and MacroFab's EDALibraries for parts; assembly notes and a full build log are in the Hackaday.io project's logs.
