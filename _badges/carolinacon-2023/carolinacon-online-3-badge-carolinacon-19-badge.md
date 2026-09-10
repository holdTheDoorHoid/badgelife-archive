---
title: CarolinaCon 19 Badge (CarolinaCon Online 3)
id: carolinacon-2023-carolinacon-online-3-badge-carolinacon-19-badge
layout: badge
parent: CarolinaCon Online 3 (CarolinaCon 2023)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: carolinacon-2023
year: 2023
makers:
- name: pettym / 49th Security Division
summary: NFC tag badge made for CarolinaCon 19 / CarolinaCon Online 3 (April 22, 2023), built around an ST M24SR16 dynamic NFC/RFID tag IC.
functions: Passive NFC tag (M24SR16-YDW6T dynamic NFC/RFID EEPROM tag); no onboard MCU, LEDs, or display found in the design files.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - nfc
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
  open_source: true
  hardware_url: https://github.com/pettym/Carolinacon-19-Badge
  firmware_url: null
  eda_tool: kicad
links:
- label: github.com/pettym/Carolinacon-19-Badge
  url: https://github.com/pettym/Carolinacon-19-Badge
  kind: repo
images:
- file: assets/images/badges/carolinacon-2023/carolinacon-online-3-badge-carolinacon-19-badge/df67f15933.png
  source: https://github.com/pettym/Carolinacon-19-Badge
  credit: pettym
  caption: Front of the Carolinacon 19 (Carolinacon Online 3) NFC badge PCB
- file: assets/images/badges/carolinacon-2023/carolinacon-online-3-badge-carolinacon-19-badge/277b74b1b7.jpg
  source: https://github.com/pettym/Carolinacon-19-Badge
  credit: pettym
  caption: Carolinacon 19 badge face-reveal graphic
contact: {}
notes:
- Electronic badge for CarolinaCon 19 / CarolinaCon Online 3 (April 22, 2023), sold in a merch bundle with a bottle-opener add-on, shirt and sticker. Found by the event-year sweep, task carolinacon.
- The sweep's title read "Carolinacon Online 3 Badge (Carolinacon 19 Badge)"; the maker's repo and README lead with "Carolinacon 19 Badge" (with "aka Carolinacon Online 3" as a parenthetical), so the entry title was reordered to match.
- The merch-bundle claim (bottle opener, shirt, sticker) is from the sweep''s notes only; nothing in the GitHub repo confirms pricing, quantity, or bundling, so those get_one fields are left empty.
status: listed
sources:
- kind: url
  url: https://github.com/pettym/Carolinacon-19-Badge
  title: Carolinacon Online 3 Badge (Carolinacon 19 Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:carolinacon); event read as ''CarolinaCon 2023''.'
- kind: url
  url: https://github.com/pettym/Carolinacon-19-Badge
  title: 'pettym/Carolinacon-19-Badge: README and KiCAD project files'
  accessed: '2026-09-08'
  note: README confirms the badge was made for CarolinaCon 19 (aka CarolinaCon Online 3), April 22, 2023. KiCAD schematic (cc-19-badge.kicad_sch) shows the only active part is an ST M24SR16-YDW6T dynamic NFC/RFID tag IC plus a 6-pin connector - no MCU, LEDs, or display in the design. Source images (front.png, red.png) pulled via media.githubusercontent.com (LFS-backed).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own GitHub repo (README + KiCAD schematic/PCB). It is a real, open-source badge: an NFC tag (ST M24SR16-YDW6T) on a small PCB, no MCU/LEDs/display. No price, quantity, or availability info found anywhere in the repo; get_one fields left empty rather than guessed. The repo''s README also carries an in-joke disclaimer ("operated ... by ChatGPT", "entirely fictional") about the fictional CarolinaCon Conference persona - not evidence the badge itself is fictional, and not reproduced as fact; ignored for cataloging purposes as clearly tongue-in-cheek framing text rather than a claim about the hardware.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/carolinacon-2023/carolinacon-online-3-badge-carolinacon-19-badge.glb
  method: kicad
  source_file: cc-19-badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 10864
---
