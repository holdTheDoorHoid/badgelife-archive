---
title: Speedometer SAO (DC32)
id: dc32-speedometer-sao-dc32
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: Uberwoozle / Car Hacking Village
summary: 'A DEF CON 32 Car Hacking Village SAO built around an ESP32 and a monochrome LCD, with a "cat battle" mode (two SAOs fight over CAN bus) and a speedometer display mode; also the vehicle for a CTF reverse-engineering challenge ("RPS FTW").'
functions: 'LCD speedometer display; "cat mode" battles against a second SAO over CAN bus (rock-paper-scissors style); embeds the CTF challenge "RPS FTW (Speedometer SAO)", which involves reversing the firmware to leak a flag hidden in the on-board font library'
look:
  colors: []
  shape: null
  themes:
  - cat
  - measurement
  - ctf
  - security
tech:
  mcu: ESP32
  leds: null
  display: LCD (ST7565 driver)
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/car-hacking-village/DC32_CHV_Speedometer_Firmware
  eda_tool: null
  license: MIT
  notes: 'Only the firmware is published (MIT licensed); no hardware/Gerbers repo for this SAO was found. The firmware includes the CTF problem and solution notes for the "RPS FTW" challenge.'
links:
- label: github.com/car-hacking-village/DC32_CHV_Speedometer_Firmware
  url: https://github.com/car-hacking-village/DC32_CHV_Speedometer_Firmware
  kind: repo
- label: car-hacking-village/DC32_CTF_CHALLENGES (challenge writeup)
  url: https://github.com/car-hacking-village/DC32_CTF_CHALLENGES/blob/main/challenges.md
  kind: doc
- label: car-hacking-village/CHV_SAO_Specification
  url: https://github.com/car-hacking-village/CHV_SAO_Specification
  kind: doc
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- This appears to be the same item as dc32-speedometer-sao-not-a-cat (same maker Uberwoozle, same event, same LCD-display/cat-battle speedometer SAO); see research.notes.
status: listed
sources:
- kind: url
  url: https://github.com/car-hacking-village/DC32_CHV_Speedometer_Firmware
  title: DC32 CHV Speedometer Firmware
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc32''. README confirms firmware is built on a display library and embeds a CTF problem; sdkconfig.defaults and file list (st7565.c, catface_helper.c, speedometer_helper.c, can_helper.c) confirm ESP32 target, ST7565 LCD driver, CAN bus, and cat-battle/speedometer functions. LICENSE file is MIT.'
- kind: url
  url: https://github.com/car-hacking-village/DC32_CTF_CHALLENGES/blob/main/challenges.md
  title: 'DC32 CTF Challenges - "RPS FTW (Speedometer SAO)"'
  accessed: '2026-09-07'
  note: 'Challenge writeup names Uberwoozle as submitter, describes "two cats" battling and sending messages over CAN, and a memory-leak flag hidden in the on-board font library, printed to the LCD.'
- kind: url
  url: https://github.com/car-hacking-village/CHV_SAO_Specification
  title: CHV SAO Specification
  accessed: '2026-09-07'
  note: 'CHV''s SAO connector is a 6-pin SAO bis v1.69 footprint repurposing the two I2C pins as CAN TX/RX, which is why this SAO talks CAN bus instead of I2C.'
- kind: url
  url: https://github.com/car-hacking-village
  title: Car Hacking Village GitHub org
  accessed: '2026-09-07'
  note: 'Confirmed the org''s badge lineage (DC31, DC32, DC33) and that DC32_CHV_Speedometer_Firmware is filed under the 2024/DC32 badge set, fixing the event/year as DC32 2024.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Confirmed via the maker's own firmware repo and the Car Hacking Village CTF challenge writeup
    that this is a DEF CON 32 (2024) Car Hacking Village SAO built on ESP32 with an ST7565 LCD,
    made by Uberwoozle, with a "cat mode" battle feature (two SAOs fight over CAN bus) and a
    speedometer display mode, and that it hosts the "RPS FTW (Speedometer SAO)" CTF challenge.
    No hardware repo, price, quantity, LED count, board color/shape, or photo of the physical SAO
    was found; only firmware-embedded animation frames (image/*.bmp in the repo) were located, and
    those are display assets, not photos of the item, so no image was saved.
    This entry is very likely a duplicate of dc32-speedometer-sao-not-a-cat, which already carries a
    $50 price, "village" distribution via the CHV booth, and near-identical functions (LCD display,
    speedometer, cat battles) for the same maker (Uberwoozle) and event; that entry's price/vendor
    details ($50, sold at the CHV booth) were not independently found in this run's sources, so they
    were not copied over here, but the technical findings from the firmware repo (ESP32, ST7565 LCD,
    CAN bus, MIT license) are new and not present in that other entry.
last_modified_date: '2026-09-07'
---

Uberwoozle's Speedometer SAO was made for the Car Hacking Village (CHV) at DEF CON 32 (2024). Under the hood it is an ESP32 driving a monochrome LCD through an ST7565 controller, and it talks CAN bus rather than I2C over its SAO connector — CHV's own SAO spec repurposes the usual I2C pins on the SAO bis v1.69 footprint for CAN TX/RX, so any two CHV SAOs (or a SAO and the CHV main badge) can exchange CAN messages. The badge has (at least) two modes: a straightforward speedometer readout on the LCD, and a "cat mode" where two Speedometer SAOs battle each other over CAN in a rock-paper-scissors-style exchange, complete with cat faces on the display.

The SAO also doubles as a CTF puzzle. Car Hacking Village's DC32 challenge set lists "RPS FTW (Speedometer SAO)," submitted by Uberwoozle, as a medium/hard reverse-engineering and exploitation challenge: competitors are given the firmware and have to work out how sending a crafted speed value and a bad rock-paper-scissors response can be used to leak a flag that is hidden as offsets into the badge's own font library, decoded by reading what gets printed to the LCD. The firmware for the SAO is published on GitHub under the MIT license and includes both the CTF problem and the intended solution notes; no separate hardware/Gerbers repository for the board itself was found.

This entry was surfaced independently by a discovery sweep from the firmware repo alone, and its details (chip, display, CAN connectivity, CTF role) look like a strong match for the existing `dc32-speedometer-sao-not-a-cat` entry, which already has this maker, event, LCD display, and "cat battles" function along with a $50 price and CHV-booth sale that this run's sources did not independently confirm. Price, quantity, LED count, board color, and a photo of the physical SAO remain unconfirmed in either entry.
