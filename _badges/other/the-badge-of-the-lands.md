---
title: The Badge of the Lands
id: other-the-badge-of-the-lands
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: Sabas
  url: https://hackaday.io/sabas
- name: Eden Candelas
  url: https://hackaday.io/eden-candelas
- name: Eduardo Wero
  url: https://hackaday.io/eduardo-wero
- name: Gustavo Reynaga
  url: https://hackaday.io/gustavo-reynaga
summary: An unofficial, independently built electronic badge made for Talent Land 2018 in Mexico, with WiFi, an OLED display, and addressable LEDs.
functions: 'Exchanges credentials/contact info between badges over IR and WiFi, mesh networking between badges, and is also documented as capable of WiFi spoofing and deauthentication.'
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
tech:
  mcu: ESP8266 (ESP-WROOM-02)
  leds:
    count: 12
    type: WS2812B
    note: Addressable Neopixel-style LEDs
  display: 128x64 OLED
  connectivity:
  - wifi
  - ir
  battery: 2x cell battery holder
  sao_version: null
get_one:
  price: '199 MXN'
  price_usd: null
  quantity: 'approximately 90 units'
  availability: unknown
  distribution:
  - purchase
  where: Distributed to attendees of Talent Land 2018 in Mexico; exact distribution details (badge sold vs. given, sign-up process) documented in the project's build logs but not fully clear from available sources.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/greenoneo0/BENOTL
  firmware_url: https://github.com/greenoneo0/BENOTL
  eda_tool: KiCad
  license: 'Hardware: CERN Open Hardware Licence v1.2; Firmware: MIT'
links:
- label: hackaday.io/project/58276-the-badge-of-the-lands
  url: https://hackaday.io/project/58276-the-badge-of-the-lands
  kind: hackaday
- label: github.com/greenoneo0/BENOTL
  url: https://github.com/greenoneo0/BENOTL
  kind: repo
images:
  - file: assets/images/badges/other/the-badge-of-the-lands/3e604775fe.jpg
    source: "https://hackaday.io/project/58276-the-badge-of-the-lands"
    credit: "Sabas / Team Badge of the Lands"
    caption: "The Badge of the Lands assembled PCB badge"
  - file: assets/images/badges/other/the-badge-of-the-lands/9a9c7cdda2.jpg
    source: "https://hackaday.io/project/58276-the-badge-of-the-lands"
    credit: "Sabas / Team Badge of the Lands"
    caption: "The Badge of the Lands, assembly / prototype view"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/58276-the-badge-of-the-lands
  title: The Badge of the Lands
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/58276-the-badge-of-the-lands
  title: The Badge of the Lands (project page and build logs)
  accessed: '2026-09-07'
  note: 'Maker, event/year, hardware specs, price, quantity, and repo link.'
- kind: url
  url: https://github.com/greenoneo0/BENOTL
  title: greenoneo0/BENOTL
  accessed: '2026-09-07'
  note: 'Confirmed open hardware (KiCad, CERN OHL v1.2) and firmware (MIT) repository contents.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This was an unofficial/unauthorized badge built by a small team (led by "Sabas") for Talent Land 2018 in Guadalajara, Mexico, not an official con badge. No matching event id exists in _data/events.yml for Talent Land, so event is left as "other" — the con and year are Talent Land 2018. Exact distribution/sale mechanics at the event are not fully clear from the sources read. sao_version and look.colors/shape left empty; sources did not clearly describe enclosure color or shape beyond a rectangular PCB.'
last_modified_date: '2026-09-07'
---

The Badge of the Lands was an independently built, unofficial electronic badge created by a small team led by a maker known as "Sabas," alongside Eden Candelas, Eduardo Wero, and Gustavo Reynaga, for Talent Land 2018, a large technology and innovation festival held in Guadalajara, Mexico. Roughly 90 units were produced and priced around 199 Mexican pesos each.

The badge is built around an ESP8266 (ESP-WROOM-02) WiFi module paired with a 128x64 OLED display and 12 WS2812B addressable LEDs, powered from a two-cell battery holder and programmed through an onboard CP2102 USB-serial converter. Two buttons round out the inputs. Functionally it was designed to exchange contact/credential information between badges over infrared and WiFi and to support mesh networking among badges in the field; the project's own documentation also notes it was capable of WiFi spoofing and deauthentication.

Hardware and firmware were released as open source under the project's GitHub repository (github.com/greenoneo0/BENOTL), with the PCB designed in KiCad under the CERN Open Hardware Licence v1.2 and firmware under the MIT license. The project appears to be inactive/unsupported as of research time, but the design files remain published for anyone who wants to build their own.
