---
title: CactusCon Badge 2017 (thatch)
id: cactuscon-2017-thatch-cactuscon-badge-2017-github
layout: badge
parent: CactusCon 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2017
year: 2017
makers:
- name: thatch
  url: https://github.com/thatch
summary: An ESP32-based electronic conference badge designed for CactusCon 2017, released as an open-source KiCad project.
functions: Runs user-uploaded Lua code via NodeMCU firmware; no built-in game or CTF is documented in the sources found.
look:
  colors: []
  shape: rectangle
  themes:
  - security
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
  open_source: partial
  hardware_url: https://github.com/thatch/cactuscon-badge-2017
  firmware_url: https://github.com/erikwilson/CactusCon6
  eda_tool: KiCad
links:
- label: github.com/thatch/cactuscon-badge-2017
  url: https://github.com/thatch/cactuscon-badge-2017
  kind: repo
- label: github.com/erikwilson/CactusCon6
  url: https://github.com/erikwilson/CactusCon6
  kind: repo
images:
- file: assets/images/badges/cactuscon-2017/thatch-cactuscon-badge-2017-github/87e01ea0ed.png
  source: https://github.com/thatch/cactuscon-badge-2017
  credit: thatch
  caption: Render of badge front
- file: assets/images/badges/cactuscon-2017/thatch-cactuscon-badge-2017-github/18333d5460.png
  source: https://github.com/thatch/cactuscon-badge-2017
  credit: thatch
  caption: Render of badge back
contact: {}
notes:
- Sweep found this under the title 'thatch/cactuscon-badge-2017 (GitHub)', which is the repo name rather than the maker's chosen badge title; retitled to 'CactusCon Badge 2017 (thatch)' since the README gives no other name.
- Spotted by a research agent while working on another entry; not yet researched.
- The sweep titled this entry after the erikwilson/CactusCon6 repo, which is the firmware side of the same badge. The PCB itself was designed by Tim Hatch and is already catalogued separately as cactuscon-2017-thatch-cactuscon-badge-2017-github; this entry and that one describe the same physical CactusCon 2017 badge.
status: released
sources:
- kind: url
  url: https://github.com/thatch/cactuscon-badge-2017
  title: thatch/cactuscon-badge-2017 (GitHub)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/thatch/cactuscon-badge-2017
  title: thatch/cactuscon-badge-2017 (GitHub)
  accessed: '2026-09-10'
  note: Confirmed repo is a real ESP32 badge project for CactusCon 2017, CC-BY-4.0 licensed; README, hardware folder listing (KiCad files), and front/back render images.
- kind: url
  url: https://github.com/erikwilson/CactusCon6
  title: CactusCon6 Badge
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://github.com/erikwilson/CactusCon6
  title: erikwilson/CactusCon6 README
  accessed: '2026-09-10'
  note: Confirms ESP32 + SSD1306 OLED hardware, NodeMCU/Lua firmware, and credits Tim Hatch for the PCB design.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Maker's own repo confirms this is a real ESP32-based badge made for CactusCon 2017, published under CC-BY-4.0 with KiCad hardware files. The README is minimal (title plus front/back renders) and does not state LED count, display, buttons, battery, price, quantity made, or how/whether it was distributed at the con, so those fields are left empty rather than guessed. No separate firmware repo or write-up was found, so open_source is marked partial (hardware only) rather than yes. Not the same item as the other CactusCon 2017 entries on file (the 'CactusCon 2017 Wi-Fi/Bluetooth Scanner Badge' or 'CactusCon6 Badge', both credited to different makers/orgs). Merged with duplicate entry 'CactusCon6 Badge' (cactuscon-2017-cactuscon6-badge).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/cactuscon-2017/cactuscon6-badge/
---

thatch's CactusCon Badge 2017 is an ESP32-based electronic badge built as an open-source KiCad project for CactusCon 2017 in Mesa, Arizona. The repository, published under a CC-BY-4.0 license, includes the full schematic and PCB layout along with a custom footprint library and a reference to a shared makerspace parts-bin submodule, plus rendered front and back images of the finished board.

Beyond the hardware source itself, the maker's README does not describe the badge's specific features (LED count, display, inputs), how many were made, or how it was distributed at the event, so those details are left unfilled here rather than guessed. No accompanying firmware repository was found.

## Make your own

The hardware is open source: clone the repository and open `cactuscon_badge_2017.kicad_pcb` / `.sch` in KiCad to view or modify the design. A `Makefile` in the `hardware` folder suggests an automated build/export step, though no build instructions are given in the README itself.

## Notes merged from the duplicate entry "CactusCon6 Badge"

The CactusCon 6 badge (2017) paired an ESP32-based PCB, designed by Tim Hatch, with a small SSD1306 OLED display. It shipped running NodeMCU firmware that let attendees upload and run their own Lua code on the badge, rather than a fixed game or firmware image. A batch of OLED displays CactusCon received that year had their VCC/GND pins reversed from what the PCB expected, requiring some attendees to bend or jump pins to get the display working.

Both halves of the project are open source: the PCB design lives in Tim Hatch's `cactuscon-badge-2017` repository (CC-BY-4.0), and the companion firmware/tooling used to build and flash the NodeMCU image lives in Erik Wilson's `CactusCon6` repository, which this entry was originally created from. No pricing, production quantity, or distribution details were found in either source.
