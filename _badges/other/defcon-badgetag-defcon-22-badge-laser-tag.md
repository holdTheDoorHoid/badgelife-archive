---
title: defcon_badgetag — Defcon 22 badge laser tag
id: other-defcon-badgetag-defcon-22-badge-laser-tag
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2014
makers:
- name: mrisher
  url: https://github.com/mrisher
  role: firmware
- name: joshcano
  url: https://github.com/joshcano
  role: firmware
summary: A laser-tag firmware mod for the official DEF CON 22 "Human" conference badge, letting attendees "shoot" each other over IR and track hits/lives, built on top of the con's stock Propeller-based badge firmware.
functions: IR "shoot" and "hit" exchange between badges over the badge's built-in IR transmitter/receiver, LED animations (a "Cylon"/chaser-style floating-bit pattern) as feedback, and a life/score counter driven by touch-pad input.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: Parallax Propeller (P8X32A)
  leds:
    count: 8
    type: discrete
    note: 8 individually PWM-driven LEDs (LED0–LED7), not an addressable strip; driven via the jm_pwm8 Spin object.
  display: none
  connectivity:
  - ir
  inputs:
  - touch
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/mrisher/defcon_badgetag
  eda_tool: null
  notes: 'Only Spin source/binaries for the game logic are published; no PCB/hardware design files, since the game runs on the stock DEF CON 22 badge hardware rather than custom-built hardware.'
links:
- label: github.com/mrisher/defcon_badgetag
  url: https://github.com/mrisher/defcon_badgetag
  kind: repo
- label: github.com/joshcano/DEFCON_22_BADGE-_TAG
  url: https://github.com/joshcano/DEFCON_22_BADGE-_TAG
  kind: repo
images: []
contact: {}
notes:
- Runs on the official DEF CON 22 attendee badge hardware (Parallax Propeller-based, ~14,000 units made across 13 badge-type/color variants for DEF CON 22, August 2014); this project is a custom game firmware for that badge, not a separate physical badge or SAO.
status: released
sources:
- kind: url
  url: https://github.com/mrisher/defcon_badgetag
  title: defcon_badgetag — Defcon 22 badge laser tag
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 22''.'
- kind: url
  url: https://raw.githubusercontent.com/mrisher/defcon_badgetag/master/human_tag.spin
  title: human_tag.spin (dc22_badge_human.spin) source
  accessed: '2026-09-07'
  note: Primary source for MCU (Propeller), pin map (8 LEDs, 4 touch pads, IR in/out), and game logic (IR "blast" codes, animations, button-triggered actions); credits base badge firmware to Jon "JonnyMac" McPhalen and Ryan "1o57" Clarke, modified by mrisher/joshcano for the laser-tag game.
- kind: url
  url: https://github.com/joshcano/DEFCON_22_BADGE-_TAG
  title: joshcano/DEFCON_22_BADGE-_TAG
  accessed: '2026-09-07'
  note: Collaborator's own copy of the same badge-tag project; confirms co-authorship and that only firmware (Spin source and a compiled .binary) is distributed, no hardware files.
- kind: url
  url: https://www.parallax.com/defcon-22-conference-badge/
  title: DEFCON 22 Conference Badge - Parallax
  accessed: '2026-09-07'
  note: Confirms the underlying official DEF CON 22 badge is Propeller 1-based, with IR transmit/receive, touch-pad buttons and LEDs; ~14,000 boards made in 13 styles for August 2014.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No dc22/DEF CON 22 event id exists in _data/events.yml (the events list starts at dc24/2016), so event is left as "other" rather than corrected. This is a firmware modification of the stock official DEF CON 22 badge (not a standalone physical badge/SAO), so no images of a distinct physical item were found or saved — the hardware is the standard DC22 badge PCB, which this entry does not depict. Price, quantity, and distribution are not applicable/unknown since this was a free community firmware hack, not a sold item. Battery/power spec for the underlying DC22 badge was not confirmed in sources checked.'
last_modified_date: '2026-09-07'
---

`defcon_badgetag` is a custom game firmware built by mrisher and Josh Cano ("joshcano") for the official DEF CON 22 attendee badge, distributed to roughly 14,000 attendees in August 2014. The stock badge — designed and manufactured by Parallax around a Propeller 1 (P8X32A) microcontroller — already carried IR transmit/receive hardware, touch-pad buttons, and eight LEDs as part of DEF CON's annual badge hacking challenge. Rather than building new hardware, mrisher and joshcano rewrote the badge's Spin firmware (based on the original badge code by Jon "JonnyMac" McPhalen and Ryan "1o57" Clarke) into a laser-tag game: pressing different touch-pad combinations fires distinct IR "blast" codes at other badges, triggers LED chase/police-light animations, and other badges respond to being "hit" over IR.

The project is published as open-source Spin source (and, in joshcano's parallel repository, a compiled binary) under a permissive license, but only the game logic is shared — there are no PCB or hardware design files, since the badge hardware itself is Parallax's stock DEF CON 22 board rather than something the makers designed. No photos specific to this firmware mod (as opposed to generic photos of the stock DC22 badge) were found, so no images are attached to this entry.
