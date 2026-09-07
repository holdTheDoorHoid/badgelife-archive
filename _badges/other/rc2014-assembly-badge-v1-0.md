---
title: RC2014 Assembly Badge v1.0
id: other-rc2014-assembly-badge-v1-0
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: Spencer (RC2014 creator)
  url: https://rc2014.co.uk/
summary: A conference name badge shaped like an RC2014 bus module, wired to the RC2014 Z80 retrocomputer's bus lines so 38 LEDs blink out its address, data, and control signals as it runs.
functions: 'Displays the wearer''s name on silkscreen while acting as a live "logic analyser" for a paired RC2014 Micro: 38 LEDs light up along the address bus (red), data bus (green), control signals (white), and serial/user signals (orange) as the Z80 steps through memory at a deliberately slowed clock speed, producing a blinkenlights effect.'
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - hardware tool
  - learn to solder
tech:
  mcu: Z80
  leds:
    count: 38
    type: discrete
    note: Color-coded by bus function - red (address), green (data), white (control), orange (serial/user)
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of the RC2014 Assembly meetup at The National Museum of Computing, Bletchley Park, UK
make_your_own:
  open_source: partial
  hardware_url: https://rc2014.co.uk/modules/other-modules/rc2014-assembly-badge-v1-0/
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2025/09/28/decorate-your-neck-with-the-first-z80-badge
  url: https://hackaday.com/2025/09/28/decorate-your-neck-with-the-first-z80-badge/
  kind: article
- label: rc2014.co.uk/modules/other-modules/rc2014-assembly-badge-v1-0
  url: https://rc2014.co.uk/modules/other-modules/rc2014-assembly-badge-v1-0/
  kind: hackaday
- label: "RC2014 Assembly - The National Museum of Computing"
  url: https://www.tnmoc.org/events/2025/9/20/rc2014-assembly
  kind: website
images:
  - file: assets/images/badges/other/rc2014-assembly-badge-v1-0/2d156a9d21.jpg
    source: "https://rc2014.co.uk/modules/other-modules/rc2014-assembly-badge-v1-0/"
    credit: "Spencer / RC2014"
    caption: "Front of the RC2014 Assembly Badge v1.0 PCB"
  - file: assets/images/badges/other/rc2014-assembly-badge-v1-0/bf9eaaa541.jpg
    source: "https://rc2014.co.uk/modules/other-modules/rc2014-assembly-badge-v1-0/"
    credit: "Spencer / RC2014"
    caption: "Badge worn on a lanyard, LEDs lit during operation"
contact: {}
notes:
- Claimed first Z80-powered event badge; based on RC2014 Micro
- 'Made for RC2014 Assembly, a one-day RC2014/retrocomputing meetup held 2025-09-20 at The National Museum of Computing, Bletchley Park, UK. No matching event id exists yet in events.yml (closest categories are DEF CON/vendor-con badges); left under "other" pending a dedicated event entry for this meetup.'
- Maker calls it v1.0 and notes a "bodge" issue with an RX pin pullup that interfered with signals; a revised version was not documented in the sources checked.
- Page includes schematic and photos but no published Gerbers, BOM, or KiCad project link was found; hardware_url points to the project page itself which shows design detail (schematic image) rather than a downloadable source repo, so open_source is marked partial.
status: released
sources:
- kind: url
  url: https://hackaday.com/2025/09/28/decorate-your-neck-with-the-first-z80-badge/
  title: RC2014 Assembly Badge v1.0
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''RC2014 Assembly 2025''.'
- kind: url
  url: https://rc2014.co.uk/modules/other-modules/rc2014-assembly-badge-v1-0/
  title: RC2014 Assembly Badge v1.0 « RC2014
  accessed: '2026-09-07'
  note: Maker's own project page; source of LED count/colors, chip, and the "bodge" note.
- kind: url
  url: https://www.tnmoc.org/events/2025/9/20/rc2014-assembly
  title: RC2014 Assembly - The National Museum of Computing
  accessed: '2026-09-07'
  note: Confirms the event date (2025-09-20) and venue (TNMOC, Bletchley Park).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own page and Hackaday agree on the core facts. Could not find price, quantity made, or a downloadable design-file archive (Gerbers/KiCad); left those empty. Event is a specific one-day RC2014/retrocomputing meetup ("RC2014 Assembly") rather than a large con, and has no matching id in events.yml, so it stays under "other" - name the event explicitly if a dedicated entry is ever added.'
last_modified_date: '2026-09-07'
---

Spencer, the designer of the RC2014 homebrew Z80 computer kit, made this badge for the RC2014 Assembly, a one-day retrocomputing meetup held on 20 September 2025 at The National Museum of Computing in Bletchley Park, UK. What started as a plan for a simple RC2014-module-shaped badge with a silkscreen name plate grew into a working piece of RC2014 hardware in its own right: the PCB carries 38 LEDs wired to the bus lines of a paired RC2014 Micro, color-coded red for address lines, green for data lines, white for control signals, and orange for serial and user signals.

When connected to a Z80-based RC2014 Micro running at a deliberately slowed clock (and powered from a USB battery bank), the badge turns into a wearable logic analyser, its LEDs blinking out the bus activity as the processor steps through memory addresses. Spencer and Hackaday both believe it may be the first event badge built around a Z80 processor, though commenters noted earlier 6502-based badges from as far back as 2017.

The v1.0 design shipped with at least one known hardware quirk - a pullup on an RX pin that interfered with a signal line - which the maker documented as a "bodge" to work around on this batch. No price, production quantity, or standalone Gerber/KiCad download was found; the project page shows the schematic and board photos but the badge appears to have been a giveaway tied to attending the meetup rather than a separate storefront item.
