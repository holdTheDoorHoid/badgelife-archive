---
title: BlinkyBracelet
id: other-blinkybracelet
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 2017
makers:
- name: Nisha K.
  url: https://nishakm.github.io/things/blinkybracelet/
summary: A DIY LED bracelet built to look like ordinary jewelry, with charlieplexed lights that blink when a button is pressed.
functions: Blinks a charlieplexed array of LEDs on button press; built as a personal exercise in driving many LEDs from few microcontroller pins.
look:
  colors: []
  shape: null
  themes:
  - jewelry
  - wearable
  - learn to solder
tech:
  mcu: none stated (prototype ran on an Arduino Uno)
  leds:
    count: 30
    type: charlieplexed
    note: Driven from 6 microcontroller pins (3, 5, 6, 9, 10, 11) using charlieplexing.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not sold; a personal/DIY project. Source files are on GitHub for anyone to build their own.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/nishakm/blinkybracelet
  firmware_url: https://github.com/nishakm/blinkybracelet
  gerbers_url: null
  bom_url: null
  eda_tool: EagleCAD
  license: 'Apache-2.0 (repository); the initial Arduino Uno prototype sketch is separately marked "Do What You Want"'
  fab_url: null
  notes: Repo also includes FreeCAD/STL files for a 3D-printed bangle enclosure.
links:
- label: nishakm.github.io/things/blinkybracelet
  url: https://nishakm.github.io/things/blinkybracelet/
  kind: website
- label: GitHub - nishakm/blinkybracelet
  url: https://github.com/nishakm/blinkybracelet
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://nishakm.github.io/things/blinkybracelet/
  title: BlinkyBracelet
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other (personal learning project, 2016/2017, not made for a specific con)''.'
- kind: url
  url: https://github.com/nishakm/blinkybracelet
  title: 'GitHub - nishakm/blinkybracelet'
  accessed: '2026-09-07'
  note: 'Confirmed license (Apache-2.0), repo contents (Arduino sketches, FreeCAD/STL bangle files, EagleCAD board files), and that the maker calls it a learning project rather than a finished product.'
- kind: url
  url: https://raw.githubusercontent.com/nishakm/blinkybracelet/master/sketch_blinkybracelet/sketch_blinkybracelet.ino
  title: sketch_blinkybracelet.ino
  accessed: '2026-09-07'
  note: 'Source comments confirm the initial prototype ran on an Arduino Uno 3 and drove 30 LEDs via charlieplexing on 6 pins.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Not made for any specific convention; it is a personal maker/learning project by Nisha K., started
    around April 2017 (repo created 2017-04-29). No price, quantity, or distribution info exists because
    it was never sold or given away as a badge/SAO in the usual sense — it's a DIY tutorial-style build.
    No photos of the finished bracelet were found on the project page or in the repo (only CAD/board/STL
    files and Arduino sketches), so images are left empty. The repo also contains a separate, later
    sub-project in banglet/ named "503Banglet" (EagleCAD files dated "dc5032018banglet"), using an
    Adafruit Bluefruit nRF52 module for BLE rather than charlieplexed LEDs — this looks like a distinct
    item tied to DC503 (the Portland DEF CON group) circa 2018, reported separately below rather than
    folded into this entry.
last_modified_date: '2026-09-07'
---

BlinkyBracelet is a DIY wearable built by Nisha K. around April 2017, aimed at proving that a functional piece of blinky tech jewelry could still look subtle enough to pass as ordinary jewelry in non-technical settings. The bracelet lights up a grid of LEDs on a button press, with the electronics driven from an early Arduino Uno prototype.

Rather than a full custom PCB, the project drives 30 LEDs from just 6 microcontroller pins using charlieplexing, and pairs the electronics with a 3D-printed bangle enclosure (FreeCAD source and an STL are included in the repo). The maker describes it as "more of a learning project than something that can be used and modified," though the full source — several Arduino sketch iterations, a unit-test sketch, and the enclosure files — is published on GitHub under Apache-2.0 for anyone to reuse.

This was never sold, kitted, or distributed at an event; it's a solo build documented on the maker's personal project blog, so there is no price, quantity, or con tie-in to record.
