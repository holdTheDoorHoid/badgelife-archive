---
title: Saw the Badge (DEF CON 27 Indie Badge)
id: dc27-saw-the-badge-def-con-27-indie-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: MagicStoneTech
  url: https://www.tindie.com/stores/magicstonetech/
summary: A DEF CON 27 indie badge shaped after the Billy puppet from the Saw film franchise, with animated LED cheeks, pulsing eyes, and an OLED nametag, plus an optional cassette-tape SAO add-on.
functions: Cycles through randomized LED animations via a mode button (including a test mode); the OLED nametag displays the character name and taglines; includes an audio playback engine and can be used as a DTMF dialer; the cassette-tape add-on animates its reel LEDs to mimic tape playing.
look:
  colors:
  - red
  - black
  shape: null
  themes:
  - horror
  - movie
  - mascot
tech:
  mcu: SAMD21
  leds:
    count: 44
    type: reverse-mount
    note: 20 & 24 LEDs in the two cheek spirals (ISSI 36-channel LED driver), plus pulsing red backlit eyes and illuminated bowtie/handkerchief; hot-glue diffusers over rear-mount LEDs.
  display: OLED nametag
  connectivity:
  - usb
  battery: LiPo 400mAh, USB micro-B charging
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: '25'
  availability: sold_out
  availability_note: Tindie listing marked "Product Retired" / no longer available for sale as of 2026-09-07.
  distribution:
  - purchase
  where: Sold via the maker's Tindie store around DEF CON 27 (2019); remaining units were later built from leftover components before the run ended.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge
  url: https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
  kind: store
  archived: https://web.archive.org/web/20260518213527/https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
images:
- file: assets/images/badges/dc27/saw-the-badge-def-con-27-indie-badge/82ea88a566.jpg
  source: https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
  credit: MagicStoneTech
  caption: SAW the Badge, DEF CON 27 indie badge
  archived: https://web.archive.org/web/20260518213527/https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
- file: assets/images/badges/dc27/saw-the-badge-def-con-27-indie-badge/d40bb1c728.jpg
  source: https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
  credit: MagicStoneTech
  caption: SAW the Badge with cassette tape SAO add-on
  archived: https://web.archive.org/web/20260518213527/https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
contact: {}
notes:
- cassette-tape add-on mentioned alongside main badge
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
  title: Saw the Badge (DEF CON 27 Indie Badge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
  archived: https://web.archive.org/web/20260518213527/https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
- kind: url
  url: https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
  title: Saw the Badge (DEF CON 27 Indie Badge) - Tindie listing
  accessed: '2026-09-07'
  note: Maker's own storefront; confirmed features, MCU, battery, SAO header, cassette add-on, retired/sold-out status.
  archived: https://web.archive.org/web/20260518213527/https://www.tindie.com/products/magicstonetech/saw-the-badge-defcon-27-indie-badge/
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27
  accessed: '2026-09-07'
  note: Confirmed quantity made (25, hand-placed), SAM D21 via Sean Hodgins' HCC module, ISSI 36-channel LED driver, DTMF dialer function, hot-glue diffusers.
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price was not stated on the archived Tindie listing (product retired, price no longer shown). Design files/open-source status not found; maker does not appear to have published hardware or firmware for this badge. Look.shape left null — no source described an overall board outline (e.g. "skull" or "humanoid") beyond describing it as a Billy-puppet-themed face badge.
last_modified_date: '2026-09-07'
---

SAW the Badge is a DEF CON 27 (2019) indie badge by MagicStoneTech (Las Vegas, NV), styled after the Billy puppet from the *Saw* film franchise. Its two cheek spirals hold 44 red LEDs total (20 and 24 per side) driven through an ISSI 36-channel LED driver, with slow-pulsing backlit eyes and an illuminated bowtie and handkerchief. A mode button cycles through the randomized lighting animations and a test mode, and a small OLED "nametag" displays the character's name and taglines. The badge runs on a SAM D21 (Arduino Zero-compatible) microcontroller carried on one of Sean Hodgins' HCC modules, and includes an onboard audio playback engine that can also work as a DTMF dialer. Power comes from an included 400 mAh LiPo battery charged over USB micro-B.

The badge carries a v1.69bis SAO header and shipped alongside an optional "Play Me" microcassette-shaped SAO: LEDs around its two tape reels animate in sync with the main badge to mimic a cassette playing. MagicStoneTech hand-placed all 25 units of the badge for the DEF CON 27 run, selling them through the maker's Tindie store; the listing was later built out with a few final units from remaining components before the product was marked retired. As of this research pass the Tindie listing is no longer available for sale, and no hardware or firmware files have been published for the design.
