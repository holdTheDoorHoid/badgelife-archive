---
title: ShmooCon 2024 NFC Medallion Badge
id: shmoocon-2024-shmoocon-2024-nfc-medallion-badge
layout: badge
parent: ShmooCon 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: shmoocon-2024
year: 2024
makers:
- name: ShmooCon
summary: 'A reusable metal-style medallion issued as the ShmooCon 2024 badge, embedding multiple NFC tags used as the physical key to that year''s "Shmooganography" puzzle track.'
functions: 'Carries at least three separate NFC tags (one confirmed NTAG215) each storing an NDEF text record; scanning the tags and combining their payloads pointed solvers to real-world locations as part of the "Chrononaut"/Shmooganography scavenger hunt run alongside the con.'
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - ctf
  - coin
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - nfc
  battery: null
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
- label: github.com/sakebomb/ctfs/blob/main/shmoocon/2024/writeup.md
  url: https://github.com/sakebomb/ctfs/blob/main/shmoocon/2024/writeup.md
  kind: repo
- label: shmooganography.org/Welcome
  url: https://shmooganography.org/Welcome
  kind: website
- label: 'github.com/sakebomb/ctfs/blob/main/shmoocon/2024/Shmooganography 24.md'
  url: https://github.com/sakebomb/ctfs/blob/main/shmoocon/2024/Shmooganography%2024.md
  kind: repo
images: []
contact: {}
notes:
- Official ShmooCon 2024 badge, a reusable medallion embedding three NFC tags (including an NTAG215 with an NDEF location record) that fed into the Shmooganography/Chrononaut puzzle track. Found by the event-year sweep, task shmoocon.
- 'research: the sweep''s source is a third-party CTF writeup (sakebomb/ctfs), not a maker page; no ShmooCon-official page or photo of the medallion was found. The writeup describes Tag 3 encoding "enmuseum" and Tag 1 encoding "en16/19364/24522", used together to route solvers to a museum location. It attributes the "Chrononaut" puzzle experience to the Battelle team, but that is the puzzle designer/runner, not necessarily who fabricated the physical medallion (kept maker as "ShmooCon" per the sheet since no other attribution surfaced). shmooganography.org/Welcome (linked in the entry) 404s as of this check. No chip, LED, display, price, quantity, or availability details were found anywhere, and no image of the medallion itself was located.'
status: listed
sources:
- kind: url
  url: https://github.com/sakebomb/ctfs/blob/main/shmoocon/2024/writeup.md
  title: ShmooCon 2024 NFC Medallion Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:shmoocon); event read as ''shmoocon-2024''.'
- kind: url
  url: https://github.com/sakebomb/ctfs/blob/main/shmoocon/2024/Shmooganography%2024.md
  title: 'Shmooganography 24 (sakebomb/ctfs writeup)'
  accessed: '2026-09-08'
  note: 'Confirms the medallion is used as the physical key ("Put your medallion to work") in the Shmooganography puzzle track; no maker, price, or physical-description details given.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): re-fetched both sakebomb/ctfs writeups directly. Both independently describe three NFC tags on the medallion, with the NTAG215 tag ("Front Top") decoding to "enmuseum" and another tag ("Back Bottom") carrying "en16/19364/24522" -- matches the entry''s summary, functions, and body text. Re-confirmed shmooganography.org/Welcome still 404s. A follow-up web search turned up no maker-official page, photo, or alternate source; all facts in the entry trace to the two cited sakebomb/ctfs pages. Confidence stays low since no maker source or image exists, but every non-empty field/sentence is now independently verified against source text. Left MCU, LEDs, display, price, quantity, and availability empty/unknown for lack of sourcing.'
last_modified_date: '2026-09-08'
---

The ShmooCon 2024 badge was a reusable medallion (rather than a powered electronic badge) built around multiple embedded NFC tags. At least three tags were present, one confirmed as an NTAG215, each carrying its own NDEF text record. The medallion served as the physical component of that year's "Shmooganography" puzzle track, part of the recurring "Chrononaut" experience Battelle ran alongside the conference: attendees scanned the tags with a phone and combined the decoded payloads (for example, one tag encoding a fragment read as "enmuseum" and another encoding coordinates-like text "en16/19364/24522") to work out a real-world location clue.

No maker's own page for the medallion was found — the shmooganography.org site linked from the community sheet now returns a 404 — so details on materials, manufacturer, production quantity, and distribution could not be confirmed. It is treated here as an official ShmooCon 2024 badge per the original sheet entry, since ShmooCon has historically produced its own badges, but that attribution is not independently confirmed by a maker source.
