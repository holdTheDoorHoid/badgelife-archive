---
title: BSidesJAX 2024 Hydra Badge Challenge
id: other-bsidesjax-2024-badge-challenge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2024
makers:
- name: blackandwhitehat
  url: https://github.com/blackandwhitehat
summary: 'A learn-to-solder conference badge for BSides Jacksonville 2024 (the event''s 10th year), shaped like a multi-headed hydra, built around a soldering-village CTF where finishing the circuits unlocks flags.'
functions: 'Attendee badge assembled at the Soldering Village: Circuit 1 is through-hole (2 user-chosen-color LEDs, a switch, a battery holder/battery, and an SAO header) and, once soldered and demonstrated to a volunteer, yields the CTF''s first flag. Circuit 2 adds SMD components (split into LF and HF sections) for an advanced/volunteer track. The first flag unlocks a 10-flag online CTF (soldering skills, BSides history, hacker trivia, puzzles/ciphers) hosted on CTFd, with a black badge and lifetime entry for 1st place and Meshtastic radios for 2nd/3rd.'
look:
  colors:
  - blue
  - gold
  shape: null
  themes:
  - fantasy
  - learn to solder
  - ctf
  - puzzle
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 'User picks the color of both LEDs from what is provided; through-hole, hand-soldered as part of Circuit 1.'
  display: none
  connectivity: []
  battery: coin cell (battery + holder provided in the kit)
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Distributed to attendees at BSides Jacksonville 2024 as the conference badge, assembled by hand at the on-site Soldering Village.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/blackandwhitehat/BSidesJAX_2024_Badge_Challenge
  url: https://github.com/blackandwhitehat/BSidesJAX_2024_Badge_Challenge
  kind: repo
- label: github.com/blackandwhitehat/BSidesJAX_2024_Badge (assembly instructions)
  url: https://github.com/blackandwhitehat/BSidesJAX_2024_Badge
  kind: repo
- label: 'BSides Jacksonville Hydra Badge Assembly (YouTube)'
  url: https://www.youtube.com/watch?v=xDVRaMgNc40
  kind: video
- label: 'CTFd registration (hydra.ctfd.io)'
  url: https://hydra.ctfd.io/
  kind: doc
images:
  - file: assets/images/badges/other/bsidesjax-2024-badge-challenge/2df1bd6f87.jpg
    source: "https://www.youtube.com/watch?v=xDVRaMgNc40"
    credit: "blackandwhitehat"
    caption: "Still from the official BSides Jacksonville 2024 Hydra badge assembly video, showing the assembled hydra-head badge with 'ATTENDEE / BSides JAX / 10 Years 2014-2024' text"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/blackandwhitehat/BSidesJAX_2024_Badge_Challenge
  title: BSidesJAX 2024 Badge Challenge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''bsides-jacksonville-2024''.'
- kind: url
  url: https://raw.githubusercontent.com/blackandwhitehat/BSidesJAX_2024_Badge_Challenge/main/Readme.md
  title: 'Contest Information (BSidesJAX_2024_Badge_Challenge Readme)'
  accessed: '2026-09-07'
  note: 'CTF rules, flag format, registration link, prizes.'
- kind: url
  url: https://raw.githubusercontent.com/blackandwhitehat/BSidesJAX_2024_Badge/main/Readme.md
  title: 'Badge Assembly Video / Circuit 1 & 2 Assembly Instructions'
  accessed: '2026-09-07'
  note: 'Confirms this is a physical soldering-village badge with two circuits (through-hole + SMD), SAO header, LEDs, switch, battery, and calls it the "2024 Hydra Badge".'
- kind: url
  url: https://www.youtube.com/watch?v=xDVRaMgNc40
  title: 'BSides Jacksonville Hydra Badge Assembly'
  accessed: '2026-09-07'
  note: 'Video thumbnail shows the assembled badge: a blue-and-gold multi-headed hydra/dragon PCB with "ATTENDEE / BSides JAX / 10 Years 2014-2024" silkscreen; used as the entry image.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No matching event id exists in events.yml for "BSides Jacksonville 2024" (only bsides-jacksonville-2018 and bsides-jacksonville-2023 are defined), so event is left as "other" pending a new event entry. No MCU is mentioned anywhere in either repo or the video description; the badge appears to be a passive board (2 LEDs, switch, battery, SAO header, plus SMD components on Circuit 2 whose exact parts are not named) rather than one with a microcontroller, so tech.mcu is set to "none" on that basis rather than left blank. Price, quantity made, and post-event availability are not stated anywhere found; the badge was given to attendees, not sold, so get_one.price/quantity/availability are left empty/unknown. Neither repo publishes Gerbers, schematics, or a BOM — only assembly instructions and a video — so make_your_own.open_source is "partial" with hardware_url/eda_tool left null.'
last_modified_date: '2026-09-07'
---

The BSidesJAX 2024 Hydra Badge Challenge was the conference badge for BSides Jacksonville's 10th year (2014-2024), made by the blackandwhitehat team and built around the Soldering Village rather than sold separately. The badge itself is shaped like a multi-headed hydra (or dragon) rendered in blue soldermask with gold circuit-trace artwork, with an open, tooth-lined mouth at the bottom and "ATTENDEE / BSides JAX" printed at the top.

Attendees assembled the badge by hand at the Soldering Village. Circuit 1 is a beginner-friendly through-hole build — two LEDs in a color of the solderer's choosing, a switch, a battery and holder, and an SAO header — and completing it and showing it to a volunteer unlocks the first flag of a 10-flag CTF (soldering skills, BSides history, hacker trivia, and puzzles/ciphers) run on CTFd under the code "HailHydra." An optional, harder Circuit 2 adds surface-mount components in low-frequency and high-frequency sections, aimed at more experienced solderers and volunteers; a companion 10-minute assembly video walked participants through both circuits. Prizes went to the top three CTF finishers: a black badge and lifetime conference entry for first place, and Meshtastic radios for second and third.

Neither of the two associated repositories (`BSidesJAX_2024_Badge_Challenge` for the CTF rules and `BSidesJAX_2024_Badge` for assembly instructions) publishes schematics, a bill of materials, or Gerber files, so build files beyond the instructions and video are not currently public.
