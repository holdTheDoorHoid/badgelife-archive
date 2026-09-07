---
title: IoB Quantum
id: dc28-iob-quantum
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
makers:
- name: trueControl
  url: https://basic.truecontrol.org/database/
  role: hardware/firmware
summary: A power-and-connectivity host badge for badgelife SAO add-ons, with four SAO ports that can back-power accessories and an ESP32-based WiFi mesh chat network.
functions: 'Hosts and back-powers up to four SAO add-ons via I2C-equipped SAO footprints; tracks power draw; joins the "Itero" WiFi mesh network for broadcast/group chat and private messages to up to 25 devices; connects to a "Captive Arcade" WiFi portal; capacitive-touch controls; multiple modes including capacity display, node counting, "party mode", and a buggy "Safe Mode with Networking".'
look:
  colors:
  - gold
  - red
  - copper
  shape: rectangle
  themes:
  - hardware tool
  - radio
tech:
  mcu: ESP32
  leds:
    count: 13
    type: RGB
    note: Nine RGB LEDs on a daughterboard plus four white indicator LEDs (one per SAO port), using upside-down SMD LEDs soldered to expose bare FR4 as a diffuser. Also includes a PSoC5 analog controller and an INA199 current-sense IC for power metering.
  display: none
  connectivity:
  - wifi
  - bluetooth
  - i2c
  inputs:
  - touch
  - capacitive
  power: micro USB (recharging)
  battery: LiPo 3.7V 900mAh
  sao_version: v1.69bis
  sao_ports: 4
get_one:
  price: ''
  price_usd: null
  quantity: approximately 50
  availability: sold_out
  availability_note: 'Sold at DEF CON 28 (August 2020) via shop.truecontrol.org "while supplies last"; not confirmed available as of check on 2026-09-07.'
  distribution:
  - purchase
  where: Sold in person at DEF CON 28 and through shop.truecontrol.org.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Aask42/IoB_DC28
  firmware_url: https://github.com/Aask42/IoB_DC28
  eda_tool: null
  notes: 'Repo hosts both hardware and firmware. The maintainers describe the engineering as "very rushed" and the release as buggy (noted websocket and Safe Mode issues); no license file was found in the repository.'
links:
- label: basic.truecontrol.org/database/dc28/iob-quantum
  url: https://basic.truecontrol.org/database/dc28/iob-quantum/
  kind: website
- label: 'Hackaday: Hands-On with Internet Of Batteries Quantum'
  url: https://hackaday.com/2020/08/09/hands-on-internet-of-batteries-quantum-badge-brings-badgelife-add-ons-the-power-and-internet-they-crave/
  kind: article
- label: 'Hackaday.io: Internet of Batteries (IoB-DC28)'
  url: https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
  kind: hackaday
- label: 'GitHub: Aask42/IoB_DC28 (hardware + firmware)'
  url: https://github.com/Aask42/IoB_DC28
  kind: repo
images:
  - file: assets/images/badges/dc28/iob-quantum/26e9247618.jpg
    source: "https://hackaday.com/2020/08/09/hands-on-internet-of-batteries-quantum-badge-brings-badgelife-add-ons-the-power-and-internet-they-crave/"
    credit: "Hackaday"
    caption: "Front of the IoB Quantum badge, showing the gold-plated copper and red solder mask with capacitive touch pads"
  - file: assets/images/badges/dc28/iob-quantum/643f88626e.jpg
    source: "https://hackaday.com/2020/08/09/hands-on-internet-of-batteries-quantum-badge-brings-badgelife-add-ons-the-power-and-internet-they-crave/"
    credit: "Hackaday"
    caption: "The RGB LED daughterboard of the IoB Quantum badge"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://basic.truecontrol.org/database/dc28/iob-quantum/
  title: IoB Quantum
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc28''. Page has only a title and nav entry, no body text.'
- kind: url
  url: https://hackaday.com/2020/08/09/hands-on-internet-of-batteries-quantum-badge-brings-badgelife-add-ons-the-power-and-internet-they-crave/
  title: 'Hands-On: Internet Of Batteries Quantum Badge Brings Badgelife Add-Ons The Power And Internet They Crave'
  accessed: '2026-09-07'
  note: Hackaday hands-on write-up; source for maker (Whiskey Pirates/trueControl), hardware details, LED design, battery, quantity sold, and images.
- kind: url
  url: https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
  title: Internet of Batteries (IoB-DC28)
  accessed: '2026-09-07'
  note: Maker's Hackaday.io project page; source for team members, MCU details, Itero mesh network, and firmware file reference.
- kind: url
  url: https://github.com/Aask42/IoB_DC28
  title: 'Aask42/IoB_DC28: Safe Mode w/ Networking'
  accessed: '2026-09-07'
  note: Hardware and firmware repository; source for open-source status, feature modes, and license (none found).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The maker''s own trueControl BASIC page for this entry has no body content (title only). Facts here come from Hackaday''s hands-on article, the maker''s Hackaday.io project page, and the GitHub repo, which agree on the core details. Current price and whether any stock remains were not found. No license file was found in the repository, so make_your_own.license is left empty rather than guessed. Badge is part of the "IoB"/"DEF CELL" line spanning DC27''s "Internet of Batteries" and this DC28 "Quantum" edition, but no formal series name is given by the maker, so series is left unset.'
last_modified_date: '2026-09-07'
---

The IoB Quantum (also called DEF CELL QUANTUM, or "Internet of Batteries") is a power-and-connectivity host badge built by trueControl, a member of the Whiskey Pirates crew, for DEF CON 28 in August 2020. Rather than being a standalone wearable, it is designed as the hub of a badgelife add-on ecosystem: it carries four SAO-compatible ports wired for I2C and back-powering, so it can supply current to other people's add-ons (and, per the maker, can itself function as an add-on to a bigger badge) while an onboard INA199 current-sense chip and PSoC5 controller track how much power is being drawn.

An ESP32 module gives the badge WiFi and Bluetooth, which it uses to join "Itero," a WiFi mesh network that lets nearby IoB badges broadcast to a shared group chat or send private messages to up to 25 other devices, plus a "Captive Arcade" WiFi portal. The board's face pairs gold-plated copper with a red solder mask and a row of capacitive touch pads (two under the "DEF" and "CELL" labels, five chevron-shaped pads above them); a daughterboard carries nine RGB LEDs alongside four white per-port indicator LEDs made by soldering SMD LEDs upside down so bare FR4 substrate acts as a diffuser. Power comes from a 3.7V 900mAh LiPo cell, recharged over micro USB.

Around 50 units were sold at DEF CON 28 through shop.truecontrol.org, with the maker noting the engineering was "very rushed" and firmware releases were known to be buggy (websocket and Safe Mode issues). Both hardware and firmware are published on GitHub (Aask42/IoB_DC28), though no license file accompanies the release.
