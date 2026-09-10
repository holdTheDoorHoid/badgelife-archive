---
title: BUSSide
id: bsides-canberra-2018-busside
layout: badge
parent: BSides Canberra 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-canberra-2018
year: 2018
makers:
- name: Silvio Cesare
  url: https://infosectcbr.com.au/
  role: designer
- name: InfoSect
  url: https://infosectcbr.com.au/
summary: The official electronic badge for BSides Canberra 2018, built as a hands-on tool for interfacing with UART, SPI, I2C, and JTAG on other hardware.
functions: Detects UART and JTAG pinouts and dumps SPI and I2C memory on a target device; ships with a Python client and an ESP-based firmware image, and a printed manual walked attendees through using it.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - security
  - learn to solder
tech:
  mcu: ESP (ESP8266/ESP-based, exact part not stated)
  leds: null
  display: null
  connectivity:
  - uart
  - i2c
  - spi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '2000'
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of BSides Canberra 2018.
make_your_own:
  open_source: true
  hardware_url: https://github.com/BSidesCbr/BUSSide
  firmware_url: https://github.com/BSidesCbr/BUSSide/tree/master/FirmwareImages
  eda_tool: null
  license: GPLv3
  notes: Firmware sketches (BUSSide.ino, plus UART/SPI/I2C/JTAG modules) are Arduino-based; flash with esptool from the provided FirmwareImages. Client software is Python-based. A user manual (BUSSideManual.pdf) is included in the repo.
links:
- label: github.com/BSidesCbr/BUSSide
  url: https://github.com/BSidesCbr/BUSSide
  kind: repo
  archived: https://web.archive.org/web/20251218111143/https://github.com/BSidesCbr/BUSSide
- label: busside.com.au
  url: http://busside.com.au
  kind: website
  archived: https://web.archive.org/web/20251122125649/http://busside.com.au/
images: []
contact: {}
notes:
- Electronic badge issued to 2,000 BSides Canberra 2018 delegates, doubling as a hardware-hacking tool interfacing I2C/SPI/UART, with public source and GitHub Pages documentation. Found by the event-year sweep, task bsides-canberra.
- Sweep title/wording matched the maker's own name for the badge ("BUSSide"); no change needed.
status: released
sources:
- kind: url
  url: https://github.com/BSidesCbr/BUSSide
  title: BUSSide
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-canberra); event read as ''BSides Canberra 2018''.'
  archived: https://web.archive.org/web/20251218111143/https://github.com/BSidesCbr/BUSSide
- kind: url
  url: http://busside.com.au
  title: The BUSSide Badge
  accessed: '2026-09-10'
  note: Official project site (resolved via cached IP, DNS for busside.com.au no longer live); confirms it is "The BSides Canberra 2018 Electronic Badge", made by InfoSect/Silvio Cesare, and its UART/SPI/I2C/JTAG functions.
  archived: https://web.archive.org/web/20251122125649/http://busside.com.au/
- kind: url
  url: https://github.com/BSidesCbr/BUSSide/blob/master/README
  title: BUSSide README
  accessed: '2026-09-10'
  note: Confirms GPLv3 license, repo contents (firmware sketches, FirmwareImages, Client, manual PDF), and esptool-based flashing.
- kind: url
  url: https://en.wikipedia.org/wiki/Silvio_Cesare
  title: Silvio Cesare - Wikipedia
  accessed: '2026-09-10'
  note: Background confirmation that Silvio Cesare (InfoSect) is a real security researcher associated with BSides Canberra.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed by the maker's own project site (busside.com.au, reached via a cached IP since the domain no longer resolves in DNS) and the GitHub repo/README. Could not find a photo of the physical badge/PCB in the repo, the manual's cover, or the project site (only InfoSect team headshots and logos were found there) - images left empty. Exact MCU part number, LED count, display, battery, price as distributed (it was a free con badge), and quantity-made corroboration beyond the sweep's "2,000 delegates" figure were not stated by any source read. PCB colors/shape not documented anywhere found.
last_modified_date: '2026-09-10'
---

The BUSSide was the official electronic badge given to attendees of BSides Canberra 2018, designed by Dr Silvio Cesare of InfoSect (the group behind the conference). Rather than being a passive blinky badge, it doubles as a hardware-hacking tool: it can interface with UART, SPI, I2C, and JTAG on other devices, letting a delegate detect UART/JTAG pinouts and dump SPI or I2C memory straight from the badge itself. InfoSect distributed it free to roughly 2,000 delegates as part of the conference badge run.

The project is fully open source under the GPLv3 license. The GitHub repository (BSidesCbr/BUSSide) includes the Arduino-based firmware sketches for the ESP-based microcontroller (a top-level `BUSSide.ino` plus separate UART, SPI, I2C, and JTAG modules), a Python client for talking to the badge, pre-built firmware images for reflashing with `esptool`, and a printed user manual (`BUSSideManual.pdf`) that walked attendees through using the interfacing features.

## Make your own

Hardware and firmware are both published. To build or reflash one: clone the `BSidesCbr/BUSSide` repository, use the Arduino sketches under `BUSSide/` (which depend on the `espsoftwareserial` library) to compile the firmware, or flash one of the pre-built images in `FirmwareImages/` directly with `esptool`. The Python code under `Client/` provides the host-side interface, and `BUSSideManual.pdf` documents how to use the UART/SPI/I2C/JTAG features once flashed.
