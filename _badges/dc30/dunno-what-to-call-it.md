---
title: Dunno what to call it...
id: dc30-dunno-what-to-call-it
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Aerospace Village
  url: https://aerospacevillage.org/
summary: A modular aerospace/space-themed SAO badge from DEF CON 30's Aerospace Village, built as a base "sky" board plus three included SAOs (space shuttle, WARNING tag, REMOVE BEFORE FLIGHT tag) that plug into five onboard SAO ports.
functions: 'LED-lit sky/horizon scene on the base board; a 2D Aztec barcode on the back encodes Buzz Aldrin''s "boarding pass to the moon" as a solvable puzzle (Aerospace Village reported 37 solvers).'
look:
  colors:
  - black
  - blue
  - green
  - red
  - white
  - silver
  shape: arc
  themes:
  - space
  - sci-fi
  - puzzle
  form_factor: pcb badge
tech:
  mcu: null
  leds:
    count: null
    type: null
    note: Blue LEDs visible along the horizon/sky boards in maker photos; exact count and part not stated.
  display: null
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Aerospace Village''s own site states "The 2022 Aerospace Village Badge are gone!" (checked 2026-09-06).'
  distribution:
  - village
  where: DEFCON, in person at the Aerospace Village
make_your_own:
  open_source: yes
  hardware_url: https://github.com/AerospaceVillage/avBadge_2022
  firmware_url: https://github.com/AerospaceVillage/avBadge_2022
  eda_tool: null
  notes: Repo README describes it as "a collection of v1.69 SAO badges" and mentions sending the space/earth board sections to JLCPCB with SMT assembly. Additional SAO designs in the repo (a 787 logo, space shuttle, SR-71, James Webb Telescope) beyond the three that shipped with the base badge.
links:
- kind: website
  label: DC30 Badge — Aerospace Village
  url: https://www.aerospacevillage.org/dc30-badge
- kind: repo
  label: avBadge_2022 (GitHub)
  url: https://github.com/AerospaceVillage/avBadge_2022
images:
- file: assets/images/badges/dc30/dunno-what-to-call-it/13fcd5495b.jpg
  source: "https://www.aerospacevillage.org/dc30-badge"
  credit: "Aerospace Village"
  caption: "Aerospace Village DEF CON 30 badge: base sky/horizon board with control-tower silhouette, plus the included space-shuttle, WARNING, and REMOVE BEFORE FLIGHT SAOs"
contact: {}
notes:
- I have only seen pictures...no details sent to me yet
- 'Sheet title carried over unchanged; the maker''s own site does not give the badge a distinct product name beyond "DC30 Badge."'
status: released
sources:
- kind: sheet
  event: dc30
  row: 35
  updated: '2022-07-17'
- kind: url
  url: https://www.aerospacevillage.org/dc30-badge
  title: DC30 Badge | Aerospace Village
  accessed: '2026-09-06'
  note: Maker's own page describing the badge, its three included SAOs, the five-port base board, the Aztec-code puzzle, distribution, and designer credits.
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2022
  title: AerospaceVillage/avBadge_2022
  accessed: '2026-09-06'
  note: Hardware-files repo; README confirms "v1.69 SAO badges" and JLCPCB fabrication with SMT assembly; contains additional unreleased SAO designs.
- kind: url
  url: https://aerospacevillage.org/badgelife/
  title: Badgelife | Aerospace Village
  accessed: '2026-09-06'
  note: Gallery page listing DC28-DC33 Aerospace Village badges, linking to the DC30 badge page and its thumbnail image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'Core facts (theme, base board + 3 SAOs, 5 SAO ports, v1.69 SAO standard, distribution at DEF CON 30, the Aztec-code puzzle) come from the maker''s own site and GitHub repo. Chip/MCU, LED part and exact count, price, and quantity made are not stated anywhere found and are left empty. No maker-given product name beyond "DC30 Badge" was found, so the sheet''s placeholder title was kept.'
last_modified_date: '2026-09-06'
---

The Aerospace Village's DEF CON 30 badge is a modular, aerospace-themed SAO set rather than a single fixed board. The base piece is a half-dome "sky" board — a starfield and constellations up top, a blue daytime sky with clouds below, and a green ground strip with an air-traffic-control-tower silhouette at the bottom — lit with blue LEDs and carrying five SAO headers. It shipped with three matching SAOs: a die-cut NASA space shuttle, a gold "WARNING" tag, and a red "REMOVE BEFORE FLIGHT" tag, the last two nodding to real aviation ground-safety streamers. The GitHub repo for the project also contains several additional SAO designs (a Boeing 787 logo, an SR-71, the James Webb Space Telescope) that appear to have been designed but not confirmed as part of the badges actually handed out.

Beyond the light show, the badge carried a puzzle: the back of a board encoded Buzz Aldrin's "boarding pass to the moon" as a 2D Aztec barcode, which the Village later said 37 attendees solved. The badges were built and distributed in person at DEF CON 30's Aerospace Village and, per the Village's own site, are no longer available. Hardware files are published on GitHub (design credited to @cybertestpilot with artwork from flysurreal.com), and the README notes the space/earth board sections were fabricated through JLCPCB with SMT assembly, but no chip, LED part, price, or production-quantity details were found in any source checked.
