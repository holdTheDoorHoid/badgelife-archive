---
title: SAO_BadgePirates
id: other-sao-badgepirates
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2021
makers:
- name: BadgePirates
  url: https://www.badgepirates.com
summary: A set of SAO add-ons ("SVG2Shenzen" board design) that BadgePirates designed for BSides KC 2021, distributed alongside their main BSides KC 2021 conference badge.
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
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
  open_source: true
  hardware_url: https://github.com/BadgePiratesLLC/SAO_BadgePirates
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/BadgePiratesLLC/SAO_BadgePirates
  url: https://github.com/BadgePiratesLLC/SAO_BadgePirates
  kind: repo
- label: badgepirates.com
  url: https://www.badgepirates.com
  kind: website
  archived: https://web.archive.org/web/20260810184033/https://badgepirates.com/
images:
- file: assets/images/badges/other/sao-badgepirates/17a45a0420.png
  source: https://www.badgepirates.com
  credit: BadgePirates
  caption: BSides KC 2021 SAOs
  archived: https://web.archive.org/web/20260810184033/https://badgepirates.com/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/BadgePiratesLLC/SAO_BadgePirates
  title: SAO_BadgePirates
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/BadgePiratesLLC/SAO_BadgePirates
  title: SAO_BadgePirates (BadgePiratesLLC/SAO_BadgePirates repo)
  accessed: '2026-09-07'
  note: KiCad project and gerbers named "Bsides-KC-2021-SAO-BP" and "SVG2Shenzen v1_00"; README empty; repo archived. Confirms hardware is open source (KiCad schematic, PCB, and gerbers present) but no firmware repo linked.
- kind: url
  url: https://github.com/BadgePiratesLLC
  title: BadgePiratesLLC (GitHub org)
  accessed: '2026-09-07'
  note: Org description "Making Badges for Fun not Profit", MidWest-based, contact admin@badgepirates.com, website badgepirates.com.
  archived: https://web.archive.org/web/20260523082542/https://github.com/BadgePiratesLLC
- kind: url
  url: https://www.badgepirates.com
  title: Badge Pirates
  accessed: '2026-09-07'
  note: Portfolio gallery includes a "BSides KC 2021 SAOs" entry (image BSidesKC21_SAOs.png) alongside a separate "BSides KC 2021 Badge" main badge entry, confirming the SAO was made for BSides KC 2021. No price, quantity, or technical spec details given on the page.
  archived: https://web.archive.org/web/20260810184033/https://badgepirates.com/
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all four cited sources directly. GitHub repo confirmed archived, README confirmed genuinely empty (just an "# SAO_BadgePirates" heading), repo contains exactly one KiCad PCB project (Bsides-KC-2021-SAO-BP.kicad_pcb/.sch/.pro/.prl, one footprint library folder named "...SVG2Shenzen v1_00.pretty", a gerbers folder) and no firmware, matching the open_source/eda_tool/hardware_url fields. Org page and badgepirates.com both confirmed as described. One inaccuracy found and corrected: the prior summary/body called this "a pair of SAO add-ons," but the site''s own gallery caption is plural ("BSides KC 2021 SAOs") and its photo (assets/images/badges/other/sao-badgepirates/17a45a0420.png) shows at least 7-8 distinct role-labeled variants (Sponsor, Village, Organizer, Participant, Speaker, Volunteer, Badge Pirates, plus a differently-shaped "RF Village" piece), not two — "pair" was unsupported and has been replaced with "set"/"variants" language grounded
    in the photo. No matching "BSides KC" event exists in _data/events.yml, so event is correctly left as "other"; the con is BSides KC 2021, noted here and in the body for a future event addition. No Hackaday.io page, store listing, price, or quantity was found anywhere, so those fields correctly stay empty.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/sao-badgepirates.glb
  method: kicad
  source_file: Bsides-KC-2021-SAO-BP.kicad_pcb
  generated: '2026-09-10'
  bytes: 37800
---

BadgePirates is a Midwest-based, non-profit badge-making collective ("Making Badges for Fun not Profit") that has designed 60+ conference badges since 2016, including this SAO add-on made for BSides KC 2021. The badgepirates.com gallery photo for this entry shows several role-labeled variants (e.g. Sponsor, Organizer, Participant, Speaker, Volunteer, plus a separately shaped "RF Village" piece) built around the same design, distributed to go with BadgePirates' main BSides KC 2021 conference badge that year. The GitHub repo's KiCad project is named "Bsides-KC-2021-SAO-BP", with a sub-library called "SVG2Shenzen v1_00".

The GitHub repository (now archived) publishes the full open-source KiCad hardware design: schematic, PCB layout, and manufacturing gerbers, but its README is empty and no firmware or write-up describing the SAO's actual function, LEDs, or chip was found, so most technical fields are left blank rather than guessed. No BSides KC event exists yet in the archive's event list, so this entry stays filed under "other" with BSides KC 2021 noted here; a future event addition for BSides KC would let this be re-filed.
