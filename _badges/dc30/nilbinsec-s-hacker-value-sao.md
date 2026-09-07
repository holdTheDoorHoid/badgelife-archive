---
title: Hackr Value SAO
id: dc30-nilbinsec-s-hacker-value-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: NilbinSec
  url: https://github.com/NilbinSec
summary: NilbinSec's first badge, a simple SMD-soldering-practice SAO for DEF CON 30 with five LEDs arranged in a wrench outline that lights up as a "light tunnel" when filled with hot glue.
functions: No active logic; five LEDs light continuously when powered from the host badge's SAO connector (passive, no microcontroller). A hot-glue fill over the wrench-shaped silkscreen diffuses the LED light into a glowing outline.
look:
  colors: []
  shape: wrench
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: none
  leds:
    count: 5
    type: discrete
    note: 5 SMD LEDs and 2 SMD resistors, arranged around a wrench-shaped silkscreen outline; cathode orientation matters (all must point the same way or LEDs can burn out).
  display: none
  connectivity: []
  battery: null
  power: powered by host badge (3.3V via SAO VCC/GND)
  sao_version: v2
get_one:
  price: free
  price_usd: 0.0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Drop
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: A step-by-step assembly/build guide with photos is published, but no schematic, gerbers, or BOM files were found in the repo — only the written guide.
links:
- label: mobile.twitter.com/nilbinsec
  url: https://mobile.twitter.com/nilbinsec
  kind: social
- label: Hackr-Value-SAO-Build-Guide (GitHub)
  url: https://github.com/NilbinSec/Hackr-Value-SAO-Build-Guide
  kind: repo
images:
- file: assets/images/badges/dc30/nilbinsec-s-hacker-value-sao/357b89dd74.jpg
  source: "https://github.com/NilbinSec/Hackr-Value-SAO-Build-Guide"
  credit: "NilbinSec"
  caption: "Hackr Value SAO PCB with both SMD resistors soldered"
- file: assets/images/badges/dc30/nilbinsec-s-hacker-value-sao/51b513835e.jpg
  source: "https://github.com/NilbinSec/Hackr-Value-SAO-Build-Guide"
  credit: "NilbinSec"
  caption: "Finished Hackr Value SAO powered on, showing the hot-glue wrench light tunnel"
contact: {}
notes:
- Sheet listed this as "NilbinSec's Hacker Value SAO"; the maker's own repo and PCB silkscreen name it "Hackr Value" (title corrected to match; id/filename kept as imported).
- Awaiting final fab. Free drops. Will be announced on Twitter
sources:
- kind: sheet
  event: dc30
  row: 51
  updated: '2022-07-09'
- kind: url
  url: https://github.com/NilbinSec/Hackr-Value-SAO-Build-Guide
  title: Hackr-Value-SAO-Build-Guide (README)
  accessed: '2026-09-06'
  note: Confirmed real title, maker, DEF CON 30 origin, parts list (5 SMD LEDs, 2 SMD resistors, SAO connector), assembly steps, wrench-shaped light tunnel detail, and source images.
- kind: url
  url: https://github.com/NilbinSec
  title: NilbinSec (GitHub profile)
  accessed: '2026-09-06'
  note: Confirmed account identity and full list of NilbinSec's badge/SAO repos by year (no separate hardware-design repo exists for this SAO).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The maker's Twitter/X account (linked from the sheet) could not be fetched (redirects/paywalled). No schematic, gerbers, or BOM were published for this SAO, only a written build guide with photos, so make_your_own fields beyond that are left empty. PCB color/finish is not stated in any source and was left blank rather than guessed. Quantity made is not stated anywhere found.
last_modified_date: '2026-09-06'
---

NilbinSec's Hackr Value SAO was the maker's first badge project, made as a free drop for DEF CON 30 (2022) and distributed via the community badge sheet under the "Drop" heading. It's a deliberately simple, passive board aimed at people practicing SMD soldering: five surface-mount LEDs and two resistors wired straight to a six-pin SAO connector, with no microcontroller or active logic. The five LEDs sit around a wrench-shaped outline etched into the silkscreen.

The build guide (published on GitHub as "Hackr-Value-SAO-Build-Guide") walks through soldering the resistors, then the LEDs — warning that LED cathode orientation matters, since a reversed LED can burn out the rest of the string — followed by the through-hole SAO connector. As a finishing touch, the guide suggests filling the wrench outline on the back of the board with hot glue to create a diffused "light tunnel" effect when the SAO is powered from a host badge's 3.3V SAO header.

No schematic, gerber files, or bill of materials were found alongside the guide, so while the assembly process is fully documented, the design itself does not appear to have been published in an editable/fabricable form. Quantity made and final PCB color are not stated in any source found.
