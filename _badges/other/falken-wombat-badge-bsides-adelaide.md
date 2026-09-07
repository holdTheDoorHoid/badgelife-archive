---
title: Falken Wombat Badge (BSides Adelaide)
id: other-falken-wombat-badge-bsides-adelaide
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2024
makers:
- name: Hackerware.io
  url: https://www.hackerware.io/
summary: A full-colour UV-printed CTF badge made for BSides Adelaide 2024, depicting the con's wombat mascot mid-transformation into a cyborg.
functions: 'Runs a CTF: a central RGB LED sits behind a torn "circuit" patch in the wombat''s eye, and six SMD LEDs on the badge each correspond to a separate challenge, lighting up as solvers find the correct flags. A Micro-USB port is used for interfacing during the CTF, with a coin cell battery and an on/off switch on the board.'
look:
  colors: [multicolor]
  shape: null
  themes: [animal, robot, ctf, security, learn to solder]
tech:
  mcu: null
  leds: null
  display: null
  connectivity: [usb]
  battery: coin cell
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: "Given to attendees of BSides Adelaide; the board arrives pre-soldered except for six SMD LEDs, which owners solder on themselves following the maker's tutorial before powering it with a coin cell."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.hackster.io/HacksFromPanda/the-falken-wombat-badge-bsides-adelaide-8c1db3
  url: https://www.hackster.io/HacksFromPanda/the-falken-wombat-badge-bsides-adelaide-8c1db3
  kind: article
- label: hackerware.io/wombat
  url: https://hackerware.io/wombat
  kind: website
- label: Wombat Badge soldering tutorial (PDF)
  url: https://hackerwares.in/wombat-soldering.pdf
  kind: doc
images:
  - file: assets/images/badges/other/falken-wombat-badge-bsides-adelaide/7c5703f2d3.jpg
    source: "https://hackerware.io/wombat"
    credit: "Hackerware.io"
    caption: "The Falken Wombat Badge, full-colour UV printed CTF badge for BSides Adelaide"
contact: {}
notes:
- 'Cyborg wombat design, full-colour UV printing, CTF.'
- 'The badge''s own silkscreen reads "FALKEN / The Combat Wombat / BSides Adelaide"; the maker''s page calls it "The BSides Adelaide Wombat Badge".'
- 'No "BSides Adelaide" event id exists in _data/events.yml, so event is left as "other" per the research guide; the con is BSides Adelaide.'
status: released
sources:
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-falken-wombat-badge-bsides-adelaide-8c1db3
  title: Falken Wombat Badge (BSides Adelaide)
  accessed: '2026-09-07'
  note: 'Never successfully loaded (Cloudflare 403 on every attempt, including a fresh check during fact-checking); kept only as a links reference, not used to support any field.'
- kind: url
  url: https://hackerware.io/wombat
  title: The BSides Adelaide Wombat Badge
  accessed: '2026-09-07'
  note: 'Maker''s own project page, fetched directly; confirms it is a full-colour UV printed CTF badge made by Hackerwares for BSides Adelaide; footer copyright reads "Hackerwares 2024"; source of the badge photo and of the linked soldering-tutorial PDF.'
- kind: url
  url: https://hackerwares.in/wombat-soldering.pdf
  title: The BSides Adelaide Wombat Badge - Soldering Tutorial
  accessed: '2026-09-07'
  note: 'Maker''s own tutorial PDF for this exact badge (board silkscreen reads "FALKEN The Combat Wombat BSides Adelaide"); confirms 6 SMD LED pads, a central RGB LED, a coin-cell battery holder, an on/off switch, and a micro-USB port, and that LEDs light up as the on-board CTF is progressed. Directly supports functions, tech.connectivity, tech.battery, and get_one.where.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): confirmed the core technical claims (6 SMD LEDs, central RGB LED, coin cell, micro-USB, CTF-by-serial mechanism) directly against the maker''s own soldering-tutorial PDF, which is specific to this badge. Removed a few things the previous pass had sourced only to hackster.io search-result summaries, since hackster.io remains inaccessible (Cloudflare 403) and was never actually read: the claim of a specific on-site "soldering village," and a note claiming a confirmed 2025 sequel badge (reworded as an unverified lead in this report''s other_items_found instead of stated as fact). Year (2024) is not stated explicitly by any source read; it is inferred from the copyright footer on the maker''s single-project page ("Hackerwares 2024") and is the best evidence available, but is not a direct statement of the event date. tech.mcu, tech.leds detail, tech.display, get_one.price/quantity, and make_your_own hardware/firmware links remain unstated by any source found and are left empty. A second PDF linked from the same page as a "CTF Tutorial" turned out to document a different badge (The Gothenburg Cyberpunk CTF Badge, Security Fest) and was not used as a source here; flagged separately below.'
last_modified_date: '2026-09-07'
---

The Falken Wombat Badge was made by Hackerware.io for BSides Adelaide. It reimagines the conference's wombat mascot as a cyborg, rendered across the PCB in full-colour UV printing, with a torn patch of "fur" revealing circuitry and a glowing RGB LED underneath. The badge doubles as a capture-the-flag challenge: six SMD LEDs each mark a separate CTF challenge and light up as solvers find the corresponding flags.

The board ships pre-assembled apart from those six LEDs, which owners solder on themselves following the maker's own tutorial, taking care to orient each LED's polarity correctly. Once soldered and powered from a coin cell, the badge is interfaced over its onboard micro-USB port to play the CTF, with a switch to power it on and off.
