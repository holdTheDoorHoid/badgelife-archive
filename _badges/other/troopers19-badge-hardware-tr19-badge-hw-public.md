---
title: Troopers19 badge hardware (tr19-badge-hw-public)
id: other-troopers19-badge-hardware-tr19-badge-hw-public
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2019
makers:
- name: jeffmakes
  url: https://github.com/jeffmakes
summary: The official electronic badge for the Troopers19 security conference (Heidelberg, March 2019), built around an ESP32-WROVER with a 2.9" e-paper display, six WS2812B RGB LEDs, an accelerometer, and a large tactile-button keypad driven by I2C IO expanders.
functions: Full-color e-paper display driven by an ESP32-WROVER; six addressable WS2812B LEDs plus four discrete indicator LEDs; onboard LIS3DHTR accelerometer for motion/orientation input; a large multi-button keypad (dozens of tactile switches read through PCA9539A/PCA9555 I2C expanders) suggesting an interactive menu or game; microSD card slot for storage; USB-C for charging/programming via an onboard CP2102N USB-UART bridge.
look:
  colors:
  - black
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP32-WROVER-I
  leds:
    count: 6
    type: WS2812B
    note: Plus four discrete LTST-C150K indicator LEDs.
  display: 2.9" e-paper (GDEH029A1)
  connectivity:
  - wifi
  - bluetooth
  - usb
  - i2c
  battery: LiPo (MCP73831T charge controller, AP2114H-3.3V regulator)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees of the Troopers19 security conference (Heidelberg, Germany, March 2019); not sold separately as far as sources found show.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/jeffmakes/tr19-badge-hw-public
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/jeffmakes/tr19-badge-hw-public
  url: https://github.com/jeffmakes/tr19-badge-hw-public
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/jeffmakes/tr19-badge-hw-public
  title: Troopers19 badge hardware (tr19-badge-hw-public)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''troopers-2019 (no matching id in events.yml)''.'
- kind: url
  url: https://raw.githubusercontent.com/jeffmakes/tr19-badge-hw-public/master/tr19-badge.kicad/tr19-badge.sch
  title: tr19-badge.sch (KiCad schematic, raw)
  accessed: '2026-09-07'
  note: Component list confirmed the MCU (ESP32-WROVER-I), display (GDEH029A1 e-paper), LEDs (WS2812B x6 + LTST-C150K x4), accelerometer (LIS3DHTR), battery charger (MCP73831T), regulator (AP2114H-3.3), USB-UART bridge (CP2102N), USB-C connector, microSD slot, and a large tactile-switch keypad driven by PCA9539A/PCA9555 I2C IO expanders.
- kind: url
  url: https://raw.githubusercontent.com/jeffmakes/tr19-badge-hw-public/master/gerber/README.txt
  title: gerber/README.txt (fab notes, raw)
  accessed: '2026-09-07'
  note: Confirmed a 4-layer PCB (F/In1/In2/B), panelised 6-up, black matte soldermask with yellow legend; only the hardware repo has no firmware repo linked, so open_source is marked partial.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No matching Troopers event exists in events.yml (only DEF CON/Supercon/SAINTCON/EMF-style ids are present), so event is left as "other" — this badge was made for Troopers19, the Troopers security conference in Heidelberg, Germany, held March 2019. No firmware repository, price, quantity, or photos of the physical badge were found; only the hardware design repo (gerbers, KiCad source, assembly PDFs) is public, so make_your_own.open_source is "partial" rather than "yes". No images of the assembled badge were located (the repo contains no photos, and web search quota was exhausted before press coverage could be checked).
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/troopers19-badge-hardware-tr19-badge-hw-public.glb
  method: kicad
  source_file: tr19-badge.kicad/tr19-badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 842372
---

The Troopers19 badge was the electronic conference badge given to attendees of Troopers, the security conference held annually in Heidelberg, Germany, for its 2019 edition. It was designed by GitHub user jeffmakes (Jeff Gough), whose public repository publishes the full hardware design: KiCad schematics and PCB layout, gerbers, assembly drawings, and fabrication notes for a black, four-layer PCB with yellow silkscreen, panelised six-up for manufacturing.

Electrically the badge centers on an ESP32-WROVER-I module, giving it Wi-Fi and Bluetooth alongside plenty of flash/PSRAM for its 2.9" e-paper display (a Good Display GDEH029A1). It carries six WS2812B addressable RGB LEDs and four smaller discrete indicator LEDs, an LIS3DHTR accelerometer, a microSD card slot for storage, and a large bank of tactile push-buttons read through PCA9539A and PCA9555 I2C IO expanders — enough switches to suggest a menu-driven or game-like interface rather than a single push-button. Power comes from an onboard LiPo battery managed by an MCP73831T charge controller and AP2114H 3.3V regulator, charged and programmed over USB-C via a CP2102N USB-to-UART bridge.

Only the hardware design has been published; no firmware repository, price, production quantity, or photos of the assembled badge turned up in the sources checked, so several fields above are left blank rather than guessed. The same maker went on to publish hardware for later Troopers badges (Troopers 20 and Troopers 23) and a 2023 "Fuccs" shitty add-on, none of which currently have entries in this archive.
