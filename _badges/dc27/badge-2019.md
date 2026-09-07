---
title: DEF CON 27 Badge (2019)
id: dc27-badge-2019
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Joe Grand (Grand Idea Studio)
  url: https://www.grandideastudio.com/
summary: The official DEF CON 27 attendee badge, a circular PCB topped with a polished natural quartz gemstone disc that doubles as an LED diffuser, communicating badge-to-badge over near-field magnetic induction instead of light or wires.
functions: Badges sense and communicate with each other wirelessly over NFMI (near-field magnetic induction) when held roughly two feet apart, triggering LED light patterns; serial pads on the board allow debugging and firmware interaction.
look:
  colors:
  - white
  - clear
  - multicolor
  shape: circle
  themes:
  - gem
tech:
  mcu: Kinetis KL27 (Arm Cortex-M0+)
  leds:
    count: 6
    type: reverse-mount
    note: Driven by a TI LP5569 LED driver; some badge variants use multicolor LEDs, others single-color.
  display: none
  connectivity:
  - nfc
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 26,500
  availability: unknown
  distribution:
  - purchase
  where: Distributed to attendees with DEF CON 27 registration; badge type (Human/general admission, Speaker, Press, Goon, Contest) determined the dye color of the quartz faceplate.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: media.defcon.org/DEF%20CON%2027/DEF%20CON%2027%20badge/DEFCON-27-Joe-Grand-Badge.pdf
  url: https://media.defcon.org/DEF%20CON%2027/DEF%20CON%2027%20badge/DEFCON-27-Joe-Grand-Badge.pdf
  kind: website
- label: 'Hackaday: First Look At DEF CON 27 Official Badge; Kingpin Is Back!'
  url: https://hackaday.com/2019/08/08/first-look-at-def-con-27-official-badge-kingpin-is-back/
  kind: article
  archived: https://web.archive.org/web/20260308104829/https://hackaday.com/2019/08/08/first-look-at-def-con-27-official-badge-kingpin-is-back/
- label: 'Hackaday: DEF CON 27 — The Badge Talk; Or That One Time Joe Grand Sourced 30,000 Gemstones'
  url: https://hackaday.com/2019/08/09/def-con-27-the-badge-talk-or-that-one-time-joe-grand-sourced-30000-gemstones/
  kind: article
  archived: https://web.archive.org/web/20260613222923/https://hackaday.com/2019/08/09/def-con-27-the-badge-talk-or-that-one-time-joe-grand-sourced-30000-gemstones/
- label: 'InfoconDB: Behind the Scenes of the DEF CON 27 Badge (talk)'
  url: https://infocondb.org/con/def-con/def-con-27/behind-the-scenes-of-the-def-con-27-badge
  kind: video
images:
- file: assets/images/badges/dc27/badge-2019/f80c4054dc.jpg
  source: https://hackaday.com/2019/08/08/first-look-at-def-con-27-official-badge-kingpin-is-back/
  credit: Hackaday / Joe Grand
  caption: The DEF CON 27 official badge with its polished quartz gemstone faceplate
  archived: https://web.archive.org/web/20260308104829/https://hackaday.com/2019/08/08/first-look-at-def-con-27-official-badge-kingpin-is-back/
- file: assets/images/badges/dc27/badge-2019/d831763eca.jpg
  source: https://hackaday.com/2019/08/08/first-look-at-def-con-27-official-badge-kingpin-is-back/
  credit: Hackaday / Joe Grand
  caption: Detail of the DEF CON 27 badge's Kinetis KL27 microcontroller and components
  archived: https://web.archive.org/web/20260308104829/https://hackaday.com/2019/08/08/first-look-at-def-con-27-official-badge-kingpin-is-back/
contact: {}
notes:
- Confirmed this session — official badge documentation PDF filename credits Joe Grand directly.
status: released
sources:
- kind: url
  url: https://media.defcon.org/DEF%20CON%2027/DEF%20CON%2027%20badge/DEFCON-27-Joe-Grand-Badge.pdf
  title: DEF CON 27 Badge (2019)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''DEF CON 27''.'
- kind: url
  url: https://hackaday.com/2019/08/08/first-look-at-def-con-27-official-badge-kingpin-is-back/
  title: First Look At DEF CON 27 Official Badge; Kingpin Is Back!
  accessed: '2026-09-07'
  note: Core specs — Kinetis KL27 MCU, LP5569 LED driver, NXH2261UK NFMI chip, 6 reverse-mount LEDs, quartz diffuser ~3in diameter, CR2032 power, 26,500 units at 99% yield, 7-day prototype-to-production turnaround.
  archived: https://web.archive.org/web/20260308104829/https://hackaday.com/2019/08/08/first-look-at-def-con-27-official-badge-kingpin-is-back/
- kind: url
  url: https://hackaday.com/2019/08/09/def-con-27-the-badge-talk-or-that-one-time-joe-grand-sourced-30000-gemstones/
  title: 'DEF CON 27: The Badge Talk; Or That One Time Joe Grand Sourced 30,000 Gemstones'
  accessed: '2026-09-07'
  note: Badge tiers (Human/general vs In-Human speaker/press/goon, dyed to match role) and quartz sourcing/processing story (mined in Brazil, cut and polished in China).
  archived: https://web.archive.org/web/20260613222923/https://hackaday.com/2019/08/09/def-con-27-the-badge-talk-or-that-one-time-joe-grand-sourced-30000-gemstones/
- kind: url
  url: https://infocondb.org/con/def-con/def-con-27/behind-the-scenes-of-the-def-con-27-badge
  title: Behind the Scenes of the DEF CON 27 Badge
  accessed: '2026-09-07'
  note: Talk description only, no new technical specifics beyond the Hackaday coverage.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price paid by attendees (if any beyond registration) and open-source status of hardware/firmware not found in the sources checked; left empty. Quantity figure varies slightly between sources (26,500 vs a rounded "28,500" mentioned in passing in one summary of the talk) — used the more specific 26,500 figure that appears alongside the "99% yield" claim in the primary Hackaday coverage.
last_modified_date: '2026-09-07'
---

The DEF CON 27 badge, designed by veteran badge maker Joe Grand ("Kingpin") of Grand Idea Studio, marked his return to badge design after a long absence. Rather than a traditional PCB-art badge, it centers on a polished disc of natural quartz — mined in Brazil and cut, shaped, and polished by a gem and jewelry company in China — mounted over the circuit board as both a decorative faceplate and an LED diffuser. Six reverse-mounted LEDs, driven by a TI LP5569 LED driver and controlled by a Kinetis KL27 (Arm Cortex-M0+) microcontroller, light the crystal from below.

Instead of the infrared or RF links used by many prior DEF CON badges, this one communicates badge-to-badge using near-field magnetic induction (NFMI) via an NXP NXH2261UK chip, sensing other badges within about two feet without needing to touch or align them. The badge runs off a single CR2032 coin cell. Badge type — general attendee ("Human"), speaker, press, or Goon staff — was distinguished by dyeing the quartz to a different color per role; contest badges were intended to be yellow but reportedly did not come out dyed correctly, making them scarce.

Grand detailed the badge's development in a DEF CON 27 talk, describing a compressed seven-day turnaround from alpha prototype to production, during which he wrote and verified all low-level drivers without first testing intermediate board revisions. Roughly 26,500 badges were manufactured with a 99% yield by a US-based fab house.
