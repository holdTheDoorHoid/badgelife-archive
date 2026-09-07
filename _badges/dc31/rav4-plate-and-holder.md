---
title: RAV4 Plate and Holder
id: dc31-rav4-plate-and-holder
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Mintynet
  url: https://www.mintynet.com
summary: A novelty UK-style number plate and plate holder sold at DEF CON 31 by
  automotive security researcher Ian Tabor (Mintynet), referencing his widely
  reported 2022 Toyota RAV4 theft via a CAN-injection attack on the headlight
  wiring.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $10 per part
  price_usd: 10.0
  quantity: ''
  availability: limited
  distribution:
  - purchase
  where: Sold in person at DEF CON 31; brought over from the UK in limited numbers.
    Three parts made up the complete set (badge, plate, and holder), $30 total.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: twitter.com/bigrinnyo/status/1684917558070124544?t=YGhsGs2MYx2CnjbYc8S9MA&s=19
  url: https://twitter.com/bigrinnyo/status/1684917558070124544?t=YGhsGs2MYx2CnjbYc8S9MA&s=19
  kind: social
- label: mintynet.com
  url: https://www.mintynet.com
  kind: website
- label: github.com/mintynet
  url: https://github.com/mintynet
  kind: repo
images: []
contact: {}
notes:
- These are in limited supply (they came in across the pond). There are three parts
  for the complete badge. So, $30 for the complete badge and plate.
status: listed
sources:
- kind: sheet
  event: dc31
  row: 60
  updated: ''
- kind: url
  url: https://www.mintynet.com
  title: 'mintynet.com - Ian Tabor''s site, "CAN Injection: keyless car theft"'
  accessed: '2026-09-07'
  note: Confirms Mintynet is Ian Tabor, a UK automotive cyber security consultant
    whose 2021 Toyota RAV4 was stolen in July 2022 via a CAN-injection attack
    through the headlight wiring (CVE-2023-29389, published April 2023 with Ken
    Tindell) - the likely backstory for a "RAV4 plate and holder" novelty sold at
    DEF CON 31's Car Hacking Village a few months later.
- kind: url
  url: https://github.com/mintynet
  title: mintynet (Ian Tabor) - GitHub
  accessed: '2026-09-07'
  note: Confirms identity (Ian Tabor, Crewe, UK, automotive cyber security / car
    hacking, blog mintynet.com) and CAN-bus-focused repos (esp32-slcan, nano-can,
    teensy-slcan).
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: The entry's only link (a tweet by @bigrinnyo) is inaccessible - the tweet
    returns "not found" via multiple fetch methods (direct, syndication API, and
    nitter mirrors, all of which are themselves offline), so it could not be read
    directly and no photo of the actual item was found. Identified "Mintynet" as
    Ian Tabor, a UK automotive security researcher known for CVE-2023-29389 (the
    CAN-injection theft of his own Toyota RAV4 in July 2022) via his GitHub profile
    and personal site; this fits a "RAV4 plate and holder" item well but no source
    directly describes the physical item itself (materials, whether it is
    electronic, exact dimensions, or images), so `type`, `tech`, and `look.shape`
    are left as originally imported rather than guessed. General web search was
    unavailable this session (search budget exhausted; DuckDuckGo/Bing/Google all
    blocked automated queries), which limited how far this could be corroborated.
last_modified_date: '2026-09-07'
---

Ian Tabor, a UK-based automotive cyber security consultant who goes by Mintynet online, had his 2021 Toyota RAV4 stolen in July 2022 using a "CAN injection" attack: thieves pried open a section of the front bumper near the headlight, exposed the CAN bus wiring, and injected fabricated messages that told the car's systems to unlock and start it. Tabor documented the theft and the technique on his blog, and it was later formally disclosed as CVE-2023-29389 in collaboration with researcher Ken Tindell in April 2023 - a story that got wide pickup in the car-hacking and infosec press.

The "RAV4 Plate and Holder" listed for DEF CON 31 (August 2023), a few months after that disclosure, appears to be Mintynet's own novelty take on the story: a UK-style number plate and plate holder sold as a three-part badge set for $10 per part ($30 complete), brought over from the UK in limited quantity. The linked tweet describing it could not be retrieved (it returns "not found," and the nitter mirrors that could have served as a fallback were unreachable), so the exact materials, dimensions, and whether any part is electronic remain unconfirmed - those fields are left blank rather than guessed.

If anyone reading this has a working link to the original post or a photo of the set, it would resolve the open questions noted above (particularly whether "badge" here means a PCB/SAO component or purely a plate-and-holder novelty).
