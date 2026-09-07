---
title: Dupe SAO
id: other-dupe-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: deshipu
  url: https://github.com/deshipu
summary: A fan-made SAO shaped like a duplicant from Klei Entertainment's "Oxygen Not Included", with a small round display that shows the character's face blinking and moving.
functions: 'Drives a round LCD as an animated face: idle blink/look animation of the duplicant character.'
look:
  colors:
  - white
  shape: null
  themes:
  - pop culture
  - video game
tech:
  mcu: CH32V203
  leds: null
  display: 0.99" round LCD (GC0907 12-pin v1 / GC9107 8-pin v2)
  connectivity: []
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
  open_source: 'yes'
  hardware_url: https://github.com/deshipu/dupe-sao/tree/main/pcb
  firmware_url: https://github.com/deshipu/dupe-sao/tree/main/code
  eda_tool: EasyEDA
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
images:
- file: assets/images/badges/other/dupe-sao/0bc159f7ba.jpg
  source: "https://github.com/deshipu/dupe-sao"
  credit: "deshipu"
  caption: "Duplicant SAO with round display showing the duplicant's face"
status: released
sources:
- kind: url
  url: https://github.com/deshipu/dupe-sao
  title: Dupe SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/deshipu/dupe-sao/main/README.md
  title: 'dupe-sao: README.md'
  accessed: '2026-09-07'
  note: Main project description, disclaimer that it is a fan project and not for sale, two hardware revisions (v1/v2 displays).
- kind: url
  url: https://raw.githubusercontent.com/deshipu/dupe-sao/main/code/README.md
  title: 'dupe-sao: code/README.md'
  accessed: '2026-09-07'
  note: Confirms MCU is CH32V203 (RISC-V), firmware built with a Makefile and the xpack riscv toolchain.
- kind: url
  url: https://raw.githubusercontent.com/deshipu/dupe-sao/main/pcb/README.md
  title: 'dupe-sao: pcb/README.md'
  accessed: '2026-09-07'
  note: PCB designed in EasyEDA, JLCPCB-ready, maker recommends white PCB.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    No event or year is named anywhere in the repository; this appears to be a personal/fan project
    rather than a badge made for a specific convention, so it is left under event "other". The maker
    explicitly says "I'm not selling this" but publishes full hardware (EasyEDA/Gerbers via JLCPCB)
    and firmware (CH32V203, RISC-V) so others can get it fabricated themselves; treated as availability
    "unknown" rather than a distribution channel. SAO connector pin count (4-pin vs 6-pin) is not
    stated. Board/solder-mask color is only inferred from the maker's own recommendation ("I recommend
    using white PCB"), not confirmed from a photo of a specific unit.
last_modified_date: '2026-09-07'
---

The Dupe SAO is a small add-on board for electronic conference badges, shaped after a duplicant — the little worker character from Klei Entertainment's colony-management game *Oxygen Not Included*. Instead of static art, the character's round helmet is an actual display: a CH32V203 RISC-V microcontroller drives a 0.99" round LCD to show the duplicant's face with a subtle blink-and-look idle animation. Two hardware revisions exist that differ only in which round-display module they carry (a 12-pin GC0907 panel for v1, an 8-pin GC9107 panel for v2); both run the same firmware.

Maker deshipu built this as an unofficial fan project and is explicit that it is not licensed by or affiliated with Klei, and that they are not selling finished units. Instead, the full PCB design (EasyEDA source and schematic, ready to order from JLCPCB), the artwork, and the firmware source are published on GitHub so that anyone who wants one can have it fabricated and assembled themselves — the README notes some fab houses can even flash the firmware for you, otherwise a dedicated RISC-V programmer is needed.

## Make your own

The `pcb/` folder holds EasyEDA project files (openable via easyeda.com's online editor) for both the v1 and v2 boards, plus a schematic PDF, and can be sent straight to JLCPCB fabrication from within EasyEDA (the maker recommends a white PCB). The `code/` folder is a CH32V203 firmware project built with a standard Makefile and the xpack RISC-V toolchain, with vendor peripheral code from OpenWCH's CH32V307 SDK. The `artwork/` folder has the source art and a Python export script used to generate the face animation frames.
