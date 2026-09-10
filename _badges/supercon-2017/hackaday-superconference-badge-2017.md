---
title: Hackaday Superconference Badge 2017
id: supercon-2017-hackaday-superconference-badge-2017
layout: badge
parent: Supercon 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2017
year: 2017
makers:
- name: Mike Harrison
  url: https://hackaday.io/mikeselectricstuff
summary: A digital camera badge for the 2017 Hackaday Superconference, built around a PIC32 and a 128x128 color OLED, with an OV9650 camera sensor for stills and video plus onboard games.
functions: Takes photos and video with the onboard OV9650 camera sensor, saves them to microSD, and runs built-in games and puzzles; includes an unpopulated expansion header for attendee hardware hacks.
look:
  colors: []
  shape: null
  themes:
  - camera
  - hardware tool
tech:
  mcu: PIC32MX170F256D
  leds: null
  display: 128x128 color OLED
  connectivity: []
  battery: 2x AA
  sao_version: none
get_one:
  price: $99 (post-event extras on Tindie, plus $10 US / $40+ international shipping)
  price_usd: 99
  quantity: ~350
  availability: sold_out
  availability_note: 'Checked 2026-09-07: no longer listed as available; the November 2017 Tindie sale of leftover units was a one-time post-event offer.'
  distribution:
  - free_drop
  - purchase
  where: Given to Supercon 2017 attendees; leftover units later sold on Tindie for $99 plus shipping.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2017/10/11/building-the-hackaday-superconference-badge
  url: https://hackaday.com/2017/10/11/building-the-hackaday-superconference-badge/
  kind: article
  archived: https://web.archive.org/web/20260608090600/https://hackaday.com/2017/10/11/building-the-hackaday-superconference-badge/
- label: hackaday.com/2017/11/08/get-your-hands-on-a-2017-hackaday-superconference-badge
  url: https://hackaday.com/2017/11/08/get-your-hands-on-a-2017-hackaday-superconference-badge/
  kind: article
- label: hackaday.com/2017/11/15/the-perils-of-developing-the-hackaday-superconference-badge
  url: https://hackaday.com/2017/11/15/the-perils-of-developing-the-hackaday-superconference-badge/
  kind: article
  archived: https://web.archive.org/web/20260515222735/https://hackaday.com/2017/11/15/the-perils-of-developing-the-hackaday-superconference-badge/
- label: Mike Harrison (mikeselectricstuff) on Hackaday.io
  url: https://hackaday.io/mikeselectricstuff
  kind: hackaday
  archived: https://web.archive.org/web/20251204204712/https://hackaday.io/mikeselectricstuff
images:
- file: assets/images/badges/supercon-2017/hackaday-superconference-badge-2017/781a9287c9.jpg
  source: https://hackaday.com/2017/11/08/get-your-hands-on-a-2017-hackaday-superconference-badge/
  credit: Hackaday
  caption: Front of the 2017 Hackaday Superconference badge camera
- file: assets/images/badges/supercon-2017/hackaday-superconference-badge-2017/bbaba25158.jpg
  source: https://hackaday.com/2017/11/08/get-your-hands-on-a-2017-hackaday-superconference-badge/
  credit: Hackaday
  caption: Detail of the badge's OLED screen and board
contact: {}
notes:
- Hardware/firmware repo not located this session; the October 2017 article says files were promised "soon" but no working link to a public hardware repo was confirmed. tech.leds left null — an "illuminator LED" for the camera is mentioned but no count/type given. look.colors and look.shape left empty — no source described the PCB color or overall silhouette precisely enough to code confidently.
status: released
sources:
- kind: url
  url: https://hackaday.com/2017/10/11/building-the-hackaday-superconference-badge/
  title: Hackaday Superconference Badge 2017
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''Hackaday Superconference 2017''.'
  archived: https://web.archive.org/web/20260608090600/https://hackaday.com/2017/10/11/building-the-hackaday-superconference-badge/
- kind: url
  url: https://hackaday.com/2017/11/08/get-your-hands-on-a-2017-hackaday-superconference-badge/
  title: Get Your Hands On A 2017 Hackaday Superconference Badge
  accessed: '2026-09-07'
  note: Confirms $99 post-event Tindie price plus shipping, camera/LCD/SD functions, and Mike Harrison as designer.
- kind: url
  url: https://hackaday.com/2017/11/15/the-perils-of-developing-the-hackaday-superconference-badge/
  title: The Perils Of Developing The Hackaday Superconference Badge
  accessed: '2026-09-07'
  note: Confirms PIC32/SRAM chips donated by Microchip, Macrofab contract manufacturing, OLED display, accelerometer, and microSD support.
  archived: https://web.archive.org/web/20260515222735/https://hackaday.com/2017/11/15/the-perils-of-developing-the-hackaday-superconference-badge/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (designer, MCU, display, camera, battery, quantity, price) confirmed across three Hackaday.com articles by the maker/publisher. Hardware/firmware open-source repo not located; LED and PCB color/shape left empty for lack of a clear source.
last_modified_date: '2026-09-07'
---

The 2017 Hackaday Superconference badge was a digital camera, designed and prototyped in a single weekend by Mike Harrison (known online as mikeselectricstuff). Built around a Microchip PIC32MX170F256D microcontroller with a 128x128 color OLED screen and an OV9650 camera sensor, it let attendees shoot stills and video and save them to a microSD card, alongside a set of built-in games and puzzles. It ran on two AA batteries and included an accessible pin header and prototyping space intended for badge hackers to build expansion hardware against.

Roughly 350 units were built for Supercon 2017 attendees, with Microchip donating the PIC32 and SRAM chips and Macrofab handling contract manufacturing. Development had its share of near-misses: a shipment of PIC chips went missing mid-production (forcing an overnight emergency order of 500 replacements before the originals reappeared), production accelerometers turned out to have a different I2C address than the prototype parts, and a sleep-mode power glitch had to be fixed in firmware. The build ran unusually smoothly overall, leaving Hackaday with a small surplus that it sold on Tindie after the event for $99 plus shipping.
