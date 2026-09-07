---
title: CypherCon Badge with Paper Tape Reader
id: cyphercon-2019-cyphercon-badge-with-paper-tape-reader
layout: badge
parent: Cyphercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2019
year: 2019
makers:
- name: tymkrs
  url: https://twitter.com/tymkrs
summary: 'The official CypherCon 4.0 (2019) conference badge, built by tymkrs around a working mechanical paper-tape reader that unlocks a hidden "party mode" when fed the correct punched pattern.'
functions: 'Reads 8-bit-plus-clock punched paper tape via IR emitters/sensors to trigger a hidden LED party mode; a "Semaphore panel" of 25 LEDs lights up in five-person groups when a valid tape is fed through. Tymkrs also ran an on-site tape-punching machine so attendees could create their own tapes.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
  - puzzle
tech:
  mcu: PIC16F15355
  leds:
    count: 25
    type: null
    note: Arranged in five-person groups on a "Semaphore panel"; red and red/green LEDs per Hackaday's photos.
  display: null
  connectivity: []
  battery: CR2450
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
- label: hackaday.com/2019/04/12/cyphercon-badge-has-a-paper-tape-reader-built-in
  url: https://hackaday.com/2019/04/12/cyphercon-badge-has-a-paper-tape-reader-built-in/
  kind: article
  archived: https://web.archive.org/web/20260607082900/https://hackaday.com/2019/04/12/cyphercon-badge-has-a-paper-tape-reader-built-in/
- label: hackaday.com/2019/04/28/emulate-a-paper-tape-to-be-life-and-soul-of-the-cyphercon-party
  url: https://hackaday.com/2019/04/28/emulate-a-paper-tape-to-be-life-and-soul-of-the-cyphercon-party/
  kind: article
  archived: https://web.archive.org/web/20260411171825/https://hackaday.com/2019/04/28/emulate-a-paper-tape-to-be-life-and-soul-of-the-cyphercon-party/
images:
- file: assets/images/badges/cyphercon-2019/cyphercon-badge-with-paper-tape-reader/21c70f8f3b.jpg
  source: "https://hackaday.com/2019/04/12/cyphercon-badge-has-a-paper-tape-reader-built-in/"
  credit: "tymkrs"
  caption: "Front of the CypherCon 4.0 badge with paper tape reader"
- file: assets/images/badges/cyphercon-2019/cyphercon-badge-with-paper-tape-reader/40902bb8ca.jpg
  source: "https://hackaday.com/2019/04/12/cyphercon-badge-has-a-paper-tape-reader-built-in/"
  credit: "tymkrs"
  caption: "Close-up of the punched paper tape feeding through the badge's IR tape reader"
contact: {}
notes:
- Same tymkrs team that built the 2018 DEF CON 26 badge and earlier CypherCon badges; badge has a built-in mechanical paper-tape reader used to unlock a hidden party mode. Companion article documents a separate tape-emulator accessory built by an attendee (Gigawatts, using a TI Stellaris LaunchPad) to trigger the same mode after AND!XOR revealed its existence.
status: listed
sources:
- kind: url
  url: https://hackaday.com/2019/04/12/cyphercon-badge-has-a-paper-tape-reader-built-in/
  title: CypherCon Badge has a Paper Tape Reader Built In
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: bsides-regional (US regional hacker cons: BSides variants, ShmooCon, Thotcon, CypherCon, DerbyCon, CarolinaCon, GrrCON, ToorCon, HOPE, CactusCon, WWHF, Circle City Con, Layer8, Blue Team Con, ShellCon, NorthSec, Hackfest)); event read as ''CypherCon (Milwaukee, 2019)''.'
  archived: https://web.archive.org/web/20260607082900/https://hackaday.com/2019/04/12/cyphercon-badge-has-a-paper-tape-reader-built-in/
- kind: url
  url: https://hackaday.com/2019/04/12/cyphercon-badge-has-a-paper-tape-reader-built-in/
  title: CypherCon Badge has a Paper Tape Reader Built In
  accessed: '2026-09-07'
  note: 'Primary source: maker (tymkrs), event/year (Cyphercon 4.0, Milwaukee, April 2019), features (IR paper-tape reader, 25-LED Semaphore panel, hidden party mode, on-site tape-punching machine), MCU (PIC16F15355), power (CR2450), and photo URLs.'
- kind: url
  url: https://hackaday.com/2019/04/28/emulate-a-paper-tape-to-be-life-and-soul-of-the-cyphercon-party/
  title: Emulate A Paper Tape To Be Life And Soul Of The CypherCon Party
  accessed: '2026-09-07'
  note: 'Confirms the hidden party-mode mechanic (all lights flash) and documents an attendee-built tape emulator (Gigawatts, TI Stellaris LaunchPad) after AND!XOR publicized the hidden mode.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Both sources are Hackaday coverage, not tymkrs''s own project page, so confidence is medium rather than high. No tymkrs project page, GitHub repo, storefront, price, quantity made, or open-source design files were found in the sources read; a web search budget limit prevented further searches for a tymkrs.io/hackaday.io project page or repo. LED color/type beyond "red and red/green" per photos is not stated explicitly in the text. look.shape left null: sources describe a modular three-panel vertical design but do not give a single simple shape word.'
last_modified_date: '2026-09-07'
---

The CypherCon 4.0 badge, built by the tymkrs team (The Toymakers, also behind the 2018 DEF CON 26 badge) for CypherCon in Milwaukee in April 2019, centers on a working mechanical paper-tape reader. A three-panel vertical PCB assembly built around a PIC16F15355 microcontroller and running on a CR2450 coin cell reads punched paper tape — an 8-bit data pattern plus a clock track per hole row — through a bank of IR emitters and sensors, feeding a 25-LED "Semaphore panel" wired in five-person groups.

Feeding the badge the correct tape pattern unlocks a hidden "party mode" that lights up the whole panel; tymkrs seeded the trick by hiding a valid tape pattern in the conference program book, and also set up an on-site punching machine so attendees could cut their own tapes. After the AND!XOR team publicized the existence of the hidden mode on social media, one attendee (going by Gigawatts) built a standalone tape emulator from a TI Stellaris LaunchPad that fed the same signal pattern directly to the badge's IR sensors, letting them trigger party mode without physical tape.

No tymkrs project page, GitHub repository, or storefront listing was located in the sources reviewed, so pricing, quantity produced, and open-source design-file status remain unknown.
