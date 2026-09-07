---
title: Vectrex SAO
id: supercon-2022-vectrex-sao-2
layout: badge
parent: Supercon 2022
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2022
year: 2022
makers:
- name: Brett Walach (Technobly)
  url: https://hackaday.io/hacker/486036-brett-walach
summary: A miniature playable Vectrex console SAO running a low-res version of Scramble on a 7x10 charlieplexed white LED display, with a PIC16F886 MCU, speaker, one-button capacitive-touch controller on a hand-made coiled cord, and I2C/PWM jumpers for badge integration; made for Hackaday Supercon 2022 and later entered in the Supercon 8 SAO Contest (2024).
functions: 'Plays a mini low-resolution version of the arcade game Scramble; auto-muting speaker (can be permanently disabled by removing a solder blob); saves high score permanently; I2C jumpers and a PWM speaker input plus touch-sensor output let a host badge control it directly.'
look:
  colors: [white, black]
  shape: null
  themes: [retro computer, console, arcade, video game]
tech:
  mcu: PIC16F886
  leds:
    count: 70
    type: charlieplexed
    note: 7x10 white LED matrix, mounted at a slight angle to mimic Vectrex box-art perspective
  display: none
  connectivity: [i2c]
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/technobly/vectrex-sao
  firmware_url: https://github.com/technobly/vectrex-sao
  gerbers_url: https://github.com/technobly/vectrex-sao/tree/master/gerbers
  bom_url: https://github.com/technobly/vectrex-sao/tree/master/bom
  eda_tool: KiCad
  license: CC BY-SA 4.0
  fab_url: null
  notes: BOM and CPL CSVs are formatted for direct upload to JLCPCB; repo includes a build guide for the hand-wound coiled-cord controller cable.
links:
- label: hackaday.io/project/197854-vectrex-sao
  url: https://hackaday.io/project/197854-vectrex-sao
  kind: hackaday
- label: github.com/technobly/vectrex-sao
  url: https://github.com/technobly/vectrex-sao
  kind: repo
- label: youtu.be/AfYQyKARwps
  url: https://youtu.be/AfYQyKARwps
  kind: video
images:
  - file: assets/images/badges/supercon-2022/vectrex-sao-2/086e25ad00.jpg
    source: "https://github.com/technobly/vectrex-sao"
    credit: "Brett Walach (Technobly)"
    caption: "The Vectrex SAO console board with charlieplexed LED display and coiled-cord controller"
  - file: assets/images/badges/supercon-2022/vectrex-sao-2/0be1d12b8f.png
    source: "https://hackaday.io/project/197854-vectrex-sao"
    credit: "Brett Walach (Technobly)"
    caption: "Vectrex SAO project photo on Hackaday.io"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197854-vectrex-sao
  title: Vectrex SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/197854-vectrex-sao
  title: Vectrex SAO
  accessed: '2026-09-07'
  note: Confirmed maker (Brett Walach / Technobly), that it was made for Hackaday Supercon 2022 and later entered in the Supercon 8 SAO Contest (project page dated Sept 2024), MCU, display, controller, speaker, and open-source status; no price/quantity/availability info given.
- kind: url
  url: https://github.com/technobly/vectrex-sao
  title: "GitHub: technobly/vectrex-sao"
  accessed: '2026-09-07'
  note: Primary source for hardware details (PIC16F886, 7x10 charlieplexed LEDs, I2C jumpers, PWM/touch lines, 1.0mm PCBs), open-source license (CC BY-SA 4.0), BOM/gerbers/KiCad files, and coiled-cord construction guide with photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own GitHub repo and Hackaday.io project page confirm all core technical facts. No pricing, quantity made, or distribution/availability details were found anywhere (this looks like a one-off/small-batch conference give or personal project rather than a sold product); those fields are left empty rather than guessed. tech.sao_version and look.shape were not stated by the maker and are left null.
last_modified_date: '2026-09-07'
---

Brett Walach (Technobly) built the Vectrex SAO as a tiny, playable homage to the classic Vectrex vector-graphics console for Hackaday Supercon 2022. In place of a real vector display it uses a 7x10 charlieplexed white LED matrix mounted at a slight angle to echo the console's box-art perspective, driven by a PIC16F886 microcontroller that Walach had pulled from a salvaged reel of parts. It plays a stripped-down, low-resolution version of the arcade game Scramble, controlled by a single-button capacitive-touch joystick wired through a hand-wound coiled silicone cord that the maker describes as "an absolute pain to make." A small speaker provides sound and auto-mutes when the game isn't running, with an option to disable it permanently by removing a solder blob; the badge also saves the player's high score permanently.

The SAO is designed to talk to a host badge over I2C, and exposes extra jumpers so a host can drive it directly, including a PWM input for the speaker and a touch-sensor output for reading button presses. Hardware and firmware are fully open source under CC BY-SA 4.0, with KiCad schematics/PCB files, Gerbers for both the console and controller boards, and BOM/CPL CSVs formatted for direct JLCPCB ordering, all published on GitHub.

The Hackaday.io project page is dated September 2024, when Walach entered the design in the Supercon 8 SAO Contest, but the project itself and its GitHub repo state it was made for Supercon 2022. No information on units produced, pricing, or how (or whether) it was distributed to attendees turned up in any source checked.

## Make your own

The GitHub repo (github.com/technobly/vectrex-sao) has everything needed to build one: KiCad source files, Gerbers for the two boards (console and controller) in the `gerbers/` folder, and BOM/CPL CSVs in `bom/` pre-formatted for JLCPCB assembly. A separate step-by-step guide with photos walks through hand-winding the coiled silicone-wire cord that connects the controller to the main board.
