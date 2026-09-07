---
title: AND!XOR DC25 Badge (2017)
id: dc25-badge-2017
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: AND!XOR
  url: https://hackaday.io/project/19121-andxor-dc25-badge
summary: 'An unofficial DEF CON 25 badge shaped like Bender from Futurama wearing a Hunter S. Thompson-style hat and glasses, built by the five-person AND!XOR crew as a follow-up to their DC24 badge.'
functions: 'CHIP-8/SuperCHIP emulator with 64+ playable ROMs, clones of Ski Free and Flappy Bird, badge-to-badge Bluetooth "botnet" multiplayer game, TCL-ish scripting engine, an unlock/activation code system, and 2,820 combinations of LED "bling" animations (30 LED patterns x 94 screen animations), including a Bring Your Own Bling (BYOB) mode that loads custom animations from the micro SD card.'
look:
  colors: [black, white, gold]
  shape: null
  themes: [pop culture, tv, cyberpunk, radio, security]
tech:
  mcu: Rigado BMD-300 (Nordic nRF52, ARM Cortex-M4F)
  leds:
    count: 15
    type: WS2812B
    note: 'Driven over SPI with DMA; maker calls it a custom WS2812B driver.'
  display: 1.44" 128x128 color LCD (Crystalfontz CFAF128128B, ~24 FPS over 8MHz SPI)
  connectivity: [bluetooth]
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '~496 badges (an initial production run of 396, plus a later add-on of 100)'
  availability: sold_out
  availability_note: 'Sold via Kickstarter in 2017; not available today (checked 2026-09-07).'
  distribution: [crowdfunding]
  where: 'Funded and sold through a Kickstarter campaign; backers picked up badges at DEF CON 25 (Caesars Palace, Las Vegas, July 27-30, 2017).'
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/19121/files
  firmware_url: null
  eda_tool: null
  notes: 'The team released VRML, SVG, and DXF 3D/mechanical models of the badge enclosure (for cases, hats, etc.) via the Hackaday.io project files, but explicitly said these are not the Gerbers and are not sufficient to fabricate the PCB. No firmware repository link was found from these sources.'
links:
- label: hackaday.com/2017/01/08/hackaday-links-january-8-2017
  url: https://hackaday.com/2017/01/08/hackaday-links-january-8-2017/
  kind: article
  archived: https://web.archive.org/web/20260215080223/https://hackaday.com/2017/01/08/hackaday-links-january-8-2017/
- label: AND!XOR DC25 Badge (Hackaday.io project)
  url: https://hackaday.io/project/19121-andxor-dc25-badge
  kind: hackaday
- label: AND!XOR on Twitter
  url: https://twitter.com/ANDnXOR
  kind: social
images:
  - file: assets/images/badges/dc25/badge-2017/bac9303e2a.jpg
    source: "https://hackaday.io/project/19121-andxor-dc25-badge"
    credit: "AND!XOR"
    caption: "AND!XOR DC25 badge project thumbnail"
  - file: assets/images/badges/dc25/badge-2017/530844abb2.jpg
    source: "https://hackaday.io/project/19121-andxor-dc25-badge"
    credit: "AND!XOR"
    caption: "The DC25 badge shown in a project update photo"
contact: {}
notes:
- 'Price paid by Kickstarter backers was not found in the sources checked; commenters on the Hackaday.io project ask about price/availability but no figure is confirmed there. Firmware repository link not located. SAO support not mentioned by the maker; recorded as none rather than unknown per guide convention, but could be revisited.'
status: released
sources:
- kind: url
  url: https://hackaday.com/2017/01/08/hackaday-links-january-8-2017/
  title: DEF CON 25 Badge (2017)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''DEF CON 25''.'
  archived: https://web.archive.org/web/20260215080223/https://hackaday.com/2017/01/08/hackaday-links-january-8-2017/
- kind: url
  url: https://hackaday.io/project/19121-andxor-dc25-badge
  title: AND!XOR DC25 Badge
  accessed: '2026-09-07'
  note: 'Maker''s own Hackaday.io project page; source for maker identity, theme, hardware specs (BMD-300, LCD, LEDs), functions/games, production quantity (396 + 100 badges), Kickstarter distribution, and the 3D-model files (not gerbers).'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Every non-empty field and body sentence was checked against the maker''s own Hackaday.io project page (text and project-log quotes) and, for the two saved photos, against the images themselves. Confirmed directly: team size/origin ("5 dudes from California"), DC24-sequel framing, BMD-300/nRF52/Cortex-M4F MCU, 15x WS2812B LEDs, 1.44" 128x128 CFAF128128B LCD at 8MHz SPI (24 FPS per a later project log, vs. an earlier 19 FPS spec note - used the higher, more specific figure), Bluetooth badge-to-badge multiplayer, CHIP-8/SuperCHIP emulator with 64+ ROMs, Ski Free/Flappy Bird clones, TCL-ish scripting, activation-code system, the 30 LED patterns x 94 screen animations = 2,820 bling-mode figure, the 396 + 100 = ~496 badge quantity, Kickstarter distribution, the 3D-model-files-are-not-gerbers quote, and the @ANDnXOR Twitter handle. look.colors (black/white/gold) is supported by the two saved photos (board photo shows black PCB, white silkscreen fill, and gold-tone trace accents) rather than by a maker statement; the project text separately confirms a white badge variant existed. Price and a firmware repo link were not found and are left empty, as is tech.battery (only a regulator/power-draw note was found, no battery spec) and tech.sao_ports (badge has no SAO header). No unsupported claims found; nothing removed.'
last_modified_date: '2026-09-07'
---

The AND!XOR DC25 badge is an unofficial DEF CON 25 badge shaped like a mashup of Bender from *Futurama* and Hunter S. Thompson, complete with a bucket hat, aviator glasses, and a cigarette holder rendered in the PCB silkscreen. It was built by AND!XOR, a five-person team of hardware and software engineers from California, as a follow-up to their DEF CON 24 badge. The badge is powered by a Rigado BMD-300 module (Nordic nRF52, ARM Cortex-M4F) driving a 1.44" 128x128 color LCD and 15 WS2812B LEDs, and was funded and sold through a Kickstarter campaign ahead of the con, with roughly 496 units produced across an initial 396-unit order and a later 100-unit add-on.

On top of blinky "bling" modes (2,820 combinations of LED patterns and screen animations, including a Bring-Your-Own-Bling mode that loads custom animations from a micro SD card), the badge runs a CHIP-8/SuperCHIP emulator with over 64 playable ROMs, clones of Ski Free and Flappy Bird, a TCL-ish scripting engine for the hardware, and a Bluetooth-based badge-to-badge "botnet" multiplayer game. An in-badge activation-code system was used to keep some features locked until the con itself, partly to avoid giving Kickstarter backers too much of a head start.

The maker later published 3D and mechanical model files for the badge's enclosure (VRML, SVG, and DXF) so people could build cases, hats, or other add-ons, but stated explicitly that these are not the PCB Gerbers, so the design cannot be fully replicated from them. No firmware repository or the exact Kickstarter price were found in the sources checked for this entry.
