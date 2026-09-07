---
title: Hardware Hacking Village DC26 RE Challenge Badge
id: dc26-hardware-hacking-village-dc26-re-challenge-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: DCHHV (Hardware Hacking Village)
summary: A small reverse-engineering puzzle board handed out at the DEF CON 26 Hardware Hacking Village, built around an ATtiny84 and a mystery second IC.
functions: Two linked challenges. Enter the right passcode on the four onboard buttons (A, B, C, D) to light the middle green LED and print a flag over serial. Separately, figure out and manipulate the board's second IC (undocumented on purpose) to light the bottom green LED.
look:
  colors:
  - green
  shape: rectangle
  themes:
  - village badge
  - puzzle
  - ctf
  - hardware tool
tech:
  mcu: ATtiny84
  leds:
    count: 3
    type: discrete
    note: One red status LED plus two green challenge-complete LEDs (middle LED for the passcode puzzle, bottom LED for the second-IC puzzle).
  display: none
  connectivity:
  - uart
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed to attendees at the DEF CON 26 Hardware Hacking Village (2018); exact distribution method (kit vs. pre-assembled, free vs. paid) is not stated in the available sources.
make_your_own:
  open_source: true
  hardware_url: https://github.com/DCHHV/DC26_HHV_RE/tree/master/Hardware
  firmware_url: https://github.com/DCHHV/DC26_HHV_RE/tree/master/Firmware
  eda_tool: null
  license: MIT
  notes: Repo includes Eagle .brd/.sch files, gerbers, a schematic PDF, and both an obfuscated and a readable Arduino sketch (the obfuscated version is what shipped, to keep the challenge intact).
links:
- label: github.com/DCHHV/DC26_HHV_RE
  url: https://github.com/DCHHV/DC26_HHV_RE
  kind: repo
images:
- file: assets/images/badges/dc26/hardware-hacking-village-dc26-re-challenge-badge/5f905c411d.jpg
  source: https://github.com/DCHHV/DC26_HHV_RE
  credit: DCHHV
  caption: Assembled DC26 HHV RE Challenge board, annotated with component values
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/DCHHV/DC26_HHV_RE
  title: Hardware Hacking Village DC26 RE Challenge Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 26 (2018)''.'
- kind: url
  url: https://github.com/DCHHV/DC26_HHV_RE
  title: DCHHV/DC26_HHV_RE README and repo contents
  accessed: '2026-09-07'
  note: Read README for challenge mechanics, MCU, license, and programming instructions; browsed the Hardware and images directories for schematics, gerbers, and the annotated assembly photo used above.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (event, year, MCU, challenge mechanics, license) confirmed from the maker's own GitHub repo and README. Price, quantity made, and exact distribution terms (free vs. paid, kit vs. assembled) are not stated anywhere in the repo and were left blank rather than guessed. No third-party coverage (Hackaday, forums, etc.) was found to cross-check or supplement. No photo of an unassembled or in-the-wild board was found beyond the annotated assembly diagram used here.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc26/hardware-hacking-village-dc26-re-challenge-badge.glb
  method: kicad
  source_file: DC26_HHV_challenge.brd
  generated: '2026-09-07'
  bytes: 130060
---

The DC26 HHV RE Challenge is a small reverse-engineering puzzle board built for the Hardware Hacking Village at DEF CON 26 (2018). It centers on an ATtiny84 microcontroller and a second, deliberately undocumented IC, and poses two separate challenges: entering a hidden passcode on four buttons (A, B, C, D) to unlock a green LED and a serial-printed flag, and independently working out how the mystery second chip is wired in to trigger a second green LED. A red status LED gives programming/activity feedback. The board runs off a coin cell and is programmed via ISP test points on the back, with a solder-bridge jumper used to put it into programming mode.

DCHHV published the full project as open hardware under the MIT license, including Eagle schematics and board files, gerbers, and firmware. The firmware ships in two forms — a readable version and an obfuscated one — so that flashing or reading the source doesn't spoil the puzzle for anyone rebuilding their own copy. mediumrehr is credited in the README as the point of contact for hints or bug reports.

No pricing, production quantity, or independent (non-maker) coverage of the badge was found; those fields are left empty rather than guessed.
