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
summary: 'The $45 badge package at CactusCon 2017 (badge, shirt, and swag) included a scanner badge, built on a WeMOS board, that scans for nearby Wi-Fi networks and Bluetooth devices.'
functions: 'A Wi-Fi and Bluetooth scanner; the attendee source that documents it does not describe the specific display behavior (e.g. signal strength readout, MAC-address scrolling).'
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
tech:
  mcu: null
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
  note: 'Primary first-hand attendee source behind the badge.gallery writeup: confirms the $45 paid badge/shirt/swag package (with free general admission otherwise), the WeMOS-board build, soldering at the event, and that the badge is a Wi-Fi/Bluetooth scanner. Read directly (raw page text) and does NOT support badge.gallery''s more specific claims of an ESP32 chip, Wi-Fi signal-strength display, or Bluetooth MAC-address scrolling -- those claims were not carried into this entry.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Fact-check pass (2026-09-10): fetched both cited sources directly. ratil.life (the primary first-hand attendee writeup) confirms only that the badge is "a tiny Wi-Fi and Bluetooth scanner made from a WemOS Board," the $45 badge/shirt/swag package, free general admission otherwise, and on-site soldering/de-soldering. It does NOT name an ESP32 chip, describe a Wi-Fi signal-strength readout, or describe Bluetooth MAC-address scrolling. badge.gallery''s page attributes those three specifics to "the writeup" but they are not present in the writeup''s text, and badge.gallery''s own "module-variant caveat" note explicitly says the exact controller was never identified. Because those specifics could not be confirmed against the primary source, tech.mcu was blanked (was "ESP32 (WeMOS board)") and functions was corrected to drop the signal-strength/MAC-scrolling claims. No maker/official CactusCon page for this badge was found. A separate GitHub repo, thatch/cactuscon-badge-2017 ("Badge for CactusCon, based on ESP-32", CC-BY-4.0, KiCad files), turned up in search and is plausibly related (same event/year, same ESP32 family) but nothing ties it explicitly to this Wi-Fi/Bluetooth-scanner badge, so it remains unlinked. Left tech.leds, tech.display, tech.battery, get_one.quantity, and get_one.availability empty/unknown; no usable image of the badge itself was found (badge.gallery notes the attendee photos lack clearable rights).'
last_modified_date: '2026-09-10'
---

CactusCon 2017 offered attendees a paid $45 package — badge, shirt, and swag — alongside free general admission to the Phoenix-area con. The badge in that package was a small Wi-Fi and Bluetooth scanner built on a WeMOS board.

The record comes from a single first-hand attendee writeup, later aggregated by badge.gallery; no page from CactusCon or a named hardware maker was found describing this specific badge. The writeup describes soldering (and some troubleshooting) required to assemble the board at the event, but does not name the exact chip, display, LEDs, battery, or firmware, and no clearable photo of the badge itself has surfaced. (The badge.gallery writeup asserts more specific behavior — a Wi-Fi signal-strength readout and a scrolling Bluetooth MAC-address display — but the attendee source it cites does not actually describe those details, so they are omitted here.) A separate open-source ESP32 KiCad project, thatch/cactuscon-badge-2017, targets the same event and year but could not be confidently tied to this particular badge, so it is noted here rather than linked as its design files.
