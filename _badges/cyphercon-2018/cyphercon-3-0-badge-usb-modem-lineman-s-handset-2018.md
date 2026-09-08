---
title: CypherCon 3.0 Badge (USB Modem / Lineman's Handset, 2018)
id: cyphercon-2018-cyphercon-3-0-badge-usb-modem-lineman-s-handset-2018
layout: badge
parent: CypherCon 3.0
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2018
year: 2018
makers:
- name: TYMKRS
  url: https://www.reddit.com/r/Tymkrs/
summary: The official CypherCon 3.0 (2018) attendee badge, shaped like a lineman's telephone handset and built to work as a real USB modem, tying into the con's "Retro Futuristic Telephreak" theme.
functions: 'Runs TBAS, a minimalist "Turing tarpit" interpreter language with single-character operators, continuously in the background. Includes a wardialer app (AUTODT) that scans a phone network for carriers and logs each detected number, a dialpad/speakerphone mode, a BLINKEN app for programmable RGB particle animations, and a tone generator that plays musical notes plus telephony tones (DTMF, trunk signals, special information tones). Connects over USB as a serial modem and was used with a 96-line telephone exchange built for the con, populated with a BBS, a ticker sign, and previous years'' badges.'
look:
  colors:
  - white
  - black
  - red
  - blue
  - purple
  - gold
  shape: null
  themes:
  - retro computer
  - hardware tool
  - puzzle
tech:
  mcu: null
  leds:
    count: null
    type: RGB
    note: Programmable particle-animation effects via the on-badge BLINKEN app.
  display: 7-segment
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of CypherCon 3.0 (Wisconsin Center, April 12-13, 2018) as the conference badge.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Wireb/badge_bus/wiki
  eda_tool: null
links:
- label: www.reddit.com/r/Tymkrs/comments/8cd16o/cyphercon_badge_2018_cyphercon_30
  url: https://www.reddit.com/r/Tymkrs/comments/8cd16o/cyphercon_badge_2018_cyphercon_30/
  kind: social
- label: CypherCon Badge 3.0 Documentation
  url: https://hackthebadge.com/cyphercon-badge-3-0-documentation/
  kind: doc
- label: 2018 CypherCon 3.0 Badge - Special Message from the TYMKRS
  url: https://hackthebadge.com/2018-cyphercon-3-0-badge-special-message-from-the-tymkrs/
  kind: article
- label: CypherCon 3.0 - CONFONE Electronic Badge (video)
  url: https://www.youtube.com/watch?v=fgYan7oo2kU
  kind: video
- label: 'CypherCon 3.0 - CypherCon.com'
  url: https://cyphercon.com/cyphercon-3-0/
  kind: website
- label: badge_bus wiki (TBAS interpreter source repo)
  url: https://github.com/Wireb/badge_bus/wiki
  kind: repo
images:
- file: assets/images/badges/cyphercon-2018/cyphercon-3-0-badge-usb-modem-lineman-s-handset-2018/f7b8852da1.jpg
  source: "https://www.youtube.com/watch?v=fgYan7oo2kU"
  credit: "TYMKRS"
  caption: "CypherCon 3.0 badge demo video thumbnail, showing the handset-shaped badge in several colorways plus the full lineman's-handset form"
contact: {}
notes:
- Official CypherCon 2018 badge combining a USB modem and lineman's telephone handset, paired with a 96-line telephone exchange installation at the con; runs a Turing-tarpit language called TBAS. Found by the event-year sweep, task cyphercon.
- 'Sweep-found title kept as-is; TYMKRS and press call it the "CONFONE" or "CypherCon Badge 3.0" rather than using this exact phrasing, but no single canonical title was found on TYMKRS''s own pages.'
status: released
sources:
- kind: url
  url: https://www.reddit.com/r/Tymkrs/comments/8cd16o/cyphercon_badge_2018_cyphercon_30/
  title: CypherCon 3.0 Badge (USB Modem / Lineman's Handset, 2018)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:cyphercon); event read as ''cyphercon-2018''.'
- kind: url
  url: https://hackthebadge.com/cyphercon-badge-3-0-documentation/
  title: CypherCon Badge 3.0 Documentation
  accessed: '2026-09-08'
  note: TYMKRS's own documentation - confirms TBAS interpreter, wardialer/AUTODT app, BLINKEN app, 7-segment display, speaker/tone generator, USB serial connection, and links the badge_bus firmware repo.
- kind: url
  url: https://hackthebadge.com/2018-cyphercon-3-0-badge-special-message-from-the-tymkrs/
  title: 2018 CypherCon 3.0 Badge - Special Message from the TYMKRS
  accessed: '2026-09-08'
  note: Describes the TBAS "Turing tarpit" language and its single-character operators.
- kind: url
  url: https://www.youtube.com/watch?v=fgYan7oo2kU
  title: Cyphercon 2018 - CONFONE Electronic Badge
  accessed: '2026-09-08'
  note: TYMKRS video confirming the badge is a USB modem / lineman's phone, shows multiple badge colorways and the telephone exchange; source of the saved photo.
- kind: url
  url: https://cyphercon.com/cyphercon-3-0/
  title: CypherCon 3.0 - CypherCon
  accessed: '2026-09-08'
  note: 'Confirms event dates (April 12-13, 2018), venue (Wisconsin Center, 745 attendees), and theme ("Retro Futuristic Telephreak").'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Chip/MCU model, battery/power details, price, and total quantity made were not stated on any source checked and are left empty. TYMKRS's own documentation and video, plus the con's own event page, confirm the badge exists, its event/year, and its functions, so confidence is high despite the missing spec fields. Hardware design files (schematic/Gerbers) were not found; only the badge_bus firmware repo (TBAS interpreter) was located, so open_source is marked partial.
last_modified_date: '2026-09-08'
---

The CypherCon 3.0 badge (2018) is TYMKRS's take on the con's "Retro Futuristic Telephreak" theme: a working attendee badge shaped like an old lineman's test handset, doubling as a functional USB modem. Attendees could plug it into a computer as a serial modem, dial into the venue's phone lines, and use its 7-segment display, dialpad, and internal speaker/tone generator for handset-style interaction, all while the badge continuously ran TBAS, a deliberately minimal "Turing tarpit" scripting language built around single-character operators.

To give the badge somewhere to dial, TYMKRS built and installed a 96-line telephone exchange at the conference, populated with toys such as a BBS, a ticker sign, and working examples of previous years' CypherCon badges. A built-in wardialer app (AUTODT) let badge holders scan the exchange for carriers, logging each number it found, while a separate BLINKEN app drove programmable RGB particle-animation effects on the badge's lighting.

TYMKRS published behavioral documentation and the TBAS/firmware source (via the `badge_bus` repository) for the badge, but no schematic, Gerbers, or BOM were found, and neither the MCU, battery, nor original price/quantity are stated in any source located during this pass.
