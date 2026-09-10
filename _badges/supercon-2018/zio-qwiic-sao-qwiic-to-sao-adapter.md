---
title: Zio-Qwiic-SAO — Qwiic to SAO adapter
id: supercon-2018-zio-qwiic-sao-qwiic-to-sao-adapter
layout: badge
parent: Supercon 2018
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2018
year: 2018
makers:
- name: ZIO.CC
  url: https://github.com/ZIOCC
summary: A small adapter board that lets a Qwiic (JST-SH) I2C module plug into a badge's SAO connector, and adds I2C pullup resistors for badges that lack them.
functions: Bridges the Qwiic I2C connector standard to the SAO connector standard so Qwiic sensor/LED modules can be plugged into any badge with an SAO header. Doubles as an I2C pullup-resistor adapter for badges missing them.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - i2c
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
  hardware_url: https://github.com/ZIOCC/Zio-Qwiic-SAO
  firmware_url: null
  eda_tool: Eagle
links:
- label: github.com/ZIOCC/Zio-Qwiic-SAO
  url: https://github.com/ZIOCC/Zio-Qwiic-SAO
  kind: repo
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/ZIOCC/Zio-Qwiic-SAO
  title: Zio-Qwiic-SAO — Qwiic to SAO adapter
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''Hackaday Supercon 2018''.'
- kind: url
  url: https://raw.githubusercontent.com/ZIOCC/Zio-Qwiic-SAO/master/README.md
  title: Zio-Qwiic-SAO README
  accessed: '2026-09-07'
  note: Confirmed purpose (Qwiic-to-SAO adapter, adds I2C pullups), event (Hackaday Supercon 2018), and maker phrasing.
- kind: url
  url: https://api.github.com/repos/ZIOCC/Zio-Qwiic-SAO
  title: ZIOCC/Zio-Qwiic-SAO repository metadata
  accessed: '2026-09-07'
  note: Confirmed MIT license; org ZIOCC has no listed website/topics in repo metadata.
- kind: url
  url: https://api.github.com/repos/ZIOCC/Zio-Qwiic-SAO/contents/Qwiic%20SAO
  title: Repository file listing (Qwiic SAO folder)
  accessed: '2026-09-07'
  note: Design files are Eagle format (.sch/.brd) plus full Gerbers and a BOM; no photos of the assembled board are included in the repo.
- kind: url
  url: https://api.github.com/orgs/ZIOCC
  title: ZIOCC GitHub organization profile
  accessed: '2026-09-07'
  note: Org blog links to Smart-Prototyping.com (Berlin/Shenzhen PCB/PCBA manufacturer); ZIO.CC appears to be a brand of that company, used here as the maker name.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No storefront, price, quantity made, or photos of the physical board were found anywhere (repo, GitHub org, or a general web check) — those fields are left empty rather than guessed. LED info in tech.leds left null: the README calls it "a fun little blinky adapter" but the repo does not specify an LED count or driver, and none is visible without a schematic read, so it is not stated with confidence. The web search budget for this session was exhausted after one query, so press coverage (Hackaday.com, forums, social posts) could not be checked; only the GitHub repo and org were verified.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2018/zio-qwiic-sao-qwiic-to-sao-adapter.glb
  method: kicad
  source_file: Qwiic_SAO.brd
  generated: '2026-09-10'
  bytes: 40860
---

The Zio-Qwiic-SAO is a small PCB adapter made by ZIO.CC for Hackaday Supercon 2018. It solves a simple compatibility problem: SparkFun's Qwiic ecosystem uses a 4-pin JST-SH connector for its plug-and-play I2C sensor and LED boards, while badge SAO headers use a different pinout. This adapter sits between the two, letting a Qwiic module plug into any badge's SAO connector. The README also notes it doubles as a way to add I2C pullup resistors to badges that were built without them.

The hardware is fully open source: the GitHub repository (ZIOCC/Zio-Qwiic-SAO) includes the Eagle schematic and board files, a full Gerber set, and a bill of materials, all released under the MIT license. No photos of the finished board, pricing, or distribution details were found in the repository or on the ZIOCC GitHub organization page, and a broader web search could not be completed in this session because the search budget was already exhausted, so those fields are left blank rather than guessed.

The ZIOCC GitHub organization's listed website points to Smart-Prototyping.com, a Berlin/Shenzhen-based PCB design, prototyping, and production company; ZIO.CC appears to be a project or product line associated with that company, though the repo itself does not spell out the relationship.
