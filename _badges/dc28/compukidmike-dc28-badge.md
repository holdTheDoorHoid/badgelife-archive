---
title: DEF CON 28 Car Hacking Village Badge
id: dc28-compukidmike-dc28-badge
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
makers:
- name: compukidmike
  url: https://github.com/compukidmike
- name: MK Factor
  role: manufacturer/store
summary: 'The official DEF CON 28 Car Hacking Village badge, a collaboration between compukidmike and the village that lets you bridge automotive Ethernet devices onto a standard Ethernet network.'
functions: 'Two automotive-Ethernet-to-standard-Ethernet media converters (100Mbps, tool-less twisted-pair terminals on P0/P1, RJ45 jacks on P2/P3); a mode button cycles through 4 blinky LED modes and 4 Ethernet modes (setting Primary/Secondary per port); status shown via amber/green port LEDs and "thruster" LEDs; firmware is field-updatable over USB (mass-storage bootloader).'
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: NXP LPC51U68
  leds:
    count: 25
    type: null
    note: 'Includes port link/activity LEDs (amber/green) and "thruster" blinky LEDs; exact mix of discrete vs addressable not confirmed.'
  display: none
  connectivity:
  - uart
  - usb
  battery: 3x AAA or USB
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: 'Sold through the MK Factor store; MK Factor''s July 2020 post described a "limited number" available at the time.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'Maker states the automotive-Ethernet chip design is covered by an NDA with NXP, so board files/firmware source were not released as of the GitHub repo; the public datasheet reportedly omits the pinout needed to reproduce it.'
links:
- label: github.com/compukidmike/dc28
  url: https://github.com/compukidmike/dc28
  kind: repo
- label: MK Factor - Car Hacking Village Badge - DEF CON 28
  url: https://mkfactor.com/?p=138
  kind: store
images:
  - file: assets/images/badges/dc28/compukidmike-dc28-badge/a24c35af46.jpg
    source: "https://github.com/compukidmike/dc28"
    credit: "compukidmike"
    caption: "Front of the DEF CON 28 Car Hacking Village badge"
  - file: assets/images/badges/dc28/compukidmike-dc28-badge/234175cd73.png
    source: "https://github.com/compukidmike/dc28"
    credit: "compukidmike"
    caption: "Back of the DEF CON 28 Car Hacking Village badge showing the mode button"
contact: {}
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/dc28
  title: compukidmike DC28 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc28''.'
- kind: url
  url: https://github.com/compukidmike/dc28
  title: 'GitHub - compukidmike/dc28: DEFCON 28 Projects'
  accessed: '2026-09-07'
  note: 'README confirms it is the DEF CON 28 Car Hacking Village badge; describes automotive Ethernet converters, mode button, USB firmware update flow, and NDA restriction on releasing board/firmware files. Front/back photo URLs found here.'
- kind: url
  url: https://mkfactor.com/?p=138
  title: Car Hacking Village Badge – Defcon 28 – MK Factor
  accessed: '2026-09-07'
  note: 'MK Factor store post gives the MCU (NXP LPC51U68), PHY chips (NXP TJA1102, 2x Microchip KSZ8091MNX), LED count (25), battery option (3x AAA or USB), and notes limited stock as of July 2020.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No price or exact production quantity found. LED type (addressable vs discrete) not specified by either source. Could not confirm whether compukidmike is an MK Factor team member or an outside collaborator; both names are credited (GitHub repo by compukidmike, store/manufacture by MK Factor). Besides the LPC51U68 MCU, the badge also uses an NXP TJA1102 100Base-T1 dual PHY (automotive Ethernet) and 2x Microchip KSZ8091MNX 100Base-TX PHYs (standard Ethernet), per the MK Factor store page.'
last_modified_date: '2026-09-07'
---

The DEF CON 28 Car Hacking Village badge (2020) was a collaboration between GitHub user compukidmike and the Car Hacking Village, sold through the MK Factor store. Rather than a general-purpose blinky badge, it doubles as a working tool: it contains two automotive-Ethernet-to-standard-Ethernet media converters, letting someone plug a car's single-twisted-pair automotive Ethernet segment into a normal RJ45 network at 100Mbps. Automotive Ethernet ports use tool-less spring terminals for bare twisted-pair wire, while standard RJ45 jacks handle the other side; a rear mode button cycles through four Ethernet-configuration modes (setting Primary/Secondary per port) and four blinky-light modes, with 25 LEDs total providing status and light-show functions.

Under the hood the badge runs an NXP LPC51U68 microcontroller alongside an NXP TJA1102 automotive PHY and two Microchip KSZ8091MNX standard-Ethernet PHYs. It runs on 3x AAA batteries or USB power (USB recommended for the Ethernet modes, since they draw more current and the board can get warm), and firmware can be updated by holding the mode button at power-on to expose a USB mass-storage bootloader.

The GitHub repo (compukidmike/dc28) documents usage but states the automotive-Ethernet chip's design is covered under an NDA with NXP, so schematic/board files and firmware source were not published; the maker noted the public datasheet does not even include the pinout needed to reverse it. MK Factor's July 2020 storefront post described the badges as available in limited quantity, but no price or total production count was found in either source.
