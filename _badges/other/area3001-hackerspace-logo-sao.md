---
title: SAO v1.69b Hackerspace Logo
id: other-area3001-hackerspace-logo-sao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2019
makers:
- name: Wim Van Gool (Area 3001)
  url: https://hackaday.io/hacker/187437-wim-van-gool
summary: A Shitty Add-On v1.69bis board that lights up the Area 3001 hackerspace logo by stacking several FR-4 PCBs over WS2812b RGB LEDs so the copper and solder mask act as a light mask and light pipe; the first run used 2020 LEDs on 1 mm boards and was too dim, so it was redone larger with 5050 LEDs.
functions: ''
look:
  colors:
  - multicolor
  shape: logo
  themes:
  - logo
  - hardware tool
tech:
  mcu: none
  leds:
    count: null
    type: WS2812B
    note: First revision used 2020-package WS2812B LEDs; the working revision uses larger 5050-package WS2812B LEDs for brighter light output.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/area3001/SAO-LOGO
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/167548-sao-v169b-hackerspace-logo
  url: https://hackaday.io/project/167548-sao-v169b-hackerspace-logo
  kind: hackaday
- label: github.com/area3001/SAO-LOGO
  url: https://github.com/area3001/SAO-LOGO
  kind: repo
- label: www.youtube.com/watch?v=vAUBq7d2TqY
  url: https://www.youtube.com/watch?v=vAUBq7d2TqY
  kind: video
images:
- file: assets/images/badges/other/area3001-hackerspace-logo-sao/756e7cc0c0.jpg
  source: "https://github.com/area3001/SAO-LOGO"
  credit: "Wim Van Gool / Area 3001"
  caption: "The final 5050-LED version of the Area 3001 logo SAO lit up in color"
- file: assets/images/badges/other/area3001-hackerspace-logo-sao/6b0330c7ed.jpg
  source: "https://github.com/area3001/SAO-LOGO"
  credit: "Wim Van Gool / Area 3001"
  caption: "The stack of separate FR-4 PCB layers that make up the 5050-LED version, unpowered"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/167548-sao-v169b-hackerspace-logo
  title: SAO v1.69b Hackerspace Logo
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/167548-sao-v169b-hackerspace-logo
  title: SAO v1.69b Hackerspace Logo
  accessed: '2026-09-07'
  note: Confirmed maker (Wim Van Gool, Area 3001 hackerspace), creation date (Sept 2019), FR-4 stacked-PCB light-pipe construction, and the switch from 2020 to 5050 LEDs.
- kind: url
  url: https://github.com/area3001/SAO-LOGO
  title: area3001/SAO-LOGO on GitHub
  accessed: '2026-09-07'
  note: README and repo contents confirm two board revisions (AREA3001_S with 2020 LEDs, AREA3001_L with 5050 LEDs), SAO v1.69bis compliance, and source of the two saved photos.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: Fact-check pass (2026-09-07) re-fetched the Hackaday.io project page, the GitHub repo README, and the linked YouTube video; every non-empty field and factual sentence in the body is supported by these sources. This is a one-off/small-batch board made by Area 3001 (a hackerspace in Leuven, Belgium) for its own use, not a badge produced for a specific convention, so no events.yml entry matches it and event is left as "other". No price, quantity, or MCU/chip is mentioned anywhere in the project page, repo, or README; the board is passive (LEDs only, driven by the host badge's SAO header) with no onboard microcontroller. Design files (KiCad/Gerber-style folders "AERA3001_L" and "AREA3001_S") are on GitHub but the README does not state a license or EDA tool, so open_source is marked partial rather than yes. tech.battery ("powered by host badge") is an inference from the board being a passive SAO with no onboard power source, not an explicit quote from a source.
last_modified_date: '2026-09-07'
---

Area 3001, a hackerspace in Leuven, Belgium, built this SAO (Shitty Add-On, v1.69bis header) as a lit-up version of its own hackerspace logo. Instead of a microcontroller and firmware, the effect comes entirely from the physical stack-up: several thin FR-4 PCB layers are stacked on top of a set of WS2812B addressable RGB LEDs, with copper fill and solder-mask openings on the layers acting as a light mask and light pipe so the logo shape glows in color while the rest of the board stays dark.

The first version, built with compact 2020-package WS2812B LEDs on thin (around 1 mm) boards, didn't put out enough light to make the logo legible, so the design was redone at a larger size using bigger 5050-package LEDs, which gave a clean, bright result. Maker Wim Van Gool documented both attempts on Hackaday.io in September 2019, with photos of the PCB stack and a short YouTube clip showing the finished board cycling colors.

## Make your own

The design files live in the `area3001/SAO-LOGO` GitHub repository, split into an `AREA3001_S` folder (the smaller, dimmer 2020-LED version) and an `AERA3001_L` folder (the larger, brighter 5050-LED version that actually worked). The repository does not state a license or which EDA tool was used, so treat the files as available to reference rather than confirmed open-source.
