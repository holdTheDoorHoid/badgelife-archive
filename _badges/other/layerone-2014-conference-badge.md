---
title: LayerOne 2014 Conference Badge
id: other-layerone-2014-conference-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2014
makers:
- name: charliex
  url: https://hackaday.io/charliex
- name: arko
  url: https://hackaday.io/arko
summary: 'The LayerOne 2014 conference badge doubled as a Proxmark3-class RFID tool, able to clone, replay, capture and analyze both 125kHz and 13.56MHz tags.'
functions: 'RFID reading/writing/cloning/replay/capture/analysis for 125kHz and 13.56MHz tags, with an onboard OLED display and SD card for standalone use; also served as the physical admission badge for the conference.'
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - hardware tool
tech:
  mcu: STM32F103RET6
  leds: null
  display: 128x64 OLED
  connectivity:
  - rfid
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Given to LayerOne 2014 attendees as the conference admission badge; not sold commercially.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: Eagle
links:
- label: hackaday.io/project/27-layerone-2014-conference-badge
  url: https://hackaday.io/project/27-layerone-2014-conference-badge
  kind: hackaday
images:
  - file: assets/images/badges/other/layerone-2014-conference-badge/57c97fcb5b.jpg
    source: "https://hackaday.io/project/27-layerone-2014-conference-badge"
    credit: "charliex / arko"
    caption: "LayerOne 2014 conference badge"
  - file: assets/images/badges/other/layerone-2014-conference-badge/4a3be4341d.jpg
    source: "https://hackaday.io/project/27-layerone-2014-conference-badge"
    credit: "charliex / arko"
    caption: "LayerOne 2014 badge assembly/prototype photo"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/27-layerone-2014-conference-badge
  title: LayerOne 2014 Conference Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''LayerOne 2014''.'
- kind: url
  url: https://hackaday.io/project/27-layerone-2014-conference-badge
  title: LayerOne 2014 Conference Badge (Hackaday.io project page)
  accessed: '2026-09-07'
  note: 'Confirmed makers (charliex and arko), STM32F103RET6-based RFID reader/cloner design with 128x64 OLED and SD card, Eagle CAD schematics in the linked SVN repo, and gallery photos of the built badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'LayerOne is not in _data/events.yml, so event is left as "other"; this badge was made for LayerOne 2014 (a Los Angeles-area hacker conference). Sources vary slightly on the exact FPGA (Spartan 3 vs Spartan II) and CPU (STM32 vs AT91SAM7) used across design revisions; the project page''s own build notes cite an STM32F103RET6 with a Spartan-family FPGA, which is what is recorded here. Price, quantity made, LED count, and a working link to the design-file repository could not be confirmed and are left empty. The project appears related to charliex''s Proxmark3 work and to a separate 2013 LayerOne badge project; those are different entries if present.'
last_modified_date: '2026-09-07'
---

The LayerOne 2014 conference badge, built by charliex and arko for the LayerOne security conference in Los Angeles, doubled as a functional RFID research tool. Based on an STM32F103RET6 ARM Cortex-M3 microcontroller paired with an FPGA, it carried "all the features of the Proxmark3 RFID tool" — the ability to read, clone, replay, capture, and analyze both 125kHz and 13.56MHz tags — plus a 128x64 OLED display and an SD card slot so captured data could be reviewed and stored without a computer attached. The board connected over USB and, alongside its RFID toolkit, also served as attendees' physical admission badge for the conference.

Design files, including Eagle CAD schematics, were shared through a linked SVN repository referenced on the project's Hackaday.io page, though a working mirror of that repository could not be located during this research pass. The badge was made in limited numbers for LayerOne 2014 attendees and was not sold commercially; charliex went on to build further LayerOne badges in subsequent years, including a 2017 electronic badge later listed on Tindie.
