---
title: still-sao-though — Hackaday Supercon 2024 SAO
id: supercon-2024-still-sao-though-hackaday-supercon-2024-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: kantoniak
  url: https://github.com/kantoniak
summary: 'A minimal SAO (v1.69bis) built around an ATtiny85 with two bottom-throwing LEDs that blink in an alternating pattern; made for Hackaday Supercon 2024 and also carried to Hackaday Europe 2025.'
functions: 'Two LEDs alternate on/off every 750ms (no buttons or other inputs); firmware is a simple Arduino sketch.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ATtiny85
  leds:
    count: 2
    type: discrete
    note: 'bottom-throwing (board-edge/downward facing) LEDs, alternating blink pattern'
  display: none
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
  open_source: yes
  hardware_url: https://github.com/kantoniak/still-sao-though/tree/main/hardware
  firmware_url: https://github.com/kantoniak/still-sao-though/tree/main/software
  eda_tool: KiCad
  notes: 'Hardware is KiCad (.kicad_pcb/.kicad_sch); firmware is a PlatformIO/Arduino sketch for ATtiny85. No LICENSE file found in the repo.'
links:
- label: github.com/kantoniak/still-sao-though
  url: https://github.com/kantoniak/still-sao-though
  kind: repo
images:
- file: assets/images/badges/supercon-2024/still-sao-though-hackaday-supercon-2024-sao/6bd70a9441.gif
  source: "https://github.com/kantoniak/still-sao-though"
  credit: "kantoniak"
  caption: "Animated preview of the still-sao-though SAO's two alternating LEDs"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/kantoniak/still-sao-though
  title: still-sao-though — Hackaday Supercon 2024 SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''Hackaday Supercon 2024''.'
- kind: url
  url: https://github.com/kantoniak/still-sao-though
  title: 'kantoniak/still-sao-though: README'
  accessed: '2026-09-07'
  note: 'README confirms ATtiny85, two bottom-throwing LEDs, made for Hackaday Supercon 2024 and also shown at Hackaday Europe 2025; describes an attempted (failed) I2C add-on via TinyWireS.'
- kind: url
  url: https://raw.githubusercontent.com/kantoniak/still-sao-though/main/software/src/main.cpp
  title: still-sao-though firmware source
  accessed: '2026-09-07'
  note: 'Firmware toggles two LEDs (pins 1 and 4) in alternating fashion every 750ms; no buttons.'
- kind: url
  url: https://kantoniak.com/
  title: kantoniak.com
  accessed: '2026-09-07'
  note: 'Maker''s personal site is just a contact-links page; no mention of this project, so no additional bio/context found there.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source is the maker''s own GitHub repo (README + firmware); no press coverage, storefront, or Hackaday.io project page found. Price, quantity, and availability are not stated anywhere, so left empty/unknown. No LICENSE file in the repo, so exact license is unspecified even though hardware and firmware are both published. Board shape/colors not determinable without a photo of the physical PCB (only an LED-blink preview GIF was found, no full board photo).'
last_modified_date: '2026-09-07'
---

The still-sao-though is a small SAO (Simple/Shitty Add-On, v1.69bis 6-pin standard) that maker kantoniak (Kay) built for Hackaday Supercon 2024. It centers on an ATtiny85 microcontroller driving two "bottom-throwing" LEDs that alternate on and off every 750 milliseconds — a deliberately minimal light show with no buttons or other inputs. The maker also brought the board along to Hackaday Europe 2025.

The README notes an attempt to add I2C support using the TinyWireS library, which the maker says failed, likely due to clock-stretching issues on the ATtiny85 — a candid detail about a feature that didn't make it into the final board. The project title and README's "eggcelent friends" phrasing suggest an egg or friend-themed design, but no photo of the assembled board was found to confirm colors or shape beyond the LED-blink preview GIF.

Both hardware (KiCad schematic/PCB files) and firmware (a PlatformIO/Arduino sketch) are published in the maker's GitHub repository, though no LICENSE file accompanies them. No pricing, production quantity, or distribution details were found in any available source.
