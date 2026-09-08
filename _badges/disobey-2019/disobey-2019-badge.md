---
title: Disobey 2019 Badge
id: disobey-2019-disobey-2019-badge
layout: badge
parent: Disobey 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: disobey-2019
year: 2019
makers:
- name: Disobey / badge.team
  url: https://github.com/disobeyfi/badge-2019
summary: 'The third Disobey electronic badge: an ESP32 badge with a backlit LCD, six capacitive touch buttons, six RGB LEDs, a buzzer, and IR, used to drive an on-site puzzle competition.'
functions: 'Runs MicroPython apps distributed via badge.disobey.fi; core use was as part of an event-wide puzzle/hacking competition, with the display, LEDs, buzzer, and IR receiver/transmitter used for puzzle interactions and status feedback.'
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - ctf
  - wearable
tech:
  mcu: ESP32
  leds:
    count: 6
    type: RGB
    note: Mounted around the outline of the PCB, on the back of the board.
  display: LCD with backlight
  connectivity:
  - wifi
  - i2c
  - usb
  - ir
  battery: 2x AAA (1.5V alkaline)
  sao_version: null
  inputs:
  - touch
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Given to participants, sponsors, and organizers of Disobey 2019; PCB art/color varied by ticket type.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/disobeyfi/badge-2019
  firmware_url: https://github.com/badgeteam/ESP32-platform-firmware
  eda_tool: null
  license: GPL-3.0
  notes: 'Repo includes BOM (PDF/XLS) and layout PDFs (front/back) but no confirmed schematic/Gerber source; firmware built on badge.team''s shared ESP32 MicroPython platform, not badge-specific.'
links:
- label: badge.team/docs/badges/disobey-2019
  url: https://badge.team/docs/badges/disobey-2019/
  kind: website
- label: disobeyfi/badge-2019 (hardware and source)
  url: https://github.com/disobeyfi/badge-2019
  kind: repo
- label: badgeteam/ESP32-platform-firmware
  url: https://github.com/badgeteam/ESP32-platform-firmware
  kind: repo
- label: wiki.badge.team/Disobey2019Badge/API
  url: https://wiki.badge.team/Disobey2019Badge/API
  kind: doc
images: []
contact: {}
notes:
- ESP32-based MicroPython badge with display, buttons, touch sensing, buzzer, IR, and RGB LEDs, used for a puzzle competition at Disobey 2019; only Disobey 2020's badge is currently in the archive. Found by the event-year sweep, task con-disobey.
- 'Sweep found the item via badge.team''s summary page; the maker''s own GitHub repo (disobeyfi/badge-2019) confirms it as the "3rd electronic badge produced for Disobey" and gives a fuller feature/team list. Title matches the sweep''s wording.'
status: released
sources:
- kind: url
  url: https://badge.team/docs/badges/disobey-2019/
  title: Disobey 2019 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-disobey); event read as ''Disobey 2019''.'
- kind: url
  url: https://github.com/disobeyfi/badge-2019
  title: disobeyfi/badge-2019 - GitHub
  accessed: '2026-09-08'
  note: 'Maker repo: README confirms features (6 RGB LEDs, 6 touch buttons, LCD w/ backlight, buzzer, WiFi, I2C, USB serial), team credits, GPL-3.0 license, BOM and layout PDFs under hardware/.'
- kind: url
  url: https://wiki.badge.team/Disobey2019Badge/API
  title: Disobey2019Badge/API - badge.team wiki
  accessed: '2026-09-08'
  note: 'Checked for photos of the badge; page has no images.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (MCU, features, team, license, distribution) confirmed via the maker''s own badge.team page and disobeyfi/badge-2019 GitHub repo, so this is better than low confidence, but no price/quantity figures, no confirmed schematic or Gerber files (only BOM and layout PDFs), and no usable photo of the physical badge were found (checked badge.team, GitHub repo, and the badge.team wiki API page). Distribution set to free_drop since it was given to attendees/sponsors/organizers rather than sold; no evidence found either way so this is inferred, not stated outright.'
last_modified_date: '2026-09-08'
---

The Disobey 2019 badge was the third electronic badge produced for Disobey, the Finnish hacker conference, built around an ESP32 and programmable in MicroPython. It shipped with a backlit LCD screen, six capacitive touch buttons, six RGB LEDs running along the back edge of the PCB, a piezoelectric buzzer, an infrared receiver/transmitter, and Wi-Fi and I2C connectivity, powered by two AAA batteries. PCB artwork and color varied depending on the recipient's ticket type (participant, sponsor, or organizer), and the badge doubled as the medium for an event-wide puzzle competition.

Hardware and firmware work was led by badge.team, with a small named team (Heikki Juva and Kliment on hardware/manufacturing, Renze and Gaja on software, Valtteri Raila on the puzzle, Otto on graphics, and Teemu Hakala running badge-assembly workshops). The badge's firmware built on badge.team's shared ESP32 MicroPython platform, the same base later used for SHA2017, HackerHotel 2019, CampZone 2019, and Disobey 2020. Community apps were distributed through badge.disobey.fi.

The `disobeyfi/badge-2019` GitHub repository (GPL-3.0) publishes a bill of materials and front/back layout PDFs, but no confirmed schematic or Gerber source was located, so hardware openness is marked partial rather than full.
