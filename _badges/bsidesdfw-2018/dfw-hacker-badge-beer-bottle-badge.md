---
title: DFW Hacker Badge (Beer Bottle Badge)
id: bsidesdfw-2018-dfw-hacker-badge-beer-bottle-badge
layout: badge
parent: BSides Dfw 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsidesdfw-2018
year: 2018
makers:
- name: alt_bier
  url: https://twitter.com/alt_bier
summary: A DIY, beer-bottle-shaped Arduino badge kit sold to raise money for BSidesDFW's 501(c)(3), with detailed build instructions and open Gerbers/code.
functions: Cycles RGB colors around the five LEDs on the star, chasing one LED at a time in the low-power default sketch (an alternate multi-LED sketch is also provided).
look:
  colors:
  - green
  - white
  shape: beer bottle
  themes:
  - beer
  - drink
  - learn to solder
  - kit
  - charity
tech:
  mcu: Arduino Nano
  leds:
    count: 5
    type: RGB
    note: 5mm 4-pin THT RGB LEDs (diffused or clear option); user-soldered.
  display: none
  connectivity: []
  battery: 2x CR2032 (in a 6V holder) or a 9V battery (optional)
  sao_version: none
get_one:
  price: $40 full kit / $20 PCB only (50% off for DFW-area early adopters)
  price_usd: 40
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - kit
  where: Sold in person at BSidesLV 2018, DEF CON 26 (Hardware Hacking Village), and BSidesDFW 2018 (which also ran a badge-building village); a local DFW meetup class was held ahead of summer camp.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/gowenrw/DFW_InfoSec_Badge_2018
  firmware_url: https://github.com/gowenrw/DFW_InfoSec_Badge_2018
  eda_tool: Fritzing
  notes: Single-layer PCB designed in Fritzing from an Illustrator-drawn SVG (board + silkscreen groups); Gerbers, financials, and two Arduino sketches (low-power single-LED chase and a brighter multi-LED version) are in the repo.
links:
- label: dfwhackerbadge.com
  url: https://dfwhackerbadge.com/
  kind: website
- label: www.youtube.com/watch?v=F5yX2TWvR1I
  url: https://www.youtube.com/watch?v=F5yX2TWvR1I
  kind: video
- label: gowenrw/DFW_InfoSec_Badge_2018 (GitHub)
  url: https://github.com/gowenrw/DFW_InfoSec_Badge_2018
  kind: repo
images:
- file: assets/images/badges/bsidesdfw-2018/dfw-hacker-badge-beer-bottle-badge/4f45c04c6d.jpg
  source: https://dfwhackerbadge.com/
  credit: alt_bier / gowenrw
  caption: DFW Hacker Badge banner image, beer-bottle-shaped PCB
- file: assets/images/badges/bsidesdfw-2018/dfw-hacker-badge-beer-bottle-badge/46aa39b8d5.jpg
  source: https://dfwhackerbadge.com/
  credit: alt_bier / gowenrw
  caption: 'Contents of the DIY badge kit: PCB, Arduino Nano, LEDs, resistors, lanyard, battery holder'
contact:
  handle: alt_bier
  url: https://twitter.com/alt_bier
notes:
- Independent (non-official) DIY educational badge sold to fund BSidesDFW's 501(c)(3), a beer-bottle-shaped single-layer PCB with a five-RGB-LED star used for soldering/Arduino classes at the con's Hardware Hacking Village, billed as the first DEF CON-scene indie badge. Found by the event-year sweep, task bsides-bsidesdfw.
- The sweep's sheet listed this only under BSidesDFW 2018; the maker's own site shows it was actually made for the whole 2018 "hacker summer camp" season and sold first at BSidesLV and DEF CON 26 before BSidesDFW that November. Kept the event as bsidesdfw-2018 per instructions since that is the entry's home event and the sheet's framing, with the wider run noted here.
status: listed
sources:
- kind: url
  url: https://dfwhackerbadge.com/
  title: DFW Hacker Badge (Beer Bottle Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsidesdfw); event read as ''BSides DFW 2018''.'
- kind: url
  url: https://dfwhackerbadge.com/
  title: DFW Hacker Badge
  accessed: '2026-09-10'
  note: Maker's own site; confirmed maker (alt_bier), 2018 sale at BSidesLV/DEFCON HHV/BSidesDFW, kit contents, price, Arduino Nano + 5 RGB LEDs, single-layer Fritzing PCB, open Gerbers and code on GitHub.
- kind: url
  url: https://github.com/gowenrw/DFW_InfoSec_Badge_2018
  title: gowenrw/DFW_InfoSec_Badge_2018
  accessed: '2026-09-10'
  note: Linked hardware/firmware repo confirmed from the maker's site; images and code files pulled from here.
- kind: url
  url: https://www.youtube.com/watch?v=F5yX2TWvR1I
  title: DFW Hackers Beer Bottle Badge Assembly
  accessed: '2026-09-10'
  note: Video title confirms it is an assembly walkthrough for this badge; full description/transcript was not accessible to extract further detail.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Quantity made is not stated anywhere found. Could not extract further detail from the YouTube assembly video beyond its title. Availability marked sold_out as a one-time 2018 charity kit sale with no ongoing storefront found.
last_modified_date: '2026-09-10'
model:
  file: assets/models/bsidesdfw-2018/dfw-hacker-badge-beer-bottle-badge.glb
  method: gerber
  source_file: gerber-export-06192018/DFW-InfoSec-Badge-2018-gerber-export-06192018.zip
  generated: '2026-09-10'
  bytes: 99648
  size_mm:
  - 69.4
  - 234.2
---

The DFW Hacker Badge is a DIY, beer-bottle-shaped circuit board designed by alt_bier (Robert Gowen) as a fundraiser and teaching tool for BSidesDFW, a 501(c)(3) nonprofit. Sold as an unassembled kit for $40 (or $20 for a bare PCB) during the 2018 "hacker summer camp" season, it was intended to teach basic soldering and Arduino development: buyers add their own Arduino Nano, five 5mm RGB LEDs, resistors, a lanyard, and a coin-cell battery holder to a single-layer green PCB shaped and silkscreened like a beer bottle (a nod to Rolling Rock). The stock firmware chases colors around the five LEDs arranged in a star on the badge face; an alternate, higher-power sketch lighting multiple LEDs at once is also included in the repo.

The badge was sold in person at BSidesLV and in the DEF CON 26 Hardware Hacking Village before reaching its home event, BSidesDFW 2018, where the maker ran a hardware hacking village with more in-depth PCB-to-assembly classes. A local DFW-area meetup class ahead of the summer con season let early buyers get kits at half price. All hardware (Fritzing source, Gerbers), firmware, and even a project financial breakdown are published on GitHub, along with companion beginner tutorials on soldering and Arduino programming hosted by the maker.

## Make your own

Gerber files, the Fritzing project, and two Arduino sketches (a low-power single-LED-at-a-time color walk, and a brighter multi-LED version) are in the [GitHub repo](https://github.com/gowenrw/DFW_InfoSec_Badge_2018). The maker's site walks through sourcing the PCB (single copper layer, no crossing traces), populating the Arduino Nano, resistors, and LEDs, wiring a coin-cell or 9V battery holder, and flashing the included code.
