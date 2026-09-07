---
title: Not Just a Crosswalk
id: dc34-not-just-a-crosswalk
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: RivaClan
  url: https://github.com/keeloi79
summary: An 18-LED rainbow SAO from RivaClan (Caelyb Riva) built as a hardware protest against 2025-2026 removals of rainbow crosswalk street art in Florida and Texas cities.
functions: Two tactile buttons cycle through LED animation effects and color palettes; a persistent-memory system on the CH32V003 saves the last-used effect and palette across power cycles. Can be worn powered by USB-C or plugged into a host badge's SAO port.
look:
  colors:
  - black
  - multicolor
  shape: rectangle
  themes:
  - pride
  - security
  - hardware tool
tech:
  mcu: CH32V003
  leds:
    count: 18
    type: WS2812-2020 (side-emitting, SK6812D-EC3210R)
    note: Custom-tuned PWM for a flicker-free pulse/breathing effect down to 1% duty cycle.
  display: none
  connectivity: []
  inputs:
  - buttons
  battery: null
  power: USB-C or SAO header (3.3V step-up via MT3608L boost converter)
  sao_version: v1.69bis / v2
  sao_ports: 1
get_one:
  price: $35
  price_usd: 35.0
  quantity: ''
  availability: sold_out
  availability_note: 'Checked 2026-09-06: no separate storefront listing found beyond the maker''s Ko-fi page, which returned an access error when checked.'
  distribution:
  - purchase
  where: Sold through Uberflux as a DEF CON 34 in-person pickup, with post-event shipping to the continental US available for $10.
make_your_own:
  open_source: true
  hardware_url: https://github.com/keeloi79/not-a-crosswalk-sao
  firmware_url: https://github.com/keeloi79/not-a-crosswalk-sao
  gerbers_url: null
  bom_url: https://github.com/keeloi79/not-a-crosswalk-sao/blob/main/docs/BOM.md
  eda_tool: EasyEDA
  license: GPL-3.0 (firmware), CERN-OHL-S-2.0 (hardware), CC-BY-SA-4.0 (docs)
  fab_url: null
  notes: PCB assembly was done through JLCPCB. LED driver code builds on Blake Sands' open WS2812 driver for the CH32V003.
links:
- label: ko-fi.com/caelybr
  url: https://ko-fi.com/caelybr
  kind: store
- label: github.com/keeloi79/not-a-crosswalk-sao
  url: https://github.com/keeloi79/not-a-crosswalk-sao
  kind: repo
- label: cdn.discordapp.com/attachments/614861657004310530/1512614773915652228/IMG_2982.mov?ex=6a4ba009&is=6a4a4e89&hm=a4dca3b820a3f9e9f690449d089838d2bd432553027ad043e860dad4b5a172af&
  url: https://cdn.discordapp.com/attachments/614861657004310530/1512614773915652228/IMG_2982.mov?ex=6a4ba009&is=6a4a4e89&hm=a4dca3b820a3f9e9f690449d089838d2bd432553027ad043e860dad4b5a172af&
  kind: video
- label: uberflux.com/product/DC34-crosswalk
  url: https://uberflux.com/product/DC34-crosswalk
  kind: store
images:
- file: assets/images/badges/dc34/not-just-a-crosswalk/7c4667834c.png
  source: https://github.com/keeloi79/not-a-crosswalk-sao
  credit: keeloi79 (Caelybr)
  caption: The SAO lit in various color patterns, spelling out NOT JUST A CROSSWALK across its rainbow LED bars
- file: assets/images/badges/dc34/not-just-a-crosswalk/cb949402c8.jpg
  source: https://github.com/keeloi79/not-a-crosswalk-sao
  credit: keeloi79 (Caelybr)
  caption: Close-up of the rainbow WS2812 LED array lit through the crosswalk-style cutout pattern
- file: assets/images/badges/dc34/not-just-a-crosswalk/96de5568d5.jpg
  source: https://uberflux.com/product/DC34-crosswalk
  credit: caelyb / Uberflux
  caption: The Not Just a Crosswalk SAO listed on Uberflux's DC34 storefront
contact:
  discord: Caelyb
  emails:
  - caelyb@caelyb.com
  handles:
  - '@caelybr'
  raw:
  - 'Insta:'
notes:
- 'Uberflux. $34, status: sold out.'
status: released
sources:
- kind: sheet
  event: dc34
  row: 30
  updated: 7/5/2026 17:19:17
  listing: New
- kind: url
  url: https://github.com/keeloi79/not-a-crosswalk-sao
  title: not-a-crosswalk-sao (GitHub repo)
  accessed: '2026-09-06'
  note: 'Primary source: README and inline docs give the mission statement, LED/MCU specs, power design, buttons, licensing, and credits.'
- kind: url
  url: https://github.com/keeloi79
  title: keeloi79 (GitHub profile)
  accessed: '2026-09-06'
  note: Confirms the maker's name as Caelyb Riva, Instagram handle caelybr; no direct mention of 'RivaClan' but the surname Riva matches the sheet's maker name.
- kind: url
  url: https://uberflux.com/product/DC34-crosswalk
  title: Not Just a Crosswalk SAO / Badge
  accessed: '2026-09-07'
  note: 'Primary source: gives the mission statement (protest of rainbow crosswalk removals), LED count/type, effects, flag palettes, price $34, and sold-out status (0 remaining, 13 sold).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Ko-fi page (ko-fi.com/caelybr) returned HTTP 403 on fetch, so price/availability/quantity beyond the sheet's $35 could not be confirmed there. No separate storefront or Hackaday.io project page was found. Quantity made and current availability are unknown. The linked Discord video attachment was not fetched (attachment URL, not a page). Type set to sao (not badge) based on the repo describing it as a "Simple Add-On (SAO) designed for Defcon 34," though the sheet's functions text says it can also be worn standalone via USB-C. Merged with duplicate entry 'Not Just a Crosswalk SAO / Badge' (dc34-not-just-a-crosswalk-sao-badge).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc34/not-just-a-crosswalk-sao-badge/
---

Not Just a Crosswalk is a rainbow-lit SAO built by RivaClan (Caelyb Riva, aka Caelybr) for DEF CON 34. Eighteen side-emitting WS2812-2020 LEDs shine through a crosswalk-striped cutout in the PCB silkscreen, driven by a CH32V003 RISC-V microcontroller with two tactile buttons — one to cycle LED effects, one to change color palettes — and flash memory that remembers the last settings used. It runs standalone on USB-C or draws power through a host badge's SAO header, with an onboard boost converter and auto-switching MOSFET so the LEDs stay at full brightness either way.

The project's README frames it explicitly as a hardware protest: the maker built it in response to state-mandated removals of rainbow crosswalk street art in Miami Beach, Austin, Gainesville, and San Antonio during 2025 and 2026. Hardware, firmware, and documentation are all published on GitHub under open licenses (CERN-OHL-S-2.0 for the hardware, GPL-3.0 for the firmware), with PCB assembly handled by JLCPCB and the low-level LED driver code built on Blake Sands' open-source WS2812 driver for the CH32V003.

## Make your own

The GitHub repository (github.com/keeloi79/not-a-crosswalk-sao) has everything needed to build one: `docs/HARDWARE.md` covers the schematic and PCB layout, `docs/firmware.md` covers build/flash instructions (programmed via a WCH-LinkE SWIO adapter), and `docs/BOM.md` lists the components, sourced and assembled through JLCPCB.

## Notes merged from the duplicate entry "Not Just a Crosswalk SAO / Badge"

Not Just a Crosswalk is a rainbow-lit SAO sold through the Uberflux storefront as a DEF CON 34 badge drop, priced at $34 with in-person pickup at the con (post-event shipping available for $10). It carries 18 side-emitting SK6812-EC3210R LEDs behind a crosswalk-styled cutout, with two tactile buttons to cycle through more than ten animation effects — static display, party mode, strobe, pulse, chase, sparkle, and burst — and over a dozen pride-flag color palettes (rainbow, bi, lesbian, trans, nonbinary, asexual, genderfluid, poly, bear, leather, disability, and demi). It can run standalone from USB-C or draw power through a host badge's SAO port, with a boost converter to keep the LEDs at full brightness either way, and it remembers the last effect and palette used across power loss. The listing sold out at 13 units.

This entry and its Uberflux listing describe what looks like the same badge already documented in more technical depth under `dc34-not-just-a-crosswalk`, credited to RivaClan (Caelyb Riva, handle caelybr): both are DEF CON 34 rainbow SAOs built explicitly as a protest against the removal of rainbow crosswalk street art, from the same maker handle (caelyb/caelybr), with the same side-emitting LED family. The Uberflux page itself does not name the microcontroller or link any open-source design files, so those fields are left empty here rather than copied over from the other entry without a source on this page confirming them.
