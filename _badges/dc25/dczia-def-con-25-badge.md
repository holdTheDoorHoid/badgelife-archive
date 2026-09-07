---
title: DCZia DEF CON 25 badge
id: dc25-dczia-def-con-25-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
series: DCZia
makers:
- name: DCZia
  url: https://dczia.net/about.html
summary: A shield for the Arduino 101 with four Cherry MX Blue mechanical keyboard switches, a 16x2 character LCD, and NeoPixel RGB LEDs.
functions: Four clicky Cherry MX Blue mechanical keys drive inputs, with a 16x2 character LCD and NeoPixel RGB LEDs for status/output; runs as a shield on top of an Arduino 101 board.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - retro computer
tech:
  mcu: Arduino 101
  leds:
    count: null
    type: NeoPixel
    note: ''
  display: 16x2 character LCD
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 290 boards plus 10 prototypes
  availability: unknown
  distribution:
  - preorder
  where: Pre-sales were coordinated through 801 Labs hackerspace in Salt Lake City ahead of DEF CON 25.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/dczia/Defcon25-Badge
  firmware_url: https://github.com/dczia/Defcon25-Badge
  eda_tool: null
links:
- label: github.com/dczia/Defcon25-Badge
  url: https://github.com/dczia/Defcon25-Badge
  kind: repo
- label: DCZia - About/History
  url: https://dczia.net/about.html
  kind: website
- label: 'Hackaday: All The Hardware Badges Of DEF CON 25'
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  kind: article
images:
- file: assets/images/badges/dc25/dczia-def-con-25-badge/3fea41ac3f.jpg
  source: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  credit: DC Zia / Hackaday
  caption: Front of the DC Zia 2017 badge showing the four Cherry MX mechanical keyboard switches, 16x2 LCD, and NeoPixel LEDs
- file: assets/images/badges/dc25/dczia-def-con-25-badge/44547741f6.jpg
  source: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  credit: DC Zia / Hackaday
  caption: Rear of the DC Zia 2017 badge, showing the Arduino 101 shield connectors and battery holder
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/dczia/Defcon25-Badge
  title: DCZia DEFCON 25 Badge - 2017 MechKeyboard Shield
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc25''. Repo README confirms it is a shield for the Arduino 101.'
- kind: url
  url: https://dczia.net/about.html
  title: DCZia - About
  accessed: '2026-09-07'
  note: Group history page; confirms the 2017 badge was the "Mech Keyboard Badge - 4 Mechanical Keys // 16x2 Character LCD // NeoPixel RGB LEDs // Acts as shield for an Arduino101," and that DCZia held the DC DarkNet DEF CON 25 black badge that year.
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: All The Hardware Badges Of DEF CON 25
  accessed: '2026-09-07'
  note: 'Press coverage: quantity (290 boards + 10 prototypes), pre-sale via 801 Labs hackerspace in Salt Lake City, and the two photos used above.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price and current availability were not stated in any source found; this was a 2017 pre-sale run and is long past availability, so availability is left unknown rather than guessed. A web search summary separately described a much smaller "~25 hand-assembled" run credited to "DC Zia crew" with "10 people" in their "third year," which conflicts with the Hackaday article's own figures (290 boards + 10 prototypes, second year leading the design) and DCZia's own history page (this was their fourth badge, following two PiBadge years and a laserdisc badge). That smaller-run description could not be traced to an original source, so it was not used.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc25/dczia-def-con-25-badge.glb
  method: kicad
  source_file: DCZia MechKeyBadge.brd
  generated: '2026-09-07'
  bytes: 231884
---

The DC Zia DEF CON 25 badge is a shield board for the Arduino 101, built by DCZia — a hacker/maker group with roots in New Mexico that has been building unofficial badges for DEF CON since 2013. For 2017 (DEF CON 25) the group's fourth badge design added four clicky Cherry MX Blue mechanical keyboard switches, a 16x2 character LCD, and NeoPixel RGB LEDs, stacking on top of an Arduino 101 to provide the microcontroller and Bluetooth/motion hardware.

Hackaday's DEF CON 25 badge roundup reported that DCZia produced 290 boards plus 10 prototypes for the run, with pre-sales coordinated through 801 Labs, a hackerspace in Salt Lake City. That year DCZia also held the DC DarkNet contest's black badge from DEF CON 25. The hardware design and accompanying software are published on GitHub under the `MechKeyboardShield` folder in the `dczia/Defcon25-Badge` repository, though the repo does not state an explicit open-source license.

## Make your own

Hardware and firmware files are in the `MechKeyboardShield` folder of the [GitHub repository](https://github.com/dczia/Defcon25-Badge), organized into `Hardware` and `Software` subdirectories. No BOM, schematic viewer, or license file was found alongside them.

## History

This was DCZia's fourth badge overall, following a found "Laserdisc Badge" (2014) and two Raspberry Pi-based "PiBadge" designs with 3.5" full-color LCDs (2015 and 2016). The group went on to build increasingly ambitious badges in later years, including a 4x4 mechanical-keyboard ESP32 badge with an OLED screen for DEF CON 26.
