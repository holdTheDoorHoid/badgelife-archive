---
title: 5ohBEE (DC503 Party Pager, DC27)
id: dc27-dc503-badge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: PDX Badgers
  url: https://github.com/pdxbadgers
  role: DC503 group
summary: 'A SMART Response XE classroom clicker repurposed into a 2.4 GHz RF pager/chat badge for the DC503 party at DEF CON 27.'
functions: 'RF pager/group-chat over a shared 2.4 GHz channel, with a "HugQuest" game layer (HUG-token accounting, a WANNAHUG infection/unlock mechanic), keyboard text entry and message buffers.'
look:
  colors: []
  shape: null
  themes:
  - meme
tech:
  mcu: ATmega128RFA1
  leds: null
  display: e-paper
  connectivity: []
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Given to DC503/503 Party attendees at DEF CON 27; base hardware was a repurposed secondhand SMART Response XE unit (originally sold for classroom use, ~$100 new).'
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/pdxbadgers/5ohBEE-2019
  firmware_url: https://github.com/pdxbadgers/5ohBEE-2019
  eda_tool: null
  license: Apache-2.0
  notes: 'Firmware is Arduino sketches (HugQuest.ino, five-oh-BEE.ino) targeting the ATmega128RFA1 via the "ATmega128RFA1 Dev Board" Arduino profile, plus a SmartResponseXE library for the display/keyboard.'
links:
- label: hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design
  url: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  kind: article
- label: github.com/pdxbadgers/5ohBEE-2019
  url: https://github.com/pdxbadgers/5ohBEE-2019
  kind: repo
- label: 'badge.gallery: 5ohBEE / SMART Response XE base pager'
  url: https://badge.gallery/addons/dc503-503-party-2019-5ohbee/smart-response-xe-base-pager
  kind: article
- label: 'badge.gallery: DC503 series'
  url: https://badge.gallery/series/dc503
  kind: article
images:
  - file: assets/images/badges/dc27/dc503-badge-dc27/d9ae781afe.jpg
    source: "https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/"
    credit: "Hackaday"
    caption: "5ohBEE pager: a repurposed SMART Response XE device made into a DC503 party pager for DEF CON 27"
contact: {}
notes:
- Original sweep title was "DC503 Badge (DC27)" and maker "DC503 group"; the project's own name is "5ohBEE" and the makers are PDX Badgers, working under the DC503 party-badge lineage. Kept both names in the record.
- Hackaday's article text reads "It uses an ATmega186rf and communicates on the 802.54 MHz band" — both figures appear to be typos on Hackaday's part (no such chip or ITU band exists); the GitHub repo and badge.gallery both independently confirm ATmega128RFA1, a 2.4 GHz-band radio.
status: released
sources:
- kind: url
  url: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  title: DC503 Badge (DC27)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-badges); event read as ''dc27''.'
- kind: url
  url: https://github.com/pdxbadgers/5ohBEE-2019
  title: pdxbadgers/5ohBEE-2019
  accessed: '2026-09-08'
  note: 'Maker''s own repo: confirms project name 5ohBEE, ATmega128RFA1 MCU, Apache-2.0 license, Arduino firmware, SmartResponseXE display/keyboard library.'
- kind: url
  url: https://badge.gallery/addons/dc503-503-party-2019-5ohbee/smart-response-xe-base-pager
  title: 'SMART Response XE base pager · Hacker Con Badges'
  accessed: '2026-09-08'
  note: 'Confirms maker (PDX Badgers), event (503 Party 2019), features (HugQuest firmware, HUG-token/WANNAHUG game mechanic, channel 11 RF, RSSI).'
- kind: url
  url: https://badge.gallery/series/dc503
  title: 'DC503 · Hacker Con Badges'
  accessed: '2026-09-08'
  note: 'Confirms DC503 is the Portland-area (PDX Badgers) DEF CON-adjacent party-badge lineage, with prior 2017/2018 entries for context.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Price, quantity made, and current availability are not stated anywhere found; left empty rather than guessed. No storefront exists (it was a free party give-away, not sold), so availability is left "unknown" rather than "free" since no source explicitly confirms free distribution vs. limited handout. tech.connectivity left empty: the radio is the ATmega128RFA1''s built-in proprietary 2.4 GHz transceiver (802.15.4-family PHY, channel-based, with RSSI), which does not map cleanly onto the controlled vocabulary (not wifi/ble/zigbee as sources describe it).'
last_modified_date: '2026-09-08'
---

The DC503 crew — Portland's PDX Badgers, working under their long-running DC503 party-badge lineage — skipped designing a badge from scratch for the 503 Party at DEF CON 27 and instead repurposed the SMART Response XE, a discontinued classroom "clicker" device built around an Atmel ATmega128RFA1 (an AVR core with an integrated 2.4 GHz radio) and a small e-paper-style display with a full keyboard. Originally sold to schools for around $100, the units could be found used for a few dollars each by 2019, and the group drilled through a normally-hidden part of the case to reach the reflashing pads for the microcontroller.

Renamed 5ohBEE, the reflashed devices formed a pager-style group chat over a shared RF channel (channel 11), with keyboard text entry and message buffering. On top of that, the project layered a game called HugQuest: a HUG-token accounting system and a "WANNAHUG" infection/unlock mechanic that spread between units, giving the party an interactive, tamagotchi-like layer beyond plain messaging.

## Make your own

The firmware and setup instructions are published on GitHub under Apache-2.0 (github.com/pdxbadgers/5ohBEE-2019). Building one means: flashing a SMART Response XE unit's ATmega128RFA1 using a USBasp programmer (via provided udev rules), installing the "ATmega128RFA1 Dev Board" Arduino profile (SparkFun AVR boards) and the bundled SmartResponseXE Arduino library, then compiling and uploading either the basic five-oh-BEE.ino pager sketch or the full HugQuest.ino game firmware.

## History

DC503 has produced a badge or add-on most years around DEF CON: an nRF52832 BLE badge with an OLED display for the 2017 Wagon Party, a BLE wrist-worn "Banglet" for DEF CON 26 (2018), and a DC503 SAO the same year, before this repurposed-hardware approach for DEF CON 27 in 2019.
