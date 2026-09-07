---
title: YoDawgSAO
id: supercon-2024-yo-dawg-sao-2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: '''Yo Dawg, I heard you like add-ons on your badges'' SAO base plate that introduces the 19x19 mm SAOAO mini add-on format (1.27 mm GND-VCC-GND header) with Iron Man, Hack-A-Day, xHain and Cluster mini boards; made around the Supercon 2024 add-on contest.'
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
  open_source: "partial"
  hardware_url: https://github.com/davedarko/YoDawgSAO
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: github.com/davedarko/YoDawgSAO
  url: https://github.com/davedarko/YoDawgSAO
  kind: repo
images:
  - file: assets/images/badges/supercon-2024/yo-dawg-sao-2/a69ddf7e5e.jpg
    source: "https://github.com/davedarko/YoDawgSAO"
    credit: "davedarko"
    caption: "KiCad render of the YoDawgSAO base plate"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/davedarko/YoDawgSAO
  title: davedarko/YoDawgSAO
  accessed: '2026-09-07'
  note: "Project README: origin story (Supercon 2024 add-on contest), 19x19mm size, 1.27mm GND-VCC-GND header, KiCad files, render image."
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/README.md
  title: davedarko/Simple-Add-ons-SAO README
  accessed: '2026-09-07'
  note: "Confirms YoDawgSAO is listed among davedarko's SAO designs, KiCad format, one-line description matching the project repo."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Maker's own README confirms what this is (a base-plate SAO defining a smaller 19x19mm 'SAOAO' sub-header standard for mini add-ons) and the design rationale, but does not state chip/LEDs, price, quantity, or distribution — the base plate itself appears to be a passive breakout with no MCU mentioned. No storefront or listing found; likely a contest/gift item rather than sold. The mini add-ons mentioned in the sheet-derived summary (Iron Man, Hack-A-Day, xHain, Cluster) are not detailed in the README examined; could not verify their individual specs. Colors/shape/themes left empty since no additional photos beyond the KiCad render were found."
last_modified_date: '2026-09-07'
---

YoDawgSAO is davedarko's entry into the Hackaday Supercon 2024 add-on contest, but with a twist: rather than building a single complex SAO packed onto the standard I2C header, davedarko designed a small base plate that itself carries a smaller add-on header, so people could plug in a "badge for your badge for your badge." The name and framing ("Yo Dawg, I heard you like add-ons on your badges?") riff on the well-known internet meme.

The base plate defines a new mini format, informally called SAOAO, constrained to 19mm x 19mm and using a 1.27mm pitch GND-VCC-GND header. In the project README, davedarko notes this header pitch was, in hindsight, "the wrong decision as it is a pain to solder — but it's the standard now," suggesting the format was adopted by others for their own mini add-ons after the contest. The design is published as KiCad files in the `davedarko/YoDawgSAO` repository and is also listed as one of many designs in his broader `Simple-Add-ons-SAO` repo, which collects his SAO work across several years and events.

No pricing, production quantity, or storefront listing was found, and the README does not mention an MCU, LEDs, or display on the base plate itself, consistent with it being a passive connector/breakout board rather than an active electronic badge. The Iron Man, Hack-A-Day, xHain and Cluster mini boards referenced in the community sheet appear to be separate small add-ons meant to plug into this base plate's mini header, but their individual specifics were not found in the sources reviewed.
