---
title: SPIvSPI Blackhat Spy SAO
id: dc27-spivspi-blackhat-spy-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: SPIvSPI (xres0nance, steve/corelit)
  url: https://github.com/SPIvSPI
summary: Spy vs. Spy themed Shitty Add-On for DEF CON 27 in the black-hat spy design, driven by a Silicon Labs EFM8BB10 (8051-core) microcontroller running LED animations authored with the project's own GUI animation tool; the repo holds its dedicated PCB design (SPIvSPI_SAO_Black), schematic, kit assembly notes, firmware and build photos.
functions: LED "blinkenlite" animations authored with the project's own custom GUI animation-generator tool
look:
  colors: [black]
  shape: null
  themes: [spy, security, pop culture]
tech:
  mcu: EFM8BB10F8G (8051 core)
  leds: null
  display: none
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
  hardware_url: https://github.com/SPIvSPI/dc27sao/tree/master/hardware
  firmware_url: https://github.com/SPIvSPI/dc27sao/tree/master/firmware
  eda_tool: null
links:
- label: github.com/SPIvSPI/dc27sao
  url: https://github.com/SPIvSPI/dc27sao
  kind: repo
- label: hackaday.io/project/166811-spivspi-sao-dc27-badge
  url: https://hackaday.io/project/166811-spivspi-sao-dc27-badge
  kind: hackaday
- label: twitter.com/SPIvSPI
  url: https://twitter.com/SPIvSPI
  kind: social
images:
- file: assets/images/badges/dc27/spivspi-blackhat-spy-sao/860a8af82d.jpg
  source: "https://github.com/SPIvSPI/dc27sao"
  credit: "SPIvSPI (xres0nance)"
  caption: "Assembled blackhat-spy SAO PCB"
- file: assets/images/badges/dc27/spivspi-blackhat-spy-sao/69aa14599f.jpg
  source: "https://github.com/SPIvSPI/dc27sao"
  credit: "SPIvSPI (xres0nance)"
  caption: "Blackhat spy artwork/render for the SAO"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/SPIvSPI/dc27sao
  title: SPIvSPI/dc27sao — Blackhat spy & Whitehat spy SAO from Def Con 27
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/SPIvSPI/dc27sao
  title: SPIvSPI/dc27sao README and /img directory
  accessed: '2026-09-07'
  note: Confirmed maker credits (xres0nance hardware/firmware, steve/corelit GUI tool), MIT-style open repo layout (/firmware, /gui, /hardware, /img), and located finished-board photos (svs-black-pcb-photo.jpg, spivspi-blackhat.jpg) used for images.
- kind: url
  url: https://hackaday.io/project/166811-spivspi-sao-dc27-badge
  title: SPIvSPI SAO DC27 Badge — Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed EFM8BB10F8G (8051-core) MCU, DEF CON 27 / 2019 timing (started mid-June 2019, files released by August 15 2019), and Spy vs Spy cartoon inspiration.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >
    Repo and Hackaday.io page confirm the maker, event/year, MCU, and open-source
    hardware/firmware. LED count/type, price, quantity made, and distribution method
    (free drop vs. sale) are not stated on either page; the hardware folder contains
    schematic and kit-notes PDFs (SPIvSPI-black-schematic.pdf, SPIvSPI-Black-Kit-Notes.pdf)
    that likely have LED/BOM detail but were not opened in this pass. A companion
    "whitehat spy" variant exists in the same repo (img/spivspi-whitehat.jpg,
    hardware/SPIvSPI_SAO_White) and may warrant its own entry.
last_modified_date: '2026-09-07'
---

SPIvSPI is a two-badge Shitty Add-On project built for DEF CON 27 (2019), pairing a "blackhat spy" and a "whitehat spy" design based on the classic Spy vs. Spy cartoon characters. This entry covers the blackhat variant. The project was started as a pencil sketch in mid-June 2019 and the finished design files were pushed to GitHub by mid-August 2019, a roughly six-week turnaround the makers called out on their own project page.

The SAO is built around a Silicon Labs EFM8BB10F8G, an 8051-core microcontroller, and runs LED "blinkenlite" animations. Those animations were authored with a custom GUI animation-generator tool the team built specifically for this project, credited to steve/corelit, while xres0nance handled the hardware and firmware. The GitHub repository (SPIvSPI/dc27sao) is fully open, with separate folders for firmware, the GUI tool, and hardware (including a dedicated PCB design, schematic PDF, and kit assembly notes for both the black and white variants), plus build photos covering reflow, panelization, and pick-and-place steps.

Sources found for this pass do not state a price, quantity produced, or how the SAO was distributed (sold, given away, or handed out at a village) — those fields are left empty rather than guessed. The hardware folder's schematic and kit-notes PDFs likely contain LED count/type and BOM detail but were not opened during this research pass.
