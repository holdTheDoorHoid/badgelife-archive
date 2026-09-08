---
title: h-c0n 2026 CTF BADge
id: h-c0n-2026-h-c0n-2026-ctf-badge
layout: badge
parent: h-c0n 2026 (VI edicion)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: h-c0n-2026
year: 2026
makers:
- name: David Reguera "Dreg" (therealdreg), with Adria Perez Montoro (@b1n4ri0) and Antonio Vazquez Blanco (@antoniovazquezblanco)
summary: "A fully functional RP2350 dev board handed out at h-c0n 2026, wrapped in a firmware-teardown and exploitation CTF built on the RISC-V Hazard3 core."
functions: "Runs a hardware-hacking CTF: participants extract and reverse the UF2 firmware, analyze the RISC-V binary in Ghidra, and exploit bugs (including buffer overflows) to capture flags; also usable afterward as a general-purpose RP2350 dev board."
look:
  colors: []
  shape: null
  themes:
  - ctf
  - security
  - hardware tool
tech:
  mcu: RP2350
  leds:
    count: 1
    type: discrete
    note: "Single SMD LED on GPIO 25 for status/visual feedback."
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: "€10"
  price_usd: null
  quantity: ''
  availability: limited
  availability_note: "Limited quantity distributed in person at conference registration, Feb 6-7 2026, with a waitlist for extra units; no source confirms current sold-out status, checked 2026-09-08."
  distribution:
  - purchase
  where: "Sold in person at h-c0n 2026 (Madrid) conference registration; a waitlist was offered for additional units."
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/therealdreg/hcon2026hwctf
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: MIT
  fab_url: null
  notes: "Repo publishes the UF2 CTF firmware, Ghidra scripts/processor definitions, and RISC-V exploitation writeups/tutorials under MIT; no PCB design files (schematic/gerbers) were found published."
links:
- label: github.com/therealdreg/hcon2026hwctf
  url: https://github.com/therealdreg/hcon2026hwctf
  kind: repo
- label: www.h-c0n.com/2025/12/ctf-badge-hc0n2026.html
  url: https://www.h-c0n.com/2025/12/ctf-badge-hc0n2026.html
  kind: website
- label: badge.gallery/badges/h-c0n-2026-ctf-badge
  url: https://badge.gallery/badges/h-c0n-2026-ctf-badge
  kind: website
- label: www.hackplayers.com/2026/02/writeups-ctf-hardware-hacking-h-c0n-2026.html
  url: https://www.hackplayers.com/2026/02/writeups-ctf-hardware-hacking-h-c0n-2026.html
  kind: article
- label: blog.elhacker.net/2026/02/writeups-ctf-hardware-hacking-h-c0n-2026.html
  url: https://blog.elhacker.net/2026/02/writeups-ctf-hardware-hacking-h-c0n-2026.html
  kind: article
images:
  - file: assets/images/badges/h-c0n-2026/h-c0n-2026-ctf-badge/d63abc55cc.png
    source: "https://www.h-c0n.com/2025/12/ctf-badge-hc0n2026.html"
    credit: "h-c0n / Hackplayers"
    caption: "The h-c0n 2026 CTF BADge, an RP2350-based dev board handed out at the conference"
contact: {}
notes:
- Official electronic conference badge for h-c0n 2026 (Hackplayers, Madrid), built on RP2350/RP2354 (RISC-V Hazard3) as a functional dev board wrapped in a firmware-teardown/reversing CTF, designed by David Reguera with public firmware and writeups released after the contest. Found by the event-year sweep, task con-navaja-negra.
status: released
sources:
- kind: url
  url: https://github.com/therealdreg/hcon2026hwctf
  title: h-c0n 2026 CTF BADge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-navaja-negra); event read as ''h-c0n 2026''.'
- kind: url
  url: https://github.com/therealdreg/hcon2026hwctf
  title: therealdreg/hcon2026hwctf
  accessed: '2026-09-08'
  note: "Confirmed makers, RP2350/Hazard3 MCU, single status LED on GPIO 25, USB connectivity, published UF2 firmware + Ghidra scripts + writeups under MIT license; no hardware design files found in repo."
- kind: url
  url: https://www.h-c0n.com/2025/12/ctf-badge-hc0n2026.html
  title: "CTF BADge #hc0n2026"
  accessed: '2026-09-08'
  note: "Confirmed event/date (h-c0n 2026, 6th edition, Feb 6-7 2026, Madrid), price (EUR 10), in-person distribution at registration with a waitlist, and the badge photo used above."
research:
  status: verified
  confidence: high
  last_checked: '2026-09-08'
  notes: "Fact-check re-confirmed the repo (RP2350/Hazard3, single SMD LED on GPIO 25, USB, MIT license, firmware+Ghidra scripts only, no PCB/gerber files) and the h-c0n event page (price EUR10, in-person distribution Feb 6-7 2026, waitlist for extra units) directly, plus the image against its source page. Corrected get_one.availability from 'sold_out' to 'limited': no source (h-c0n page, hackplayers writeup, or badge.gallery) actually states the badge sold out, only that quantity was limited with a waitlist. Exact LED count/type beyond the single GPIO-25 status LED, and any display/battery details, were not stated anywhere found. Quantity made was not disclosed."
last_modified_date: '2026-09-08'
---

The h-c0n 2026 CTF BADge is the official electronic badge of h-c0n 2026 (Hackplayers' Hacking Conference, 6th edition) in Madrid, designed by David Reguera ("Dreg") with Adria Perez Montoro and Antonio Vazquez Blanco. Rather than a purely decorative badge, it is a fully functional RP2350 development board (RISC-V Hazard3 core) with a single status LED on GPIO 25 and USB connectivity, sold to attendees for €10 at in-person registration on February 6-7, 2026, in limited quantity, with a waitlist offered for extra units.

The badge doubled as the venue for the "CTF BADge" hardware-hacking competition, which ran from the afternoon of February 6 through February 13, 2026 (or until three participants captured every flag). Challengers extracted and reverse-engineered the board's UF2 firmware and exploited RISC-V-specific bugs, including buffer overflows, using Ghidra and RISC-V tooling. After the contest, the organizers published the firmware image, Ghidra processor definitions and analysis scripts, exploitation tutorials, and winners' writeups on GitHub under the MIT license; no PCB schematic or gerber files were found in the release, so the hardware design itself does not appear to be open-sourced, only the firmware and CTF materials.

## Make your own

The `ctf.uf2` firmware and Ghidra scripts/processor definitions are published at github.com/therealdreg/hcon2026hwctf under the MIT license, along with RISC-V exploitation tutorials that use the Spike emulator. No hardware files (schematic, PCB layout, or BOM) were found published, so building the physical board from scratch is not currently possible from what's public — the repo is oriented toward the firmware/CTF side.
