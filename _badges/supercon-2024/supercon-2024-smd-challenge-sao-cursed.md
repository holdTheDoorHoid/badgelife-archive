---
title: Supercon 2024 SMD Challenge SAO (Cursed)
id: supercon-2024-supercon-2024-smd-challenge-sao-cursed
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Tom Nardi
  url: https://hackaday.io/hacker/1022-tom-nardi
summary: An SAO version of the Supercon SMD soldering challenge board (ATtiny85 plus LEDs, powered from the SAO header instead of a CR2032) made for Supercon 2024, but the ATtiny85 power and ground pins were inverted, so the 150+ boards fabricated were pulled from the competition and later handed out at events as a curiosity.
functions: Intended fading/chasing LED patterns driven by the ATtiny85, like the original SMD soldering-challenge board it was adapted from.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - puzzle
tech:
  mcu: ATtiny85
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 150+
  availability: free
  distribution:
  - free_drop
  where: Handed out by Tom Nardi at various events after Supercon 2024; not sold.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
  url: https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
  kind: hackaday
  archived: https://web.archive.org/web/20251111231018/https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
images:
- file: assets/images/badges/supercon-2024/supercon-2024-smd-challenge-sao-cursed/3032e0c6c9.png
  source: https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
  credit: Tom Nardi
  caption: The Supercon 2024 SMD Challenge SAO board
  archived: https://web.archive.org/web/20251111231018/https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
- file: assets/images/badges/supercon-2024/supercon-2024-smd-challenge-sao-cursed/1adb3f2094.jpg
  source: https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
  credit: Tom Nardi
  caption: Close-up of the SAO board showing the ATtiny85 and LEDs
  archived: https://web.archive.org/web/20251111231018/https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
  title: Supercon 2024 SMD Challenge SAO (Cursed)
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20251111231018/https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
- kind: url
  url: https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
  title: Supercon 2024 SMD Challenge SAO (Cursed)
  accessed: '2026-09-07'
  note: Confirmed maker (Tom Nardi), event/year, ATtiny85 MCU, SAO-header power in place of CR2032, the inverted power/ground pin defect, ~150+ boards fabricated and pulled from competition, and free distribution at later events.
  archived: https://web.archive.org/web/20251111231018/https://hackaday.io/project/198225-supercon-2024-smd-challenge-sao-cursed
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Only source available is the maker's own Hackaday.io project page, which confirms the core story but does not give an LED count/type, exact quantity beyond "150+", or any published design files. Web search was unavailable this session (budget exhausted), so press coverage or forum discussion of the "cursed" batch could not be checked.
last_modified_date: '2026-09-07'
---

Tom Nardi built this SAO as a variant of the SMD soldering-challenge board used at Supercon, swapping the challenge board's usual CR2032 coin cell for power drawn straight off the SAO header. The board carries an ATtiny85 driving a set of LEDs meant to fade and chase once soldered up and plugged into a host badge.

The design shipped with a wiring error: the ATtiny85's power and ground pins were swapped, so any board built as designed would overheat the chip instead of running the light show. Hackaday caught the mistake before the batch could be used in the soldering competition it was made for, and the roughly 150-plus boards that had already been fabricated were pulled. Nardi kept a stock of the boards and has since handed them out at other events as a novelty - a "cursed" SAO that can't actually be built correctly, at least not without correcting the pinout.

No hardware or firmware files, LED type/count, or a formal price and distribution channel are documented on the project page; it exists strictly as a giveaway curiosity rather than a released product.
