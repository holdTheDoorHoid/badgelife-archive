---
title: 614Con Badge
id: other-614con-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: syn-ack-zack / HTHackers
summary: A DIY Arduino badge kit sold to attendees of 614Con 2018, an information-security conference in Columbus, Ohio.
functions: Runs a custom Arduino sketch driving a color TFT screen and an RGB NeoPixel; assembled by the attendee from a parts kit with an SD card slot for extra assets.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - learn to solder
tech:
  mcu: ATmega328P (Arduino Nano)
  leds:
    count: 1
    type: NeoPixel 5050 RGB (integrated driver)
    note: ''
  display: 1.8in TFT LCD (ST7735S, 128x160)
  connectivity: []
  battery: 9V battery (clip + holder)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - kit
  where: 'Sold as a "badge kit" add-on to 614Con 2018 conference tickets; also buildable from the published parts list for anyone who attended without one.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HTHackers/614Con-Badge
  eda_tool: null
links:
- label: github.com/HTHackers/614Con-Badge
  url: https://github.com/HTHackers/614Con-Badge
  kind: repo
- label: github.com/syn-ack-zack/614Con-Badge (original)
  url: https://github.com/syn-ack-zack/614Con-Badge
  kind: repo
- label: 614Con - Info Security Calendar
  url: https://infosecuritycalendar.com/event/614con/
  kind: article
images:
- file: assets/images/badges/other/614con-badge/6966d8fc04.png
  source: "https://github.com/HTHackers/614Con-Badge"
  credit: "syn-ack-zack / HTHackers"
  caption: "Badge assembly diagram showing the Arduino Nano, 1.8in TFT, NeoPixel, and 9V battery layout"
contact: {}
notes:
- Arduino-based badge with a 1.8in TFT and NeoPixel, hosted in the same GitHub org as the Hackers Teaching Hackers badges; possibly a Columbus-area predecessor/sister event to HTH but the link and exact year were not confirmed. Found by the event-year sweep, task con-blue-team-con.
- 'Sweep title matched the maker''s own naming ("614Con Badge"); no correction needed.'
status: released
sources:
- kind: url
  url: https://github.com/HTHackers/614Con-Badge
  title: 614Con Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-blue-team-con); event read as ''614Con''.'
- kind: url
  url: https://raw.githubusercontent.com/HTHackers/614Con-Badge/master/README.md
  title: 614Con-Badge README (parts list and assembly)
  accessed: '2026-09-08'
  note: Part list confirms Arduino Nano (ATmega328P), 1.8in ST7735S TFT, NeoPixel 5050, 9V battery, SD card slot.
- kind: url
  url: https://github.com/syn-ack-zack/614Con-Badge
  title: syn-ack-zack/614Con-Badge (original repo)
  accessed: '2026-09-08'
  note: 'Original repo, created 2018-06-14 / last pushed 2018-06-19 -- dates the badge to 614Con 2018.'
- kind: url
  url: https://infosecuritycalendar.com/event/614con/
  title: 614Con - Info Security Calendar
  accessed: '2026-09-08'
  note: Confirms 614Con is an annual infosec conference in Columbus, Ohio, founded 2014; distinct from Hackers Teaching Hackers (HTH), run by an overlapping crew.
- kind: url
  url: https://www.youtube.com/watch?v=TD1SOdSFuUg
  title: 614Con 2018 - Magick Mick (YouTube, video description)
  accessed: '2026-09-08'
  note: 'Video description links "2018 Badge Kit: github.com/syn-ack-zack/614Con-Badge", confirming the badge is the 2018 614Con kit.'
- kind: url
  url: https://www.facebook.com/hackersteachinghackers/posts/if-you-attended-614con-but-didnt-get-a-badge-kit-no-worries-get-the-parts-list-b/1276426189155259/
  title: HTHackers Facebook post - badge kit parts list
  accessed: '2026-09-08'
  note: 'Confirms the badge was distributed as a paid "badge kit" add-on to 614Con tickets, with build-your-own instructions offered to attendees who skipped the kit.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, released badge: a self-assembly kit sold to attendees of 614Con 2018 (an annual Columbus, OH infosec conference, unrelated to DEF CON group DC614). No maker page states an exact unit count or per-kit price, so get_one.quantity/price and look.colors/shape are left empty. events.yml has no id for 614Con (it only lists Hackers Teaching Hackers, a related but separate Columbus event run by overlapping organizers), so event is left as "other" rather than guessed.'
last_modified_date: '2026-09-08'
---

The 614Con Badge is a self-assembly electronic badge sold as an optional kit to attendees of 614Con 2018, an annual information-security conference held in Columbus, Ohio (unrelated to the DEF CON group DC614, and a separate event from the same organizers' later Hackers Teaching Hackers conference). Builders sourced their own parts from a published bill of materials -- an Arduino Nano (ATmega328P), a 1.8" ST7735S TFT display, a NeoPixel 5050 RGB LED, a tactile button and slide switch, an SD card slot, and a 9V battery -- and assembled the board by hand following photographed instructions and an Arduino sketch (`614ConBadge.ino`) published by the con's organizer, syn-ack-zack. HTHackers, the group behind the later Hackers Teaching Hackers badges, later forked the repository into their own GitHub org, keeping the kit's build files available for anyone who wants to make one after the fact.

Badge kits were sold as an add-on to conference admission and reportedly sold out during the ticketing window, with organizers converting a few general-admission tickets to badge-kit tickets to meet demand; attendees who missed out were pointed to the public repo to source and build their own copy instead of buying a finished unit.

## Make your own

The GitHub repos (both the original by syn-ack-zack and the HTHackers fork) hold everything needed to build one: the parts list with example AliExpress/Amazon/Adafruit sourcing links, the Arduino libraries used, the bitmap assets shown on the TFT, the `614ConBadge.ino` sketch, and a photographed step-by-step assembly guide. No PCB or enclosure design files are included -- it is a point-to-point build on off-the-shelf modules rather than a custom PCB, so `make_your_own.open_source` is marked `partial` (firmware and BOM published, no board files) rather than `yes`.
