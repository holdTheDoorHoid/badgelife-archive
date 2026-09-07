---
title: Mr Stash
id: dc26-mr-stash
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Peter Shabino
  url: https://github.com/Wireb
summary: A trading badge Peter Shabino (Wireb) built for DEF CON 26, meant to be swapped for other badges and SAOs rather than sold.
functions: LED patterns, a vibration motor, a touch sensor, and an IR sensor intended for badge-to-badge IR trading/communication.
look:
  colors: []
  shape: null
  themes:
  - mascot
tech:
  mcu: PIC
  leds: null
  display: none
  connectivity:
  - ir
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - swap
  where: 'Not sold; the maker made it to trade in person at DEF CON 26 (2018).'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Wireb/Mr_Stash
  firmware_url: https://github.com/Wireb/Mr_Stash
  eda_tool: KiCad
links:
- label: github.com/Wireb/Mr_Stash
  url: https://github.com/Wireb/Mr_Stash
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/Wireb/Mr_Stash
  title: Mr Stash
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/Wireb/Mr_Stash
  title: 'Mr Stash - README'
  accessed: '2026-09-07'
  note: 'Maker (Peter Shabino), event (DC26, 2018), purpose (trading badge), tech (PIC MCU, KiCad hardware, MPLAB X assembly firmware), and the missing-firmware caveat all confirmed from the README and MIT LICENSE copyright line.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No LED count/type, display, battery, price, or quantity-made details are given anywhere in the repo; this was a personal trading badge, not a sold product, so those fields are left empty. No photos of the assembled badge were found in the repo (no image files present) or linked elsewhere, so the images list stays empty. The firmware in the repo is explicitly incomplete per the maker (final version was lost before the badge shipped to DEF CON 26), which is why open_source is "partial" rather than "yes".'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/mr-stash/
---

Mr Stash is a badge Peter Shabino (GitHub handle Wireb) built for DEF CON 26 in 2018, not to sell but to trade in person for other attendees' badges and SAOs. The design combines an Inkscape-drawn "mustache" art layer (outline, motor and IR-sensor cutouts, eyebrows) imported into KiCad as footprints, with a PIC microcontroller programmed in assembly via MPLAB X and a PicKit debugger. Functions included LED lighting patterns, a vibration motor, a touch sensor, and an IR sensor meant to let badges communicate with each other.

The maker notes that shortly before leaving for DEF CON 26 his laptop's hard drive failed and he lost the final firmware build, so the version published to GitHub is an earlier one missing several features he had built: a mode that cycles through all LED patterns, a hidden Morse-code easter egg, most of the vibration patterns, and a working touch sensor (the version in the repo worked at home in Minnesota but not in Nevada's dry climate). Several parts (a handful of capacitors, diodes, a badge-bus connector, and an SAO connector) were also left unpopulated in the final board.

## Make your own

The GitHub repo (github.com/Wireb/Mr_Stash, MIT-licensed) contains the KiCad 5.0 hardware project, the Inkscape source for the badge artwork, the MPLAB X 5.0 firmware project with the PIC assembly source (`Mr_Stash.asm`), and an XLS/PDF documentation dump describing the menu items and IR command protocol — enough to reproduce the hardware and the incomplete firmware as they existed just before DEF CON 26.
