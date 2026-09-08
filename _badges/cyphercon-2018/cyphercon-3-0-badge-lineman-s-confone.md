---
title: CypherCon 3.0 Badge (Lineman's CONFONE)
id: cyphercon-2018-cyphercon-3-0-badge-lineman-s-confone
layout: badge
parent: CypherCon 3.0
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2018
year: 2018
makers:
- name: Tymkrs
summary: 'A pocket USB modem and lineman''s telephone handset badge for CypherCon 3.0, built for the "Retro Futuristic Telephreak" theme. It dials and answers real phone calls, runs a scanner for other badges on the conference''s phone network, and hosts an onboard esoteric-language interpreter.'
functions: 'AUTODT: automatic sequential-range dialing with carrier-detection logging. BLINKEN: RGB LED animation controller (up to four programmable particles/waveforms). CONFIG: settings for modem passthrough, ringtones, LED themes, and display messages. DIALER: voice calling/answering with speakerphone. SCROLLER: 7-segment scrolling text/message editor. TBAS: an onboard esoteric programming language interpreter (logic, arithmetic, I/O, app execution), edited via TBASED (touchpad) or TBASCL (command line). TONEGN: tone generator for musical notes, 3-channel polyphonic audio, and telephony tones.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - hardware tool
  - radio
tech:
  mcu: null
  leds:
    count: null
    type: RGB
    note: Programmable brightness layers; up to four particles/waveforms via the BLINKEN app.
  display: 7-segment display
  connectivity:
  - usb
  - uart
  battery: rechargeable battery
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Conference badge for CypherCon 3.0 (2018) attendees; distribution details not published.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Wireb/badge_bus/wiki
  eda_tool: null
links:
- label: cyphercon.com/history
  url: https://cyphercon.com/history/
  kind: website
- label: 'Cyphercon 2018 - CONFONE Electronic Badge (YouTube)'
  url: 'https://www.youtube.com/watch?v=fgYan7oo2kU'
  kind: video
- label: 'CypherCon Badge 3.0 Documentation (Hack the Badge)'
  url: https://hackthebadge.com/cyphercon-badge-3-0-documentation/
  kind: doc
- label: 'CypherCon 3.0 (2018) Badge (Hack the Badge)'
  url: https://hackthebadge.com/cyphercon-3-0-badge-video/
  kind: website
- label: 'badge_bus wiki (GitHub, Wireb)'
  url: https://github.com/Wireb/badge_bus/wiki
  kind: repo
images: []
contact: {}
notes:
- 'Retro telephone-lineman-themed USB modem/phone badge for CypherCon 3.0 (2018), built around the "Retro Futuristic Telephreak" theme, made by Tymkrs; also demoed in a companion 96-line telephone exchange (YouTube: watch?v=fgYan7oo2kU). Found by the event-year sweep, task general-2016.'
- 'The sweep''s title "CypherCon 3.0 Badge (Lineman''s CONFONE)" matches Tymkrs'' own naming; kept as-is. This appears to duplicate entry cyphercon-2018-cyphercon-3-0-badge-usb-modem-lineman-s-handset-2018, which covers the same badge.'
status: released
sources:
- kind: url
  url: https://cyphercon.com/history/
  title: CypherCon 3.0 Badge (Lineman's CONFONE)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2016); event read as ''CypherCon 2018''.'
- kind: url
  url: https://hackthebadge.com/cyphercon-badge-3-0-documentation/
  title: CypherCon Badge 3.0 Documentation
  accessed: '2026-09-08'
  note: 'TYMKRS''s own documentation (posted April 10, 2018); source for functions, apps, display, LEDs, connectivity, battery, and firmware repo link.'
- kind: url
  url: https://hackthebadge.com/cyphercon-3-0-badge-video/
  title: CypherCon 3.0 (2018) Badge
  accessed: '2026-09-08'
  note: 'Confirms the badge as the 2018 CypherCon 3.0 conference badge; links the YouTube demo.'
- kind: url
  url: 'https://www.youtube.com/watch?v=fgYan7oo2kU'
  title: 'Cyphercon 2018 - CONFONE Electronic Badge'
  accessed: '2026-09-08'
  note: 'Search snippet confirms: "The Cyphercon 3.0 electronic badge is a usb modem and a lineman''s phone," built alongside a companion 96-line telephone exchange.'
- kind: url
  url: https://github.com/Wireb/badge_bus/wiki
  title: 'badge_bus wiki'
  accessed: '2026-09-08'
  note: 'Firmware/documentation repo linked from the Hack the Badge documentation page; not independently reviewed for hardware files.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, year, what it is, functions) confirmed via TYMKRS''s own Hack the Badge documentation and the CypherCon history page, so confidence is not higher only because MCU, exact price, quantity made, and availability were never published. No photo of the badge itself could be found in the time budgeted (only decorative theme-site images and an unrelated slide graphic turned up); the reddit.com/r/Tymkrs writeup could not be fetched (blocked). Likely duplicates cyphercon-2018-cyphercon-3-0-badge-usb-modem-lineman-s-handset-2018 (same event, same maker, same badge) — left both entries in place per instructions.'
last_modified_date: '2026-09-08'
---

TYMKRS built the CypherCon 3.0 (2018) attendee badge around that year's "Retro Futuristic Telephreak" theme: a pocket lineman's telephone handset that doubles as a USB modem. It can place and answer real voice calls, and it runs AUTODT, a war-dialer style scanner that sequentially dials phone numbers and logs which ones answer with a carrier tone — a nod to old-school phone phreaking. A 7-segment display and scrolling-text editor (SCROLLER) show status and messages, RGB LEDs run through a small particle-based animation engine (BLINKEN), and a tone generator (TONEGN) plays musical notes, telephony tones, and three-channel polyphonic audio.

Beyond telephony, the badge carries TBAS, an onboard esoteric programming language with its own touchpad and command-line editors, letting attendees write and run small programs directly on the badge. To give the phone functions somewhere to dial, Tymkrs also built a companion 96-line telephone exchange for the conference floor, populated with toys such as a BBS and a ticker sign, and reachable by badges dialing in.

No pricing, production quantity, or specific MCU details for the badge have been published; TYMKRS's own documentation and a linked firmware/documentation repository (badge_bus on GitHub) cover the feature set but not full hardware specifics.
---

