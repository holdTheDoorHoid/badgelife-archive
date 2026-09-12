---
title: Hacker Warehouse Electronic Badge
id: dc25-hacker-warehouse-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: Hacker Warehouse
  url: https://hackerwarehouse.com/
summary: A WiFi-focused electronic badge built by security-tool retailer Hacker Warehouse for DEF CON 25, with an ESP8266EX, an OLED display, and 14 NeoPixel LEDs.
functions: 802.11 channel activity monitor, access point scanner, LED patterns, OLED animations, badge personalization, and other network utilities. Some offensive WiFi features (e.g. deauth) were left out of the shipped firmware after internal debate.
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - hardware tool
tech:
  mcu: ESP8266EX
  leds:
    count: 14
    type: NeoPixel
    note: Mini NeoPixel RGB LEDs
  display: 96x64 graphic full-color OLED
  connectivity:
  - wifi
  battery: 2x AA
  sao_version: none
get_one:
  price: $50
  price_usd: 50.0
  quantity: '425'
  availability: sold_out
  distribution:
  - purchase
  where: Presale through the Hacker Warehouse online store, picked up in person at DEF CON 25; not shipped before or after the con.
make_your_own:
  open_source: true
  hardware_url: https://github.com/hackerwarehouse/HW-DC25-Badge/tree/master/hardware
  firmware_url: https://github.com/hackerwarehouse/HW-DC25-Badge
  eda_tool: null
links:
- label: hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  kind: article
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
- label: hackerwarehouse/HW-DC25-Badge
  url: https://github.com/hackerwarehouse/HW-DC25-Badge
  kind: repo
- label: Hacker Warehouse Electronic Badge (store)
  url: https://hackerwarehouse.com/product/hacker-warehouse-electronic-badge/
  kind: store
  archived: https://web.archive.org/web/20260415031917/https://hackerwarehouse.com/product/hacker-warehouse-electronic-badge/
- label: 'Reddit: Hacker Warehouse DC25 Badge Source on Github'
  url: https://www.reddit.com/r/Defcon/comments/6soup4/hacker_warehouse_dc25_badge_source_on_github/
  kind: social
images: []
contact: {}
notes:
- ESP8266-based WiFi pentest badge (AP scanning/deauth) built as Hacker Warehouse's first hardware effort for DEF CON 25. Found by the event-year sweep, task dc25-saos.
- The sweep title read "Hacker Warehouse Badge"; the maker's own store lists it as "Hacker Warehouse Electronic Badge" and the GitHub repo/README call it "HW-DC25-Badge" / "Hacker Warehouse DC25 Badge" for DEF CON 25 -- all the same item.
- Firmware is GPL-3.0 licensed per the repo LICENSE file.
- 'Per the README: some offensive tools (deauth, etc.) were built but deliberately left out of the shipped firmware rather than unlocked in-con; wording about "locked" features led to confusion at the event. Users also reported WiFi stopping working after extended use, a bug the team was still chasing when the code was released.'
- Could not find any usable photo of the physical badge within the research budget -- the Hacker Warehouse store site is behind Cloudflare bot-blocking for direct fetches, and the only other page with an "og:image" found (eritrean-smart.org) is an unrelated AI-generated content-farm page (it even describes a different, ESP32/SAO-equipped badge) and was not used as a source.
status: released
sources:
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: Hacker Warehouse Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc25-saos); event read as ''dc25''.'
  archived: https://web.archive.org/web/20260907165055/https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
- kind: url
  url: https://github.com/hackerwarehouse/HW-DC25-Badge
  title: 'GitHub: hackerwarehouse/HW-DC25-Badge'
  accessed: '2026-09-08'
  note: Maker's own project page/README -- confirms MCU, LEDs, display, buttons, battery, functions, quantity (425), GPL-3.0 license, and that hardware + firmware are both published.
- kind: url
  url: https://hackerwarehouse.com/product/hacker-warehouse-electronic-badge/
  title: Hacker Warehouse Electronic Badge (product page)
  accessed: '2026-09-08'
  note: Maker's storefront -- confirms official title, price ($50), sold-out status, SKU, and that it was presale/in-person distribution only.
  archived: https://web.archive.org/web/20260415031917/https://hackerwarehouse.com/product/hacker-warehouse-electronic-badge/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (maker, chip, LEDs, display, price, quantity, open-source status) confirmed by the maker's own GitHub repo and storefront, which agree with each other and with the Hackaday roundup. No photo of the badge could be saved within budget; look.colors and look.shape are left empty rather than guessed. No SAO header is mentioned anywhere, so tech.sao_version is set to none.
last_modified_date: '2026-09-10'
model:
  file: assets/models/dc25/hacker-warehouse-badge.glb
  method: kicad
  source_file: HW-DC25-Badge-20170609-1.2.brd
  generated: '2026-09-10'
  bytes: 304748
---

Hacker Warehouse, a retailer of penetration-testing hardware, built the Hacker Warehouse Electronic Badge as its first foray into custom hardware, for DEF CON 25 in 2017 (with help from Jaycon Systems on manufacturing). The badge centers on an ESP8266EX driving a 96x64 full-color OLED display, 14 mini NeoPixel RGB LEDs, and four tactile buttons in a joypad layout, running off two AA batteries. Its headline function is WiFi-focused: an 802.11 channel activity monitor and access-point scanner, alongside LED animation patterns, OLED animations, and badge personalization. The team debated including more aggressive WiFi tools (like deauth) but chose to leave them out of the shipped firmware, a decision that caused some confusion among owners who expected "locked" features to unlock during the con.

425 units were produced and sold through a presale on the Hacker Warehouse store for $50, picked up in person at the conference; the badge was never shipped outside that window and the listing is now marked sold out. After the con, Hacker Warehouse released both hardware and firmware source on GitHub under a GPL-3.0 license, along with notes acknowledging a WiFi-stability bug in the field that they hadn't fully diagnosed before release, and a two-week software crunch that preceded the badge's mass flashing.

## Make your own

The [GitHub repo](https://github.com/hackerwarehouse/HW-DC25-Badge) contains both a `hardware` directory and the Arduino-based firmware source (`src`). To rebuild the firmware you need the Arduino IDE with the ESP8266 board package, plus the Adafruit_NeoPixel and WS2812FX libraries; flashing an existing badge is done over a 3.3V serial cable while holding the badge's up button during power-on.
