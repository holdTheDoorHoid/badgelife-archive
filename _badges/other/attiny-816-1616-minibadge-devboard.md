---
title: ATtiny 816/1616 Minibadge Devboard
id: other-attiny-816-1616-minibadge-devboard
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: other
year: 2024
makers:
- name: Beehive Engineering
  url: https://github.com/Pips801
summary: A SAINTCON-format minibadge that breaks out an ATtiny816 or ATtiny1616 microcontroller for hardware hacking, with UPDI programming and two onboard LEDs.
functions: 'Ships pre-loaded with firmware that blinks "PIPS WAS HERE" in Morse code on its two LEDs; breakout pins for I2C, USART, SPI, DAC, ADC and PTC (touch-sense) let a buyer program their own logic via UPDI.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
  - minibadge
tech:
  mcu: ATtiny816 / ATtiny1616
  leds:
    count: 2
    type: null
    note: null
  display: none
  connectivity:
  - i2c
  - uart
  battery: null
  sao_version: null
get_one:
  price: $5.00
  price_usd: 5.0
  quantity: ''
  availability: limited
  availability_note: 'Tindie listing checked 2026-09-07: 20 units of the ATtiny816 variant and 3 units of the ATtiny1616 variant in stock.'
  distribution:
  - purchase
  where: Sold on Tindie by Beehive Engineering (seller "pips").
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/Pips801/minibadges/tree/main/ATTiny%20Development%20Minibadge
  firmware_url: https://github.com/Pips801/minibadges/tree/main/ATTiny%20Development%20Minibadge
  eda_tool: KiCad
links:
- label: www.tindie.com/products/pips/attiny-8161616-minibadge-devboard
  url: https://www.tindie.com/products/pips/attiny-8161616-minibadge-devboard/
  kind: store
- label: Pips801/minibadges - ATTiny Development Minibadge (source)
  url: https://github.com/Pips801/minibadges/tree/main/ATTiny%20Development%20Minibadge
  kind: repo
- label: ATTiny Development Minibadge README
  url: https://github.com/Pips801/minibadges/blob/main/ATTiny%20Development%20Minibadge/README.md
  kind: doc
images:
- file: assets/images/badges/other/attiny-816-1616-minibadge-devboard/79d39a7f45.jpg
  source: "https://www.tindie.com/products/pips/attiny-8161616-minibadge-devboard/"
  credit: "Beehive Engineering"
  caption: "The assembled ATtiny 816/1616 Minibadge Devboard"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/pips/attiny-8161616-minibadge-devboard/
  title: ATtiny 816/1616 Minibadge Devboard
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other''.'
- kind: url
  url: https://www.tindie.com/products/pips/attiny-8161616-minibadge-devboard/
  title: ATtiny 816/1616 Minibadge Devboard - Tindie listing
  accessed: '2026-09-07'
  note: 'Confirmed maker (Beehive Engineering, Tindie seller "pips"), price $5, stock counts (20/3), description text, and links to the GitHub source/documentation.'
- kind: url
  url: https://github.com/Pips801/minibadges/blob/main/ATTiny%20Development%20Minibadge/README.md
  title: ATTiny Development Minibadge README
  accessed: '2026-09-07'
  note: 'Confirmed two-LED layout, UPDI programming pin, default Morse-code firmware, and Arduino/MegaTinyCore setup details.'
- kind: url
  url: https://github.com/Pips801/minibadges/tree/main/ATTiny%20Development%20Minibadge
  title: Pips801/minibadges - ATTiny Development Minibadge directory listing
  accessed: '2026-09-07'
  note: 'Confirmed KiCad schematic/PCB/project files and two Arduino .ino firmware sketches are published; no gerbers, BOM or license file present.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Listed for sale on Tindie under the SAINTCON minibadge form factor, but the listing and its linked GitHub repo do not name a specific SAINTCON year; the listing''s photo timestamps are from December 2024, so year is recorded as 2024 with low certainty. No matching per-year SAINTCON entry could be confirmed, so event is left as "other" (see research guide: add a new event only in the report). Could not confirm PCB solder-mask color, LED color/type, or exact quantity produced from available sources.'
last_modified_date: '2026-09-07'
---

The ATtiny 816/1616 Minibadge Devboard is a hobbyist development board built by Beehive Engineering (Tindie seller "pips", GitHub user Pips801) in the SAINTCON minibadge form factor. Rather than being tied to a specific event badge, it is meant as a general-purpose way to prototype with Microchip's ATtiny816 or ATtiny1616 microcontrollers inside the minibadge standard: the board breaks out I2C, USART, SPI, DAC, ADC and PTC (capacitive touch) pins, and carries two onboard LEDs. It ships pre-loaded with firmware that blinks "PIPS WAS HERE" in Morse code, and is intended to be reprogrammed by the buyer using any UPDI programmer (the maker recommends Adafruit's UPDI Friend) together with the Arduino IDE and the MegaTinyCore board library.

The maker describes it on Tindie as a first attempt at incorporating a programmable, flashable chip into their badge work, aimed at making ATtiny-based minibadge development approachable and inexpensive. It sells for $5.00, with the ATtiny816 and ATtiny1616 versions listed as separate variants (20 and 3 units in stock respectively as of this check).

## Make your own

Full KiCad design files (schematic, PCB layout and project file), a PDF of the circuit, and two example Arduino sketches (`I2C_Client_blink.ino` and `morse_code.ino`) are published in the maker's `minibadges` GitHub repository. The README documents the UPDI programming pin and recommended Arduino IDE settings (SerialUPDI programmer, 57600 baud, ATtiny816 selection, 10 MHz internal clock), but the repository does not include gerber files, a bill of materials, or an explicit license.
