---
title: THOTCON 0xC Badge
id: thotcon-2023-thotcon-0xc-badge
layout: badge
parent: THOTCON 0xC
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: thotcon-2023
year: 2023
makers:
- name: Rob Rehrig (design), Fourfold (assembly/manufacturing)
summary: 'The official THOTCON 0xC (2023) conference badge: an ESP32 board in a
  custom injection-molded clear polycarbonate shell shaped like the target from
  the NES game Contra, built to run a conference-wide infrared laser-tag game.'
functions: 'Conference-wide infrared laser-tag game inspired by Contra: a center
  IR receiver flanked by two IR emitters (each with a total-internal-reflection
  lens for a focused, long-range beam) let attendees "tag" each other''s badges.
  Also drives an RGB LED animation, a small speaker for sound effects/music, a
  D-pad and touch input, and was required for entry to the official 0xC party.'
look:
  colors:
  - clear
  shape: crosshair / target
  themes:
  - video game
  - retro computer
  - arcade
tech:
  mcu: ESP32
  leds:
    type: driven by IS31FL3731
    note: RGB LEDs arranged in an X/crosshair pattern around the IR receiver, driven
      through a Lumissil IS31FL3731 matrix LED driver
  display: none
  connectivity:
  - ir
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'approximately 2,000'
  availability: free
  distribution:
  - free_drop
  where: Given to THOTCON 0xC (May 19-20, 2023, Chicago) attendees; badge-required
    for entry to the official 0xC party. No longer available.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ristich/TC0xC/tree/main/Hardware
  firmware_url: https://github.com/ristich/TC0xC/tree/main/Firmware
  eda_tool: null
links:
- label: badge.gallery/badges/thotcon-0xc-badge
  url: https://badge.gallery/badges/thotcon-0xc-badge
  kind: website
- label: www.reddit.com/r/Thotcon/comments/y7ntzz/thotcon_0xc_ticket_update_update
  url: https://www.reddit.com/r/Thotcon/comments/y7ntzz/thotcon_0xc_ticket_update_update/
  kind: social
- label: robrehrig.com/TC0xC (designer's writeup)
  url: https://www.robrehrig.com/TC0xC
  kind: article
  note: Rob Rehrig's first-hand design writeup with concept sketches and manufacturing
    notes; accessed 2026-09-08, supported design story, materials, manufacturing,
    quantity.
- label: github.com/ristich/TC0xC (badge repo)
  url: https://github.com/ristich/TC0xC
  kind: repo
  note: Official hardware/firmware repo (Hardware, Firmware, Art, BadgeBattles
    folders); accessed 2026-09-08, supported open-source status, MCU (ESP32),
    LED driver chip (IS31FL3731), touch/audio/IR firmware modules.
images:
- file: assets/images/badges/thotcon-2023/thotcon-0xc-badge/c2711b75f4.png
  source: "https://github.com/ristich/TC0xC"
  credit: "Rob Rehrig / Fourfold"
  caption: "3D render of the THOTCON 0xC badge PCB front, showing the crosshair-target layout with the IR receiver in the center and two IR emitters"
- file: assets/images/badges/thotcon-2023/thotcon-0xc-badge/cd18536c4c.png
  source: "https://github.com/ristich/TC0xC"
  credit: "Rob Rehrig / Fourfold"
  caption: "3D render of the THOTCON 0xC badge PCB back, showing the D-pad, speaker footprint, on/off switch and reset button"
contact: {}
notes:
- Official 2023 THOTCON badge built around a conference-wide, Contra-inspired infrared
  laser-tag game in a custom injection-molded clear polycarbonate enclosure, roughly
  2,000 units manufactured via Xometry. Found by the event-year sweep, task thotcon-b.
- 'Sweep-imported title matched the maker''s own naming; no change needed.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/thotcon-0xc-badge
  title: THOTCON 0xC Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:thotcon-b); event
    read as ''thotcon-2023''.'
- kind: url
  url: https://www.robrehrig.com/TC0xC
  title: "Rob Rehrig dot com — TC0xC"
  accessed: '2026-09-08'
  note: Designer's own writeup; confirmed design story, Contra theme, TIR lens
    optics, polycarbonate housing, Xometry manufacturing, ~2,000 unit quantity.
- kind: url
  url: https://github.com/ristich/TC0xC
  title: 'GitHub - ristich/TC0xC: THOTCON 0xC Badge'
  accessed: '2026-09-08'
  note: Confirmed open-source hardware+firmware, ESP32 MCU, IS31FL3731 LED driver,
    touch/audio/tag firmware modules; source of the two saved PCB render images.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (maker, theme, game mechanic, housing, manufacturing, quantity,
    open-source status, MCU) confirmed via the designer's own writeup and the
    official GitHub repo. Not found in any source, left empty - price paid by
    THOTCON for manufacturing, exact LED count, battery/power spec (repo firmware
    references a rechargeable cell footprint but no capacity is documented), and
    a photo of the assembled/enclosed badge (only bare-PCB renders and a concept
    sketch were found; the enclosure itself was never photographed in a source
    we could reach). Reddit thread in the entry's links could not be fetched (Claude
    Code cannot access www.reddit.com) - left as-is, unverified.
last_modified_date: '2026-09-08'
---

The THOTCON 0xC badge was the official electronic badge for THOTCON 0xC, held May 19-20, 2023 in Chicago. Designed by Rob Rehrig with assembly and manufacturing by Fourfold, it was built around a conference-wide, infrared laser-tag game inspired by the target enemy from the first stage of the NES game *Contra* — the badge's crosshair-shaped PCB directly echoes that in-game target. A center-mounted IR receiver is flanked by two IR emitters, each paired with a custom total-internal-reflection lens that Rehrig developed to give the beam enough range and focus for reliable "tagging" across a room.

The badge's housing was a first for the event: a custom injection-molded clear polycarbonate shell, manufactured through Xometry in a roughly 2,000-unit run. The original plan called for a two-material shell (opaque ABS body with clear polycarbonate windows for the LEDs and lens), but the tight nine-to-ten week manufacturing schedule forced a switch to a single clear polycarbonate piece, letting the badge's own green PCB show through as its "color." On the electronics side the badge runs on an ESP32, drives its LEDs through a Lumissil IS31FL3731 matrix driver, and adds a D-pad, capacitive touch, and a small speaker for sound and music alongside the IR gameplay hardware. The badge was required for entry to the official 0xC after-party, and Rehrig — who did not attend in person — reported that the laser-tag game was a well-received success with attendees.

Both hardware and firmware are published on GitHub (`ristich/TC0xC`), including PCB/enclosure design files, ESP32 firmware sources for the IR tag logic, LED driver, audio and touch handling, and materials from an on-badge "BadgeBattles" CTF component.
