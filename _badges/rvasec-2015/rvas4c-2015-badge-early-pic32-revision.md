---
title: RVAs4c 2015 Badge ("early" PIC32 revision)
id: rvasec-2015-rvas4c-2015-badge-early-pic32-revision
layout: badge
parent: RVAsec 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2015
year: 2015
makers:
- name: HackRVA (Paul Bruggeman)
summary: 'A hand-assembled, hand-soldered RVAsec 2015 conference badge built around a PIC32 MCU, with capacitive touch sliders, IR Tx/Rx, and an LCD.'
functions: 'Runs a state-machine "app/stage" firmware framework; planned uses included IR badge-to-badge messaging, on-badge games/apps, and tie-ins with the RVAsec CTF, though the touch, IR, and graphics support were still under active development at release.'
look:
  colors: []
  shape: null
  themes: [security, hardware tool]
tech:
  mcu: PIC32MX250128D
  leds:
    count: 1
    type: RGB
    note: ''
  display: LCD
  connectivity: [usb, ir]
  inputs: [buttons, touch, capacitive]
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: '~350'
  availability: sold_out
  distribution: [free_drop]
  where: 'Given to RVAsec 2015 attendees; roughly 350 units were hand-assembled by HackRVA volunteers at pick-and-place/reflow build sessions ahead of the conference.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HackRVA/rvasec-badge-2015-early
  eda_tool: null
links:
- label: github.com/HackRVA/rvasec-badge-2015-early
  url: https://github.com/HackRVA/rvasec-badge-2015-early
  kind: repo
- label: 'RV4sec 2015 Badge Build (rvasec.com)'
  url: https://rvasec.com/rv4sec-2015-badge-build/
  kind: article
- label: 'Badge - hack.RVA'
  url: https://www.hackrva.org/badge/
  kind: website
images: []
contact: {}
notes:
- 32-bit PIC32MX250128D based badge with capacitive touch sliders, IR Tx/Rx, USB, and buttons, documented on the HackRVA GitHub org and rvasec.com build-update post; not present in the badge.gallery RVAsec credits list. Found by the event-year sweep, task con-rvasec.
status: released
sources:
- kind: url
  url: https://github.com/HackRVA/rvasec-badge-2015-early
  title: RVAs4c 2015 Badge ("early" PIC32 revision)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2015''.'
- kind: url
  url: https://github.com/HackRVA/rvasec-badge-2015-early
  title: 'HackRVA/rvasec-badge-2015-early README (dev branch)'
  accessed: '2026-09-08'
  note: 'Confirmed maker (Hack.RVA), MCU (PIC32MX250128D), feature list (2 capacitive touch sliders, IR Tx/Rx, 1 RGB LED, USB, RTC, LCD, speaker, momentary button); README notes hardware TODOs (schematics/BOM not yet posted at this stage) and that this early revision was developed while the badge was "still working out some of the features."'
- kind: url
  url: https://rvasec.com/rv4sec-2015-badge-build/
  title: 'RV4sec 2015 Badge Build - RVAsec'
  accessed: '2026-09-08'
  note: 'HackRVA''s Paul Bruggeman describes the physical build: fiberglass PCB, ~50 parts mostly SMD, solder-paste stencil + volunteer pick-and-place, reflow in donated toaster ovens, hand-soldered IR Tx/Rx, piezo buzzer, USB connector and LCD; approximately 350 badges assembled with a dozen-plus volunteers. No price or "early vs. later revision" distinction is made in the post itself.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: >-
    Confirmed via HackRVA's own GitHub org and the rvasec.com build write-up: this is a real, distributed
    badge (not just a sweep snippet). The GitHub org also holds a second, separately-named repo,
    "rvasec-badge-2015" (no "-early" suffix), with an apparently identical README/feature list; it's unclear
    whether that is a later production revision, a renamed fork, or the same project mirrored under two repo
    names -- reported separately rather than guessed at here. Hardware design files (schematics/BOM) were
    listed as outstanding TODOs in the README at the point captured, so make_your_own.hardware_url is left
    empty and open_source is marked "partial" (firmware only, confirmed). No maker photos of the assembled
    board were found on the pages checked (the hack.RVA badge-page photos are capitioned as general/2020-era
    build photos, not identified as the 2015 badge specifically), so no images were saved. Price was not
    stated anywhere; badges were given to conference attendees rather than sold, so get_one.price is set to
    "free" and price_usd to 0 on that basis.
last_modified_date: '2026-09-08'
---

RVAs4c 2015 was the conference badge for RVAsec 2015, designed and built by the Richmond, VA hackerspace HackRVA (with Paul Bruggeman leading development). It's built around a 32-bit Microchip PIC32MX250128D microcontroller and adds two linear capacitive touch sliders, infrared transmit/receive, a single RGB LED, USB, a real-time clock, an LCD, a small speaker, and a momentary button. This repository, `rvasec-badge-2015-early`, captures an early development snapshot of that badge, built while the team was still finalizing touch, IR, and graphics support -- the README notes they were developing against the prior year's (2014) badge hardware in the meantime.

Roughly 350 badges were hand-assembled by more than a dozen HackRVA volunteers ahead of the conference: copper etched with ferric chloride, solder paste applied through stencils, parts placed at a volunteer "pick and place" session, and reflowed in donated toaster ovens, with the IR transmitter/receiver, piezo buzzer, USB connector, and LCD hand-soldered afterward. Badges were given to attendees rather than sold.

The firmware is open source on GitHub, built with MPLAB X and the MPLAB XC32 compiler, and includes a bootloader (entered by holding the badge's button while plugging in USB) so badges could be reflashed without dedicated programming hardware. Hardware design files (schematics, BOM) were still listed as open TODOs in the README captured here, so it's unclear whether they were ever published for this specific revision.

