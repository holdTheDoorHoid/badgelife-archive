---
title: Tricorder SAO
id: dc33-tricorder-sao
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: Make it Hackin
  url: https://www.tindie.com/stores/makeithackin/
summary: A Star Trek-inspired light-up SAO shaped like a tricorder, sold as either a standalone rechargeable-battery unit or a badge-powered SAO connector version.
functions: It has tons of blinky lights in the same sequence from The Next Generation. Both versions have an on/off switch; the badge-powered version supports additional LEDs, including scanning LEDs and side-emitting LEDs, since it draws power from the host badge instead of a battery.
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - tv
  - pop culture
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: Li-Ion rechargeable (USB-C) on the battery-powered version; powered by host badge on the SAO-connector version
  sao_version: null
get_one:
  price: $30-$35 SAO / $50 rechargeable battery version
  price_usd: 30.0
  quantity: ''
  availability: limited
  availability_note: 'Checked 2026-09-06 on Tindie: rechargeable version showed 9 units left, SAO-connector version showed zero stock.'
  distribution:
  - purchase
  where: Sold in person at DEF CON 33 (the maker carried some) and at Hacker Warehouse during DEF CON; also listed on Tindie (tindie.com/products/makeithackin/tricorder-sao/).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/MakeItHackin/tricorderSAO
  url: https://github.com/MakeItHackin/tricorderSAO
  kind: repo
  archived: https://web.archive.org/web/20260509064117/https://github.com/MakeItHackin/tricorderSAO/
- label: Tricorder SAO on Tindie
  url: https://www.tindie.com/products/makeithackin/tricorder-sao/
  kind: store
images:
- file: assets/images/badges/dc33/tricorder-sao/71f536ae23.jpg
  source: https://www.tindie.com/products/makeithackin/tricorder-sao/
  credit: Make it Hackin
  caption: Front view of the Tricorder SAO
- file: assets/images/badges/dc33/tricorder-sao/a3f9004843.jpg
  source: https://github.com/MakeItHackin/tricorderSAO
  credit: Make it Hackin
  caption: Back of the badge-powered SAO version showing the SAO connector
  archived: https://web.archive.org/web/20260509064117/https://github.com/MakeItHackin/tricorderSAO/
contact:
  emails:
  - Andrew@makeithackin.com
notes:
- I will have some Tricorders on me. But they are also for sale at Hacker Warehouse during Def Con ($35) I also have a rechargeable battery version in Limited quantities ($50)
status: released
sources:
- kind: sheet
  event: dc33
  row: 41
  updated: 8/3/2025 10:35:40
- kind: url
  url: https://github.com/MakeItHackin/tricorderSAO
  title: MakeItHackin/tricorderSAO
  accessed: '2026-09-06'
  note: Repo README describes the two hardware versions, contents of the bag, and how power/LEDs work; no schematic, firmware, or BOM published in the repo.
  archived: https://web.archive.org/web/20260509064117/https://github.com/MakeItHackin/tricorderSAO/
- kind: url
  url: https://www.tindie.com/products/makeithackin/tricorder-sao/
  title: Tricorder SAO - MakeItHackin - Tindie
  accessed: '2026-09-06'
  note: Storefront listing gives price ($35 for the SAO-connector listing) and live stock counts.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-06'
  notes: Maker's GitHub repo and Tindie listing confirm the item, its two power versions, and pricing, but neither publishes MCU, LED count/type, schematic, or firmware, so those tech fields are left empty rather than guessed. The community sheet's stated price ($30) and Hacker Warehouse price ($35) both appear; Tindie's own listing price is also $35, and the rechargeable battery version is $50, matching the sheet note. Fact-check 2026-09-06 re-opened the repo README and Tindie listing; both describe the cell as lithium-ion, not LiPo (corrected). The $50 rechargeable price and Hacker Warehouse sales rest on the maker's sheet note only.
last_modified_date: '2026-09-06'
---

The Tricorder SAO is a Star Trek: The Next Generation-inspired add-on made by Make it Hackin (Andrew) for DEF CON 33. It ships in a small bag with the SAO itself, a lanyard, googly eyes, decorative claps, and a set of stickers. It comes in two hardware versions that look identical from the front: a standalone battery-powered version with a rechargeable Li-Ion cell and USB-C charge port, and a badge-powered version that plugs into a host badge's SAO header and draws power from it, which allows for a few extra LEDs (described by the maker as "scanning" and "side-emitting" LEDs). Both versions have a physical on/off switch and run through an LED light sequence referencing the show's tricorder prop.

The maker carried units in person at DEF CON 33 and said they were also for sale at Hacker Warehouse during the con for $35, with a separate limited run of the rechargeable battery version at $50. It remained listed on the maker's Tindie store afterward, where a check on 2026-09-06 showed only a handful of the rechargeable version left and the SAO-connector version out of stock. No schematic, firmware, or bill of materials is published in the maker's GitHub repository, which contains only assembly/usage documentation and product photos.
