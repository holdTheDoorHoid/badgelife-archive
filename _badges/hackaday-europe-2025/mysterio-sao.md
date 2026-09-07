---
title: Mysterio SAO
id: hackaday-europe-2025-mysterio-sao
layout: badge
parent: HaD Europe 2025
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: hackaday-europe-2025
year: 2025
makers:
- name: davedarko
  url: https://hackaday.io/hacker/3459-davedarko
summary: A Simple Add-On shaped like the Spider-Man villain Mysterio, using a 4-layer 0.8 mm purple ENIG PCB as a light-shading mask so NeoPixel LEDs driven by a CH32V003 glow through his glass dome; 50 units were produced for Hackaday Europe 2025.
functions: Lights the glass-dome head with four addressable NeoPixel LEDs, custom-animated to look foggy and mystical.
look:
  colors:
  - purple
  - gold
  shape: null
  themes:
  - movie
  - pop culture
  - villain
  - skull
tech:
  mcu: CH32V003
  leds:
    count: 4
    type: NeoPixel
    note: Addressable RGB LEDs shining through the PCB's light-shading layers to light the dome.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '50'
  availability: limited
  distribution:
  - free_drop
  where: Handed out by the maker at Hackaday Europe 2025.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: https://github.com/cnlohr/ch32v003fun/tree/master/examples/dma_gpio_ws2812
  eda_tool: null
links:
- label: hackaday.io/project/199296-mysterio-sao
  url: https://hackaday.io/project/199296-mysterio-sao
  kind: hackaday
- label: hackaday.io/project/199296/logs
  url: https://hackaday.io/project/199296/logs
  kind: hackaday
- label: cdn.hackaday.io/files/1992968526680064/mysterio.mp4
  url: https://cdn.hackaday.io/files/1992968526680064/mysterio.mp4
  kind: hackaday
- label: cnlohr/ch32v003fun (WS2812 DMA example used for the LED driving)
  url: https://github.com/cnlohr/ch32v003fun/tree/master/examples/dma_gpio_ws2812
  kind: repo
images:
  - file: assets/images/badges/hackaday-europe-2025/mysterio-sao/7779a337b4.jpg
    source: "https://hackaday.io/project/199296-mysterio-sao"
    credit: "davedarko"
    caption: "Mysterio SAO, version 3 boards, dome lit"
  - file: assets/images/badges/hackaday-europe-2025/mysterio-sao/4794af9426.jpg
    source: "https://hackaday.io/project/199296-mysterio-sao"
    credit: "davedarko"
    caption: "Mysterio SAO, unlit, purple ENIG PCB"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/199296-mysterio-sao
  title: Mysterio SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/199296-mysterio-sao
  title: Mysterio SAO project page
  accessed: '2026-09-07'
  note: Confirmed maker, concept (glowing Mysterio dome), final CH32V003 + NeoPixel design, 50-unit run, version-3 purple ENIG 0.8mm 4-layer PCB, and intended distribution at Hackaday Europe 2025.
- kind: url
  url: https://hackaday.io/project/199296/logs
  title: Mysterio SAO project logs
  accessed: '2026-09-07'
  note: Confirmed CH32V003 programmed via ch32v003fun configured for 4 NeoPixels, the "ordered 50 ... for Hackaday Europe" quantity, boards arriving February 2025, and the PCB layer/shading evolution (2-layer to 4-layer, purple stopmask, ENIG).
last_modified_date: '2026-09-07'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Maker's own Hackaday.io project page and logs confirm design, chip, LED count, PCB spec,
    and 50-unit production run for Hackaday Europe 2025. No price was ever stated (units were
    handed out by the maker rather than sold, per the project's phrasing "populate as many as
    I have chips and LEDs for it for Hackaday Europe"), so get_one.price/price_usd are left
    empty and distribution is marked free_drop. No dedicated hardware/Gerber repo for the SAO
    itself was found (only the shared ch32v003fun firmware example used for driving the
    NeoPixels), so make_your_own.open_source and hardware_url are left null rather than guessed.
    look.shape left null: no single short phrase (e.g. "skull") fully captures the astronaut-suit
    silhouette with a round dome head; look.themes covers it instead.
---

The Mysterio SAO is a Simple Add-On by Hackaday.io user davedarko, shaped like Marvel villain Mysterio: a caped, astronaut-suited figure whose round glass-dome head is illuminated from inside. The design goes through several revisions on the project's Hackaday.io page, moving from an ATtiny202 to an ESP32 prototype before settling on a CH32V003 RISC-V microcontroller driving four addressable NeoPixel LEDs. The PCB itself does double duty as the artwork and the light-shading mask: earlier single- and two-layer boards let light bleed out around the neck, so the final version 3 uses a 4-layer, 0.8 mm, purple-ENIG board to block and shape the glow so it reads as a foggy, mystical dome rather than a bare LED glare.

Davedarko ordered 50 of the version-3 boards, which arrived in February 2025, and handed them out to badge collectors at Hackaday Europe 2025 as chips and LEDs allowed. The MCU is programmed with cnlohr's open-source `ch32v003fun` toolchain, using its WS2812/NeoPixel DMA example as the basis for the LED driving code; no dedicated hardware repository or Gerbers for the SAO board itself were found on the project page.
