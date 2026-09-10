---
title: senSAOr (SAO with an adapted SAOAO header)
id: other-sensaor-sao-with-an-adapted-saoao-header
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2024
makers:
- name: bwasserm
  url: https://github.com/bwasserm
summary: A hand-designed sensor SAO built for Hackaday Supercon 2024, reading an analog sensor input and using it to drive a small chain of addressable LEDs, with a "SAOAO" secondary header so another SAO can be chained off it.
functions: Reads a sensor voltage (0-3.3V) on an input pin and uses it to set the color, brightness, speed, and sine-wave "shape"/"phase" pattern of onboard WS2812/WS2811 LEDs, clocking colors up the board each cycle; can drive additional NeoPixels chained off the top, and passes through a SAOAO port so a second SAO can be plugged in behind it.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - measurement
tech:
  mcu: CH32V003
  leds:
    count: 3
    type: WS2812/WS2811
    note: Three onboard addressable LEDs, chainable to more NeoPixels via a header pad.
  display: none
  connectivity:
  - i2c
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
  open_source: true
  hardware_url: https://github.com/bwasserm/sensaor/tree/main/pcba/sensaor
  firmware_url: https://github.com/bwasserm/sensaor/tree/main/src
  eda_tool: KiCad
links:
- label: github.com/bwasserm/sensaor
  url: https://github.com/bwasserm/sensaor
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- No event id for "Hackaday Supercon 2024" exists yet in _data/events.yml (it has supercon-2017/2018/2019/2022/2023 but no 2024 entry), so event is left as "other" pending that addition.
status: released
sources:
- kind: url
  url: https://github.com/bwasserm/sensaor
  title: sensaor (SAO with an adapted SAOAO header)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''unknown''.'
- kind: url
  url: https://github.com/bwasserm/sensaor
  title: 'bwasserm/sensaor: README - senSAOr, a sensor SAO'
  accessed: '2026-09-07'
  note: GitHub repo description ("Sensor SAO for Hackaday Supercon 2024") and README supplied maker, event/year, MCU, LED behavior, connectivity, and confirmed KiCad hardware + Rust firmware are both published in the same repo (pcba/sensaor and src/).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own README and repo metadata confirm what it is, the event it was built for (Hackaday Supercon 2024), the MCU (CH32V003, RISC-V), and LED/sensor behavior. No photos of the assembled board were found in the repo or turned up by search; SAO header pin count/version, price, quantity made, and distribution method (beyond the README's stated goal of making "a bunch" to trade) are not stated anywhere found. WebSearch was unavailable (session search budget exhausted) so press/forum coverage could not be checked.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/sensaor-sao-with-an-adapted-saoao-header.glb
  method: kicad
  source_file: pcba/sensaor/sensaor.kicad_pcb
  generated: '2026-09-10'
  bytes: 171248
---

senSAOr is a Simple Add-On (SAO) that maker bwasserm designed and built in time for Hackaday Supercon 2024. It centers on a CH32V003 RISC-V microcontroller, chosen deliberately (the maker's stated project goals were to use a RISC-V chip and write the firmware in Rust) and reads an analog sensor voltage on an input pin to drive three onboard WS2812/WS2811 addressable LEDs, cycling colors up the board each update. Dedicated input pins let the color mix, update speed, and a sine-wave blending ("shape" and "phase") be set independently, and unused I2C and GPIO pins are broken out for future use.

The board's distinguishing feature is a "SAOAO" port — a secondary header, per the SAOAO specification linked from the README, meant to let a second SAO be daisy-chained behind the first — plus a pad for connecting additional NeoPixels beyond the three built in. The README frames the project's goals plainly: build something in time for Supercon, keep it cheap and simple enough to make a batch and trade with other badge makers, and make the blinky pattern more interesting than a plain blink.

Both the hardware (a KiCad schematic and PCB under `pcba/sensaor/`) and the Rust firmware are published in the same GitHub repository, along with an extensive build log covering the CH32V003 Rust toolchain setup, ADC reads, and bit-banging WS2812 timing over SPI in the absence of a hardware SPI-based NeoPixel driver for that HAL. No photos of an assembled unit, pricing, or quantity-made information were found.
