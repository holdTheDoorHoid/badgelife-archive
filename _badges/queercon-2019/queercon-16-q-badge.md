---
title: Queercon 16 Q Badge
id: queercon-2019-queercon-16-q-badge
layout: badge
parent: Queercon 16
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: queercon-2019
year: 2019
makers:
- name: Evan Mackay, George Louthan, Tara Scape, Subterfuge
summary: 'A companion "ARG control panel" badge for Queercon 16, with a custom membrane keyboard and an e-ink display.'
functions: 'Acts as a control panel for the con''s ARG; communicates with other badges over a wired RJ12 link.'
look:
  colors: [multicolor]
  shape: null
  themes: [sci-fi]
tech:
  mcu: TI CC2640R2
  leds:
    count: 18
    type: RGB
    note: 6 side-view RGB LEDs lighting the display edges through 3D-printed bezels, plus 12 more full-color LEDs around the PCB perimeter; driven by a Holtek HT16D35B LED controller.
  display: 2.9" e-ink (128x296)
  connectivity: [ble, uart]
  battery: 2x AA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard
  url: https://hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard/
  kind: article
images:
  - file: assets/images/badges/queercon-2019/queercon-16-q-badge/4b97a2adfd.jpg
    source: "https://hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard/"
    credit: "Hackaday / Queercon badge team"
    caption: "Queercon 16 Q Badge with membrane keyboard and eInk display"
contact: {}
notes:
- Primary Queercon 16 (DC27) badge with custom membrane keyboard, 2.9in eInk display, BLE, acting as ARG control panel; not in archive. Found by the event-year sweep, task dc27-badges.
- 'Sweep called it "Primary Queercon 16 (DC27) badge"; Hackaday''s own coverage treats it as a distinct "Q Badge"/ARG control panel alongside the separately catalogued main Queercon 16 badge (queercon-2019-queercon-16-badge, credited to duplico) — kept the sweep''s "Q Badge" title since that matches Hackaday''s framing.'
status: released
sources:
- kind: url
  url: https://hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard/
  title: Queercon 16 Q Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-badges); event read as ''queercon-2019''.'
- kind: url
  url: https://hackaday.com/2019/08/16/hands-on-queercon-16-hardware-badge-shows-off-custom-membrane-keyboard/
  title: "Hands-On: Queercon 16 Hardware Badge Shows Off Custom Membrane Keyboard"
  accessed: '2026-09-08'
  note: "Confirmed the badge exists and pulled team, chip, display, LED, keyboard, and power details; source of the featured image."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed on Hackaday''s own hands-on coverage (a maker/team is credited but no maker-run project page or repo was found for this specific badge, hence medium confidence). Price and quantity for the finished badge are not stated in the article (only that the membrane keyboard component alone cost ~$5/unit at a 700-unit run, which is not the same as the badge''s retail price or total production count) — left empty rather than guessed. No open-source hardware/firmware links found for this specific badge (a repo, duplico/qc16_badge, exists on GitHub but its README does not confirm it is for this "Q Badge" rather than the separately catalogued main Queercon 16 badge, so it was not added). No additional photos beyond the one saved were found.'
last_modified_date: '2026-09-08'
---

The Queercon 16 "Q Badge" was a companion device built alongside Queercon 16's main electronic badge in 2019, serving as a control panel for the convention's alternate-reality game. A team of four — Evan Mackay, George Louthan, Tara Scape, and Subterfuge — built it around a TI CC2640R2 Bluetooth-capable microcontroller, a 2.9" e-ink display (128x296), and a custom CMYK membrane keyboard with embossed buttons laid out in a circle and tailored to the ARG's puzzles. Tara Scape's artwork gives the badge what Hackaday described as a "Rainbow Blade Runner" look.

Lighting comes from 18 RGB LEDs total: six side-view LEDs lighting the display's edges through 3D-printed bezels, driven together with twelve more perimeter LEDs by a Holtek HT16D35B controller. The badge talks to others over a wired RJ12 (6P6C) jack rather than (or in addition to) its BLE radio, and runs off two AA batteries through a Skyworks voltage regulator.

No maker-published project page, price, production quantity, or open-source hardware/firmware release for this specific badge was found; what is documented above comes from Hackaday's hands-on coverage at the show.
