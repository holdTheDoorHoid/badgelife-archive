---
title: CarolinaCon Online 2 Badge
id: carolinacon-2022-carolinacon-online-2-badge
layout: badge
parent: CarolinaCon Online 2
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: carolinacon-2022
year: 2022
makers:
- name: Matt Agius
summary: A keychain-sized PCB badge for CarolinaCon Online 2, shaped around the con's ivy-covered logo art with a single blinking red LED driven by a 555-style timer circuit.
functions: Blinks a single red LED via an astable 555/7555 timer circuit; no other interactivity.
look:
  colors:
  - blue
  - black
  shape: keychain
  themes:
  - logo
  - minimalist
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Single through-hole red LED, blinking, driven by the 555 timer astable circuit.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold through the CarolinaCon Online 2 shop bundled with a shirt, shot glass, and sticker; current availability not confirmed.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/184890-carolina-con-online-2-badge
  url: https://hackaday.io/project/184890-carolina-con-online-2-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260308010955/https://hackaday.io/project/184890-carolina-con-online-2-badge
images:
- file: assets/images/badges/carolinacon-2022/carolinacon-online-2-badge/ab6edcf9ba.jpg
  source: https://hackaday.io/project/184890-carolina-con-online-2-badge
  credit: Matt Agius
  caption: CarolinaCon Online 2 badge, blue PCB variant with con logo artwork and blinking LED
  archived: https://web.archive.org/web/20260308010955/https://hackaday.io/project/184890-carolina-con-online-2-badge
- file: assets/images/badges/carolinacon-2022/carolinacon-online-2-badge/a1e4853297.jpg
  source: https://hackaday.io/project/184890-carolina-con-online-2-badge
  credit: Matt Agius
  caption: CarolinaCon Online 2 badge, black PCB variant
  archived: https://web.archive.org/web/20260308010955/https://hackaday.io/project/184890-carolina-con-online-2-badge
contact: {}
notes:
- Official badge for CarolinaCon Online 2 (April 29-May 1, 2022), featuring the con logo as PCB art with a 555 timer circuit, bundled with shirt/shot glass/sticker. Found by the event-year sweep, task carolinacon.
- The sweep's notes gave the dates as April 29-30; the Hackaday project page states April 29-May 1, 2022.
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/184890-carolina-con-online-2-badge
  title: CarolinaCon Online 2 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:carolinacon); event read as ''CarolinaCon 2022''.'
  archived: https://web.archive.org/web/20260308010955/https://hackaday.io/project/184890-carolina-con-online-2-badge
- kind: url
  url: https://hackaday.io/project/184890-carolina-con-online-2-badge
  title: CarolinaCon Online 2 Badge
  accessed: '2026-09-08'
  note: Confirmed maker, event/dates, 555-timer circuit, sale through the con shop bundled with shirt/shot glass/sticker; pulled two project gallery photos showing blue and black PCB variants.
  archived: https://web.archive.org/web/20260308010955/https://hackaday.io/project/184890-carolina-con-online-2-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via the maker's own Hackaday.io project page (photos and description). Could not confirm price, quantity made, or whether it is still available anywhere else online; no repo or design files were found. Chip is visibly marked "7555" (a CMOS 555 variant) in the project photos rather than a classic bipolar 555, though Hackaday's own text just says "555 timer."
last_modified_date: '2026-09-08'
---

The CarolinaCon Online 2 badge is a small keychain-shaped PCB made by Matt Agius for CarolinaCon Online 2, a volunteer-run North Carolina hacker con held online April 29 to May 1, 2022. The board's face is engraved with the con's ivy-and-trellis logo art and the event wordmark, cut into a shield-like keychain outline with a keyring loop at the top.

Electrically it is a simple decorative badge: a single red LED blinks on and off, driven by an astable timer circuit built around a 7555 CMOS timer chip (a low-power variant of the classic 555), a pair of resistors, and an electrolytic capacitor visibly labeled "120uF" in the project photos. There is no microcontroller, display, or wireless connectivity — the badge does one thing, blink, and exists mainly as PCB art and a keepsake.

It was sold through the official CarolinaCon Online 2 shop as part of a bundle with a shirt, shot glass, and sticker. The Hackaday.io project page shows at least two color variants, a blue solder mask and a black solder mask, both with gold/tan silkscreen artwork. Pricing, production quantity, and current availability were not stated on the maker's page, and no hardware or firmware files were published for it.
