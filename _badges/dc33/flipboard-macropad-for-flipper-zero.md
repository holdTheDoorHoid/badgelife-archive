---
title: FlipBoard Macropad for Flipper Zero
id: dc33-flipboard-macropad-for-flipper-zero
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc33
year: 2025
makers:
- name: Make it Hackin
  url: https://www.youtube.com/makeithackin
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
  availability: sold_out
  availability_note: Listed sold out on Tindie as of Jun 2, 2025; still shown out of stock with restock signup when checked 2026-09-06.
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
- label: Etsy listing
  url: https://www.etsy.com/listing/1601295558/
  kind: store
images:
- file: assets/images/badges/dc33/flipboard-macropad-for-flipper-zero/d995a2083b.jpg
  source: "https://www.tindie.com/products/32844/"
  credit: "Make It Hackin"
  caption: "FlipBoard macropad attached to a Flipper Zero"
contact:
  emails:
  - Andrew@makeithackin.com
notes:
- Check out the GitHub for more!
status: released
sources:
- kind: sheet
  event: dc33
  row: 44
  updated: 8/3/2025 10:54:16
- kind: url
  url: https://github.com/MakeItHackin/FlipBoard
  title: MakeItHackin/FlipBoard (GitHub)
  accessed: '2026-09-06'
  note: Overview, features, mechanical hot-swap switches, blinky mode, macro count, assembly options, store links
- kind: url
  url: https://www.tindie.com/products/32844/
  title: FlipBoard MacroPad Keyboard for Flipper Zero (Tindie)
  accessed: '2026-09-06'
  note: Price ($40), 16 buttons, RGB backlighting, sold-out status, assembly options
- kind: url
  url: https://github.com/jamisonderek/flipboard
  title: jamisonderek/flipboard (GitHub)
  accessed: '2026-09-06'
  note: Companion apps (FlipKeyboard, FlipBlinky, FlipSignal, Simon), GPL-3.0 license, confirms maker/store links
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: No MCU/chip model, LED part number, or hardware design-file (KiCad/Gerbers/BOM) source was found published for the FlipBoard PCB itself, so tech.mcu and make_your_own.hardware_url are left empty. Type set to "accessory" since it is an add-on module for the Flipper Zero rather than a standalone badge or SAO. Quantity made is not stated anywhere found.
last_modified_date: '2026-09-06'
---

The FlipBoard is a macropad expansion module built by Make It Hackin that clips onto a Flipper Zero and communicates with it over the Flipper's GPIO header. It adds 16 hot-swappable mechanical keys, each with its own RGB backlight, and pairs with a companion Flipper Zero app suite (FlipKeyboard, FlipBlinky, FlipSignal, and a Simon memory-game tutorial) published on GitHub under GPL-3.0. Through the app, users can assign up to 15 macro actions per key — keystrokes, shortcuts, or text strings — confirmed to work when the Flipper is plugged into a Windows, Mac, or Linux host, and can also drop the board into a standalone "blinky mode" that shows flashing patterns or custom text/bitmaps on the button LEDs.

It was sold on Tindie and Etsy for $40, either fully assembled or as a DIY kit that snaps together in 5-10 minutes with just a Phillips screwdriver; it was listed sold out on Tindie as of June 2025 and remained out of stock (with a restock-notification signup) when checked in September 2026. No PCB design files for the FlipBoard hardware itself were found published, so it is open source only in part — the Flipper-side software, not the board design.
