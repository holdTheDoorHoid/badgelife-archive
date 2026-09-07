---
title: Hackers In Space Badge
id: dc34-hackers-in-space-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: MakeItHackin (GhostGlitch)
  url: https://github.com/MakeItHackin
summary: "A storefront listing titled \"Hackers In Space Badge\" on Uberflux whose actual product data, description, specs and photo are all for MakeItHackin's Original Series Tricorder badge -- the same Star Trek TOS tricorder prop already catalogued as the dc34-original-series-tricorder-badge entry."
functions: "As described on the listing (copied from the Tricorder product): ten on-device menus, five games (Quadrant Invaders, Battle of Wolf 359, Shuttle Pod Lander, Cargo Bay Stacker, Gagh), USB keyboard/mouse emulation, NFC/RFID read-write, WiFi, Bluetooth BLE, and a detachable magnetic hand scanner."
look:
  colors: []
  shape: handheld device
  themes:
  - sci-fi
  - tv
  - space
tech:
  mcu: XIAO ESP32-S3
  leds:
    count: 3
    type: RGB
    note: three addressable RGB LEDs, per the listing's copied specifications
  display: 1.69" 280x240 IPS main display + 1.28" round secondary display, separate buses
  connectivity:
  - wifi
  - ble
  - bluetooth
  - nfc
  - usb
  inputs:
  - buttons
  - accelerometer
  battery: USB-C with charging; about 4 hours with both displays lit
  sao_version: null
get_one:
  price: $120
  price_usd: 120.0
  quantity: '19'
  availability: sold_out
  availability_note: 'Uberflux listing showed sold: 19, total: 19 (presale) as of 2026-09-07.'
  distribution:
  - purchase
  where: Sold via presale on Uberflux under the product code MIH-HackersInSpaceBadge; all 19 units were sold.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/MakeItHackin/TOSTricorder
  eda_tool: null
  fab_url: null
  notes: 'Same firmware/flasher links as the Tricorder listing: MakeItHackin/TOSTricorder (firmware) and the browser-based flasher at https://makeithackin.github.io/tricorder-flasher/. No separate hardware files for a distinct "Hackers In Space" product were found.'
links:
- label: uberflux.com/product/MIH-HackersInSpaceBadge
  url: https://uberflux.com/product/MIH-HackersInSpaceBadge
  kind: store
- kind: repo
  label: TOSTricorder firmware & docs (GitHub)
  url: https://github.com/MakeItHackin/TOSTricorder
- kind: video
  label: Tricorder walkthrough (YouTube)
  url: https://youtu.be/mJSx17gsqMw
images:
- file: assets/images/badges/dc34/hackers-in-space-badge/b7be2cead1.jpg
  source: "https://uberflux.com/product/MIH-HackersInSpaceBadge"
  credit: "MakeItHackin"
  caption: "The Uberflux storefront listing titled \"Hackers In Space Badge,\" whose product photo and description are actually those of MakeItHackin's Original Series Tricorder badge"
contact: {}
notes:
- 'Uberflux. $120, status: sold out.'
- 'This listing''s title/URL slug say "Hackers In Space Badge," but every other field on the page (og:description, description_html, specs table, cover image, docs links) is verbatim the Original Series Tricorder content -- apparently a mislabeled or cloned product page on Uberflux rather than a second, distinct item.'
status: listed
sources:
- kind: url
  url: https://uberflux.com/product/MIH-HackersInSpaceBadge
  title: Hackers In Space Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/MIH-HackersInSpaceBadge
  title: Hackers In Space Badge (raw page data)
  accessed: '2026-09-07'
  note: 'Fetched the raw HTML/hydration JSON directly. Confirmed the product record (code HackersInSpaceBadge, maker MakeItHackin) carries price_cents 12000, sold 19 of 19, presale true, and a description_html/spec table identical to the Original Series Tricorder badge, including the same GitHub and flasher links and cover image.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This listing is a duplicate of the archive''s dc34-original-series-tricorder-badge entry (same maker, same specs/description/images/links, same firmware repo). The Uberflux page''s title says "Hackers In Space Badge" but its content is the Tricorder''s -- kept as its own entry per instructions (one entry per task, do not merge), with event/year corrected to match the real product (DC34, 2026) and duplicate_of reported. No evidence a genuinely separate "Hackers in Space"-themed badge by this maker exists; none was found in web search either.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/hackers-in-space-badge/
---

The Uberflux marketplace listing "Hackers In Space Badge" (product code MIH-HackersInSpaceBadge) appears, from its own page data, to be a duplicate or mislabeled clone of MakeItHackin's Original Series Tricorder badge, already catalogued in this archive as `dc34-original-series-tricorder-badge`. The listing's title and URL slug reference "Hackers in Space," but its description, specifications table, cover photo, price ($120), sales count (19 of 19 sold via presale), and every linked resource -- the TOSTricorder firmware repository and the browser-based Web Serial flasher -- are identical to the Tricorder listing, a working Star Trek: The Original Series tricorder prop built for DEF CON 34 (2026) around a Seeed XIAO ESP32-S3.

No separate "Hackers in Space" product, event, or theme by MakeItHackin (also known online as GhostGlitch) turned up in a web search, so this entry is best read as the same physical badge sold or listed under a second name/URL on the storefront rather than a distinct item. The event and year have been corrected here to dc34 / 2026 to match what the listing actually documents.
