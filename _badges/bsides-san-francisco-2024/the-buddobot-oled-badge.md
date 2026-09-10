---
title: The Buddobot OLED Badge
id: bsides-san-francisco-2024-the-buddobot-oled-badge
layout: badge
parent: BSides San Francisco 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-san-francisco-2024
year: 2024
makers:
- name: Abhinav Pandagale / Hackerware.io
  url: https://www.hackerware.io/
summary: 'A CTF badge with an OLED display, made for the BSidesSF Hardware Challenge Village, that has the wearer answer prompts to be sorted onto the red or blue team.'
functions: 'A five-stage CTF played over a micro-USB serial connection (Arduino IDE serial monitor, 9600 baud): players send commands and flags to progress and unlock the badge''s lights.'
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - village badge
tech:
  mcu: null
  leds: null
  display: OLED
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
  - village
  where: Distributed at the BSidesSF Hardware Challenge Village, 2024.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.hackster.io/HacksFromPanda/the-buddobot-oled-badge-38be31
  url: https://www.hackster.io/HacksFromPanda/the-buddobot-oled-badge-38be31
  kind: website
- label: hackerware.io/buddo-oled
  url: https://www.hackerware.io/buddo-oled
  kind: website
images:
- file: assets/images/badges/bsides-san-francisco-2024/the-buddobot-oled-badge/b5c09bbe40.jpg
  source: "https://www.hackerware.io/buddo-oled"
  credit: "Hackerware.io"
  caption: "The Buddobot OLED Badge, a CTF badge with red/blue team selection"
contact: {}
notes:
- Sweep found the title via a Hackster.io listing, which is blocked by Cloudflare for automated fetches; confirmed instead via Hackerware's own project page and social posts about the BSidesSF Hardware Challenge Village.
- Not to be confused with "The Buddobot Badge" (dc31-buddo-badge), an earlier, non-OLED badge by the same maker for DEF CON 31.
status: released
sources:
- kind: url
  url: https://www.hackster.io/HacksFromPanda/the-buddobot-oled-badge-38be31
  title: The Buddobot OLED Badge
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://www.hackerware.io/buddo-oled
  title: Hardware Challenge Village OLED Badge
  accessed: '2026-09-10'
  note: Maker's own project page; confirms description, gameplay mechanics, USB/serial interaction, and event.
- kind: url
  url: https://www.linkedin.com/posts/hackerwares_the-buddobot-oled-badge-activity-7193339899226345473-elWa
  title: 'Hackerware LinkedIn post: The Buddobot OLED Badge'
  accessed: '2026-09-10'
  note: Confirms it was made for the BSidesSF Hardware Challenge Village and links the Hackster.io writeup.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Hackster.io project page (the fullest source, with likely MCU/LED/battery specs and a build story) is blocked by Cloudflare for automated fetches and could not be read. Maker''s own hackerware.io page and social posts confirm the badge is real and describe its CTF gameplay, but do not state MCU, LED count/type, battery, price, or quantity made, so those fields are left empty. Availability is unknown beyond having been distributed at the village in 2024.'
last_modified_date: '2026-09-10'
---

The Buddobot OLED Badge is a capture-the-flag badge built by Abhinav Pandagale of Hackerware.io for the BSidesSF Hardware Challenge Village in 2024. Wearers connect the badge over micro-USB and interact with it through the Arduino IDE serial monitor (9600 baud, both NL & CR), answering a series of five staged challenges; correct, lowercase flag submissions progress the game and ultimately sort the player onto the red or blue team while unlocking the badge's lights.

The badge is a follow-up to Hackerware's earlier, non-OLED "Buddobot Badge" made for DEF CON 31, this time adding an OLED display to the design. Hackerware published the full build story on Hackster.io, but that page returns a Cloudflare challenge to automated fetches, so details like the MCU, LED type/count, and battery could not be confirmed independently; readers can follow the Hackster.io link directly for that write-up.
