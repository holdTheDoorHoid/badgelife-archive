---
title: Sympetrum (v1)
id: dc24-sympetrum-v1
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc24
year: 2016
makers:
- name: borgel
  url: https://github.com/borgel
summary: 'A dragonfly-shaped electronic pin, inspired by the cloisonne dragonfly pins in Neal Stephenson''s "The Diamond Age," that trades infrared beacons with nearby units to synchronize their light shows.'
functions: 'Runs an LED animation and, over IR, exchanges a periodic beacon with other Sympetrum pins in range so their animations sync to a shared clock; a lone pin instead plays randomized colors.'
look:
  colors: []
  shape: dragonfly
  themes:
  - animal
  - nature
tech:
  mcu: Cypress PSoC
  leds: null
  display: null
  connectivity:
  - ir
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
  hardware_url: https://upverter.com/borgel/748d5ee8f0eb00f8/sympetrum-v02/
  firmware_url: https://github.com/borgel/sympetrum
  eda_tool: null
links:
- label: github.com/borgel/sympetrum
  url: https://github.com/borgel/sympetrum
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: listed
sources:
- kind: url
  url: https://github.com/borgel/sympetrum
  title: sympetrum (v1)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc24''.'
- kind: url
  url: https://github.com/borgel/sympetrum
  title: 'borgel/sympetrum: HW documents and firmware for the Sympetrum pins'
  accessed: '2026-09-07'
  note: 'README confirms the concept (Diamond Age dragonfly pin, IR-synced light show), Cypress PSoC MCU, and points to hardware files hosted on Upverter (v0.2) with a note that "baked gerbers" were not yet available; commit history on this repo is dated August 2016 ("ks/fw-at-defcon" branch), consistent with DEF CON 24.'
- kind: url
  url: https://github.com/borgel/sympetrum-v2
  title: 'borgel/sympetrum-v2: A communicative piece of wearable electronics'
  accessed: '2026-09-07'
  note: 'Later, distinct hardware revision (STM32 + APA102 LEDs) covered separately; not used to fill v1 fields.'
- kind: url
  url: https://hackaday.com/2017/07/14/badge-from-diamond-age-comes-to-def-con/
  title: 'Badge From Diamond Age Comes To DEF CON'
  accessed: '2026-09-07'
  note: 'Covers the v2 hardware (STM32 driving ten APA102 modules) ahead of DEF CON 25 (2017); confirms the IR-sync concept and badgelife framing, but describes a later revision than this entry, so its LED/chip specifics were not applied to v1.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This entry is specifically the original "sympetrum" repo (no version suffix), which the maker''s own commit history (August 2016, branch "ks/fw-at-defcon") ties to DEF CON 24, matching the sheet''s event/year. The maker built at least two later, hardware-distinct revisions under separate repos (sympetrum-v2: STM32 + 10x APA102 LEDs, aimed at DEF CON 25/26; sympetrum-v3: described on GitHub as "the Dragonfly badge as seen at DEFCON26") -- those are different boards and were not used to fill this v1 entry''s tech/get_one fields, to avoid mixing revisions. LED count/type, display, battery, price, quantity, and availability for v1 specifically were not stated anywhere found and are left empty. Hardware files for v1 are on Upverter (labelled "sympetrum-v02" there, i.e. the v1 firmware pairs with a v0.2 board revision) with gerbers described in the README as "coming eventually" -- unclear if they were ever posted. No photo of the assembled pin was found; the repo includes only a schematic image, not a photo of the item.'
last_modified_date: '2026-09-07'
---

Sympetrum is a dragonfly-shaped electronic pin built by Kerry Scharfglass ("borgel"), inspired by the cloisonne dragonfly pins worn by partygoers in Neal Stephenson's novel *The Diamond Age*. Unlike the book's inert pins, this one is interactive: it runs its own LED light show and periodically beacons over infrared, listening for beacons from other Sympetrum pins nearby. When it hears one, it synchronizes its animation clock to it, so a lone pin cycles random colors while a group of them in the same room fall into a shared animation.

This entry covers the original hardware/firmware revision, built around a Cypress PSoC microcontroller. The maker's commit history for this repository is dated August 2016 on a branch named "ks/fw-at-defcon," which lines up with DEF CON 24. The firmware is open source in this repository; the matching board files were shared separately on Upverter (as "sympetrum-v02"), with the README noting that finished gerber files were not yet posted.

The maker went on to build at least two further, hardware-distinct versions of the badge -- sympetrum-v2 (an STM32 driving ten APA102 LEDs, covered by Hackaday ahead of DEF CON 25) and sympetrum-v3 (billed on GitHub as "the Dragonfly badge as seen at DEFCON26") -- which are different boards from this v1 and would need their own archive entries.
