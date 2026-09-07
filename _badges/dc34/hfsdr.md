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
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
tech:
  mcu: CH32V305
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: approx 75USD with battery, 65USD without battery
  price_usd: 65
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold directly by the maker (Hackin7) around DEF CON 34; approx $75 with battery, $65 without.
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
  accessed: '2026-09-06'
  note: Live WebUSB-based waterfall/config interface for the device, linked from the repo README.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The GitHub repo (built with collaborator rhgndf) documents the hardware/firmware/software in detail but never mentions DEF CON 34 by name - it reads as a general open-source SDR project, possibly originating from a hackathon ('Hack & Roll') credit found in the repo. The DC34 community sheet ties it to Hackin7 with a price of ~$75/$65 and Discord/email contact matching the GitHub account, so it is treated here as the badge/device Hackin7 sold at DC34. Could not find quantity made, LED count/type, battery spec, or an explicit software/hardware license. No independent (press/storefront) coverage of a DC34 sale was found.
last_modified_date: '2026-09-06'
---

HFSDR is an open-source software-defined radio badge built around a CH32V305 microcontroller. It receives signals from 0-300MHz and streams 192kHz I/Q data over USB, either into a browser-based waterfall/spectrum viewer (via WebUSB) or into GNU Radio through the project's Python host tools. A rotary encoder lets it run standalone as well, including a basic FM receiver mode with audio output.

The hardware (KiCad schematics and PCB), CH32V305 firmware, host-side Python drivers, and the Svelte/Vite web UI are all published on GitHub by the maker, who goes by Hackin7 (Terence Chan Zun Mun) and is credited alongside collaborator rhgndf. The project appears to trace back to a hackathon build before being sold as a badge; the DEF CON 34 community badge sheet lists it as new that year at roughly $75 with a battery or $65 without, with contact details (Discord handle and email) matching the maker's GitHub account.

Beyond the repository and its live web-UI demo, no additional press, storefront listing, or photos of the badge in the wild were found, so quantity made, LED details, battery type, and licensing terms are left blank.
