---
title: PepitaBadgeShieldCompatible — BSides Badge (Pepita)
id: other-pepitabadgeshieldcompatible-bsides-badge-pepita
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2015
makers:
- name: soynerdito
summary: An Arduino shield-compatible electronic badge made by soynerdito (codename "Pepita") for BSidesPR 2015, built around an ATmega328P and reprogrammable with an external USBasp programmer.
functions: 'Runs custom Arduino sketches flashed via USBasp; the board itself doubles as an Arduino-compatible target rather than shipping with a fixed game or light show.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ATmega328P
  leds: null
  display: null
  connectivity: []
  battery: null
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
  hardware_url: https://github.com/soynerdito/PepitaBadgeShieldCompatible
  firmware_url: https://github.com/soynerdito/PepitaBadgeShieldCompatible
  eda_tool: Eagle
links:
- label: github.com/soynerdito/PepitaBadgeShieldCompatible
  url: https://github.com/soynerdito/PepitaBadgeShieldCompatible
  kind: repo
- label: "Soynerdito's Blog: Badge as USBASP (very badly explained)"
  url: http://blog.soynerdito.com/2015/11/badge-as-usbasp-verry-badly-explained.html
  kind: article
images:
  - file: assets/images/badges/other/pepitabadgeshieldcompatible-bsides-badge-pepita/484ca107be.png
    source: "https://github.com/soynerdito/PepitaBadgeShieldCompatible"
    credit: "soynerdito"
    caption: "Concept sketch of the Pepita badge PCB shape, showing the USB programming header and bottom edge connector"
contact: {}
notes:
- "Sheet listed this as an untitled 'BSides' entry; the repo names it codename Pepita and the Arduino IDE board manager package inside the repo identifies it as the 'BSides Badge 2015' board, which is why year is set to 2015."
status: released
sources:
- kind: url
  url: https://github.com/soynerdito/PepitaBadgeShieldCompatible
  title: PepitaBadgeShieldCompatible — BSides Badge (Pepita)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides''.'
- kind: url
  url: https://github.com/soynerdito/PepitaBadgeShieldCompatible
  title: soynerdito/PepitaBadgeShieldCompatible README
  accessed: '2026-09-07'
  note: 'Confirms ATmega328P, Arduino-shield compatibility, USBasp programming instructions, and the "BSides Badge 2015" Arduino board name.'
- kind: url
  url: http://blog.soynerdito.com/2015/11/badge-as-usbasp-verry-badly-explained.html
  title: "Soynerdito's Blog: Badge as USBASP verry badly explained"
  accessed: '2026-09-07'
  note: 'Companion post (Nov 2015) on using the same ATmega328P BSides badge as a USBasp programmer; no additional badge photo found.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No confirmed event id for BSidesPR exists in _data/events.yml, so event is left as "other"; this badge was made for BSidesPR (BSides Puerto Rico) 2015, per the repo''s Arduino board manager entry ("BSides Badge 2015") and soynerdito''s other BSidesPR-focused repos (e.g. BSides20016Badge, RickBadge). No price, quantity, LED count, or display info is stated anywhere found; no actual photograph of an assembled/soldered board was located, only the maker''s concept/PCB-layout sketch (concept.png) saved as the entry image. Maker''s own site (blog.soynerdito.com) and GitHub are the only sources found; no press coverage or storefront listing exists.'
last_modified_date: '2026-09-07'
---

The Pepita badge is an Arduino shield-compatible electronic badge that soynerdito built for BSidesPR (BSides Puerto Rico) 2015. Instead of shipping as a sealed novelty, it is designed to be reprogrammed like any other Arduino board: it runs an ATmega328P at 16 MHz, and the README walks through wiring an external USBasp programmer at 5V (bypassing the badge's onboard 3.3V regulator) to flash new sketches or update the AVR fuses. The repository ships a custom Arduino IDE board-manager package so the badge shows up as "BSides Badge 2015" in the Tools menu, alongside precompiled firmware hex files and both standard and "XL" hardware variants.

The maker's companion blog post from November 2015 covers the same ATmega328P badge doubling as a USBasp programmer itself, suggesting the board was meant to be useful past the con as a general-purpose AVR programming and hacking platform, not just a wearable. No pricing, production quantity, LED count, or display details were found in the repository or the maker's blog, and no photo of an assembled board turned up — only the maker's concept sketch of the PCB outline and connectors, which is used as the entry image here.

## Make your own

Hardware (Eagle schematic/board files, Gerbers) and firmware (Arduino sketches and precompiled hex files with AVR fuse settings) are both published in the [GitHub repo](https://github.com/soynerdito/PepitaBadgeShieldCompatible). To reproduce it: add the repo's Arduino board-manager URL, install the "BSides Badge" board package, select the "BSides Badge 2015" board and a USBasp programmer, then flash `mega32p_16mhz_program_on_reset.hex` (or your own sketch) over 5V power fed through the board's 3.3V-labeled pin.
