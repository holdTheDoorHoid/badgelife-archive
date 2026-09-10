---
title: keyboard-addon — BB-Q10 Keyboard Shitty Add-On
id: other-keyboard-addon-bb-q10-keyboard-shitty-add-on
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2020
makers:
- name: AramCon Badge Team
  url: https://github.com/aramcon-badge
- name: Uri Shaked
  role: firmware
summary: A BlackBerry Q10 physical keyboard wired up as a Shitty Add-On for the AramCon 2 badge, scanning the keyboard matrix and reporting keypresses over I2C.
functions: Scans a 7x5 BlackBerry Q10 keyboard matrix and buffers keydown/keyup events for the host badge to read over I2C; also drives the keyboard's own backlight LEDs and a status LED under host control.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: STM32F030C8T6
  leds:
    count: 1
    type: discrete
    note: One status LED plus the BB Q10 keyboard's own 4-segment backlight (2 anode/2 cathode lines), all driven by the add-on's MCU.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/aramcon-badge/keyboard-addon/tree/master/pcb
  firmware_url: https://github.com/aramcon-badge/keyboard-addon/tree/master/firmware
  eda_tool: KiCad
links:
- label: github.com/aramcon-badge/keyboard-addon
  url: https://github.com/aramcon-badge/keyboard-addon
  kind: repo
- label: Aramcon Badge Team (GitHub org)
  url: https://github.com/aramcon-badge
  kind: repo
- label: The Badge Add-on ID System (ARAMCON Badge docs)
  url: https://badge.a-combinator.com/addons/addon-id/
  kind: doc
images: []
contact: {}
notes:
- Keyboard SAO for AramCon badge
- No event id for AramCon exists yet in events.yml; this add-on was built for the "AramCon 2" badge (the org's aramcon-firmware repo, created 2020-01-13, is described as "the main firmware code for the AramCon 2 Badge"), so this is most likely a 2020 AramCon item. A separate "badge-2019-upgrade-kit" repo in the same org implies an earlier 2019 AramCon badge existed too, but this add-on repo (created 2020-01-24) postdates the 2020 firmware repo.
status: listed
sources:
- kind: url
  url: https://github.com/aramcon-badge/keyboard-addon
  title: keyboard-addon — BB-Q10 Keyboard Shitty Add-On
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://api.github.com/repos/aramcon-badge/keyboard-addon
  title: aramcon-badge/keyboard-addon (GitHub API)
  accessed: '2026-09-07'
  note: Repo description, creation date (2020-01-24), default branch, file listing (firmware/ and pcb/ dirs).
- kind: url
  url: https://raw.githubusercontent.com/aramcon-badge/keyboard-addon/master/firmware/platformio.ini
  title: firmware/platformio.ini
  accessed: '2026-09-07'
  note: Confirms MCU is an STM32F030C8T6 (disco_f030r8 board, Arduino framework).
- kind: url
  url: https://raw.githubusercontent.com/aramcon-badge/keyboard-addon/master/firmware/src/main.cpp
  title: firmware/src/main.cpp
  accessed: '2026-09-07'
  note: Firmware source confirming I2C keyboard-scanner design, pinout, LED control bits, keyboard matrix size (7 rows x 5 cols), I2C address 0x42, and 2021 copyright by Uri Shaked.
- kind: url
  url: https://api.github.com/orgs/aramcon-badge/repos?per_page=100
  title: aramcon-badge GitHub org repo list
  accessed: '2026-09-07'
  note: Shows keyboard-addon repo alongside "aramcon-firmware" (described as "the main firmware code for the AramCon 2 Badge") and "badge-2019-upgrade-kit", used to date this add-on to the AramCon 2 (2020) badge generation.
- kind: url
  url: https://badge.a-combinator.com/addons/addon-id/
  title: The Badge Add-on ID System | ARAMCON Badge
  accessed: '2026-09-07'
  note: Describes the general AramCon SAO add-on detection system (I2C EEPROM at address 0x50); does not mention the keyboard add-on specifically.
- kind: url
  url: https://badge.a-combinator.com/addons/addons/
  title: Badge Shitty Add-ons | ARAMCON Badge
  accessed: '2026-09-07'
  note: Lists the badge team's documented SAOs (Floppy Disk, Peacock, Speaker, Charlieplexing LED-Matrix); the keyboard add-on is not listed on this public page, suggesting it may not have been an official mass-distributed add-on.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The repo (firmware + KiCad PCB source) is the only real documentation found; there is no README, project write-up, price, quantity, or photo of the finished board. The public AramCon add-on catalog page does not list this keyboard add-on among the badge team's official SAOs, so it may have been a smaller/limited build rather than a mass-distributed give-away. No AramCon event id exists yet in this archive's events.yml, so event is left as "other"; best evidence points to the "AramCon 2" (2020) badge generation. Could not confirm price, quantity made, or availability.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/keyboard-addon-bb-q10-keyboard-shitty-add-on.glb
  method: kicad
  source_file: pcb/q10keyboard-addon.kicad_pcb
  generated: '2026-09-10'
  bytes: 219160
---

The BB-Q10 Keyboard Shitty Add-On is a small board built by the AramCon Badge Team that turns a salvaged BlackBerry Q10 physical keyboard into a Shitty Add-On (SAO) for the AramCon badge. An STM32F030C8T6 microcontroller on the add-on scans the keyboard's 7x5 button matrix, buffers keydown and keyup events in a ring buffer, and exposes them to the host badge over I2C (address 0x42) using the standard 6-pin SAO v1.69bis connector. The host badge can also command the add-on to enable an interrupt line and to switch on the keyboard's own segmented backlight and a small status LED, which breathes gently while the badge hasn't yet talked to it over I2C.

The firmware, written by badge-team member Uri Shaked, and the KiCad hardware design (including custom BlackBerry Q10 keyboard and SAO footprints) are both published in the `aramcon-badge/keyboard-addon` GitHub repository. The repository was created in January 2020, shortly after the org's "AramCon 2 Badge" firmware repository, which places this add-on with the second-generation AramCon badge rather than the original 2019 unit. Unlike some of the badge team's other add-ons (Floppy Disk, Peacock, Speaker, Charlieplexing LED-Matrix), the keyboard add-on does not appear on AramCon's public add-on catalog page, so it is unclear whether it was distributed broadly at the event or built in smaller numbers for internal/demo use.

No price, production quantity, or photos of the assembled board were found in the available sources; anyone with more detail on how (or whether) it was handed out at AramCon should update this entry.

## Make your own

The full source is open: KiCad schematic and PCB files live under `pcb/` in the repository (custom footprints for the Q10 keyboard and SAO connector are included as KiCad libraries), and the PlatformIO-based Arduino firmware lives under `firmware/`, targeting an STM32F030 ("disco_f030r8" board definition) flashed via a J-Link. Building one requires a salvaged BlackBerry Q10 keyboard module wired to the PCB's row/column and backlight anode/cathode pins as defined in `firmware/src/main.cpp`.
