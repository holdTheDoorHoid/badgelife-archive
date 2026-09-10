---
title: Queercon 16 badge
id: queercon-2019-queercon-16-badge
layout: badge
parent: Queercon 16
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: queercon-2019
year: 2019
makers:
- name: duplico
  url: https://github.com/duplico
summary: 'The official electronic badge for Queercon 16 (2019, held alongside DEF CON 27 in Las Vegas), built around a "cyber world overlaid on Vegas" theme: badges (Q badges) run an on-badge "Agent" that takes on missions from "Handlers," using Bluetooth LE proximity to find other badges and small companion "C badges" (access-pass fobs) that unlock extra content.'
functions: BLE-based proximity/"radar" detection of nearby Q badges and Handlers; an Agent/mission system with a Queer Coin virtual currency; badge-to-badge pairing over a serial link; a menu-driven UI with a color picker, text entry, file/animation management, and configurable RGB LED "tail" light animations. Small companion C badges plug in over a wired link to grant one-shot capabilities to a paired Q badge.
look:
  colors:
  - blue
  shape: null
  themes:
  - cyberpunk
  - security
  - puzzle
  form_factor: pcb badge
tech:
  mcu: CC2640R2F
  leds:
    count: 6
    type: RGB
    note: Driven by a Holtek HT16D35B LED controller over I2C; used for animated "tail" light patterns plus a sidelight.
  display: 2.9" e-paper (128x296)
  connectivity:
  - ble
  inputs:
  - buttons
  battery: LiPo (voltage sensed on an ADC pin); also has a light sensor
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to Queercon 16 attendees at DEF CON 27, Las Vegas, August 2019.
make_your_own:
  open_source: true
  hardware_url: https://github.com/duplico/qc16_badge
  firmware_url: https://github.com/duplico/qc16_badge
  eda_tool: KiCad
links:
- label: github.com/duplico/qc16_badge
  url: https://github.com/duplico/qc16_badge
  kind: repo
- label: hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard
  url: https://hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard/
  kind: article
images:
- file: assets/images/badges/queercon-2019/queercon-16-badge/abef92c545.jpg
  source: https://github.com/duplico/qc16_badge
  credit: duplico
  caption: Prototype Queercon 16 companion C badge PCB, back side
- file: assets/images/badges/queercon-2019/queercon-16-badge/2ad9c98545.jpg
  source: https://github.com/duplico/qc16_badge
  credit: duplico
  caption: Prototype Queercon 16 companion C badge PCB, front side with silkscreen reading 'QUEERCON 16 2019 C BADGE R0'
- file: assets/images/badges/queercon-2019/queercon-16-badge/4b97a2adfd.jpg
  source: https://hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard/
  credit: Hackaday / Queercon badge team
  caption: Queercon 16 Q Badge with membrane keyboard and eInk display
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- Primary Queercon 16 (DC27) badge with custom membrane keyboard, 2.9in eInk display, BLE, acting as ARG control panel; not in archive. Found by the event-year sweep, task dc27-badges.
- Sweep called it "Primary Queercon 16 (DC27) badge"; Hackaday's own coverage treats it as a distinct "Q Badge"/ARG control panel alongside the separately catalogued main Queercon 16 badge (queercon-2019-queercon-16-badge, credited to duplico) — kept the sweep's "Q Badge" title since that matches Hackaday's framing.
status: released
sources:
- kind: url
  url: https://github.com/duplico/qc16_badge
  title: Queercon 16 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''queercon-2019''.'
- kind: url
  url: https://github.com/duplico/qc16_badge/blob/master/ccs_workspace/qbadge/queercon_drivers/epd_phy.h
  title: epd_phy.h (Queercon 16 badge repo)
  accessed: '2026-09-07'
  note: Confirms the 128x296 e-paper display and its driver.
- kind: url
  url: https://github.com/duplico/qc16_badge/blob/master/ccs_workspace/qbadge/queercon_drivers/ht16d35b.h
  title: ht16d35b.h (Queercon 16 badge repo)
  accessed: '2026-09-07'
  note: Confirms the HT16D35B RGB LED controller and 6-color tail animation struct.
- kind: url
  url: https://github.com/duplico/qc16_badge/blob/master/docs/notes/peripherals.txt
  title: peripherals.txt (Queercon 16 badge repo)
  accessed: '2026-09-07'
  note: 'Peripheral pinout: light sensor, battery sensor ADC, B2B serial connector, SPI flash, matrix keypad, LED driver, e-paper display.'
- kind: url
  url: https://github.com/duplico/qc16_badge/blob/master/docs/notes/notes_call_20190530.txt
  title: notes_call_20190530.txt (Queercon 16 badge repo)
  accessed: '2026-09-07'
  note: Design-call notes describing the "cyber world overlaid on Vegas" theme, Agents, Handlers, Queer Coin, and Q/C badge roles.
- kind: url
  url: https://github.com/duplico/qc16_badge/blob/master/boards/renders/cbadge_front.png
  title: C badge front render (Queercon 16 badge repo)
  accessed: '2026-09-07'
  note: Confirms the companion "C badge" is a separate small MSP430FR2111-based board, silkscreened "QUEERCON 16 2019 C BADGE R0", queercon.org - blinkylights.ninja.
- kind: url
  url: https://hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard/
  title: Queercon 16 Q Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-badges); event read as ''queercon-2019''.'
- kind: url
  url: https://hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard/
  title: 'Hands-On: Queercon 16 Hardware Badge Shows Off Custom Membrane Keyboard'
  accessed: '2026-09-08'
  note: Confirmed the badge exists and pulled team, chip, display, LED, keyboard, and power details; source of the featured image.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This repo covers two boards for Queercon 16 (2019): the main "Q badge" (TI CC2640R2F BLE SoC, e-paper display, RGB LED tail, keypad, BLE proximity/game system) and a smaller companion "C badge" access-pass fob (MSP430FR2111). The two photos saved here (from the repo''s art/ folder, dated July 2019) are of a C badge prototype, since no photo of an assembled Q badge was found in the repo; the Q badge''s only image asset is a tiny logo graphic. Price, quantity made, and current availability are not stated anywhere in the repo; it is presumed given free to registered attendees, per Queercon''s usual badge distribution model, but that specific claim is not sourced. No maker blog post or press coverage was found beyond the repo itself. Merged with duplicate entry ''Queercon 16 Q Badge'' (queercon-2019-queercon-16-q-badge).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/queercon-16-badge/
- /badges/queercon-2019/queercon-16-q-badge/
model:
  file: assets/models/queercon-2019/queercon-16-badge.glb
  method: kicad
  source_file: boards/epaper_breakout/epaper_breakout.kicad_pcb
  generated: '2026-09-10'
  bytes: 98248
---

Queercon 16's badge was a two-part electronic system built by George Louthan ("duplico") for the 2019 edition of Queercon, the LGBTQ+ hacker party and community held alongside DEF CON 27 in Las Vegas. The main "Q badge" is a Bluetooth LE-enabled board around a TI CC2640R2F SoC, with a 2.9" (128x296) e-paper display, a matrix keypad, six RGB "tail" LEDs driven by a Holtek HT16D35B controller, a light sensor, and battery-voltage sensing. It ran a game layered over the con's "cyber world overlaid on Vegas" theme: each badge hosted an on-board "Agent" that could be sent on missions assigned by nearby "Handlers," found via BLE proximity scanning, and earn or spend a virtual currency called Queer Coin.

A smaller companion board, the "C badge," plugged into a Q badge over a short wired link to grant one-shot capabilities — effectively an access pass tied to specific real-world locations or activities at the con. It ran on a simpler MSP430FR2111 microcontroller with its own small board, silkscreened "QUEERCON 16 2019 C BADGE R0."

Both boards' hardware (KiCad) and firmware (TI Code Composer Studio, for the CC2640R2F and MSP430FR2111) are published in a single public repository. No pricing, production quantity, or distribution details beyond "given to attendees" were found; the archive marks those fields empty rather than guess.

## Make your own

Hardware and firmware for both the Q badge and C badge are in the repo. Board files are KiCad (for the e-paper breakout) and native TI CCS/PCB layout for the main boards; firmware is written for TI Code Composer Studio targeting the CC2640R2F (Q badge, using TI's BLE stack) and the MSP430FR2111 (C badge). Pre-built production firmware images (`qbadge.hex`, `qbadge.out`) and a flashing script are included under `prod_qbadge/`.

## Notes merged from the duplicate entry "Queercon 16 Q Badge"

The Queercon 16 "Q Badge" was a companion device built alongside Queercon 16's main electronic badge in 2019, serving as a control panel for the convention's alternate-reality game. A team of four — Evan Mackay, George Louthan, Tara Scape, and Subterfuge — built it around a TI CC2640R2 Bluetooth-capable microcontroller, a 2.9" e-ink display (128x296), and a custom CMYK membrane keyboard with embossed buttons laid out in a circle and tailored to the ARG's puzzles. Tara Scape's artwork gives the badge what Hackaday described as a "Rainbow Blade Runner" look.

Lighting comes from 18 RGB LEDs total: six side-view LEDs lighting the display's edges through 3D-printed bezels, driven together with twelve more perimeter LEDs by a Holtek HT16D35B controller. The badge talks to others over a wired RJ12 (6P6C) jack rather than (or in addition to) its BLE radio, and runs off two AA batteries through a Skyworks voltage regulator.

No maker-published project page, price, production quantity, or open-source hardware/firmware release for this specific badge was found; what is documented above comes from Hackaday's hands-on coverage at the show.
