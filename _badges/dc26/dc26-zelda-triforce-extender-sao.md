---
title: Zelda Shitty Add-on Extender
id: dc26-dc26-zelda-triforce-extender-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: awkward intelligence
  url: https://hackaday.io/Awkwardai
summary: A Triforce-shaped shitty add-on (SAO) extender board from awkward intelligence's "Harbinger" collection made for DEF CON 26, distributed as a bare-PCB Gerber set with no schematic or firmware included.
functions: ''
look:
  colors: []
  shape: triforce
  themes:
  - pop culture
  - fantasy
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://cdn.hackaday.io/files/1599526843386368/shittytriforce.zip
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  kind: hackaday
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- label: hackaday.io/project/159952/files
  url: https://hackaday.io/project/159952/files
  kind: hackaday
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
images: []
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  title: The Harbinger Shitty Add-on Badges
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260505144653/https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
- kind: url
  url: https://hackaday.io/project/159952/files
  title: 'Project file listing: shittytriforce.zip'
  accessed: '2026-09-07'
  note: File entry names it "Zelda Shitty add-on extender," uploaded 2019-03-04, 233.52 kB zip.
  archived: https://web.archive.org/web/20260907115748/https://hackaday.io/project/159952/files
- kind: url
  url: https://cdn.hackaday.io/files/1599526843386368/shittytriforce.zip
  title: shittytriforce.zip (design file contents)
  accessed: '2026-09-07'
  note: Downloaded and listed archive contents to verify it is Gerber-only (no schematic/firmware); files are internally dated 2018-07-23, i.e. made just before DEF CON 26 (Aug 2018), confirming the event/year despite the later hackaday.io upload date.
  archived: https://web.archive.org/web/20260907115759/https://cdn.hackaday.io/files/1599526843386368/shittytriforce.zip
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check (2026-09-07): re-fetched both hackaday.io pages and re-downloaded shittytriforce.zip independently; all claims held up. The project page confirms Defcon 26 (2018) and awkward intelligence, and names the Gucci Mane tattoo badge, Shitty Calvin, Mr. Robopoly, Thereminion, and Galaxia as siblings in the same project, but indeed does not mention the Triforce piece by name. The files listing confirms shittytriforce.zip is titled "Zelda Shitty add-on extender," 233.52 kB, uploaded 2019-03-04. The zip itself contains exactly 9 Gerber/drill files (front/back copper, silkscreen, solder mask, edge cuts, drill map), all internally dated 2018-07-23, and the Gerber headers explicitly read "Created by KiCad (PCBNEW 4.0.7...)", directly confirming the eda_tool field. No schematic, BOM, or firmware present, supporting tech.mcu: none and make_your_own.open_source: partial. The parent "Harbinger Shitty Add-on Badges" project page (a DC26 badge-hacking roundup by awkward intelligence) does
    not mention the Triforce piece by name in its own description; it is known only from the file listing and archive contents. No maker photo of the assembled/populated board was found, and none is included in this entry. Price, quantity, and availability were not stated anywhere found and remain empty.'
last_modified_date: '2026-09-07'
---

This is a Triforce-shaped shitty add-on (SAO) board from awkward intelligence's "Harbinger" line of indie badges made for DEF CON 26 in 2018. It belongs to the same project as the maker's Gucci Mane-tattoo LED flasher, "Shitty Calvin," Mr. Robopoly, Thereminion, and the Galaxia prototyping board, though the Triforce piece itself isn't singled out in the project's own write-up - it's known only from a design-file archive, "shittytriforce.zip," that the maker added to the Hackaday.io project page in March 2019.

The archive contains only KiCad-style Gerber and drill files (front/back copper, silkscreen, solder mask, edge cuts, drill map) with no schematic, BOM, or firmware, so this appears to be a passive extender board rather than an active add-on with its own chip or LEDs. The Gerber files are internally dated July 23, 2018 - about two weeks before DEF CON 26 - which lines up with the rest of the Harbinger collection despite the later upload date.

## Make your own

The Gerbers are on Hackaday.io and can be sent straight to a PCB fab: [shittytriforce.zip](https://cdn.hackaday.io/files/1599526843386368/shittytriforce.zip). No schematic or bill of materials is included, so anyone recreating it would need to reverse-engineer the copper/silkscreen layers or treat it purely as a shaped, unpopulated extender PCB.
