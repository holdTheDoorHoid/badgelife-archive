---
title: Defcon 27 TV3Y3 Badge
id: dc27-defcon-27-tv3y3-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: awkward intelligence
  url: https://hackaday.io/hacker/332977-awkward-intelligence
summary: 'An indie DEF CON 27 badge built as an augmented-reality image target: the front is all artwork meant to be recognized by a phone camera (Vuforia-based AR app, no facial recognition), while the back carries an ATtiny85 in an 8-pin socket driving a Charlieplexed LED matrix, SAO ports, and bare-copper artwork that exposes hack points; the maker funded production by selling their own SAOs on Tindie.'
functions: Recognized as an AR image target by a companion phone app (iOS/Android) for AR content; drives a 12-LED charlieplexed matrix with multiple animations; exposed copper pads and an 8-pin ATtiny85 socket invite hardware hacking.
look:
  colors:
  - black
  - gold
  shape: null
  themes:
  - sci-fi
  - robot
  - security
tech:
  mcu: ATtiny85
  leds:
    count: 12
    type: charlieplexed
    note: Twelve LEDs driven in a charlieplexed matrix by the ATtiny85.
  display: none
  connectivity: []
  battery: 2x coin/AAA cell (unspecified), rated over a week of runtime
  sao_version: v1
  sao_ports: 2
get_one:
  price: $50
  price_usd: 50
  quantity: '118'
  availability: sold_out
  availability_note: 'Tindie listing checked 2026-09-07: seller page shows "This seller is taking a break," no stock offered.'
  distribution:
  - purchase
  where: Sold by the maker (Harbinger LTD / awkwardai) on Tindie around DEF CON 27 (2019).
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/164210/files
  firmware_url: null
  gerbers_url: https://hackaday.io/project/164210/files
  eda_tool: null
  notes: Final Gerbers ("Finaltv3y3") posted as a project file on Hackaday.io; no BOM, schematic, or firmware source found published.
links:
- label: hackaday.io/project/164210-defcon-27-tv3y3-badge
  url: https://hackaday.io/project/164210-defcon-27-tv3y3-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260508164750/https://hackaday.io/project/164210-defcon-27-tv3y3-badge
- label: hackaday.io/project/164210/files
  url: https://hackaday.io/project/164210/files
  kind: hackaday
- label: youtu.be/1c3xUFGXntY
  url: https://youtu.be/1c3xUFGXntY
  kind: video
- label: TV3Y3 Indie Badge for DEF CON 27 (Tindie)
  url: https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
  kind: store
  archived: https://web.archive.org/web/20260503123834/https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
images:
- file: assets/images/badges/dc27/defcon-27-tv3y3-badge/b6e3d0133b.jpg
  source: https://hackaday.io/project/164210-defcon-27-tv3y3-badge
  credit: awkward intelligence
  caption: TV3Y3 badge front, alien eyeball AR image-target artwork
  archived: https://web.archive.org/web/20260508164750/https://hackaday.io/project/164210-defcon-27-tv3y3-badge
- file: assets/images/badges/dc27/defcon-27-tv3y3-badge/982cb14e59.jpg
  source: https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
  credit: awkward intelligence
  caption: TV3Y3 badge product photo from the Tindie listing
  archived: https://web.archive.org/web/20260503123834/https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/164210-defcon-27-tv3y3-badge
  title: Defcon 27 TV3Y3 Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260508164750/https://hackaday.io/project/164210-defcon-27-tv3y3-badge
- kind: url
  url: https://hackaday.io/project/164210/files
  title: Defcon 27 TV3Y3 Badge - Files
  accessed: '2026-09-07'
  note: Confirmed gerber files ("Finaltv3y3") are the only published design files; no BOM/schematic/firmware found.
- kind: url
  url: https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
  title: TV3Y3 Indie Badge for DEF CON 27 (Tindie, Harbinger LTD)
  accessed: '2026-09-07'
  note: Price ($50), two SAO ports, 8-pin chip holder, battery life ("over a week"), and current sold-out/unavailable status.
  archived: https://web.archive.org/web/20260503123834/https://www.tindie.com/products/awkwardai/tv3y3-indie-badge-for-def-con-27/
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  accessed: '2026-09-07'
  note: Confirmed 118 units made, ATtiny85 driving a 12-LED charlieplexed matrix, and the AR/fiducial purpose.
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No BOM, schematic, or firmware source was located, so make_your_own.firmware_url stays empty. Battery cell type/count not stated precisely by any source beyond "a single set of batteries" giving over a week of runtime, so tech.battery is left as an approximate description rather than a specific cell spec. look.colors/shape are inferred loosely from photos (dark PCB with gold/copper exposed artwork, eyeball-shaped graphic) and may be worth a closer look if higher-res images turn up.
last_modified_date: '2026-09-07'
---

The TV3Y3 badge was an independent DEF CON 27 (2019) badge from the maker "awkward intelligence" (Harbinger LTD), built around an unusual premise: the badge's own artwork is the interactive element. The front is covered in a Vuforia-recognizable image — styled as a severed alien robotic eyeball — that a companion AR app (iOS/Android) can track and use to overlay content, explicitly framed by the maker as an alternative to facial-recognition-based AR. The back holds the actual electronics: an ATtiny85 seated in an 8-pin socket drives a charlieplexed matrix of twelve LEDs through a few animation patterns, while bare copper traces and pads are deliberately exposed as hack points for anyone who wants to reprogram or rewire the board. Two SAO headers let it host add-ons, and the maker sold their own SAOs separately on Tindie to help fund the badge's production run of 118 units, sold at $50 each; by the maker's own account the project barely broke even.

The badge is documented on Hackaday.io alongside a project video and a set of "Final Gerbers" files, but no bill of materials, schematic, or firmware source has been published — the gerbers appear to be the only build file the maker released. The Tindie storefront that originally sold the badge is now inactive ("this seller is taking a break"), consistent with the badge being a one-time 2019 DEF CON release rather than an ongoing product.

## Make your own

Final gerber files ("Finaltv3y3") for the PCB are posted as a project file on the Hackaday.io page; no schematic, BOM, or firmware source code has been found, so a from-scratch rebuild would require reverse-engineering the ATtiny85 firmware and re-deriving a BOM from the gerbers and photos.
