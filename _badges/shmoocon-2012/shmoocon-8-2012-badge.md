---
title: ShmooCon 8 (2012) Badge
id: shmoocon-2012-shmoocon-8-2012-badge
layout: badge
parent: ShmooCon 8 (2012)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: shmoocon-2012
year: 2012
makers:
- name: ShmooCon
summary: 'The attendee/speaker badge for ShmooCon 8 (January 2012), gear-shaped with letters printed around the teeth, that doubled as a physical puzzle piece for the annual badge contest.'
functions: 'Carries the yearly ShmooCon badge-puzzle contest: seven gear badges (one per attendee day/type) are put in order, combined with images in the program book, then walked through a transposition cipher, a physical gear-mesh step, a Vigenere cipher, and a keystream cipher to reach a final question.'
look:
  colors: []
  shape: gear
  themes:
  - puzzle
  - ctf
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: 'Given to attendees and speakers at ShmooCon 8 (Washington, DC, January 27-29, 2012) as their conference badge.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: dn.dashome.org/fun/2012/02/03/sc8-closing
  url: https://dn.dashome.org/fun/2012/02/03/sc8-closing/
  kind: website
- label: darthnull.org/media/2012/02/annotatedbadges.pdf
  url: https://darthnull.org/media/2012/02/annotatedbadges.pdf
  kind: doc
- label: darthnull.org/shmoocon-2012-badge-puzzle
  url: https://darthnull.org/shmoocon-2012-badge-puzzle/
  kind: article
images:
  - file: assets/images/badges/shmoocon-2012/shmoocon-8-2012-badge/c20bfb1a68.png
    source: "https://darthnull.org/shmoocon-2012-badge-puzzle/"
    credit: "David Schuetz (Darth Null)"
    caption: "ShmooCon 8 (2012) speaker badge, gear-shaped with letters around the teeth"
contact: {}
notes:
- Official ShmooCon 8 (2012) attendee/speaker badge. The sweep's notes described it as an "electronic" badge reverse-engineered from a disassembly, but the sources found describe a non-electronic gear-shaped card badge (letters around the teeth, a six-letter string and four-digit number printed on it) used as a physical puzzle piece; the "annotated disassembly" PDF is puzzle organizer David Schuetz's decode of the badge-contest cipher/program logic, not firmware for an onboard chip. No LEDs, MCU, or display are documented for this badge.
status: released
sources:
- kind: url
  url: https://dn.dashome.org/fun/2012/02/03/sc8-closing/
  title: ShmooCon 8 (2012) Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:shmoocon); event read as ''shmoocon-2012''.'
- kind: url
  url: https://darthnull.org/media/2012/02/annotatedbadges.pdf
  title: 'ShmooCon 8 Badge Contest - Badge Data / Disassembly'
  accessed: '2026-09-08'
  note: 'David Schuetz''s decode of the puzzle logic encoded in the badges (PDP-8-style opcode/punch notation), not device firmware; confirms the puzzle mechanism but not physical badge construction.'
- kind: url
  url: https://darthnull.org/shmoocon-2012-badge-puzzle/
  title: ShmooCon 2012 Badge Puzzle
  accessed: '2026-09-08'
  note: 'Maker/organizer write-up describing the badge as gear-shaped with letters in the teeth, a speaker vs attendee variant, and the four-stage puzzle (transposition cipher, gear mesh, Vigenere, keystream); source of the badge photo.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed this is a physical (non-electronic) gear-shaped puzzle badge, not the electronic PCB badge the sweep''s note implied - corrected tech fields to none/null and dropped the earlier "electronic" framing. Exact badge material (plastic vs. cardstock) and colors were not stated in any source found; left blank rather than guessed. No maker/designer credit beyond "ShmooCon" for the badge object itself was found (David Schuetz designed the puzzle content, not necessarily the physical badge).'
last_modified_date: '2026-09-08'
---

The ShmooCon 8 (2012) badge was the standard attendee and speaker credential for the January 2012 running of the Washington, DC hacker conference, in the year's chosen gear motif: a gear-shaped card with letters printed around the teeth, a six-letter string at the bottom, and a four-digit number at the top. Speaker and attendee versions differed slightly. It carried no electronics; instead, the printed markings were the raw material for that year's badge-puzzle contest.

The puzzle, designed by David Schuetz (Darth Null) working with the ShmooCon organizers and building on three prior years of badge puzzles by G. Mark Hardy, used seven of the gear badges together with images from the program book. Solvers ordered the badges by the founding dates of past ShmooCons, then worked through a four-stage chain - a transposition cipher, a step keyed by physically meshing the gears, a Vigenere cipher, and a final keystream cipher - to arrive at a closing question (answered "Volvo" by the winning team). Schuetz later published closing-ceremony slides walking through the solution and a from-source "disassembly" of the puzzle's internal logic, written up in PDP-8-style opcode notation, which is what the archive's discovery sweep had flagged as an "annotated disassembly" of the badge.
