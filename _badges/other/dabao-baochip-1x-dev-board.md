---
title: Dabao (Baochip-1x dev board)
id: other-dabao-baochip-1x-dev-board
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 2026
makers:
- name: Andrew "bunnie" Huang
  url: https://www.bunniestudios.com/blog/
summary: A low-cost evaluation board for the Baochip-1x, a "mostly-open" RISC-V microcontroller built for hardware-inspectable, high-assurance applications.
functions: General-purpose embedded development. The Baochip-1x pairs a 350 MHz Vexriscv main core with the "BIO" — four 700 MHz PicoRV I/O coprocessor cores that can bit-bang protocols, drive LED strips, or render simple animations independent of the main CPU.
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - hardware tool
tech:
  mcu: Baochip-1x (350 MHz Vexriscv RV32-IMAC, with 4x 700MHz PicoRV RV32-EMC I/O coprocessor cores)
  leds: null
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: none
get_one:
  price: $12 (+ $10 US / $18 worldwide shipping)
  price_usd: 12
  quantity: ''
  availability: sold_out
  distribution:
  - crowdfunding
  - preorder
  where: Crowdfunded on Crowd Supply (funded March 2026, 1,066 backers, $40,482 raised); "we will resume taking orders once the next production run is confirmed" as of the September 2026 check.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/baochip/dabao
  firmware_url: https://github.com/baochip/baochip-1x
  eda_tool: KiCad
  notes: 'The Dabao board files and the Xous OS are fully open source. The Baochip-1x SoC RTL is "mostly open" (per the maker) rather than fully open; the bootloader and OS are open source and reproducible.'
links:
- label: www.hackster.io/news/andrew-bunnie-huang-prepares-the-dabao-a-dev-board-for-baochip-s-mostly-open-x1-risc-v-mcu-1b7cad7fa2ea
  url: https://www.hackster.io/news/andrew-bunnie-huang-prepares-the-dabao-a-dev-board-for-baochip-s-mostly-open-x1-risc-v-mcu-1b7cad7fa2ea
  kind: article
- label: Crowd Supply — Dabao Evaluation Board for Baochip-1x
  url: https://www.crowdsupply.com/baochip/dabao
  kind: store
- label: GitHub — baochip/dabao (board files)
  url: https://github.com/baochip/dabao
  kind: repo
- label: GitHub — baochip/baochip-1x (SoC RTL)
  url: https://github.com/baochip/baochip-1x
  kind: repo
- label: bunnie's blog — Baochip-1x announcement
  url: https://www.bunniestudios.com/blog/2026/baochip-1x-a-mostly-open-22nm-soc-for-high-assurance-applications/
  kind: article
images:
  - file: assets/images/badges/other/dabao-baochip-1x-dev-board/c238b37d38.jpg
    source: "https://www.crowdsupply.com/baochip/dabao"
    credit: "Baochip / Crowd Supply"
    caption: "Dabao evaluation board for the Baochip-1x RISC-V microcontroller"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- 'Not made for, or tied to, a specific hacker convention. It is a commercial/crowdfunded product from Baochip (Andrew "bunnie" Huang''s company, based in Singapore); a talk on the accompanying Xous OS was given at 39C3 (Chaos Communication Congress, Dec 2025/Jan 2026), but that con has no entry in events.yml and the board itself was not distributed there. Left under "other".'
status: released
sources:
- kind: url
  url: https://www.hackster.io/news/andrew-bunnie-huang-prepares-the-dabao-a-dev-board-for-baochip-s-mostly-open-x1-risc-v-mcu-1b7cad7fa2ea
  title: Dabao (Baochip-1x dev board)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other''.'
- kind: url
  url: https://www.crowdsupply.com/baochip/dabao
  title: Dabao Evaluation Board for Baochip-1x — Crowd Supply
  accessed: '2026-09-07'
  note: Primary source for specs, pricing, campaign status, open-source status, links, and the product image; maker's own crowdfunding page.
- kind: url
  url: https://www.bunniestudios.com/blog/2026/baochip-1x-a-mostly-open-22nm-soc-for-high-assurance-applications/
  title: 'Baochip-1x: A Mostly-Open, 22nm SoC for High Assurance Applications — bunnie''s blog'
  accessed: '2026-09-07'
  note: Maker's own announcement post confirming the Crowd Supply pre-order and open-RTL claims.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'No LED count, no distinct "shape" beyond a rectangular PCB, and no battery spec are given by any source — left null/empty. Quantity of units made is not stated (campaign mentions up to ~3,500 boards possible across two wafer batches, but that is a production ceiling, not a confirmed run size, so quantity was left blank). Availability is listed sold_out/paused because Crowd Supply states orders are paused pending the next production run as of the September 2026 check; it may reopen.'
last_modified_date: '2026-09-07'
---

The Dabao is a low-cost evaluation board built around the Baochip-1x, a "mostly-open" RISC-V system-on-chip designed by Andrew "bunnie" Huang's company Baochip. Rather than being made for a specific hacker convention, it's a commercial hardware-security product: the Baochip-1x pairs a 350 MHz Vexriscv main CPU with a quad-core 700 MHz "BIO" I/O coprocessor, on-chip cryptographic accelerators, key stores, and physical attack countermeasures, and ships in a package designed to support IRIS (Infra-Red, In-situ) optical inspection of the actual transistors, so owners can visually verify the silicon rather than trusting it blindly. The board itself is a cost-optimized two-layer PCB exposing 20 I/O pins and a USB-C connector, running a Rust-based operating system called Xous.

Baochip crowdfunded the Dabao on Crowd Supply, where the campaign funded in March 2026 with 1,066 backers and $40,482 raised against a $1 token goal; boards were priced at $12 plus shipping. As of this check, Crowd Supply lists it as available for pre-order but paused pending confirmation of the next production run, with prior orders having shipped in batches tied to Baochip-1x wafer lots (an initial ~500 chips from an engineering lot, with up to ~3,000 more from a full production run). The Dabao board design and the Xous OS are fully open source (KiCad files on GitHub); the Baochip-1x SoC's RTL is described by the maker as "mostly open" rather than fully open, and the bootloader is open source and independently reproducible.
