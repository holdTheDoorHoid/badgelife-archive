---
title: Kernelcon 2021 Hacker HotKey
id: kernelcon-2021-kernelcon-2021-hacker-hotkey
layout: badge
parent: Kernelcon 2021
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: kernelcon-2021
year: 2021
makers:
- name: Kernelcon
  url: https://kernelcon.org/
summary: A customizable USB hotkey/macro-pad badge for Kernelcon's 2021 Hack Live! virtual event, used to vote in event challenges and launch event links.
functions: 'Four "launch" buttons that detect the host OS and open event web links; a second row of "voting" buttons that type vote commands for event challenges, sabotages, and hints. Fully reprogrammable as a general-purpose USB HID macro pad after the event.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: Arduino Leonardo (ATmega32u4)
  leds: null
  display: 'none'
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Given out for Kernelcon''s 2021 "Hack Live!" event, described as free and one day only; not sold through a storefront that sources could confirm.'
make_your_own:
  open_source: 'yes'
  hardware_url: null
  firmware_url: https://github.com/kernelcon/hacker-hotkey
  firmware_url_note: 'Includes a basic sample sketch and a more advanced configuration-driven firmware; also links a 3D-printable case on Thingiverse (thing:4828073).'
  eda_tool: null
  license: Apache-2.0
links:
- label: badge.gallery/badges/kernelcon-2021-hacker-hotkey
  url: https://badge.gallery/badges/kernelcon-2021-hacker-hotkey
  kind: website
- label: github.com/kernelcon/hacker-hotkey
  url: https://github.com/kernelcon/hacker-hotkey
  kind: repo
images:
- file: assets/images/badges/kernelcon-2021/kernelcon-2021-hacker-hotkey/69a89f70ae.jpg
  source: "https://github.com/kernelcon/hacker-hotkey"
  credit: "Kernelcon"
  caption: "The Hacker HotKey badge"
- file: assets/images/badges/kernelcon-2021/kernelcon-2021-hacker-hotkey/1a4249e5d8.jpg
  source: "https://github.com/kernelcon/hacker-hotkey"
  credit: "Kernelcon"
  caption: "Default hotkey button mapping"
contact: {}
notes:
- Customizable hotkey/stream-deck style conference badge for Kernelcon 2021. Found by the event-year sweep, task con-kernelcon.
- The sweep's summary called it a "stream-deck style conference badge"; the maker's own GitHub README describes it plainly as the "Hacker HotKey" firmware repo for Kernelcon's 2021 Hack Live! badge, which this entry follows.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/kernelcon-2021-hacker-hotkey
  title: Kernelcon 2021 Hacker HotKey
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kernelcon); event read as ''Kernelcon 2021''.'
- kind: url
  url: https://github.com/kernelcon/hacker-hotkey
  title: kernelcon/hacker-hotkey
  accessed: '2026-09-08'
  note: 'Maker''s own GitHub repo README; confirmed Arduino Leonardo hardware, USB HID firmware, button mapping, open-source Apache-2.0 license, and the 3D-printed case on Thingiverse. Provided the two saved images.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, released badge via the maker''s own GitHub repo. Could not confirm price, quantity made, or a working storefront link (kernelcon.square.site referenced in badge.gallery''s summary was not checked directly and is not cited as a source here); PCB colors/shape and LED/display details are not stated anywhere found, so left empty. No third-party press coverage located.'
last_modified_date: '2026-09-08'
---

The Hacker HotKey is Kernelcon's badge for its 2021 "Hack Live!" virtual event, built as a small USB macro pad rather than a wearable electronic badge. It runs on an Arduino Leonardo and presents itself to a computer as a USB HID keyboard: a top row of "launch" buttons detects the host operating system and opens event web links, while a second row of "voting" buttons types vote commands so attendees could participate in Hack Live's challenges, sabotages, and hint polls.

Kernelcon published the firmware openly on GitHub under the Apache-2.0 license, offering both a simple sample sketch and a more advanced, configuration-driven version that lets owners remap the buttons into a general-purpose hotkey device once the event was over. The project also links an optional 3D-printable case on Thingiverse for attendees who wanted to finish the look.

No pricing, production quantity, or ongoing storefront availability could be confirmed from the sources reviewed; the badge appears to have been a free giveaway tied specifically to the one-day Hack Live event rather than an item sold afterward.
