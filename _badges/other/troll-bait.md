---
title: Troll Bait
id: other-troll-bait
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: unknown
event: other
year: 0
makers: []
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/28179-troll-bait
  url: https://hackaday.io/project/28179-troll-bait
  kind: hackaday
images: []
contact: {}
notes: []
status: not_an_item
sources:
- kind: url
  url: https://hackaday.io/project/28179-troll-bait
  title: Troll Bait
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/28179-troll-bait
  title: Troll Bait
  accessed: '2026-09-07'
  note: 'Confirms this is a software/hardware hack layered on top of the Hackaday SuperCon 2017 CamBadge, not a standalone badge or SAO. Maker Scott Swaaley (scott-swaaley) used a Raspberry Pi 3 running Node.js/Express with the Aylien sentiment-analysis API to accept web-submitted text messages, flag negative ones as "troll" messages, and push them over UART to the SuperCon 2017 badge display. Repos: github.com/scottswaaley/trollBait-PI and github.com/scottswaaley/trollBait-BADGE.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This is a project/hack page, not a physical badge or SAO product: it describes a Raspberry Pi + sentiment-analysis add-on built to run alongside the official Hackaday SuperCon 2017 CamBadge, not a distinct piece of hardware distributed to attendees. No standalone badge exists to catalog here.'
last_modified_date: '2026-09-07'
---

Troll Bait was a companion hack for the Hackaday SuperCon 2017 CamBadge, built by Scott Swaaley (scott-swaaley). Rather than being a badge or SAO in its own right, it paired a Raspberry Pi 3 with the official SuperCon badge over UART: a small Node.js/Express web server accepted text messages submitted by attendees, ran them through the Aylien sentiment-analysis API, and pushed a "* * TROLL! * *" message with a red background to the badge display whenever a submission read as negative.

The project's source is split across two repositories, github.com/scottswaaley/trollBait-PI for the Raspberry Pi server and github.com/scottswaaley/trollBait-BADGE for the badge-side firmware (built with MPLAB X), both linked from the Hackaday.io project page along with downloadable project zips.

