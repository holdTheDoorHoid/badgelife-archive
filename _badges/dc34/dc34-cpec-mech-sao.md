---
title: DC34 Mech SAO (weapon plug-ins)
id: dc34-dc34-cpec-mech-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Cyber Professionals Enthusiast Club (CPEC)
  url: https://cpec.club
summary: A family of five weapon-themed SAO plug-in boards (missile, gatling/machine gun, laser, fist, sword) for the CPEC DEF CON 34 "MechBattle" Badge; each runs the same ATtiny816 Adafruit-seesaw I2C firmware with its identity set by onboard ID resistors, so the badge's ESP32-S3 MCU can detect which weapon is plugged into each of its three SAO slots and feed that into a battle-calculator game.
functions: 'Identifies itself over I2C (Adafruit seesaw protocol) to the host badge''s three SAO ports so the badge''s onboard "battle calculator" game logic knows which of five weapons (missile, gatling, laser, fist, sword) is plugged into each slot; purely a game-identity peripheral, no LEDs or display of its own confirmed.'
look:
  colors: []
  shape: null
  themes:
  - robot
  - hardware tool
tech:
  mcu: ATtiny816
  leds: null
  display: null
  connectivity:
  - i2c
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
  hardware_url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Mech-SAO
  firmware_url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Mech-SAO/tree/master/DC34-Mech-SAO-Firmware
  eda_tool: KiCad
  notes: 'Five KiCad 6 board variants (fist, gatling, laser, missile, sword) share one Arduino firmware sketch built on the Adafruit ATtiny817-seesaw I2C library; each board reports its identity to the badge by pulling ID pins low with onboard resistors. A companion breadboard demo (eggsactly/DcC4-Mech-SAO-Plugin-Demo, later mirrored into the CPEC org) validates the hot-plug I2C concept: the badge''s ESP32 scans all three SAO slots and reports which weapon (if any) is present in each, e.g. "SAO 1: laser 4".'
links:
- label: github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Mech-SAO
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Mech-SAO
  kind: repo
- label: github.com/eggsactly/DcC4-Mech-SAO-Plugin-Demo
  url: https://github.com/eggsactly/DcC4-Mech-SAO-Plugin-Demo
  kind: repo
- label: github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Mech-SAO-Plugin-Demo
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Mech-SAO-Plugin-Demo
  kind: repo
- label: github.com/Cyber-Professionals-Enthusiast-Club/DC34-Mech-Badge
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC34-Mech-Badge
  kind: repo
- label: github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Badge
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Badge
  kind: repo
- label: github.com/Cyber-Professionals-Enthusiast-Club
  url: https://github.com/Cyber-Professionals-Enthusiast-Club
  kind: repo
- label: cpec.club
  url: https://cpec.club
  kind: website
images: []
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Mech-SAO
  title: DC-34-Mech-SAO - Kicad 6 design files for the CPEC DEFCON 34 Badge SAO pluggin weapon and power ups
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC-34-Mech-SAO/master/README.md
  title: DC-34-Mech-SAO README
  accessed: '2026-09-07'
  note: Describes repo structure (art, KiCad project, Arduino firmware, libraries) and points to the eggsactly firmware demo repo.
- kind: url
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Mech-SAO/tree/master
  title: DC-34-Mech-SAO file tree
  accessed: '2026-09-07'
  note: 'Confirms five weapon PCB variants (fist-03, gatling-01, laser-02, missile-00, sword-04) plus a panel file, matching art assets fist/laser/machine_gun/missile_launcher/sword.svg; JLCPCB BOM lists "Attiny-816" as the MCU.'
- kind: url
  url: https://raw.githubusercontent.com/eggsactly/DcC4-Mech-SAO-Plugin-Demo/master/README.md
  title: DC34-Mech-SAO-Plugin-Demo README
  accessed: '2026-09-07'
  note: Explains the hot-pluggable I2C/seesaw concept, sample query_sao() output identifying a "laser" SAO, and that it was tested on an ESP-32 at 240 MHz.
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC34-Mech-Badge/master/README.md
  title: DC 34 MechBattle Badge README
  accessed: '2026-09-07'
  note: Confirms the host badge is CPEC's "DC34 MechBattle Badge" with menu/game logic and a battle-calculator concept, still described as "not final."
- kind: url
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC-34-Badge
  title: DC-34-Badge (host badge hardware repo)
  accessed: '2026-09-07'
  note: Separate hardware repo for the same badge; documents an ESP32-S3 MCU, three SAO 1.69bis/I2C ports, 2.2" 320x240 display, WiFi/BLE, buttons, rumble motor, six LEDs, buzzer and photoresistor.
- kind: url
  url: https://cpec.club
  title: CPEC club homepage
  accessed: '2026-09-07'
  note: Site marked "under construction" at time of check; no price, quantity, or photos of the badge/SAOs found; has an unpopulated Shop page.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Maker's own repos and READMEs confirm the concept, the five weapon variants, the
    ATtiny816 MCU (per JLCPCB BOM) and seesaw I2C protocol, and the host badge (an
    ESP32-S3 "MechBattle" badge with three SAO ports). No pricing, quantity made, or
    distribution method found; CPEC's own site is still under construction and has no
    shop listing or product photos yet, and no photos of an assembled SAO or badge
    turned up in web/press search, so images and get_one fields are left empty rather
    than guessed. tech.leds and tech.display left null: no LEDs or display are
    mentioned for the SAO itself in any source (only the host badge has a display and
    LEDs). Firmware README documentation references the "Adafruit ATtiny817-seesaw"
    Arduino library/dependency page even though the actual BOM'd chip is an ATtiny816;
    this discrepancy is in the maker's own materials, not introduced here.
last_modified_date: '2026-09-07'
---

CPEC (Cyber Professionals Enthusiast Club) built a set of five interchangeable weapon-themed SAOs — missile, gatling/machine gun, laser, fist, and sword — for its DEF CON 34 "MechBattle" badge. Each weapon is its own small PCB carrying an ATtiny816 running Adafruit's seesaw I2C firmware, with onboard resistors setting a unique identity so the badge can tell which weapon occupies which of its three SAO slots. The host badge (documented in a separate CPEC repo) is an ESP32-S3 board with a 2.2" color display, WiFi/BLE, six LEDs, a rumble motor, and game/menu firmware described by the maker as a "battle calculator" for turning the plugged-in weapons into gameplay — CPEC's own README calls this second iteration of the firmware "not final."

The hot-plug I2C mechanism was proven out first as a standalone breadboard demo (by contributor eggsactly, later mirrored into the CPEC GitHub org) showing an ESP32 scanning all three SAO ports and correctly reporting, for example, a laser SAO present in slot 1. All hardware (KiCad 6 project files, art, and BOM) and firmware for the weapon SAOs are published on GitHub as open source.

No pricing, production quantity, or distribution details were found — CPEC's public site was still marked "under construction" with an empty shop page at the time of this research, and no photos of an assembled weapon SAO or the badge itself turned up in a web search, so those fields and the image gallery are left blank.
