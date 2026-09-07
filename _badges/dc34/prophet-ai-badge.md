---
title: Prophet AI Badge
id: dc34-prophet-ai-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Abhinav Panda / Hackerware.io
  url: https://www.hackerware.io/
summary: A hand-built puzzle badge Hackerware.io made for Prophet AI, styled as a "temporal energy cell" with three cipher-locked LED sets unlocked through a CTF.
functions: Three separate locked puzzles; solvers decode ciphers printed on the lanyard, convert the answers to 7-bit binary keys, and tap each bit in on the badge while holding the CTF key to light each LED set in turn. A buzzer with an on/off switch gives audio feedback.
look:
  colors: [white, red, yellow]
  shape: rectangle
  themes: [sci-fi, ctf, puzzle]
tech:
  mcu: Nuvoton
  leds:
    count: null
    type: discrete
    note: Three red-and-yellow LED sets, each unlocked by solving one puzzle stage; count per set not stated.
  display: none
  connectivity: [audio]
  battery: 2x coin cell
  sao_version: none
get_one:
  price: Free Giveaways
  price_usd: 0.0
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: Listed on the community sheet as a free giveaway; the maker's pages do not say where or when it was handed out.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackerware.io/prophet-ai
  url: https://hackerware.io/prophet-ai
  kind: store
- label: x.com/TweetsFromPanda/status/2085867981016375706
  url: https://x.com/TweetsFromPanda/status/2085867981016375706
  kind: video
- label: Hackerware.io
  url: https://www.hackerware.io/
  kind: website
  archived: false
- label: 'Facebook: Prophet AI Badge announcement'
  url: https://www.facebook.com/Hackerware/posts/prophet-ai-badge-is-a-hand-built-temporal-energy-cellsolve-ctf-challenges-and-un/1461017809384107/
  kind: social
  archived: false
images:
- file: assets/images/badges/dc34/prophet-ai-badge/195725f59e.jpg
  source: "https://www.facebook.com/Hackerware/posts/prophet-ai-badge-is-a-hand-built-temporal-energy-cellsolve-ctf-challenges-and-un/1461017809384107/"
  credit: "Hackerware.io"
  caption: "Prophet AI Badge, a hand-built temporal energy cell badge"
contact:
  discord: abhinav_panda
  emails:
  - abhinav@hackerwares.in
  raw:
  - 'Twitter: TweetsFromPanda'
notes: []
status: announced
sources:
- kind: sheet
  event: dc34
  row: 63
  updated: 8/7/2026 18:19:26
  listing: New
- kind: url
  url: https://hackerware.io/prophet-ai
  title: Prophet AI Badge - Hackerware.io
  accessed: '2026-09-06'
  note: Maker's product page. Says the badge was designed for Prophet AI; describes it as a hand-built temporal energy cell; lists Nuvoton MCU, 2x coin cell, buzzer with on/off switch, cream 3D-printed hand-openable enclosure, three red/yellow LED sets unlocked via CTF puzzles using ciphers on the lanyard converted to 7-bit binary keys. Does not give event, date, price, quantity or open-source status.
- kind: url
  url: https://www.hackerware.io/
  title: Hackerware - #BadgeLife | Hardware Design, Security, & Research.
  accessed: '2026-09-06'
  note: Hackerware portfolio page; lists the Prophet AI Badge with the "temporal energy cell" blurb and links to the product page. Carries the abhinav@hackerwares.in contact.
- kind: url
  url: https://www.facebook.com/Hackerware/posts/prophet-ai-badge-is-a-hand-built-temporal-energy-cellsolve-ctf-challenges-and-un/1461017809384107/
  title: 'Hackerware Facebook: Prophet AI Badge announcement'
  accessed: '2026-09-06'
  note: Announcement post; only the title and preview image could be read without logging in. Source of the saved image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Verification pass 2026-09-06. The maker's product page and portfolio page confirm the badge, its hardware and the CTF mechanic; the product page says it was made for "Prophet AI" (not "Prophet Security" as an earlier draft said). No source read states which event it was handed out at, when, or where; the community sheet lists it under dc34 as a free giveaway, so event and availability follow the sheet. Status is "announced" rather than "released" because no source read shows people receiving it. The Facebook post body and date could not be read (login wall); the X link returns an error and could not be checked. Price beyond "free", quantity, LED count, exact Nuvoton part and open-source status are not stated by the maker.
last_modified_date: '2026-09-06'
---

The Prophet AI Badge is a hand-built puzzle badge by Hackerware.io (Abhinav Panda), made for Prophet AI and listed on the DEF CON 34 community badge sheet as a free giveaway. Styled as a "temporal energy cell," the badge runs on a Nuvoton microcontroller and two coin-cell batteries, with a buzzer (and a switch to silence it), housed in a cream 3D-printed enclosure that opens by hand.

Its hook is a layered CTF: three separate locked puzzles, each solved by decoding a cipher printed on the badge's lanyard, converting the answer into a 7-bit binary key, and tapping the bits in on the badge while holding the CTF key. A correct key lights one of the three red-and-yellow LED sets at once; a wrong one leaves it locked, playing on the theme of a device that "behaves like it's already seen tomorrow."

Where and when it was handed out, how many were made, and whether the hardware or firmware are published could not be confirmed from the maker's site or social posts.
