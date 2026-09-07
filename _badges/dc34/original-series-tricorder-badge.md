---
title: Original Series Tricorder badge
id: dc34-original-series-tricorder-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: MakeItHackin
  url: https://github.com/MakeItHackin
summary: 'A working Star Trek: The Original Series tricorder prop badge with two displays, real sensors, and a detachable magnetic hand scanner, built to mark 60 years of Star Trek.'
functions: Celebrate 60 years of Star Trek with this Original Series Tricorder Badge featuring various sensors! Ten on-device menus (Con Mode, Sensors, Animations, Clock, Games, Input devices, NFC/RFID, WiFi, Bluetooth, Settings), five built-in games (Quadrant Invaders, Battle of Wolf 359, Shuttle Pod Lander, Cargo Bay Stacker, Gagh), a detachable hand scanner that triggers a medical-scan mode via a magnet sensor, USB HID keyboard/mouse emulation, and an onboard NFC tag that shares the project link when tapped.
look:
  colors: []
  shape: handheld device
  themes:
  - sci-fi
  - tv
tech:
  mcu: XIAO ESP32-S3
  leds:
    count: 3
    type: RGB
    note: three addressable RGB LEDs on the front
  display: 1.69" IPS main display (280x240) plus a 1.28" round secondary display
  connectivity:
  - wifi
  - ble
  - bluetooth
  - nfc
  - usb
  inputs:
  - buttons
  - accelerometer
  battery: USB-C rechargeable LiPo; roughly 4 hours active use per charge (detachable hand scanner has its own separate coin-cell battery)
  sao_version: null
get_one:
  price: Approximately $125
  price_usd: 125.0
  quantity: '19'
  availability: sold_out
  distribution:
  - purchase
  where: Sold via presale on Uberflux under the product code MIH-HackersInSpaceBadge; all 19 units were sold.
  availability_note: 'Uberflux listing showed sold: 19, total: 19 (presale) as of 2026-09-07.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/MakeItHackin/TOSTricorder
  eda_tool: null
  fab_url: null
  notes: Firmware source and a 3D-printable scanner stand STL are published on GitHub (MakeItHackin/TOSTricorder); a browser-based Web Serial flasher is hosted at MakeItHackin/tricorder-flasher (https://makeithackin.github.io/tricorder-flasher/). No PCB/schematic hardware files were found published as of 2026-09-06.
links:
- kind: repo
  label: TOSTricorder firmware & docs (GitHub)
  url: https://github.com/MakeItHackin/TOSTricorder
- kind: repo
  label: tricorder-flasher (Web Serial flashing tool)
  url: https://github.com/MakeItHackin/tricorder-flasher
- label: uberflux.com/product/MIH-HackersInSpaceBadge
  url: https://uberflux.com/product/MIH-HackersInSpaceBadge
  kind: store
- kind: video
  label: Tricorder walkthrough (YouTube)
  url: https://youtu.be/mJSx17gsqMw
images:
- file: assets/images/badges/dc34/original-series-tricorder-badge/b7be2cead1.jpg
  source: https://uberflux.com/product/MIH-HackersInSpaceBadge
  credit: MakeItHackin
  caption: The Uberflux storefront listing titled "Hackers In Space Badge," whose product photo and description are actually those of MakeItHackin's Original Series Tricorder badge
contact:
  discord: MakeItHackin
  emails:
  - andrew@makeithackin.com
  handles:
  - '@makeithackin'
  raw:
  - on everything
notes:
- The community sheet listed this only as "New" for DC34; no maker storefront listing (Tindie/Etsy) was found for this specific badge, only resale listings on eBay.
- 'Uberflux. $120, status: sold out.'
- This listing's title/URL slug say "Hackers In Space Badge," but every other field on the page (og:description, description_html, specs table, cover image, docs links) is verbatim the Original Series Tricorder content -- apparently a mislabeled or cloned product page on Uberflux rather than a second, distinct item.
status: listed
sources:
- kind: sheet
  event: dc34
  row: 32
  updated: 7/5/2026 17:36:18
  listing: New
- kind: url
  url: https://github.com/MakeItHackin/TOSTricorder
  title: 'MakeItHackin/TOSTricorder: TOS Tricorder Badge'
  accessed: '2026-09-06'
  note: Primary source for hardware (XIAO ESP32-S3, sensors, displays, LEDs, scanner), features, menus, games, battery life, and firmware/flasher publication.
- kind: url
  url: https://github.com/MakeItHackin/tricorder-flasher
  title: MakeItHackin/tricorder-flasher
  accessed: '2026-09-06'
  note: Confirms the browser-based Web Serial flashing tool and that firmware binaries are published there.
- kind: url
  url: https://www.ebay.com/itm/206540280748
  title: Defcon 34 2026 MakeItHackin Star Trek TOS Tricorder DEF CON Hacker Badge | eBay
  accessed: '2026-09-06'
  note: Secondary-market resale listing confirming this exact badge was distributed at DEF CON 34, 2026; page returned an error on direct fetch so only search-result summaries and the listing title were usable, not full listing text or photos.
- kind: url
  url: https://www.tindie.com/products/makeithackin/tricorder-sao/
  title: Tricorder SAO from MakeItHackin on Tindie
  accessed: '2026-09-06'
  note: Checked to rule out duplication with the maker's separate "Tricorder SAO" product (a smaller SAO add-on, distinct from this full standalone badge; see archive entry dc33-tricorder-sao).
- kind: url
  url: https://uberflux.com/product/MIH-HackersInSpaceBadge
  title: Hackers In Space Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/MIH-HackersInSpaceBadge
  title: Hackers In Space Badge (raw page data)
  accessed: '2026-09-07'
  note: Fetched the raw HTML/hydration JSON directly. Confirmed the product record (code HackersInSpaceBadge, maker MakeItHackin) carries price_cents 12000, sold 19 of 19, presale true, and a description_html/spec table identical to the Original Series Tricorder badge, including the same GitHub and flasher links and cover image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Hardware/firmware details, features, and games are well documented on the maker's own GitHub repo (high confidence for those fields). However, get_one fields (exact quantity made, current availability, and precise distribution channel/price at the con) could not be confirmed from a maker storefront -- the sheet's "Approximately $125" price was kept as-is, and only resale listings on eBay (blocked from full fetch) were found for corroboration. No official product photos of the badge itself were located from a source reachable by this research pass, so no images were saved. Not a duplicate of MakeItHackin's separate dc33-tricorder-sao entry, which is a smaller SAO add-on rather than this standalone tricorder badge. Merged with duplicate entry 'Hackers In Space Badge' (dc34-hackers-in-space-badge).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc34/hackers-in-space-badge/
---

MakeItHackin's Original Series Tricorder badge is a functional prop replica of the tricorder from Star Trek: The Original Series, built to mark the franchise's 60th anniversary and released for DEF CON 34 (2026). It runs standalone on a Seeed XIAO ESP32-S3, with a 1.69" main IPS display and a separate 1.28" round display that idles with its own moiré animation on the second CPU core. Real sensors -- an accelerometer, a Hall-effect magnetic sensor, a temperature sensor, and battery monitoring -- back up ten on-device menus covering a "Con Mode" wearable display mode, sensor readouts, animations, a clock, five original games (Quadrant Invaders, Battle of Wolf 359, Shuttle Pod Lander, Cargo Bay Stacker, and Gagh), USB input-device emulation, NFC/RFID, WiFi, and Bluetooth settings.

A detachable hand-held medical scanner attaches magnetically to the back of the unit and carries its own coin-cell battery; removing it can trigger the badge's medical-scanning mode automatically. The badge also functions as a USB HID keyboard or mouse (wired or over Bluetooth) and carries an onboard NFC tag that shares the project's link when tapped by a phone. There is no speaker -- all alerts are visual, delivered through the three addressable RGB LEDs and the two screens.

The maker publishes the firmware source and a 3D-printable stand for the hand scanner on GitHub (MakeItHackin/TOSTricorder), along with a companion browser-based Web Serial flasher (MakeItHackin/tricorder-flasher) that lets owners update the firmware from Chrome or Edge with no drivers or IDE required. No PCB or schematic files were found published alongside the firmware, so the project is only partially open source. Beyond the community sheet's listing and a secondary-market eBay resale, no maker storefront page was found confirming price, quantity produced, or ongoing availability.

## Notes merged from the duplicate entry "Hackers In Space Badge"

The Uberflux marketplace listing "Hackers In Space Badge" (product code MIH-HackersInSpaceBadge) appears, from its own page data, to be a duplicate or mislabeled clone of MakeItHackin's Original Series Tricorder badge, already catalogued in this archive as `dc34-original-series-tricorder-badge`. The listing's title and URL slug reference "Hackers in Space," but its description, specifications table, cover photo, price ($120), sales count (19 of 19 sold via presale), and every linked resource -- the TOSTricorder firmware repository and the browser-based Web Serial flasher -- are identical to the Tricorder listing, a working Star Trek: The Original Series tricorder prop built for DEF CON 34 (2026) around a Seeed XIAO ESP32-S3.

No separate "Hackers in Space" product, event, or theme by MakeItHackin (also known online as GhostGlitch) turned up in a web search, so this entry is best read as the same physical badge sold or listed under a second name/URL on the storefront rather than a distinct item. The event and year have been corrected here to dc34 / 2026 to match what the listing actually documents.
