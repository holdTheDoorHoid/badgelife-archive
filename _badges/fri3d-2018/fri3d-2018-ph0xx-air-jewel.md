---
title: Ph0xx Air Jewel
id: fri3d-2018-fri3d-2018-ph0xx-air-jewel
layout: badge
parent: Fri3d 2018
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: fri3d-2018
year: 2018
makers:
- name: Wim Van Gool
  url: https://hackaday.io/wim-van-gool
- name: Fri3d Camp
  url: https://github.com/Fri3dCamp
summary: An air-quality expansion "jewel" for the Fri3d Camp 2018 Ph0xx badge, adding a particulate-matter sensor, an environmental sensor, and GPS so a badge could be turned into a portable air-quality monitor.
functions: Measures fine dust/particulate matter and ambient pressure, humidity, temperature and gas via onboard sensors, with GPS for location-tagging readings; plugs into and is powered from the Ph0xx badge.
look:
  colors: []
  shape: null
  themes:
  - measurement
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - gps
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Built by attendees in a Fri3d Camp 2018 workshop as an add-on to the Ph0xx badge; not sold separately as far as sources show.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/Fri3dCamp/Fri3dBadge
  url: https://github.com/Fri3dCamp/Fri3dBadge
  kind: repo
- label: hackaday.io/project/160534-ph0xx-air-jewel
  url: https://hackaday.io/project/160534-ph0xx-air-jewel
  kind: hackaday
  archived: https://web.archive.org/web/20260122045256/https://hackaday.io/project/160534-ph0xx-air-jewel
- label: web.archive.org/web/2019/wiki2018.fri3d.be/index.php?title=Badge
  url: https://web.archive.org/web/2019/http://wiki2018.fri3d.be/index.php?title=Badge
  kind: website
- label: www.dustcube.be/2018/06/01/air-jewel-voor-badgefri3d-be-2018-meet-fijn-stof
  url: http://www.dustcube.be/2018/06/01/air-jewel-voor-badgefri3d-be-2018-meet-fijn-stof/
  kind: website
images:
- file: assets/images/badges/fri3d-2018/fri3d-2018-ph0xx-air-jewel/178257e7f7.jpg
  source: https://hackaday.io/project/160534-ph0xx-air-jewel
  credit: Wim Van Gool / Fri3d Camp
  caption: The Ph0xx Air Jewel expansion board
  archived: https://web.archive.org/web/20260122045256/https://hackaday.io/project/160534-ph0xx-air-jewel
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Fri3dCamp/Fri3dBadge
  title: Fri3dCamp/Fri3dBadge - Arduino library for the Fri3d Camp badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/160534-ph0xx-air-jewel
  title: Ph0xx Air Jewel project page (Hackaday.io)
  accessed: '2026-09-07'
  note: 'Main source: maker (Wim Van Gool), sensors (SDS011 particulate sensor, BME680/BMP680 environmental sensor, SX1308 step-up converter), GPS capability, and the weather-balloon flight where the dust sensor failed below -61C. Also source of the project photo used here.'
  archived: https://web.archive.org/web/20260122045256/https://hackaday.io/project/160534-ph0xx-air-jewel
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: |
    Could not reach www.dustcube.be (DNS failure) or the archived wiki2018.fri3d.be page (fetch tool blocked web.archive.org) to cross-check the Dutch-language coverage, so price, quantity built, and exact distribution method remain unconfirmed. The Fri3dCamp/Fri3dBadge and Fri3dCamp/badge GitHub repos do not appear to contain Air Jewel-specific hardware/firmware files (search of repo contents found no "jewel"/"dust"/"GPS"-named files), so make_your_own fields are left empty rather than guessed. Hackaday.io project is the primary source; it doesn't state MCU, LED, price or quantity, so those stay null/empty.
last_modified_date: '2026-09-07'
---

The Ph0xx Air Jewel is an expansion module built at Fri3d Camp 2018 for the Fri3d Camp's Ph0xx badge, turning it into a portable air-quality monitor. It was designed by Wim Van Gool with Fri3d Camp and combines an SDS011 particulate-matter (fine dust) sensor with a BME680-family environmental sensor for pressure, humidity, temperature and gas, plus GPS so readings could be tagged with location. An SX1308 step-up converter supplies the 5V the sensors need from the badge's lower supply voltage.

The most notable use of the Jewel was a Fri3d Camp weather-balloon flight, where a Ph0xx badge fitted with the Air Jewel was sent aloft to sample air quality at altitude. The dust sensor stopped working once temperatures dropped to around -61C, but the flight otherwise demonstrated the module's intended purpose as a field air-quality logger.

Sources reviewed do not state a price, production quantity, or whether the Jewel was distributed beyond the workshop that produced it; it reads as a one-off/small-batch build tied to that Fri3d Camp 2018 session rather than a badge sold on its own. No dedicated hardware or firmware repository for the Jewel itself was located separately from the general Fri3d badge codebase.
