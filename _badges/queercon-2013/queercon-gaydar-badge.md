---
title: Queercon "GayDar" Badge
id: queercon-2013-queercon-gaydar-badge
layout: badge
parent: Queercon 10 (2013)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: queercon-2013
year: 2013
makers:
- name: Queercon
- name: George Louthan
  url: https://github.com/duplico
  role: firmware
- name: Evan G Mackay
  role: hardware
summary: The Queercon 10 electronic badge for DEF CON 21 (2013), nicknamed "GayDar" by attendees for its radio-based neighbor-tracking feature that senses nearby badges.
functions: Rainbow-circle LED animation, a heartbeat pulse mode, radio-based neighbor-tracking that detects other nearby badges (the feature behind the "GayDar" nickname), and an audio-reactive party mode that drives the LEDs to ambient sound.
look:
  colors: []
  shape: null
  themes:
  - radio
tech:
  mcu: ATmega328 (JeeNode-based)
  leds:
    type: TLC5940-driven
    note: A single TI TLC5940 16-channel constant-current LED driver chip controls the badge's LEDs; exact LED count not stated in the sources found.
  display: none
  connectivity:
  - sub-ghz
  inputs:
  - microphone
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 105 (per BADGES_IN_SYSTEM constant in firmware)
  availability: free
  distribution:
  - free_drop
  where: Distributed to Queercon attendees at the DEF CON 21 (2013) Queercon party; exact distribution method not confirmed beyond that it was event-given, not sold.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Queercon/QC10-Badge
  firmware_url: https://github.com/Queercon/QC10-Badge
  eda_tool: null
  license: 'Hardware: CC BY 3.0. Software: MIT License, with the bundled TLC5940 driver library under the Simplified BSD License.'
  notes: A parallel copy of the same badge's firmware, with a more descriptive README, is maintained by co-creator George Louthan at https://github.com/duplico/qc10 ; that repo notes the design was "lightly adapted for Queercon 13" into a top-hat form factor.
links:
- label: hackaday.com/tag/queercon-badge
  url: https://hackaday.com/tag/queercon-badge/
  kind: article
- label: Queercon/QC10-Badge (GitHub)
  url: https://github.com/Queercon/QC10-Badge
  kind: repo
- label: duplico/qc10 (GitHub)
  url: https://github.com/duplico/qc10
  kind: repo
- label: 'DEF CON Forums: Queercon Badges (announcing the Queercon 11 badge, referencing "GayDar")'
  url: https://forum.defcon.org/node/14911
  kind: article
- label: blinkylights.ninja/blinky-lights/queercon-10-2013
  url: https://blinkylights.ninja/blinky-lights/queercon-10-2013/
  kind: website
images: []
contact: {}
notes:
- 'Original sweep import: "Queercon''s debut electronic badge in 2012, the first year Queercon produced its own hardware badge for the DEF CON 20 party." That was unconfirmed and turned out to be wrong on both the year and the "debut" claim — see research.notes.'
- Electronic badge for Queercon's 10th anniversary at DEF CON 21, built on an Atmel ATmega with a TI PWM LED driver, HopeRF 433MHz radio, and a Maxim mic amp, featuring dual rainbow LED rings that tracked a 'score' and nearby-badge detection. Found by the event-year sweep, task dc21-all. Confirmed against the maker's own GitHub repository, which matches every element of this description.
status: released
sources:
- kind: url
  url: https://hackaday.com/tag/queercon-badge/
  title: Queercon "GayDar" Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc20-all); event read as ''queercon-2012''.'
- kind: url
  url: https://forum.defcon.org/node/14911
  title: Queercon Badges - DEF CON Forums
  accessed: '2026-09-10'
  note: Official Queercon forum post (dated April 24, 2014) announcing the Queercon 11 badge, opening "After our 'GayDar' badge's overwhelming debut last year..." — this dates GayDar to Queercon 10, the year before Queercon 11. Confirms the nickname is genuine and pins the year.
- kind: url
  url: https://github.com/Queercon/QC10-Badge
  title: Queercon/QC10-Badge
  accessed: '2026-09-10'
  note: Official hardware/firmware repo. readme.txt header reads "Queercon 10 (2013)"; confirms hardware credit (Evan G Mackay, CC BY 3.0, JeeNode-based) and software credit (George Louthan et al., MIT/BSD); hardware/ folder contains a BOM and schematic PDF. Uses one TLC5940 LED driver chip; pin defines match an ATmega-family MCU consistent with the JeeNode (ATmega328) base. Repo itself does not use the name "GayDar."
- kind: url
  url: https://github.com/duplico/qc10
  title: duplico/qc10
  accessed: '2026-09-10'
  note: 'Co-creator George Louthan''s copy of the same Queercon 10 firmware with a fuller description: "Rainbow circle, heartbeat, radio neighbor-tracking, and audio reactive party mode. Also lightly adapted for Queercon 13 as a top hat." Supplies the functions list and the Queercon 13 reuse note.'
- kind: url
  url: https://blinkylights.ninja/blinky-lights/queercon-10-2013/
  title: Queercon 10 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc21-all); event read as ''queercon-2013''.'
- kind: url
  url: https://raw.githubusercontent.com/Queercon/QC10-Badge/master/main.c
  title: QC10-Badge main.c
  accessed: '2026-09-10'
  note: Source of the BADGES_IN_SYSTEM=105 quantity, RFM12B/JeeLib radio config, and ADC-based mic amplitude sampling.
- kind: url
  url: https://raw.githubusercontent.com/Queercon/QC10-Badge/master/readme.txt
  title: QC10-Badge readme.txt
  accessed: '2026-09-10'
  note: Confirms authorship (Evan G Mackay hardware, George Louthan firmware) and licensing (CC BY 3.0 hardware; BSD-2-Clause TLC5940 library; MIT for the rest).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The sweep''s year (2012) was wrong. Working backward from the maker''s own forum post: Queercon''s official DEF CON forum thread announcing the Queercon 11 badge (posted 2014-04-24) says it follows the "GayDar" badge''s "overwhelming debut last year" — i.e. Queercon 10, which the badge''s own repo readme dates to "Queercon 10 (2013)" (DEF CON 21). Corrected event/year to queercon-2013 accordingly. No source found actually uses "GayDar" as the badge''s formal name in a caption or product listing — it appears once, in quotes, in the Queercon forum post, which is the strongest evidence available that it was the badge''s real nickname (referencing its radio-based neighbor-detection feature) rather than an archive-sweep misread; title kept as-is on that basis. Could not find price, quantity made, a maker-labeled photo, or the exact chip variant (JeeNode boards used several ATmega328 variants) in the time budgeted — left blank rather than guessed. No image of the physical badge was found
    via search in budget; images field left empty. Merged with duplicate entry ''Queercon 10 Badge'' (queercon-2013-queercon-10-badge).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/queercon-2012/queercon-gaydar-badge/
- /badges/queercon-2013/queercon-10-badge/
---

The Queercon 10 electronic badge, given out to attendees at the DEF CON 21 (2013) Queercon party, became known among attendees as the "GayDar" badge — a nod to its radio-based feature that let a badge sense and register other Queercon badges nearby. Alongside that neighbor-tracking, it ran a rainbow-circle LED animation, a heartbeat-style pulse mode, and an audio-reactive "party mode" that drove its LEDs to ambient sound.

The hardware was built around a JeeNode-derived ATmega328 board with a single TI TLC5940 16-channel LED driver chip, credited to Evan G Mackay (hardware) and George Louthan (firmware), with both released as open source (hardware under CC BY 3.0, firmware mostly MIT-licensed). The badge was recognized enough within Queercon's own circle that the following year's badge announcement referenced its "overwhelming debut" by name, and its design was later adapted into a top-hat form factor for Queercon 13.

## Make your own

Both the hardware (schematics PDF and BOM) and firmware are published on GitHub. The official repository is [Queercon/QC10-Badge](https://github.com/Queercon/QC10-Badge); a parallel copy with a fuller project description, maintained by co-creator George Louthan, is at [duplico/qc10](https://github.com/duplico/qc10). No CAD/EDA source files (only a schematic PDF) were found, so board files would need to be redrawn from the BOM and schematic to fabricate a new one.

## Notes merged from the duplicate entry "Queercon 10 Badge"

The Queercon 10 badge was given to attendees of Queercon's 10th-anniversary party at DEF CON 21 in Las Vegas in 2013. It is a JeeNode-compatible board (an ATmega328-class AVR MCU paired with a HopeRF sub-GHz radio through the JeeLib stack) designed by Evan G Mackay, with firmware primarily by George Louthan. Two six-LED "rainbow" rings, one inside the other, are driven through a TI TLC5940 constant-current LED driver and run a set of ambient and celebratory ("bling") animations.

The badge's radio lets units detect each other nearby, incrementing a running badge count and unlocking an escalating "uber" animation tier the more other badges it has seen — an early instance of the badge-to-badge social/scoring mechanic that later Queercon badges became known for. An onboard microphone amplifier feeds the ADC so the badge can react to ambient sound or music volume. Firmware constants put the fleet size at 105 badges.

## Make your own

Both hardware and firmware are published on GitHub at [Queercon/QC10-Badge](https://github.com/Queercon/QC10-Badge). The hardware (schematics and BOM, under `hardware/`) is released under CC BY 3.0; the firmware is a mix of the BSD-2-Clause-licensed TLC5940 driver library and MIT-licensed code for everything else, built as an Arduino/AVR-C project (`qc10badge.ino`, `main.c`, `animations.c`).
