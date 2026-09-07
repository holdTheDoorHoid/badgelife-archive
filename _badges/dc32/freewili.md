---
title: DEFCON32_FREEWiLi
id: dc32-freewili
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: unknown
event: dc32
year: 2024
makers:
- name: FreeWili
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
- label: web.archive.org/web/20241014122935/freewili.com/products/defcon32-badge
  url: https://web.archive.org/web/20241014122935/https://freewili.com/products/defcon32-badge/
  kind: website
- label: FREE-WILi Turns DC32 Badge Into Hardware Dev Tool (Hackaday)
  url: https://hackaday.com/2024/11/21/free-wili-turns-dc32-badge-into-hardware-dev-tool/
  kind: article
  archived: https://web.archive.org/web/20260607141141/https://hackaday.com/2024/11/21/free-wili-turns-dc32-badge-into-hardware-dev-tool/
- label: FREE-WILi Brings Its Flexible Development and Debugging Platform to the DEF CON 32 Badge (Hackster.io)
  url: https://www.hackster.io/news/free-wili-brings-its-flexible-development-and-debugging-platform-to-the-def-con-32-badge-bd5ab94f1b9e
  kind: article
- label: FREE-WiLi announcement post (X/Twitter)
  url: https://x.com/FREE_WiLi_/status/1856426705268945360
  kind: social
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: not_an_item
sources:
- kind: url
  url: https://web.archive.org/web/20241014122935/https://freewili.com/products/defcon32-badge/
  title: DEFCON32_FREEWiLi
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc32''.'
- kind: url
  url: https://hackaday.com/2024/11/21/free-wili-turns-dc32-badge-into-hardware-dev-tool/
  title: FREE-WILi Turns DC32 Badge Into Hardware Dev Tool
  accessed: '2026-09-07'
  note: Confirms this is a free firmware/software port for the official DEF CON 32 conference badge (RP2350-based, made by DEF CON, ~30,000 in circulation), not a separate badge/SAO manufactured by FreeWili.
  archived: https://web.archive.org/web/20260607141141/https://hackaday.com/2024/11/21/free-wili-turns-dc32-badge-into-hardware-dev-tool/
- kind: url
  url: https://www.hackster.io/news/free-wili-brings-its-flexible-development-and-debugging-platform-to-the-def-con-32-badge-bd5ab94f1b9e
  title: FREE-WILi Brings Its Flexible Development and Debugging Platform to the DEF CON 32 Badge
  accessed: '2026-09-07'
  note: Title/snippet corroborates same story; the full article body returned HTTP 403 so it was not read in full.
- kind: url
  url: https://x.com/FREE_WiLi_/status/1856426705268945360
  title: 'FREE-WiLi announcement: DC32 badge firmware port released for free'
  accessed: '2026-09-07'
  note: Search snippet quotes the maker's own post confirming the badge is DEF CON's RP2350-powered DC32 badge and that the FreeWili code for it is a free release; the live post itself returned HTTP 402 to direct fetch.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This page is not a distinct badge or SAO made by FreeWili. It is FreeWili's free firmware/software port that adds their multitool-style GUI (GPIO control, I2C, IR, sound, WASM scripting) to the *official* DEF CON 32 conference badge (the RP2350/Raspberry Pi Pico 2-based "DC32 Human Badge" issued by DEF CON itself to all roughly 30,000 attendees). FreeWili released the code for free to promote their own standalone FREE-WILi hardware multitool. The archived freewili.com "products/defcon32-badge" page could not be fetched directly (web.archive.org fetches are blocked in this research environment); its content was reconstructed from Hackaday's November 2024 coverage, a Hackster.io article title, and the maker's own X/Twitter post, all of which agree on this reading. No separate FreeWili-made DC32 badge/SAO product was found. The official DC32 badge itself does not currently appear to have its own entry in this archive and may be worth adding separately.
last_modified_date: '2026-09-07'
---

This entry was created from a page titled "DEFCON32_FREEWiLi" on freewili.com, but research shows it is not a standalone badge or SAO. FreeWili (maker of the FREE-WILi open-hardware multitool) released a free firmware/software port that brings their development-tool GUI to the *official* DEF CON 32 conference badge — the RP2350-based "DC32 Human Badge" that DEF CON itself issued to roughly 30,000 attendees in 2024. The port adds screen, button, accelerometer, and LED light-show control, IR transmit/receive, I2C, GPIO access to the badge's USER1/USER2/SAO pins, a buzzer-driven sound board, a USB serial console, and WASM ROM scripting — pitched by FreeWili as turning the badge into a handy tool for testing and debugging SAOs.

FreeWili gave the code away for free specifically to introduce badge holders to their paid FREE-WILi hardware line, rather than selling any DC32-specific hardware of their own. No FreeWili-manufactured badge or SAO tied to DEF CON 32 was found in any source consulted.
