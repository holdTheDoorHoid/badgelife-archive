---
title: OSHWDem 2019 Badge (Oshwi 2019)
id: oshwdem-2019-oshwdem-2019-badge-oshwi-2019
layout: badge
parent: OSHWDem 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: oshwdem-2019
year: 2019
makers:
- name: akirasan (Jorge)
  url: https://github.com/akirasan
summary: A two-LED, button-controlled ATtiny85 conference badge made for OSHWDem 2019, shaped after the event's "Oshwi" mascot.
functions: 'Press the button to step through a set list of colors, with each change fading smoothly between the two NeoPixel LEDs rather than snapping; holding the button down at power-on unlocks a hidden demo mode that auto-cycles the colors.'
look:
  colors: []
  shape: null
  themes:
  - mascot
tech:
  mcu: ATtiny85
  leds:
    count: 2
    type: WS2812B
    note: Adafruit NeoPixel library, GRB order; colors set in firmware (green, red, blue, violet, orange, white, yellow, sky blue).
  display: null
  connectivity: []
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
  open_source: yes
  hardware_url: https://github.com/akirasan/oshwdem_2019_badge
  firmware_url: https://github.com/akirasan/oshwdem_2019_badge/tree/master/ATTiny85
  eda_tool: KiCad
  license: GPL-3.0
  notes: 'Repo includes KiCad schematic/PCB/library files, Gerbers, 3D shape files, and two ATtiny85 Arduino sketches (a base color-cycling version and an "_sound" variant with added audio).'
links:
- label: github.com/akirasan/oshwdem_2019_badge
  url: https://github.com/akirasan/oshwdem_2019_badge
  kind: repo
images:
- file: assets/images/badges/oshwdem-2019/oshwdem-2019-badge-oshwi-2019/32dc8a0675.jpg
  source: "https://github.com/akirasan/oshwdem_2019_badge"
  credit: "akirasan"
  caption: "Front of the Oshwi 2019 badge PCB"
- file: assets/images/badges/oshwdem-2019/oshwdem-2019-badge-oshwi-2019/8405cee613.jpg
  source: "https://github.com/akirasan/oshwdem_2019_badge"
  credit: "akirasan"
  caption: "Back of the Oshwi 2019 badge PCB"
contact: {}
notes:
- ATtiny85-based Oshwi-mascot conference badge for OSHWDem 2019, with KiCad design files, Gerbers and firmware; not currently in the archive. Found by the event-year sweep, task oshwdem.
- 'The sweep''s wording "OSHWDem 2019 Badge (Oshwi 2019)" is not the repo''s own title; the repo itself is only named "oshwdem_2019_badge" with README text "Badge Oshwi para la OSHWDem 2019" ("Oshwi badge for OSHWDem 2019"). Kept the existing title since no clearer maker-given name was found.'
status: listed
sources:
- kind: url
  url: https://github.com/akirasan/oshwdem_2019_badge
  title: OSHWDem 2019 Badge (Oshwi 2019)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:oshwdem); event read as ''oshwdem-2019''.'
- kind: url
  url: https://github.com/akirasan/oshwdem_2019_badge/blob/master/ATTiny85/ATTiny85/ATTiny85.ino
  title: ATTiny85.ino firmware source
  accessed: '2026-09-08'
  note: 'Confirmed 2x WS2812-family NeoPixel LEDs on pin 2, a button on pin 3, the color palette, the fade-between-colors behavior, and a hidden hold-button-at-boot demo mode.'
- kind: url
  url: https://raw.githubusercontent.com/akirasan/oshwdem_2019_badge/master/README.md
  title: README.md
  accessed: '2026-09-08'
  note: 'Confirmed README text "Badge Oshwi para la OSHWDem 2019" and no further description.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Fact-checked 2026-09-08 against the maker''s own GitHub repo and firmware source; every non-empty field and factual sentence in the entry is supported. Confirmed via GitHub API: repo license is GPL-3.0, root contains ATTiny85/, Gerber/, shapes3D/, and the KiCad .pro/.sch/.kicad_pcb/.lib files as stated. Re-read ATTiny85.ino directly: 2x NeoPixel on pin 2 (NUMPIXELS=2), button on pin 3, the exact 8-color palette and order (verde/rojo/azul/violeta/naranja/blanco/amarillo/celeste = green/red/blue/violet/orange/white/yellow/sky blue) matching tech.leds.note, the fade-between-colors loop (ajustar_RGB/fundir_a_color), and the hidden hold-button-at-boot demo mode (estado_boton==1023 at setup) all confirmed as described. The programming instructions in "Make your own" match the .ino header comment verbatim (Arduino UNO + ArduinoISP, ATtiny85 board profile/16MHz internal, "Arduino as ISP", optional bootloader burn first). tech.leds.type "WS2812B" is now confirmed directly (previously only inferred from the generic Adafruit_NeoPixel/NEO_KHZ800 timing): OSHWI19.lib defines the LED symbol as "LED_WS2812B" with footprint "LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm". The "mascot" theme and "Oshwi" framing are corroborated independently by third-party sources (Hackaday.io, OSH Park blog, BricoLabs wiki, PCBWay) describing Oshwi as OSHWDem''s recurring octopus mascot. Both saved images are confirmed to be resized copies of the repo''s own imagenes/front.jpg and imagenes/back.jpg (a KiCad 3D render, not a photograph) — same content, verified by side-by-side inspection. Event id oshwdem-2019 matches _data/events.yml exactly. build_index.py --check reports 0 errors for this entry. No contradictions found; price/quantity/availability/distribution/contact/look.colors/look.shape/tech.display/tech.connectivity/tech.battery/tech.sao_version remain correctly empty — still unsupported by any source (note: the repo''s shapes3D/ folder does include a CR2032 holder step file, a possible battery lead, but this is new research beyond this fact-check''s scope and was not pursued). A second ATtiny85 sketch, "ATTiny85_sound", exists as described but its audio behavior was not read in this pass either, consistent with the entry''s existing hedge.'
last_modified_date: '2026-09-08'
---

The OSHWDem 2019 badge was made by akirasan (Jorge) for Spain's Open Source Hardware Demonstration (OSHWDem) conference, styled after "Oshwi," the event's recurring mascot character. It is a small ATtiny85-based board carrying two NeoPixel (WS2812-family) LEDs and a single button: pressing the button steps through a fixed list of eight colors, with the firmware smoothly fading each LED from its old color to the new one rather than switching instantly. Holding the button down at power-on unlocks a hidden "demo mode" that runs the color-cycling effect automatically.

The full design is published on GitHub under GPL-3.0, including KiCad schematic and PCB files, Gerbers, footprint/3D-shape libraries, and two Arduino sketches for the ATtiny85 — a base color-cycling version and a second "_sound" variant that appears to add audio, though its behavior was not verified in detail. No price, production quantity, or distribution details were found; the repository is a pure open-hardware release rather than a storefront listing, and no outside coverage of the badge turned up in a search.

## Make your own

Everything needed to build the badge is in the [GitHub repo](https://github.com/akirasan/oshwdem_2019_badge): open `OSHWI19.pro`/`OSHWI19.sch`/`OSHWI19.kicad_pcb` in KiCad for the design, or send the files in `Gerber/` straight to a fab. To program the ATtiny85, the README-linked build notes call for an Arduino Uno running the "ArduinoISP" example sketch as the programmer, the ATtiny85 board profile (internal 16 MHz) selected in the Arduino IDE, and "Arduino as ISP" as the upload method; burning the bootloader first is recommended on a fresh chip. The firmware sketches live under `ATTiny85/`.
