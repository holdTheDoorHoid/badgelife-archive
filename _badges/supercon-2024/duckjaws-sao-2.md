---
title: duckJAWS SAO
id: supercon-2024-duckjaws-sao-2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Adrian Studer (astuder)
  url: https://hackaday.io/astuder
summary: A shark-shaped SAO from the duckGLOW project that lights a small rubber duck with an RGB or UV LED and adds side-lit red LEDs in the shark's teeth, driven by a CH32V003 and controllable over I2C or as a WS2812-style addressable LED; entered in the Supercon 8 SAO Contest in 2024 and later sold assembled on Tindie.
functions: "Glows a rubber duck seated in the shark's jaws with a common-anode RGB (or 2-legged UV) LED, plus side-lit red LEDs for the teeth. Controllable over I2C (default address 0x6C, four addresses selectable via solder jumpers) with per-channel min/max brightness, fade speed, phase offset, and saveable power-on presets; can also run as a plain WS2812/NeoPixel-protocol addressable LED on GPIO2. Default out-of-box behavior is a slow pulsing yellow glow."
look:
  colors: [black, red, yellow]
  shape: shark
  themes: [animal, duck, sea creature]
tech:
  mcu: CH32V003
  leds:
    count: 2
    type: RGB
    note: One common-anode RGB (or 2-legged UV) LED lights the duck; separate red LEDs side-light the shark's teeth. Onboard 3.3V boost converter keeps brightness consistent across supply voltage.
  display: none
  connectivity: [i2c]
  battery: powered by host badge
  sao_version: v1
get_one:
  price: $10
  price_usd: 10
  quantity: ''
  availability: sold_out
  availability_note: Listed sold out on Tindie as of 2026-09-07; seller page states they are "on break until May 31, 2027" and points buyers to wegmatt.com for other options.
  distribution: [purchase]
  where: Sold assembled and pre-programmed on Tindie (seller Wegmatt LLC, Redmond, WA) after debuting at Supercon 2024; also distributed as a kit (partially-assembled PCB plus unassembled duck/LED for the buyer to solder) alongside the sibling duckBATH variant.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/astuder/duckglow
  firmware_url: https://github.com/astuder/duckglow
  eda_tool: null
  license: MIT
  notes: Repo includes I2C register documentation and firmware examples for both duckJAWS and the duckBATH variant; no separate BOM or Gerber links were found in the pages checked.
links:
- label: hackaday.io/project/198918-duckglow-sao
  url: https://hackaday.io/project/198918-duckglow-sao
  kind: hackaday
- label: github.com/astuder/duckglow
  url: https://github.com/astuder/duckglow
  kind: repo
- label: www.tindie.com/products/astuder/duckjaws-sao
  url: https://www.tindie.com/products/astuder/duckjaws-sao/
  kind: store
images:
  - file: assets/images/badges/supercon-2024/duckjaws-sao-2/602dd4c0e4.jpg
    source: "https://www.tindie.com/products/astuder/duckjaws-sao/"
    credit: "Adrian Studer / Wegmatt LLC"
    caption: "The duckJAWS SAO, a shark-shaped PCB with a rubber duck in its jaws"
  - file: assets/images/badges/supercon-2024/duckjaws-sao-2/dfe953f24e.jpg
    source: "https://hackaday.io/project/198918-duckglow-sao"
    credit: "Adrian Studer"
    caption: "duckGLOW SAO project photo showing the duckJAWS and duckBATH variants"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198918-duckglow-sao
  title: duckGLOW SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/198918-duckglow-sao
  title: duckGLOW SAO
  accessed: '2026-09-07'
  note: Confirmed maker (with Marc Merlin credited on the project), event (Supercon 8 SAO Contest 2024), duckJAWS vs. duckBATH variants, CH32V003 MCU, I2C/WS2812 control, and pulled a project photo.
- kind: url
  url: https://github.com/astuder/duckglow
  title: astuder/duckglow (GitHub)
  accessed: '2026-09-07'
  note: Confirmed hardware/firmware are published, MIT license, I2C register details, and default I2C address/jumper configuration.
- kind: url
  url: https://www.tindie.com/products/astuder/duckjaws-sao/
  title: duckJAWS SAO by astuder - Tindie
  accessed: '2026-09-07'
  note: Confirmed price ($10), sold-out status, seller (Wegmatt LLC), assembled/pre-programmed condition, and pulled the product photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Marc Merlin is credited alongside Adrian Studer on the Hackaday.io project page, but the GitHub repo and Tindie listing name only Adrian Studer (astuder) as maker/seller, so only he is listed under makers. Quantity made was not stated anywhere checked. No separate BOM or Gerber file links were found (only the GitHub repo, which appears to hold both hardware and firmware).'
last_modified_date: '2026-09-07'
---

The duckJAWS SAO is one of two variants of Adrian Studer's duckGLOW project, built for the Supercon 8 SAO Contest at Supercon 2024. Where the sibling duckBATH variant sets the glowing rubber duck in a small bathtub for a "mellow" look, duckJAWS casts the same duck as prey, seating it in the jaws of a shark-shaped PCB and lighting the shark's teeth with red LEDs for what the maker describes as an "ominous glow." Both variants share a CH32V003-driven board with a common-anode RGB (or UV) LED for the duck, an onboard 3.3V boost converter for consistent brightness, and I2C control with four selectable addresses set by solder jumpers; the board can also run as a plain WS2812/NeoPixel-style addressable LED.

After its debut at Supercon, Studer sold the duckJAWS SAO assembled and pre-programmed through his Tindie storefront (as Wegmatt LLC) for $10, alongside a kit version pairing a partially-assembled PCB with the unassembled duck and LED for buyers to finish themselves. As of this research pass the Tindie listing is sold out, with the seller's page noting they are on a break until May 2027 and pointing interested buyers to wegmatt.com instead.

## Make your own

Hardware and firmware for duckGLOW (covering both duckJAWS and duckBATH) are published on GitHub under the MIT license at github.com/astuder/duckglow. The repository includes I2C register documentation and firmware examples covering color/animation control, per-channel brightness and fade settings, and power-on presets; no separate BOM or Gerber download links were found in the pages checked, so anyone rebuilding it would need to work from the repo's source files directly.
