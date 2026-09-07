---
title: Cicada Invada (<--- this wins the badge name award thus far)
id: dc32-cicada-invada-this-wins-the-badge-name-award-thus-far
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Hak4Kidz
  url: https://www.hak4kidz.com/
summary: A cicada-shaped soldering-learning badge that chirps like a real cicada, sold by Hacker Warehouse at DEF CON 32 to raise funds for Hak4Kidz.
functions: Chirps like a cicada with a dial to change the frequency. Lower frequency chirps can be used as a gag in someone's house. Makes them think a bug got inside their home.
look:
  colors:
  - white
  shape: cicada
  themes:
  - animal
  - insect
  - learn to solder
tech:
  mcu: none
  leds:
    count: 2
    type: reverse-mount
    note: Two red LEDs form the cicada's eyes.
  display: none
  connectivity: []
  battery: 9V
  sao_version: none
get_one:
  price: $30.00
  price_usd: 30.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Purchase from Hacker Warehouse at DC 32
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: store
  label: Hacker Warehouse product page
  url: https://hackerwarehouse.com/product/cicada-invada-diy-kit/
- kind: video
  label: Audio demo (YouTube Shorts)
  url: https://youtube.com/shorts/7Asbn2EzBgU
images:
- file: assets/images/badges/dc32/cicada-invada-this-wins-the-badge-name-award-thus-far/8b9f52ccbc.jpg
  source: "https://hackerwarehouse.com/product/cicada-invada-diy-kit/"
  credit: "Hacker Warehouse"
  caption: "Assembled Cicada Invada DIY soldering kit, DC32 2024"
- file: assets/images/badges/dc32/cicada-invada-this-wins-the-badge-name-award-thus-far/dcc5b02e65.jpg
  source: "https://hackerwarehouse.com/product/cicada-invada-diy-kit/"
  credit: "Hacker Warehouse"
  caption: "Unpopulated Cicada Invada PCB before assembly"
contact:
  emails:
  - questions@hak4kidz.com
notes: []
status: released
sources:
- kind: sheet
  event: dc32
  row: 66
  updated: '2024-06-29'
- kind: url
  url: https://hackerwarehouse.com/product/cicada-invada-diy-kit/
  title: Cicada Invada DIY Kit - Hacker Warehouse
  accessed: '2026-09-06'
  note: Full product description, kit contents, price, dimensions, and product photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Product page (SKU H4K-CI23) confirms it as a DIY soldering kit sold through Hacker Warehouse to benefit Hak4Kidz, an evolution of an earlier "Cricket Badge" design. Could not find a maker/designer name beyond the Hak4Kidz org, nor quantity made or open-source design files. Listing images are dated 2025 (product may have been re-listed for a later con) but the badge silkscreen itself reads "DC32 2024", matching this sheet entry.
last_modified_date: '2026-09-06'
---

The Cicada Invada is a soldering-practice kit shaped like a cicada, sold by Hacker Warehouse at DEF CON 32 to raise money for Hak4Kidz, the nonprofit that runs hands-on security and soldering activities for kids at DEF CON and other events. It is described as an evolution of an earlier "Cricket Badge" design from the same program.

Builders solder a 555 timer, two red LEDs (the cicada's eyes), a potentiometer, a piezo buzzer, and a handful of passives onto the insect-shaped PCB, along with a 9V battery clip. The 555-timer astable circuit drives the piezo to produce a chirping tone, and the potentiometer lets the builder dial the pitch up or down; at low pitch it doubles as a prank noisemaker that can be hidden in a room to sound like a bug got inside. Assembly instructions are reached via a QR code printed on the badge itself, and the kit includes a soldering iron cleaner and a Hak4Kidz-branded lanyard alongside the electronic parts. It sold for $30.
