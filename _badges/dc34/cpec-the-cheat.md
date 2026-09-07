---
title: DC34-CPEC-The-Cheat
id: dc34-cpec-the-cheat
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Cyber Professionals Enthusiast Club
  url: https://github.com/Cyber-Professionals-Enthusiast-Club
summary: A small ATtiny816-based SAO with three programmable LEDs, made by the Cyber Professionals Enthusiast Club (CPEC) to plug into their own DEF CON 34 "Mech" badge.
functions: Runs a firmware LED-cycling demo (a four-state "landed / inflight up / apogee / inflight down" sequence across three LEDs); the ATtiny816 is user-programmable via UPDI for custom light patterns.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ATtiny816
  leds:
    count: 3
    type: discrete
    note: Driven directly from GPIO pins 1-3 of the ATtiny816; reference firmware cycles them in a rocket-flight-themed pattern.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-The-Cheat/tree/master/DC34-CPEC-The-Cheat-Board
  firmware_url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-The-Cheat/tree/master/DC34-CPEC-The-Cheat-Firmware
  eda_tool: KiCad
links:
- label: github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-The-Cheat
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-The-Cheat
  kind: repo
- label: CPEC DEF CON 34 "Mech" badge (host board this SAO plugs into)
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Badge
  kind: repo
images: []
contact: {}
notes:
- The repo's README calls it a "Shitty Add On Board (SAO)"; no separate name beyond "The Cheat" was found.
status: released
sources:
- kind: url
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-The-Cheat
  title: DC34-CPEC-The-Cheat
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 34''.'
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-The-Cheat/master/README.md
  title: DC34-CPEC-The-Cheat README
  accessed: '2026-09-07'
  note: Confirms it is a SAO with KiCad 6 board files and an Arduino firmware project; directory structure.
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC34-CPEC-The-Cheat/master/DC34-CPEC-The-Cheat-Firmware/DC34-CPEC-The-Cheat-Firmware.ino
  title: DC34-CPEC-The-Cheat-Firmware.ino
  accessed: '2026-09-07'
  note: Identifies the MCU as an ATtiny816 (megaTinyCore, UPDI programming) driving 3 LEDs on GPIO 1-3 with a landed/inflight/apogee blink sequence.
- kind: url
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Badge
  title: DC-34-Badge (CPEC's DEF CON 34 badge repo)
  accessed: '2026-09-07'
  note: Confirms CPEC independently designed its own DEF CON 34 "Mech" badge with three SAO 1.69bis/I2C ports, which this SAO is built to plug into.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (MCU, LED behavior, open-source status, host badge) come from the maker''s own repos. Could not find: price, quantity made, distribution method, or whether it was ever actually handed out at DEF CON 34 versus only published as a design. No photos of the assembled board were found -- the repo''s /art directory only contains vector logo/QR/graphic SVGs (CPEC.svg, cpec_qr.svg, rat-bite-1-inch.svg, the_cheat.svg), not photos of the physical item, so none were saved per the image guidelines. No PCBWay/OSH Park shared-project page specific to this SAO was found (a PCBWay commit exists in the repo history but no public share link was located). No license file is present in the repo despite hardware and firmware both being published.'
last_modified_date: '2026-09-07'
---

"The Cheat" is a Shitty Add-On (SAO) built by the Cyber Professionals Enthusiast Club (CPEC), a group that also designed its own independent "Mech" badge for DEF CON 34 complete with a 2.2" display and three SAO 1.69bis/I2C ports. The Cheat is meant to plug into that host badge (or any board with a compatible SAO header) and adds three LEDs driven by an ATtiny816 microcontroller.

The reference firmware, written for the Arduino IDE with Spence Konde's megaTinyCore, cycles the three LEDs through a four-state sequence labeled LANDED, INFLIGHT_UP, APOGEE, and INFLIGHT_DOWN -- a simple rocket-flight-themed blink pattern rather than a functional sensor readout. The board is programmed over UPDI rather than a traditional ISP header, reflecting the newer 0/1/2-series ATtiny family.

CPEC published the full project on GitHub: KiCad 6 schematic and PCB files, the Arduino firmware sketch, and BOMs formatted for both PCBWay and JLCPCB fabrication, making it straightforward for someone else to reproduce the board. No information was found about how many were made, what it cost, or how (or whether) it was distributed at DEF CON 34 -- the archive only has the maker's design-file repository to go on.
