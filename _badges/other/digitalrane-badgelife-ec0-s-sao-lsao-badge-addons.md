---
title: digitalrane/badgelife — ec0's SAO/LSAO badge addons
id: other-digitalrane-badgelife-ec0-s-sao-lsao-badge-addons
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 2019
makers:
- name: digitalrane (ec0)
  url: https://github.com/digitalrane
summary: 'A GitHub repo of three separate SAO/LSAO addon-board designs by ec0, made for OzSecCon 2019: a vape-mod-style "ecig" board, a 16-key mechanical "keyboard" board, and a passive LSAO port "mult"iplier.'
functions: 'ecig: a functional vape-mod circuit (boost converter, MOSFET switch, power monitor, manual/MCU fire buttons, indicator LEDs). keyboard: a 16-switch Cherry MX micro-keyboard read over I2C via a GPIO expander. mult: a passive hub that fans one LSAO connection out to five more LSAO ports.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: null
  leds:
    count: null
    type: discrete
    note: 'ecig board has 3 indicator LEDs (D1-D3); keyboard board has 1 LED.'
  display: none
  connectivity:
  - i2c
  battery: 18650 (ecig board only; holder on ecig-BOM, powered by host badge otherwise)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/digitalrane/badgelife
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/digitalrane/badgelife
  url: https://github.com/digitalrane/badgelife
  kind: repo
- label: devec0/badgelife-parts (referenced resources repo)
  url: https://github.com/devec0/badgelife-parts
  kind: repo
images:
  - file: assets/images/badges/other/digitalrane-badgelife-ec0-s-sao-lsao-badge-addons/5ec5a00606.jpg
    source: "https://github.com/digitalrane/badgelife/tree/master/OzSecCon2019/ecig"
    credit: "digitalrane (ec0)"
    caption: "The e-cig themed SAO/LSAO addon (OzSecCon 2019)"
contact: {}
notes:
- collection of multiple SAO/LSAO designs
- 'Made for OzSecCon 2019 (Australia); no matching event id exists yet in events.yml, so this entry is filed under "other".'
- 'Repo contains three distinct KiCad designs under OzSecCon2019/: ecig, keyboard, mult — each is arguably its own SAO and could get a separate entry if desired.'
status: listed
sources:
- kind: url
  url: https://github.com/digitalrane/badgelife
  title: digitalrane/badgelife — ec0's SAO/LSAO badge addons
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/digitalrane/badgelife/tree/master/OzSecCon2019
  title: 'OzSecCon2019 folder — ecig, keyboard, mult designs'
  accessed: '2026-09-07'
  note: 'Repo root shows only one event folder, OzSecCon2019, containing three separate KiCad projects; confirms the "collection" nature of the entry.'
- kind: url
  url: https://raw.githubusercontent.com/digitalrane/badgelife/master/OzSecCon2019/ecig/ecig-BOM.csv
  title: ecig-BOM.csv
  accessed: '2026-09-07'
  note: 'BOM confirms ecig board is a functional vape-mod circuit: 18650 holder, TPS61092 boost converter, IRLS3034 MOSFET, LTC2992 power monitor, 74HCT595 shift register, manual/MCU fire buttons, 3 LEDs.'
- kind: url
  url: https://raw.githubusercontent.com/digitalrane/badgelife/master/OzSecCon2019/keyboard/keyboard-BOM.csv
  title: keyboard-BOM.csv
  accessed: '2026-09-07'
  note: 'BOM shows 16 Cherry MX switches, an MCP23017 I2C GPIO expander, and 1 LED.'
- kind: url
  url: https://raw.githubusercontent.com/digitalrane/badgelife/master/OzSecCon2019/mult/mult-BOM.csv
  title: mult-BOM.csv
  accessed: '2026-09-07'
  note: 'BOM shows only LSAO connectors (1 input socket, 5 output headers) — a passive port multiplier, no active components.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No storefront, price, quantity, or distribution info found — this appears to be a personal/one-off project repo rather than a sold product, so get_one fields are left empty. No photo found for the keyboard or mult boards, only the ecig one (ozsecvape.2019.png in-repo). Event stays "other": OzSecCon (Australia) 2019 has no matching id in events.yml. LED count for the ecig board not stated as a total elsewhere; left as null with a note. The linked devec0/badgelife-parts repo (an EDA parts library) was not deeply reviewed since it is a resources dependency, not the item itself.'
last_modified_date: '2026-09-07'
---

This repository, by ec0 (digitalrane), is a personal collection of SAO/LSAO conference-badge addon designs, all built for OzSecCon 2019. Rather than one badge, it holds three separate KiCad projects under a single `OzSecCon2019/` folder: **ecig**, a working vape-mod-style circuit with an 18650 cell, a TPS61092 boost converter, an IRLS3034 MOSFET switch, an LTC2992 power/current monitor, manual and MCU-triggered "fire" buttons, and three indicator LEDs; **keyboard**, a tiny 16-key mechanical keyboard using real Cherry MX switches read through an MCP23017 I2C GPIO expander; and **mult**, a simple passive board that fans a single LSAO connection out to five more LSAO ports, letting a badge host several addons off one header.

All three use the open LSAO (large SAO) connector standard rather than a standalone microcontroller of their own — they are meant to be driven or read by whatever badge or SAO chain they are plugged into. Designs are published in KiCad with Gerbers, BOMs, and in the ecig board's case a 3D model and photo, but there is no evidence of these having been sold, kitted, or distributed beyond the repository itself; no pricing, quantity, or storefront information could be found.

Because the repo bundles three functionally distinct designs, each could reasonably warrant its own catalog entry in the future; for now they are documented together as this "kit" collection.
