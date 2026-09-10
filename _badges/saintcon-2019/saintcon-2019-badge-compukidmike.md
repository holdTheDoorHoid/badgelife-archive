---
title: SAINTCON 2019 Enigma Badge
id: saintcon-2019-saintcon-2019-badge-compukidmike
layout: badge
parent: Saintcon 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2019
year: 2019
makers:
- name: compukidmike
  url: https://github.com/compukidmike
- name: _bashNinja
- name: Sodium_Hydrogen
  role: firmware
- name: risenrigel
  role: firmware
summary: The official SAINTCON 2019 conference badge, styled as a section of an Enigma rotor and built around a working Enigma-machine emulator with a curved LED matrix and lampboard.
functions: Emulates a historical Enigma machine (rotor IX) for a con-wide decryption challenge, with "Hut 6" challenge stations, JST lighting connectors that let up to 26 badges link together into a ring, and support for plugging in minibadges.
look:
  colors:
  - black
  shape: null
  themes:
  - security
  - puzzle
  - ctf
  - village badge
tech:
  mcu: STM32L433
  leds:
    count: 1051
    type: RGB
    note: 16x64 curved RGB matrix on the top board, 26 lampboard RGB LEDs, plus one charging-status LED
  display: LED matrix 16x64
  connectivity: []
  battery: LiPo 1500 mAh
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '1350'
  availability: not_released
  distribution:
  - free_drop
  where: Given to SAINTCON 2019 attendees as the conference badge; not sold.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/compukidmike/Saintcon2019/tree/master/Hardware
  firmware_url: https://github.com/compukidmike/Saintcon2019/tree/master/Firmware/Saintcon2019
  eda_tool: null
links:
- label: github.com/compukidmike/Saintcon2019
  url: https://github.com/compukidmike/Saintcon2019
  kind: repo
- label: 'mkfactor.com: SAINTCON 2019 badge writeup'
  url: https://mkfactor.com/?p=100
  kind: article
- label: SAINTCON badge talk (YouTube)
  url: https://www.youtube.com/watch?v=MAhJ2W_oN14
  kind: video
images:
- file: assets/images/badges/saintcon-2019/saintcon-2019-badge-compukidmike/1f5b996fd0.jpg
  source: https://mkfactor.com/?p=100
  credit: compukidmike / mkfactor.com
  caption: SAINTCON 2019 Enigma badge, front
- file: assets/images/badges/saintcon-2019/saintcon-2019-badge-compukidmike/e24e892ae4.jpg
  source: https://mkfactor.com/?p=100
  credit: compukidmike / mkfactor.com
  caption: SAINTCON 2019 Enigma badge, back showing lampboard LEDs and boards
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2019
  title: SAINTCON 2019 badge (compukidmike)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''saintcon-2019''.'
- kind: url
  url: https://github.com/compukidmike/Saintcon2019
  title: compukidmike/Saintcon2019 repository
  accessed: '2026-09-07'
  note: Confirms hardware (Hardware/) and firmware (Firmware/Saintcon2019, fpga.hex, SaintconFPGA.ice) are published; no explicit license found; STM32 + Lattice iCE40 FPGA, built via STM32CubeIDE and Icestudio.
- kind: url
  url: https://mkfactor.com/?p=100
  title: 'mkfactor.com: SAINTCON 2019 badge project writeup'
  accessed: '2026-09-07'
  note: Primary source for maker team, LED counts, MCU/FPGA parts, battery, construction, distribution quantity (1350), and cost overrun ($50 target vs ~$70 actual due to tariffs); also source of the two saved photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No price is listed because the badge was distributed free to registered attendees, not sold. No explicit open-source license was found in the repo despite hardware and firmware both being published, so open_source is marked 'partial' rather than 'yes'. look.shape left null; the badge is described as an Enigma-rotor section rather than a standard shape from the vocabulary.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2019/saintcon-2019-badge-compukidmike.glb
  method: gerber
  source_file: Hardware/KiCad Files/Saintcon2019TopBoard/Saintcon2019TopBoard.kicad_pcb
  generated: '2026-09-10'
  bytes: 419648
  size_mm:
  - 148.3
  - 147.3
---

The SAINTCON 2019 badge, designed by compukidmike with _bashNinja and firmware help from Sodium_Hydrogen and risenrigel, was built as a working homage to the WWII Enigma machine. It is shaped like a section of an Enigma rotor and carries an STM32L433 microcontroller alongside a Lattice iCE40HX1K FPGA, driving a curved 16x64 RGB LED matrix and a 26-key lampboard for a total of 1,051 LEDs, powered by a 1500 mAh LiPo sandwiched between two stacked PCBs.

The badge doubled as the vehicle for SAINTCON's annual puzzle: attendees used the onboard Enigma emulator (rotor IX) to decode messages, visited in-person "Hut 6" challenge stations that used a dot-matrix printer, and could link up to 26 badges together via JST lighting connectors to form a ring, with "Commander" badges (held by conference committee members, marked with etched brass emblems) needed to unlock parts of the game. The badge also included a holder for minibadges. About 1,350 units were made and given to attendees as the conference badge itself rather than sold; the team's $50-per-badge target ended up closer to $70 once the design grew in scope and 25% import tariffs hit component costs.

## Make your own

Both the firmware (STM32 code plus the FPGA's Icestudio source and compiled `fpga.hex`) and hardware design files are published in the GitHub repository, along with PDF build and assembly instructions and a challenge/code-sheet reference, though no explicit open-source license is stated in the repo.
