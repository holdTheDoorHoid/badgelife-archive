---
title: A DC27 CircuitPython Shitty Add-On V1.69BIS Totem
id: dc27-dc27-circuitpython-shitty-add-on-v169bis-totem
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Corey Benn
  url: https://hackaday.io/hacker/220082-corey-benn
summary: A DEF CON 27 "WeBadge" built around an ATSAMD21G18A running CircuitPython 4.0 that acts as a Shitty Add-On totem, hosting up to four SAO v1.69bis add-ons with I2C and GPIO on each connector, per-connector power control and PWM from Python, twelve bottom-entry LEDs, solder jumpers for always-on power and I2C pull-ups, and AA battery power through a Pololu 3.3V step-up regulator.
functions: Hosts and powers up to four SAO add-ons at once; each of the four connectors gets its own I2C bus access, GPIO, and independently switchable power (including PWM dimming/pulsing of add-on power via CircuitPython's PulseIO) so a wearer can display a stack of SAO bling from one badge without needing a host badge.
look:
  colors: []
  shape: null
  themes:
  - sao
  - hardware tool
  - learn to solder
tech:
  mcu: ATSAMD21G18A
  leds:
    count: 12
    type: reverse-mount
    note: Twelve SunLED bottom-entry SMD LEDs (XZM2CYK45WT), yellow.
  display: none
  connectivity:
  - i2c
  - usb
  battery: 1-2 AA cells through a Pololu 3.3V step-up regulator
  sao_version: v1.69bis
  sao_ports: 4
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
get_one:
  price: ''
  price_usd: null
  quantity: approximately 100
  availability: free
  distribution:
  - free_drop
  where: Handed out at DEF CON 27 (2019); no commercial sale found.
links:
- label: hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
  url: https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
  kind: hackaday
  archived: https://web.archive.org/web/20260213195949/https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
images:
- file: assets/images/badges/dc27/dc27-circuitpython-shitty-add-on-v169bis-totem/07c672d2c7.jpg
  source: https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
  credit: Corey Benn
  caption: The DC27 CircuitPython Shitty Add-On V1.69BIS Totem board
  archived: https://web.archive.org/web/20260213195949/https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
- file: assets/images/badges/dc27/dc27-circuitpython-shitty-add-on-v169bis-totem/c1a346bf1b.jpg
  source: https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
  credit: Corey Benn
  caption: Assembled totem board with LEDs and SAO connectors
  archived: https://web.archive.org/web/20260213195949/https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
  title: A DC27 CircuitPython Shitty Add-On V1.69BIS Totem
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260213195949/https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
- kind: url
  url: https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
  title: A DC27 CircuitPython Shitty Add-On V1.69BIS Totem (project page and logs)
  accessed: '2026-09-07'
  note: Confirmed maker, event/year, MCU, LED count/part, SAO connector count, power design, and quantity (~100 built for DC27); source of both saved photos.
  archived: https://web.archive.org/web/20260213195949/https://hackaday.io/project/166397-a-dc27-circuitpython-shitty-add-on-v169bis-totem
- kind: url
  url: https://oshpark.com/shared_projects/uYwa5w3S
  title: DEFCON 26 Shitty Add-On Totem (OSH Park shared project)
  accessed: '2026-09-07'
  note: Found while searching for design-file shares; this is a different, unrelated DEFCON 26 board by a different maker (Benchoff), not a fab share for this DC27 project. Checked and ruled out.
  archived: https://web.archive.org/web/20260421200800/https://oshpark.com/shared_projects/uYwa5w3S
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, event/year, MCU, LED part/count, four SAO v1.69bis connectors with per-connector I2C/GPIO/power, AA + Pololu step-up power, CircuitPython 4.0) come from the maker's own Hackaday.io project page and logs. The project page mentions KiCad footprints for the LEDs but no complete published hardware/firmware repo was found, so make_your_own is marked partial rather than yes; hardware_url/firmware_url left empty. Price is not stated anywhere found; it was a free DEF CON handout so get_one.price is left blank rather than guessed. No separate storefront, video, or press coverage was located in the search budget.
last_modified_date: '2026-09-07'
---

Corey Benn built this board as a personal "WeBadge" for DEF CON 27 (2019): rather than being a single SAO itself, it's a totem that carries up to four other Shitty Add-Ons at once, giving each of its four v1.69bis-standard connectors its own I2C bus access, GPIO, and independently switchable power. The board runs CircuitPython 4.0 on an ATSAMD21G18A, so a wearer (or anyone with a USB cable) can edit the Python code directly to turn add-on power on and off, or even PWM it for pulsing/dimming effects, without touching a compiler. Twelve bottom-entry SunLED SMD LEDs, solder jumpers for always-on add-on power and I2C pull-up resistors, and a photoresistor round out the hardware. Power comes from AA batteries boosted to 3.3V through a Pololu step-up regulator, with a micro-USB connector for CircuitPython development.

Around 100 units were assembled and handed out at DEF CON 27; the project does not appear to have been sold commercially. Benn's Hackaday.io project logs document build issues along the way, including KiCad footprint mistakes for the LEDs and an I2C "invalid pins" problem traced to the SAMD21's VDDCore pin needing to be bent up during assembly — useful detail for anyone trying to reproduce the board, though no single combined hardware/firmware repository was found; the footprint fix and code discussion live in the Hackaday.io logs rather than a separate repo.
