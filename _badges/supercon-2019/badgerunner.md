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
  url: https://hackaday.io/csun.codes
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
  open_source: yes
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
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched both cited sources and confirmed all non-empty fields and body sentences against them. Two corrections made. (1) The Claire Sun maker URL was dead (hackaday.io/claire-sun 404s); the Hackaday.io project page''s own author link resolves to hackaday.io/csun.codes, which is her real profile and does list this project - fixed. (2) make_your_own.open_source was "partial", reasoned from the absence of a LICENSE file in the repo; per this archive''s own field definition ("yes" if hardware and firmware are both published), the repo contains both the PCB/art files and the firmware sketch, and the maker''s own project page states outright that "this project is opensource and all the code and files needed to build your own Badgerunner is located on Github" - changed to "yes". Also removed the "security" look.theme tag: nothing in either source ties this badge to security/hacking function or theming beyond the general Blade Runner setting, and it does not fit the archive''s vocabulary as used elsewhere; "sci-fi", "cyberpunk", and "bird" are all directly supported. Independently confirmed via the GitHub API that the "sphawes" account name is in fact Stephen Hawes, matching the credited maker. Hackaday.io project page lists only Claire Sun as the creator; GitHub repo (hardware/firmware host) is under Stephen Hawes''s account, so both remain credited as makers per the sheet. No price or production quantity is stated anywhere. Could not confirm whether the badge was ever actually listed on Tindie after Supercon (no independent Tindie search was run for this pass). The saved image was checked against its cited Hackaday.io source page and clearly shows this badge (owl-shaped black PCB, visible ESP-12E module, 8 front NeoPixels, micro-USB jack, header pins on both ears).'
last_modified_date: '2026-09-07'
---

The Badgerunner (formally "Badge Runner") is a Blade Runner-themed conference badge Claire Sun made for Hackaday Supercon 2019, shaped after the owl used by the Tyrell Corporation in the film. Sun was inspired after seeing #badgelife projects from DEF CON and picked the theme partly because Supercon that year was held near Los Angeles, around the time and place the original film is set. The board art was laid out in Inkscape and exported with svg2shenzhen, with schematics and board layout done in KiCad.

Electronically, the badge runs on an ESP12 driving nine NeoPixels: eight across the front flash a hidden message, and a ninth is soldered in reverse to backlight the owl's cybernetic eye from behind. It's powered by a rechargeable LiPo battery, chargeable over micro-USB, and each ear carries its own SAO header so two add-ons can be plugged in at once.

Sun made multiple badges to sell in person at Supercon 2019, with the plan to list any leftovers on Tindie afterward; no surviving Tindie listing was found to confirm that happened. Hardware and firmware are hosted on GitHub under Stephen Hawes's account (sphawes/badgerunner), with a companion programmer in a separate "glowtie" repo, though the repo carries no explicit open-source license.
