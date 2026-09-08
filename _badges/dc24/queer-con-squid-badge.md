---
title: Queercon 13 Badge (squid/cuttlefish badge)
id: dc24-queer-con-squid-badge
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc24
year: 2016
makers:
- name: Evan Mackay
- name: George Louthan
- name: Jonathan Nelson
- name: Jason Painter
summary: The 2016 Queercon badge (Queercon 13, at DEF CON 24) is a squid/cuttlefish-shaped
  PCB badge with a clear solder mask over black FR4 and curved, organic traces.
functions: Squid eyes made of 60 cyan LEDs display expressions; RGB LEDs light the
  tentacles in selectable patterns; an onboard 2.4 GHz radio lets badges "mate" with
  each other to learn patterns; a phototransistor auto-adjusts LED brightness.
look:
  colors:
  - black
  - clear
  shape: squid
  themes:
  - animal
  - sci-fi
tech:
  mcu: null
  leds:
    count: 60
    type: RGB
    note: 60 cyan LEDs form the eyes/expressions; RGB LEDs light the tentacles in selectable patterns.
  display: none
  connectivity:
  - radio
  battery: null
  sao_version: null
  sao_ports: 2
get_one:
  price: "$125"
  price_usd: 125
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold to Queercon attendees at DEF CON 24 (2016).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.vice.com/en/article/a-history-of-badgelife-def-cons-unlikely-obsession-with-artistic-circuit-boards
  url: https://www.vice.com/en/article/a-history-of-badgelife-def-cons-unlikely-obsession-with-artistic-circuit-boards/
  kind: website
- label: Hackaday - What We Learned From The 2016 Queercon Badge
  url: https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/
  kind: article
- label: "Hackaday.io - An oral history of the shitty add-on standard"
  url: https://hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  kind: article
images:
- file: assets/images/badges/dc24/queer-con-squid-badge/7c3839b874.jpg
  source: "https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/"
  credit: "Hackaday"
  caption: "The 2016 Queercon squid/cuttlefish badge"
contact: {}
notes:
- 'Original sweep note: "Squid-shaped village badge Evan Mackay designed for Queer
  Con at DEF CON 23, cited in Vice''s badgelife history as an early independent village
  badge. Found by the event-year sweep, task general-2006."'
status: released
sources:
- kind: url
  url: https://www.vice.com/en/article/a-history-of-badgelife-def-cons-unlikely-obsession-with-artistic-circuit-boards/
  title: Queer Con Squid Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2006); event read as ''dc23''.'
- kind: url
  url: https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/
  title: What We Learned From The 2016 Queercon Badge
  accessed: '2026-09-08'
  note: Confirms squid/cuttlefish shape, LED counts, radio, expansion ports, and names the four makers; dates the badge to 2016 (DEF CON 24), not 2015.
- kind: url
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  title: All The Unofficial Electronic Badges Of DEF CON (2015)
  accessed: '2026-09-08'
  note: Shows the actual DEF CON 23 (2015) Queercon badge ("Queercon 11") was a Tamagotchi-style pet badge, not a squid - confirming the Vice article's year is wrong.
- kind: url
  url: https://hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  title: An oral history of the shitty add-on standard
  accessed: '2026-09-08'
  note: Independently dates the squid/cuttlefish badge with hat expansion ports to "the 2016 Queercon badge."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'The Vice article that seeded this entry calls the squid badge "its 2015
    badge," but two independent sources (Hackaday''s contemporaneous 2015 DEF CON
    badge roundup, and Hackaday''s own 2016 Queercon badge writeup) show the actual
    DEF CON 23 (2015) Queercon badge was a Tamagotchi-style pet badge ("Queercon
    11"), while the squid/cuttlefish design with hat expansion ports is the 2016
    badge (Queercon 13, DEF CON 24). Corrected event from dc23 to dc24 and year from
    2015 to 2016 accordingly; retitled to match the maker-side "Queercon 13" naming
    used elsewhere in this archive. This is a duplicate of two existing entries for
    the same badge: queercon-2016-queercon-13-badge-2016-cephalopod-squid-badge and
    queercon-2016-queercon-13-badge-squid-cuttlefish-badge. MCU, battery, price beyond
    the $125 DEF CON 23-era Queercon price point, open-source status, and exact
    quantity made were not confirmed by sources checked.'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc23/queer-con-squid-badge/
---

The 2016 Queercon badge - the badge produced for Queercon 13, the LGBTQ+ village at DEF CON 24 - is shaped like a squid (also described as a cuttlefish), with a clear solder mask over black FR4 and smooth, organic curved traces. Its eyes are built from sixty cyan LEDs that can form different expressions, while RGB LEDs along the tentacles cycle through selectable light patterns. An onboard 2.4 GHz radio lets nearby badges "mate" and exchange patterns, and a phototransistor automatically adjusts LED brightness for the room. The badge was designed by Evan Mackay, George Louthan, Jonathan Nelson, and Jason Painter.

Two small expansion ports on the squid's head carried power, ground, and an I2C bus on a 1x4 connector, letting attendees plug in "hats" such as a light-up unicorn horn, an emo haircut, or an LED-studded top hat - one of several independent conference badge add-on schemes cited in the community's own history of what later became the standardized "shitty add-on" (SAO) connector.

This entry was originally filed under DEF CON 23 (2015) after a press retrospective (Vice's badgelife history) described the squid badge as "its 2015 badge." Checking Hackaday's own contemporaneous coverage shows that was a mistake on Vice's part: the actual 2015 Queercon badge ("Queercon 11") was a separate, Tamagotchi-style pet-raising badge, and the squid/cuttlefish design belongs to 2016 (Queercon 13, DEF CON 24) instead. It also duplicates two badges already cataloged in this archive under DEF CON 24.
