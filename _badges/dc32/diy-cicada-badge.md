---
title: DIY Cicada Badge
id: dc32-diy-cicada-badge
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
summary: A cicada-shaped soldering-learning kit that chirps like a real cicada, sold by Hacker Warehouse at DEF CON 32 to raise funds for Hak4Kidz.
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
images:
- file: assets/images/badges/dc32/diy-cicada-badge/c9dab2b816.jpg
  source: "https://hackerwarehouse.com/product/cicada-invada-diy-kit/"
  credit: "Hacker Warehouse"
  caption: "Cicada Invada DIY Kit soldering badge, assembled"
- file: assets/images/badges/dc32/diy-cicada-badge/884364a1ce.jpg
  source: "https://hackerwarehouse.com/product/cicada-invada-diy-kit/"
  credit: "Hacker Warehouse"
  caption: "Cicada Invada DIY Kit, alternate view"
contact:
  emails:
  - questions@hak4kidz.com
notes:
- 'Sheet wording: "Makers have just finished other projects and have started these. More to follow" — an early/in-progress note from before the badge was finalized as the "Cicada Invada" kit.'
- This entry duplicates dc32-cicada-invada-this-wins-the-badge-name-award-thus-far, another sheet row for the same Hak4Kidz product (the "DC32 2024" cicada soldering kit sold via Hacker Warehouse). See that entry for a fuller writeup, including the "Cricket Badge" lineage and a video demo link.
status: released
sources:
- kind: sheet
  event: dc32
  row: 67
  updated: '2024-06-29'
- kind: url
  url: https://hackerwarehouse.com/product/cicada-invada-diy-kit/
  title: Cicada Invada DIY Kit - Hacker Warehouse
  accessed: '2026-09-06'
  note: Full product description, kit contents, price, and product photos, confirming this is the same item as another sheet row for this event.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: This sheet row and dc32-cicada-invada-this-wins-the-badge-name-award-thus-far both describe the same Hak4Kidz "Cicada Invada" soldering kit sold at DC32 through Hacker Warehouse (SKU H4K-CI23) — same maker, same price, same product page. Treated as a duplicate; filled in from the same source rather than left as a stub. Could not find a quantity made or open-source design files.
last_modified_date: '2026-09-06'
---

The DIY Cicada Badge is a soldering-practice kit shaped like a cicada, sold by Hacker Warehouse at DEF CON 32 (2024) to raise money for Hak4Kidz, the nonprofit that runs hands-on security and soldering activities for kids at DEF CON and other events. Hacker Warehouse lists the same product as the "Cicada Invada DIY Kit," an evolution of an earlier "Cricket Badge" design from the same program.

Builders solder a 555 timer, two red LEDs (the cicada's eyes), a potentiometer, a piezo buzzer, and a handful of passives onto the insect-shaped PCB, along with a 9V battery clip. The 555-timer astable circuit drives the piezo to produce a chirping tone, and the potentiometer lets the builder dial the pitch up or down; at low pitch it doubles as a prank noisemaker that can be hidden in a room to sound like a bug got inside. Assembly instructions are reached via a QR code printed on the badge itself, and the kit includes a Hak4Kidz-branded lanyard alongside the electronic parts. It sold for $30.

This entry's sheet row appears to be an earlier, less-detailed listing of the same product — the sheet note ("Makers have just finished other projects and have started these. More to follow") reads like a status update from before the badge had a final name — while the sibling entry dc32-cicada-invada-this-wins-the-badge-name-award-thus-far carries the finished product's playful full name and a video demo.
