---
title: 'PyCard: Jean Luc (Python/Arduino in a Card Shape)'
id: other-pycard-jean-luc-python-arduino-in-a-card-shape
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2017
makers:
- name: Peter Misenko (bobricius)
  url: https://hackaday.io/bobricius
summary: A wallet-sized, card-shaped development board with a SAMD21 microcontroller, programmable in CircuitPython or Arduino, built around a large charlieplexed LED matrix.
functions: Runs user Python/CircuitPython scripts (edited over USB mass storage) or Arduino sketches; drives a 22x5 charlieplexed LED matrix; logs sensor data (temperature, humidity, pressure) to its SD card; keeps time via an onboard RTC.
look:
  colors: []
  shape: card
  themes:
  - retro computer
  - hardware tool
  - learn to solder
tech:
  mcu: SAMD21
  leds:
    count: 110
    type: charlieplexed
    note: 22x5 charlieplexed LED matrix display
  display: LED matrix 22x5
  connectivity:
  - usb
  - i2c
  battery: CR2032
  sao_version: none
get_one:
  price: ~$20 per unit (in batches of 20)
  price_usd: 20
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold via the maker's Tindie store (bobricius); also documented as a DIY build on Hackaday.io.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/19597-pycard-jean-luc-pythonarduino-in-card-shape
  firmware_url: https://hackaday.io/project/19597-pycard-jean-luc-pythonarduino-in-card-shape
  eda_tool: null
links:
- label: hackaday.io/project/19597-pycard-jean-luc-pythonarduino-in-card-shape
  url: https://hackaday.io/project/19597-pycard-jean-luc-pythonarduino-in-card-shape
  kind: hackaday
  archived: https://web.archive.org/web/20251115221642/https://hackaday.io/project/19597-pycard-jean-luc-pythonarduino-in-card-shape
- label: PYcARD (Jean-Luc) - Python + Arduino in card from Bobricius on Tindie
  url: https://www.tindie.com/products/bobricius/pycard-jean-luc-python-arduino-in-card/
  kind: store
- label: Jean-Luc PYcARD Is A Pocketable Python Development Platform (Hackaday)
  url: https://hackaday.com/2017/02/23/jean-luc-pycard-is-a-pocketable-python-development-platform/
  kind: article
  archived: https://web.archive.org/web/20260514140425/https://hackaday.com/2017/02/23/jean-luc-pycard-is-a-pocketable-python-development-platform/
images:
- file: assets/images/badges/other/pycard-jean-luc-python-arduino-in-a-card-shape/a10430b8e7.jpg
  source: https://hackaday.io/project/19597-pycard-jean-luc-pythonarduino-in-card-shape
  credit: Peter Misenko (bobricius)
  caption: PYcARD Jean-Luc board with 22x5 charlieplexed LED matrix
  archived: https://web.archive.org/web/20251115221642/https://hackaday.io/project/19597-pycard-jean-luc-pythonarduino-in-card-shape
- file: assets/images/badges/other/pycard-jean-luc-python-arduino-in-a-card-shape/44e5088de5.jpg
  source: https://hackaday.io/project/19597-pycard-jean-luc-pythonarduino-in-card-shape
  credit: Peter Misenko (bobricius)
  caption: PYcARD board, front view showing LED matrix and buttons
  archived: https://web.archive.org/web/20251115221642/https://hackaday.io/project/19597-pycard-jean-luc-pythonarduino-in-card-shape
contact: {}
notes:
- Sheet/original title used 'PyCard'; the maker's own spelling is 'PYcARD (Jean-Luc)'.
status: released
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is a general-purpose hobby/dev-board project (submitted to the 2017 Hackaday Prize and Sci-Fi Contest), not a badge or SAO made for a specific hacker convention, so no event correction was made and it stays filed under 'other'. The name 'Jean-Luc' is a Star Trek Jean-Luc Picard pun on 'card.' Quantity made and current availability are not stated anywhere found; the Tindie storefront could not be checked directly (Cloudflare blocked automated access), so availability is left unknown. No dedicated GitHub repo for this specific project was located (only files hosted directly on the Hackaday.io project page - schematic, board file, firmware, BOM); open_source is marked 'partial' since design files are published but no explicit license is stated.
last_modified_date: '2026-09-07'
---

PYcARD (Jean-Luc) is a wallet/card-sized development board designed by Peter Misenko, who goes by bobricius, and posted to Hackaday.io in January 2017 as an entry in that year's Hackaday Prize and Sci-Fi Contest. It is built around a SAMD21 microcontroller and can be programmed either as an Arduino board or in CircuitPython/MicroPython, with scripts editable directly through the USB mass-storage interface the board presents when plugged in. The name is a nod to Star Trek's Jean-Luc Picard, playing on "card."

The board's most visible feature is a large 22x5 charlieplexed LED matrix built from bobricius's own charlieplexed-display project, alongside a DS3231 real-time clock, an SHT21 temperature/humidity sensor, and a BME280 environmental (temperature/humidity/pressure) sensor, an SD card slot, an RGB indicator LED, three user buttons plus a reset button, and CR2032 battery backup. The PCB is finished in ENIG gold and was reported as costing around $20 per unit when ordered in batches of 20 as of early 2017; it was later sold through the maker's Tindie store. It is a general-purpose hobbyist development platform rather than a badge or SAO produced for a specific hacker conference, so it has no associated event or year of convention use beyond its 2017 creation date.

## Make your own

The Hackaday.io project page hosts the board's design and firmware files directly: a schematic (PYcARD.sch), PCB layout (PYcARD-RTM.brd), a bill of materials (bom.txt), a sample CircuitPython script (main.py), and a CircuitPython firmware build. No separate GitHub repository or explicit open-source license was found for this specific project.
