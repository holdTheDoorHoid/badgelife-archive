---
title: DEF CON 25 Darknet Badge
id: dc25-darknet-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: Krux
  url: https://krux.org/darknet/
  role: hardware design
- name: Cmdc0de
  role: firmware
summary: A round, rotary-phone-styled kit badge for the DarkNet contest at DEF CON 25, used to pair with other badges over radio and step through in-person "quest" challenges.
functions: Pairs with other Darknet badges over a 915MHz radio link and IR, runs a menu system (address book, "DCDN" net messages, radio info, keyboard test, quest dialing, gateway) on its color LCD; the ten numbered pads are capacitive-touch buttons used like a phone dial/keypad for the contest's challenges.
look:
  colors: [red, gold]
  shape: circle
  themes: [retro computer, puzzle, ctf, security, radio, wearable]
tech:
  mcu: STM32F302 (ARM Cortex-M4)
  leds:
    count: 11
    type: discrete
    note: One 5mm Vishay IR LED plus ten SMD OSRAM yellow LEDs that backlight the copper number/letter cutouts on the dial pads.
  display: color LCD (SPI, 8-pin header)
  connectivity: [ir, sub-ghz]
  inputs: [touch]
  power: LiPo battery via JST connector, power switch
  battery: LiPo 2000mAh (PKCELL LP803960), JST connector
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: Checked 2026-09-07; sold at DEF CON 25 (2017), no longer offered.
  distribution: [purchase, contest]
  where: Sold at DEF CON 25 as a kit; those who solved a pre-con online "casefile" challenge could buy in 2 hours early, ahead of general conference sale. Reported to have sold out within hours.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/thedarknet/defcon25-badge
  firmware_url: https://github.com/thedarknet/defcon25-badge
  gerbers_url: https://oshpark.com/profiles/Krux
  bom_url: null
  eda_tool: null
  license: MIT
  fab_url: https://oshpark.com/profiles/Krux
  notes: GitHub repo (thedarknet/defcon25-badge, MIT license) holds hardware and firmware source together, developed with GNU ARM Eclipse and OpenOCD. Assembly walkthrough published separately by the maker.
links:
- label: oshpark.com/profiles/Krux
  url: https://oshpark.com/profiles/Krux
  kind: fab
- label: thedarknet/defcon25-badge (GitHub)
  url: https://github.com/thedarknet/defcon25-badge
  kind: repo
- label: DarkNet 2017 Badge Kit assembly guide (krux.org)
  url: https://krux.org/darknet/2017/index.html
  kind: doc
- label: All The Hardware Badges Of DEF CON 25 (Hackaday)
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  kind: article
images:
- file: assets/images/badges/dc25/darknet-badge/f8ac050769.jpg
  source: "https://krux.org/darknet/2017/index.html"
  credit: "Krux"
  caption: "Assembled DEF CON 25 Darknet badge, rotary-phone layout, showing the LCD main menu"
- file: assets/images/badges/dc25/darknet-badge/25421896d2.jpg
  source: "https://krux.org/darknet/2017/index.html"
  credit: "Krux"
  caption: "Unassembled DEF CON 25 Darknet badge kit: PCB, LiPo battery, LCD, radio module, IR LED, hardware"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://oshpark.com/profiles/Krux
  title: DEF CON 25 Darknet Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc25''.'
- kind: url
  url: https://github.com/thedarknet/defcon25-badge
  title: "thedarknet/defcon25-badge: Badge Related items for defcon 25"
  accessed: '2026-09-07'
  note: Confirmed STM32 MCU family, MIT license, hardware+firmware repo, dev tooling (GNU ARM Eclipse, OpenOCD).
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: All The Hardware Badges Of DEF CON 25
  accessed: '2026-09-07'
  note: Maker (Krux), rotary-phone design with capacitive-touch dial pads and back-mounted LEDs, kit-built, casefile early-purchase mechanic, sold out fast.
- kind: url
  url: https://krux.org/darknet/2017/index.html
  title: DefCon DarkNet 2017 Badge Kit
  accessed: '2026-09-07'
  note: Maker's own assembly guide; exact MCU (STM32F302), LED counts/types, RFM69HCW-915S2 radio, LCD module, LiPo battery, kit parts list, and source photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Firmware credited to Cmdc0de per Hackaday/search coverage but not independently confirmed on a maker page in this pass. Exact unit price and quantity made were not found in any source checked; secondhand listings (Worthpoint) exist but were not used as they carry no verifiable maker-sourced facts and one could not be fetched (403). Badge is part of the recurring DarkNet/DCDN series (see later years dc26 "DC26 Darknet Industries Badge", dc30-dc34 entries already in the archive) — series name not set here since sources for this specific year did not use one consistently.
last_modified_date: '2026-09-07'
---

The DEF CON 25 Darknet badge was the kit-built centerpiece of DarkNet, DEF CON's long-running "Daemon"/"Freedom"-inspired contest, where players ("agents") pair badges over radio and infrared, build address books, and work through quests and ciphers to earn reputation. Designed by Krux with firmware by Cmdc0de, the board is laid out as a red rotary phone: the ten dial positions are capacitive-touch pads with cutouts in the copper that let back-mounted LEDs shine the numbers and letters through, and a small color LCD in the center runs the badge's menu system (address book, net messages, radio info, quest dialing, and more), driven by an STM32F302 ARM Cortex-M4 microcontroller.

Badges shipped as unassembled kits — PCB, LiPo battery, LCD module, an RFM69HCW 915MHz radio, an IR LED/receiver pair, SMD LEDs, and mounting hardware — that buyers had to solder themselves, continuing DarkNet's tradition of teaching soldering as part of the challenge. Anyone who solved a pre-conference online "casefile" puzzle got a two-hour early purchase window before the badge went on general sale to conference attendees; it reportedly sold out within hours either way.

## Make your own

Hardware and firmware are published together at github.com/thedarknet/defcon25-badge under the MIT license, developed using GNU ARM Eclipse with OpenOCD for flashing/debugging (a Nucleo-F302R8 dev board stood in for the badge's MCU during development). Board files are also shared on OSH Park under the maker's Krux profile. The maker's own site hosts a full photographed assembly walkthrough for the 2017 kit.
