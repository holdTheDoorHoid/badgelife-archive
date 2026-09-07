---
title: Badge Runner
id: supercon-2019-badge-runner
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2019
year: 2019
makers:
- name: Claire Sun
  url: https://hackaday.io/csun.codes
summary: A Blade Runner-themed PCB badge shaped like the Tyrell Corporation's owl, made for Hackaday Supercon 2019 in Los Angeles; an ESP12 drives nine NeoPixels (eight on the front that flash a secret message, one reversed to backlight the owl's cybernetic eye), it charges a LiPo over micro-USB, and each ear carries an SAO header.
functions: Flashes a secret message on the eight front NeoPixels; backlights the owl's eye with a ninth, reverse-mounted NeoPixel.
look:
  colors: []
  shape: bird
  themes:
  - bird
  - sci-fi
  - movie
tech:
  mcu: ESP12
  leds:
    count: 9
    type: NeoPixel
    note: Eight front-facing NeoPixels flash a secret message; a ninth is reverse-mounted to backlight the owl's eye.
  display: null
  connectivity:
  - wifi
  battery: LiPo, charges over micro-USB
  sao_version: null
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold at Hackaday Supercon 2019; remaining units were offered on Tindie afterward, per the maker's project page.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/sphawes/badgerunner
  firmware_url: https://github.com/sphawes/badgerunner
  eda_tool: KiCad
  notes: Artwork made in Inkscape and converted with svg2shenzhen, then laid out in KiCad. A separate companion project, glowtie's "programmer" subfolder, provides the hardware needed to flash the badge.
links:
- label: hackaday.io/project/168402-badge-runner
  url: https://hackaday.io/project/168402-badge-runner
  kind: hackaday
- label: github.com/sphawes/badgerunner
  url: https://github.com/sphawes/badgerunner
  kind: repo
- label: github.com/sphawes/glowtie/tree/master/programmer
  url: https://github.com/sphawes/glowtie/tree/master/programmer
  kind: repo
images:
  - file: assets/images/badges/supercon-2019/badge-runner/0f6f672287.jpg
    source: "https://hackaday.io/project/168402-badge-runner"
    credit: "Claire Sun"
    caption: "Badge Runner PCB badge, owl-shaped with NeoPixel display"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/168402-badge-runner
  title: BADGE RUNNER
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/168402-badge-runner
  title: BADGE RUNNER
  accessed: '2026-09-07'
  note: Confirmed maker, event/year, theme, ESP12 MCU, 9 NeoPixels, LiPo/micro-USB charging, two SAO headers (one per ear), and that leftover units were sold on Tindie after Supercon 2019.
- kind: url
  url: https://github.com/sphawes/badgerunner
  title: sphawes/badgerunner
  accessed: '2026-09-07'
  note: Confirms open-source hardware repo (art/pcb/ref folders); design done in Inkscape + svg2shenzhen + KiCad, per the project page.
- kind: url
  url: https://github.com/sphawes/glowtie/tree/master/programmer
  title: sphawes/glowtie - programmer
  accessed: '2026-09-07'
  note: A companion project (cad/pcb for a "glowtieProgrammer") used to flash the badge; not itself a badge or SAO.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, event, theme, MCU, LED count/behavior, battery, SAO headers) confirmed on the maker's own Hackaday.io project page and GitHub repo. Price, quantity made, and exact Tindie listing URL were not found; sources only say leftover units were later offered on Tindie. No image credit/date beyond the project page was available.
last_modified_date: '2026-09-07'
---

Badge Runner is a Blade Runner-themed conference badge made by Claire Sun for Hackaday Supercon 2019 in Los Angeles, shaped like the owl seen at the Tyrell Corporation in the film. An ESP12 module drives nine addressable NeoPixels: eight across the front flash a secret message, and a ninth is reverse-mounted to backlight the owl's cybernetic eye. The badge runs off a rechargeable LiPo battery topped up over micro-USB, and each ear carries its own SAO header, letting two add-ons be plugged in at once.

The hardware is fully open source, with artwork built in Inkscape and converted to PCB traces with svg2shenzhen before being laid out in KiCad; the files live in the `badgerunner` GitHub repo under art, pcb, and reference folders. A separate companion project, the "glowtieProgrammer" found in the `programmer` subfolder of the maker's `glowtie` repo, provides the hardware used to flash the badge's firmware.

Units were sold at Supercon 2019, and the maker's project page notes that leftover badges were later made available on Tindie, though the specific listing, price, and production quantity were not confirmed by any source found in this pass.
