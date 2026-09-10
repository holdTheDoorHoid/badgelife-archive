---
title: Hack-Man SAO
id: supercon-2024-hack-man-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: InstantArcade (Bob)
  url: https://hackaday.io/hacker/179291-instantarcade-bob
summary: A Pac-Man themed SAO built around the ten-cent Puya PY32F002A Cortex-M0+ microcontroller with five side-firing SK6805 RGB LEDs, whose default mode replays the Pac-Man arcade attract sequence, with button-selectable hue-cycle and Larson-scanner modes and an I2C command mode (address 0x1A) for control from a host badge; entered in the Supercon 8 SAO Contest.
functions: Default mode plays a simulation of the original Pac-Man arcade attract-mode animation. Buttons switch to a slow hue-cycle mode, a discrete Larson-scanner mode with shifting hue, and a slower Larson-scanner mode using the ghost/Pac-Man actor colors with fade. An I2C command mode (device address 0x1A, 4-byte commands) lets a host badge set LED colors, set global brightness (0-255), clear/latch colors, and read back status. On boot the five LEDs flash the firmware revision number in binary.
look:
  colors: []
  shape: null
  themes:
  - arcade
  - retro computer
  - pop culture
tech:
  mcu: PY32F002A
  leds:
    count: 5
    type: SK6805
    note: side-firing SMD LEDs; one LED represents Pac-Man and four represent the ghosts, indexed so the routing works without mirroring in software
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/198301-hack-man-sao
  url: https://hackaday.io/project/198301-hack-man-sao
  kind: hackaday
  archived: https://web.archive.org/web/20260415034852/https://hackaday.io/project/198301-hack-man-sao
- label: hackaday.io/project/198301-hack-man-sao/details
  url: https://hackaday.io/project/198301-hack-man-sao/details
  kind: hackaday
- label: hackaday.io/project/198301-hack-man-sao/logs
  url: https://hackaday.io/project/198301-hack-man-sao/logs
  kind: hackaday
images:
- file: assets/images/badges/supercon-2024/hack-man-sao/a4b2f3dfeb.jpg
  source: https://hackaday.io/project/198301-hack-man-sao
  credit: InstantArcade (Bob)
  caption: Hack-Man SAO main project photo
  archived: https://web.archive.org/web/20260415034852/https://hackaday.io/project/198301-hack-man-sao
- file: assets/images/badges/supercon-2024/hack-man-sao/919bad1807.jpg
  source: https://hackaday.io/project/198301-hack-man-sao
  credit: InstantArcade (Bob)
  caption: Hack-Man SAO board detail
  archived: https://web.archive.org/web/20260415034852/https://hackaday.io/project/198301-hack-man-sao
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/198301-hack-man-sao
  title: Hack-Man SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260415034852/https://hackaday.io/project/198301-hack-man-sao
- kind: url
  url: https://hackaday.io/project/198301-hack-man-sao
  title: Hack-Man SAO (project page)
  accessed: '2026-09-07'
  note: Confirmed maker, contest entry (Supercon 8 SAO Contest), chip, LED type/count, I2C address, modes; page has no pricing, quantity, or sale info; sourced project photos via og:image and inline log images.
  archived: https://web.archive.org/web/20260415034852/https://hackaday.io/project/198301-hack-man-sao
- kind: url
  url: https://hackaday.io/project/198301-hack-man-sao/details
  title: Hack-Man SAO details
  accessed: '2026-09-07'
  note: Details tab; content largely overlaps the main page (features, I2C command mode, brightness control).
- kind: url
  url: https://hackaday.io/project/198301-hack-man-sao/logs
  title: Hack-Man SAO logs
  accessed: '2026-09-07'
  note: 'Five build logs confirming: 5x side-firing SK6805 LEDs (Pac-Man + 4 ghosts), Puya PY32F002A chip (~$0.12/unit at qty 100), 8-pin SOP with pin 6 (NRST) repurposed as GPIO for I2C SDA, ARM HAL-based firmware, and hot glue used as the LED diffuser after testing acrylic light pipes and 3D-printed frames.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday.io project page and its five build logs confirm the chip, LED count/type, contest entry, and functional modes described in the existing summary. No pricing, unit quantity, sale/availability, or open-source hardware/firmware repo link were found anywhere on the project pages — this appears to be a contest-entry writeup rather than a product for sale, so those fields are left empty rather than guessed. No separate GitHub repo, store listing, or press coverage was located.
last_modified_date: '2026-09-07'
---

The Hack-Man SAO is a Pac-Man themed Simple Add-On built by InstantArcade (Bob) for the Supercon 8 SAO Contest in October 2024. It centers on the Puya PY32F002A, an ARM Cortex-M0+ microcontroller that costs around 12 cents in quantity, driving five side-firing SK6805 RGB LEDs arranged as Pac-Man and his four ghosts. The default behavior replays a simulation of the original arcade game's attract-mode animation, and onboard buttons cycle through alternate light shows: a slow hue cycle and two Larson-scanner ("Cylon eye") patterns, one using shifting hues and a slower one using the actual ghost colors with a fade effect.

Beyond its standalone modes, the badge exposes an I2C command interface at address 0x1A so a host conference badge can drive it directly — setting individual LED colors, adjusting global brightness, and clearing or latching color state over 4-byte commands. On power-up the five LEDs flash the firmware's revision number in binary as a quick sanity check.

The maker's five build logs go into unusually specific detail on the engineering tradeoffs: reworking the 8-pin microcontroller's NRST pin into a GPIO to free up an I2C data line while keeping SWD debug access, choosing ARM's HAL over low-level register writes for readability, and solving LED light diffusion (acrylic light pipes and 3D-printed reflective frames were tried and discarded in favor of plain hot glue). The project pages do not mention a price, production quantity, or whether it was ever offered for sale beyond the contest entry, nor do they link to a published hardware or firmware repository.
