---
title: SAO Speak and Spell
id: supercon-2024-sao-speak-and-spell
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Jeremy Geppert
  url: https://hackaday.io/hacker/1277492-jeremygeppert
summary: A Simple Add-On shaped like a scaled-down 1979 Speak & Spell, carrying a 0.91-inch 128x32 SSD1306 I2C OLED, a PAM8302-amplified 8-ohm speaker and a single tactile button on the standard 6-pin SAO header, built by first-time board designer Jeremy Geppert (coached by his brother Andy Geppert of Core64) for the Supercon 8 / 2024 Hackaday Supercon SAO Contest, with V1.2 going to production and being bagged as kits in late October 2024.
functions: Plays a startup tone and a spoken "welcome" clip through the amplified speaker, drives text/graphics on the small OLED, and reads the single tactile button as input; controlled by a CircuitPython demo script (audiodemo.py).
look:
  colors:
  - red
  - white
  shape: null
  themes:
  - retro computer
  - console
  - music
tech:
  mcu: RP2040 Zero
  leds: null
  display: 0.91" 128x32 OLED (SSD1306, I2C)
  connectivity:
  - i2c
  - audio
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: about 30
  availability: unknown
  distribution:
  - contest
  - kit
  where: Distributed as kits to Supercon 8 (2024) attendees who entered/received the SAO contest add-ons; OLED and speaker pre-installed, final assembly (button, connector) left to the recipient.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/198045/files
  firmware_url: https://hackaday.io/project/198045/files
  eda_tool: null
links:
- label: hackaday.io/project/198045-sao-speak-and-spell
  url: https://hackaday.io/project/198045-sao-speak-and-spell
  kind: hackaday
  archived: https://web.archive.org/web/20250917210859/https://hackaday.io/project/198045-sao-speak-and-spell
- label: hackaday.io/project/198045/files
  url: https://hackaday.io/project/198045/files
  kind: hackaday
- label: hackaday.com/2024/09/27/2024-sao-contest-speak-sao
  url: https://hackaday.com/2024/09/27/2024-sao-contest-speak-sao/
  kind: article
  archived: https://web.archive.org/web/20251211101809/https://hackaday.com/2024/09/27/2024-sao-contest-speak-sao/
- label: hackaday.io/contest/197237-supercon-8-add-on-contest
  url: https://hackaday.io/contest/197237-supercon-8-add-on-contest
  kind: hackaday
images:
- file: assets/images/badges/supercon-2024/sao-speak-and-spell/3be38e4b79.png
  source: https://hackaday.io/project/198045-sao-speak-and-spell
  credit: Jeremy Geppert
  caption: The SAO Speak and Spell, a Speak & Spell-shaped Simple Add-On
  archived: https://web.archive.org/web/20250917210859/https://hackaday.io/project/198045-sao-speak-and-spell
- file: assets/images/badges/supercon-2024/sao-speak-and-spell/393f869efe.png
  source: https://hackaday.io/project/198045-sao-speak-and-spell
  credit: Jeremy Geppert
  caption: Assembled SAO Speak and Spell showing OLED display and speaker
  archived: https://web.archive.org/web/20250917210859/https://hackaday.io/project/198045-sao-speak-and-spell
contact: {}
notes:
- Sheet listed no chip/display/price details; filled in from the maker's Hackaday.io project page and its files section.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198045-sao-speak-and-spell
  title: SAO Speak and Spell
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20250917210859/https://hackaday.io/project/198045-sao-speak-and-spell
- kind: url
  url: https://hackaday.io/project/198045-sao-speak-and-spell
  title: SAO Speak and Spell (project page)
  accessed: '2026-09-07'
  note: Confirmed maker, event, RP2040 Zero MCU, OLED/speaker/button spec, V1.2 red PCB, ~30 units, CircuitPython firmware.
  archived: https://web.archive.org/web/20250917210859/https://hackaday.io/project/198045-sao-speak-and-spell
- kind: url
  url: https://hackaday.io/project/198045/files
  title: SAO Speak and Spell - Files
  accessed: '2026-09-07'
  note: Listed available files - Gerbers/drill (V1.2), schematic PDF, audiodemo.py CircuitPython script, and audio assets. No explicit license or EDA tool stated.
- kind: url
  url: https://hackaday.com/2024/09/27/2024-sao-contest-speak-sao/
  title: '2024 SAO Contest: Speak SAO'
  accessed: '2026-09-07'
  note: Hackaday.com coverage confirming maker, 128x32 OLED, amplified speaker, single button, and that it was Jeremy's first board design.
  archived: https://web.archive.org/web/20251211101809/https://hackaday.com/2024/09/27/2024-sao-contest-speak-sao/
- kind: url
  url: https://hackaday.io/contest/197237-supercon-8-add-on-contest
  title: Supercon 8 Add-on Contest
  accessed: '2026-09-07'
  note: Confirms the entry in the 2024 SAO contest; did not place among the four category winners (Digital Multimeter, Etch sAo Sketch, Bendy SAO, Vectrex SAO), so it was distributed as a contest entry kit rather than mass-produced for a later event.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price paid/charged for the kit is not stated anywhere found; left empty. Exact SAO connector pin count/version confirmed as 6-pin (v1.69bis) from the original sheet summary but not independently re-verified against the schematic PDF (not opened in detail). EDA tool and license unstated in the files list.
last_modified_date: '2026-09-07'
---

Jeremy Geppert's SAO Speak and Spell is a Simple Add-On shaped like a scaled-down 1979 Speak & Spell, built as his first-ever PCB design and first SAO, with early guidance from his brother Andy Geppert (of Core64, himself a fellow SAO contest entrant). It was made for the Supercon 8 / 2024 Hackaday Supercon SAO Contest: a small red PCB carrying a 0.91-inch 128x32 SSD1306 I2C OLED, an 8-ohm speaker driven by a PAM8302 amplifier, and a single tactile button, all wired to an RP2040 Zero running CircuitPython. A bundled `audiodemo.py` script plays a startup tone and a spoken "welcome" clip through the speaker.

About 30 units reached V1.2 production and were bagged as kits — OLED and speaker pre-installed, with the button and SAO connector left for the recipient to solder — distributed to Supercon 8 attendees in late October 2024 as part of the SAO contest's add-on giveaway. The project did not place among the contest's four category winners (Best Overall, Fun, Fine Art, Functional), so unlike those it was not selected for mass production and distribution at Hackaday Europe 2025.

## Make your own

Gerber and drill files for the V1.2 board, a schematic PDF, and the CircuitPython demo script (`audiodemo.py`) are posted in the project's files section on Hackaday.io. No BOM, EDA tool, or license is stated alongside them.
