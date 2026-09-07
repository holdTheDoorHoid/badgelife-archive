---
title: ImpBadge (Hack for Satan, DC26)
id: dc26-hack-for-satan-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Hack for Satan
  url: https://x.com/hackforsatan
- name: Ryan Sheffield
  url: https://x.com/RYANxSHEFFIELD
  role: PCB illustration and "Asylum" game script
summary: A black PCB badge for DEF CON 26 illustrated with a ram/goat-skull occult
  design, built around a PIC18F4520 microcontroller with a capacitive touch sensor
  and small onboard screen. Its centerpiece is a hidden text-adventure horror game,
  "Asylum," unlocked by working through on-badge and in-person puzzle clues.
functions: Runs a hidden text-adventure/RPG horror game ("Asylum") with save state
  in EEPROM; a "seance" puzzle mode; capacitive touch input; a pentagram-shaped LED
  effect; screen-based menus.
look:
  colors:
  - black
  - white
  - red
  shape: ram skull
  themes:
  - horror
  - occult
  - ctf
  - puzzle
tech:
  mcu: PIC18F4520
  leds:
    count: null
    type: discrete
    note: Red LEDs arranged in a five-point star/pentagram pattern near the top
      of the board, driven by dedicated firmware (imp_pentagram.c).
  display: Present (imp_screen.c / imp_display.c firmware modules); size and part
    not stated by the maker.
  connectivity:
  - uart
  inputs:
  - touch
  - capacitive
  battery: null
  sao_version: null
get_one:
  price: $100
  price_usd: 100
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold in person at DEF CON 26 via pop-up cash drops around the venue by
    the Hack for Satan crew (based on the same practice documented for their following
    year's badge).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/hackforsatan/impbadge/
  eda_tool: null
links:
- label: twitter.com/hackforsatan
  url: https://twitter.com/hackforsatan
  kind: social
- label: hackforsatan/impbadge (firmware source)
  url: https://github.com/hackforsatan/impbadge/
  kind: repo
- label: Asylum (web-playable version of the badge's hidden game)
  url: https://hackforsatan.github.io/asylum/asylum.html
  kind: website
images:
- file: assets/images/badges/dc26/hack-for-satan-badge-dc26/3b10df5e3c.jpg
  source: "https://github.com/hackforsatan/impbadge/"
  credit: "Hack for Satan"
  caption: "ImpBadge (DC26) PCB art: a ram/goat-skull illustration with occult and alchemical symbols, red star-shaped LED lit"
contact: {}
notes:
- 300 units in VHS cassette cases
status: released
sources:
- kind: url
  url: https://twitter.com/hackforsatan
  title: Hack for Satan Badge (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
- kind: url
  url: https://fxtwitter.com/hackforsatan/feed.atom.xml
  title: "@hackforsatan tweet archive (via FxTwitter RSS/Atom feed)"
  accessed: '2026-09-07'
  note: Confirmed the DC26/2018 badge is called "ImpBadge," that it hides a text-adventure
    game called Asylum unlocked via puzzles/"seances," that Ryan Sheffield did the
    PCB art and wrote the Asylum script, and that the firmware/source was released
    publicly after the con. A 2019 tweet about the following year's badge ("Badges
    are 100 again this year") implies the 2018 badge also sold for $100.
- kind: url
  url: https://github.com/hackforsatan/impbadge/
  title: hackforsatan/impbadge GitHub repository
  accessed: '2026-09-07'
  note: Firmware source for the ImpBadge. README confirms PIC18F4520 target, XC8
    v1.43 compiler, PICKit 3 programmer, version 1.0.666. Source tree shows a QT1110
    capacitive touch driver, screen/display modules, an RPG/game engine (imp_rpg.c),
    a seance module, an EEPROM save module, and a pentagram LED-pattern module. No
    LICENSE file present. Only a placeholder image exists under docs/art/pcb; no
    schematic or gerber files found in the repo.
- kind: url
  url: https://raw.githubusercontent.com/hackforsatan/impbadge/master/seance.jpeg
  title: seance.jpeg (README hero image, "IMPBADGE 2018")
  accessed: '2026-09-07'
  note: Photo of five assembled ImpBadge units, used as the archive's saved image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core identity, MCU, firmware architecture, and the hidden Asylum game
    are confirmed from the maker''s own GitHub repo and tweets. Not confirmed for
    the 2018 (DC26) badge specifically: exact LED count, display part/size, battery
    type, quantity made (the sheet''s "300 units in VHS cassette cases" note is
    kept as-is but not independently verified for this year), and whether it is
    sold out today. The $100 price is inferred from a 2019 tweet about the following
    year''s badge that says the price is "100 again this year," implying the 2018
    price was also $100 — flagged as inference rather than a direct DC26 quote.
    No PCB design files (schematic/gerbers) were found published, only firmware
    source and a small placeholder art image, hence make_your_own.open_source is
    marked "partial" rather than "yes."'
last_modified_date: '2026-09-07'
---

The ImpBadge was Hack for Satan's badge for DEF CON 26 (2018): a black PCB shaped
around a ram/goat-skull illustration surrounded by alchemical symbols, drawn by
Ryan Sheffield, with a cluster of red LEDs forming a five-point star near the top.
Under the art is a PIC18F4520 microcontroller running custom C firmware (built with
XC8 v1.43 via a PICKit 3) that drives a small onboard screen, reads a QT1110 capacitive
touch sensor, and saves game state to EEPROM.

The badge's main feature is a hidden text-adventure horror game called "Asylum,"
worked into the firmware alongside a "seance" puzzle mechanic; attendees pieced
together in-person clues and on-badge interactions to unlock it during the con.
After DEF CON 26 ended, Hack for Satan released the full firmware source on GitHub
and later put up a browser-playable version of Asylum with all of its unlockable
items already open, so people who missed the badge could still finish the game.

## Make your own

Firmware source (C, targeting a PIC18F4520 via Microchip's XC8 toolchain and a
PICKit 3 programmer) is published at https://github.com/hackforsatan/impbadge/.
No PCB schematic or gerber files were found in the repo, so recreating the hardware
itself would mean reverse-engineering the board from photos.
