---
title: SAINTCON 2020 badge (compukidmike)
id: saintcon-2020-saintcon-2020-badge-compukidmike
layout: badge
parent: Saintcon 2020
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2020
year: 2020
makers:
- name: compukidmike
  url: https://github.com/compukidmike
summary: 'The official SAINTCON 2020 attendee badge, built as a 17-slot minibadge holder: a soldering kit that comes with its surface-mount parts pre-assembled, plus everything needed to design and produce your own minibadge.'
functions: 'Runs eight discrete LEDs through several animation modes (chase, ring, wave, pulse, alternate, circle) driven by a single button, with the current mode saved to EEPROM. It only supplies power to plugged-in minibadges; no data lines are connected between the main board and the minibadges it holds.'
look:
  colors: []
  shape: null
  themes:
  - minibadge
  - village badge
  - learn to solder
  - kit
tech:
  mcu: ATtiny84A
  leds:
    count: 8
    type: discrete
    note: Eight discrete LEDs on the main board driving several animation modes; the badge's 17 minibadge slots are unpowered pass-throughs with no data lines.
  display: none
  connectivity: []
  battery: 2x AA or micro USB
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed to SAINTCON 2020 attendees as the conference's official badge kit.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/compukidmike/Saintcon2020/tree/main/Hardware
  firmware_url: https://github.com/compukidmike/Saintcon2020/tree/main/Firmware
  eda_tool: KiCad
links:
- label: github.com/compukidmike/Saintcon2020
  url: https://github.com/compukidmike/Saintcon2020
  kind: repo
- label: SAINTCON 2020 - Badge Assembly (YouTube)
  url: https://youtu.be/r8JDBqyHX5A
  kind: video
- label: Minibadge Tutorial Part 1 (YouTube)
  url: https://youtu.be/kkLfmo14oiQ
  kind: video
images:
  - file: assets/images/badges/saintcon-2020/saintcon-2020-badge-compukidmike/e282b36669.jpg
    source: "https://youtu.be/r8JDBqyHX5A"
    credit: "SAINTCON"
    caption: "Still from the official SAINTCON 2020 badge assembly video"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/Saintcon2020
  title: SAINTCON 2020 badge (compukidmike)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''saintcon-2020''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2020/main/README.md
  title: compukidmike/Saintcon2020 README
  accessed: '2026-09-07'
  note: 'Confirms concept (17-slot minibadge holder kit), pre-soldered SMD assembly, 2xAA/micro USB power with no data lines, and the make-your-own-minibadge tutorial links.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2020/main/Firmware/Saintcon2020/Saintcon2020.cppproj
  title: Firmware project file (Atmel Studio)
  accessed: '2026-09-07'
  note: 'Confirms MCU is an ATtiny84A.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2020/main/Firmware/Saintcon2020/main.cpp
  title: Main board firmware source
  accessed: '2026-09-07'
  note: 'Confirms 8 discrete LEDs, button-driven animation modes (chase/ring/wave/pulse/alternate/circle), and EEPROM-stored display state.'
- kind: url
  url: https://www.youtube.com/oembed?url=https://youtu.be/r8JDBqyHX5A&format=json
  title: 'SAINTCON 2020 - Badge Assembly (oEmbed metadata)'
  accessed: '2026-09-07'
  note: 'Confirms the assembly video is published by the official SAINTCON YouTube channel, supporting that this is the conference''s official badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Repo and firmware source confirm hardware/technical details directly. No price, print run size, or attendee-count figures were found anywhere in the repo or linked videos, so get_one.price/quantity are left empty. No photo of the assembled badge itself was found (repo has no image assets); the saved image is a YouTube video-thumbnail still rather than a dedicated product photo. Look colors/shape were not stated by any source and are left empty rather than guessed.'
last_modified_date: '2026-09-07'
---

The SAINTCON 2020 badge, built by compukidmike, was the official attendee badge for that year's SAINTCON (a Utah-based security conference). SAINTCON dubbed 2020 "the year of minibadges": the badge itself is a 17-slot minibadge holder distributed as a soldering kit, with all the fiddly surface-mount parts pre-assembled so attendees only need to solder the easy through-hole pieces. An ATtiny84A on the main board drives eight discrete LEDs through several selectable animation patterns (chase, ring, wave, pulse, alternate, circle) via a single button, remembering the last mode in EEPROM. The badge runs on 2x AA batteries or micro USB, and that power is only routed out to the plugged-in minibadges — there are no data lines between the main board and the minibadges it holds.

What makes this badge notable is the added kit: each one shipped with parts for attendees to design and build their own minibadge (pins, resistors, LEDs) plus a gift certificate for three fabricated copies of that design, so people could trade minibadges at the show. SAINTCON published a full assembly video and a three-part "make your own minibadge" video tutorial series covering KiCad, Inkscape, and svg2shenzhen for laying out badge art, alongside a linked minibadge footprint library.

## Make your own

The GitHub repo publishes full KiCad source for the main board, the vertical/horizontal/daughter boards, and the minibadge holder panels, along with schematic PDFs and the ATtiny84A firmware (Atmel Studio project plus a pre-built .hex). To build one: open the KiCad projects in the `Hardware/` folder to get board files and Gerbers, flash `Firmware/Saintcon2020.hex` to an ATtiny84A (or rebuild from `main.cpp` in Atmel Studio), and follow SAINTCON's own minibadge tutorial series to design a compatible minibadge for the 17 holder slots.
