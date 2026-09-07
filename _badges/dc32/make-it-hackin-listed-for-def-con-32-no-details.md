---
title: FlipBoard Macropad for Flipper Zero
id: dc32-make-it-hackin-listed-for-def-con-32-no-details
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc32
year: 2024
makers:
- name: Make it Hackin
  url: https://github.com/MakeItHackin
summary: A GPIO expansion module that clips onto a Flipper Zero, adding 16 mechanical, RGB-backlit macro buttons and a "blinky mode" LED badge display.
functions: Programs up to 15 custom macro actions (keystrokes, key combos, and text strings) triggered from 16 hot-swap mechanical buttons, tested on Windows, Mac, and Linux; also runs a standalone "blinky mode" with flashing light patterns and custom text/bitmap display, and includes an IR/Sub-GHz sender app (FlipSignal) and a memory-game tutorial app (Simon).
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - kit
tech:
  mcu: null
  leds:
    count: 16
    type: RGB
    note: One RGB LED per button; per-button, per-state color is user-configurable.
  display: null
  connectivity:
  - ir
  - sub-ghz
  battery: powered by host badge
  sao_version: none
get_one:
  price: $40
  price_usd: 40.0
  quantity: ''
  availability: unknown
  availability_note: Product photo on Tindie dates to Nov 2023, so it was already an ongoing product line by DEF CON 32 (Aug 2024), not a badge made specifically for that con.
  distribution:
  - purchase
  - kit
  where: Sold via Tindie and Etsy, fully assembled or as a DIY kit (5-10 minute build, Phillips screwdriver only); attaches directly to a Flipper Zero.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/jamisonderek/flipboard
  eda_tool: null
  license: GPL-3.0 (companion FlipBoard Flipper Zero app/firmware repo)
  notes: The FlipBoard companion apps (FlipKeyboard, FlipBlinky, FlipSignal, Simon) that run on the Flipper Zero are open source under GPL-3.0. No PCB hardware files (KiCad/Gerbers/BOM) for the FlipBoard module itself were found published.
links:
- label: github.com/MakeItHackin/FlipBoard
  url: https://github.com/MakeItHackin/FlipBoard
  kind: repo
- label: github.com/jamisonderek/flipboard
  url: https://github.com/jamisonderek/flipboard
  kind: repo
- label: Tindie listing
  url: https://www.tindie.com/products/32844/
  kind: store
images:
- file: assets/images/badges/dc32/make-it-hackin-listed-for-def-con-32-no-details/1f646207d1.jpg
  source: https://www.tindie.com/products/32844/
  credit: Make It Hackin
  caption: FlipBoard macropad attached to a Flipper Zero
contact: {}
notes:
- Sheet only listed the maker's name for DEF CON 32, with no item name or details.
status: listed
sources:
- kind: sheet
  event: dc32
  row: 76
  updated: ''
- kind: url
  url: https://github.com/MakeItHackin/FlipBoard
  title: MakeItHackin/FlipBoard (GitHub)
  accessed: '2026-09-07'
  note: Overview, features, mechanical hot-swap switches, blinky mode, macro count, assembly options, store links; repo has commits from Dec 2023 through an Aug 7, 2024 upload (the day before DEF CON 32 opened).
- kind: url
  url: https://github.com/MakeItHackin/SummerCampSAO
  title: MakeItHackin/SummerCampSAO (GitHub)
  accessed: '2026-09-07'
  note: Maker's own README for a later (DC33) kit lists "DC32 Flipboard sticker" among leftover swag included in the kit bag, tying the FlipBoard product to DEF CON 32.
- kind: url
  url: https://www.tindie.com/products/32844/
  title: FlipBoard MacroPad Keyboard for Flipper Zero (Tindie)
  accessed: '2026-09-07'
  note: Price ($40), 16 buttons, RGB backlighting, assembly options; product photo timestamped Nov 2023, showing FlipBoard predates DEF CON 32 as an ongoing product.
- kind: url
  url: https://github.com/jamisonderek/flipboard
  title: jamisonderek/flipboard (GitHub)
  accessed: '2026-09-07'
  note: Companion apps (FlipKeyboard, FlipBlinky, FlipSignal, Simon), GPL-3.0 license, confirms maker/store links.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'The DC32 community sheet listed only the maker "Make it Hackin" with no item name. No DC32-specific product from this maker was found; instead the best evidence points to FlipBoard, their ongoing Flipper Zero macropad, being what they had at DEF CON 32: its GitHub repo received an upload on Aug 7, 2024 (the day before DC32 opened), and the maker''s own README for a later kit (SummerCampSAO, sold at DC33) lists a leftover "DC32 Flipboard sticker" among included swag, tying the product name to that con. However, FlipBoard''s Tindie product photo is timestamped Nov 2023, so it was already an established product line rather than something made specifically for DC32 -- this may just be "what they were selling at their table that year," not a DC32-exclusive release. This is the same product already documented under dc33-flipboard-macropad-for-flipper-zero (event dc33, 2025 sheet); no direct confirmation was found that identifies exactly which item(s) they brought to DC32 specifically,
    so confidence is kept low. Web search (WebSearch tool) was unavailable for this task (session budget exhausted); research relied on WebFetch of the maker''s GitHub org/repos and the Tindie listing only.'
last_modified_date: '2026-09-07'
related:
- dc33-flipboard-macropad-for-flipper-zero
---

The DEF CON 32 community badge sheet listed only the maker "Make it Hackin" for 2024, with no item name or description. No standalone DC32 product from this maker could be confirmed, but the maker's own GitHub account shows their FlipBoard macropad for the Flipper Zero was active right around that time: its repository received an upload on August 7, 2024, the day before DEF CON 32 opened, and a later kit's README (for a DC33 soldering kit) lists a leftover "DC32 Flipboard sticker" among included swag, tying the FlipBoard name to that convention.

FlipBoard itself is a GPIO expansion module that clips onto a Flipper Zero, adding 16 hot-swappable mechanical keys with individually configurable RGB backlighting. A companion Flipper Zero app suite (FlipKeyboard, FlipBlinky, FlipSignal, and a Simon memory-game tutorial), published on GitHub under GPL-3.0, lets users assign up to 15 macro actions per key, or run the board in a standalone "blinky mode" showing patterns or custom bitmaps. It was sold on Tindie and Etsy for $40, assembled or as a DIY kit.

Because FlipBoard's product photos date to November 2023, it appears to have already been an established product rather than something made new for DEF CON 32 -- this entry likely represents ongoing sales at their table that year rather than a con-exclusive item. It is the same product already catalogued under the DC33 entry (`dc33-flipboard-macropad-for-flipper-zero`), which has fuller research and confirms it was later listed sold out on Tindie.
