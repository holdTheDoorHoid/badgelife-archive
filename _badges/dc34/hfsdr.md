---
title: HFSDR
id: dc34-hfsdr
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Hackin7
  url: https://github.com/Hackin7
summary: A software-defined-radio badge that tunes 0-300MHz and streams 192kHz I/Q data to a PC over USB, with a standalone FM-receiver mode.
functions: Receives 0-300MHz radio signals; standalone FM radio with audio output; streams 192kHz I/Q data to a host PC over USB/WebUSB for use with a browser-based waterfall display or GNU Radio; rotary encoder cycles onboard modes/LEDs.
look:
  colors:
  - black
  - white
  shape: null
  themes:
  - radio
  - hardware tool
  - kit
tech:
  mcu: CH32V305
  leds:
    count: null
    type: discrete
    note: SMD LEDs supplied in the kit; count not stated
  display: small screen for waterfall/FFT (type and size not stated)
  connectivity:
  - usb
  battery: optional LiPo (sold with or without battery; onboard LiPo charger)
  sao_version: null
get_one:
  price: $65 no battery / $75 with battery / $72 smaller battery / $85 fully soldered
  price_usd: 65
  quantity: ''
  availability: available
  availability_note: 'Uberflux checked 2026-09-07: $65 no-battery kit still listed (36 remaining); battery and fully-soldered variants sold out.'
  distribution:
  - purchase
  - kit
  where: Sold as a mini soldering kit through Hackin7's Uberflux store for DEF CON 34, with variants at $65 (no battery), $75 (with battery), $72 (smaller battery) and $85 (fully soldered).
make_your_own:
  open_source: true
  hardware_url: https://github.com/rhgndf/hfsdr/tree/main/hardware
  firmware_url: https://github.com/rhgndf/hfsdr/tree/main/ch32v305
  eda_tool: KiCad
  notes: Repo also includes a Python/GNU Radio host driver and a Svelte/Vite WebUSB web UI (live at rhgndf.github.io/hfsdr). No LICENSE file was found in the repo, so terms of reuse aren't explicit.
links:
- label: github.com/rhgndf/hfsdr
  url: https://github.com/rhgndf/hfsdr
  kind: repo
- label: HFSDR web UI (WebUSB waterfall)
  url: https://rhgndf.github.io/hfsdr/
  kind: website
- label: uberflux.com/product/HCK-hfsdr
  url: https://uberflux.com/product/HCK-hfsdr
  kind: store
- label: uberflux.com/maker/hackin7
  url: https://uberflux.com/maker/hackin7
  kind: store
- label: github.com/Hackin7
  url: https://github.com/Hackin7
  kind: repo
images:
- file: assets/images/badges/dc34/hfsdr/025f17e18b.png
  source: https://github.com/rhgndf/hfsdr
  credit: Hackin7 / rhgndf
  caption: The HFSDR badge board
contact:
  discord: Hackin7
  emails:
  - zunmun@gmail.com
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 22
  updated: 6/21/2026 16:25:29
  listing: New
- kind: url
  url: https://github.com/rhgndf/hfsdr
  title: 'rhgndf/hfsdr: HFSDR host, firmware and hardware'
  accessed: '2026-09-06'
  note: Confirms function (0-300MHz SDR, 192kHz I/Q over USB, standalone FM mode), CH32V305 MCU, KiCad hardware, open-source firmware/hardware/host-software, and maker credits including Hackin7.
- kind: url
  url: https://github.com/Hackin7
  title: Hackin7 (Terence Chan Zun Mun) - GitHub
  accessed: '2026-09-06'
  note: Confirms maker identity behind the Hackin7 handle; no DEF CON or badge mention on the profile itself.
- kind: url
  url: https://rhgndf.github.io/hfsdr/
  title: HFSDR web UI
  accessed: '2026-09-07'
  note: Live web UI for the device, linked from the repo README as the Web UI (page itself is a JavaScript app; only the title is visible without a browser).
- kind: url
  url: https://uberflux.com/product/HCK-hfsdr
  title: hfsdr - Hackin7 - Uberflux
  accessed: '2026-09-07'
  note: Maker's store listing. Confirms DEF CON 34, sold as a mini soldering kit (PCB, SMA + antenna, encoder, screen, SMD LEDs), up to 300MHz reception, onboard FM demod, waterfall/FFT screen, LiPo charger, web UI config, and the four price variants with stock status.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check 2026-09-07: repo README confirms 0-300MHz, 192kHz I/Q over USB, standalone FM mode, rotary encoder, CH32V305, KiCad, credits (rhgndf design, Hackin7 art/PCB layout, Hack & Roll). The Uberflux listing (already linked, not read by the first pass) confirms the DEF CON 34 tie, kit contents, screen, LiPo charger and prices, so earlier notes claiming no storefront was found were removed. Still unknown: total quantity made (only per-variant sold counts on the store), LED count, screen type/size, and license (no LICENSE file in the repo). PCB colors taken from the maker''s photo.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/hfsdr.glb
  method: kicad
  source_file: hardware/hfsdr.kicad_pcb
  generated: '2026-09-07'
  bytes: 693756
---
HFSDR is an open-source software-defined radio badge built around a CH32V305 microcontroller. It receives signals from 0-300MHz and streams 192kHz I/Q data over USB, either into the project's browser-based web UI or into GNU Radio through the Python host tools. A rotary encoder lets it run standalone as well, including a basic FM receiver mode with audio output, and the board carries a small screen for a waterfall/FFT view.

The hardware (KiCad schematics and PCB), CH32V305 firmware, host-side Python drivers and the web UI are all published on GitHub. The repo credits rhgndf for the schematic and design, Hackin7 (Terence Chan Zun Mun) for the art and PCB layout, and members of the Hack & Roll community, and it draws on the CentSDR project. Hackin7 sold it for DEF CON 34 through Uberflux as a mini soldering kit (PCB with hand-drawn radio artwork, SMA connector and antenna, encoder, screen, SMD LEDs), in no-battery, battery, smaller-battery and fully-soldered variants; when checked in September 2026 only the $65 no-battery kit was still in stock.

No press coverage was found; quantity made, LED count, screen type and licensing terms are left blank.
