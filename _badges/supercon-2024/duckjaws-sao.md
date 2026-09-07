---
title: duckJAWS SAO
id: supercon-2024-duckjaws-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Adrian Studer (astuder)
  url: https://github.com/astuder
- name: Marc Merlin
  url: https://github.com/marcmerlin
summary: A shark-shaped SAO from the duckGLOW family with a rubber duck lit by an RGB or UV LED plus side-lit red LEDs for the shark's teeth, driven by a CH32V003 and controllable over I2C or as a WS2812-style addressable LED, entered in the Supercon 8 SAO Contest and later sold assembled on Tindie.
functions: 'Per-channel LED fading with configurable brightness, speed, and phase, set over I2C (default address 0x6C, configurable via solder jumpers) or driven like a WS2812/NeoPixel; settings can be stored as power-on defaults, with a factory reset option. Ships with a default yellow slow-pulse pattern.'
look:
  colors: [red, black]
  shape: shark
  themes: [duck, animal, sci-fi]
tech:
  mcu: CH32V003
  leds:
    count: 4
    type: RGB
    note: One common-anode RGB (or 2-legged UV) LED lights the duck; separate red LEDs side-light the shark's teeth. A 3.3V boost converter keeps brightness consistent across power sources.
  display: none
  connectivity: [i2c]
  battery: powered by host badge
  sao_version: v1
get_one:
  price: $10
  price_usd: 10
  quantity: ''
  availability: unknown
  availability_note: 'Tindie listing checked 2026-09-07 still shows the item, but the seller''s page states the shop is on pause until 2027-05-31 due to "technical problems with Tindie."'
  distribution: [purchase, contest]
  where: Sold assembled (SMT pre-soldered, duck attached with hot glue by the builder) on Tindie by Wegmatt LLC (astuder's storefront); originally entered in the Supercon 8 SAO Contest in October 2024.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/astuder/duckglow
  firmware_url: https://github.com/astuder/duckglow
  eda_tool: null
links:
- label: github.com/astuder/duckglow/tree/master
  url: https://github.com/astuder/duckglow/tree/master
  kind: repo
- label: github.com/astuder/duckglow
  url: https://github.com/astuder/duckglow
  kind: repo
- label: hackaday.io/project/198918-duckglow-sao
  url: https://hackaday.io/project/198918-duckglow-sao
  kind: hackaday
- label: www.tindie.com/products/astuder/duckjaws-sao
  url: https://www.tindie.com/products/astuder/duckjaws-sao/
  kind: store
- label: www.youtube.com/watch?v=yjSSQkx-x7U
  url: https://www.youtube.com/watch?v=yjSSQkx-x7U
  kind: video
images:
  - file: assets/images/badges/supercon-2024/duckjaws-sao/602dd4c0e4.jpg
    source: "https://www.tindie.com/products/astuder/duckjaws-sao/"
    credit: "Adrian Studer (astuder)"
    caption: "duckJAWS SAO: shark-shaped PCB with rubber duck and red LED teeth"
  - file: assets/images/badges/supercon-2024/duckjaws-sao/dfe953f24e.jpg
    source: "https://hackaday.io/project/198918-duckglow-sao"
    credit: "Adrian Studer (astuder)"
    caption: "duckGLOW/duckJAWS SAO project photo"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/astuder/duckglow/tree/master
  title: 'astuder/duckglow: A set of basic SAOs with glowing rubber duckies'
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/astuder/duckglow
  title: 'astuder/duckglow: A set of basic SAOs with glowing rubber duckies'
  accessed: '2026-09-07'
  note: 'Confirmed project scope (duckGLOW family, duckJAWS and duckBATH variants), I2C behavior, LED options, and open-source repo hosting both hardware and firmware.'
- kind: url
  url: https://hackaday.io/project/198918-duckglow-sao
  title: duckGLOW SAO project page
  accessed: '2026-09-07'
  note: 'Confirmed makers (Adrian Studer and Marc Merlin), Supercon 8 SAO Contest / October 2024 timing, CH32V003 MCU, boost converter, and duck/LED assembly details; source of one project photo.'
- kind: url
  url: https://www.tindie.com/products/astuder/duckjaws-sao/
  title: duckJAWS SAO - Tindie listing (Wegmatt LLC)
  accessed: '2026-09-07'
  note: 'Confirmed price ($10), assembled/hot-glue-duck construction, default yellow pulse behavior, and that the storefront is currently paused; source of the product photo.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Quantity made is not stated anywhere found. Availability is ambiguous: the Tindie listing itself is still visible and priced, but the seller''s account-level message says the store is on pause until 2027-05-31, so left as unknown rather than guessing "available" or "sold_out." The GitHub repo covers two PCB variants (duckJAWS, shark-themed, and duckBATH, bathtub-themed); this entry is duckJAWS only.'
last_modified_date: '2026-09-07'
---

The duckJAWS SAO is one of two designs in Adrian Studer (astuder) and Marc Merlin's duckGLOW project, a small family of SAOs built around lighting up a genuine small rubber duck. On duckJAWS, the duck sits in the mouth of a shark-shaped PCB, with an RGB (or UV) LED shining up through the duck via a hole in its base, while additional red LEDs side-light the shark's teeth for what the maker describes as an ominous glow. The board runs a CH32V003 microcontroller with a 3.3V boost converter to keep brightness consistent, and can be driven either over I2C (with a configurable address, default 0x6C) or addressed like a WS2812/NeoPixel LED, with color and animation settings storable as power-on defaults. It was entered in the Supercon 8 SAO Contest in October 2024.

After Supercon, Studer sold assembled units through his Wegmatt LLC storefront on Tindie for $10, pre-soldered with the duck attached by the builder using hot glue (removable and reattachable). As of this check the Tindie listing is still visible and priced, but the storefront carries a notice that it is on pause until May 2027 due to a Tindie technical issue, so current availability is unclear. Hardware and firmware are both published on GitHub under astuder/duckglow, alongside the companion duckBATH (bathtub-themed) variant.

## Make your own

Hardware design files and firmware/example code for both duckJAWS and duckBATH are published at https://github.com/astuder/duckglow. No EDA tool, bill of materials, or license was stated on the pages checked.
