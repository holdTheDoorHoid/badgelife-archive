---
title: DEF CON 30 Official Badge
id: dc30-badge-discussed-in-supercon-2022-badgelife-history-talk
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Michael Whiteley
  url: https://twitter.com/compukidmike
  role: MK Factor (with Katie Whiteley)
- name: Katie Whiteley
  role: MK Factor (with Michael Whiteley)
summary: The official DEF CON 30 conference badge, a musical instrument badge built around an RP2040 with a capacitive-touch keyboard, speaker, and microphone, made under severe chip-shortage constraints during 2021-2022.
functions: Plays built-in songs via a capacitive touch keyboard; records audio samples from an onboard microphone or line-in jack; acts as a class-compliant USB MIDI device when plugged into a computer, sending MIDI events for key presses; supports a self-test mode and USB-bootloader re-flashing via button combos at startup.
look:
  colors: []
  shape: null
  themes:
  - music
  - puzzle
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity:
  - usb
  - audio
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '25000'
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of DEF CON 30 (2022) as the official conference badge.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2023/03/03/supercon-2022-michael-whiteley-saves-the-badge
  url: https://hackaday.com/2023/03/03/supercon-2022-michael-whiteley-saves-the-badge/
  kind: article
- label: Tindie Blog - Badge Me if You Can - DEF CON 30
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  kind: article
- label: DEF CON 30 Badge Instructions (defcon.org)
  url: https://defcon.org/badge/30/
  kind: doc
- label: 'Supercon 2022: Michael Whiteley - "There''s No Rev 2: When Badgelife Goes Wrong" (YouTube)'
  url: https://www.youtube.com/watch?v=9v9v67Z7J6M
  kind: video
images:
- file: assets/images/badges/dc30/badge-discussed-in-supercon-2022-badgelife-history-talk/d590d4d7ac.jpg
  source: "https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/"
  credit: "MK Factor / Tindie Blog"
  caption: "The official DEF CON 30 badge, with its curved PCB face and capacitive touch keyboard"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.com/2023/03/03/supercon-2022-michael-whiteley-saves-the-badge/
  title: 'Supercon 2022: Michael Whiteley Saves The Badge'
  accessed: '2026-09-07'
  note: Covers the Supercon 2022 talk about DC30 badge manufacturing problems (audio amplifier BGA rework, 25,000-unit run, chip-shortage redesigns).
- kind: url
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  title: 'Tindie Blog: Badge Me if You Can - DEF CON 30'
  accessed: '2026-09-07'
  note: Describes the official DC30 badge's appearance (curved PCB face, capacitive touch keyboard, speaker/mic), maker (MK Factor / theMKFactor), and RP2040 chip; source of the badge photo.
- kind: url
  url: https://defcon.org/badge/30/
  title: DEF CON 30 Badge Instructions
  accessed: '2026-09-07'
  note: Official instructions confirming badge functions (audio playback, mic recording, line-in, USB MIDI, self-test and bootloader button combos) and the audio-loopback damage warning.
- kind: url
  url: https://www.youtube.com/watch?v=9v9v67Z7J6M
  title: 'Supercon 2022: Michael Whiteley - There''s No Rev 2: When Badgelife Goes Wrong'
  accessed: '2026-09-07'
  note: Talk video title/listing, confirming talk name and speaker; not watched in full.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This entry covers the official DEF CON 30 conference badge itself (made by MK Factor / Michael & Katie Whiteley), which the Hackaday article discusses via a Supercon 2022 retrospective talk about its manufacturing problems. Retitled from a generic "discussed in..." placeholder to "DEF CON 30 Official Badge" for clarity; original sheet title kept in the entry id/filename per instructions. LED count/type, display, price, and open-source status were not stated in any source checked and are left empty. Quantity (25,000) and the RP2040 MCU are the only hard technical facts found in sources actually read.
last_modified_date: '2026-09-07'
---

The DEF CON 30 (2022) conference badge, made by the husband-and-wife badgemaking team MK Factor (Michael and Katie Whiteley), is a musical-instrument badge built around a Raspberry Pi RP2040. Its face is a curved PCB insert that holds a pressure-connected speaker in place above a capacitive-touch keyboard; attendees could play built-in songs, record samples through an onboard microphone or a line-in jack, and the badge doubled as a class-compliant USB MIDI device when plugged into a computer. About 25,000 units were produced for the con.

The badge's story became notable less for its music features than for how it was built: MK Factor described DEF CON 30 as a "herculean project" completed during the 2021-2022 semiconductor shortage, with the design repeatedly reworked as different microcontrollers went in and out of stock before RP2040 supply held. A late substitution of the audio amplifier chip introduced a hardware flaw where looping the badge's audio output back into its own input, or shorting the audio jack (as could happen with certain lanyard clips), could permanently damage the tiny 1.5mm BGA-package amplifier. DEF CON's own badge instructions carry an explicit warning against this. The Hardware Hacking Village offered rework help for damaged units over the weekend. Michael Whiteley recounted this and other badge disasters in his Supercon 2022 talk "There's No Rev 2: When Badgelife Goes Wrong," which is the source this entry was originally logged from.
