---
title: THOTCON 0xB Badge
id: thotcon-2021-thotcon-0xb-badge
layout: badge
parent: THOTCON 0xB (actually held Oct 8-9, 2021, not 2022)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: thotcon-2021
year: 2022
makers:
- name: Rob Rehrig
  url: https://www.robrehrig.com/TC0xB
  role: electronic design, schematic capture, board layout, firmware drivers
- name: Fourfold
  role: badge team / manufacturing
- name: Jay Margalus
  role: workshop presenter
- name: Rudy Ristich
  url: https://github.com/ristich/TC0xB_Samples
  role: workshop presenter, sample firmware
summary: The official badge for THOTCON 0xB (2021) mashes up an NES-style game controller and a circus ticket for that year's Bozo the Clown theme, with capacitive touch buttons, RGB backlighting, and an onboard accelerometer-driven tone synthesizer.
functions: RGB LEDs light up the THOTCON lettering; single-color reverse-mount LEDs sit at the capacitive touch buttons; a piezo buzzer plays circus-themed jingles and button-feedback tones (including "Entry of the Gladiators"); an onboard accelerometer works as a tilt-controlled tone synthesizer; the badge exposes a serial interface and had 2.4GHz Wi-Fi node / IRC connectivity for the badge network.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - console
  - arcade
  - circus
tech:
  mcu: ESP32
  leds:
    count: null
    type: reverse-mount
    note: RGB LEDs behind the THOTCON letters, driven by an IS32FL3731 LED driver, plus single-color reverse-mount LEDs at the capacitive touch buttons.
  display: none
  connectivity:
  - wifi
  - uart
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
  firmware_url: https://github.com/ristich/TC0xB_Samples
  eda_tool: null
links:
- label: badge.gallery/badges/thotcon-0xb-badge
  url: https://badge.gallery/badges/thotcon-0xb-badge
  kind: website
- label: www.robrehrig.com/TC0xB
  url: https://www.robrehrig.com/TC0xB
  kind: website
- label: github.com/ristich/TC0xB_Samples
  url: https://github.com/ristich/TC0xB_Samples
  kind: repo
- label: www.reddit.com/r/Thotcon
  url: https://www.reddit.com/r/Thotcon/
  kind: social
images:
- file: assets/images/badges/thotcon-2021/thotcon-0xb-badge/9bb48a3db0.jpg
  source: "https://www.robrehrig.com/TC0xB"
  credit: "Rob Rehrig"
  caption: "THOTCON 0xB badge, front view"
- file: assets/images/badges/thotcon-2021/thotcon-0xb-badge/21b22f89c3.jpg
  source: "https://www.robrehrig.com/TC0xB"
  credit: "Rob Rehrig"
  caption: "THOTCON 0xB badge, detail"
contact: {}
notes:
- Official THOTCON badge in a retro-controller / circus-ticket form factor with an ESP32 main controller, actually produced for the COVID-delayed Oct 2021 edition (0xB) rather than the calendar year 2022 slot in this catalog's id scheme. Found by the event-year sweep, task thotcon-b.
- The sweep's original makers line read "Fourfold / Rob Rehrig team"; Rob Rehrig's own project page and badge.gallery both credit him for the electronic design specifically, with Fourfold as the broader badge team and Jay Margalus / Rudy Ristich running the badge-hacking workshop, so the makers list was split out accordingly.
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/thotcon-0xb-badge
  title: THOTCON 0xB Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:thotcon-b); event read as ''thotcon-2021''.'
- kind: url
  url: https://www.robrehrig.com/TC0xB
  title: Rob Rehrig - THOTCON 0xB
  accessed: '2026-09-08'
  note: Maker's own project page; confirms design (NES controller / circus ticket, Bozo the Clown theme), ESP32 + IS32FL3731 LED driver, capacitive touch, piezo buzzer, accelerometer tone synth, GPIO0 buffer design note; source of the two saved photos.
- kind: url
  url: https://github.com/ristich/TC0xB_Samples
  title: TC0xB_Samples
  accessed: '2026-09-08'
  note: Workshop sample-firmware repo (Arduino/ESP32 sketches) for the badge; no hardware files or explicit license found, so make_your_own.open_source set to partial.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Core facts (maker, ESP32, LED driver, features, event/theme) confirmed on Rob Rehrig's own project page and corroborated by badge.gallery. Price, quantity made, and availability are not stated anywhere found and are left empty. No hardware design files (schematics/gerbers/EDA) were located, only workshop sample firmware, so open_source is "partial" rather than "yes". Battery/power details and exact LED count are not specified in sources.
last_modified_date: '2026-09-08'
---

The THOTCON 0xB badge was the official electronic badge for THOTCON's 2021 conference (delayed by COVID from its usual spring slot to October, but keeping the "0xB" designation). Designed around an ESP32 microcontroller, it mashes up the look of an NES-style game controller with a circus ticket, playing on that year's Bozo the Clown theme. Rob Rehrig handled the electronic design, schematic capture, board layout, and firmware drivers, working with the broader Fourfold badge team.

The badge lights RGB LEDs behind its THOTCON lettering and single-color reverse-mount LEDs at its capacitive touch buttons, all driven through an IS32FL3731 LED driver chip. A piezo buzzer plays circus-themed jingles and button-feedback tones (including "Entry of the Gladiators"), and an onboard accelerometer doubles as a tilt-controlled tone synthesizer. It also carried a serial interface and 2.4GHz Wi-Fi connectivity for badge-to-badge and IRC features tied to the conference network. Rehrig's write-up notes a small but notable design detail: a two-transistor GPIO0 buffer that frees the pin from DTR load after boot, letting the same pin serve capacitive touch sensing while still allowing firmware uploads over UART.

## Make your own

Full hardware design files (schematics, PCB layout, gerbers) have not been published. Jay Margalus and Rudy Ristich ran a badge-hacking workshop at the conference, and the accompanying sample firmware (Arduino/ESP32 sketches using the Tone32 and SparkFun LIS3DH libraries, plus workshop slides) is available at github.com/ristich/TC0xB_Samples, though no explicit open-source license is stated.
