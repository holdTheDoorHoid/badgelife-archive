---
title: CactusCon6 Badge
id: cactuscon-2017-cactuscon6-badge
layout: badge
parent: CactusCon 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2017
year: 2017
makers:
- name: Tim Hatch
  url: https://github.com/thatch
  role: PCB design
- name: Erik Wilson
  url: https://github.com/erikwilson
  role: firmware
summary: 'The CactusCon 6 (2017) conference badge: an ESP32-based board with an
  SSD1306 OLED display, running NodeMCU/Lua firmware that attendees could reflash
  with their own code.'
functions: 'Runs user-uploaded Lua code via NodeMCU firmware; no built-in game or
  CTF is documented in the sources found.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ESP32
  leds: null
  display: 0.96" OLED (SSD1306)
  connectivity:
  - wifi
  - ble
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
  open_source: yes
  hardware_url: https://github.com/thatch/cactuscon-badge-2017
  firmware_url: https://github.com/erikwilson/CactusCon6
  eda_tool: null
links:
- label: github.com/erikwilson/CactusCon6
  url: https://github.com/erikwilson/CactusCon6
  kind: repo
- label: github.com/thatch/cactuscon-badge-2017
  url: https://github.com/thatch/cactuscon-badge-2017
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'The sweep titled this entry after the erikwilson/CactusCon6 repo, which is the
  firmware side of the same badge. The PCB itself was designed by Tim Hatch and is
  already catalogued separately as cactuscon-2017-thatch-cactuscon-badge-2017-github;
  this entry and that one describe the same physical CactusCon 2017 badge.'
status: released
sources:
- kind: url
  url: https://github.com/erikwilson/CactusCon6
  title: CactusCon6 Badge
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/erikwilson/CactusCon6
  title: erikwilson/CactusCon6 README
  accessed: '2026-09-10'
  note: Confirms ESP32 + SSD1306 OLED hardware, NodeMCU/Lua firmware, and credits
    Tim Hatch for the PCB design.
- kind: url
  url: https://github.com/thatch/cactuscon-badge-2017
  title: thatch/cactuscon-badge-2017
  accessed: '2026-09-10'
  note: The PCB design repo this firmware targets; CC-BY-4.0 licensed, ESP-32 based,
    for CactusCon 2017.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: No pricing, quantity, or distribution details found in either repo. No
    photos of the physical badge were found in either repository (both are
    firmware/hardware-design repos with no image assets). This entry duplicates
    cactuscon-2017-thatch-cactuscon-badge-2017-github, which already covers the
    hardware side of the same badge; consider merging.
last_modified_date: '2026-09-10'
---

The CactusCon 6 badge (2017) paired an ESP32-based PCB, designed by Tim Hatch, with a small SSD1306 OLED display. It shipped running NodeMCU firmware that let attendees upload and run their own Lua code on the badge, rather than a fixed game or firmware image. A batch of OLED displays CactusCon received that year had their VCC/GND pins reversed from what the PCB expected, requiring some attendees to bend or jump pins to get the display working.

Both halves of the project are open source: the PCB design lives in Tim Hatch's `cactuscon-badge-2017` repository (CC-BY-4.0), and the companion firmware/tooling used to build and flash the NodeMCU image lives in Erik Wilson's `CactusCon6` repository, which this entry was originally created from. No pricing, production quantity, or distribution details were found in either source.
