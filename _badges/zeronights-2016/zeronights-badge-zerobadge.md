---
title: ZeroNights Badge (ZeroBadge)
id: zeronights-2016-zeronights-badge-zerobadge
layout: badge
parent: ZeroNights 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: zeronights-2016
year: 2016
makers:
- name: ZeroNights
summary: 'A matryoshka-doll-shaped PCB badge that is functionally an Arduino Leonardo board, requiring attendees to hand-solder its surface-mount components.'
functions: 'Runs as a general-purpose ATmega32U4 (Arduino Leonardo) board once soldered; ships with a single onboard LED (Blink demo shown running in coverage).'
look:
  colors: []
  shape: null
  themes:
  - mascot
tech:
  mcu: ATmega32U4
  leds:
    count: 1
    type: discrete
    note: single SMD 0603 LED on digital pin 12
  display: none
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
  where: 'Distributed at ZeroNights, November 2016, in Russia.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: remontka.com/zeronights-badge
  url: https://remontka.com/zeronights-badge/
  kind: website
images:
- file: assets/images/badges/zeronights-2016/zeronights-badge-zerobadge/80074a3e06.jpg
  source: "https://remontka.com/zeronights-badge/"
  credit: "remontka.com"
  caption: "Soldered ZeroNights Badge with the Blink program running"
contact: {}
notes:
- PCB badge shaped like the ZeroNights matryoshka-doll logo, functionally an Arduino Leonardo (ATmega32U4) board requiring attendee soldering, distributed at ZeroNights November 2016. Found by the event-year sweep, task con-phdays.
- Sweep's title matches the maker coverage's own name for the badge ("ZeroNights Badge" / "ZeroBadge"); no change needed.
status: listed
sources:
- kind: url
  url: https://remontka.com/zeronights-badge/
  title: ZeroNights Badge (ZeroBadge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-phdays); event read as ''ZeroNights 2016''.'
- kind: url
  url: https://remontka.com/zeronights-badge/
  title: ZeroNights Badge (ZeroBadge) - remontka.com
  accessed: '2026-09-08'
  note: 'Confirmed the badge is a matryoshka-shaped ATmega32U4/Arduino Leonardo board with a single SMD LED on pin 12, a micro-USB port, and 1x40 GPIO header; requires the attendee to hand-solder SMD parts; distributed at ZeroNights November 2016. No pricing, quantity, or open-source file links found. Image of a soldered, working unit saved from this page.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Only one source found (a Russian-language hobbyist writeup on remontka.com); could not confirm price, quantity made, availability today, or whether hardware/firmware files were ever published. No maker (ZeroNights) storefront, GitHub, or Hackaday page for this badge was located in searches. Colors and shape not confirmed from the text description alone (no clean photo of the unpopulated/painted PCB outline was available to judge solder-mask color).'
last_modified_date: '2026-09-08'
---

The ZeroNights Badge, also called the ZeroBadge, was handed out at ZeroNights 2016, a Russian information-security conference held in November 2016. Rather than a pre-built wearable, it is a bare PCB shaped like the conference's signature matryoshka-doll logo that is functionally an Arduino Leonardo board: it carries an ATmega32U4 microcontroller with a 16 MHz crystal, a micro-USB port for programming, a 1x40 GPIO header at 2.54mm spacing, and a single SMD LED wired to digital pin 12.

Attendees had to hand-solder the surface-mount components themselves before the badge would do anything, making it as much a soldering exercise as a badge. Coverage of the badge (a hobbyist writeup on remontka.com) shows a completed unit running a Blink-style LED demo, but notes that information about the badge from its creators was sparse and scattered; no pricing, production quantity, or design-file links were found in the available sources.
