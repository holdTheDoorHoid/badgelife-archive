---
title: MCH2022 Butterfly
id: mch-2022-mch2022-butterfly
layout: badge
parent: MCH 2022
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: mch-2022
year: 2022
makers:
- name: tilde.industries
  url: https://tilde.industries
summary: A butterfly-shaped SAO made by tilde.industries for MCH2022, given as a thank-you to Badge.Team.
functions: Lights up its five reverse-mounted NeoPixel LEDs in animated patterns; carries an EEPROM with a per-unit "LIFE ID" that a companion ESP32 badge app on the MCH2022 badge can read and display.
look:
  colors: []
  shape: butterfly
  themes:
  - animal
  - insect
tech:
  mcu: ATtiny85
  leds:
    count: 5
    type: reverse-mount
    note: Adafruit NeoPixel-compatible (WS2812-style), driven from the ATtiny85; no soldermask over the LED pads, which the maker warns makes soldering trickier.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given by tilde.industries as a thank-you gift to Badge.Team around MCH2022; not confirmed as generally sold.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/tildeindustries/MCH2022-Butterfly/tree/main/Hardware
  firmware_url: https://github.com/tildeindustries/MCH2022-Butterfly/tree/main/Arduino%20Sketches
  eda_tool: KiCad
links:
- label: github.com/tildeindustries/MCH2022-Butterfly
  url: https://github.com/tildeindustries/MCH2022-Butterfly
  kind: repo
- label: "MCH2022 Butterfly SAO – tilde.industries"
  url: https://tilde.industries/mch2022-butterfly/
  kind: website
images:
- file: assets/images/badges/mch-2022/mch2022-butterfly/1b1205a9d3.jpg
  source: "https://tilde.industries/mch2022-butterfly/"
  credit: "tilde.industries"
  caption: "The MCH2022 Butterfly SAO, soldered"
- file: assets/images/badges/mch-2022/mch2022-butterfly/b93d407434.jpg
  source: "https://tilde.industries/mch2022-butterfly/"
  credit: "tilde.industries"
  caption: "MCH2022 Butterfly SAO plugged into a badge"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/tildeindustries/MCH2022-Butterfly
  title: MCH2022 Butterfly
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''mch-2022''.'
- kind: url
  url: https://raw.githubusercontent.com/tildeindustries/MCH2022-Butterfly/main/Arduino%20Sketches/Demo_butterfly_animation/Demo_butterfly_animation.ino
  title: Demo_butterfly_animation.ino
  accessed: '2026-09-07'
  note: "Firmware source confirms ATtiny85 MCU, Adafruit_NeoPixel driving 5 LEDs on pin A3, I2C EEPROM read for a butterfly ID."
- kind: url
  url: https://tilde.industries/mch2022-butterfly/
  title: MCH2022 Butterfly SAO
  accessed: '2026-09-07'
  note: "Maker's own product page: soldering instructions (reverse-mount LEDs, no soldermask, watch EEPROM orientation), and MCH2022 badge app install steps via the 'Hatchery' app store; source of both saved photos."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: "Repo description (via GitHub org page) states it was made 'as thanks for Badge.Team~', so it may not have had a general public sale; price, quantity made, and current availability are not stated anywhere found. sao_version (4-pin vs 6-pin) is not specified in the repo or product page."
last_modified_date: '2026-09-07'
---

The MCH2022 Butterfly is a butterfly-shaped SAO (shitty add-on) made by tilde.industries for May Contain Hackers 2022, the Dutch outdoor hacker camp. By the maker's own account it was created as a thank-you gift for Badge.Team, the group behind the MCH2022 badge platform, rather than as a general retail product.

The board is built around an ATtiny85 driving five reverse-mounted, NeoPixel-compatible LEDs in animated color patterns, plus an I2C EEPROM that stores a per-unit "LIFE ID" the badge can read. Because the LED footprints have no soldermask, the maker's build guide specifically warns that solder bridges are easy to create and shows which pads to solder first. Owners of the MCH2022 badge can install a matching companion app through the badge's "Hatchery" app store (ESP32 native binaries > Hardware > MCH2022 Butterfly) to interact with the add-on from the badge's own screen.

## Make your own

Full KiCad hardware files, Gerbers, and Arduino firmware (an ID-reader test sketch and a demo animation sketch) are published in the maker's GitHub repository, along with photographed soldering instructions covering LED orientation and EEPROM placement.
