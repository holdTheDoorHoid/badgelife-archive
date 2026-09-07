---
title: Beardo Badge
id: dc27-beardo-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: s7a73farm
  url: https://hackaday.io/hacker/338486-s7a73farm
- name: gr3yR0n1n
  url: https://hackaday.io/gr3yr0n1n
  role: firmware/code
- name: Compukidmike
  role: engineering support
summary: An audio-reactive DEF CON 27 indie badge with 112 SK6812-MINI RGB LEDs arranged as a bearded, goggle-wearing figure, driven by an ESP32-WROOM with a microphone input, 23 LED modes, micro-USB charging and a 1500 mAh LiPo, engineered with Compukidmike and assembled by Seeed Studio.
functions: Sound-reactive LED animation across 23 modes, three-button control with mode cycling and adjustable brightness, a "Looky Eyes" mode, and (as originally designed) a soft-AP for custom scrolling text and a multi-badge "party mode" when several units are in range.
look:
  colors: []
  shape: null
  themes:
  - security
  - wearable
tech:
  mcu: ESP32-WROOM
  leds:
    count: 112
    type: SK6812-MINI
    note: Originally designed around WS2812 3535 packages; switched to SK6812-MINI after a footprint error was found between prototype sizes.
  display: none
  connectivity:
  - wifi
  - bluetooth
  - usb
  - audio
  battery: LiPo 1500 mAh, charged via micro-USB
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold as a DEF CON 27 indie badge; exact storefront and remaining quantity not found. Production was limited by LED-component shortages at the time.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/s7a73farm/s7a73farm_DC27_BeardoBadge
  eda_tool: null
  notes: The GitHub repo holds firmware/source code and usage documentation (button controls, modes); no schematics, Gerbers, or BOM were found published there, so hardware is not confirmed open.
links:
- label: hackaday.io/project/167172-beardo-badge-dc27-indie-badge
  url: https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260614033854/https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
- label: medium.com/@s7a73farm/badgelife-the-good-the-bad-and-the-i-did-not-see-that-coming-c64c081f517
  url: https://medium.com/@s7a73farm/badgelife-the-good-the-bad-and-the-i-did-not-see-that-coming-c64c081f517
  kind: website
- label: github.com/s7a73farm/s7a73farm_DC27_BeardoBadge
  url: https://github.com/s7a73farm/s7a73farm_DC27_BeardoBadge
  kind: repo
images:
- file: assets/images/badges/dc27/beardo-badge/bc33b503e0.jpg
  source: https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
  credit: s7a73farm
  caption: The Beardo Badge, a bearded goggle-wearing figure lit by 112 RGB LEDs
  archived: https://web.archive.org/web/20260614033854/https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
- file: assets/images/badges/dc27/beardo-badge/9896561ac7.jpg
  source: https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
  credit: s7a73farm
  caption: Beardo Badge assembled prototype photo
  archived: https://web.archive.org/web/20260614033854/https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
  title: Beardo Badge - DC27 Indie Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260614033854/https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
- kind: url
  url: https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
  title: Beardo Badge - DC27 Indie Badge
  accessed: '2026-09-07'
  note: Core facts - maker team (s7a73farm, gr3yR0n1n, Compukidmike), ESP32-WROOM MCU, 112 SK6812-MINI LEDs (changed from WS2812 3535), 23 modes, 1500 mAh LiPo, micro-USB charging, WiFi/BLE, LED shortage limiting production. Also source of the two saved photos.
  archived: https://web.archive.org/web/20260614033854/https://hackaday.io/project/167172-beardo-badge-dc27-indie-badge
- kind: url
  url: https://github.com/s7a73farm/s7a73farm_DC27_BeardoBadge
  title: GitHub - s7a73farm/s7a73farm_DC27_BeardoBadge
  accessed: '2026-09-07'
  note: 'Firmware/source repo exists with usage docs (buttons, modes); no schematics/Gerbers/BOM found, so hardware files are unconfirmed - used for make_your_own.open_source: partial.'
- kind: url
  url: https://hackaday.io/project/166728-s7a73farm-unofficial-def-con-27-mega-badge
  title: S7a73farm Unofficial DEF CON 27 Mega badge
  accessed: '2026-09-07'
  note: Confirms this is a separate, oversized (22"x22") promotional plexiglass build of the same design, not the indie badge itself; not used to fill fields, only for context in research.notes.
  archived: https://web.archive.org/web/20251011200006/https://hackaday.io/project/166728-s7a73farm-unofficial-def-con-27-mega-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io project page and GitHub repo confirm the core technical facts (MCU, LED count/type, battery, modes). Price, quantity made, and exact distribution/storefront were not stated in any source found and are left empty. The Medium retrospective post (linked from the entry) returned a Cloudflare block on every fetch attempt and could not be read - it likely holds more of the origin story and production numbers. A related item exists: an oversized 22"x22" plexiglass "Mega Badge" replica of this same design (440 SK6812 LEDs on strips, USB power bank) built by the same maker for DJ shows/promotion while waiting on corrected Beardo Badge prototypes - see other_items_found in the report; it is a distinct build, not a duplicate of this entry.'
last_modified_date: '2026-09-07'
---

The Beardo Badge is a DEF CON 27 (2019) indie badge shaped like a bearded, goggle-wearing figure, built by s7a73farm with firmware/code help from gr3yR0n1n and engineering support from Compukidmike. An ESP32-WROOM drives 112 SK6812-MINI RGB LEDs through 23 animation modes, reacting to sound picked up by an onboard microphone; three buttons cycle modes and adjust brightness, and a dedicated "Looky Eyes" mode animates the figure's goggles. Power comes from a 1500 mAh LiPo charged over micro-USB, and the design originally planned WiFi soft-AP scrolling text and a multi-badge "party mode" for when several units were near each other.

The project went through at least one hardware revision: it started out designed around WS2812 3535-package LEDs before a footprint mismatch between prototype sizes was found, and the design was corrected to use SK6812-MINI parts instead. LED component shortages around the DEF CON 27 timeframe also constrained how many badges could be built. While waiting on corrected PCB prototypes, the maker built a separate, much larger 22"x22" plexiglass "Mega Badge" version of the same artwork, strung with 440 SK6812 LEDs on strips and run off a USB power bank, as a promotional piece for BadgeLife rather than a wearable.

Firmware and source code for the badge are published on GitHub (s7a73farm/s7a73farm_DC27_BeardoBadge), including usage documentation for the button controls and modes, but no schematics, Gerbers, or bill of materials were found published alongside it, so the hardware side is not confirmed to be open. Sale price, production quantity, and current availability were not found in the sources checked.
