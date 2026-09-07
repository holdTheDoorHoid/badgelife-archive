---
title: Bender SAO (AND!XOR DC27)
id: dc27-bender-sao-and-xor-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: AND!XOR
  url: https://andnxor.com/
summary: A DEF CON 27 SAO add-on from AND!XOR that brings back Bender, the team's original mascot, after the main DC27 badge switched to a new character design.
functions: Includes an on-board microcontroller with a hidden serial output; other AND!XOR add-ons from the same year (notably the Doom SAO) could read that output over the shared I2C/SAO header.
look:
  colors: []
  shape: robot
  themes:
  - robot
  - mascot
  - sci-fi
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Given out by AND!XOR alongside the main DC27 badge as part of a set of three add-ons (Bender, Audio Reactive SAO rev 6, Doom SAO rev 1); part of the team''s fundraising effort to make the DC27 badge free at the con.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes
  url: https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
  kind: article
- label: AND!XOR DC27 Badge (Hackaday.io project)
  url: https://hackaday.io/project/164346-andxor-dc27-badge
  kind: hackaday
- label: AND!XOR sao-reference-designs (GitHub)
  url: https://github.com/ANDnXOR/sao-reference-designs
  kind: repo
images:
  - file: assets/images/badges/dc27/bender-sao-and-xor-dc27/82b74f213a.jpg
    source: "https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/"
    credit: "AND!XOR / Hackaday"
    caption: "The Bender SAO add-on, a 3x2 SAO board depicting the team's Bender mascot"
contact: {}
notes:
- add-on returning classic Bender mascot; no dedicated project page found
status: released
sources:
- kind: url
  url: https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
  title: Bender SAO (AND!XOR DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://hackaday.io/project/164346-andxor-dc27-badge
  title: AND!XOR DC27 Badge | Hackaday.io
  accessed: '2026-09-07'
  note: 'Confirms badge uses SAO 1.69bis interface; no separate Bender SAO product page found on this project.'
- kind: url
  url: https://github.com/ANDnXOR/sao-reference-designs
  title: 'GitHub - ANDnXOR/sao-reference-designs: AND!XOR Reference Designs for SAOs'
  accessed: '2026-09-07'
  note: 'DC27 folder in this repo contains BobRoss, DC619-EEPROM, GPIO-16-MCP23017, and Shitty-Brooch designs but no Bender-named design; no open-source files found for this specific SAO.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s Hackaday article and Hackaday.io project page confirm the Bender SAO was one of three DC27 add-ons from AND!XOR (with the Audio Reactive SAO rev 6 and Doom SAO rev 1), used the SAO v1.69bis 3x2 header, and had a hidden serial output readable by the Doom SAO. Chip, LED count/type, price, and quantity made are not stated in any source found. No dedicated project page or design-file repo entry for Bender specifically was located, despite AND!XOR publishing a general sao-reference-designs repo for other DC27 add-ons.'
last_modified_date: '2026-09-07'
---

The Bender SAO is one of three plug-in add-ons AND!XOR made for DEF CON 27 (2019), alongside an Audio Reactive SAO (rev 6) and a Doom SAO (rev 1). Where the main DC27 badge moved away from the team's long-running Bender (Futurama) mascot in favor of a new gas-mask character, this SAO brought Bender back, giving longtime badge collectors a nod to AND!XOR's very first badge. It plugs into a host badge's SAO header using the SAO v1.69bis (6-pin, I2C) standard.

Functionally, the Bender SAO carries its own microcontroller and exposes a hidden serial output over the shared I2C bus; the team's Doom SAO from the same year was built with a serial sniffer that could read Bender's hidden output, an easter-egg-style interaction between the two add-ons. The set of DC27 add-ons was part of AND!XOR's fundraising push that let them distribute the main DC27 badge for free at the conference.

No dedicated project page, storefront listing, or design-file repository entry specific to the Bender SAO could be found; AND!XOR's public sao-reference-designs GitHub repo has a DC27 folder, but it holds other add-ons (BobRoss, DC619-EEPROM, GPIO-16-MCP23017, Shitty-Brooch) rather than Bender. Chip family, LED details, price, and production quantity remain unconfirmed.
