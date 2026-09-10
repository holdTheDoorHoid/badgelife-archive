---
title: bsidescpt2016badge
id: bsides-cape-town-2016-bsidescpt2016badge
layout: badge
parent: BSides Cape Town 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cape-town-2016
year: 2016
makers:
- name: Andrew Mohawk
  url: https://www.andrewmohawk.com/
- name: dodgymike (Mike Davis / @ElasticNinja)
  url: https://github.com/dodgymike
summary: An ESP8266-based conference badge built for BSides Cape Town 2016 that turns attendees into an "organic game" of faction conversion via infrared.
functions: Randomly assigns each attendee to one of three factions (red, green, blue) shown by an RGB LED; badges brought within ~45cm IR range trade level/faction data and can convert each other based on level and 50/50 chance when tied. Five LEDs show current level. Also displayed handles and conference programming, and unlocked extra games (Pong, Rock/Paper/Scissors/Lizard/Spock) and wireless network scanning as challenges were solved.
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - wearable
tech:
  mcu: ESP8266
  leds:
    count: 6
    type: discrete
    note: One RGB LED for faction color plus five single-color LEDs indicating player level.
  display: 128x64 OLED SPI display
  connectivity:
  - wifi
  - ir
  battery: 600 mAh LiPo with USB charging circuit
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to BSides Cape Town 2016 attendees; roughly 120 badges were active in the game at peak, 110 at the event's close.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/dodgymike/bsidescpt2016badge
  firmware_url: https://github.com/dodgymike/bsidescpt2016badge
  eda_tool: null
links:
- label: github.com/dodgymike/bsidescpt2016badge
  url: https://github.com/dodgymike/bsidescpt2016badge
  kind: repo
- label: BSides CPT Badge 2016 - Andrew Mohawk's
  url: https://www.andrewmohawk.com/2017/05/16/bsides-cpt-badge-2016/
  kind: article
  archived: https://web.archive.org/web/20260608081138/https://andrewmohawk.com/2017/05/16/bsides-cpt-badge-2016/
- label: Zombie Badges Take Over Security Con - Hackaday
  url: https://hackaday.com/2017/05/22/zombie-badges-take-over-security-con/
  kind: article
  archived: https://web.archive.org/web/20260514041816/https://hackaday.com/2017/05/22/zombie-badges-take-over-security-con/
- label: github.com/AndrewMohawk/BSidesBadge2016
  url: https://github.com/AndrewMohawk/BSidesBadge2016
  kind: repo
  archived: https://web.archive.org/web/20260907104447/https://github.com/AndrewMohawk/BSidesBadge2016
- label: BSides Cape Town 2016 Badge Walkthrough (YouTube)
  url: https://www.youtube.com/watch?v=w9I2ZdwkZjE
  kind: video
- label: BSides Cape Town 2016 Badge Game (YouTube)
  url: https://www.youtube.com/watch?v=dKPYCC3GlRQ
  kind: video
images:
- file: assets/images/badges/bsides-cape-town-2016/bsidescpt2016badge/7cf84b420f.jpg
  source: https://www.andrewmohawk.com/2017/05/16/bsides-cpt-badge-2016/
  credit: Andrew Mohawk
  caption: Finished BSides Cape Town 2016 badge
  archived: https://web.archive.org/web/20260608081138/https://andrewmohawk.com/2017/05/16/bsides-cpt-badge-2016/
- file: assets/images/badges/bsides-cape-town-2016/bsidescpt2016badge/bbcfbfa0d1.jpg
  source: https://www.andrewmohawk.com/2017/05/16/bsides-cpt-badge-2016/
  credit: Andrew Mohawk
  caption: BSides Cape Town 2016 badge PCB with silkscreen label
  archived: https://web.archive.org/web/20260608081138/https://andrewmohawk.com/2017/05/16/bsides-cpt-badge-2016/
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/dodgymike/bsidescpt2016badge
  title: bsidescpt2016badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''BSides Cape Town 2016 (no matching event id currently in events.yml)''.'
- kind: url
  url: https://www.andrewmohawk.com/2017/05/16/bsides-cpt-badge-2016/
  title: BSides CPT Badge 2016 - Andrew Mohawk's
  accessed: '2026-09-07'
  note: Maker's own write-up; source for MCU, display, LEDs, battery, IR range, game mechanics, and player counts; also source of both saved images.
  archived: https://web.archive.org/web/20260608081138/https://andrewmohawk.com/2017/05/16/bsides-cpt-badge-2016/
- kind: url
  url: https://hackaday.com/2017/05/22/zombie-badges-take-over-security-con/
  title: Zombie Badges Take Over Security Con
  accessed: '2026-09-07'
  note: Corroborates hardware specs and game mechanics; notes badge also displayed handles/programming and unlocked Pong and RPSLS as challenges.
  archived: https://web.archive.org/web/20260514041816/https://hackaday.com/2017/05/22/zombie-badges-take-over-security-con/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: GitHub repo (dodgymike/bsidescpt2016badge) has almost no README content of its own; the technical detail here comes from Andrew Mohawk's blog post, who co-designed the badge with dodgymike (Mike Davis, @ElasticNinja) with additional support credited to @shifttymike and @fluffyponyza. A separate repo, github.com/AndrewMohawk/BSidesBadge2016, holds Andrew Mohawk's copy of the badge code and is listed here as an additional source rather than a duplicate entry. Price/cost to attendees not stated anywhere found; badges were a free conference giveaway. Quantity manufactured not stated, only that ~120 were active in the game at peak.
last_modified_date: '2026-09-07'
model:
  file: assets/models/bsides-cape-town-2016/bsidescpt2016badge.glb
  method: kicad
  source_file: badge-dc24/_autosave-badge-bsides-v0.7.kicad_pcb
  generated: '2026-09-07'
  bytes: 272228
---

The BSides Cape Town 2016 badge was designed by Andrew Mohawk and Mike Davis (dodgymike, @ElasticNinja), with additional help credited to @shifttymike and @fluffyponyza, as a successor to Andrew Mohawk's earlier ZACon badges. Built around an ESP8266 with a 128x64 OLED SPI display, it ran on a 600 mAh LiPo charged over USB and had eight front-facing UI buttons plus a rear reset/programming button. An IR transmitter and receiver with roughly 45cm of range let nearby badges exchange data.

On badging in, each attendee's badge was randomly assigned to one of three factions (red, green, or blue), shown by an RGB LED, and started at level 1, shown on five level LEDs. Bringing two badges within IR range triggered a conversion check: the higher-level badge could flip a lower-level opponent to its faction, equal levels came down to a coin flip, and interactions within the same faction could raise loyalty or trigger defection. Beyond the core game, the badge showed attendee handles and conference schedule information, and solving on-badge challenges unlocked extra features including Pong, Rock/Paper/Scissors/Lizard/Spock, and wireless network scanning. By the organizers' own count, around 120 badges were active in the game at its peak and 110 remained by the event's end.

The linked GitHub repository (dodgymike/bsidescpt2016badge) contains the badge's board designs and server code but its README gives no further detail; the fuller account of the hardware and game design comes from Andrew Mohawk's own write-up, which also hosts a parallel copy of the firmware at github.com/AndrewMohawk/BSidesBadge2016.
