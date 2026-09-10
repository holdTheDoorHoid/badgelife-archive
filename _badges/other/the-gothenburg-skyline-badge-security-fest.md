---
title: The Gothenburg Skyline Badge | Security Fest
id: other-the-gothenburg-skyline-badge-security-fest
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2023
makers:
- name: Abhinav SP / Hackerware.io
summary: A UV-printed, full-color CTF badge made for the Security Fest 2023 Hardware Village in Gothenburg, Sweden, styled as the city's skyline with a cyberpunk twist.
functions: 'Serial-console CTF: attendees connect over the badge''s Micro-USB port (9600 baud) and work through eight cryptography puzzles. Attendees also solder their own choice of LEDs to the board in a soldering-village workshop to complete the badge''s look.'
look:
  colors: []
  shape: rectangle
  themes:
  - cyberpunk
  - security
  - ctf
  - learn to solder
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Handed out at the Security Fest 2023 Hardware Village in Gothenburg, Sweden; assembled (LEDs soldered on) by attendees at an on-site soldering village.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.hackster.io/HacksFromPanda/the-gothenburg-skyline-badge-security-fest-eed557
  url: https://www.hackster.io/HacksFromPanda/the-gothenburg-skyline-badge-security-fest-eed557
  kind: website
- label: Hackerware.io - Security Fest badge page
  url: https://hackerwares.in/secfest
  kind: website
images:
- file: assets/images/badges/other/the-gothenburg-skyline-badge-security-fest/7424e4e8d3.jpg
  source: "https://hackerwares.in/secfest"
  credit: "Hackerware.io"
  caption: "The Gothenburg Skyline Badge, UV-printed with cyberpunk skyline design"
contact: {}
notes:
- "Sweep's sources list gave the title as 'The Gothenburg Skyline Badge | Security Fest'; maker's own site calls it the 'Gothenburg Cyberpunk CTF Badge'. Kept the sweep's title since it matches the Hackster.io project title verbatim."
- 'Made for Security Fest 2023 in Gothenburg, Sweden. No matching event id exists in _data/events.yml (only Security Fest years present, if any, would need checking); left event as "other" per instructions.'
- 'MCU, LED count/type, and pricing/quantity are not stated on either the maker''s own page (hackerwares.in/secfest) or the badge.gallery mirror; the primary Hackster.io writeup (hackster.io/HacksFromPanda/...) could not be fetched directly (Cloudflare-blocked) so some detail may exist there that was not captured.'
status: released
sources:
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-gothenburg-skyline-badge-security-fest-eed557
  title: The Gothenburg Skyline Badge | Security Fest
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://hackerwares.in/secfest
  title: Welcome To Hackerware - Security Fest badge page
  accessed: '2026-09-10'
  note: "Maker's own page; confirmed maker, event, UV printing, cyberpunk/skyline theme, soldering + CTF workshop, and badge photo."
- kind: url
  url: https://badge.gallery/issues/security-fest-2023-gothenburg-skyline-badge/hands-on-assembly-dependency
  title: 'Security Fest 2023 Gothenburg Skyline Badge - badge.gallery'
  accessed: '2026-09-10'
  note: Third-party mirror/summary corroborating maker attribution (HacksFromPanda/Hackerware), Micro-USB CTF interface, 9600 baud serial, and 8 crypto puzzles.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed real and released via the maker''s own site (hackerwares.in/secfest) and a third-party mirror; the primary Hackster.io project page returned a Cloudflare block on both WebFetch and curl, so it could not be read directly. No MCU, LED, price, or quantity details were found on the sources that were reachable. No open-source hardware/firmware links were found.'
last_modified_date: '2026-09-10'
---

The Gothenburg Skyline Badge (also called the "Gothenburg Cyberpunk CTF Badge" on the maker's own site) was made by Abhinav SP of Hackerware.io for the Hardware Village at Security Fest 2023 in Gothenburg, Sweden. It followed an earlier Security Fest badge inspired by Gothenburg's trams, and this one carries a full-color, UV-printed board art depicting the city's skyline reimagined in a cyberpunk style.

The badge doubled as a hands-on workshop piece and a CTF: attendees soldered their own choice of LEDs onto the board at an on-site soldering village to finish its look, then plugged into its Micro-USB port and used a 9600-baud serial console to work through a set of eight cryptography puzzles.

Details on the exact microcontroller, LED type/count, production quantity, and price were not found on the sources reachable during this pass (the maker's own page and a third-party mirror); the original Hackster.io project writeup, which likely has fuller build details, could not be fetched due to a Cloudflare block.
