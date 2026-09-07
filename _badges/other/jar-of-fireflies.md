---
title: Jar of Fireflies
id: other-jar-of-fireflies
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 2016
makers:
- name: securelyfitz
  url: https://github.com/securelyfitz
summary: An ATtiny85-based soldering kit that lights six charlieplexed LEDs inside a glass jar to look like fireflies, with capacitive touch sensing through the jar's metal ring.
functions: 'Drives 6 charlieplexed LEDs to create a flickering firefly effect; a capacitive-touch sensor (using the jar''s metal ring plus an exposed ground pad) can trigger or change behavior. Runs from a CR2032 coin cell, with an optional reset button.'
look:
  colors: []
  shape: null
  themes:
  - nature
  - learn to solder
  - kit
tech:
  mcu: ATtiny85
  leds:
    count: 6
    type: reverse-mount
    note: Charlieplexed across 3 I/O pins; through-hole LED pads are also provided as an alternative to the reverse-mount build shown.
  display: null
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/securelyfitz/JarOfFireflies/tree/master/hardware
  firmware_url: https://github.com/securelyfitz/JarOfFireflies/tree/master/software
  eda_tool: Eagle
  notes: 'Hardware is an Eagle library (firefly.lbr) plus gerbers; firmware is an Arduino sketch. The PDF in the repo (JarOfFireflies.pdf) is a step-by-step build/assembly guide with photos.'
links:
- label: github.com/securelyfitz/JarOfFireflies
  url: https://github.com/securelyfitz/JarOfFireflies
  kind: repo
- label: Jason Webb's original Jar of Fireflies
  url: https://github.com/jasonwebb/Jar-of-Fireflies
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- 'Not actually an SAO: it has no SAO connector (sao_version: none) and is not tied to any specific
  conference or event. It is a standalone ATtiny85 soldering kit built to fit inside a glass jar,
  created in 2016 by GitHub user securelyfitz as an explicit derivative of Jason Webb''s earlier
  Jar of Fireflies project. No event, price, or quantity-made information was found, so event is
  left as ''other'' and year reflects the repository''s creation date rather than a confirmed con
  appearance.'
status: listed
sources:
- kind: url
  url: https://github.com/securelyfitz/JarOfFireflies
  title: Jar of Fireflies
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/securelyfitz/JarOfFireflies/master/README.md
  title: 'securelyfitz/JarOfFireflies README'
  accessed: '2026-09-07'
  note: 'Confirmed MCU (ATtiny85), BOM, charlieplexed LED wiring, capacitive touch design, CR2032 power, and that it is a derivative of Jason Webb''s Jar of Fireflies.'
- kind: url
  url: https://api.github.com/repos/securelyfitz/JarOfFireflies/contents/
  title: 'securelyfitz/JarOfFireflies repo contents'
  accessed: '2026-09-07'
  note: 'Confirmed hardware (Eagle library + gerbers) and software (Arduino sketch) directories are both present, i.e. fully open source.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No con/event, price, quantity, or availability information exists for this project anywhere
    in the repo; it reads as a personal/educational soldering-kit project rather than a badge or SAO
    made for a specific conference. No photos of the finished item were found outside a PDF build
    guide embedded in the repo (not extracted). Repo creation date (2016-05-21) used as year in the
    absence of any stated release date.'
last_modified_date: '2026-09-07'
---

Jar of Fireflies is an open-source ATtiny85 soldering project by GitHub user securelyfitz, built as an explicit derivative of an earlier project of the same name by Jason Webb. A small through-hole PCB sits inside a glass jar and drives six charlieplexed LEDs across three of the ATtiny's I/O pins to produce a flickering, firefly-like glow, powered by a CR2032 coin cell. Two more I/O pins run a capacitive-touch sensor: touching the jar's metal ring together with an exposed ground pad completes the circuit, since the ring itself can't sense capacitance without the builder providing a ground path.

The project is fully open source: the repository includes an Eagle library and gerbers for the board, an Arduino sketch for the firmware (reusing Paul Stoffregen's CapacitiveSensor library and Jason Webb's charlieplexing code), and a PDF walkthrough with build photos. It reads as a standalone educational soldering kit rather than a badge or SAO made for any particular convention — it has no SAO connector, and no source found ties it to a specific event, price, or production run.
