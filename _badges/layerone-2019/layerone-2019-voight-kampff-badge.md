---
title: LayerOne 2019 Voight-Kampff Badge
id: layerone-2019-layerone-2019-voight-kampff-badge
layout: badge
parent: LayerOne 2019 (Blade Runner theme)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: layerone-2019
year: 2019
makers:
- name: LayerOne / null space labs
  url: https://github.com/charlie-x/layerOne2019
  role: charlie-x (design/firmware)
summary: The LayerOne 2019 attendee badge, a Blade Runner-themed take on the Voight-Kampff machine with a ring of orange LEDs under a clear dome and an optional ESP32-CAM eye-scanning add-on.
functions: Cycles LED lighting patterns (orange ring plus blue/red blink) evoking the Voight-Kampff prop; an optional M5Stack ESP32-CAM module pairs with a companion iOS app to do live eye detection and overlay the movie's UI on a phone screen. A separate "logo kit" add-on is an SMD soldering challenge built around an ATtiny2313 in QFN.
look:
  colors:
  - black
  - orange
  shape: circle
  themes:
  - movie
  - sci-fi
  - security
tech:
  mcu: ATtiny2313
  leds:
    count: 6
    type: discrete
    note: Six orange LEDs under a clear dome plus separate blue and red indicator LEDs; a side-emitting LED strip lights the "LAYERONE2019" logo.
  display: none
  connectivity: []
  battery: 18650 Li-ion cell (with an APM4953 dual MOSFET protection circuit)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to LayerOne 2019 attendees; the ESP32-CAM eye-recognition add-on and the ATtiny2313 logo-LED soldering kit were separate builds available at the con.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/charlie-x/layerOne2019
  eda_tool: null
  notes: 'The GitHub repo (MIT licensed) has the ESP32-CAM add-on firmware and pinout notes ("firmware" folder, kitbadge L1 LOGO); it does not include the main badge''s board files or a stated EDA tool.'
links:
- label: hackaday.com/2019/06/04/hunting-replicants-with-the-2019-layerone-badge
  url: https://hackaday.com/2019/06/04/hunting-replicants-with-the-2019-layerone-badge/
  kind: article
- label: github.com/charlie-x/layerOne2019
  url: https://github.com/charlie-x/layerOne2019
  kind: repo
images:
- file: assets/images/badges/layerone-2019/layerone-2019-voight-kampff-badge/a6bb9a77a3.jpg
  source: "https://hackaday.com/2019/06/04/hunting-replicants-with-the-2019-layerone-badge/"
  credit: "LayerOne / Hackaday"
  caption: "LayerOne 2019 badge with lit LAYERONE2019 logo LED strip"
- file: assets/images/badges/layerone-2019/layerone-2019-voight-kampff-badge/bedc2df60a.jpg
  source: "https://hackaday.com/2019/06/04/hunting-replicants-with-the-2019-layerone-badge/"
  credit: "LayerOne / Hackaday"
  caption: "Reverse side of the LayerOne 2019 badge showing the ATtiny2313 and components"
contact: {}
notes:
- Blade Runner-themed badge modeled on the Voight-Kampff machine with an optional eye-recognition camera add-on. Found by the event-year sweep, task con-layerone.
- Title matches the sweep's wording; Hackaday's own headline just calls it "the 2019 LayerOne badge" and does not use "Voight-Kampff Badge" as a formal product name, but the badge is explicitly modeled on the Voight-Kampff machine prop from Blade Runner, so the descriptive title is kept.
status: released
sources:
- kind: url
  url: https://hackaday.com/2019/06/04/hunting-replicants-with-the-2019-layerone-badge/
  title: LayerOne 2019 Voight-Kampff Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''LayerOne 2019''.'
- kind: url
  url: https://hackaday.com/2019/06/04/hunting-replicants-with-the-2019-layerone-badge/
  title: "Hunting Replicants With The 2019 LayerOne Badge - Hackaday"
  accessed: '2026-09-08'
  note: 'Primary source for badge description: ATtiny2313 MCU, 18650 battery, orange LED ring, optional ESP32-CAM eye-detection add-on with companion iOS app, ATtiny2313 QFN soldering kit, and photos.'
- kind: url
  url: https://github.com/charlie-x/layerOne2019
  title: charlie-x/layerOne2019 (GitHub)
  accessed: '2026-09-08'
  note: 'MIT-licensed repo with firmware for the ESP32-CAM add-on and pinout notes; confirms charlie-x as the badge''s designer/firmware author within LayerOne/null space labs.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (theme, MCU, battery, LED layout, camera add-on, iOS companion app) come from the Hackaday writeup, which is thorough but is press coverage rather than a maker post. The linked GitHub repo (charlie-x/layerOne2019) confirms the add-on firmware and MIT license but does not include the main badge board files, a stated EDA tool, price, or production quantity, so those fields are left empty. No separate maker storefront or Hackaday.io project page was found.'
last_modified_date: '2026-09-08'
---

The LayerOne 2019 conference badge riffed on the Voight-Kampff machine from *Blade Runner*, the film's fictional device for detecting replicants through pupil response. The badge itself is a black PCB built around an ATtiny2313, running on an 18650 lithium-ion cell, with six orange LEDs arranged under a clear dome alongside separate blue and red indicator LEDs, plus a side-emitting LED strip that lights up the "LAYERONE2019" logo. It was handed out to attendees as the standard con badge.

For attendees who wanted to lean further into the theme, LayerOne also offered an optional add-on: an M5Stack ESP32-CAM module, mounted to the badge with a 3D-printed bracket, paired with a companion iOS app that ran live eye detection and overlaid a Voight-Kampff-style interface over the camera feed — turning the wearer into an impromptu replicant-hunting rig. A separate soldering challenge kit was also available, built around the same ATtiny2313 chip in its harder-to-hand-solder QFN package, driving the logo LED strip.

Firmware for the ESP32-CAM add-on, along with pinout notes, is published under an MIT license in charlie-x's `layerOne2019` GitHub repository, tying the build to null space labs' longtime work on LayerOne's badges. The main badge's board files, price, and production numbers were not found in the sources checked.
