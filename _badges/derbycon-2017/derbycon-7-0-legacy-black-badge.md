---
title: DerbyCon Legacy Black Badge
id: derbycon-2017-derbycon-7-0-legacy-black-badge
layout: badge
parent: DerbyCon 7.0 "Legacy"
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: derbycon-2017
year: 2017
makers:
- name: Ben Hibben
  url: https://www.hackster.io/blenster
- name: Charles "The Hat" Lehman
summary: A hand-built wooden Black Badge made for DerbyCon 7.0 "Legacy", awarded to individuals honored for service to the community rather than sold.
functions: Powers up to display animated LED patterns across the front artwork; a hidden header on the back can be populated with an ATmega328P to turn the badge into a USB-programmable Arduino.
look:
  colors:
  - wood
  - black
  shape: null
  themes:
  - wearable
  - logo
  - art
tech:
  mcu: Atmel XMEGA 32A4U (x9, one master + eight LED-driver MCUs)
  leds:
    count: 198
    type: discrete
    note: Bright white SMT LEDs, software-dimmed via PDM (pulse density modulation) since the XMEGA lacks enough hardware PWM channels for 32 LEDs per chip.
  display: none
  connectivity:
  - usb
  battery: Rechargeable LiPo, charges over USB
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - contest
  where: Not sold or publicly distributed; DerbyCon Black Badges are a special award given to individuals recognized for achievement or service to the community, granting lifetime conference access.
make_your_own:
  open_source: no
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.hackster.io/blenster/derbycon-legacy-black-badge-ca2917
  url: https://www.hackster.io/blenster/derbycon-legacy-black-badge-ca2917
  kind: article
images:
- file: assets/images/badges/derbycon-2017/derbycon-7-0-legacy-black-badge/c1b134494d.jpg
  source: "https://www.hackster.io/blenster/derbycon-legacy-black-badge-ca2917"
  credit: "Ben Hibben"
  caption: "The finished wooden Legacy black badge, lit up, showing the LED front artwork"
- file: assets/images/badges/derbycon-2017/derbycon-7-0-legacy-black-badge/e3ae8d2446.jpg
  source: "https://www.hackster.io/blenster/derbycon-legacy-black-badge-ca2917"
  credit: "Ben Hibben"
  caption: "Wood case layers and PCB assembly during fabrication of the badge"
contact: {}
notes:
- 'The archive sweep''s title read "DerbyCon 7.0 Legacy Black Badge"; the maker''s own project title on Hackster.io is "DerbyCon Legacy Black Badge" (no "7.0"). Kept the event/year framing in the entry slug and event field since the badge was made for DerbyCon 7.0 "Legacy" (2017).'
- 'LED count corrected: the sweep''s note said 224 LEDs; Hibben''s own Hackster page and parts list say almost 200 (198 "Bright White SMT LEDs" exactly, described in prose as "over 200" and "almost 200").'
- 'hackster.io returns a Cloudflare block to automated fetches; content was read from the Wayback Machine capture of the same page (web.archive.org), which mirrors the maker''s own text and photos.'
status: released
sources:
- kind: url
  url: https://www.hackster.io/blenster/derbycon-legacy-black-badge-ca2917
  title: DerbyCon 7.0 Legacy Black Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-derbycon); event read as ''DerbyCon 2017''.'
- kind: url
  url: https://www.hackster.io/blenster/derbycon-legacy-black-badge-ca2917
  title: DerbyCon Legacy Black Badge - Ben Hibben (Hackster.io, via Wayback Machine)
  accessed: '2026-09-08'
  note: Maker's own project write-up (fetched via web.archive.org since the live page blocks automated requests); confirmed maker names, MCU, LED count/type, materials, battery, USB/Arduino header, and the black-badge award context.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (makers, MCU, LED count, construction, battery, distribution as an award) confirmed on Ben Hibben's own Hackster.io project page. No pricing, production quantity, or design-file release found or expected, since DerbyCon Black Badges are explicitly not shared/released "to avoid making it too easy to replicate" and are limited, awarded artifacts rather than sold products. No repo, storefront, or additional press coverage located.
last_modified_date: '2026-09-08'
---

The DerbyCon 7.0 "Legacy" Black Badge is a one-off award badge built by Ben Hibben (Blenster) with Charles "The Hat" Lehman for DerbyCon's 2017 event. DerbyCon Black Badges are given each year to individuals recognized for achievement or service to the community and grant lifetime conference access; they are not sold. Following the "Legacy" theme, Hibben built a case that looks like plain wood until it's powered on: six laser-cut layers of walnut, aspen, and red cedar with burled and pale maple faces, backed by black acrylic (for sharper LED-cutout edges) and clear acrylic spacers, all hand-finished in shellac.

Behind the wood sits a PCB carrying 198 bright-white SMT LEDs, laid out by a Python script that exported LED coordinates into the firmware so animations could be positioned to match the artwork. Because each of nine Atmel XMEGA 32A4U microcontrollers (eight LED drivers reporting to one master over 2 Mbps serial) has to drive up to 32 LEDs without enough hardware PWM channels, dimming is done in software using pulse density modulation. A rechargeable LiPo battery charges over USB, and a hidden pin header on the back — designed to be populated with an ATmega328P and an Arduino bootloader — turns the badge into a programmable Arduino board when needed.

As with other DerbyCon Black Badges, Hibben and Lehman did not publish build files or a BOM in full, noting the badges are meant to stay unique and hard to replicate. No price, sale, or production-run count is documented; it exists only as an awarded, limited artifact.
