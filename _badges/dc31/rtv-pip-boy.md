---
title: DC31 RTV "Pip-Boy"
id: dc31-rtv-pip-boy
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Red Team Village
  url: https://redteamvillage.io/
summary: A red PCB handheld badge styled after the Pip-Boy wrist computer from the Fallout video game series, made for Red Team Village at DEF CON 31.
functions: 'Product photos show a front panel silkscreened like a Fallout Pip-Boy: labels for STAT, INV, DATA, MAP and RADIO around a rotary "TUNE" dial, a "WIFIs" dial, a D-pad, two round buttons, and a POWER button, plus a rectangular screen window. The back carries wardriving/aircrack-style command-line text (WEP/WPA-PSK, deauth, MAC address notes) as board art, a 2xAA battery holder, and an "Untitled Electronics / 404 Name Not Found" fab credit.'
look:
  colors:
  - red
  - orange
  - black
  shape: handheld
  themes:
  - retro computer
  - console
  - security
  - pop culture
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: 2x AA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Listed on Red Team Village's Square storefront under their "Badges" category; the product page is still live but is a JavaScript-rendered Square Online page that would not return price or stock status to automated fetches.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: redteamvillage.square.site/product/dc31badge/2
  url: https://redteamvillage.square.site/product/dc31badge/2
  kind: store
images:
- file: assets/images/badges/dc31/rtv-pip-boy/262f610c80.jpg
  source: "https://redteamvillage.square.site/product/dc31badge/2"
  credit: "Red Team Village"
  caption: "Front of the DC31 RTV Pip-Boy badge, styled after the Fallout Pip-Boy interface with STAT/INV/DATA/MAP/RADIO labels"
- file: assets/images/badges/dc31/rtv-pip-boy/6719f913bc.jpg
  source: "https://redteamvillage.square.site/product/dc31badge/2"
  credit: "Red Team Village"
  caption: "Back of the DC31 RTV Pip-Boy badge, showing the Red Team Village logo, a 2xAA battery holder, and Untitled Electronics fab credit"
contact: {}
notes: []
status: listed
sources:
- kind: sheet
  event: dc31
  row: 68
  updated: '2023-02-14'
- kind: url
  url: https://redteamvillage.square.site/product/dc31badge/2
  title: DC31 RTV "Pip-Boy" | Red Team Village
  accessed: '2026-09-06'
  note: Confirmed product title, "Badges" store category, and (via an archive.org snapshot from 2023-05-15 of the same URL) two product photos showing the badge's front and back.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: 'The storefront is a client-side-rendered Square Online page; automated fetches (and a wayback capture) could not recover price, quantity, or MCU/display/LED specs, only the title, category, and product photos. No Hackaday.io project, GitHub repo, or press coverage of this badge was found via web search or search-engine scraping (WebSearch was unavailable for this task; DuckDuckGo, Bing, Google, and Reddit searches via curl/WebFetch either blocked the request or returned no on-topic results). Front-panel silkscreen (STAT/INV/DATA/MAP/RADIO, a "TUNE" dial) confirms the Fallout Pip-Boy reference in the name; back-panel silkscreen printing wardriving/aircrack-style syntax (WEP/WPA-PSK, deauth, MAC notes) appears to be thematic board art rather than a stated wifi feature, so connectivity was left empty rather than guessed. MCU, LED, and display specs were not stated anywhere reachable and are left null.'
last_modified_date: '2026-09-06'
---

Red Team Village's DEF CON 31 badge is a die-cut red PCB shaped and silkscreened like the Pip-Boy, the wrist-mounted computer from Bethesda's Fallout games. The front reproduces the Pip-Boy's tab menu (STAT, INV, DATA, MAP, RADIO) around a rotary "TUNE" dial and a second "WIFIs" dial, alongside a D-pad, two round buttons, a POWER button, and a rectangular screen cutout, all rendered in RTV's red-and-orange house style with their shield logo in the corner. The back holds a 2xAA battery compartment and is silkscreened with command-line-style wardriving text (WEP/WPA-PSK key notes, deauth and MAC-address references) as board art, along with a fabrication credit to "Untitled Electronics."

The badge was sold through Red Team Village's Square storefront under their "Badges" category; that listing is still reachable but did not yield price, quantity, or stock-status information to this pass because the store page renders its catalog data client-side in JavaScript. No hardware repository, BOM, or third-party writeup for this specific badge turned up in the sources checked, so the electronics (MCU, display, LEDs) remain unconfirmed and are left blank rather than guessed.
