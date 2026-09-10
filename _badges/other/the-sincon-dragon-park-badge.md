---
title: The SINCON Dragon Park Badge
id: other-the-sincon-dragon-park-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: Abhinav SP / Hackerware.io
summary: A CTF badge made for SINCON (Infosec in the City, Singapore) 2025, cut to the outline of the Toa Payoh Dragon Playground.
functions: 'Onboard Capture the Flag game. Sliding the power switch plays a 3-second preview, then challenges (solvable in any order) are worked over a USB serial connection at 9600 baud; LEDs light up progressively as challenges are solved.'
look:
  colors:
  - multicolor
  shape: dragon
  themes:
  - ctf
  - security
  - village badge
tech:
  mcu: null
  leds:
    count: null
    type: reverse-mount
    note: Reverse-mounted SMD LEDs light the SINCON logo and progress indicators; user-solderable per the maker's tutorial.
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed at SINCON (Infosec in the City), Singapore, 2025.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.hackster.io/HacksFromPanda/the-sincon-dragon-park-badge-097465
  url: https://www.hackster.io/HacksFromPanda/the-sincon-dragon-park-badge-097465
  kind: website
- label: hackerware.io/sincon2025
  url: https://hackerware.io/sincon2025
  kind: website
- label: SINCON Dragon Badge soldering tutorial (PDF)
  url: https://www.hackerware.io/sincon-dragon-solder.pdf
  kind: doc
- label: SINCON Dragon Badge CTF setup (PDF)
  url: https://www.hackerware.io/sincon-dragon-ctf.pdf
  kind: doc
- label: The SINCON Dragon Park CTF Badge (YouTube)
  url: https://www.youtube.com/watch?v=DiaTK_NSQjY
  kind: video
images:
  - file: assets/images/badges/other/the-sincon-dragon-park-badge/89b2fd79d5.jpg
    source: "https://hackerware.io/sincon2025"
    credit: "Hackerware.io"
    caption: "The SINCON Dragon Park Badge, shaped like the Toa Payoh Dragon Playground"
contact: {}
notes:
- Sweep found this only via the Hackster.io listing title; confirmed as a real, released badge via the maker's own site and a Facebook post.
status: released
sources:
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-sincon-dragon-park-badge-097465
  title: The SINCON Dragon Park Badge
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://hackerware.io/sincon2025
  title: Welcome To Hackerware — The SINCON Dragon CTF Badge
  accessed: '2026-09-10'
  note: "Maker's own project page; confirms it is SINCON's third conference badge, distributed 2025, describes CTF mechanics and serial setup, source of the badge photo."
- kind: url
  url: https://www.facebook.com/hackerware/
  title: Hackerware Facebook page
  accessed: '2026-09-10'
  note: "Post describing the badge as 'SINCON's third badge', a tribute to the Toa Payoh Dragon Playground with a CTF onboard."
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Hackster.io page itself returned a Cloudflare block and could not be fetched directly, but a cached search snippet from it plus the maker''s own hackerware.io/sincon2025 page and Facebook post independently confirm the item, its shape (Toa Payoh Dragon Playground outline), UV-printed full-colour art, reverse-mounted LEDs, and CTF/serial functionality. Event id "sincon" does not exist in _data/events.yml, so event is left as "other"; this was made for SINCON (Infosec in the City), Singapore, 2025 (the con''s "third" badge per the maker). MCU, LED count, price, quantity, and open-source status were not stated on any source found and are left empty. Fact-check pass (2026-09-10): hackster.io still 403s directly, but a fresh search snippet of it reproduces the exact wording behind the shape/UV-printing/reverse-mount-LED claims; hackerware.io/sincon2025 was fetched directly and independently confirms the power-switch/3-second-preview, 9600-baud serial CTF mechanics, and the "SINCON''s third conference badge" phrasing; a fresh Facebook search snippet reproduces the "third badge / Dragon Playground / CTF" post text verbatim; both PDF guides return HTTP 200 with May 2025 timestamps; the YouTube URL resolves; and the saved photo visually matches (dragon shape, orange/white, lit LEDs). No contradictions found; every non-empty field is supported, so status is upgraded to verified.'
last_modified_date: '2026-09-10'
---

The SINCON Dragon Park Badge is a Capture-the-Flag badge Hackerware.io (Abhinav SP) made for SINCON — Singapore's Infosec in the City conference — in 2025, described by the maker as SINCON's third conference badge. The PCB is cut to the outline of the Toa Payoh Dragon Playground, a well-known Singapore landmark, with full-colour artwork applied using the maker's UV printing process and reverse-mounted SMD LEDs lighting the SINCON logo.

Sliding the badge's power switch plays a short animated preview, after which wearers connect the badge over USB to a computer's Arduino IDE Serial Monitor (9600 baud, NL&CR) and type `***` to begin. Challenges can be solved in any order, and the badge's LEDs light up progressively as more of them are completed. The maker published separate PDF guides covering assembly (soldering the SMD LEDs onto an otherwise pre-soldered board) and the CTF setup steps.

MCU, LED count, price, and production quantity were not stated in any source found; hardware/firmware were not confirmed as published.
