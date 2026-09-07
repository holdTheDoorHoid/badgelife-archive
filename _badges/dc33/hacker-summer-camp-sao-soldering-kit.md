---
title: Hacker Summer Camp SAO Soldering Kit
id: dc33-hacker-summer-camp-sao-soldering-kit
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
summary: A beginner through-hole soldering kit from Make it Hackin that builds into a small SAO with four RGB LEDs that slowly change color when plugged into a badge.
functions: It slowly changes color. The four RGB LEDs cycle through colors once the assembled SAO is powered from a host badge's SAO port.
look:
  colors:
  - black
  - white
  shape: rectangle
  themes:
  - learn to solder
  - kit
  form_factor: pcb sao
tech:
  mcu: none
  leds:
    count: 4
    type: RGB
    note: Through-hole RGB LEDs plus one resistor, soldered by the buyer; no other components on the board.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: v2
get_one:
  price: $5
  price_usd: 5.0
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Sold on Tindie by MakeItHackin.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/MakeItHackin/SummerCampSAO
  url: https://github.com/MakeItHackin/SummerCampSAO
  kind: repo
- label: Assembly tutorial (YouTube)
  url: https://youtu.be/E3vtrzXdGKo
  kind: video
- label: www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit
  url: https://www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit/
  kind: store
images:
- file: assets/images/badges/dc33/hacker-summer-camp-sao-soldering-kit/9bb538c890.jpg
  source: https://github.com/MakeItHackin/SummerCampSAO
  credit: Make it Hackin
  caption: Assembled Hacker Summer Camp SAO, front, unpowered
- file: assets/images/badges/dc33/hacker-summer-camp-sao-soldering-kit/0684ca08c0.jpg
  source: https://github.com/MakeItHackin/SummerCampSAO
  credit: Make it Hackin
  caption: Kit contents laid out before assembly
- file: assets/images/badges/dc33/hacker-summer-camp-sao-soldering-kit/913715de87.jpg
  source: https://www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit/
  credit: Make it Hackin
  caption: 'All kit items laid out: board, LEDs, resistor, stickers'
contact:
  emails:
  - andrew@makeithackin.com
notes:
- Teaches you how to solder through-hole components
- Spotted by a research agent while working on a neighbouring entry.
status: listed
sources:
- kind: sheet
  event: dc33
  row: 43
  updated: 8/3/2025 10:50:24
- kind: url
  url: https://github.com/MakeItHackin/SummerCampSAO
  title: MakeItHackin/SummerCampSAO
  accessed: '2026-09-07'
  note: 'README lists the kit''s contents (board, 4 RGB LEDs, 1 resistor, 1 SAO connector, stickers, googly eyes), assembly order, and says it lights up from the badge''s power with slow-changing RGB LEDs. Repo holds only the README and photos: no design files, no license. Repo created July 2024; stickers reference DC32.'
- kind: url
  url: https://www.youtube.com/watch?v=E3vtrzXdGKo
  title: How to Assemble and Solder Your Hacker Summer Camp SAO | DEF CON 32
  accessed: '2026-09-07'
  note: Maker's assembly video on the Make It Hackin channel, published 2024-08-05; the title places the kit at DEF CON 32.
- kind: url
  url: https://www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit/
  title: Summer Camp SAO Soldering Kit
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unclear - may overlap with existing dc33-hacker-summer-camp-sao-soldering-kit entry, worth a cross-check but not created here''.'
- kind: url
  url: https://www.tindie.com/products/makeithackin/summer-camp-sao-soldering-kit/
  title: Summer Camp SAO Soldering Kit (Tindie listing)
  accessed: '2026-09-07'
  note: Tindie listing gives price $10, describes 4 RGB LEDs / 1 resistor / 1 SAO connector kit, links the GitHub repo, and hosts product photos dated 2024-08-05 (product id 845303) matching the DEF CON 32 timeframe.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Verified against the DC33 community sheet row (maker, title, $5, contact email, functions, notes) and the maker''s own GitHub README, repo photos and YouTube video. Board colours, rectangular shape and the 6-pin (v2) SAO header are read from the maker''s photos. mcu: none follows from the README''s complete parts list (4 LEDs, 1 resistor, 1 connector) and the photos showing a bare board. Discrepancy: the maker''s repo (July 2024) and video title ("DEF CON 32", published 2024-08-05) and the DC32 stickers in the bag show this kit was made for DEF CON 32 (2024); the community sheet lists it for DC33 (2025), so it was presumably offered again in 2025. Kept as dc33 per the sheet. open_source left null: the repo has no schematic, Gerbers or firmware. No storefront, quantity or availability found; the sheet''s $5 is the only price source. Merged with duplicate entry ''Summer Camp SAO Soldering Kit'' (dc33-summer-camp-sao-soldering-kit).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc33/summer-camp-sao-soldering-kit/
---

The Hacker Summer Camp SAO is a beginner-friendly soldering kit by Make it Hackin. Builders solder one resistor, four through-hole RGB LEDs and a 6-pin SAO connector onto a small black board printed with a Las Vegas skyline and the words "Learn, Share, Hack", then plug it into a badge's SAO port to see the LEDs slowly change color, powered entirely by the host badge. The bag also holds googly eyes and a few stickers (Hacker Summer Camp, DC32 Engage, Make it Hackin, DC32 Flipboard).

Make it Hackin published a step-by-step README and a companion YouTube video walking through the resistor, LED and connector soldering steps and testing the finished board on a badge simulator. The repo and video date from July and August 2024 and the video title says DEF CON 32, so the kit was made for DC32; it appears on the DC33 community sheet at $5, which is where this entry comes from. No separate storefront listing or production quantity was found.

## Notes merged from the duplicate entry "Summer Camp SAO Soldering Kit"

The Summer Camp SAO Soldering Kit is a $10 beginner-friendly soldering kit sold on Tindie by Make it Hackin (Huntsville, AL). Builders solder one resistor, four through-hole RGB LEDs and an SAO connector onto a small circuit board; once assembled and plugged into a host badge's SAO port, the LEDs slowly cycle through colors, drawing power entirely from the host badge.

This listing is functionally identical to the archive's dc33-hacker-summer-camp-sao-soldering-kit entry: both point to the same maker GitHub repo (MakeItHackin/SummerCampSAO), describe the same four-LED/one-resistor/one-connector board, and the Tindie product photos are timestamped August 2024, matching that entry's DEF CON 32 timing. The two differ only in listed price ($10 here on Tindie versus $5 on the DC33 community sheet) and exact title wording ("Summer Camp SAO" versus "Hacker Summer Camp SAO"), which most likely reflects the same kit being sold through two channels rather than two separate products.
