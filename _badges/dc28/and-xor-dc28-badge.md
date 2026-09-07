---
title: AND!XOR DC28 Badge
id: dc28-and-xor-dc28-badge
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
makers:
- name: AND!XOR
  url: https://hackaday.io/andxor
summary: 'An unofficial DEF CON 28 badge from AND!XOR, built as a text-adventure CTF console after DEF CON 28 itself went virtual and was distributed hand-to-hand through trusted hackers instead of a convention floor.'
functions: 'Runs an embedded text-based CTF adventure called BENDER~PISS, playable directly on the badge via its BlackBerry Q10 keyboard and dual displays. Includes a ported MyBASIC interpreter so owners can write and run their own code on the hardware. 60 possible flags spread across 21 main challenges, 3 bonus challenges, and 36 easter eggs. A "bling" mode drives RGB LED light effects.'
look:
  colors: [red, gold, black]
  shape: rectangle
  themes: [skull, cyberpunk, ctf, hardware tool]
tech:
  mcu: STM32F412RET6
  leds:
    count: null
    type: APA-102C
    note: 'RGB LEDs hidden beneath the laser-etched acrylic faceplate, driven over SPI.'
  display: '128x64 OLED and 160x128 color TFT (ST7735)'
  connectivity: [usb]
  inputs: [keyboard]
  battery: 3x AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'a few hundred'
  availability: sold_out
  availability_note: 'Not sold at retail; distributed via trusted-hacker "drops" after DEF CON 28 was cancelled. Checked 2026-09-07: no active storefront found.'
  distribution: [free_drop, purchase]
  where: 'Most badges were given away free through caches handed to trusted hackers in locations across North America, who awarded them to puzzle-solvers and active community members; some were sold to fund the run.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ANDnXOR/ANDnXOR_DC28_Badge
  firmware_url: https://github.com/ANDnXOR/ANDnXOR_DC28_Badge
  eda_tool: null
links:
- label: hackaday.io/project/173627-andxor-dc28-badge
  url: https://hackaday.io/project/173627-andxor-dc28-badge
  kind: hackaday
- label: 'GitHub: ANDnXOR/ANDnXOR_DC28_Badge'
  url: https://github.com/ANDnXOR/ANDnXOR_DC28_Badge
  kind: repo
- label: 'Hackaday: Hands-On: AND!XOR Unofficial DC28 Badge Embraces The Acrylic Stackup'
  url: https://hackaday.com/2020/08/07/hands-on-andxor-unofficial-dc28-badge-embraces-the-acrylic-stackup/
  kind: article
images:
  - file: assets/images/badges/dc28/and-xor-dc28-badge/f91d375588.jpg
    source: "https://hackaday.io/project/173627-andxor-dc28-badge"
    credit: "AND!XOR"
    caption: "AND!XOR DC28 badge, front, with acrylic stackup and OLED/LCD displays"
  - file: assets/images/badges/dc28/and-xor-dc28-badge/a09e97f68f.jpg
    source: "https://hackaday.io/project/173627-andxor-dc28-badge"
    credit: "AND!XOR"
    caption: "AND!XOR DC28 badge detail"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/173627-andxor-dc28-badge
  title: AND!XOR DC28 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 28''.'
- kind: url
  url: https://hackaday.io/project/173627-andxor-dc28-badge
  title: AND!XOR DC28 Badge
  accessed: '2026-09-07'
  note: 'Maker project page; confirmed chip, displays, LEDs, keyboard, distribution plans, GitHub repo link.'
- kind: url
  url: https://github.com/ANDnXOR/ANDnXOR_DC28_Badge
  title: 'ANDnXOR/ANDnXOR_DC28_Badge'
  accessed: '2026-09-07'
  note: 'Confirmed open-source hardware/firmware repo for the badge.'
- kind: url
  url: https://hackaday.com/2020/08/07/hands-on-andxor-unofficial-dc28-badge-embraces-the-acrylic-stackup/
  title: 'Hands-On: AND!XOR Unofficial DC28 Badge Embraces The Acrylic Stackup'
  accessed: '2026-09-07'
  note: 'Third-party hands-on review; confirmed look/colors (red PCB, gold-mirrored acrylic, laser-etched skull/gear face), APA-102 LEDs, USB-C mass storage, quantity ("a few hundred"), and free-drop distribution model.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Price and exact LED count not stated by any source found; left empty. sao_version and sao_ports not applicable/found (no SAO header mentioned). Some sources say USB-C, others just USB; recorded as usb pending clarity on connector type.'
last_modified_date: '2026-09-07'
---

AND!XOR is a hacker collective known for a long-running series of unofficial DEF CON badges. When DEF CON 28 went virtual in 2020 due to the pandemic, the team built this badge anyway and solved the distribution problem by handing caches of them to trusted hackers across North America, who in turn gave badges to puzzle-solvers and active community members rather than selling them from a convention table. A few hundred were made in total, with some sold to help fund the run.

The badge is built around an STM32F412RET6 microcontroller, a BlackBerry Q10 mechanical keyboard, and a dual-display setup (a 128x64 OLED alongside a 160x128 color TFT), all housed under a double stack-up of laser-etched acrylic over a red PCB with a "mirrored gold" finish depicting a skull half-covered by a gear-themed mask. APA-102C RGB LEDs hidden beneath the faceplate provide a "bling" lighting mode, driven over SPI rather than through a dedicated LED driver chip.

On the software side, the badge runs an original text-adventure CTF called BENDER~PISS, playable entirely on-device through the keyboard and screens, spread across 21 main challenges, 3 bonus challenges, and 36 easter eggs for 60 possible flags. AND!XOR also ported the MyBASIC interpreter to the hardware so owners could write and run their own code. Hardware and firmware are published on GitHub.
