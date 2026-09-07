---
title: vecdec (Vecdeck)
id: dc34-vecdec-vecdeck
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: svenscore
summary: ''
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/svenscore/vecdec
  url: https://github.com/svenscore/vecdec
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: not_an_item
sources:
- kind: url
  url: https://github.com/svenscore/vecdec
  title: vecdec (Vecdeck)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''DEF CON 34 (per a cyberdeck-competition mention; not confirmed as a con badge sheet item)''.'
- kind: url
  url: https://github.com/svenscore/vecdec
  title: vecdec (Vecdeck) README
  accessed: '2026-09-07'
  note: 'Confirms this is a DIY cyberdeck build (split mechanical keyboard, touchscreen, Raspberry Pi 4, Meshtastic LoRa radio), not a con-distributed badge or SAO. No specific convention or distribution event is mentioned in the README.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    The linked repo is a cyberdeck project (a homebuilt portable computer with a split
    ergonomic keyboard, touchscreen, Raspberry Pi 4, and Meshtastic LoRa radio), not a
    con-distributed badge or SAO. The v1.1 revision adds SAO-style i2c ports so other
    badges/SAOs can plug into the deck, which is likely what triggered the discovery
    sweep's badge/SAO classification, but the vecdec itself is the host device, not an
    SAO. No con or year is stated anywhere in the README; the "DEF CON 34" association
    in the original sweep note is unconfirmed and not supported by the source.
last_modified_date: '2026-09-07'
---

The vecdec (also styled Vecdeck) is svenscore's open-source cyberdeck: a homebuilt,
3D-printed portable computer built around a Raspberry Pi 4, a split ergonomic Sofle
Choc mechanical keyboard on an Elite-C controller, and a touchscreen display (a
400x1280 panel in the v1.0 build, upgraded to a 1280x800 Waveshare touchscreen in
v1.1). It includes a MeshAdv Mini LoRa hat for Meshtastic mesh networking, plus
rotary encoders and a gesture sensor (v1.0) or trackball (v1.1) for input.

Notably for this archive, the v1.1 revision adds its own SAO-style i2c expansion
ports via a custom KiCad adapter board, letting other people's badges and SAOs plug
into the deck rather than the vecdec being an SAO itself. That "SAO" hardware detail
is almost certainly what caused the archive's automated discovery sweep to flag it
as a possible badge/SAO entry, and the README's mention of cyberdeck contests is
likely the source of the tentative "DEF CON 34" event guess. Nothing in the repository
ties the project to a specific convention, year, or distribution, so it does not
belong in the archive as a con badge or SAO.
