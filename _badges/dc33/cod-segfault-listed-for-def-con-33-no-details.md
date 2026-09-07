---
title: CoD_Segfault (listed for DEF CON 33, no details)
id: dc33-cod-segfault-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: unknown
event: dc33
year: 2025
makers:
- name: CoD_Segfault
  url: https://github.com/CoD-Segfault
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
- kind: repo
  url: https://github.com/CoD-Segfault
  label: CoD_Segfault on GitHub
- kind: social
  url: https://twitter.com/CoD_Segfault
  label: CoD_Segfault on Twitter/X
images: []
contact: {}
notes:
- 'The community sheet''s "2025 (expected makers)" tab lists only the name CoD_Segfault
  in row 27, with every other column (badge/SAO name, links, price, functions) blank.'
status: unknown
sources:
- kind: sheet
  event: dc33
  row: 27
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://api.github.com/users/CoD-Segfault
  title: CoD-Segfault (GitHub user profile)
  accessed: '2026-09-06'
  note: Confirms CoD_Segfault is a real hardware hacker (bio, Chicagoland area, Twitter handle CoD_Segfault) with 27 public repos, but lists no DEF CON 33 / 2025 badge or SAO project.
- kind: url
  url: https://github.com/CoD-Segfault/wifi-shuriken
  title: 'wifi-shuriken: Software for the WiFi Shuriken project'
  accessed: '2026-09-06'
  note: Most relevant recent hardware project on the account (RP2350 + ESP32-C5 distributed WiFi wardriving scanner), but the repo was created March 2026, after DEF CON 33 (Aug 2025), so it cannot be what was listed for that con.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    No badge/SAO name, description, or links were ever entered for CoD_Segfault
    on the DC33 "expected makers" sheet tab -- only the maker name appears. Web
    search (DuckDuckGo, Bing) and Hackaday.io search for "CoD_Segfault" turned
    up nothing about a DEF CON 33 item. Found the maker's real GitHub account
    (github.com/CoD-Segfault, confirmed via GitHub's user-search API) and Twitter
    handle from the bio; their repos show wardriving/WiFi-scanner hardware
    (a wardriver.uk rev3 fork, alternative BW16 firmware for wardriver.uk, an ESP32-C5 port of that firmware, the WiFi Shuriken project) and repos named
    DefCon27badge and DefCon29Badge (no descriptions), but none for DC31,
    DC32, or DC33. The archive also holds equally detail-free entries for this
    maker at DC31 ("I have no idea") and DC32 ("listed, no details"). Could
    not determine what, if anything, CoD_Segfault actually brought to DEF CON
    33. Fact-check 2026-09-07: GitHub profile, repo list, wifi-shuriken repo
    and the local sheet export (row 27, no extra columns) all re-confirmed;
    removed speculation about the listing being an in-joke.
last_modified_date: '2026-09-07'
---

CoD_Segfault appears on the DEF CON 33 (2025) community badge sheet's "expected makers" tab, but the row carries no badge/SAO name, no links, no price, and no functions -- just the maker's name. No announcement, storefront listing, or social post describing a DEF CON 33 badge or SAO from this maker could be found.

CoD_Segfault is a real, active hardware hacker based in the Chicagoland area, publicly identifiable through a GitHub account (github.com/CoD-Segfault) and matching Twitter/X handle. Their public work centers on WiFi wardriving hardware -- a fork of the wardriver.uk rev3 project, an alternative AT firmware for the BW16 module used in wardriver.uk rev3, an ESP32-C5 port of that firmware, and their own "WiFi Shuriken" distributed scanning rig (RP2350 controller plus ESP32-C5 scanners, repo created March 2026) -- plus repos named DefCon27badge and DefCon29Badge. None of that work is dated to, or described as, a DEF CON 33 badge or SAO, so this entry cannot be filled in beyond confirming who the maker is.

This is the third consecutive year (after DC31's "I have no idea" and an identically blank DC32 listing) that CoD_Segfault appears on the badge sheet with no further detail.
