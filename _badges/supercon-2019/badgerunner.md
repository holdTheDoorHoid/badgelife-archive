---
title: Badgerunner
id: supercon-2019-badgerunner
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2019
year: 2019
makers:
- name: Claire Sun
  url: https://hackaday.io/claire-sun
- name: Stephen Hawes
  url: https://github.com/sphawes
summary: A Blade Runner-themed badge for Hackaday Supercon 2019 shaped like the Tyrell Corporation's owl, with an ESP12 driving nine NeoPixels (eight on the front flashing a hidden message, one reversed to backlight the cybernetic eye), LiPo power with micro-USB charging, and an SAO header on each ear.
functions: 'Eight front-facing NeoPixels flash a secret message; a ninth NeoPixel is mounted reversed to backlight the owl''s cybernetic eye.'
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - cyberpunk
  - bird
  - security
tech:
  mcu: ESP12
  leds:
    count: 9
    type: NeoPixel
    note: Eight front-facing, one soldered reversed to backlight the eye
  display: null
  connectivity: []
  battery: LiPo, rechargeable via micro-USB
  sao_version: null
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold in person at Supercon 2019; remaining stock was planned to go up on Tindie afterward, but no Tindie listing could be confirmed.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/sphawes/badgerunner
  firmware_url: https://github.com/sphawes/badgerunner
  gerbers_url: null
  eda_tool: KiCad
  notes: Board artwork was laid out in Inkscape and exported with svg2shenzhen; schematics and board layout were done in KiCad. A separate companion repo (glowtie) holds a programmer.
links:
- label: github.com/sphawes/badgerunner
  url: https://github.com/sphawes/badgerunner
  kind: repo
- label: hackaday.io/project/168402-badge-runner
  url: https://hackaday.io/project/168402-badge-runner
  kind: hackaday
- label: github.com/sphawes/glowtie/tree/master/programmer
  url: https://github.com/sphawes/glowtie/tree/master/programmer
  kind: repo
images:
  - file: assets/images/badges/supercon-2019/badgerunner/0f6f672287.jpg
    source: "https://hackaday.io/project/168402-badge-runner"
    credit: "Claire Sun"
    caption: "Badge Runner PCB badge shaped like the Tyrell Corporation owl"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/sphawes/badgerunner
  title: Badgerunner - A Bladerunner-themed Conference Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/168402-badge-runner
  title: "BADGE RUNNER - Hackaday.io"
  accessed: '2026-09-07'
  note: Maker's own project writeup - origin story, event, ESP12/NeoPixel details, battery, SAO headers, and that it was sold at Supercon with leftover stock intended for Tindie.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Hackaday.io project page lists only Claire Sun as the creator; GitHub repo (hardware/firmware host) is owned by Stephen Hawes (sphawes), so both are credited as makers per the existing sheet entry. No price or production quantity could be confirmed from either source. Could not confirm whether the badge was ever actually listed on Tindie after Supercon. GitHub repo contains "art" and "pcb" folders (KiCad-based) but no explicit open-source license file was found, so make_your_own.open_source is marked "partial" rather than "yes".
last_modified_date: '2026-09-07'
---

The Badgerunner (formally "Badge Runner") is a Blade Runner-themed conference badge Claire Sun made for Hackaday Supercon 2019, shaped after the owl used by the Tyrell Corporation in the film. Sun was inspired after seeing #badgelife projects from DEF CON and picked the theme partly because Supercon that year was held near Los Angeles, around the time and place the original film is set. The board art was laid out in Inkscape and exported with svg2shenzhen, with schematics and board layout done in KiCad.

Electronically, the badge runs on an ESP12 driving nine NeoPixels: eight across the front flash a hidden message, and a ninth is soldered in reverse to backlight the owl's cybernetic eye from behind. It's powered by a rechargeable LiPo battery, chargeable over micro-USB, and each ear carries its own SAO header so two add-ons can be plugged in at once.

Sun made multiple badges to sell in person at Supercon 2019, with the plan to list any leftovers on Tindie afterward; no surviving Tindie listing was found to confirm that happened. Hardware and firmware are hosted on GitHub under Stephen Hawes's account (sphawes/badgerunner), with a companion programmer in a separate "glowtie" repo, though the repo carries no explicit open-source license.
