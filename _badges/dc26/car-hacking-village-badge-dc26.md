---
title: Car Hacking Village Badge (DC26)
id: dc26-car-hacking-village-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Car Hacking Village
summary: The 2018 (DEF CON 26) Car Hacking Village badge, a wrench-shaped PCB badge with an unusually dense LED matrix, built to double as an OBD-II CAN bus hacking tool.
functions: Connects to a car's OBD-II port for CAN bus scripting/hacking exercises; also functions as a wearable LED badge with two rows of LEDs (purple exterior ring, RGB interior) driven by shift registers.
look:
  colors: []
  shape: wrench
  themes:
  - hardware tool
  - security
  - village badge
tech:
  mcu: NXP S32/K22/S99 (three microcontrollers)
  leds:
    count: 320
    type: 0404
    note: Two rows of 0404 LEDs (purple on the outer row, RGB on the inner row), scanned via five 74HC595 shift registers.
  display: null
  connectivity:
  - usb
  - uart
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed at the DEF CON 26 (2018) Car Hacking Village; secondhand units have since turned up on eBay and WorthPoint.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  kind: article
- label: blog.stackattack.net/2018/09/02/defcon-26-badge-photos
  url: https://blog.stackattack.net/2018/09/02/defcon-26-badge-photos/
  kind: article
images:
- file: assets/images/badges/dc26/car-hacking-village-badge-dc26/ab7a69a97b.jpg
  source: "https://blog.stackattack.net/2018/09/02/defcon-26-badge-photos/"
  credit: "Hermit's Cave (blog.stackattack.net)"
  caption: "Both sides of the DC26 Car Hacking Village wrench-shaped badge, photographed with a quarter for scale"
contact: {}
notes:
- 'Sweep''s original wording: "Wrench-shaped 2018 CHV badge described as the most TSA-unfriendly badge of the con, dense LED matrix." That description is accurate but the sweep had cited the wrong Hackaday URL (vol. 2, which never mentions this badge); the correct article is vol. 1, linked above.'
status: released
sources:
- kind: url
  url: https://hackaday.com/2018/08/21/all-the-badges-of-def-con-26-vol-2/
  title: Car Hacking Village Badge (DC26)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc26-indie); event read as ''dc26''.'
- kind: url
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  title: 'All the Badges of DEF CON 26 (vol 1)'
  accessed: '2026-09-08'
  note: 'Correct source article (the sweep had linked vol. 2 by mistake, which does not mention this badge). Confirms wrench shape, TSA-unfriendly size, 320-LED dense matrix in two rows (purple outer, RGB inner), five 74HC595 shift registers, three NXP microcontrollers (S32/K22/S99), OBD-II CAN bus scripting, USB and SD card connectivity, and that this was the 4th year of the CHV badge; also notes the original PCB supplier abandoned the job three days before the con, forcing a scramble to complete production.'
- kind: url
  url: https://www.worthpoint.com/worthopedia/defcon-26-car-hacking-village-badge-3924631632
  title: 'DEFCON 26 Car Hacking Village Badge - DC 26 CHV Wrench - WorthPoint'
  accessed: '2026-09-08'
  note: 'Secondhand listing confirming the badge exists and circulated after the con (page itself blocked by a bot check; used only the public search snippet, which says it was ordered from the manufacturer post-con with "upgraded circuitry").'
- kind: url
  url: https://blog.stackattack.net/2018/09/02/defcon-26-badge-photos/
  title: 'DEFCON 26 Badge Photos - Hermit''s Cave'
  accessed: '2026-09-08'
  note: 'Source of the saved photo (both sides of the badge with a quarter for scale).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (shape, LED count/layout, MCUs, OBD-II function, TSA anecdote, 4th-year production trouble) confirmed by Hackaday''s own write-up. No maker name beyond "Car Hacking Village" the group was found — no individual designer credited in the source, and no CHV GitHub repo or Google Drive SDK link surfaced specifically for the 2018/DC26 board (a companion repo, ttepatti/Car-Hacking-Village-Badges, lists 2018 as sourced from a private Google Drive folder, not public). Price, quantity made, and open-source status remain unknown. Confidence is medium rather than high because the primary confirming source is press coverage (Hackaday), not the maker''s own page or repo.'
last_modified_date: '2026-09-08'
---

The 2018 Car Hacking Village badge, given out at DEF CON 26, breaks from the typical rectangular badge shape: it is cut in the outline of a wrench, and large enough that at least one attendee found it ran afoul of TSA carry-on size rules on the way home. Underneath the theme is a serious piece of hardware — 320 individual 0404 LEDs packed into two rows (a purple outer ring and an RGB inner row), scanned by five 74HC595 shift registers and driven by three separate NXP microcontrollers (S32, K22, and S99 parts). Alongside the light show, the badge doubles as a real car-hacking tool: an OBD-II connector lets it tap a vehicle's CAN bus, with a small scripting language for reading and manipulating that traffic, plus USB and SD card support for saving captures.

This was the fourth consecutive year the Car Hacking Village had produced its own badge, and 2018's build did not go smoothly — the team's original PCB manufacturer dropped the job with only three days' notice before the badges were due, and the group had to scramble to get boards produced in time for the con. Despite that, badges did make it out to the Village, and examples have since surfaced in secondhand listings on eBay and WorthPoint (one description mentions units later ordered directly from the manufacturer post-con, with "upgraded circuitry").

No individual designer is credited by name in available coverage, and no public hardware or firmware repository specific to the 2018 board was located — a badge-history repo maintained by a community member notes that the 2018 SDK/design files were shared only through a private Google Drive folder rather than GitHub, so they are not independently verifiable here.
