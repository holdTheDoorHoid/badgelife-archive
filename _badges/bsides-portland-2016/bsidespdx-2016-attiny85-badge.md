---
title: BSidesPDX 2016 ATTiny85 Badge
id: bsides-portland-2016-bsidespdx-2016-attiny85-badge
layout: badge
parent: BSidespdx 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-portland-2016
year: 2016
makers:
- name: PDX Badgers
summary: 'A capacitive-touch LED badge with a 36-LED array, made by PDX Badgers for BSidesPDX 2016.'
functions: 'Runs a four-step LED pattern animation plus an alternate sine/cosine analogWrite loop; a capacitive touch pad changes the pattern.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ATtiny85
  leds:
    count: 36
    type: discrete
    note: 36 yellow 0603 LEDs driven via PWM
  display: none
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: 'Given away to attendees at BSidesPDX 2016; a Calagator listing for the con mentions PCB badges, T-shirts, and bags to give away, with donors prioritized, but no confirmed final quantity.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/pdxbadgers/pcb-2016
  firmware_url: https://github.com/pdxbadgers/pcb-2016
  eda_tool: Eagle
links:
- label: badge.gallery/badges/bsidespdx-2016-attiny85-badge
  url: https://badge.gallery/badges/bsidespdx-2016-attiny85-badge
  kind: website
- label: github.com/pdxbadgers/pcb-2016
  url: https://github.com/pdxbadgers/pcb-2016
  kind: repo
images: []
contact: {}
notes:
- ATTiny85-based capacitive LED PCB conference badge for BSidesPDX 2016. Found by the event-year sweep, task bsides-portland.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/bsidespdx-2016-attiny85-badge
  title: BSidesPDX 2016 ATTiny85 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-portland); event read as ''BSidesPDX 2016''.'
- kind: url
  url: https://badge.gallery/badges/bsidespdx-2016-attiny85-badge
  title: BSidesPDX 2016 ATTiny85 Badge
  accessed: '2026-09-10'
  note: 'Confirmed chip (ATTINY85-20SUR @ 1MHz), 36 yellow 0603 LEDs, CR2032 power, capacitive touch input, and the PDX Badgers GitHub repo as the design-file source; no photo of the physical badge could be recovered.'
- kind: url
  url: https://github.com/pdxbadgers/pcb-2016
  title: pdxbadgers/pcb-2016
  accessed: '2026-09-10'
  note: 'PDX Badgers GitHub repo confirming open hardware/firmware: badge.brd, badge.sch (Eagle), BoM.csv, and badge.ino firmware. Page rendering was limited; file contents were not individually verified.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'No maker photo of the physical badge could be found; images left empty rather than guessed. Price and exact production quantity are not stated anywhere found; get_one.where reflects the only distribution detail located (a Calagator con listing). GitHub repo file contents (BoM, schematic, firmware) were not individually opened to verify every technical claim beyond what badge.gallery already summarized from them.'
last_modified_date: '2026-09-10'
---

The BSidesPDX 2016 badge is an ATtiny85-based PCB badge made by PDX Badgers, the volunteer group behind BSidesPDX's badge program, for the 2016 event at the Oregon Convention Center in Portland. It carries a 36-LED array of yellow 0603 LEDs driven by the ATtiny85's PWM outputs, runs off a CR2032 coin cell, and uses a capacitive touch pad to switch between a four-step LED animation and an alternate sine/cosine fade pattern.

The badge was given away to attendees rather than sold; a contemporaneous Calagator listing for the con mentions PCB badges, T-shirts, and bags being distributed with donors prioritized, though no exact production count survives in the sources found. PDX Badgers published the full design as open hardware and firmware in the `pdxbadgers/pcb-2016` GitHub repository, including Eagle board and schematic files, a bill of materials, and the Arduino firmware.

No photograph of the physical badge could be located during this research pass, so the entry remains source-backed but without an image.


