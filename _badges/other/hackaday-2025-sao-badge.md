---
title: Vince SAO Badge
id: other-hackaday-2025-sao-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2025
makers:
- name: dtwprojects
summary: A DIY SAO built around an LP5810 I2C LED driver, with a button and an analog sensor input, that blinks out an elapsed-time value as an LED pulse pattern.
functions: 'Reads a button and an analog sensor; on a button press it blinks out the elapsed time since the last press as an LED pulse pattern via four LEDs on an LP5810 I2C LED driver. The analog sensor is read each cycle but its value is not encoded into the output pattern in the published firmware.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: ATtiny
  leds:
    count: 4
    type: null
    note: Driven via an LP5810 I2C LED driver (I2C address 0x50, four LED outputs at registers 0x40-0x43).
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/dtwprojects/Hackaday_2025_SAO_badge
  eda_tool: null
links:
- label: github.com/dtwprojects/Hackaday_2025_SAO_badge
  url: https://github.com/dtwprojects/Hackaday_2025_SAO_badge
  kind: repo
images: []
contact: {}
notes:
- The repository ("Vince_SAO_Badge") contains only firmware (one .ino sketch) and a GPL-3.0 LICENSE; no schematic, gerbers, BOM, or photos are published, so hardware details beyond what the firmware implies are unconfirmed.
status: listed
sources:
- kind: url
  url: https://github.com/dtwprojects/Hackaday_2025_SAO_badge
  title: Hackaday_2025_SAO_badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''Hackaday 2025''.'
- kind: url
  url: https://raw.githubusercontent.com/dtwprojects/Hackaday_2025_SAO_badge/main/Vince_SAO_Badge/Vince_SAO_Badge.ino
  title: Vince_SAO_Badge.ino
  accessed: '2026-09-07'
  note: 'Firmware source: ATtiny + TinyWireM talking to an LP5810 LED driver at I2C address 0x50, pins for an LED signal output, an analog sensor (A3), and a pull-up button (pin 4). On button release it blinks out the elapsed time (dt = micros() - tm) as a bit pattern across four LED channels; the analog sensor reading (val) is assigned each loop but never referenced by any output routine, so it is not actually displayed.'
- kind: url
  url: https://api.github.com/repos/dtwprojects/Hackaday_2025_SAO_badge/git/trees/main?recursive=1
  title: 'GitHub API: repo file tree'
  accessed: '2026-09-07'
  note: Confirms the repo holds only .gitignore, LICENSE (GPL-3.0), a one-line README, and the single firmware sketch under Vince_SAO_Badge/ - no hardware design files or images.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Verification pass (2026-09-07): confirmed the firmware, LED-driver, and file-tree claims against the cited sources, but made two corrections. (1) The previous functions/summary text said the badge encodes "sensor/timing values" - re-reading Vince_SAO_Badge.ino shows the analog sensor value (val) is read into a variable each loop but never passed to any output routine; only the elapsed time (dt) is actually blinked out. Wording corrected to stop claiming the sensor reading is displayed. (2) The previous entry moved this into supercon-2025 based solely on the repo being named "Hackaday_2025_SAO_badge" and 2025 timing, while its own notes admitted no source confirms the event. Checked the maker''s GitHub profile and dtwprojects.com for corroboration; neither mentions Supercon, a Hackaday event, or this badge at all. Repo-name inference alone does not meet the "never invent" bar for an event/distribution claim, so this entry is moved back to event: other (year 2025 kept, since that much is directly readable from the repo name/timing). No maker profile, storefront, Hackaday.io page, or press coverage of this specific project was found, so maker''s real name, price, quantity, availability, board shape/color, event of distribution, and photos remain unknown.'
last_modified_date: '2026-09-07'
---

This is a small DIY SAO (Simple Add-On) whose firmware repository is named "Vince_SAO_Badge," published by the GitHub user dtwprojects under the repo `Hackaday_2025_SAO_badge`. Only firmware is published: an Arduino sketch for an ATtiny-family microcontroller that talks over I2C (via TinyWireM) to an LP5810 LED driver at address 0x50, controlling four LED channels. The board also reads an analog sensor and a push-button; releasing the button after a hold triggers a routine that blinks out the elapsed hold time as a bit pattern across the four LEDs. The analog sensor is read on every loop but its value is not passed to any output routine in the published code, so despite the sensor wiring, only timing data is actually displayed.

No schematic, PCB files, bill of materials, or photos accompany the code, and no storefront, Hackaday.io project page, or press coverage of the board turned up in research, so its real name, price, production quantity, availability, and appearance remain unconfirmed. The repository's name and file contents point to 2025, but no source - including the maker's own GitHub profile and personal site - confirms which event, if any, this SAO was built for or distributed at, so it is filed as unaffiliated (event: other) rather than assigned to a specific convention.
