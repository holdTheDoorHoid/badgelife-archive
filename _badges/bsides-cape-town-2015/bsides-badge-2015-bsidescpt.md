---
title: bsides-badge-2015 (BSidesCPT)
id: bsides-cape-town-2015-bsides-badge-2015-bsidescpt
layout: badge
parent: BSides Cape Town 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cape-town-2015
year: 2015
makers:
- name: dodgymike
  url: https://github.com/dodgymike
summary: 'The official electronic badge for BSides Cape Town 2015, built around a PIC18F2455 microcontroller with USB-to-serial firmware.'
functions: ''
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: PIC18F2455
  leds: null
  display: null
  connectivity:
  - usb
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
  hardware_url: null
  firmware_url: https://github.com/dodgymike/bsides-badge-2015/tree/master/pic-usb-serial
  eda_tool: null
links:
- label: github.com/dodgymike/bsides-badge-2015
  url: https://github.com/dodgymike/bsides-badge-2015
  kind: repo
  archived: https://web.archive.org/web/20260907110030/https://github.com/dodgymike/bsides-badge-2015
images: []
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/dodgymike/bsides-badge-2015
  title: bsides-badge-2015 (BSidesCPT)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''BSides Cape Town 2015''.'
  archived: https://web.archive.org/web/20260907110030/https://github.com/dodgymike/bsides-badge-2015
- kind: url
  url: https://raw.githubusercontent.com/dodgymike/bsides-badge-2015/master/README.md
  title: 'README.md - bsides-badge-2015'
  accessed: '2026-09-07'
  note: 'Confirmed repo description ("BSidesCPT Badge 2015, software, hardware and docs"); README carries no further detail, no images, no price/quantity info.'
- kind: url
  url: https://github.com/dodgymike/bsides-badge-2015/blob/master/pic-usb-serial/usb-serial.X/nbproject/configurations.xml
  title: MPLAB X project configuration
  accessed: '2026-09-07'
  note: 'targetDevice entry gives the MCU as PIC18F2455; only a USB-serial firmware skeleton is present in the repo, no schematic/PCB/BOM files despite the repo description mentioning hardware.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass (2026-09-07): re-fetched the repo root, README, the
    full repo file tree via the GitHub API, the MPLAB X configurations.xml,
    and dodgymike's GitHub profile/repo list; every remaining field and
    body sentence is directly supported by these. The repo (dodgymike/bsides-badge-2015)
    contains only an MPLAB X project for PIC18F2455 USB-to-serial firmware
    (pic-usb-serial/usb-serial.X) plus a two-line README; despite the repo
    description promising "software, hardware and docs," the full tree
    listing confirms no schematic, PCB, BOM, or image files exist. dodgymike's
    profile confirms a Cape Town base and SDR/security focus, and their repo
    list confirms the AND!XOR DC24 badge, DC26 Monero badge PCB, and
    bsidescpt2016badge repos cited in the body. No maker statement on
    functions, LEDs, display, price, quantity, or availability was found, so
    those fields stay empty; independent (non-GitHub) coverage was still not
    searched this pass, which is why confidence stays low.
last_modified_date: '2026-09-07'
---

The bsides-badge-2015 repository is dodgymike's badge project for BSides Cape Town 2015. The only technical detail confirmed from the repository itself is the firmware target: an MPLAB X project implementing USB-to-serial communication on a Microchip PIC18F2455. Beyond that skeleton, the repository does not include schematics, a PCB layout, a bill of materials, or photographs of the finished badge, even though its own description advertises "software, hardware and docs."

No independent write-up, storefront listing, or social media post about this badge could be located in this pass, so its physical appearance, LED count, display, price, production quantity, and distribution are unknown. The maker, dodgymike, is a South Africa-based security and software-defined-radio researcher active in the badgelife space; he also built the AND!XOR DEF CON 24 badge hardware/software and a Monero badge PCB for DEF CON 26, and produced a follow-up badge repo (`bsidescpt2016badge`) for BSides Cape Town 2016.
