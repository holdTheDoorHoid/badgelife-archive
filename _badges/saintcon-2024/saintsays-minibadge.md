---
title: SaintSays MiniBadge
id: saintcon-2024-saintsays-minibadge
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: durkinza (Zane Durkin)
summary: A Simon-Says-style memory game minibadge for SAINTCON 2024, with four buttons and four LEDs and an EEPROM-saved high score.
functions: 'Memory/pattern game (Simon Says style) with four buttons and four LEDs; tracks and saves a high score to EEPROM; optional I2C link lets the main SAINTCON badge read button presses and the score, and set settings/brightness; also has a settings mode and a lightshow/party mode.'
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - learn to solder
tech:
  mcu: ATtiny
  leds:
    count: 4
    type: discrete
    note: Four individual LEDs used for the memory-game pattern display.
  display: none
  connectivity:
  - i2c
  inputs:
  - buttons
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - swap
  where: Distributed/traded as a SAINTCON 2024 minibadge; exact acquisition method (kit vs. assembled, con store vs. trading table) not stated in available sources.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/durkinza/SaintSays-MiniBadge/tree/main/KiCad
  firmware_url: https://github.com/durkinza/SaintSays-MiniBadge/tree/main/SaintSays
  eda_tool: KiCad
  notes: 'Repo includes KiCad schematic/PCB, Gerbers, and the Arduino .ino firmware. No BOM file found. Documentation: assembly/soldering guide and "how it''s made" post on the maker''s site (zanedurk.in), unreachable at last check (502 error).'
links:
- label: github.com/durkinza/SaintSays-MiniBadge
  url: https://github.com/durkinza/SaintSays-MiniBadge
  kind: repo
- label: SAINTSAYS Assembly (YouTube)
  url: https://www.youtube.com/watch?v=7bsx-1z2B9c
  title: SAINTSAYS Assembly
  kind: video
images: []
contact: {}
notes:
- ATtiny-based memory-game minibadge, the maker's first SAINTCON minibadge, made for SAINTCON 2024. Found by the event-year sweep, task saintcon-2024.
- 'Sweep imported the title as "SaintSays MiniBadge"; the maker''s own README/repo title it "SAINTSays Mini-Badge" (all-caps SAINT). Kept the sweep''s title casing here since it matches the entry id/slug.'
status: released
sources:
- kind: url
  url: https://github.com/durkinza/SaintSays-MiniBadge
  title: SaintSays MiniBadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/durkinza/SaintSays-MiniBadge/main/README.md
  title: durkinza/SaintSays-MiniBadge README
  accessed: '2026-09-10'
  note: 'Confirms maker, event/year, ATtiny MCU, I2C programming/header pinout, disclaimer of non-affiliation with SAINTCON/Utah SAINT; links to assembly/build docs on zanedurk.in.'
- kind: url
  url: https://raw.githubusercontent.com/durkinza/SaintSays-MiniBadge/main/SaintSays/SaintSays.ino
  title: SaintSays.ino firmware source
  accessed: '2026-09-10'
  note: 'Confirms 4 buttons and 4 LEDs, I2C device address, EEPROM-saved high score and settings, game/settings/lightshow modes, and pin mapping differences between minibadge hardware revisions.'
- kind: url
  url: https://www.youtube.com/watch?v=7bsx-1z2B9c
  title: SAINTSAYS Assembly - YouTube
  accessed: '2026-09-10'
  note: 'Confirms it is "a fun memory game" designed by durkinza for SAINTCON 2024; used as a secondary description source. Thumbnail frame considered for an image but rejected as a text title card, not a clear shot of the badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, event/year, MCU, game mechanic, I2C link to the main badge, open hardware/firmware) are confirmed from the maker''s own GitHub repo and firmware source, so this is better than low confidence, but several fields stay empty: PCB color/look, price, quantity made, and exact distribution method (sold vs. given vs. traded) were not stated anywhere found. The maker''s own site (zanedurk.in), which hosts the assembly guide and a "how it''s made" writeup, returned a 502 Bad Gateway at last check and could not be read; those two pages likely have the missing details (photos, PCB color, build story) and are worth a retry later. No product photo of the assembled badge was found; the only image available (a YouTube thumbnail) is a text title card, not a usable photo, so images was left empty rather than filled with something that does not show the item.'
last_modified_date: '2026-09-10'
---

The SaintSays MiniBadge is an ATtiny-based memory game made by Zane Durkin (durkinza) for SAINTCON 2024 — by his own account, his first minibadge design for the con. It plays like Simon Says: four LEDs flash a growing pattern and the player repeats it back on four buttons, with the current high score saved to the chip's EEPROM so it survives a power cycle.

The badge also has an optional I2C link (address `0x23`) that lets a host SAINTCON badge read button presses and the current score, and push settings or brightness changes to the minibadge — a feature that can be compiled out to save code space if the I2C header pins are needed for something else. Beyond the core game mode, the firmware includes a settings mode and a lightshow/party mode. The repository documents two pin-mapping revisions of the hardware (an earlier v1/v2 layout and a v3+ layout), with the shipped firmware wired for the v3+ minibadge.

Both the KiCad hardware (schematic, PCB, and Gerbers) and the Arduino firmware are published on GitHub, making it open source in design, though no bill of materials was found in the repo. The maker's own site (zanedurk.in) hosts a soldering guide and a "how it's made" writeup that likely cover build details, PCB appearance, and distribution, but the site returned a server error when checked and could not be read for this entry.
