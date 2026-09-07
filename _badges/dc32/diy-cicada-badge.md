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
  availability: sold_out
  distribution:
  - purchase
  where: Purchase from Hacker Warehouse at DC 32
  availability_note: Tindie listing for the same product shows sold out since 2024-09-22; Hacker Warehouse listing was in stock as of 2026-09-06.
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
- kind: store
  label: Tindie listing (Cicada Invada DC32 2024 Badge)
  url: https://www.tindie.com/products/h4klab/cicada-invada-dc32-2024-badge/
images:
- file: assets/images/badges/dc32/diy-cicada-badge/c9dab2b816.jpg
  source: https://hackerwarehouse.com/product/cicada-invada-diy-kit/
  credit: Hacker Warehouse
  caption: Cicada Invada DIY Kit soldering badge, assembled
- file: assets/images/badges/dc32/diy-cicada-badge/884364a1ce.jpg
  source: https://hackerwarehouse.com/product/cicada-invada-diy-kit/
  credit: Hacker Warehouse
  caption: Cicada Invada DIY Kit, alternate view
- file: assets/images/badges/dc32/diy-cicada-badge/8b9f52ccbc.jpg
  source: https://hackerwarehouse.com/product/cicada-invada-diy-kit/
  credit: Hacker Warehouse
  caption: Assembled Cicada Invada DIY soldering kit, DC32 2024
- file: assets/images/badges/dc32/diy-cicada-badge/dcc5b02e65.jpg
  source: https://hackerwarehouse.com/product/cicada-invada-diy-kit/
  credit: Hacker Warehouse
  caption: Unpopulated Cicada Invada PCB before assembly
contact:
  emails:
  - questions@hak4kidz.com
notes:
- 'Sheet wording: "Makers have just finished other projects and have started these. More to follow" — an early/in-progress note from before the badge was finalized as the "Cicada Invada" kit.'
- This entry duplicates dc32-cicada-invada-this-wins-the-badge-name-award-thus-far, another sheet row for the same Hak4Kidz product (the "DC32 2024" cicada soldering kit sold via Hacker Warehouse). See that entry for a fuller writeup, including the "Cricket Badge" lineage and a video demo link.
- Hacker Warehouse storefront, listed under couture/badgelife category. $30, SKU H4K-CI23. Learn-to-solder badge fundraiser for Hak4Kidz events; evolution of an earlier 'Cricket Badge'; 555-timer piezo buzzer, 2 LEDs, potentiometer. In stock.
- This is the same product already covered in depth by _badges/dc32/diy-cicada-badge.md (id dc32-diy-cicada-badge), which itself merged a second duplicate sheet row. No new images were saved here since that entry already carries four photos of the assembled and unpopulated PCB.
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
- kind: sheet
  event: dc32
  row: 66
  updated: '2024-06-29'
- kind: url
  url: https://www.tindie.com/products/h4klab/cicada-invada-dc32-2024-badge/
  title: Cicada Invada DC32 2024 Badge - Tindie
  accessed: '2026-09-07'
  note: Confirms event/year as DEF CON 32 (2024), maker as Hak4Kidz Lab (Northbrook, IL), and that the Tindie listing sold out 2024-09-22.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: This sheet row and dc32-cicada-invada-this-wins-the-badge-name-award-thus-far both describe the same Hak4Kidz "Cicada Invada" soldering kit sold at DC32 through Hacker Warehouse (SKU H4K-CI23) — same maker, same price, same product page. Treated as a duplicate; filled in from the same source rather than left as a stub. Could not find a quantity made or open-source design files. Merged with duplicate entry 'Cicada Invada (<--- this wins the badge name award thus far)' (dc32-cicada-invada-this-wins-the-badge-name-award-thus-far). Merged with duplicate entry 'Cicada Invada DIY Kit' (dc32-cicada-invada-diy-kit).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc32/cicada-invada-this-wins-the-badge-name-award-thus-far/
- /badges/dc32/cicada-invada-diy-kit/
---

The DIY Cicada Badge is a soldering-practice kit shaped like a cicada, sold by Hacker Warehouse at DEF CON 32 (2024) to raise money for Hak4Kidz, the nonprofit that runs hands-on security and soldering activities for kids at DEF CON and other events. Hacker Warehouse lists the same product as the "Cicada Invada DIY Kit," an evolution of an earlier "Cricket Badge" design from the same program.

Builders solder a 555 timer, two red LEDs (the cicada's eyes), a potentiometer, a piezo buzzer, and a handful of passives onto the insect-shaped PCB, along with a 9V battery clip. The 555-timer astable circuit drives the piezo to produce a chirping tone, and the potentiometer lets the builder dial the pitch up or down; at low pitch it doubles as a prank noisemaker that can be hidden in a room to sound like a bug got inside. Assembly instructions are reached via a QR code printed on the badge itself, and the kit includes a Hak4Kidz-branded lanyard alongside the electronic parts. It sold for $30.

This entry's sheet row appears to be an earlier, less-detailed listing of the same product — the sheet note ("Makers have just finished other projects and have started these. More to follow") reads like a status update from before the badge had a final name — while the sibling entry dc32-cicada-invada-this-wins-the-badge-name-award-thus-far carries the finished product's playful full name and a video demo.

## Notes merged from the duplicate entry "Cicada Invada (<--- this wins the badge name award thus far)"

The Cicada Invada is a soldering-practice kit shaped like a cicada, sold by Hacker Warehouse at DEF CON 32 to raise money for Hak4Kidz, the nonprofit that runs hands-on security and soldering activities for kids at DEF CON and other events. It is described as an evolution of an earlier "Cricket Badge" design from the same program.

Builders solder a 555 timer, two red LEDs (the cicada's eyes), a potentiometer, a piezo buzzer, and a handful of passives onto the insect-shaped PCB, along with a 9V battery clip. The 555-timer astable circuit drives the piezo to produce a chirping tone, and the potentiometer lets the builder dial the pitch up or down; at low pitch it doubles as a prank noisemaker that can be hidden in a room to sound like a bug got inside. Assembly instructions are reached via a QR code printed on the badge itself, and the kit includes a soldering iron cleaner and a Hak4Kidz-branded lanyard alongside the electronic parts. It sold for $30.

## Notes merged from the duplicate entry "Cicada Invada DIY Kit"

The Cicada Invada DIY Kit is a learn-to-solder kit shaped like a cicada, sold by Hacker Warehouse (SKU H4K-CI23) and on Tindie by Hak4Kidz Lab at DEF CON 32 (2024) to raise money for Hak4Kidz, the nonprofit that runs hands-on security and soldering activities for kids. It is described as an evolution of an earlier "Cricket Badge" design from the same program.

Builders solder a 555 timer, two red LEDs (the cicada's eyes), a potentiometer, a piezo buzzer, and a handful of passives onto the insect-shaped PCB, along with a 9V battery clip. The 555-timer astable circuit drives the piezo to produce a chirping tone, and the potentiometer lets the builder dial the pitch up or down; at a low pitch it doubles as a prank noisemaker that can be hidden in a room to sound like a bug got inside. Assembly instructions are reached via a QR code printed on the badge itself, and the kit includes a Hak4Kidz-branded lanyard. It sold for $30; the Tindie listing shows it sold out by September 2024.

This entry duplicates dc32-diy-cicada-badge, which already carries a fuller writeup (including the "Cricket Badge" lineage) and four photos of the assembled and unpopulated PCB, so no new images were saved for this entry.
