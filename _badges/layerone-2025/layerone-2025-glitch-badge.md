---
title: LayerOne 2025 GLiTCh BadgE
id: layerone-2025-layerone-2025-glitch-badge
layout: badge
parent: LayerOne 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: layerone-2025
year: 2025
makers:
- name: Null Space Labs
  url: https://github.com/charlie-x/LayerOne_2025
  role: hardware/firmware (charlie-x)
- name: LayerOne Hardware Hacking Village
  role: challenge content and support
summary: A hardware-hacking platform badge for LayerOne 2025 built around an RP2040 and an iCE40 FPGA, aimed at teaching voltage glitching and embedded debugging rather than being a purely decorative badge.
functions: Voltage glitching against a target via a crowbar circuit and two potentiometers (VR1 sets run voltage, VR2 sets the low/glitch voltage), a basic ~10kHz 12-bit logic analyzer, dual interleaved ADC streaming for power-trace capture, SWD debugging of ARM targets, AVRISP programming of AVR chips, and CMSIS-DAP support. The RP2040 exposes three USB CDC interfaces (main CLI, FPGA link, ADC stream) plus Normal/DAP/DFU USB modes; the onboard iCE40 FPGA can be exercised as if it were a pico-ice board.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - security
tech:
  mcu: RP2040
  leds: 'charlieplexed RGB LED array; count not published, and the maker''s own README notes a routing error on one LED'
  display: none
  connectivity:
  - usb
  battery: powered via USB-C (no onboard battery); solder-jumper pads select 3.3V vs. variable target voltage
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
  hardware_url: https://365.altium.com/files/01BF9671-6FB8-4A9E-9FD1-49A52BA8D165
  firmware_url: https://github.com/charlie-x/LayerOne_2025
  eda_tool: Altium
  notes: 'Firmware/CLI/docs (~30k lines of C/Python/shell) are MIT-licensed on GitHub; the PCB design itself lives only on a proprietary Altium 365 cloud link, not as redistributable Gerbers/schematics, so the badge is only partially open source.'
links:
- label: badge.gallery/badges/layerone-2025-glitch-badge
  url: https://badge.gallery/badges/layerone-2025-glitch-badge
  kind: website
- label: charlie-x/LayerOne_2025 (GitHub repo)
  url: https://github.com/charlie-x/LayerOne_2025
  kind: repo
- label: LayerOne_2025 Altium design files
  url: https://365.altium.com/files/01BF9671-6FB8-4A9E-9FD1-49A52BA8D165
  kind: fab
- label: charlie-x/LayerOne_2025 on DeepWiki
  url: https://deepwiki.com/charlie-x/LayerOne_2025
  kind: doc
images: []
contact: {}
notes:
- Official electronic conference badge for LayerOne 2025. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task con-layerone.
- The sweep's title "LayerOne 2025 GLiTCh BadgE" matches the maker's own README wording exactly, so it was kept as-is.
- The GitHub repo folder is titled "GLiTCh BadgE" throughout; maker credit line reads "charlie-x" for code with "Null Space Labs" / "LayerOne Hardware Hacking Village" providing context, matching the badge.gallery credits page.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/layerone-2025-glitch-badge
  title: LayerOne 2025 GLiTCh BadgE
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''LayerOne 2025''.'
- kind: url
  url: https://github.com/charlie-x/LayerOne_2025
  title: 'charlie-x/LayerOne_2025: LayerOne 2025 GLiTCh BadgE'
  accessed: '2026-09-10'
  note: 'Maker''s own repo/README: confirms MCU (RP2040), FPGA (iCE40), glitching/crowbar/SWD/AVRISP/ADC features, USB modes, LED routing error, Altium (not open) hardware files, MIT-licensed firmware, and maker (charlie-x / Null Space Labs).'
- kind: url
  url: https://365.altium.com/files/01BF9671-6FB8-4A9E-9FD1-49A52BA8D165
  title: LayerOne_2025 Altium project (365.altium.com)
  accessed: '2026-09-10'
  note: 'Linked from the repo README as the hardware design source; confirmed as an Altium cloud project, not a redistributable open file set.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core facts (MCU, FPGA, functions, USB modes, license split) confirmed against the maker''s own GitHub README. Price, quantity made, and availability/distribution are not stated anywhere in the repo or badge.gallery page and are left empty. No photo of the assembled badge PCB was found; the only images in the repo are schematic solder-jumper diagrams and an ADC-stream data plot screenshot, neither of which shows the item itself, so no images were saved. LED count is not published.'
last_modified_date: '2026-09-10'
---

The LayerOne 2025 GLiTCh BadgE is less a wearable conference badge in the usual blinky sense and more a pocket-sized hardware-hacking lab, built by charlie-x of Null Space Labs for LayerOne's Hardware Hacking Village. At its core sits an RP2040 paired with an iCE40 FPGA, plus a voltage glitcher and crowbar circuit for fault-injection attacks against target chips, SWD and AVRISP headers for debugging ARM and AVR targets, and a simple 12-bit logic analyzer and dual-ADC streaming setup for watching power traces during a glitch. Two onboard potentiometers (VR1 and VR2) tune the target's run voltage and glitch voltage, and solder-jumper pads let a builder configure 3.3V vs. variable-voltage operation. Over USB-C the board presents three separate CDC serial interfaces alongside Normal, DAP, and DFU USB modes, and its FPGA can be exercised the same way a pico-ice dev board would be.

The firmware, CLI tooling, and roughly 30,000 lines of documentation and Python/C support scripts are published on GitHub under the MIT license, but the PCB schematic and layout live only behind a proprietary Altium 365 cloud link rather than as redistributable Gerbers, so the project is only partially open source. The maker's own README flags two known hardware issues: a routing error on one LED of the charlieplexed RGB array, and a reversed 3-pin JST SWD connector.

Pricing, production quantity, and how (or whether) it was distributed beyond the Hardware Hacking Village are not documented on any source found; no photograph of the assembled badge was located, only schematic jumper diagrams and a data-plot screenshot from the ADC streaming demo.

## Make your own

1. Clone the firmware/CLI/docs from https://github.com/charlie-x/LayerOne_2025 (MIT licensed).
2. Get the PCB design from the linked Altium 365 project (proprietary cloud link, not a downloadable open file set): https://365.altium.com/files/01BF9671-6FB8-4A9E-9FD1-49A52BA8D165
3. Flash via the RPI-RP2 mass-storage bootloader (drag the .uf2 file on), or use the CLI's reboot-to-DFU command, or hold BOOTSEL at power-on/reset.
4. Follow the repo's `docs/quick_start.md` and `docs/hardware_hacking_guide.md` for wiring solder-jumper pads (switch_pwr, glitch_ctrl, 3v3_ctrl, fet) before use.
