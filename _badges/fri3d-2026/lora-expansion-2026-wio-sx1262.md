---
title: LoRa Kit (2026, Wio-SX1262)
id: fri3d-2026-lora-expansion-2026-wio-sx1262
layout: badge
parent: Fri3d Camp 2026
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: fri3d-2026
year: 2026
makers:
- name: Fri3d Camp
  url: https://fri3d.be/en/badge/
- name: Seeed Studio
  url: https://www.seeedstudio.com
summary: A solder-it-yourself LoRa upgrade kit for the Fri3d Camp 2026 badge, built around Seeed Studio's Wio-SX1262-N module, used camp-wide for a LoRa foxhunt through the woods.
functions: Adds a LoRa transceiver to the main Fri3d Camp 2026 badge. Used at camp for a radio foxhunt (hidden LoRa beacons hidden in the forest, found using homemade directional antennas).
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
  - kit
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - lora
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'nearly 200 (per Seeed Studio/LinkedIn coverage)'
  availability: unknown
  distribution:
  - kit
  where: 'Distributed to Fri3d Camp 2026 attendees as an optional soldering add-on kit for the main event badge; exact sale/distribution channel not stated in sources found.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Fri3dCamp/badge_2026_hw
  firmware_url: null
  eda_tool: null
links:
- label: www.seeedstudio.com/blog/2026/08/31/fri3d-camp-2026-lora-badge-wio-sx1262
  url: https://www.seeedstudio.com/blog/2026/08/31/fri3d-camp-2026-lora-badge-wio-sx1262/
  kind: website
- label: fri3dcamp.github.io/badge_2026/en/lora
  url: https://fri3dcamp.github.io/badge_2026/en/lora/
  kind: doc
- label: github.com/Fri3dCamp/badge_2026_hw
  url: https://github.com/Fri3dCamp/badge_2026_hw
  kind: repo
images:
  - file: assets/images/badges/fri3d-2026/lora-expansion-2026-wio-sx1262/176ec5a7f2.jpg
    source: "https://fri3dcamp.github.io/badge_2026/en/lora/"
    credit: "Fri3d Camp"
    caption: "Wio-SX1262-N LoRa module mounted on the Fri3d Camp 2026 badge"
  - file: assets/images/badges/fri3d-2026/lora-expansion-2026-wio-sx1262/a61275fb5b.jpg
    source: "https://fri3dcamp.github.io/badge_2026/en/lora/"
    credit: "Fri3d Camp"
    caption: "Spiral antenna mounted on the LoRa module"
contact: {}
notes:
- 'The sweep''s title read as "LoRa Expansion (2026, Wio-SX1262)"; Fri3d Camp''s own documentation calls it the "LoRa kit," which is used here as the title.'
- 'Seeed Studio''s own blog post (the sources original link) could not be fetched directly — it sits behind a Cloudflare JS challenge that blocked both WebFetch and curl. Its content was confirmed instead via Fri3d Camp''s own official documentation site (fri3dcamp.github.io/badge_2026/en/lora/) and via the Seeed blog post''s title/snippet as indexed by search, plus corroborating LinkedIn/Facebook posts from Seeed Studio describing the same event ("nearly 200 campers" adding Wio-SX1262 modules for a forest foxhunt).'
status: released
sources:
- kind: url
  url: https://www.seeedstudio.com/blog/2026/08/31/fri3d-camp-2026-lora-badge-wio-sx1262/
  title: LoRa Expansion (2026, Wio-SX1262)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:fri3d); event read as ''fri3d-2026''.'
- kind: url
  url: https://fri3dcamp.github.io/badge_2026/en/lora/
  title: 'LoRa kit - Fri3d 2026'
  accessed: '2026-09-10'
  note: 'Fri3d Camp''s own official assembly/documentation page for the kit: module, antenna options, soldering steps, warnings, and product photos.'
- kind: url
  url: https://github.com/Fri3dCamp/badge_2026_hw
  title: 'Fri3dCamp/badge_2026_hw'
  accessed: '2026-09-10'
  note: 'Open hardware design files repo for the main Fri3d Camp 2026 badge that the LoRa kit plugs into (no separate hardware/firmware repo for the LoRa kit itself was found).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, chip, function, distribution scale, foxhunt use) confirmed via Fri3d Camp''s own docs and corroborating Seeed Studio social posts, but the original Seeed blog post itself could not be loaded (Cloudflare challenge). No price, exact quantity, or dedicated hardware/firmware repo for the LoRa kit specifically was found (it plugs into the open-source main badge, whose own repo is linked). Availability/where-to-get details are unclear beyond "distributed at camp as an optional kit."'
last_modified_date: '2026-09-10'
---

The LoRa kit is an optional, solder-it-yourself expansion for the Fri3d Camp 2026 badge, built around Seeed Studio's Wio-SX1262-N LoRa transceiver module. Rather than a stand-alone SAO or accessory, it is a small kit of parts — the module, a choice of a soldered spiral antenna or an SMA-connector setup paired with an external 5dBi 868MHz antenna — that campers add to their main 2026 badge themselves, following Fri3d Camp's own step-by-step soldering guide.

At Fri3d Camp 2026, roughly 200 campers assembled the kit and used it for a camp-wide LoRa foxhunt: hidden radio beacons scattered through the surrounding woods, tracked down with homemade directional antennas. Seeed Studio, whose module the kit is built on, covered the event on its own blog and social channels as a showcase of the Wio-SX1262 in the field.

The kit is not sold or documented as an independent open-source hardware/firmware project; it plugs into the main Fri3d Camp 2026 badge, whose hardware design files are published at `Fri3dCamp/badge_2026_hw`. No separate repository, firmware, or pricing specific to the LoRa kit was found.
