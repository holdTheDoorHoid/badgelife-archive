---
title: L33T Badge Add-On for DEF CON 31 Badge
id: dc31-l33t-badge-add-on-for-def-con-31-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: MakeItHackin
  url: https://www.tindie.com/stores/makeithackin/
series: null
summary: A learn-to-solder add-on that slides into the chamber of the official DEF CON 31 badge, driving four 16-segment LED displays that can spell out words, numbers, or leet speak.
functions: Displays up to four characters (letters, numbers, or leet-speak substitutions) across four 16-segment LED displays; three color-changing LEDs add extra blink/color effects. Character selection is set by soldering jumper pads on the back of the board rather than by firmware.
look:
  colors: []
  shape: rectangle
  themes:
  - text
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 4
    type: 16-segment
    note: Plus three separate color-changing LEDs. No MCU; character display is set by solder-pad jumpers, not programmed.
  display: 16-segment LED x4
  connectivity: []
  inputs: []
  power: 1x AA (of 3 included)
  battery: 1x AA, ~10-12 hours per battery
  sao_version: none
  sao_ports: null
get_one:
  price: $35
  price_usd: 35
  quantity: ''
  availability: sold_out
  availability_note: 'Checked 2026-09-06: Tindie listing (product 30972) shows the item as a past/limited listing; entry notes it also sold at Hacker Warehouse at DC31.'
  distribution:
  - purchase
  where: 'Sold via the maker''s Tindie store ($35, learn-to-solder kit) and, per the entry''s original notes, also available at the Hacker Warehouse booth at DEF CON 31 for those who missed the Tindie drop. Slides into and electrifies a DEF CON 31 badge; kit ships with three AA batteries, stickers, googly eyes, and a mini lanyard for stability.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/MakeItHackin/L33TBadge
  firmware_url: null
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: GitHub repo (MakeItHackin/L33TBadge) hosts assembly instructions, photos, and a parts list (circuit board, 16-segment displays, boost converter, mini lanyard, color-changing LEDs, capacitor, resistors, switch, battery holder) plus a YouTube build tutorial, but does not publish KiCad/Eagle/Gerber design files, firmware, or a license, so it is not a full open-source release.
links:
- label: t.co/lXQ3GK8Xf1
  url: https://t.co/lXQ3GK8Xf1
  kind: website
- label: Tindie listing
  url: https://www.tindie.com/products/30972/
  kind: store
- label: GitHub (MakeItHackin/L33TBadge)
  url: https://github.com/MakeItHackin/L33TBadge
  kind: repo
images:
- file: assets/images/badges/dc31/l33t-badge-add-on-for-def-con-31-badge/ee9b17329f.jpg
  source: "https://www.tindie.com/products/30972/"
  credit: "MakeItHackin"
  caption: "L33T Badge Add-On slotted into a DEF CON 31 badge, displaying leet-speak on four 16-segment LED displays"
contact: {}
notes:
- Currently on sale at Tindie... wait, sold out on Tindie. You have a second chance at DCXXXI at the Hacker Warehouse. May the odds be ever in your favor!!
status: released
sources:
- kind: sheet
  event: dc31
  row: 58
  updated: ''
- kind: url
  url: https://www.tindie.com/products/30972/
  title: L33T Badge Add-On for DEF CON 31 Badge - Tindie
  accessed: '2026-09-06'
  note: Maker name, price ($35), kit contents, battery power, 16-segment display count, and photos.
- kind: url
  url: https://github.com/MakeItHackin/L33TBadge
  title: MakeItHackin/L33TBadge GitHub repository
  accessed: '2026-09-06'
  note: Confirmed parts list and that the repo is documentation/instructions rather than a full hardware+firmware release; no Gerbers, code, or license found.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts (maker, price, kit contents, display count, battery power) confirmed on the maker's own Tindie listing and GitHub repo. Could not find a Hackaday.io project page, a specific units-made/quantity figure, or an explicit open-source license for the GitHub repo, so those fields are left empty/partial. The board has no MCU; character selection is set by solder-pad jumpers, so it is not "programmed" in the usual SAO sense.
last_modified_date: '2026-09-06'
---

The L33T Badge Add-On is a learn-to-solder kit made by MakeItHackin (Huntsville, Alabama) for DEF CON 31. It slides into the chamber of the official DC31 badge, turning the otherwise non-electronic con badge into a small display: four 16-segment LED displays can be wired, via solder-pad jumpers on the back of the board, to spell out up to four characters of a word, a number, or leet speak, alongside three separate color-changing LEDs for extra flair. There's no microcontroller on board — the "programming" is entirely in how a builder solders the jumpers — which makes it a straightforward soldering exercise as much as a badge accessory.

The kit sold for $35 on the maker's Tindie store and included three AA batteries (good for roughly 10-12 hours of runtime each), stickers, googly eyes, and a mini lanyard to help it sit securely on the host badge. According to the entry's original notes, when the Tindie listing sold out, a second batch was available in person at the Hacker Warehouse booth at DEF CON 31. MakeItHackin's GitHub repo hosts assembly photos, a parts list, and a companion YouTube tutorial, but stops short of a full open hardware release — no Gerbers, schematic files, or firmware/license are published there.

## Make your own

No complete open-source hardware files (schematics, PCB layout, or Gerbers) were found; the GitHub repo linked above documents the parts list and assembly process (with a build tutorial video) rather than providing manufacturable design files.
