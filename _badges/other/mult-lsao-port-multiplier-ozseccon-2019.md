---
title: mult (LSAO port multiplier, OzSecCon 2019)
id: other-mult-lsao-port-multiplier-ozseccon-2019
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 2019
makers:
- name: digitalrane (ec0)
  url: https://github.com/digitalrane
summary: A small passive PCB that takes a single LSAO (Large SAO) connector and fans it out into five LSAO headers, letting one badge port drive multiple add-ons at once.
functions: 'No active function of its own: one LSAO input socket wired straight out to five LSAO output headers, so several SAOs/LSAOs can be chained or piggybacked off one badge port.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
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
  hardware_url: https://github.com/digitalrane/badgelife/tree/master/OzSecCon2019/mult
  firmware_url: null
  eda_tool: KiCad
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: listed
sources:
- kind: url
  url: https://github.com/digitalrane/badgelife/tree/master/OzSecCon2019/mult
  title: mult (LSAO port multiplier, OzSecCon 2019)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other''.'
- kind: url
  url: https://api.github.com/repos/digitalrane/badgelife/contents/OzSecCon2019/mult
  title: mult folder listing (GitHub API)
  accessed: '2026-09-07'
  note: Confirms the folder is KiCad-only (schematic, PCB, BOM, gerbers dir) with no README or firmware.
- kind: url
  url: https://raw.githubusercontent.com/digitalrane/badgelife/master/OzSecCon2019/mult/mult-BOM.csv
  title: mult-BOM.csv
  accessed: '2026-09-07'
  note: BOM lists only J1 (one LSAO PinSocket, 2x05) and J2-J6 (five LSAO PinHeaders, 2x05) - a passive 1-to-5 LSAO port splitter, no active components.
- kind: url
  url: https://github.com/digitalrane
  title: digitalrane (GitHub profile)
  accessed: '2026-09-07'
  note: 'Maker profile: handle digitalrane/ec0, based in Australia, personal site junkyard.systems; repo badgelife described as "ec0''s SAO/LSAO badge addons and resources for various hacker cons #badgelife" with an OzSecCon2019 folder.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No matching "ozseccon"/"OzSecCon" event id exists in _data/events.yml, so event is left as "other" with the con named here: OzSecCon 2019 (Australian security conference), per the repo folder path OzSecCon2019/mult. No photo of an assembled/populated board was found - only KiCad design files (schematic, PCB, BOM, gerbers directory) in the repo, so images could not be saved. Price, quantity made, and availability are not stated anywhere in the repo. tech.sao_version is left null: the top-level badgelife repo description mentions plans for future "SAO v1.69bis compatible" addons, but that is not stated for mult specifically, and the connector itself is LSAO (not SAO), so it was not assumed. confidence: medium because only the maker''s own repo/profile were available - no third-party coverage or photos were found.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/mult-lsao-port-multiplier-ozseccon-2019.glb
  method: kicad
  source_file: OzSecCon2019/mult/mult.kicad_pcb
  generated: '2026-09-10'
  bytes: 213992
---

"mult" is a bare-bones passive PCB by Australian maker digitalrane (handle ec0, github.com/digitalrane), made for OzSecCon 2019, part of their `badgelife` repo of SAO/LSAO badge addons for various hacker cons. Unlike most entries in this archive it isn't a badge or a standalone SAO with its own lights or microcontroller - it's strictly an adapter: one LSAO socket in, and five LSAO headers out, all wired directly together. In effect it turns a single LSAO port on a con badge into five, letting an attender stack or chain multiple SAOs/LSAOs off a badge that only has one connector.

The GitHub folder holds only KiCad design files - a schematic, PCB layout, a two-line bill of materials (one LSAO socket, five LSAO headers, nothing else), and an empty `gerbs` directory - with no README, no photos, and no firmware, since there is nothing to program. No price, production quantity, or distribution details are given anywhere in the repository, and no assembled-board photo could be found to illustrate the piece.

The event tag on this entry is left as "other" because the archive's controlled event list (`_data/events.yml`) has no entry for OzSecCon; the con itself is OzSecCon 2019, an Australian security conference, as read from the repository's folder path.
