---
title: Wombat 3
id: bsides-adelaide-2026-wombat-3
layout: badge
parent: BSides Adelaide 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-adelaide-2026
year: 2026
makers:
- name: Hackerware.io
summary: A hardware CTF badge for BSides Adelaide 2026, the third in Hackerware's Wombat series, built around seven LED "subsystem" puzzles spelling out B/SIDES.
functions: Seven separate puzzle challenges (cold-boot ID, tangled comms, runic translation, and others) each resolve to a 10-bit binary code; entering the code on the badge's binary keys lights the matching LED. A CTF key arms flag-entry mode, a MODE key cycles LED blink patterns, and completing all seven challenges at the conference's hardware village unlocks a small UFO-shaped RGB add-on PCB that plugs into a spare 2-pin connector.
look:
  colors: []
  shape: null
  themes:
  - animal
  - ctf
  - puzzle
  - security
tech:
  mcu: null
  leds:
    count: 12
    type: discrete
    note: 1 LED "eye" plus 11 small LEDs (one per B/SIDES letter) hand-soldered by attendees at the hardware village.
  display: none
  connectivity:
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  - village
  where: 'Assembled/solved at the BSides Adelaide 2026 hardware village; most components come pre-soldered and attendees solder the LEDs themselves.'
make_your_own:
  open_source: partial
  hardware_url: https://hackerware.io/wombat3-gerber.zip
  firmware_url: null
  eda_tool: null
links:
- label: www.hackerware.io/wombat3
  url: https://www.hackerware.io/wombat3
  kind: website
- label: Hackerware Wombat badge page
  url: https://hackerware.io/wombat
  kind: website
- label: 'Soldering instructions (PDF)'
  url: https://hackerware.io/wombat3-soldering-instructions.pdf
  kind: doc
- label: Gerber files (zip)
  url: https://hackerware.io/wombat3-gerber.zip
  kind: fab
- label: 'BSides Adelaide 2026 Hardware Badge Writeup (semaja2.net)'
  url: https://semaja2.net/2026/07/29/bsides-adelaide-2026-badge-writeup-part-1/
  kind: article
images: []
contact: {}
notes:
- Third BSides Adelaide hardware CTF badge with an LED eye, push-button binary input puzzles, 7 challenges, and a bonus unlockable UFO RGB PCB attachment; gerbers published at hackerware.io/wombat3-gerber.zip. Found by the event-year sweep, task bsides-bsides-adelaide.
- 'Community-sheet wording matched the maker''s own title reasonably closely; the maker''s puzzle-console page brands it "WOMBAT CTF 3.0" / "WOMBAT3 CTF" but "Wombat 3" (used here) is consistent with that.'
status: listed
sources:
- kind: url
  url: https://www.hackerware.io/wombat3
  title: Wombat 3
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-adelaide); event read as ''BSides Adelaide 2026''.'
- kind: url
  url: https://www.hackerware.io/wombat3
  title: 'WOMBAT3 CTF // BSides Adelaide 2026 Badge'
  accessed: '2026-09-10'
  note: 'Maker''s interactive puzzle console for the badge; confirms maker, event/year, the 7 subsystem challenges, 10-bit binary code mechanic, CTF/MODE keys, and gerber file reference. No photo of the physical badge on this page (only a decorative SVG eye graphic).'
- kind: url
  url: https://semaja2.net/2026/07/29/bsides-adelaide-2026-badge-writeup-part-1/
  title: 'BSides Adelaide 2026 Hardware Badge Writeup'
  accessed: '2026-09-10'
  note: 'Attendee writeup confirming physical BOM (1 LED eye, 11 small LEDs to solder at the hardware village, 4 push buttons labelled CTF/MODE/1/0, a 2-pin connector, and a 4-pin +/-/T/R connector suggesting UART), and the UFO RGB bonus PCB unlocked by finishing all 7 challenges.'
- kind: url
  url: https://hackerware.io/wombat3-gerber.zip
  title: 'Wombat 3 gerber files'
  accessed: '2026-09-10'
  note: 'Confirmed the gerber zip is live (HTTP 200, application/zip) at the URL referenced on the badge console page.'
- kind: url
  url: https://hackerware.io/wombat
  title: 'Welcome To Hackerware'
  accessed: '2026-09-10'
  note: 'General Hackerware "Wombat Badge" landing page linking the soldering and CTF-interfacing PDFs; footer copyright reads 2024, so its photo (wombat.JPG) likely depicts an earlier badge in the series rather than the 2026 Wombat 3 specifically -- not used as an image for this entry for that reason.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Maker''s own console page and an independent attendee writeup both confirm the badge exists and describe matching mechanics, so this is more than a search-snippet sighting. However: no MCU/chip is named anywhere found, no price/quantity/availability (free vs. purchased vs. registration-bundled) is stated, PCB color/shape is not described, and no confirmed in-the-wild photo of the Wombat 3 board itself was found (the hackerware.io/wombat page photo is dated 2024 and probably shows an earlier Wombat badge, not this one, so it was not attached). A Facebook post ("The Wombat strikes again! ... comes with a gemstone eye") likely shows the real board but was not fetched (platform not reachable via the tools available this session).'
last_modified_date: '2026-09-10'
---

Wombat 3 is Hackerware's third hardware CTF badge for BSides Adelaide, following the original Wombat badge and 2025's FALKEN Wombat Badge 2. It ships mostly pre-assembled, with attendees hand-soldering eleven small LEDs (plus a larger LED "eye") at the conference's hardware village. Each LED corresponds to a letter in "B/SIDES" and lights up once its matching puzzle -- among them a cold-boot ID challenge, a scrambled comms intercept, and an Elder Futhark rune translation -- is solved and its 10-bit binary answer is entered on the badge's own buttons.

A dedicated CTF key arms flag-entry mode and a MODE key cycles the badge's LED blink patterns. Finishing all seven challenges at the hardware village unlocks a bonus: a small UFO-shaped RGB PCB that plugs into a previously-unused 2-pin connector on the board. A separate 4-pin connector labelled +, -, T, R points to an onboard UART, hinted by at least one attendee writeup to hide further undocumented functionality.

Hackerware published the gerber files for the badge (confirmed live as of this check) alongside a soldering-instructions PDF, but no firmware source, schematic, MCU part number, or pricing/quantity information was found on the maker's pages or in the attendee coverage reviewed.
