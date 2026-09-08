---
title: BADGEr
id: other-badger
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2013
makers:
- name: Anool Mahidharia
  url: https://hackaday.io/anool-mahidharia
summary: An Arduino-compatible e-paper conference badge that keeps showing its image with zero power draw once set.
functions: Displays a static image (personal info, a company logo, or a conference schedule) on an e-paper panel; the image persists with no power once written, so the badge only draws current briefly while updating the display.
look:
  colors: []
  shape: null
  themes:
  - wearable
tech:
  mcu: Arduino-compatible
  leds: null
  display: 2.7" e-paper (Pervasive Displays / Repaper.org panel)
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed as a conference badge at OSHWS (Open Source Hardware Summit) 2013; EPD library and related boards were also sold through Seeed Studio and Maker Shed.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/wyolum/EPD
  eda_tool: null
links:
- label: hackaday.io/project/231-badger
  url: https://hackaday.io/project/231-badger
  kind: hackaday
- label: github.com/wyolum/EPD
  url: https://github.com/wyolum/EPD
  kind: repo
  archived: https://web.archive.org/web/20251213064551/https://github.com/wyolum/EPD
images:
- file: assets/images/badges/other/badger/37c5004204.jpg
  source: https://hackaday.io/project/231-badger
  credit: Anool Mahidharia
  caption: BADGEr e-paper conference badge
contact: {}
notes:
- Sheet listed the event as unknown; sources point to OSHWS 2013, but no matching event id exists yet in events.yml (closest existing entry, oshwdem-2017, is a different event/year), so event is left as 'other'.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/231-badger
  title: Badger
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/231-badger
  title: BADGEr Hackaday.io project page
  accessed: '2026-09-07'
  note: Confirmed maker (Anool Mahidharia, with Justin and Kevin on code), that it is an e-paper badge distributed at OSHWS 2013, display sourced from Pervasive Displays via Repaper.org, and og:image used for the saved photo.
- kind: url
  url: https://github.com/wyolum/EPD
  title: wyolum/EPD
  accessed: '2026-09-07'
  note: Electronic paper display library/examples repo referenced by the project; no explicit mention of BADGEr, OSHWS, or license found in the fetched excerpt.
  archived: https://web.archive.org/web/20251213064551/https://github.com/wyolum/EPD
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, purpose, e-paper tech, OSHWS 2013 distribution) come from the maker's own Hackaday.io project page. Price, quantity made, exact MCU model, and firmware license were not stated on the pages fetched. The wyolum/EPD repo appears to be the associated library but the fetched excerpt did not explicitly link it to this badge by name, so hardware_url is left empty and open_source is marked partial (firmware only) pending direct confirmation.
last_modified_date: '2026-09-07'
---

BADGEr is a miniature e-paper "badge that thinks it's an e-reader," built by Anool Mahidharia (with Justin and Kevin contributing code) and distributed as a conference badge at the 2013 Open Source Hardware Summit (OSHWS). It pairs an Arduino-compatible board with a 2.7-inch electronic paper display sourced from Pervasive Displays via Repaper.org, and its defining trick is that the display keeps showing whatever image was last written to it — a name badge, a company logo, a schedule — without drawing any power at all, so the board only needs current briefly during an update.

The project's e-paper driver code lives in the wyolum/EPD repository on GitHub, which supplies libraries and examples for working with the panel; related e-paper boards and shields from the same ecosystem were also sold commercially through Seeed Studio and Maker Shed around the same period, though it is not confirmed those listings were this specific badge rather than the underlying shield hardware.

No matching "OSHWS 2013" event exists yet in this archive's event list, so this entry stays filed under "Other" until one is added.
