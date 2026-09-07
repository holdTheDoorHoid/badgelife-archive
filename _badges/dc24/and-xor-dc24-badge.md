---
title: AND!XOR DC24 Badge
id: dc24-and-xor-dc24-badge
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc24
year: 2016
makers:
- name: AND!XOR
  url: https://shop.andnxor.com/
summary: An unofficial, hackable electronic badge AND!XOR made for DEF CON 24, nicknamed "Bender," built as an open dev board with an OLED screen, RGB LEDs, and a 433 MHz radio for badge-to-badge interaction.
functions: Runs 14 LED animations, exposes a terminal shell over serial/USB, and uses its RFM69W radio for wireless badge-to-badge social/networking features.
look:
  colors: [black, white]
  shape: null
  themes: [robot, sci-fi, hardware tool]
tech:
  mcu: STM32F103CBT6
  leds:
    count: 8
    type: WS2812B
    note: Surface-mount RGB LEDs.
  display: 0.96" OLED (SSD1306, 128x64)
  connectivity: [sub-ghz]
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'about 170 (100 white, 20 black, 50 LED-only "bling" variants)'
  availability: sold_out
  distribution: [purchase]
  where: Sold at DEF CON 24 (2016) by AND!XOR.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ANDnXOR/ANDnXOR_DC24_Badge
  firmware_url: https://github.com/ANDnXOR/ANDnXOR_DC24_Badge
  eda_tool: null
  license: Apache-2.0
  notes: dodgymike's github.com/dodgymike/ANDnXOR_DC24_Badge repo (the entry's original source) is a fork of the maker's own github.com/ANDnXOR/ANDnXOR_DC24_Badge repo.
links:
- label: github.com/dodgymike/ANDnXOR_DC24_Badge
  url: https://github.com/dodgymike/ANDnXOR_DC24_Badge
  kind: repo
- label: github.com/ANDnXOR/ANDnXOR_DC24_Badge
  url: https://github.com/ANDnXOR/ANDnXOR_DC24_Badge
  kind: repo
- label: AND!XOR DEFCON 24 Badge (Hackaday.io)
  url: https://hackaday.io/project/9064-andxor-defcon-24-badge
  kind: hackaday
- label: "Hands-on: The AND!XOR Unofficial DEF CON Badge (Hackaday)"
  url: https://hackaday.com/2016/07/25/hands-on-the-andxor-unofficial-def-con-badge/
  kind: article
images:
  - file: assets/images/badges/dc24/and-xor-dc24-badge/079965719f.jpg
    source: "https://hackaday.io/project/9064-andxor-defcon-24-badge"
    credit: "AND!XOR"
    caption: "AND!XOR DEF CON 24 badge (Bender design)"
  - file: assets/images/badges/dc24/and-xor-dc24-badge/8a1c8b20a7.jpg
    source: "https://hackaday.io/project/9064-andxor-defcon-24-badge"
    credit: "AND!XOR"
    caption: "AND!XOR DEF CON 24 badge PCB"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/dodgymike/ANDnXOR_DC24_Badge
  title: AND!XOR DC24 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''DEF CON 24''. This is a fork of the maker''s own repo.'
- kind: url
  url: https://github.com/ANDnXOR/ANDnXOR_DC24_Badge
  title: "ANDnXOR/ANDnXOR_DC24_Badge: AND!XOR DEFCON 24 Badge HW and SW"
  accessed: '2026-09-07'
  note: The maker's original repo (dodgymike's is a fork); confirms Apache-2.0 license and DFU flashing steps.
- kind: url
  url: https://hackaday.io/project/9064-andxor-defcon-24-badge
  title: AND!XOR DEFCON 24 Badge | Hackaday.io
  accessed: '2026-09-07'
  note: Primary source for maker (AND!XOR, three-person team), MCU, OLED, LED count/type, radio, quantities made, and event/year.
- kind: url
  url: https://hackaday.com/2016/07/25/hands-on-the-andxor-unofficial-def-con-badge/
  title: "Hands-on: The AND!XOR Unofficial DEF CON Badge"
  accessed: '2026-09-07'
  note: Press coverage confirming the badge as an unofficial DEF CON 24 badge with LEDs, RF, and OLED.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all four cited sources. Core facts (maker team, MCU, OLED, LED count/type, RFM69W 433MHz radio, 14 animations, ~170-unit quantity breakdown, Apache-2.0 license, DFU flashing steps) are directly confirmed on the maker''s own Hackaday.io project page and ANDnXOR/ANDnXOR_DC24_Badge GitHub repo, and corroborated by the Hackaday.com article. Two corrections made: (1) removed maker entry "dodgymike (hardware/software contributor)" — no source states dodgymike contributed to the badge or the AND!XOR team; GitHub confirms the dodgymike repo is only a fork of the maker''s repo, which does not establish authorship or contribution, so this was an invented credit and has been removed (the fork relationship is still noted in make_your_own.notes and kept as a source). (2) tech.connectivity changed from "radio" to "sub-ghz" to match the guide''s controlled vocabulary (RFM69W is a 433MHz sub-GHz radio). Both saved images were confirmed present in assets/ and visually match Bender-shaped AND!XOR DC24 badges (OLED, WS2812B LEDs, spring antenna) consistent with their cited Hackaday.io source page. Battery/power type, exact unit price, and shape/theme details beyond the "Bender" robot design remain unstated in the sources checked and are correctly left empty (the Hackaday.com article does mention a planned $40/$20 price, but that was not added since this pass is fact-checking existing content, not new research). Everything remaining in the entry is source-supported, so status is set to verified.'
last_modified_date: '2026-09-07'
---

AND!XOR — a three-person hardware/software team from California — built the AND!XOR DEF CON 24 badge as an unofficial, hackable badge for attendees of DEF CON 24 in Las Vegas (August 2016). Nicknamed "Bender," it doubled as an open dev board: an STM32F103CBT6 ARM Cortex-M3 microcontroller drives a 0.96" SSD1306 OLED display and eight surface-mount WS2812B RGB LEDs through 14 built-in animations, while an RFM69W 433 MHz radio let badges talk to each other for social/networking features. A terminal shell reachable over serial/USB rounded out the hacking surface.

The team produced roughly 170 units for the con — about 100 white PCBs, 20 black PCBs, and 50 stripped-down LED-only "bling" variants — sold on-site at DEF CON 24. Hardware and firmware were released as open source under the Apache-2.0 license on GitHub, including Gerbers and provisioning tools; badges can be reflashed over USB in DFU mode.

## Make your own

Hardware (Gerbers, schematic) and firmware are published at github.com/ANDnXOR/ANDnXOR_DC24_Badge under Apache-2.0. To reflash a badge, hold "Down" while connecting USB (or while pressing reset) to enter DFU mode — a red LED near the AND!XOR DEFCON 24 silkscreen confirms it — then flash with `dfu-util -D Provision/ANDnXOR_Badge-Human.bin -a 2`.
