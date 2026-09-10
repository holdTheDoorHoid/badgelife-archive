---
title: The BSides Indore Badge
id: other-bsides-indore-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2023
makers:
- name: Abhinav SP (Hackerware.io / HacksFromPanda)
  url: https://www.hackster.io/HacksFromPanda
summary: A double-sided blinky badge made for the inaugural BSides Indore, with a UV-printed robot on the front and a silkscreened spaceship on the back.
functions: 'No electronics interaction beyond a power switch: flipping it on lights the robot''s eye and alternately blinks "BSIDES" and "INDORE" text on the front artwork.'
look:
  colors:
  - black
  - red
  - blue
  shape: rectangle
  themes:
  - robot
  - space
  - security
tech:
  mcu: none
  leds:
    count: 26
    type: 1206 SMD
    note: 13 red and 13 blue 1206 SMD LEDs, driven by discrete transistor logic (no microcontroller).
  display: none
  connectivity: []
  battery: 2x CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of the inaugural BSides Indore conference in 2023.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.hackster.io/HacksFromPanda/the-bsides-indore-badge-08044e
  url: https://www.hackster.io/HacksFromPanda/the-bsides-indore-badge-08044e
  kind: article
images:
- file: assets/images/badges/other/bsides-indore-badge/50ea5873c5.jpg
  source: "https://www.hackster.io/HacksFromPanda/the-bsides-indore-badge-08044e"
  credit: "Abhinav SP (HacksFromPanda)"
  caption: "Front side of the BSides Indore badge with UV-printed robot artwork"
- file: assets/images/badges/other/bsides-indore-badge/7a4fb2aeaa.jpg
  source: "https://www.hackster.io/HacksFromPanda/the-bsides-indore-badge-08044e"
  credit: "Abhinav SP (HacksFromPanda)"
  caption: "Badge lit up, robot eye glowing and text blinking, powered by two CR2032 cells"
contact: {}
notes:
- Custom badge designed for the inaugural BSides Indore conference, commissioned by founder Aditya Rai. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task bsides-any.
- The sweep's title "BSides Indore Badge" is close to the maker's own title, "The BSides Indore Badge" (Hackster.io, published Nov 27, 2023); title updated to match.
- 'No entry for BSides Indore exists in _data/events.yml (searched for "indore" and "bsides"); event left as "other". The badge was made for the inaugural BSides Indore conference, India, 2023, per the maker''s Hackster.io writeup, commissioned by founder Aditya Rai.'
status: released
sources:
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-bsides-indore-badge-08044e
  title: BSides Indore Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides Indore''.'
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-bsides-indore-badge-08044e
  title: The BSides Indore Badge - Hackster.io
  accessed: '2026-09-10'
  note: Maker's own project writeup; confirmed maker, event/year, artwork, BOM (13 red + 13 blue 1206 LEDs, 2x CR2032, BC547 transistors, no MCU), and behavior (glowing eye, blinking text).
- kind: url
  url: https://www.facebook.com/Hackerwares/posts/bsides-indore-gets-its-first-ever-badge-in-a-double-sided-artwork-front-in-uv-pr/734792088673353/
  title: 'Hackerwares Facebook post: BSides Indore gets its first-ever badge'
  accessed: '2026-09-10'
  note: Confirms double-sided artwork (UV-printed front, silkscreened back) and that it was the event's first-ever badge.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Maker's own Hackster.io project page confirms the badge exists and gives full BOM and behavior, so confidence is above low, but pricing, quantity made, and open-source status are not published anywhere found. No BSides Indore event id exists in events.yml, so event is left as "other"; this was made for BSides Indore, India, 2023.
last_modified_date: '2026-09-10'
---

Hackerware.io (Abhinav SP, publishing as HacksFromPanda) designed this badge at the request of Aditya Rai, founder of BSides Indore, for the conference's inaugural 2023 edition. The badge is a double-sided PCB: the front carries a UV-printed robot design, while the back is silkscreened with a spaceship. It was the first badge BSides Indore ever had.

There's no microcontroller on board. A slide switch and two CR2032 coin cells feed a small discrete circuit — 13 red and 13 blue 1206 SMD LEDs driven through BC547 transistors — that lights the robot's eye and alternates blinking "BSIDES" and "INDORE" text on the front artwork when powered on.

No pricing, production quantity, or design-file release could be confirmed from available sources; the maker's writeup covers only the design story and bill of materials.
