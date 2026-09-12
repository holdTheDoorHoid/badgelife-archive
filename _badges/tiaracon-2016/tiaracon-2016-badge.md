---
title: TiaraCon 2016 badge
id: tiaracon-2016-tiaracon-2016-badge
layout: badge
parent: TiaraCon 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: tiaracon-2016
year: 2016
makers:
- name: securelyfitz
summary: A charlieplexed-LED electronic badge for TiaraCon 2016, built as a simple through-hole soldering project.
functions: LED animations driven by charlieplexing, with mode selection via a capacitive-touch button.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ATtiny85
  leds:
    count: 6
    type: charlieplexed
    note: 3mm or 5mm through-hole LEDs, driven from 3 I/O pins
  display: null
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: ~$2 in bulk (BOM cost)
  price_usd: 2
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/securelyfitz/tiaracon2016/tree/master/hardware
  firmware_url: https://github.com/securelyfitz/tiaracon2016/tree/master/software
  eda_tool: Eagle
links:
- label: github.com/securelyfitz/tiaracon2016
  url: https://github.com/securelyfitz/tiaracon2016
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/securelyfitz/tiaracon2016
  title: TiaraCon 2016 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''tiaracon-2016''.'
- kind: url
  url: https://raw.githubusercontent.com/securelyfitz/tiaracon2016/master/README.md
  title: securelyfitz/tiaracon2016 README
  accessed: '2026-09-07'
  note: Confirmed event (TiaraCon 2016, tiaracon.org), MCU (ATtiny85), 6 charlieplexed LEDs, capacitive mode button, CR2032 power, ~$2 BOM cost, and that it derives from an earlier "fireflies" project with custom pony artwork.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No photo of the assembled badge was found in the repo (only Eagle .brd/.lbr files, gerbers, and a JarOfFireflies.pdf reference doc) or elsewhere online, so no images could be saved. Total production quantity and current availability are not stated anywhere found.
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/tiaracon-2016-badge/
model:
  file: assets/models/tiaracon-2016/tiaracon-2016-badge.glb
  method: kicad
  source_file: tiaracon.brd
  generated: '2026-09-10'
  bytes: 81200
---

The TiaraCon 2016 badge is a simple through-hole soldering-project badge made by securelyfitz for TiaraCon, a small event held in 2016 (tiaracon.org). It runs on an ATtiny85 and drives six charlieplexed LEDs from just three I/O pins, with a capacitive-touch button used to cycle through LED animation modes. Power comes from a coin-cell (CR2032) holder on the board.

The design is derived from an earlier "fireflies" project by the same maker, adapted with new artwork for TiaraCon — the README notes custom pony artwork on the back of the board. Bill-of-materials cost was cited as just over $2 per unit in bulk, though the maker noted ATtiny85 pricing had fluctuated higher at times.

Hardware (Eagle board and library files, plus Gerbers) and firmware are published in full on GitHub, making this an open-source build. No total production quantity, sale price, or photo of the finished badge could be found in the repository or elsewhere, so those fields and images are left empty.
