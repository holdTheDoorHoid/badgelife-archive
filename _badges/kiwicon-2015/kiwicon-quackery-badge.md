---
title: Kiwicon Quackery Badge
id: kiwicon-2015-kiwicon-quackery-badge
layout: badge
parent: Kiwicon 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: kiwicon-2015
year: 2015
makers:
- name: Peter Fillmore
  url: http://www.peterfillmore.com/
summary: A duck-shaped LED party badge Peter Fillmore designed for Kiwicon 2015, notable for being laid out in PCBmodE (an SVG-based PCB tool) instead of a conventional EDA like KiCad or Eagle.
functions: A push button cycles through LED modes - a fast flashing "annoying" mode plus several solid-color modes - driven by a 3-pin charlieplexed "eye" LED and a set of additional charlieplexed 1206 LEDs.
look:
  colors: []
  shape: rubber duck
  themes:
  - duck
  - animal
tech:
  mcu: ATtiny85
  leds:
    count: null
    type: charlieplexed
    note: One 5050 LED used as a tri-color "eye" (charlieplexed across 3 pins for multiple color combinations) plus a number of 1206 LEDs charlieplexed for the flashing mode; exact LED count not stated by the maker.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/peterfillmore/kiwicon_badge
  firmware_url: https://github.com/peterfillmore/kiwicon_badge
  eda_tool: PCBmodE
  notes: PCB source (component footprints, placement/routing JSON, and outline) is under pcb/ in the repo; firmware (AVR C, built with the standard avr-gcc/avrdude toolchain) is under src/. The maker wrote up the full PCBmodE design process, including the JSON editing and SVG routing steps, in a blog post.
links:
- label: github.com/peterfillmore/kiwicon_badge
  url: https://github.com/peterfillmore/kiwicon_badge
  kind: repo
- label: 'peterfillmore.com: Designing a badge for Kiwicon in PCBmodE'
  url: http://www.peterfillmore.com/2015/12/designing-badge-for-kiwicon-in-pcbmode.html
  kind: article
images:
- file: assets/images/badges/kiwicon-2015/kiwicon-quackery-badge/9cc32c978e.jpg
  source: http://www.peterfillmore.com/2015/12/designing-badge-for-kiwicon-in-pcbmode.html
  credit: Peter Fillmore
  caption: PCBmodE render of the duck-shaped badge outline with components placed
- file: assets/images/badges/kiwicon-2015/kiwicon-quackery-badge/7b3dc01a76.jpg
  source: http://www.peterfillmore.com/2015/12/designing-badge-for-kiwicon-in-pcbmode.html
  credit: Peter Fillmore
  caption: Final gerber render of the duck-shaped PCB before sending to DirtyPCB for fabrication
contact: {}
notes:
- AVR-based Kiwicon badge project ('Kiwicon Quackery') by Peter Fillmore with PCB design and firmware source, exact edition year not confirmed within budget. Found by the event-year sweep, task con-kiwicon.
status: released
sources:
- kind: url
  url: https://github.com/peterfillmore/kiwicon_badge
  title: Kiwicon Quackery Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kiwicon); event read as ''Kiwicon''.'
- kind: url
  url: http://www.peterfillmore.com/2015/12/designing-badge-for-kiwicon-in-pcbmode.html
  title: 'Technical Bitlets: Designing a badge for Kiwicon in PCBmodE'
  accessed: '2026-09-08'
  note: 'Maker''s own build log: confirms Kiwicon 2015, ATtiny85, 5050+1206 charlieplexed LEDs, CR2032, PCBmodE (not KiCad/Eagle) as the EDA, DirtyPCB fab, duck-shaped outline inspired by a DC503 Defcon party badge, and the switch/reset-pin wiring mistakes made under time pressure.'
- kind: url
  url: https://api.github.com/repos/peterfillmore/kiwicon_badge
  title: kiwicon_badge repo metadata
  accessed: '2026-09-08'
  note: Repo created 2015-12-11, last pushed 2015-12-17, consistent with the Kiwicon 2015 (Dec 10-11) event date.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Event corrected from the generic "other" bucket to kiwicon-2015: the maker''s blog post (dated 16-17 Dec 2015, "<1 week to kiwicon") and the GitHub repo''s creation/push dates (11-17 Dec 2015) both line up with Kiwicon 2015 (Dec 10-11, Wellington NZ), not a later Kiwicon. README.md in the repo is a generic AVR-template boilerplate and gave no badge-specific facts; all functional/technical detail came from the maker''s blog post and src/main.c instead. Could not confirm: exact LED count, price, quantity made, or whether it was distributed beyond the maker''s own build - the blog post reads as a single one-off build for personal use at the con, with no mention of a batch or giveaway, so get_one fields are left unknown rather than guessed. The maker credits the circuit as adapted from a DC503 (Defcon) party badge designed by @securelyfitz, which may be worth its own entry (see other_items_found).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/kiwicon-quackery-badge/
model:
  file: assets/models/kiwicon-2015/kiwicon-quackery-badge.glb
  method: gerber
  source_file: pcb/production
  generated: '2026-09-10'
  bytes: 138872
  size_mm:
  - 100.0
  - 87.7
---

Peter Fillmore built the "Kiwicon Quackery" badge for Kiwicon 2015 in Wellington, New Zealand, as a personal side project to try PCBmodE - an SVG-based PCB design tool from Boldport's Saar Drimer - instead of a conventional EDA like KiCad or Eagle. The result is a small ATtiny85-powered LED badge laid out in the shape of a rubber duck, running on a CR2032 coin cell. A push button cycles through a fast, "obnoxious" flashing mode and several solid-color modes, driven by a 5050 LED wired as a charlieplexed tri-color "eye" plus a handful of charlieplexed 1206 LEDs.

Fillmore has said he based the circuit on a Defcon party badge that Chicago-area group DC503 had handed out, designed by @securelyfitz and also built around an ATtiny85. He ordered parts from Alibaba and had DirtyPCB fabricate the duck-shaped boards, assembling and debugging the first unit in the week before the con - in the process discovering he'd wired the mode button to the chip's reset pin (and wired it normally-closed), which he patched with bodge wires rather than a respin.

Both the PCB source (as PCBmodE's JSON/SVG design files) and the AVR firmware are published on GitHub. The build is documented start-to-finish in Fillmore's own blog post, which walks through footprint creation, component placement, hand-routing in an SVG editor, and Gerber generation for DirtyPCB - useful as a rare public example of a badge designed outside the usual KiCad/Eagle toolchain.

## Make your own

The `pcb/` folder of the [GitHub repo](https://github.com/peterfillmore/kiwicon_badge) holds the PCBmodE component and routing JSON for the duck-shaped board; `src/main.c` holds the ATtiny85 firmware, built with the standard `gcc-avr`/`avr-libc`/`avrdude` toolchain (`make` to build, `make flash` to program over an Arduino-as-ISP or similar). PCBmodE itself, and the JSON-editing/SVG-routing workflow needed to modify the board, are documented in Fillmore's blog post above.
