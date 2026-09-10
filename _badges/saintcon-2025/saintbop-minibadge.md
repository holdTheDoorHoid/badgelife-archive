---
title: SaintBop-Minibadge
id: saintcon-2025-saintbop-minibadge
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: durkinza
  url: https://github.com/durkinza
summary: A "Bop It"-style reflex game minibadge with a Twist It knob, Bop It button, and Shake It vibration sensor, built as a SAINTCON badge add-on.
functions: 'Menu-driven modes: a copy-the-random-action reflex game with a saved high score (EEPROM), a settings menu (fast mode, "chaotic" mode, mute, boot-to-light-show, score-while-asleep), a light-show/party mode, and a second game mode listed as not yet implemented. LEDs display the current menu selection in binary.'
look:
  colors: []
  shape: null
  themes:
  - game
  - puzzle
tech:
  mcu: ATtiny84
  leds:
    count: 3
    type: discrete
    note: One LED each for Bop It, Shake It, and Twist It actions; used together to show menu position in binary.
  display: none
  connectivity:
  - i2c
  inputs:
  - rotary encoder
  - buttons
  - accelerometer
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/durkinza/SaintBop-Minibadge/tree/main/KiCad/SaintBop
  firmware_url: https://github.com/durkinza/SaintBop-Minibadge/blob/main/SaintBop/SaintBop.ino
  eda_tool: KiCad
links:
- label: github.com/durkinza/SaintBop-Minibadge
  url: https://github.com/durkinza/SaintBop-Minibadge
  kind: repo
images: []
contact: {}
notes:
- Maker is Zane Durkin (durkinza), co-founder of NeverLAN CTF, per his public GitHub profile.
status: released
sources:
- kind: url
  url: https://github.com/durkinza/SaintBop-Minibadge
  title: SaintBop-Minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/durkinza/SaintBop-Minibadge/blob/main/SaintBop/SaintBop.ino
  title: SaintBop.ino firmware source
  accessed: '2026-09-07'
  note: Pin definitions and mode/game logic; confirms ATtiny target (build/ATTinyCore.avr.attinyx4), 3 LEDs, potentiometer/rotary encoder, vibration sensor, piezo buzzer, I2C link to a "Main badge", EEPROM high-score storage.
- kind: url
  url: https://api.github.com/repos/durkinza/SaintBop-Minibadge
  title: GitHub repo metadata (API)
  accessed: '2026-09-07'
  note: Repo created 2025-06-30, last pushed 2025-10-03; confirms maker durkinza, language C++, no license file.
- kind: url
  url: https://raw.githubusercontent.com/durkinza/SaintBop-Minibadge/main/SAINTBop%20User%20Guide.odt
  title: SAINTBop User Guide (ODT)
  accessed: '2026-09-07'
  note: Titled "SAINT Bop By Durkinza"; describes the 7 modes (Sleep, Menu, Game 1, Game 2 [not implemented], Show Score, Settings, Light Show) and menu/settings behavior in the maker's own words.
- kind: url
  url: https://api.github.com/repos/durkinza/SaintBop-Minibadge/commits
  title: Commit history (API)
  accessed: '2026-09-07'
  note: Commit messages "Adding document draft" (2025-08-29) and "Adding peer reviewed document" (2025-08-31) match SAINTCON's badge-add-on peer review process and SAINTCON 2025's late-August 2025 dates, supporting the event correction from "other" to saintcon-2025.
- kind: url
  url: https://api.github.com/users/durkinza
  title: durkinza GitHub profile (API)
  accessed: '2026-09-07'
  note: Real name Zane Durkin, co-founder of NeverLAN CTF; personal site zanedurk.in was unreachable (502) at time of check.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No maker photos of the assembled badge were found; the only images in the repo/User Guide are two QR codes, not product photos, so no images could be saved. No storefront, price, quantity, or distribution details were found anywhere -- this looks like a SAINTCON badge-add-on village submission (built for personal/community distribution rather than sale) but that is inferred from the peer-review commit message, not stated outright, so it is noted here rather than filled into get_one. The event was corrected from "other" to saintcon-2025 based on the "SAINT" name, the "peer reviewed document" commit dated 2025-08-31, and SAINTCON 2025's late-August timing -- no source states the event by name outright, so confidence is medium rather than high. Game Mode 2 is explicitly unimplemented per both the firmware and the user guide. durkinza's personal blog (zanedurk.in) returned a 502 error and could not be checked for further posts.
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/saintbop-minibadge/
model:
  file: assets/models/saintcon-2025/saintbop-minibadge.glb
  method: kicad
  source_file: KiCad/SaintBop/SaintBop.kicad_pcb
  generated: '2026-09-10'
  bytes: 104220
---

SaintBop is a "Bop It"-style reflex minibadge made by Zane Durkin (GitHub handle durkinza, co-founder of NeverLAN CTF), built around an ATtiny84. It gives the wearer three actions -- Bop It (a button), Twist It (a rotary/potentiometer knob), and Shake It (a vibration sensor) -- each paired with its own LED and driven by a piezo buzzer for feedback, closely mirroring the mechanics of the Hasbro "Bop It" toy the name riffs on.

The badge boots into a menu (selections shown as a binary LED pattern) offering a reflex game that shows a random action to copy against a shrinking timer, a high-score display saved to EEPROM, a settings menu (fast mode, a "chaotic" single-sense mode, mute, boot-to-light-show, and showing the scoreboard while asleep), and a light-show "party mode." A second game mode is present in the menu but explicitly marked not yet implemented in both the firmware and the maker's user guide. The firmware also defines an I2C link intended to let a "main badge" read or set the minibadge's settings and high score, though this is commented out in the current source.

The repository's commit history includes a "peer reviewed document" commit dated 2025-08-31, which lines up with SAINTCON's practice of peer-reviewing badge add-ons and with SAINTCON 2025's late-August dates -- the basis for setting this entry's event to SAINTCON 2025 rather than leaving it under "Other." No storefront, price, quantity-made, or distribution details turned up in the repo, its documentation, or a search for the maker elsewhere, so those fields remain empty rather than guessed.

## Make your own

KiCad source and Gerber files for the PCB are in the repo's `KiCad/SaintBop` folder, and the Arduino firmware is `SaintBop/SaintBop.ino`, written for the ATtiny84 (built against ATTinyCore's `attinyx4` variant, per the included build output). A user guide (`SAINTBop User Guide.odt`) documents the modes and settings for anyone assembling or using the badge.
