---
title: CactusCon 2017 Wi-Fi/Bluetooth Scanner Badge
id: cactuscon-2017-cactuscon-2017-wi-fi-bluetooth-scanner-badge
layout: badge
parent: CactusCon 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2017
year: 2017
makers:
- name: CactusCon
summary: 'The $45 badge package at CactusCon 2017 (badge, shirt, and swag) included an ESP32-based scanner badge, built on a WeMOS board, that displays nearby Wi-Fi networks and Bluetooth devices.'
functions: 'Scans for and displays nearby Wi-Fi SSIDs with signal strength, and scrolls detected Bluetooth device MAC addresses.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
tech:
  mcu: ESP32 (WeMOS board)
  leds: null
  display: null
  connectivity:
  - wifi
  - bluetooth
  battery: null
  sao_version: null
get_one:
  price: $45 (badge + shirt + swag package)
  price_usd: 45
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: 'Sold as part of a paid badge/shirt/swag package at CactusCon 2017 in Phoenix, AZ; general admission (without this badge) was also available free.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/badges/cactuscon-2017-wifi-bluetooth-scanner-badge
  url: https://badge.gallery/badges/cactuscon-2017-wifi-bluetooth-scanner-badge
  kind: website
- label: 'ratil.life: Hacking and Skydiving (attendee writeup)'
  url: https://ratil.life/hacking-and-skydiving/
  kind: article
images: []
contact: {}
notes:
- Official CactusCon 2017 badge that scans for nearby Wi-Fi and Bluetooth devices. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task con-layerone.
- 'Confirmed to exist via an attendee first-hand writeup (ratil.life), aggregated by badge.gallery. Sweep''s one-line summary held up.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/cactuscon-2017-wifi-bluetooth-scanner-badge
  title: CactusCon 2017 Wi-Fi/Bluetooth Scanner Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''CactusCon 2017''.'
- kind: url
  url: https://ratil.life/hacking-and-skydiving/
  title: Hacking and Skydiving
  accessed: '2026-09-10'
  note: 'Primary first-hand attendee source behind the badge.gallery writeup: confirms the $45 paid badge/shirt/swag package, the WeMOS-board build, soldering at the event, and Wi-Fi/Bluetooth scanning behavior.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-10'
  notes: 'No maker/official CactusCon page for this specific badge was found, only a third-party aggregator (badge.gallery) built from a single attendee blog post (ratil.life), which does not include photos of the badge itself or full hardware specs (exact WeMOS module, display, battery, LEDs, firmware). A separate GitHub repo, thatch/cactuscon-badge-2017 ("Badge for CactusCon, based on ESP-32", CC-BY-4.0, KiCad files, renders cactus_front.png/cactus_back.png), turned up in search and is plausibly related (same event/year, same ESP32 family) but nothing ties it explicitly to the Wi-Fi/Bluetooth-scanner functionality described by the attendee, so it was not linked as design files here. Left tech.leds, tech.display, tech.battery, get_one.quantity, and get_one.availability empty/unknown for the same reason. No usable image of the badge itself was found (badge.gallery notes the attendee photos lack clearable rights).'
last_modified_date: '2026-09-10'
---

CactusCon 2017 offered attendees a paid $45 package — badge, shirt, and swag — alongside free general admission to the Phoenix-area con. The badge in that package was a small scanner built on a WeMOS board (ESP32-based) that displayed nearby Wi-Fi SSIDs with signal strength and scrolled the MAC addresses of detected Bluetooth devices.

The record comes from a single first-hand attendee writeup, later aggregated by badge.gallery; no page from CactusCon or a named hardware maker was found describing this specific badge. The writeup describes soldering (and some troubleshooting) required to assemble the board at the event, but does not go into the exact module variant, display, LEDs, battery, or firmware, and no clearable photo of the badge itself has surfaced. A separate open-source ESP32 KiCad project, thatch/cactuscon-badge-2017, targets the same event and year but could not be confidently tied to this particular badge, so it is noted here rather than linked as its design files.
