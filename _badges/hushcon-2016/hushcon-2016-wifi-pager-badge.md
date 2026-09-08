---
title: Hushcon 2016 WiFi Pager Badge
id: hushcon-2016-hushcon-2016-wifi-pager-badge
layout: badge
parent: HushCon 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hushcon-2016
year: 2016
makers:
- name: whitey
summary: A "some assembly required" WiFi pager badge for HushCon 2016, combining an ESP8266 module with an ATmega328p.
functions: 'Out of the box, joins a WiFi access point and fetches a page over HTTP. A motor interface, backlight control, buttons, and Twitter notifications were planned (documented as TODO by the person who wrote the sample firmware) but not confirmed as finished.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
tech:
  mcu: ESP8266 + ATmega328p
  leds: null
  display: null
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Given out as the HushCon 2016 conference badge.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/osresearch/hushcon
  eda_tool: null
links:
- label: trmm.net/Hushcon
  url: https://trmm.net/Hushcon/
  kind: website
- label: osresearch/hushcon (sample Arduino firmware)
  url: https://github.com/osresearch/hushcon
  kind: repo
images:
- file: assets/images/badges/hushcon-2016/hushcon-2016-wifi-pager-badge/94259d38f1.jpg
  source: "https://trmm.net/Hushcon/"
  credit: "Trammell Hudson (Flickr: osr)"
  caption: "Hushcon 2016 WiFi pager badge kit"
- file: assets/images/badges/hushcon-2016/hushcon-2016-wifi-pager-badge/34cc0ecd22.jpg
  source: "https://trmm.net/Hushcon/"
  credit: "Trammell Hudson (Flickr: osr)"
  caption: "Hushcon 2016 WiFi pager badge, assembled"
contact: {}
notes:
- 'HushCon 2016 badge: an ESP8266 + ATmega328p WiFi pager, sold as a some-assembly-required soldering kit. Found by the event-year sweep, task con-toorcon.'
- 'The sweep''s title matches how the badge is generally referred to; no alternate maker-given name was found.'
status: listed
sources:
- kind: url
  url: https://trmm.net/Hushcon/
  title: Hushcon 2016 WiFi Pager Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-toorcon); event read as ''HushCon 2016''.'
- kind: url
  url: https://trmm.net/Hushcon/
  title: "Hushcon - Trammell Hudson's Projects"
  accessed: '2026-09-08'
  note: 'Primary source: confirms the badge, designer "whitey", ESP8266+ATmega328p, kit assembly details, and TODO list (motor, backlight, buttons, board redesign were unfinished as of the post). Two Flickr photos pulled from this page.'
- kind: url
  url: https://github.com/osresearch/hushcon
  title: osresearch/hushcon
  accessed: '2026-09-08'
  note: 'Repo of sample Arduino sketches written by Trammell Hudson (not the badge designer) for the badge; contains htp/, hushcon/, simple/ directories. No hardware design files found there, so open_source is "partial" (firmware sample only).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real badge via the maker-adjacent page trmm.net/Hushcon/ (Trammell Hudson, who wrote the sample firmware at the con). The badge''s actual designer, "whitey", has no separate profile or storefront found, so maker `url` is empty and price/quantity/availability are unknown. The page describes several features (motor interface, backlight, buttons, Twitter notifications) as an unfinished TODO list rather than confirmed working features -- only WiFi join + HTTP fetch is confirmed working. No board/case design files were found (repo has firmware only). "Design a board to fit in the Bravo pager" appears on the TODO list, suggesting the pager form factor may reference a Motorola Bravo-style pager case, but this is not confirmed.'
last_modified_date: '2026-09-08'
---

The HushCon 2016 badge was a "some assembly required" WiFi pager kit designed by a badge maker known as "whitey." Most surface-mount components came pre-installed, but attendees had to solder on the buttons, a motor, and through-hole pins for the ESP8266 module themselves. The badge paired an ESP8266 (WiFi) with an ATmega328p (main logic), linked over a software serial connection -- though the write-up notes that link was unreliable at 115200 baud and worked better rewired to the AVR's hardware UART.

The badges arrived without working software, so Trammell Hudson wrote a set of sample Arduino sketches for it during the conference itself. That code (published at github.com/osresearch/hushcon) gets a badge joining a WiFi access point and fetching a page over HTTP; a longer TODO list on the same page -- Twitter notifications, a motor interface, backlight control, dedicated buttons, and a purpose-built board to fit inside a Bravo-style pager case -- was left unfinished. No hardware design files (schematics, Gerbers, or a case design) have been located, so this entry treats the release as partially open source: sample firmware only.

## Make your own

No hardware files are available. The published sample firmware (Arduino sketches for the ESP8266 and ATmega328p pairing) is at [github.com/osresearch/hushcon](https://github.com/osresearch/hushcon); it joins a WiFi network and performs a basic HTTP fetch, but the author describes it as quickly written and in need of cleanup before further use.
