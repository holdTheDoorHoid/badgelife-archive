---
title: TR20 badge
id: other-troopers-20-badge-hardware
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2020
makers:
- name: jeffmakes
  url: https://github.com/jeffmakes
summary: ESP32-WROVER badge with a 2.9" e-paper display designed for TROOPERS20, the Heilbronn security conference's 2020 edition, which was cancelled by COVID-19 before the badge could ship.
functions: Custom firmware menu system on the e-paper display; a joystick, buttons and touch input; haptic feedback; onboard sound; a CC1200 sub-GHz radio for wireless features; microSD storage; and a 6-pin SAO header for add-ons.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP32-WROVER
  leds:
    count: null
    type: WS2812B
    note: Successor to the TR19 badge, which used six WS2812B-mini LEDs; TODO notes in the repo mention buying SK6812s as a possible LED swap.
  display: 2.9" e-paper (GDEH029A1, 296x128, partial redraw)
  connectivity:
  - sub-ghz
  - uart
  - usb
  battery: LiPo, USB-C rechargeable (1500 mAh cell referenced in parts docs)
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: cancelled
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/jeffmakes/tr20-badge-hw
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/jeffmakes/tr20-badge-hw
  url: https://github.com/jeffmakes/tr20-badge-hw
  kind: repo
- label: 'Insinuator: Troopers 19 – Badge Hardware (predecessor)'
  url: https://insinuator.net/2019/07/troopers-19-badge-hardware/
  kind: article
images:
- file: assets/images/badges/other/troopers-20-badge-hardware/ef2c5cfff2.jpg
  source: https://github.com/jeffmakes/tr20-badge-hw
  credit: jeffmakes
  caption: 3D render of the TR20 badge PCB, top side
- file: assets/images/badges/other/troopers-20-badge-hardware/2bffe9dfe1.jpg
  source: https://github.com/jeffmakes/tr20-badge-hw
  credit: jeffmakes
  caption: 3D render of the TR20 badge PCB, bottom side
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- TROOPERS is an annual IT security conference in Germany (organized by SySS); TROOPERS20, the 2020 edition, was cancelled outright due to COVID-19 ("the hardest decision in TROOPERS history"), so this badge appears to have been designed but never distributed to attendees.
- No matching event id for TROOPERS exists yet in events.yml; left under "other".
- The repo's TODO.txt (checked 2026-09-07) shows an in-progress bring-up/test list for a revision 2 board — USB-C, e-paper, touch, haptics, ESP32, SD, buttons/joystick and LEDs are marked working, sound is marked failing, and radio TX is unconfirmed — consistent with a board that was still being validated when the event was cancelled.
- The predecessor, the TROOPERS19 badge (also by jeffmakes/Jeff), used an ESP32-WROVER, the same 2.9" GDEH029A1 e-paper display, six WS2812B-mini LEDs, a PCA9555/PCA9539 I2C keyboard, an LIS3DHTR accelerometer, and MicroPython firmware; about 600 were made. TR20 appears to expand on that design with a joystick, haptic driver (DRV2605L), a CC1200 sub-GHz radio, and microSD.
status: cancelled
sources:
- kind: url
  url: https://github.com/jeffmakes/tr20-badge-hw
  title: jeffmakes/tr20-badge-hw
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''troopers-2020''. Repo description: "Hardware design for the Troopers 20 badge". KiCad project with submodule libraries; docs/ folder contains datasheets for ESP32-WROVER, GDEH029A1 e-paper, CC1200 radio, DRV2605L haptics, LIS3DHTR accelerometer, PCA9555/PCA9539 IO expanders, PCM5100A/PAM8901 audio, CP2102N USB-serial, and a 1500 mAh LiPo cell.'
- kind: url
  url: https://raw.githubusercontent.com/jeffmakes/tr20-badge-hw/main/TODO.txt
  title: tr20-badge-hw TODO.txt
  accessed: '2026-09-07'
  note: Bring-up/test checklist for revision 2 of the board, listing which subsystems passed and failed testing.
- kind: url
  url: https://insinuator.net/2019/07/troopers-19-badge-hardware/
  title: Troopers 19 – Badge Hardware – Insinuator.net
  accessed: '2026-09-07'
  note: Background on the predecessor TR19 badge by the same maker (jeffmakes), used for comparison and context on the TR20 design.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Confirmed via the maker's own repo (KiCad hardware, docs folder with component datasheets, TODO.txt bring-up log) and background press on the predecessor TR19 badge. Could not find a firmware repository, a price, quantity made, or confirmation that any TR20 boards were physically assembled beyond revision 2 prototypes — TROOPERS20 was cancelled due to COVID-19, so this may never have been distributed. No TROOPERS event exists yet in events.yml; flagging troopers-2020 as a candidate new event id.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/troopers-20-badge-hardware.glb
  method: kicad
  source_file: r2/src/r2.kicad_pcb
  generated: '2026-09-10'
  bytes: 1154104
---

The TR20 badge is hardware designed by jeffmakes for TROOPERS20, the 2020 edition of the TROOPERS IT security conference held in Germany. It follows the same maker's TROOPERS19 badge — an ESP32-WROVER board with a 2.9" Good Display GDEH029A1 e-paper screen — but adds a joystick, touch input, a DRV2605L haptic driver, onboard sound, a CC1200 sub-GHz radio, and microSD storage, on top of the earlier accelerometer and USB-C charging. The design files live in a public KiCad repository, with a docs folder collecting datasheets for every part used, from the ESP32 module to the e-paper panel to the radio.

TROOPERS20 itself was cancelled outright due to the COVID-19 pandemic, described by the organizers as "the hardest decision in TROOPERS history." The repository's TODO.txt shows a revision-2 bring-up log with USB-C, the e-paper display, touch, haptics, the ESP32, SD card, buttons and joystick, and LEDs all marked as working, while sound testing had failed and sub-GHz radio transmission was unconfirmed — suggesting the board was still mid-validation when the event was called off. It is not clear whether any TR20 badges were ever assembled beyond prototypes or handed out to anyone.

## Make your own

Hardware is open: the `tr20-badge-hw` GitHub repository holds a KiCad project (with the maker's own component library plus Digikey/KiCad symbol and footprint libraries as git submodules) covering two board revisions (r1, r2), along with mechanical files for the badge's coverlay/case. No firmware repository was found, so software is not confirmed to be published.
