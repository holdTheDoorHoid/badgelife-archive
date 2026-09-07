---
title: Penghicorn
id: other-penghicorn
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: davedarko
  url: https://hackaday.io/davedarko
- name: deantonious
  role: contributor
- name: Stefan Kremser
  role: contributor
summary: 'An unofficial conference badge made for 35C3 (2018), combining a penguin and a unicorn, with touch-sensitive horn/beak buttons and support for Shitty Add-Ons.'
functions: 'Runs on an ESP8266; drives a 1.3" OLED display and a Neopixel/WS2812 RGB LED, with a single push button and touch-sensitive horn and beak buttons handled by an onboard ATtiny45. Can talk over NRF24L01 (2.4GHz) or CC1101 (sub-GHz) radio, with a PCF8574 I/O expander for extra pins.'
look:
  colors: []
  shape: null
  themes:
  - animal
  - bird
  - mascot
tech:
  mcu: ESP8266
  leds:
    count: 1
    type: WS2812B
    note: Neopixel
  display: 1.3" OLED (SH1106)
  connectivity:
  - wifi
  - sub-ghz
  battery: LiPo or 3x AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Given to attendees at 35C3 (2018); a group around Spacehuhn commissioned davedarko to design it.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/davedarko/pengicorn
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/162293-penghicorn
  url: https://hackaday.io/project/162293-penghicorn
  kind: hackaday
- label: github.com/davedarko/pengicorn
  url: https://github.com/davedarko/pengicorn
  kind: repo
images:
  - file: assets/images/badges/other/penghicorn/69ce4ac38d.jpg
    source: "https://hackaday.io/project/162293-penghicorn"
    credit: "davedarko"
    caption: "Penghicorn badge for 35C3"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/162293-penghicorn
  title: Penghicorn
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/162293-penghicorn
  title: Penghicorn
  accessed: '2026-09-07'
  note: 'Confirmed maker (davedarko, with deantonious and Stefan Kremser), event (35C3, 2018), and hardware details (ESP8266, OLED, NRF24L01, CC1101, PCF8574, ATtiny45 touch controller, WS2812 LED).'
- kind: url
  url: https://github.com/davedarko/pengicorn
  title: davedarko/pengicorn
  accessed: '2026-09-07'
  note: 'Hardware repository (KiCad/Eagle badge files, SAO folder, Alpha and OSH Park revisions); confirms open hardware.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'No 35C3 event id exists in _data/events.yml (only Chaos Communication Camp 2019 is present), so event is left as "other"; this badge was made for 35C3 (Chaos Communication Congress), 2018. Price, quantity made, and availability were not stated in any source found. No firmware repo link was found separately from the hardware repo. SAO header pin version not confirmed by sources.'
last_modified_date: '2026-09-07'
---

The Penghicorn is an unofficial hardware badge created for 35C3, the 35th Chaos Communication Congress, held in December 2018. A group around the Spacehuhn hacking collective asked designer davedarko to build the badge, which he developed with contributions from deantonious and Stefan Kremser. Its name and look combine a penguin and a unicorn, complete with a touch-sensitive horn and beak.

Under the hood it runs an ESP8266 microcontroller paired with a 1.3-inch OLED display, a single Neopixel RGB LED, and a push button. davedarko added a PCF8574 I/O expander for extra pins and an ATtiny45 to turn the badge's horn and beak into capacitive touch buttons. For wireless communication the badge carries both an NRF24L01 2.4GHz radio and a CC1101 sub-GHz radio, and it can run from either a LiPo battery or three AAA cells. The hardware design is published on GitHub (davedarko/pengicorn), including alpha and OSH Park production revisions plus a separate SAO folder, making the project open source, though no separate firmware repository was located.
