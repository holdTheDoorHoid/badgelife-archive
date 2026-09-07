---
title: DC25 HHV Reverse Engineering Challenge
id: dc25-hardware-hacking-village-dc25-re-challenge-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc25
year: 2017
makers:
- name: DCHHV (Hardware Hacking Village)
  url: https://github.com/DCHHV
summary: A locked reverse-engineering puzzle kit handed out at the DEF CON 25 Hardware Hacking Village, unlocked either by tracing the PCB or by finding the button/serial passcode.
functions: 'Two-stage RE challenge: (1) reverse-engineer the schematic from the bare PCB and bring it to the HHV for a small prize; (2) find the unlock code for the device itself. Unlocking is possible via an 8-digit code entered on four front buttons, or via the "unlockit" command over a 9600-baud serial pad on the board edge; a wrong 8-button entry triggers 10 seconds of red-LED blinking to slow brute-forcing, and a built-in "relock" sequence exists. A red herring version number printed at boot is the right digit-length to look like a code, with a small easter egg if entered.'
look:
  colors: []
  shape: rectangle
  themes:
  - puzzle
  - ctf
  - hardware tool
  - security
tech:
  mcu: PIC12F1572
  leds:
    count: 2
    type: discrete
    note: One green LED (lit solid when unlocked) and one red LED (blinks on wrong entries), both 5mm through-hole.
  display: none
  connectivity:
  - uart
  battery: coin cell (THM holder, cell size not specified)
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  - village
  where: Picked up in person at the DEF CON 25 Hardware Hacking Village; not sold.
make_your_own:
  open_source: true
  hardware_url: https://github.com/DCHHV/DC25_HHV_RE/tree/master/eagle
  firmware_url: https://github.com/DCHHV/DC25_HHV_RE/tree/master/DC25_HHV_RE.X
  gerbers_url: https://github.com/DCHHV/DC25_HHV_RE/tree/master/eagle
  bom_url: https://github.com/DCHHV/DC25_HHV_RE/blob/master/eagle/DC25_HHV_RE-A-BOM.txt
  eda_tool: Eagle
  license: MIT
  fab_url: null
  notes: Repo includes full Eagle schematic/board files, gerbers, BOM, production .hex firmware image, and a spoiler-heavy docs/writeup.txt explaining the intended solve paths and the actual unlock codes.
links:
- label: github.com/DCHHV/DC25_HHV_RE
  url: https://github.com/DCHHV/DC25_HHV_RE
  kind: repo
  archived: https://web.archive.org/web/20260907113102/https://github.com/DCHHV/DC25_HHV_RE
images: []
contact: {}
notes:
- BOM lists the microcontroller as "PIC12F1571"; the maker's own writeup.txt names it "PIC12F1572" (an 8-pin PIC12F157x family part either way). Kept both readings in tech and here rather than guessing which is the typo.
status: released
sources:
- kind: url
  url: https://github.com/DCHHV/DC25_HHV_RE
  title: Hardware Hacking Village DC25 RE Challenge Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON 25 (2017)''.'
  archived: https://web.archive.org/web/20260907113102/https://github.com/DCHHV/DC25_HHV_RE
- kind: url
  url: https://raw.githubusercontent.com/DCHHV/DC25_HHV_RE/master/README.md
  title: DC25_HHV_RE README
  accessed: '2026-09-07'
  note: Confirms it is a DEF CON 25 HHV reverse-engineering challenge kit, distributed as a kit at the village, with eagle/gerber hardware files and a hex firmware blob; describes the two-part challenge (schematic + unlock) and prize structure.
- kind: url
  url: https://raw.githubusercontent.com/DCHHV/DC25_HHV_RE/master/eagle/DC25_HHV_RE-A-BOM.txt
  title: DC25_HHV_RE-A-BOM.txt
  accessed: '2026-09-07'
  note: Bill of materials confirms PIC12F1571 MCU, one green and one red 5mm LED, four Omron B3F buttons, and a coin-cell battery holder (BAT-HLD-001-THM).
- kind: url
  url: https://raw.githubusercontent.com/DCHHV/DC25_HHV_RE/master/docs/writeup.txt
  title: DC25 HHV RE Challenge writeup (spoilers)
  accessed: '2026-09-07'
  note: Maker's own post-con writeup; source for the four buttons/serial unlock mechanism, the PIC12F1572 chip name, the 9600-baud serial pad, and the button/serial unlock codes and behavior.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No photo of the physical device was found anywhere in the repo (no images/ folder, no README screenshots) or via a general web search, so images could not be saved. Quantity made and exact battery cell size are not stated in any source. The repo names this a "challenge" kit handed out at the HHV rather than a wearable badge, so type was corrected from badge to kit; happy to revert if the community sheet meant something more badge-like by the title.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc25/hardware-hacking-village-dc25-re-challenge-badge.glb
  method: kicad
  source_file: DC25_HHV_RE-P1.brd
  generated: '2026-09-07'
  bytes: 108588
---

The DC25 HHV Reverse Engineering Challenge is a small locked puzzle board that the DEF CON 25 Hardware Hacking Village gave out in person in 2017. It follows on from a DC24 HHV RE challenge, but simplifies to a single main puzzle meant to mimic a "real-world" locked device. A PIC12F157x microcontroller reads four front-panel buttons through a resistor ladder and drives a red/green LED pair; entering the right 8-digit code on the buttons, or typing "unlockit" over an exposed 9600-baud serial pad, lights the green LED solid. Wrong attempts cost 10 seconds of red-LED blinking to slow brute forcing, and the board deliberately plants a red herring (a boot-time version string the same length as a valid code) along with a small easter egg for players who try it anyway.

Participants faced two tasks: first, reverse-engineer the bare PCB back into a schematic and bring it to the village for a small prize, then find the actual unlock code for a larger prize. The maker's own writeup documents several solve paths that were built into the firmware on purpose, including a side-channel timing leak in the button-compare routine and weaknesses in the serial command parser, alongside the straight brute-force route.

DCHHV published the full Eagle schematic and board files, gerbers, BOM, and the production firmware hex under the MIT license, along with a spoiler-filled writeup after the con. The kit was a free village giveaway rather than a sold item, and no photo of the assembled board turned up in the repository or elsewhere.

## Make your own

The repository at [github.com/DCHHV/DC25_HHV_RE](https://github.com/DCHHV/DC25_HHV_RE) has everything needed to rebuild the challenge: the `eagle/` folder holds the Eagle schematic, board file, and gerbers (plus a BOM) that can be sent to a fab house, and the top-level `.hex` file is the firmware image to program onto a PIC12F157x. `docs/writeup.txt` explains the intended solve paths and gives the actual unlock codes, so treat it as a spoiler if you want to solve the challenge yourself first.
