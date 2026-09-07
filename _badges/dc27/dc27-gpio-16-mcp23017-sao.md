---
title: GPIO 16 (MCP23017) reference design
id: dc27-dc27-gpio-16-mcp23017-sao
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
summary: A 16-LED SAO reference design driven by an MCP23017 I2C GPIO expander at address 0x20, published by AND!XOR for DEF CON 27; their badge plays special patterns when it detects the chip on the bus, a behaviour carried over from DEF CON 26.
functions: 'Drives 16 onboard LEDs as GPIO outputs via I2C using the MCP23017 expander; a compatible host badge (e.g. the AND!XOR DC26/DC27 badge) detects the MCP23017 on the bus and plays special LED patterns in response.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 16
    type: discrete
    note: 16x LEDs each with a 1kOhm current-limiting resistor, driven as GPIO outputs from the MCP23017.
  display: none
  connectivity:
  - i2c
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ANDnXOR/sao-reference-designs/tree/master/DC27/GPIO-16-MCP23017_sao1.69bis
  firmware_url: https://github.com/ANDnXOR/ANDnXOR_DC26_Badge/blob/master/Firmware/components/drivers/addons.c
  eda_tool: null
  notes: 'Reference design published as a README + schematic image (mcp23017.png), not a full KiCad/Eagle project; BOM listed in the README. Example firmware driver for detecting/driving the MCP23017 lives in the ANDnXOR DC26 badge firmware repo, not a dedicated firmware repo for this SAO.'
links:
- label: github.com/ANDnXOR/sao-reference-designs/tree/master
  url: https://github.com/ANDnXOR/sao-reference-designs/tree/master
  kind: repo
- label: github.com/zapp1337/sao-reference-designs/tree/master/DC27/GPIO-16-MCP23017_sao1.69bis
  url: https://github.com/zapp1337/sao-reference-designs/tree/master/DC27/GPIO-16-MCP23017_sao1.69bis
  kind: repo
- label: github.com/ANDnXOR/ANDnXOR_DC26_Badge/blob/master/Firmware/components/drivers/addons.c
  url: https://github.com/ANDnXOR/ANDnXOR_DC26_Badge/blob/master/Firmware/components/drivers/addons.c
  kind: repo
- label: github.com/ANDnXOR/sao-reference-designs/tree/master/DC27/GPIO-16-MCP23017_sao1.69bis
  url: https://github.com/ANDnXOR/sao-reference-designs/tree/master/DC27/GPIO-16-MCP23017_sao1.69bis
  kind: repo
images:
  - file: assets/images/badges/dc27/dc27-gpio-16-mcp23017-sao/2facd88345.png
    source: "https://github.com/ANDnXOR/sao-reference-designs/tree/master/DC27/GPIO-16-MCP23017_sao1.69bis"
    credit: "AND!XOR"
    caption: "Schematic/reference diagram for the GPIO-16 MCP23017 SAO"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/ANDnXOR/sao-reference-designs/tree/master
  title: AND!XOR SAO Reference Designs
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/ANDnXOR/sao-reference-designs/tree/master/DC27/GPIO-16-MCP23017_sao1.69bis
  title: "GPIO-16-MCP23017_sao1.69bis directory (README + mcp23017.png)"
  accessed: '2026-09-07'
  note: "README text and BOM: MCP23017-E/SS, 16 LEDs, 16x 1kOhm resistors, 0.1uF cap, 2x3 keyed SAO header; confirms v1.69bis (6-pin) SAO connector."
- kind: url
  url: https://github.com/zapp1337/sao-reference-designs/tree/master/DC27/GPIO-16-MCP23017_sao1.69bis
  title: "zapp1337 mirror/fork of the same DC27 reference design directory"
  accessed: '2026-09-07'
  note: "Same README/BOM content as the ANDnXOR upstream copy of this directory; appears to be a fork/mirror, not a separate maker's design."
- kind: url
  url: https://github.com/ANDnXOR/ANDnXOR_DC26_Badge/blob/master/Firmware/components/drivers/addons.c
  title: "ANDnXOR DC26 Badge firmware, addons.c"
  accessed: '2026-09-07'
  note: "Attempted fetch returned HTTP 404 (file path may have moved); could not directly confirm the I2C address or pattern-trigger code in this file. The 0x20 address and 'plays special patterns' behaviour are stated in the entry's existing summary/notes and corroborated by web search results describing the same repo, but were not independently re-verified against current file contents."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a reference design published by AND!XOR (not a specific one-off badge sold under its own name) intended for use with their DC26/DC27 badges, which recognize the MCP23017 on the I2C bus and react with special LED patterns. No pricing, quantity, or sale/distribution information was found — the design appears to have been shared as an open reference/example rather than sold as a standalone product, consistent with get_one fields being left empty. The addons.c firmware file link in the original entry returned a 404 on refetch; could not verify current file contents, though the general behaviour is corroborated by other sources describing the same project. No photo of an assembled/built unit was found; the only image available is the maker''s schematic/reference diagram, which was saved.'
last_modified_date: '2026-09-07'
---

The GPIO 16 (MCP23017) SAO is a reference design published by AND!XOR under their `sao-reference-designs` GitHub repository, intended for DEF CON 27. Rather than being a one-off badge or SAO sold under its own name, it functions as an example/reference for other badge makers: a single MCP23017 I2C GPIO expander (address 0x20) drives 16 onboard LEDs as simple outputs, each through a 1kOhm resistor, with a 0.1uF decoupling capacitor and a keyed 2x3 SAO header (the v1.69bis/6-pin connector).

The design is paired with firmware in AND!XOR's own DC26/DC27 badges: when the badge detects an MCP23017 on the I2C bus, it recognizes the add-on and plays special LED patterns, a behavior the maker notes was carried over from DEF CON 26. The repository provides only a README and a schematic/reference image rather than full CAD source files, so it is best understood as documentation of a known-good circuit for anyone building a compatible SAO, rather than a ready-to-fab project.

No information was found on pricing, quantities made, or whether physical units were ever sold or distributed; it appears to have been shared purely as an open reference design.
