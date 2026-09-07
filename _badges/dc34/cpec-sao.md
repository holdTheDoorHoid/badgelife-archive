---
title: DC34-CPEC-SAO
id: dc34-cpec-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Cyber Professionals Enthusiast Club
  url: https://cpec.club
summary: An open-source SAO carrying the Cyber Professionals Enthusiast Club (CPEC) logo, made for DEF CON 34.
functions: 'Six discrete red LEDs cycle through button-selectable patterns (clockwise, counterclockwise, flash, random), with the current mode saved to EEPROM.'
look:
  colors: []
  shape: null
  themes:
  - logo
tech:
  mcu: ATtiny816
  leds:
    count: 6
    type: discrete
    note: 0603 SMD red LEDs (D1-D6)
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
  hardware_url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO/tree/master/DC34-CPEC-SAO-Board
  firmware_url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO/tree/master/DC34-CPEC-SAO-Firmware
  eda_tool: KiCad
links:
- label: github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO
  kind: repo
- label: cpec.club
  url: https://cpec.club
  kind: website
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO
  title: DC34-CPEC-SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc34''.'
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO/master/README.md
  title: 'DC34-CPEC-SAO README'
  accessed: '2026-09-07'
  note: 'Confirms it is the CPEC logo SAO for DEF CON 34; KiCad 6 board, Arduino firmware.'
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO/master/DC34-CPEC-SAO-Firmware/DC34-CPEC-SAO-Firmware.ino
  title: 'DC34-CPEC-SAO-Firmware.ino'
  accessed: '2026-09-07'
  note: 'MCU is ATtiny816 (megaTinyCore, UPDI programming); button-cycled LED flash patterns (clockwise/counterclockwise/flash/random) saved to EEPROM.'
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO/master/DC34-CPEC-SAO-Board/DC34-CPEC-SAO-Board.kicad_sch
  title: 'DC34-CPEC-SAO-Board.kicad_sch'
  accessed: '2026-09-07'
  note: 'Schematic lists six LEDs (D1-D6) valued RED, 0603 SMD, and one switch (SW1).'
- kind: url
  url: https://cpec.club
  title: 'CPEC club site'
  accessed: '2026-09-07'
  note: 'Club''s own site (under construction) confirms the club name and IRC/community focus; no pricing, quantity, or photos of the SAO.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Design files (KiCad board/schematic, Arduino firmware, BOM, art) are fully published on GitHub, confirming this is a real, built SAO rather than a concept, so status was raised to "released". No photo of the assembled board was found anywhere (the repo only has vector logo art), and no source states price, quantity made, or how it was distributed at DEF CON 34 -- those fields are left empty rather than guessed. The club''s own site (cpec.club) is a bare "under construction" placeholder with no badge information.'
last_modified_date: '2026-09-07'
---

The DC34-CPEC-SAO is a Shitty Add-On badge carrying the logo of the Cyber Professionals Enthusiast Club (CPEC), designed for DEF CON 34. The board is built around an Adafruit-style ATtiny816 (programmed over UPDI with megaTinyCore), driving six discrete 0603 red LEDs. A single button cycles the LED animation through four modes -- clockwise, counterclockwise, flash, and random -- with the selected mode persisted to EEPROM so it survives a power cycle.

CPEC published the complete design as open hardware and firmware on GitHub: a KiCad 6 board and schematic, an Arduino sketch, a JLCPCB-formatted BOM and pick-and-place file, and the vector art used for the CPEC logo silkscreen/panel. No photos of an assembled unit, pricing, quantity produced, or distribution details (e.g. free giveaway vs. sold) were found in the repository or on the club's own site, which was still a bare "under construction" placeholder at time of research.
