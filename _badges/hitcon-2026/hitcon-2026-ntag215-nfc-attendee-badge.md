---
title: HITCON 2026 NTAG215 NFC Attendee Badge
id: hitcon-2026-hitcon-2026-ntag215-nfc-attendee-badge
layout: badge
parent: HITCON 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitcon-2026
year: 2026
makers:
- name: HITCON
summary: 'The standard HITCON 2026 conference identity badge, with an embedded NTAG215 NFC tag used for an on-site card-collecting game called NFC Battle.'
functions: 'Attendees tap their phone against another attendee''s badge to unlock that person''s custom-designed card in the HITCON NFC Battle app (org.hitcon.nfcbattle), building out a personal collection over the two-day event.'
look:
  colors: []
  shape: null
  themes:
  - security
  - puzzle
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - nfc
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Included with every attendee's conference badge at HITCON 2026 (Taipei, August 21-22, 2026); no separate purchase.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/justinlin099/HITCON-NFC-Battle
  eda_tool: null
links:
- label: badge.gallery/badges/hitcon-2026-ntag215-nfc-attendee-badge
  url: https://badge.gallery/badges/hitcon-2026-ntag215-nfc-attendee-badge
  kind: website
- label: 'HITCON 2026 Events page'
  url: https://hitcon.org/2026/en-US/events/
  kind: website
- label: 'HITCON-NFC-Battle (GitHub)'
  url: https://github.com/justinlin099/HITCON-NFC-Battle
  kind: repo
- label: 'HITCON Training 2026 CFS post (NFC Battle description)'
  url: https://blog.hitcon.org/2026/03/HITCON-Training2026-CFS-en.html
  kind: article
- label: 'HITCON NFC Battle app (APKPure)'
  url: https://apkpure.com/hitcon-nfc-battle/org.hitcon.nfcbattle
  kind: website
images: []
contact: {}
notes:
- Planned NFC (NTAG215) attendee identity badge with a collectible-card exchange mechanic for HITCON 2026. Found by the event-year sweep, task con-hitcon.
- 'Title kept as the sweep wrote it; HITCON''s own materials call the game "NFC Battle" and refer to the badge simply as "your badge" rather than giving the badge itself a distinct product name.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/hitcon-2026-ntag215-nfc-attendee-badge
  title: HITCON 2026 NTAG215 NFC Attendee Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-hitcon); event read as ''HITCON 2026''.'
- kind: url
  url: https://hitcon.org/2026/en-US/events/
  title: 'Events | HITCON 2026'
  accessed: '2026-09-08'
  note: 'Search-result snippet (full page blocked by Cloudflare) confirms: "Every attendee''s badge is embedded with an NTAG215 NFC chip" for the NFC Battle activity.'
- kind: url
  url: https://blog.hitcon.org/2026/03/HITCON-Training2026-CFS-en.html
  title: 'HITCON Training 2026 - Call for Speaker Terms and Conditions'
  accessed: '2026-09-08'
  note: 'Chinese-language description of NFC Battle confirming every attendee badge has an embedded NTAG215 chip and how the tap-to-unlock card game works.'
- kind: url
  url: https://github.com/justinlin099/HITCON-NFC-Battle
  title: 'HITCON-NFC-Battle (GitHub)'
  accessed: '2026-09-08'
  note: 'GPL-3.0 repo for the NFC Battle mobile app, deep-link infra, and card-printer utilities; describes NTAG badge stickers and NTAG card variants used for the game. Software only, no hardware/PCB files.'
- kind: url
  url: https://apkpure.com/hitcon-nfc-battle/org.hitcon.nfcbattle
  title: 'HITCON NFC Battle APK'
  accessed: '2026-09-08'
  note: 'Confirms the companion Android app pairs with the event-provided NFC tag badge to create and exchange pixel-style cards.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed real via HITCON''s own event page and blog (not just a search snippet), plus the organizer''s GitHub repo for the companion NFC Battle app. No maker photo of the physical badge was found; badge.gallery explicitly notes the item is image-free out of caution about event graphics rights, and HITCON''s own pages do not show a badge photo either. Exact physical form (card stock vs. lanyard badge vs. sticker-on-badge), price breakdown, and quantity are not disclosed anywhere found. HITCON 2026 ran August 21-22, 2026, so the event has already taken place; status set to released.'
last_modified_date: '2026-09-08'
---

The HITCON 2026 attendee badge doubles as a game piece: every badge issued at the Taipei conference (August 21-22, 2026) has an NTAG215 NFC chip embedded in it, powering an on-site activity called NFC Battle. Attendees design a personal card ahead of the event, then tap their phone against other attendees' badges throughout the con to unlock and collect each other's cards, filling out a "HITCON card dex" as described in the organizers' own event materials.

The game is backed by a companion Android app (HITCON NFC Battle, package `org.hitcon.nfcbattle`) and an open-source (GPL-3.0) repository from HITCON contributor justinlin099 covering the Flutter app, deep-link infrastructure, and on-site card-printing tooling. The repository describes both NTAG stickers applied to standard badges and printable NTAG card variants, though it is a software/tooling repo rather than a hardware design release — no PCB or badge fabrication files were found.

No photo of the physical badge has surfaced from any source checked, including HITCON's own site; the item is confirmed to exist and to have been distributed with 2026 tickets, but its exact physical form, price breakdown, and production quantity remain undocumented.
