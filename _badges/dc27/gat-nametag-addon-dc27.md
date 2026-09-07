---
title: GAT Nametag Addon (DC27)
id: dc27-gat-nametag-addon-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: "true"
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
summary: An OLED nametag badge addon for DEF CON 27 that keeps your name readable right-side-up no matter how the badge is oriented, using an onboard accelerometer.
functions: Displays the wearer's name on a small OLED in a choice of fixed- and variable-width fonts, using an accelerometer to keep the text upright regardless of orientation; has programmable RGB LEDs with selectable color modes and rear buttons for on-device configuration.
look:
  colors: []
  shape: null
  themes:
  - text
  - wearable
tech:
  mcu: EFM8UB20F64G-B
  leds:
    count: null
    type: RGB
    note: Programmable RGB LEDs with selectable color modes.
  display: 0.91" SSD1306 I2C 128x32 OLED
  connectivity:
  - usb
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: '113 assembled units (plus additional partial "80% kits") as of late July 2019'
  availability: unknown
  distribution:
  - purchase
  where: Distributed at DEF CON 27 via a closed reservation form run by the maker.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: basic.truecontrol.org/dc27/gat-nametag
  url: https://basic.truecontrol.org/dc27/gat-nametag/
  kind: website
- label: GAT Nametag DC27 Addon (Hackaday.io)
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  kind: hackaday
images:
- file: assets/images/badges/dc27/gat-nametag-addon-dc27/d5551f3699.jpg
  source: "https://hackaday.io/project/166453-gat-nametag-dc27-addon"
  credit: "true (trueControl)"
  caption: "GAT Nametag DC27 Addon"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://basic.truecontrol.org/dc27/gat-nametag/
  title: GAT Nametag Addon (DC27)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27''. Page now returns 404 despite still being linked from the site''s own navigation; content confirmed via Hackaday.io project instead.'
- kind: url
  url: https://hackaday.io/project/166453-gat-nametag-dc27-addon
  title: GAT Nametag DC27 Addon
  accessed: '2026-09-07'
  note: Primary source for maker, event/year, MCU, display, sensor, LEDs, features, unit count, and distribution method.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The basic.truecontrol.org project page for this item now 404s even though it is still linked from that site's own nav menu; details instead confirmed via the maker's Hackaday.io project page. Exact firmware/hardware download links, LED count, price, and battery/power details were not found and left empty. This is distinct from the "Nametag SC8" line (a later, different Supercon 8 addon by the same maker/series) already in the archive.
last_modified_date: '2026-09-07'
---

The GAT Nametag Addon was released by the maker "true" (of trueControl / Whiskey Pirates) at DEF CON 27 in 2019 as a badge addon built to the GAT/SAO v1.69bis standard. It centers on a small OLED display that shows the wearer's name in one of several selectable fonts, and it uses an onboard accelerometer to keep the text upright no matter which way the badge is rotated or flipped. Programmable RGB LEDs and a pair of rear buttons round out the hardware, letting the wearer switch fonts, colors, and display modes on the fly.

By late July 2019 the maker had built roughly 113 working units, along with a number of partially-assembled "80% kits," and distributed them at DEF CON 27 through a closed reservation process rather than open retail sale. Firmware (version 0.2.7a) and a REV3 schematic were shared as downloadable files on the project's Hackaday.io page.
