---
title: Boozeboard - Alcohol Sensor SAO (DEF CON 30)
id: dc30-boozeboard-alcohol-sensor-sao-def-con-30
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: MakeItHackin
summary: A Talkboy-shaped SAO for DEF CON 30 "Homecoming" built around a real MQ303A alcohol sensor, with a breath-controlled game and a blinky "flashy badge" mode.
functions: 'Three modes: an alcohol sensor you blow into through a 3D-printed mouthpiece (entertainment only, not a real breathalyzer), a video game based on Tapper, and a "Flashy Badge" mode that blinks lights for walking around the con.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - drink
  - game
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
  distribution:
  - purchase
  where: Sold on Tindie by MakeItHackin (listing ID 27513).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/makeithackin/def-con-30-boozeboard-alcohol-sensor-sao
  url: https://www.tindie.com/products/makeithackin/def-con-30-boozeboard-alcohol-sensor-sao/
  kind: store
- label: github.com/MakeItHackin/DEFCON30SAO
  url: https://github.com/MakeItHackin/DEFCON30SAO
  kind: repo
- label: 'Hackster.io: Talkboy-Inspired Breathalyzer Badge Measures DEF CON Inebriation'
  url: https://www.hackster.io/news/talkboy-inspired-breathalyzer-badge-measures-def-con-inebriation-a1f22136ad30
  kind: article
- label: 'YouTube: Boozeboard v2 demonstration'
  url: https://youtu.be/6X5EPYohPvw
  kind: video
- label: 'YouTube: Boozeboard v1 demonstration'
  url: https://youtu.be/hNfToZ39VKg
  kind: video
images:
  - file: assets/images/badges/dc30/boozeboard-alcohol-sensor-sao-def-con-30/91b028b1ff.jpg
    source: "https://github.com/MakeItHackin/DEFCON30SAO"
    credit: "MakeItHackin"
    caption: "Boozeboard v2 SAO, Talkboy-shaped PCB"
  - file: assets/images/badges/dc30/boozeboard-alcohol-sensor-sao-def-con-30/ba38bbd9f1.jpg
    source: "https://github.com/MakeItHackin/DEFCON30SAO"
    credit: "MakeItHackin"
    caption: "Boozeboard v2 alcohol sensor mouthpiece in use"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/makeithackin/def-con-30-boozeboard-alcohol-sensor-sao/
  title: Boozeboard - Alcohol Sensor SAO (DEF CON 30)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc30''.'
- kind: url
  url: https://github.com/MakeItHackin/DEFCON30SAO
  title: 'GitHub: MakeItHackin/DEFCON30SAO'
  accessed: '2026-09-07'
  note: Maker's own repo; README describes features, versions (v1/v2 button difference), what's included, and links to demo videos. Only 3D-printed mouthpiece files and photos are published here, not PCB/firmware source.
- kind: url
  url: https://www.hackster.io/news/talkboy-inspired-breathalyzer-badge-measures-def-con-inebriation-a1f22136ad30
  title: 'Hackster.io: Talkboy-Inspired Breathalyzer Badge Measures DEF CON Inebriation'
  accessed: '2026-09-07'
  note: Press coverage confirming the DEF CON 30 "Homecoming" theme, Talkboy inspiration, and MQ303A sensor.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Tindie listing itself returned a Cloudflare bot-check page and could not be fetched directly; details came from the maker's GitHub README, web search summaries of the Tindie listing, and Hackster.io coverage. No source states the MCU, LED count/type, display, price, or quantity made, so those fields are left empty. The GitHub repo publishes only 3D-print files (mouthpiece STLs) and photos, not PCB design files or firmware, hence open_source is marked "partial" rather than "yes". Two hardware revisions exist (v1 has an unused "C" button, v2 replaced it with a "HEAT" button); this entry covers the SAO generally rather than one specific revision.
last_modified_date: '2026-09-07'
---

The Deluxe Boozeboard is an unofficial SAO made by MakeItHackin for DEF CON 30, whose theme that year was "Homecoming." The board is shaped like a Talkboy, the toy voice recorder from *Home Alone 2*, and leans into a broader 1990s nostalgia theme running through the maker's other DC30 pieces. At its core is a real MQ303A alcohol gas sensor: the wearer blows across it through a 3D-printed mouthpiece (with disposable sanitary covers included) to get a reading, though the listing is explicit that this is for entertainment and education only and not a real breathalyzer.

Beyond the sensor gimmick, the SAO doubles as a small game console, running a game based on the arcade classic *Tapper*, and has a "Flashy Badge" mode that blinks its lights for wandering the con floor. It connects to a host badge over a standard SAO header or can run independently from micro-USB power. Two hardware revisions were made: version 1 had an unused "C" button that version 2 replaced with a functional "HEAT" button (used to speed up the sensor's warm-up time).

MakeItHackin sold the Boozeboard on Tindie alongside their other DEF CON 30 badges and SAOs. The maker's GitHub repository for the DC30 lineup publishes the 3D-printable mouthpiece files and build photos, but not the PCB schematics or firmware, so the hardware is only partially open source.
