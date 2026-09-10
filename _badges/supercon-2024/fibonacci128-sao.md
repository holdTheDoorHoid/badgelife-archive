---
title: Fibonacci128 SAO
id: supercon-2024-fibonacci128-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Squidgeefish
  url: https://squidgeefish.com/projects/fibonacci128-sao/
summary: A one-inch circular SAO packing 128 addressable RGB LEDs into a Fibonacci spiral, recreating Jason Coon's Fibonacci128 LED art as a wearable add-on for Supercon 2024.
functions: Drives animated patterns (pinwheel, horizontal/vertical rainbow, Fibonacci-mapped effects) across the 128-LED spiral. An onboard I2C slave (address 0x37, 256 registers) lets a host badge select patterns, set brightness, and stream live framebuffer updates.
look:
  colors: []
  shape: circle
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: STM8S001J3
  leds:
    count: 128
    type: WS2812B
    note: 1mm-pitch XL-1010RGBC-WS2812B package LEDs arranged in a Fibonacci spiral on a 1-inch, four-layer circular PCB; driven by the STM8S001J3 over a single WS2812 data pin.
  display: null
  connectivity:
  - i2c
  battery: 'powered by host badge (via boost-converter backpack: TPS613222ADBVR, 3.3V to 5V, castellated SAO-header pins)'
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '5'
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://squidgeefish.com/otterwork/
  eda_tool: KiCad
links:
- label: hackaday.com/2024/12/16/building-the-spectacular-fibonacci128-simple-add-on
  url: https://hackaday.com/2024/12/16/building-the-spectacular-fibonacci128-simple-add-on/
  kind: article
  archived: https://web.archive.org/web/20260516052449/https://hackaday.com/2024/12/16/building-the-spectacular-fibonacci128-simple-add-on/
- label: squidgeefish.com/projects/fibonacci128-sao
  url: https://squidgeefish.com/projects/fibonacci128-sao/
  kind: website
  archived: https://web.archive.org/web/20260104015317/https://squidgeefish.com/projects/fibonacci128-sao/
- label: squidgeefish.com/otterwork
  url: https://squidgeefish.com/otterwork/
  kind: doc
  archived: https://web.archive.org/web/20260227080727/https://squidgeefish.com/otterwork/
images:
- file: assets/images/badges/supercon-2024/fibonacci128-sao/016a428d7f.jpg
  source: https://squidgeefish.com/projects/fibonacci128-sao/
  credit: Squidgeefish
  caption: Five assembled Fibonacci128 SAO boards
  archived: https://web.archive.org/web/20260104015317/https://squidgeefish.com/projects/fibonacci128-sao/
- file: assets/images/badges/supercon-2024/fibonacci128-sao/233a667d0c.jpg
  source: https://hackaday.com/2024/12/16/building-the-spectacular-fibonacci128-simple-add-on/
  credit: Squidgeefish / Hackaday
  caption: Fibonacci128 SAO with 128 RGB LEDs lit in a spiral pattern
  archived: https://web.archive.org/web/20260516052449/https://hackaday.com/2024/12/16/building-the-spectacular-fibonacci128-simple-add-on/
contact: {}
notes:
- 128 RGB LEDs on 1-inch PCB in Fibonacci spiral, I2C controlled; includes boost-converter backpack PCB
status: released
sources:
- kind: url
  url: https://hackaday.com/2024/12/16/building-the-spectacular-fibonacci128-simple-add-on/
  title: Fibonacci128 SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''Hackaday Supercon 2024''.'
  archived: https://web.archive.org/web/20260516052449/https://hackaday.com/2024/12/16/building-the-spectacular-fibonacci128-simple-add-on/
- kind: url
  url: https://squidgeefish.com/projects/fibonacci128-sao/
  title: Fibonacci128 SAO project page
  accessed: '2026-09-07'
  note: Maker's own project writeup; confirmed LED count/type, MCU, I2C address/register scheme, boost-converter backpack, KiCad image-import design process, and image assets.
  archived: https://web.archive.org/web/20260104015317/https://squidgeefish.com/projects/fibonacci128-sao/
- kind: url
  url: https://squidgeefish.com/otterwork/
  title: Otterwork
  accessed: '2026-09-07'
  note: Maker's firmware/build page for the STM8S001J3 + WS2812 I2C driver used on this SAO; confirms firmware is documented/available, hardware files are not.
  archived: https://web.archive.org/web/20260227080727/https://squidgeefish.com/otterwork/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker (Squidgeefish) declined to open-source the hardware design files out of respect for Jason Coon (Evil Genius Labs), whose original one-inch Fibonacci128 LED art this SAO recreates via KiCad image import; firmware/build details are documented on the "otterwork" page. Only five prototype units were assembled, with no stated price or commercial release, so get_one fields beyond quantity are left empty. No maker contact details were found on their own pages.
last_modified_date: '2026-09-07'
---

The Fibonacci128 SAO is a dense LED showpiece made by first-time Supercon attendee Squidgeefish for Hackaday Supercon 2024 in Pasadena. It packs 128 individually addressable WS2812-style RGB LEDs into a Fibonacci spiral on a one-inch, four-layer circular PCB, recreating the look of Jason Coon's original Fibonacci128 LED art pieces. Lacking access to Coon's source files, the maker rebuilt the layout by importing a reference image directly into KiCad and hand-placing all 128 LED footprints and traces.

An STM8S001J3 microcontroller, hand-soldered in SOIC-8 package on the back of the board, drives the LED chain over a single WS2812 data pin and exposes an I2C slave interface (address 0x37, 256 registers) so a host conference badge can pick animation patterns, adjust brightness, and even stream live framebuffer updates to the array in real time. Because the Supercon 2023 badge's battery rail wasn't reliable enough to run the LEDs directly, the project also includes a small boost-converter backpack board (built around a TPS613222ADBVR) with castellated pins that mates to the SAO header and steps the input up to a stable 5V.

Only five prototype units were assembled and the SAO was never sold or otherwise released to the public. The maker chose not to publish the hardware design files, citing the design's roots in Jason Coon's original artwork, but documented the firmware and I2C driver on their "otterwork" project page, and has mentioned plans for a future daughterboard that would let Coon's own existing one-inch Fibonacci128 boards be used as SAOs directly.
