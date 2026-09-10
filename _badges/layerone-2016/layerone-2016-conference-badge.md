---
title: LayerOne 2016 Conference Badge
id: layerone-2016-layerone-2016-conference-badge
layout: badge
parent: LayerOne 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: layerone-2016
year: 2016
makers:
- name: charliex
  url: https://hackaday.io/charliex
  role: design and firmware
- name: mmca
  role: team member
summary: The official electronic badge for LayerOne 2016, a PSoC4-based board with a 5x4 grid of WS2812B LEDs and an ESP8266 add-on that gave it working Wi-Fi for the first time.
functions: Displays RGB LED patterns (driven locally or over Wi-Fi from a PC via the ESP8266 bridge); exposes a mini prototyping area with 3.3V rail, battery rail, and PSoC4 I/O for attendees to add their own components.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - radio
tech:
  mcu: PSoC4
  leds:
    count: 20
    type: WS2812B
    note: 5x4 grid
  display: none
  connectivity:
  - wifi
  battery: CR123A
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 'about 8 hand-built by the creator, plus a pick-and-place production run of unstated size'
  availability: unknown
  distribution:
  - free_drop
  where: Given to LayerOne 2016 attendees as the conference badge.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/charlie-x/layerone2016
  firmware_url: https://github.com/charlie-x/layerone2016
  eda_tool: Eagle
  license: Unlicense
links:
- label: badge.gallery/badges/layerone-2016-conference-badge
  url: https://badge.gallery/badges/layerone-2016-conference-badge
  kind: website
- label: Hackaday.io project 6003
  url: https://hackaday.io/project/6003-layerone-2016-conference-badge
  kind: hackaday
- label: charlie-x/layerone2016 (GitHub)
  url: https://github.com/charlie-x/layerone2016
  kind: repo
images:
  - file: assets/images/badges/layerone-2016/layerone-2016-conference-badge/f9cde549c8.jpg
    source: "https://hackaday.io/project/6003-layerone-2016-conference-badge"
    credit: "charliex"
    caption: "LayerOne 2016 Conference Badge, PSoC4/ESP8266/WS2812B board"
contact: {}
notes:
- 'Sweep wording was "Official electronic conference badge for LayerOne 2016" — confirmed and matches the Hackaday.io project title.'
- Price and total production quantity are not stated in any source found; only "about 8" early hand-built units before the pick-and-place run are documented.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/layerone-2016-conference-badge
  title: LayerOne 2016 Conference Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''LayerOne 2016''.'
- kind: url
  url: https://hackaday.io/project/6003-layerone-2016-conference-badge
  title: LayerOne 2016 Conference Badge (Hackaday.io project 6003)
  accessed: '2026-09-10'
  note: "Maker's own project page; confirmed makers (charliex, mmca), PSoC4/ESP8266/WS2812B hardware, CR123A power, mini prototyping area, and source image."
- kind: url
  url: https://github.com/charlie-x/layerone2016
  title: charlie-x/layerone2016
  accessed: '2026-09-10'
  note: Confirmed open hardware (Eagle files) and firmware (PSoC Creator C, bootloader) under the Unlicense, plus a companion Windows lights-server tool.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: No price or total production quantity found in any source; only the ~8 early hand-built units are documented before the pick-and-place run. No public storefront found (it was a badge given to attendees, not sold).
last_modified_date: '2026-09-10'
---

The LayerOne 2016 Conference Badge was designed by charliex (with mmca) of the LayerOne badge team as the official electronic badge handed out at LayerOne 2016 (May 28-29, 2016, Sheraton Gateway LAX, Los Angeles). It carries a PSoC4 microcontroller driving a 5x4 grid of 20 WS2812B RGB LEDs, plus an ESP8266 module that gave the badge working Wi-Fi before the event — a feature the team had run out of time for the previous year. A mini prototyping area breaks out a 3.3V rail, a battery rail, and spare PSoC4 I/O so attendees could add their own add-ons (planned examples included a speaker, switches, an IR sensor, and a photo-sensor module). Power comes from a CR123A cell with reverse-polarity protection.

Public build logs on the project's Hackaday.io page describe PCB bring-up, Eagle board work, level-shifting and capacitance debugging between the PSoC4 and ESP8266, and a pick-and-place production run following roughly eight early hand-built units. No price or total production count is documented; the badge was distributed to attendees as the conference badge rather than sold.

## Make your own

Hardware (Eagle PCB files) and firmware (PSoC Creator project in C, plus bootloader .elf/.hex files) are published at github.com/charlie-x/layerone2016 under the Unlicense. The repo also includes a Windows "lights server" tool that sends UDP packets to drive the LEDs and adds audio-reactive visualization. Firmware is flashed via a UART connection at 115200 baud using PSoC Creator 3.3 SP2.
