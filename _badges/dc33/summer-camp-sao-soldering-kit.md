---
title: Summer Camp SAO Soldering Kit
id: dc33-summer-camp-sao-soldering-kit
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc33
year: 2025
makers:
- name: Make it Hackin
  url: https://github.com/MakeItHackin
summary: A $10 beginner soldering kit from Make it Hackin that builds into a small SAO with four RGB LEDs that slowly cycle color when plugged into a host badge's SAO port.
functions: The four through-hole RGB LEDs slowly change color once the assembled SAO is powered from a host badge's SAO connector; no other functions.
look:
  colors: []
  shape: rectangle
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 4
    type: RGB
    note: Through-hole RGB LEDs plus one resistor, soldered by the buyer; passive board with no other components.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: $10.00
  price_usd: 10.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  - kit
  where: Sold on Tindie by MakeItHackin.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit
  url: https://www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit/
  kind: store
- label: github.com/MakeItHackin/SummerCampSAO
  url: https://github.com/MakeItHackin/SummerCampSAO
  kind: repo
images:
- file: assets/images/badges/dc33/summer-camp-sao-soldering-kit/913715de87.jpg
  source: "https://www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit/"
  credit: "Make it Hackin"
  caption: "All kit items laid out: board, LEDs, resistor, stickers"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit/
  title: Summer Camp SAO Soldering Kit
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unclear - may overlap with existing dc33-hacker-summer-camp-sao-soldering-kit entry, worth a cross-check but not created here''.'
- kind: url
  url: https://www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit/
  title: Summer Camp SAO Soldering Kit (Tindie listing)
  accessed: '2026-09-07'
  note: 'Tindie listing gives price $10, describes 4 RGB LEDs / 1 resistor / 1 SAO connector kit, links the GitHub repo, and hosts product photos dated 2024-08-05 (product id 845303) matching the DEF CON 32 timeframe.'
- kind: url
  url: https://github.com/MakeItHackin/SummerCampSAO
  title: MakeItHackin/SummerCampSAO
  accessed: '2026-09-07'
  note: 'Same repo already cited on the dc33-hacker-summer-camp-sao-soldering-kit entry; confirms this is the same kit (board, 4 RGB LEDs, 1 resistor, 1 SAO connector), not a distinct product.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This Tindie listing ("Summer Camp SAO Soldering Kit", $10) appears to be the same physical kit already documented at dc33-hacker-summer-camp-sao-soldering-kit ("Hacker Summer Camp SAO Soldering Kit", $5 per the DC33 community sheet): same maker, same GitHub repo (MakeItHackin/SummerCampSAO), same board contents (4 RGB LEDs, 1 resistor, 1 SAO connector), and the Tindie product photos are dated 2024-08-05, matching that entry''s DEF CON 32 (2024) timing. Filled in from the Tindie listing itself since it is a distinct, citable source, but this is very likely a duplicate listing of the same kit rather than a second product. Left tech.sao_version and look.colors empty/null since the Tindie page and photo available here do not show the header pin count or board colour clearly (the sibling entry states 6-pin/v2 and black/white from its own photos). Quantity made and current availability not stated on the listing.'
last_modified_date: '2026-09-07'
---

The Summer Camp SAO Soldering Kit is a $10 beginner-friendly soldering kit sold on Tindie by Make it Hackin (Huntsville, AL). Builders solder one resistor, four through-hole RGB LEDs and an SAO connector onto a small circuit board; once assembled and plugged into a host badge's SAO port, the LEDs slowly cycle through colors, drawing power entirely from the host badge.

This listing is functionally identical to the archive's dc33-hacker-summer-camp-sao-soldering-kit entry: both point to the same maker GitHub repo (MakeItHackin/SummerCampSAO), describe the same four-LED/one-resistor/one-connector board, and the Tindie product photos are timestamped August 2024, matching that entry's DEF CON 32 timing. The two differ only in listed price ($10 here on Tindie versus $5 on the DC33 community sheet) and exact title wording ("Summer Camp SAO" versus "Hacker Summer Camp SAO"), which most likely reflects the same kit being sold through two channels rather than two separate products.
