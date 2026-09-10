---
title: CyberAthena
id: supercon-2024-cyberathena
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: ndGarage
  url: https://hackaday.io/ndGarage
summary: An owl-of-Athena themed Simple Add-On with two back-mounted RGB LEDs driven by an IS31FL3196A over the standard SAO header, submitted to the Supercon 8 SAO Contest, with a colourful high-definition silkscreen variant added in October 2024.
functions: Blinks two RGB LEDs (back-mounted, shining through the eyes) via an IS31FL3196A driver over I2C; also doubles as a hand-soldering practice kit for QFN-20 packages.
look:
  colors:
  - black
  - white
  - silver
  - gold
  shape: bird
  themes:
  - owl
  - animal
  - bird
tech:
  mcu: none
  leds:
    count: 2
    type: RGB3528
    note: Driven by an IS31FL3196A 6-channel LED driver (QFN-20) rather than addressable/smart LEDs.
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ndGarage/CyberAthena
  firmware_url: null
  bom_url: https://github.com/ndGarage/CyberAthena/blob/main/CyberAthena-BOM.md
  eda_tool: null
  license: null
  notes: GitHub repo has a bill of materials and product photos, but no schematic, PCB layout, or Gerber files were found; no license is declared on the repo.
links:
- label: hackaday.io/project/171896-cyberathena
  url: https://hackaday.io/project/171896-cyberathena
  kind: hackaday
- label: github.com/ndGarage/CyberAthena
  url: https://github.com/ndGarage/CyberAthena
  kind: repo
  archived: https://web.archive.org/web/20260507211643/https://github.com/ndGarage/CyberAthena
images:
- file: assets/images/badges/supercon-2024/cyberathena/6df8d93227.jpg
  source: https://github.com/ndGarage/CyberAthena
  credit: ndGarage
  caption: CyberAthena owl-shaped SAO, silver/black metallic-armour silkscreen
  archived: https://web.archive.org/web/20260507211643/https://github.com/ndGarage/CyberAthena
- file: assets/images/badges/supercon-2024/cyberathena/0f87f01eb3.jpg
  source: https://github.com/ndGarage/CyberAthena
  credit: ndGarage
  caption: Two assembled CyberAthena boards side by side
  archived: https://web.archive.org/web/20260507211643/https://github.com/ndGarage/CyberAthena
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://hackaday.io/project/171896-cyberathena
  title: CyberAthena
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/171896-cyberathena
  title: CyberAthena project page
  accessed: '2026-09-07'
  note: Confirmed maker, description, features (2x RGB LEDs, IS31FL3196A QFN-20 driver, 4-pin SAO header with SDA/SCL/GND/VCC), Supercon 8 SAO Contest submission, and the October 2024 colourful-silkscreen variant.
- kind: url
  url: https://hackaday.io/ndGarage
  title: ndGarage Hackaday.io profile
  accessed: '2026-09-07'
  note: Maker profile; confirmed maker handle and no separate storefront listed; found the linked GitHub org.
  archived: https://web.archive.org/web/20251010135134/https://hackaday.io/ndGarage
- kind: url
  url: https://github.com/ndGarage/CyberAthena
  title: ndGarage/CyberAthena
  accessed: '2026-09-07'
  note: Repo README describes it as a "soldering kit"; BOM file lists 2x RGB3528 LEDs, IS31FL3196A driver, and a 2x2 2.54mm-pitch header; supplied the two product photos used here; no license or PCB design files present.
  archived: https://web.archive.org/web/20260507211643/https://github.com/ndGarage/CyberAthena
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Price, quantity made, and availability/where-sold are not stated anywhere found (no Tindie or other storefront link located for this item). No schematic or Gerber files were found in the linked GitHub repo, only a BOM and photos, so open_source is marked partial rather than yes. Web search quota was exhausted this session, so only the linked Hackaday and GitHub pages plus the maker profile were checked; a broader search might turn up a storefront listing.
last_modified_date: '2026-09-07'
---

CyberAthena is a Simple Add-On (SAO) by the maker ndGarage, styled as a stylized, armour-plated owl of Athena — a nod to the Greek myth that the owl sat on Athena's blind side so she could see the whole truth. The PCB is cut to the owl's silhouette, with the bird's two eyes doubling as light pipes for a pair of back-mounted RGB3528 LEDs driven by an IS31FL3196A 6-channel LED driver (QFN-20 package) over the badge's I2C bus, connected through a standard 4-pin SAO header (SDA, SCL, GND, VCC). It was submitted to the Supercon 8 SAO Contest in 2024, and in October of that year the maker added a second, more colourful high-definition silkscreen variant alongside the original silver-and-black metallic-armour finish.

ndGarage's GitHub repository for the project doubles it as a hand-soldering practice kit, in keeping with other QFN-soldering-challenge projects from the same maker; it includes a bill of materials and photographs of assembled boards, but no schematic, PCB layout, or Gerber files, and declares no license. No separate storefront, price, production quantity, or availability information was found for CyberAthena during this pass.
