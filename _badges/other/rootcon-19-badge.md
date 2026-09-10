---
title: ROOTCON 2025 Badge
id: other-rootcon-19-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: Electronic Cats
  url: https://electroniccats.com/
- name: ROOTCON
  url: https://www.rootcon.org/
summary: An interactive electronic badge designed by Electronic Cats for ROOTCON 19 (2025), the Philippines' largest hacking conference, built around a CH32V003 microcontroller with addressable RGB LEDs and a hidden Ping Pong minigame.
functions: 'Two-button interface: holding both buttons for half a second starts a Ping Pong game; single-button presses trigger other (undocumented) interactions; the badge also hides a secret message for attendees to find.'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
  - hardware tool
tech:
  mcu: CH32V003
  leds:
    count: null
    type: Neopixel
    note: Addressable RGB LEDs (WS2812-family/Neopixel), count not specified by the maker.
  display: none
  connectivity: []
  battery: 2x AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Distributed on-site at ROOTCON 19 (2025) check-in on a first-come, first-served basis; guaranteed for Human+ and Blackcard tier attendees. Other attendees received a simpler non-electronic "Type-B" fallback badge instead.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ROOTCONLabs/RC19/tree/main/hardware
  firmware_url: https://github.com/ROOTCONLabs/RC19/tree/main/firmware
  eda_tool: KiCad
  license: CERN-OHL-1.2 (hardware), GPL-3.0 (firmware)
  notes: Pre-built firmware binaries and hardware/firmware source archives are also mirrored at https://media.rootcon.org/ROOTCON%2019/Badge/.
links:
- label: badge.gallery/years/2025
  url: https://badge.gallery/years/2025
  kind: website
- label: ROOTCONLabs/RC19 (GitHub)
  url: https://github.com/ROOTCONLabs/RC19
  kind: repo
- label: ROOTCON 19 Badge media mirror
  url: https://media.rootcon.org/ROOTCON%2019/Badge/?C=M&O=A
  kind: fab
- label: ROOTCON official site
  url: https://www.rootcon.org/
  kind: website
images: []
contact: {}
notes:
- ROOTCON 19's electronic badge with a Type-B fallback design, per the badge.gallery compendium. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task general-2025.
status: released
sources:
- kind: url
  url: https://badge.gallery/years/2025
  title: ROOTCON 19 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2025); event read as ''ROOTCON 19 (2025)''.'
- kind: url
  url: https://github.com/ROOTCONLabs/RC19
  title: 'ROOTCONLabs/RC19: ROOTCON 2025 Badge'
  accessed: '2026-09-10'
  note: 'Maker''s own repo README: confirms maker (Electronic Cats, for ROOTCON), MCU (CH32V003), LEDs (Neopixels), battery (2x AAA), Ping Pong game, hidden message, and open-source hardware (CERN-OHL-1.2) + firmware (GPL-3.0) licensing.'
- kind: url
  url: https://media.rootcon.org/ROOTCON%2019/Badge/?C=M&O=A
  title: ROOTCON Media Server - ROOTCON 19 / Badge
  accessed: '2026-09-10'
  note: 'Mirror hosting firmware.zip and hardware.zip for the badge; no badge photos present in this directory.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed via the maker''s own GitHub repo (ROOTCONLabs/RC19) and ROOTCON''s media mirror, not just the badge.gallery snippet, so this is a real, documented item. No official photo of the assembled badge was found (GitHub repo has no images beyond schematics/PCB source files; badge.gallery pages carried no image either), so no images could be saved. LED count and any details of the "hidden message" or single-button interactions are not documented by the maker. No matching event id exists in _data/events.yml for ROOTCON, so event is left as "other"; this item was made for ROOTCON 19 (ROOTCON''s 2025 conference), Philippines. Title corrected from the sweep''s "ROOTCON 19 Badge" to the maker''s own repo title "ROOTCON 2025 Badge" (both names are used interchangeably by ROOTCON/Electronic Cats for the same event); original sweep wording kept in the notes list above. Distribution model (first-come at check-in, guaranteed for premium tiers, Type-B non-electronic fallback for others) corroborated by badge.gallery and a Philippine IT Security Forums Facebook post.'
last_modified_date: '2026-09-10'
---

The ROOTCON 19 badge is an interactive electronic badge that Electronic Cats designed for ROOTCON's 2025 conference, the Philippines' largest hacking event. Built around a CH32V003 microcontroller with Neopixel RGB LEDs and running off two AAA batteries, the badge doubles as a small game console: holding both of its buttons for half a second launches a Ping Pong minigame, while single-button presses trigger other interactions the maker left for attendees to discover, alongside a hidden message embedded somewhere in the badge's behavior.

Rather than being guaranteed to every attendee, the electronic badge was distributed first-come, first-served at on-site check-in, with Human+ and Blackcard tier attendees guaranteed one. Attendees who missed out received a simpler, non-electronic "Type-B" badge instead.

Both the hardware (KiCad source, released under CERN-OHL-1.2) and firmware (GPL-3.0) are open source, published in the `ROOTCONLabs/RC19` GitHub repository and mirrored, along with pre-built firmware binaries, on ROOTCON's own media server.

## Make your own

The badge ships with firmware pre-installed. To reflash it, download the binaries from the GitHub repo's releases section (or the `firmware.zip` on ROOTCON's media mirror) and flash them with a compatible programmer. To build custom firmware, the repository includes a guide in `firmware/README.md`. Hardware files (KiCad schematic, PCB layout, and footprints) are in the repo's `hardware/` folder.
