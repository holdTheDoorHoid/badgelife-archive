---
title: BSidesSF 2024 Electronic Badge (Attribution Game)
id: bsides-san-francisco-2024-bsidessf-2024-electronic-badge-attribution-game
layout: badge
parent: BSides San Francisco 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-san-francisco-2024
year: 2024
makers:
- name: Joe FitzPatrick (securityfitz)
  role: hardware design
- name: rlc4
  role: software
- name: lanrat
  role: software
- name: securelyfitz
  role: software
summary: The official BSidesSF 2024 conference badge, built to run the "Attribution Game," an infrared card-trading CTF where attendees deduce a threat actor, tool, and victim.
functions: 'Players enter a handle on first boot, then use an onboard IR transceiver to trade cryptographically-signed "clue" cards and contact info with other attendees. Collecting enough clues lets a player attribute an attack across each of six rounds; a game organizer verifies the win. After the con the badge doubles as a CircuitPython learning platform.'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
  - security
  - learn to solder
tech:
  mcu: RP2040 (Seeed Xiao RP2040-derived)
  leds:
    count: 2
    type: WS2812B
    note: 2x neopixel LEDs
  display: 128x64 OLED (SH1106 controller, I2C)
  connectivity:
  - ir
  - i2c
  - usb
  battery: 1x AA plus boost converter, with USB-C power option and a switch between the two
  sao_version: null
  inputs:
  - buttons
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Distributed to attendees of BSidesSF 2024.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/BSidesSF/badge-2024/tree/main/hardware
  firmware_url: https://github.com/BSidesSF/badge-2024/tree/main/software
  eda_tool: KiCad
  license: CC BY-SA 4.0
  notes: KiCad hardware source, CircuitPython firmware, and docs (BADGE.md, GAME.md, DEVELOP.md, HARDWARE.md) are all in the repo.
links:
- label: github.com/BSidesSF/badge-2024
  url: https://github.com/BSidesSF/badge-2024
  kind: repo
images: []
contact: {}
notes:
- Official BSidesSF 2024 conference electronic badge built around an 'Attribution Game' CTF challenge (identify threat actor, tool, and victim), source and hardware/firmware docs on GitHub. Found by the event-year sweep, task bsides-las-vegas.
- 'Sheet/sweep title matches the maker''s own README title, no change needed.'
status: released
sources:
- kind: url
  url: https://github.com/BSidesSF/badge-2024
  title: BSidesSF 2024 Electronic Badge (Attribution Game)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-las-vegas); event read as ''BSides San Francisco 2024''.'
- kind: url
  url: https://raw.githubusercontent.com/BSidesSF/badge-2024/master/README.md
  title: 'badge-2024: README'
  accessed: '2026-09-10'
  note: 'Confirms maker, game concept, that hardware is based on the LABScon badge, and CC BY-SA 4.0 license.'
- kind: url
  url: https://raw.githubusercontent.com/BSidesSF/badge-2024/master/docs/HARDWARE.md
  title: 'badge-2024: Hardware docs'
  accessed: '2026-09-10'
  note: 'MCU (RP2040/Xiao-derived), 16MB flash, SH1106 OLED, IR PHY on UART, 5-way d-pad, 2x neopixel, AA battery + boost, USB-C.'
- kind: url
  url: https://raw.githubusercontent.com/BSidesSF/badge-2024/master/docs/BADGE.md
  title: 'badge-2024: Using the Badge'
  accessed: '2026-09-10'
  note: 'Confirms IR-based card trading mechanics, 6 rounds of the game, and post-con CircuitPython reuse.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'No photo of the assembled badge was found (the GitHub repo has no images of the physical unit, only KiCad source files and an .xcf card-art file; a search turned up only text coverage). Price and quantity made are not stated anywhere found; distribution is free to attendees per the docs, so availability is recorded as free rather than unknown. A LABScon 2023 badge (pdxbadgers/badge-2024 fork notes it was "designed for LABScon 2023 and then revised... for BSidesSF 2024") is the direct ancestor design and may deserve its own entry under a different event.'
last_modified_date: '2026-09-10'
---

The 2024 BSidesSF badge was designed by Joe FitzPatrick (securityfitz) as a favor to the conference, reusing a LABScon badge as its hardware base; the firmware is a CircuitPython fork of the LABScon badge software, further developed by rlc4, lanrat, and securelyfitz. Rather than a simple wearable, the badge is the vehicle for the "Attribution Game," a Clue-like CTF: attendees pick a handle on first boot, then hold badges edge-to-edge to trade infrared "clue" cards and contact info. Each of six rounds asks players to deduce a threat actor, an attack tool, and a victim from the clues they've collected; a completed set is checked by a game organizer.

Hardware is built around an RP2040 (derived from the Seeed Xiao RP2040), a 128x64 SH1106 OLED over I2C, a 5-way d-pad, two WS2812B ("neopixel") LEDs, an IR transceiver on UART for badge-to-badge trading, and a AA-battery-plus-boost-converter power supply with a USB-C option. Hardware (KiCad) and firmware (CircuitPython) are both published on GitHub under CC BY-SA 4.0, and the docs note the badge doubles as a general CircuitPython learning platform after the conference.

No price or production quantity is stated in any source found; the badge was given to BSidesSF 2024 attendees rather than sold.
