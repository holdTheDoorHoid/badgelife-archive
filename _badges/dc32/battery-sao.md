---
title: Battery SAO
id: dc32-battery-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: p0ns/idk
  url: https://idk.bz/
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
- kind: website
  label: IDK (p0ns) project site
  url: https://idk.bz/
  archived: false
images: []
contact: {}
notes:
- "Sheet lists this maker with four separate dc32 rows (Battery SAO, 420 Bud SAO, IDK SAO, Disappointing Badge); the maker's own site (idk.bz) only documents one of those by name (\"IDK SAO\", posted May 2024: Attiny 0/1-series chip, 4x SK6812-mini LEDs, button, 6-pin SAO connector) plus a 2023 DEFCON31 SAO (CR2032 battery holder, switch, 6 LEDs). Neither page names or describes a \"Battery SAO\"."
status: listed
sources:
- kind: sheet
  event: dc32
  row: 84
  updated: '2024-06-23'
- kind: url
  url: https://idk.bz/
  title: 'IDK - p0ns'
  accessed: '2026-09-07'
  note: "Confirms p0ns/idk as a real, active badge/SAO maker in the DEF CON 31-32 era; lists their known SAO projects (DEFCON31 SAO, IDK SAO), neither of which is titled or described as a battery-powered SAO for DC32."
- kind: url
  url: https://idk.bz/idksao/
  title: 'IDK SAO - IDK'
  accessed: '2026-09-07'
  note: "The maker's DC32-era SAO project (Attiny 0/1-series MCU, 4x SK6812-mini LEDs, button, 6-pin SAO connector, powered from the host badge's SAO header, no onboard battery mentioned). Does not match the 'Battery SAO' title or a battery-specific feature."
- kind: url
  url: https://idk.bz/dc31sao/
  title: 'DEFCON31 SAO - IDK'
  accessed: '2026-09-07'
  note: "The maker's 2023 SAO: CR2032 battery holder, switch, 6 LEDs (Attiny85 in first 50 kits). Closest match to a 'battery-powered' SAO by this maker, but it is dated/titled for DEF CON 31, not 32, and is not named 'Battery SAO'."
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Extensive search (WebSearch queries on title+maker, title+"DEF CON 32", maker+SAO+2024,
    maker's own site and its linked pages, Reddit/forum/Bluesky angles) turned up no page,
    post, storefront listing, or press mention specifically titled or describing a "Battery
    SAO" by p0ns/idk. The maker is confirmed real and active (idk.bz), with two documented
    SAO projects in the DC31/DC32 window, but neither is a confirmed match for this exact
    sheet entry. Left tech/get_one/make_your_own fields empty rather than guess which (if
    either) of the maker's documented projects this sheet row refers to. The sheet also
    lists three other dc32 rows from the same maker ("420 Bud SAO", "IDK SAO", "Disappointing
    Badge") that are not all individually documented on the maker's site, suggesting some
    were informal/joke SAOs traded at the con without a web page.
last_modified_date: '2026-09-07'
---

The community sheet credits a "Battery SAO" to p0ns (of idk.bz) at DEF CON 32 (2024), but no independent source — the maker's own site, search engines, storefronts, or press — describes an item by that exact name. The maker is a real, identifiable badgelife participant who has published at least two other SAOs in the same period: a 2023 "DEFCON31 SAO" kit (CR2032 battery holder, switch, six LEDs, with an ATtiny85 socket in the first 50 units) and a 2024 "IDK SAO" (an ATtiny 0/1-series chip driving four SK6812-mini LEDs behind a button, powered from the host badge's SAO header rather than an onboard battery).

Neither documented project is a confident match for "Battery SAO": the DC31 SAO is the right shape (its own battery) but the wrong year, and the DC32-era IDK SAO has no battery of its own. It is possible the sheet's "Battery SAO" is a fourth, undocumented item this maker brought to DC32 — the sheet lists three other rows attributed to the same maker for that year, at least one of which ("Disappointing Badge") also has no discoverable web presence, consistent with small joke SAOs that circulated at the con without ever getting a project page.

Given the lack of a confirmed primary source for this specific title, all technical and commercial fields have been left empty rather than filled from a guess.
