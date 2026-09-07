---
title: DC619 EEPROM SAO
id: dc27-dc27-dc619-eeprom-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: AND!XOR
  url: https://github.com/ANDnXOR
summary: A simple I2C EEPROM SAO (AT24-family chip at address 0x50) that AND!XOR published for DEF CON 27 as the reference for their proposed EEPROM data format of DC year, maker ID, SAO type ID, then arbitrary data.
functions: 'Lets a badge with I2C detect the SAO on the bus and read a small standardized header (DC year, maker ID, SAO type ID) followed by arbitrary data, so other makers'' SAOs can be recognized and reacted to automatically.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not sold; published as an open reference design on GitHub for other badgelife makers to fabricate or adapt.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/zapp1337/sao-reference-designs/tree/master/DC27/DC619-EEPROM_sao1.69bis
  firmware_url: null
  eda_tool: null
links:
- label: github.com/ANDnXOR/sao-reference-designs/tree/master
  url: https://github.com/ANDnXOR/sao-reference-designs/tree/master
  kind: repo
- label: github.com/zapp1337/sao-reference-designs/tree/master/DC27/DC619-EEPROM_sao1.69bis
  url: https://github.com/zapp1337/sao-reference-designs/tree/master/DC27/DC619-EEPROM_sao1.69bis
  kind: repo
- label: AND!XOR DC27 Badge (Hackaday.io project)
  url: https://hackaday.io/project/164346-andxor-dc27-badge
  kind: hackaday
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/ANDnXOR/sao-reference-designs/tree/master
  title: AND!XOR SAO Reference Designs
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/zapp1337/sao-reference-designs/tree/master/DC27/DC619-EEPROM_sao1.69bis
  title: 'zapp1337/sao-reference-designs: DC27/DC619-EEPROM_sao1.69bis'
  accessed: '2026-09-07'
  note: 'README confirms chip (AT24C02N in this fork''s copy), I2C address 0x50 with address pins pulled low, and that the AND!XOR badge can only address the first 256 bytes; folder contains only a schematic image (dc619-eeprom-schematic.png), no assembled-board photo.'
- kind: url
  url: https://hackaday.io/project/164346-andxor-dc27-badge
  title: AND!XOR DC27 Badge | Hackaday.io
  accessed: '2026-09-07'
  note: 'Confirms the DC27 badge''s SAO v1.69bis standard, the EEPROM reference design based on AT24C32 at 7-bit address 0x50, and the DC Year/Maker ID/SAO Type ID/Data header format (DC27 = 0x1B, AND!XOR maker ID = 0x49).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a reference design, not a standalone product that was sold or distributed as its own SAO -- AND!XOR published it on GitHub so other badgelife makers could build EEPROM-based SAOs that DC27-badge-compatible hardware would recognize (the DOOM SAO built for DC27 uses this reference design). Two copies of the folder disagree on the exact EEPROM part: the top-level AND!XOR repo description and the Hackaday.io project page say AT24C32, while the zapp1337 fork''s own README for this specific DC619 folder says AT24C02N (noting the AND!XOR badge can only address the first 256 bytes regardless of which AT24-family chip is used). No price, quantity, or distribution channel exists because it was never sold -- it is schematics/Gerbers only. No photo of an assembled unit was found, only a schematic diagram, so no image was saved per the guide''s rule against non-photo images. Left get_one and most look/tech fields empty or minimal since sources do not describe a physical retail item.'
last_modified_date: '2026-09-07'
---

AND!XOR designed the DC619 EEPROM SAO as a reference design for DEF CON 27 (2019), published openly on GitHub rather than sold as a product. It is a minimal I2C add-on built around an AT24-family serial EEPROM (sources differ on the exact part -- AT24C32 per the main repo and the AND!XOR Hackaday.io project page, AT24C02N per the specific DC619 folder's own README) wired to the standard 7-bit address 0x50 with all address pins grounded. The point of the design was not the SAO itself but the data format it demonstrated: a small header of DC year, AND!XOR's registered maker ID (0x49), a SAO type ID, and then arbitrary payload data, which AND!XOR hoped other badgelife makers would adopt so any SAO could be automatically recognized and reacted to by a badge with I2C support.

The design plugs into the SAO v1.69bis (6-pin) header used by the DC27 AND!XOR badge. Because it is a reference design rather than a finished product, no price, production quantity, or purchase channel exists for it; makers were meant to copy or adapt the schematic to build their own compatible EEPROM SAOs. The DOOM SAO built for DC27 is one known example that built on this EEPROM reference design for its I2C detection.

## Make your own

The hardware is openly published: a schematic (`dc619-eeprom-schematic.png`) and a short README live in the `DC27/DC619-EEPROM_sao1.69bis` folder of the `sao-reference-designs` repository (mirrored between the ANDnXOR and zapp1337 GitHub accounts). No firmware, Gerbers, BOM, or EDA source files were found alongside it -- just the schematic image and a plain-text note on the EEPROM part and I2C address to use.
