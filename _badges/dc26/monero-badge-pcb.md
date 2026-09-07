---
title: dc26-monero-badge-pcb
id: dc26-monero-badge-pcb
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
series: Monero Badge
makers:
- name: dodgymike (Mike Davis / @elasticninja)
  url: https://github.com/dodgymike
  role: PCB/hardware design, firmware
- name: tonym128
  url: https://github.com/tonym128
  role: co-creator, challenge puzzle
- name: fluffypony
  role: co-creator, challenge puzzle
summary: An unofficial Monero-branded badge made for DEF CON 26 (2018), built around a dense 576-LED APA102 matrix and unlocked through an encoded-message challenge run by its creators.
functions: Displays bright RGB animations across a tightly packed 576-APA102-LED matrix; includes an accelerometer/gyro for motion-driven input. Distributed via a cryptography challenge -- attendees decoded an encrypted message printed on companion challenge tokens/cards, used the same key to encode a phrase, and tweeted it at the creators to redeem the real badge.
look:
  colors: []
  shape: rectangle
  themes:
  - crypto
  - puzzle
  - ctf
tech:
  mcu: STM32F4 (STM32F405)
  leds:
    count: 576
    type: APA102
    note: Extremely dense LED matrix; the display manufacturing difficulty limited the number of working units.
  display: LED matrix (576x APA102)
  connectivity: []
  inputs:
  - accelerometer
  battery: 2x 18650 Li-ion cells (after redesign; an earlier power supply failed during testing)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 155 attempted; 125 completed working boards (non-working units were given to hackers to try to repair)
  availability: sold_out
  availability_note: 'Checked 2026-09-07: this was a one-time DEF CON 26 (2018) run distributed via an in-person challenge, not a standing storefront.'
  distribution:
  - contest
  where: Redeemed in person at DEF CON 26 (2018) by solving the Monero Badge Challenge (decoding an encrypted message on companion tokens/cards and tweeting an encoded reply to the creators).
make_your_own:
  open_source: true
  hardware_url: https://github.com/dodgymike/dc26-monero-badge-pcb
  firmware_url: https://github.com/dodgymike/monero-badge-f405
  eda_tool: KiCad
  notes: The hardware repo also contains a companion "dc26-challenge" coin PCB project (in the dc26-challenge directory) and a Python script for board visualization. A separate repo (github.com/tonym128/monero-badge) documents the decode puzzle used to redeem the badge.
links:
- label: github.com/dodgymike/dc26-monero-badge-pcb
  url: https://github.com/dodgymike/dc26-monero-badge-pcb
  kind: repo
- label: github.com/dodgymike/monero-badge-f405 (firmware)
  url: https://github.com/dodgymike/monero-badge-f405
  kind: repo
- label: github.com/tonym128/monero-badge (challenge puzzle)
  url: https://github.com/tonym128/monero-badge
  kind: repo
- label: The Monero Badge Challenge || DEF CON 26
  url: https://monerobadge.org
  kind: website
- label: 'Hackaday: All The Badges Of DEF CON 26 (vol 4)'
  url: https://hackaday.com/2018/09/05/all-the-badges-of-def-con-26-vol-4/
  kind: article
- label: 'Hermit''s Cave: DEFCON 26 Badge Photos'
  url: https://blog.stackattack.net/2018/09/02/defcon-26-badge-photos/
  kind: article
images:
- file: assets/images/badges/dc26/monero-badge-pcb/f6ca688ada.jpg
  source: https://hackaday.com/2018/09/05/all-the-badges-of-def-con-26-vol-4/
  credit: Hackaday
  caption: The Monero badge's dense APA102 LED matrix lit up
- file: assets/images/badges/dc26/monero-badge-pcb/1318cb1f19.jpg
  source: https://blog.stackattack.net/2018/09/02/defcon-26-badge-photos/
  credit: Hermit's Cave (blog.stackattack.net)
  caption: The Monero unofficial DEF CON 26 badge, front and back, shown next to a quarter for scale
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/dodgymike/dc26-monero-badge-pcb
  title: dc26-monero-badge-pcb
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''DEF CON 26''.'
- kind: url
  url: https://github.com/dodgymike/monero-badge-f405
  title: monero-badge-f405
  accessed: '2026-09-07'
  note: Firmware repo README confirms STM32F4 target, DFU flashing procedure, and 24x24-pixel graphics for a display; links back to the hardware repo.
- kind: url
  url: https://hackaday.com/2018/09/05/all-the-badges-of-def-con-26-vol-4/
  title: All The Badges Of DEF CON 26 (vol 4)
  accessed: '2026-09-07'
  note: Names creators @elasticninja and @tonym128, states 155 attempted / 125 completed working boards, 576 APA102 LEDs, STM32F4 MCU, accelerometer/gyro, dual 18650 power after a power-supply failure during testing; source of the badge photo saved.
- kind: url
  url: https://blog.stackattack.net/2018/09/02/defcon-26-badge-photos/
  title: DEFCON 26 Badge Photos - Hermit's Cave
  accessed: '2026-09-07'
  note: Two photos of the physical badge (front/back) next to a coin for scale; one saved to images.
- kind: url
  url: https://github.com/tonym128/monero-badge
  title: 'monero-badge: #DefCon26 #MoneroCoinChallenge solution writeup'
  accessed: '2026-09-07'
  note: Documents the decode-the-message challenge (Vigenere/XOR-style cipher on hex strings) used to redeem the badge; credits @tonym128, @elasticninja and @fluffypony as creators.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: GitHub user dodgymike (Mike Davis) is confirmed as @elasticninja via his own GitHub profile bio, tying the hardware repo to the Hackaday-credited creator. Could not confirm exact price (this was a challenge-redeemed badge, not sold), an exact firmware chip part suffix beyond "STM32F405", or reach monerobadge.org directly (site returned an error; a 2022 Wayback snapshot exists but was not fetchable with available tools). "sao_version"/SAO header not mentioned in any source, left null.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/monero-badge-pcb.glb
  method: kicad
  source_file: dc26.kicad_pcb
  generated: '2026-09-07'
  bytes: 2343760
---

The Monero Badge was an unofficial DEF CON 26 (2018) badge built around a strikingly dense matrix of 576 APA102 LEDs, driven by an STM32F4 microcontroller with an onboard accelerometer/gyro for motion input. It was created by dodgymike (Mike Davis, `@elasticninja`), `@tonym128`, and Monero project figure `@fluffypony`, and was not sold outright: attendees had to solve the "Monero Badge Challenge," decoding an encrypted message printed on companion cards/tokens, then using the same key to encode a phrase and tweet it at the creators to be handed a working badge in person.

The team set out to build 155 units but ran into manufacturing trouble with the LED matrix/display, finishing only 125 working boards; the non-working boards were reportedly given to hackers willing to try to repair them themselves. An earlier power supply design also failed (caught fire) during testing before the team settled on two 18650 Li-ion cells to feed the LED matrix's substantial current draw.

## Make your own

Hardware (KiCad schematics, PCB layout, Gerbers, stencil files, footprints, and a CSV bill of materials) is published at `dodgymike/dc26-monero-badge-pcb`, which also includes a companion DC26 challenge-coin PCB project and a Python board-visualization script. Firmware lives in a separate repo, `dodgymike/monero-badge-f405`, built with a GCC ARM cross-toolchain and flashed over USB DFU (hold the boot button while powering up, then `dfu-util` against the STM32 bootloader). The decode puzzle used to redeem the badge is documented separately at `tonym128/monero-badge`.
