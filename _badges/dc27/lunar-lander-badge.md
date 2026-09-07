---
title: Lunar Lander Badge
id: dc27-lunar-lander-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Kate Morris
  url: https://hackaday.io/kate-morris
- name: Rowan Phipps
  url: https://hackaday.io/rowan-phipps
summary: 'An independent DEF CON 27 badge shaped like a rocket, built around an ESP32 with a TFT screen, that plays a Lunar Lander game to mark the 50th anniversary of Apollo 11.'
functions: 'Plays a Lunar Lander landing-simulator game and includes "some puzzles" on its TFT screen; drives a companion SAO with flashing LEDs over the badge''s SAO port.'
look:
  colors: []
  shape: rocket
  themes:
  - space
  - sci-fi
  - puzzle
tech:
  mcu: ESP32
  leds:
    count: 7
    type: null
    note: 'Seven LEDs on the main badge, plus additional flashing LEDs on the companion Lunar Lander SAO.'
  display: TFT LCD (SPI)
  connectivity:
  - i2c
  battery: LiPo (3.2-4.2V, built-in charging circuit; shipped uncharged)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  distribution:
  - crowdfunding
  where: 'Funded via Kickstarter for DEF CON 27 (2019) and shipped to backers; the campaign is closed and there is no current storefront.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/lunarbadge/LunarBadgeDC27
  firmware_url: https://github.com/lunarbadge/LunarBadgeDC27
  eda_tool: null
links:
- label: hackaday.io/project/165774-lunar-lander-badge
  url: https://hackaday.io/project/165774-lunar-lander-badge
  kind: hackaday
- label: lunarbadge.github.io
  url: https://lunarbadge.github.io
  kind: website
- label: github.com/lunarbadge/LunarBadgeDC27
  url: https://github.com/lunarbadge/LunarBadgeDC27
  kind: repo
- label: github.com/lunarbadge/LunarLanderSAO
  url: https://github.com/lunarbadge/LunarLanderSAO
  kind: repo
images:
- file: assets/images/badges/dc27/lunar-lander-badge/d184e3d9b9.jpg
  source: "https://hackaday.io/project/165774-lunar-lander-badge"
  credit: "Kate Morris / Rowan Phipps"
  caption: "Lunar Lander Badge project photo"
- file: assets/images/badges/dc27/lunar-lander-badge/3c0f920497.png
  source: "https://lunarbadge.github.io"
  credit: "Kate Morris / Rowan Phipps"
  caption: "Lunar Lander Badge with SAO attached"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/165774-lunar-lander-badge
  title: Lunar Lander Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/165774-lunar-lander-badge
  title: Lunar Lander Badge - Hackaday.io project page
  accessed: '2026-09-07'
  note: 'Confirmed makers (Kate Morris, Rowan Phipps), DEF CON 27 / 2019 origin, and og:image used for the first saved photo.'
- kind: url
  url: https://lunarbadge.github.io
  title: Lunar Lander Badge project site
  accessed: '2026-09-07'
  note: 'Confirmed Apollo 11 50th-anniversary theme, Lunar Lander game plus puzzles, companion SAO with flashing LEDs, and the withSAO.png image.'
- kind: url
  url: https://github.com/lunarbadge/LunarBadgeDC27
  title: lunarbadge/LunarBadgeDC27
  accessed: '2026-09-07'
  note: 'Confirmed ESP32 (Adafruit Feather form factor) MCU, SPI TFT LCD, seven LEDs, five buttons, LiPo battery with charging circuit, and keyed SAO port (I2C + 2 GPIO); no license file noted so open-source status recorded as partial.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event, hardware) confirmed from the maker''s own Hackaday.io project, project website, and GitHub repo. Price and quantity made were not stated anywhere found (it was Kickstarter-backer-only); left empty. No license file was found in the hardware/firmware repo, so open_source is recorded as partial rather than yes. A separate companion accessory, the Lunar Lander SAO (github.com/lunarbadge/LunarLanderSAO), is linked from the same project but not created as its own archive entry per instructions.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/lunar-lander-badge/
---

The Lunar Lander Badge is an independent conference badge made by Kate Morris and Rowan Phipps for DEF CON 27 in 2019, timed to the 50th anniversary of the Apollo 11 moon landing. Shaped like a rocket, it runs on an ESP32 (in an Adafruit Feather form factor) driving a small SPI TFT LCD screen, and plays a Lunar Lander-style landing simulator along with some additional puzzles. Five buttons handle input, seven LEDs add blinky accents, and a LiPo battery with onboard charging circuitry powers the board (it shipped to backers uncharged).

The badge carries a keyed SAO port exposing I2C plus two spare GPIO pins, and the team designed a companion "Lunar Lander SAO" with its own flashing LEDs to plug into it. The project was funded and distributed through a Kickstarter campaign rather than a general storefront; that campaign is long closed, and no current way to buy one was found.

Hardware and firmware are published on GitHub (schematic PDF, pinout header, and Arduino/ESP32-native C++ firmware built on FreeRTOS), though no license file was located in the repository, so the project is recorded here as partially open source rather than fully so.
