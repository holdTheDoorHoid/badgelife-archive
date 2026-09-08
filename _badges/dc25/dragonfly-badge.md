---
title: Sympetrum v2 (Dragonfly Badge)
id: dc25-dragonfly-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: borgel
  url: https://github.com/borgel
summary: A self-powered blinky badge with 10 APA102C RGB LEDs whose patterns sync across nearby badges via an IR beacon, shaped like a dragonfly in homage to Neal Stephenson's "The Diamond Age."
functions: 'Plays ambient RGB color fades from an internal clock; beacons that clock and metadata over IR so nearby badges synchronize their color patterns to each other.'
look:
  colors: []
  shape: dragonfly
  themes:
  - sci-fi
  - wearable
tech:
  mcu: STM32F030x6
  leds:
    count: 10
    type: APA102C
    note: DotStar-compatible RGB LEDs, IR receiver mounted on the tail
  display: none
  connectivity:
  - ir
  battery: coin cell (custom-fit holder)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '106 units built (85 fully functional as of the DEF CON 25 badge meetup)'
  availability: sold_out
  distribution:
  - free_drop
  where: Given out at DEF CON 25 (2017); maker reported being "totally out" shortly after.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/borgel/sympetrum-v2
  firmware_url: https://github.com/borgel/sympetrum-v2/releases/tag/v4
  eda_tool: KiCad
  notes: 'License: MIT. Gerbers ("FF1.1") and BOM available via a Kitnic project page linked from the repo; alternate CPU STM32F051K8T6 documented as a substitute if the primary part is out of stock.'
links:
- label: hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  kind: article
- label: 'Hackaday: Badge From Diamond Age Comes To DEF CON'
  url: https://hackaday.com/2017/07/14/badge-from-diamond-age-comes-to-def-con/
  kind: article
- label: borgel/sympetrum-v2 (GitHub)
  url: https://github.com/borgel/sympetrum-v2
  kind: repo
images:
- file: assets/images/badges/dc25/dragonfly-badge/416782e347.jpg
  source: "https://hackaday.com/2017/07/14/badge-from-diamond-age-comes-to-def-con/"
  credit: "Hackaday / borgel"
  caption: "The Sympetrum (Dragonfly) badge, DEF CON 25"
contact: {}
notes:
- Independent blinky badge (106 units) at DEF CON 25 with IR sync between badges via a tail-mounted receiver. Found by the event-year sweep, task dc25-saos.
- 'The sweep''s title was "Dragonfly Badge"; the maker calls it "Sympetrum v2" (Sympetrum is a dragonfly genus) — retitled to carry both.'
- 'This appears to duplicate an existing entry: dc25-sympetrum-v2 (same maker, same badge). Flagged as duplicate_of in the research report; not merged or deleted here per the one-entry-per-task rule.'
status: released
sources:
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: Dragonfly Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc25-saos); event read as ''dc25''.'
- kind: url
  url: https://hackaday.com/2017/07/14/badge-from-diamond-age-comes-to-def-con/
  title: 'Badge From Diamond Age Comes To DEF CON'
  accessed: '2026-09-08'
  note: 'Confirms the badge''s origin, the Diamond Age theme, IR-sync behavior, and provides the source photo.'
- kind: url
  url: https://github.com/borgel/sympetrum-v2
  title: 'borgel/sympetrum-v2: A communicative piece of wearable electronics'
  accessed: '2026-09-08'
  note: 'Maker''s own repo: confirms this is the "final design used at DEFCON25," MCU (STM32F030x6, alt STM32F051K8T6), 10x APA102C LEDs, IR sync mechanism, MIT license, KiCad hardware files, firmware v4 release.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Maker''s own GitHub repo confirms all core facts. Price and exact battery cell type (only "custom-fit coin cell holder" per BOM notes, chemistry/size not stated) were not found and left empty. This entry duplicates dc25-sympetrum-v2 (same badge, same maker) — see duplicate_of in the report.'
last_modified_date: '2026-09-08'
---

The Sympetrum v2, better known by the sweep's working title "Dragonfly Badge," is an independent electronic badge borgel built for DEF CON 25 in 2017. It is a rewrite of an earlier, hastier build shown at DEF CON 24, and takes its shape and behavior from a scene in Neal Stephenson's *The Diamond Age*, where partygoers wear dragonfly pins that shift from random flickering into synchronized color as a crowd gathers. The badge does the same: ten APA102C RGB LEDs run gentle color fades driven by an internal clock, and a tail-mounted infrared receiver lets nearby badges beacon their clock and metadata to each other, pulling their patterns into sync when several are together.

106 units were built for the con, though only 85 were working by the Thursday-night badge meetup, with the rest reportedly being repaired in hotel rooms over the weekend; the maker later said they were "totally out." The board runs on an STM32F030x6 (an STM32F051K8T6 is documented as a drop-in substitute), and the full design — KiCad hardware files, gerbers, BOM, and firmware — is published under the MIT license on GitHub, with the firmware tagged as release "v4" and considered final for DEF CON 25.

This entry duplicates an existing archive entry, dc25-sympetrum-v2, for the same badge by the same maker.

## Make your own

Hardware and firmware are both open source. Gerbers (named "FF1.1") and a bill of materials are linked from the [GitHub repo](https://github.com/borgel/sympetrum-v2) via a Kitnic project page; the README recommends PCBWay, Seeed Studio, or Dirty PCBs for fabrication (roughly $25 for 10 boards), and notes that the APA102C LEDs are sometimes easier to source from Adafruit, eBay, or AliExpress than Digikey. The firmware release is tagged [v4](https://github.com/borgel/sympetrum-v2/releases/tag/v4).
