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
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Blue LED count disagrees between sources — Hackaday.io project page says 4 blue LEDs (matching the earlier sheet import), the Hackaday.com DEF CON 26 roundup article says 3 blue LEDs. Left tech.leds.count at 22 total (18 red + 4 blue, the maker's own project page) and noted the discrepancy rather than guess which is correct. No Gerber-specific share link or BOM found; hardware/firmware are both in the GitHub repo. No evidence of any commercial sale — distributed free at DEF CON 26.
last_modified_date: '2026-09-07'
---

Mike Szczys built the CoinOp Badge as a personal tribute to the arcade game Galaga, shaping the PCB itself like the game's spaceship. An ATmega48 microcontroller charlieplexes 18 red and a handful of blue 0603 LEDs (sources differ on whether it's 3 or 4) across the board, scanning them at a 1kHz, 1/6 duty cycle to keep current draw low. Two momentary push buttons let the wearer fire "lasers," cycle through LED animation modes, and put the badge to sleep; a CR2032 coin cell powers the whole thing, with the firmware dropping to roughly 4.3 microamps in sleep and 0.1 microamps when switched fully off.

Szczys hand-assembled about 59 of these boards in his basement and handed them out at DEF CON 26 in Las Vegas in 2018. The badge was covered in Hackaday's "All The Badges Of DEF CON 26" roundup, and Szczys documented the build (including a time-lapse assembly video) on its Hackaday.io project page.

## Make your own

Both the KiCad hardware design and the AVR firmware are published together in the [szczys/coinop-badge GitHub repository](https://github.com/szczys/coinop-badge), split into `board/` and `firmware/` directories. The README notes the KiCad library dependencies (the standard KiCad library plus MacroFab's EDALibraries footprints and schematics) needed to open the board files; no separate Gerber share link or bill of materials was found.
