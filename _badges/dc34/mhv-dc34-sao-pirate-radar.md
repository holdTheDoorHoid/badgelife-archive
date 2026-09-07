---
title: 'MHV DC34 SAO: Pirate Radar!'
id: dc34-mhv-dc34-sao-pirate-radar
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Maritime Hacking Village
  url: https://maritimehackingvillage.com
summary: A 198-LED radar scope SAO with eleven spiral arms and eighteen range rings, driven by an ATtiny412 over a two-wire I2C connection to any SAO header.
functions: Ninety-two built-in LED animations (sonar returns, storm fronts, moon phases, a ship's wheel, Pac-Man, and more), selected at compile time; talks I2C so owners can write their own animations.
look:
  colors: []
  shape: circle
  themes:
  - pirate
  - radar
  - security
  - hardware tool
tech:
  mcu: ATtiny412
  leds:
    count: 198
    type: LP5860RKPR
    note: Driven via the LP5860RKPR LED matrix driver over bit-banged I2C (PA1/PA2); 11 spiral arms across 18 range rings.
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: $50
  price_usd: 50
  quantity: '100'
  availability: available
  availability_note: Listed in stock (qty 100, not sold out) as of 2026-09-07 on the MHV shop.
  distribution:
  - purchase
  where: Sold directly through the Maritime Hacking Village online shop.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Maritime-Hacking-Village/SAO-2026-Radar
  firmware_url: https://github.com/Maritime-Hacking-Village/SAO-2026-Radar/tree/main/firmware
  eda_tool: KiCad
  license: CERN-OHL-W-2.0
  notes: Repo includes KiCad hardware, AVR (ATtiny412) firmware, acrylic-diffuser generation scripts, and build/flash/EEPROM scripts over UPDI.
links:
- label: maritimehackingvillage.com/shop/p/pirate-radar
  url: https://maritimehackingvillage.com/shop/p/pirate-radar
  kind: store
  note: Original sheet URL now returns 404; the live product page is at a different slug (see next link).
- label: maritimehackingvillage.com/shop/p/mhv-dc34-sao
  url: https://maritimehackingvillage.com/shop/p/mhv-dc34-sao
  kind: store
- label: github.com/Maritime-Hacking-Village/SAO-2026-Radar
  url: https://github.com/Maritime-Hacking-Village/SAO-2026-Radar
  kind: repo
images:
- file: assets/images/badges/dc34/mhv-dc34-sao-pirate-radar/3cca982373.png
  source: https://maritimehackingvillage.com/shop/p/mhv-dc34-sao
  credit: Maritime Hacking Village
  caption: Product photo of the Pirate Radar SAO
- file: assets/images/badges/dc34/mhv-dc34-sao-pirate-radar/1c1e90fea9.gif
  source: https://maritimehackingvillage.com/shop/p/mhv-dc34-sao
  credit: Maritime Hacking Village
  caption: Animated GIF of the radar LED animation in action
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- The sheet-sourced URL (/shop/p/pirate-radar) 404s; the product is actually listed at /shop/p/mhv-dc34-sao. Both are recorded in links.
status: released
sources:
- kind: url
  url: https://maritimehackingvillage.com/shop/p/pirate-radar
  title: 'MHV DC34 SAO: Pirate Radar!'
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc34''.'
- kind: url
  url: https://maritimehackingvillage.com/shop/p/mhv-dc34-sao
  title: 'MHV DC34 SAO: Pirate Radar! (live product page, embedded shop-collection JSON)'
  accessed: '2026-09-07'
  note: Confirmed price ($50), stock (100, not sold out), description, images, and GitHub link. Fetched via curl since the original sheet URL 404s; product data recovered from the /shop collection JSON.
- kind: url
  url: https://github.com/Maritime-Hacking-Village/SAO-2026-Radar
  title: Maritime-Hacking-Village/SAO-2026-Radar
  accessed: '2026-09-07'
  note: Confirmed open-source hardware (KiCad) and firmware (AVR/ATtiny412), CERN-OHL-W-2.0 license, LP5860RKPR LED driver, bit-banged I2C.
- kind: url
  url: https://raw.githubusercontent.com/Maritime-Hacking-Village/SAO-2026-Radar/main/firmware/README.md
  title: firmware/README.md
  accessed: '2026-09-07'
  note: Confirmed MCU is ATtiny412 and firmware architecture (LP5860 driver, bit-banged I2C on PA1/PA2, compile-time animation selection).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts (chip, LEDs, price, open-source status) confirmed from the maker''s own shop listing and GitHub repo. Not confirmed: exact SAO connector version (v1 vs v2/1.69bis), battery/power draw, and total production run beyond the 100 units shown in stock at check time (could be a restockable number rather than a hard limit).'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/mhv-dc34-sao-pirate-radar.glb
  method: kicad
  source_file: KiCAD/radar/radar.kicad_pcb
  generated: '2026-09-07'
  bytes: 536920
---

The Pirate Radar is a 2026 SAO from Maritime Hacking Village (MHV), the maritime-security community that has run a village at DEF CON since at least DC33. It clips onto any badge's SAO header and turns it into a miniature radar scope: 198 LEDs arranged in eleven spiral arms across eighteen range rings, driven by an ATtiny412 talking to an LP5860RKPR LED-matrix driver over a bit-banged I2C connection using only two wires. The board ships with ninety-two built-in animations — sonar sweeps, storm fronts, moon phases, a ship's wheel, and even a Pac-Man pattern — selected at compile time, and because it exposes I2C, owners can write and flash their own.

MHV sold the SAO directly through its Squarespace shop for $50, with 100 units shown in stock and not marked sold out as of this check. The hardware (KiCad), AVR firmware, and even the Python scripts used to generate the acrylic diffuser/case are published on GitHub under the CERN Open Hardware Licence v2 (Weakly Reciprocal), along with shell scripts for building, flashing, and reading the ATtiny412 over UPDI.

Note for anyone following the sheet's original link: the URL captured during the sweep (`/shop/p/pirate-radar`) now 404s. The live listing is at `/shop/p/mhv-dc34-sao`; both are recorded in this entry's links.
