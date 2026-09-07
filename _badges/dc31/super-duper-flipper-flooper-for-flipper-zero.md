---
title: Super Duper Flipper Flooper for Flipper Zero
id: dc31-super-duper-flipper-flooper-for-flipper-zero
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
summary: A GPIO add-on board that turns a Flipper Zero into a wearable electronic conference badge, with color-changing RGB LEDs, a small display, and a 3D-printed lanyard holder.
functions: Runs a "Flashy Mode" of colorful LED lighting, a customizable on-screen text message (SET TEXT), a small video game, and a flashlight mode. Plug-and-play with its own onboard microcontroller; no programming required.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - wearable
tech:
  mcu: null
  leds:
    count: null
    type: RGB
    note: Described only as "color-changing RGB LEDs"; exact count and part not published.
  display: unspecified small display
  connectivity: []
  battery: null
  power: powered by host badge
  sao_version: null
get_one:
  price: $50
  price_usd: 50
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold on Tindie by MakeItHackin (Huntsville, AL); the maker's DC31-era listing also pointed buyers to a second-chance stock at the Hacker Warehouse booth at DEF CON 31. The Tindie listing is now marked "Product Retired."
make_your_own:
  open_source: partial
  hardware_url: https://github.com/MakeItHackin/Flooper
  firmware_url: null
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: The linked GitHub repo (MakeItHackin/Flooper) hosts only the 3D-printable lanyard-holder STL, not schematics, gerbers, or firmware source.
links:
- label: t.co/bMkLSlkfOq
  url: https://t.co/bMkLSlkfOq
  kind: website
- label: Tindie listing (Super Duper Flipper Flooper)
  url: https://www.tindie.com/products/makeithackin/super-duper-flipper-flooper/
  kind: store
- label: MakeItHackin/Flooper (GitHub)
  url: https://github.com/MakeItHackin/Flooper
  kind: repo
  archived: https://web.archive.org/web/20260513103834/https://github.com/MakeItHackin/Flooper
- label: MakeItHackin Tindie store
  url: https://www.tindie.com/stores/makeithackin/
  kind: store
  archived: https://web.archive.org/web/20260503115032/https://www.tindie.com/stores/makeithackin/
images:
- file: assets/images/badges/dc31/super-duper-flipper-flooper-for-flipper-zero/f612517ef4.jpg
  source: https://www.tindie.com/products/makeithackin/super-duper-flipper-flooper/
  credit: MakeItHackin
  caption: Super Duper Flipper Flooper attached to a Flipper Zero
- file: assets/images/badges/dc31/super-duper-flipper-flooper-for-flipper-zero/3be0bc94a6.jpg
  source: https://www.tindie.com/products/makeithackin/super-duper-flipper-flooper/
  credit: MakeItHackin
  caption: Super Duper Flipper Flooper at DEF CON 31
contact: {}
notes:
- Currently on sale at Tindie... wait, sold out on Tindie. You have a second chance at DCXXXI at the Hacker Warehouse. May the odds be ever in your favor!!
status: released
sources:
- kind: sheet
  event: dc31
  row: 57
  updated: ''
- kind: url
  url: https://www.tindie.com/products/makeithackin/super-duper-flipper-flooper/
  title: Super Duper Flipper Flooper - Tindie
  accessed: '2026-09-06'
  note: Confirms maker (MakeItHackin, Huntsville AL), price ($50), features (RGB LEDs, display, 3D-printed holder, lanyard, Flashy Mode, video game, flashlight mode, stickers/googly eyes), two hardware versions (3.3V/5V GPIO powered), retired/sold-out status, and links to the GitHub repo.
- kind: url
  url: https://github.com/MakeItHackin/Flooper
  title: MakeItHackin/Flooper
  accessed: '2026-09-06'
  note: Repo contains only the 3D-printed holder STL, not schematics/gerbers/firmware; confirms no chip/LED-count detail is published.
  archived: https://web.archive.org/web/20260513103834/https://github.com/MakeItHackin/Flooper
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Maker's own Tindie listing and linked GitHub repo confirm what the item is, how it works, and its price/status, but neither source names the microcontroller, exact LED count/part, or display size, and no quantity-made figure is published. The sheet's original link (t.co/bMkLSlkfOq) redirects to the Tindie listing, confirming it as the same item. No hardware/firmware source beyond a 3D-print STL was found.
last_modified_date: '2026-09-06'
---

The Super Duper Flipper Flooper is a GPIO add-on from MakeItHackin (Huntsville, AL) that turns a Flipper Zero handheld into a wearable "Electronic Conference Badge." It draws power directly from the Flipper Zero's GPIO header (a 3.3V version and an older 5V version were both sold) and needs no setup: plug it in and it runs on its own onboard microcontroller. The board adds color-changing RGB LEDs and a small display, and ships with a 3D-printed conference-badge holder, a lanyard, stickers, and a pair of googly eyes for decoration.

On the Flipper Zero it offers a "Flashy Mode" light show, a customizable on-screen text message via a SET TEXT option, a small video game, and a flashlight mode. It sold for $50 on Tindie; MakeItHackin's DEF CON 31-era listing noted that if Tindie stock sold out, backup units would be available at the Hacker Warehouse booth on-site. The listing is now marked "Product Retired" on Tindie.

MakeItHackin published a companion GitHub repo (MakeItHackin/Flooper), but it holds only the STL file for the 3D-printed lanyard holder rather than the board's schematics, firmware, or gerbers, so the hardware itself is not openly documented.
