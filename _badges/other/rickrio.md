---
title: RickRio
id: other-rickrio
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: unknown
event: other
year: 0
makers:
- name: wrickert
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/wrickert/RickRio
  url: https://github.com/wrickert/RickRio
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: not_an_item
sources:
- kind: url
  url: https://github.com/wrickert/RickRio
  title: RickRio
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://api.github.com/repos/wrickert/RickRio/contents/Schematics
  title: 'wrickert/RickRio: Schematics directory listing'
  accessed: '2026-09-07'
  note: 'Lists Rick_LiteX-CNC.kicad_sch/pcb, EPC5.kicad_sch, RPi_CM4.kicad_sch, Power.kicad_sch, CNC_IO.kicad_sch — an FPGA CNC controller board, not a badge or SAO.'
- kind: url
  url: https://api.github.com/repos/wrickert/RickRio/contents/Documents
  title: 'wrickert/RickRio: Documents directory listing'
  accessed: '2026-09-07'
  note: 'Datasheets for the Lattice iCE40/ECP5 FPGA family and icebreaker-bitsy reference schematics, confirming an FPGA dev/CNC-control context.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    This GitHub repo is not a conference badge or SAO. Its contents (Rick_LiteX-CNC.kicad_pcb/sch,
    a Raspberry Pi CM4 IO schematic, an EPC5 (ECP5 FPGA) schematic, a CNC_IO schematic, and reference
    datasheets/schematics for Lattice iCE40/ECP5 FPGAs and the icebreaker-bitsy board) describe an
    FPGA-based CNC controller board built around a Raspberry Pi Compute Module 4 and a LiteX SoC —
    a personal hobbyist hardware project with no evident tie to any hacker conference. The README
    contains only the repo title. No badge/SAO features, event, year, price, or images were found.
    The maker's GitHub handle (wrickert) also appears in the archive on dc33-neosword (NeoSword,
    Untitled Electronics), a separate and unrelated item, so this is not a duplicate of that entry.
last_modified_date: '2026-09-07'
---

This repository, `wrickert/RickRio`, is not a hacker-conference badge or SAO. Its KiCad schematics and PCB files describe **Rick_LiteX-CNC**, an FPGA-based CNC motion-control board built around a Raspberry Pi Compute Module 4 for I/O and a Lattice ECP5 FPGA running a LiteX soft SoC, with a dedicated `CNC_IO` schematic and power section. The `Documents` folder holds reference material for Lattice iCE40/ECP5 FPGAs and the icebreaker-bitsy dev board, consistent with a from-scratch FPGA hardware project rather than con swag.

The README contains only the project name, and nothing in the repo — commits, file names, or documentation — references a conference, an event year, or a distribution/sale channel. This entry is retained in the archive only as a record that the link was checked and found not to be a badge or SAO.
