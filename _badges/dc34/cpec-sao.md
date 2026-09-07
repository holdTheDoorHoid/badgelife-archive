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
functions: Four of the board's six red LEDs cycle through button-selectable patterns (clockwise, counterclockwise, flash, random), with the current mode saved to EEPROM; the firmware code does not appear to drive the remaining two LEDs.
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
    note: 0603 SMD red LEDs (D1-D6); firmware only actively drives D1-D4 in the flash-pattern logic
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
  open_source: true
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
status: announced
sources:
- kind: url
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO
  title: DC34-CPEC-SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc34''.'
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO/master/README.md
  title: DC34-CPEC-SAO README
  accessed: '2026-09-07'
  note: Confirms it is the CPEC logo SAO for DEF CON 34; KiCad 6 board, Arduino firmware.
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO/master/DC34-CPEC-SAO-Firmware/DC34-CPEC-SAO-Firmware.ino
  title: DC34-CPEC-SAO-Firmware.ino
  accessed: '2026-09-07'
  note: MCU is ATtiny816 (megaTinyCore, UPDI programming); button-cycled LED flash patterns (clockwise/counterclockwise/flash/random) saved to EEPROM.
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-SAO/master/DC34-CPEC-SAO-Board/DC34-CPEC-SAO-Board.kicad_sch
  title: DC34-CPEC-SAO-Board.kicad_sch
  accessed: '2026-09-07'
  note: Schematic lists six LEDs (D1-D6) valued RED, 0603 SMD, and one switch (SW1).
- kind: url
  url: https://cpec.club
  title: CPEC club site
  accessed: '2026-09-07'
  note: Club's own site (under construction) confirms the club name and IRC/community focus; no pricing, quantity, or photos of the SAO.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass corrected two points from the prior research draft. (1) status was changed from "released" back to "announced": the repo publishes complete design files, but per the guide''s own vocabulary "released" means people have the item, and no source (repo or cpec.club) shows a photo of an assembled unit or any distribution/sale detail -- publishing files is not the same as confirmed distribution. (2) The claim that "six" LEDs cycle through the flash patterns was not supported: the firmware (DC34-CPEC-SAO-Firmware.ino) only calls digitalWrite on GPIO 0-3 (four pins) inside the pattern logic, while the schematic shows six LEDs (D1-D6) and net labels IO1-IO5, so D5 and D6 are not part of the animation the firmware drives. Also worth noting: the firmware file''s own header comments describe it as "DC34-Mech-SAO-Firmware ... for the small mech weapon boards ... configured by different resistors on individual boards" -- likely reused/copy-pasted from the club''s separate Mech-SAO
    product (a different entry in this archive) rather than written fresh for this board, though the README and repo structure do specifically tie this repository to the CPEC logo SAO for DEF CON 34. No photo of the assembled board was found anywhere (the repo only has vector logo art), and no source states price, quantity made, or distribution at DEF CON 34 -- those fields remain empty. The club''s own site (cpec.club) is a bare "under construction" placeholder with no badge information. With these two corrections, everything remaining in the entry is supported by a source that was read.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/cpec-sao.glb
  method: kicad
  source_file: DC34-CPEC-SAO-Board/DC34-CPEC-SAO-Board-panel.kicad_pcb
  generated: '2026-09-07'
  bytes: 500080
---

The DC34-CPEC-SAO is a Shitty Add-On badge carrying the logo of the Cyber Professionals Enthusiast Club (CPEC), designed for DEF CON 34. The board is built around an Adafruit-style ATtiny816 (programmed over UPDI with megaTinyCore) and populates six discrete 0603 red LEDs, though the published firmware's animation logic only drives four of them. A single button cycles the LED animation through four modes -- clockwise, counterclockwise, flash, and random -- with the selected mode persisted to EEPROM so it survives a power cycle.

CPEC published the complete design as open hardware and firmware on GitHub: a KiCad 6 board and schematic, an Arduino sketch, a JLCPCB-formatted BOM and pick-and-place file, and the vector art used for the CPEC logo silkscreen/panel. No photos of an assembled unit, pricing, quantity produced, or distribution details (e.g. free giveaway vs. sold) were found in the repository or on the club's own site, which was still a bare "under construction" placeholder at time of research.
