---
title: TEST-O the Test Robot Addon
id: supercon-2023-supercon-2023-test-o-the-test-robot-addon
layout: badge
parent: Supercon 2023
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2023
year: 2023
makers:
- name: trueControl
  url: https://basic.truecontrol.org
summary: TEST-O is a robot-shaped SAO from true / trueControl (Whiskey Pirates) that tests continuity, diodes and LEDs through alligator-clip arms while its RGB eyes run knob-selected light programs; it was released for Hackaday Supercon 7 (2023) and sold on trueControl's own webshop.
functions: 'Bottom switch selects continuity test, diode test, or fun (light-show) modes. Knobs on the body select RGB eye program and features. Top button toggles the continuity beep and RGB brightness. Rear switch chooses battery or SAO-header power. Dangly alligator-clip arms probe circuits or pinch its own cheeks; continuity-test contacts are in the cheeks and a test diode sits between the antennas.'
look:
  colors:
  - black
  shape: robot
  themes:
  - robot
  - hardware tool
  - measurement
tech:
  mcu: PY32F003
  leds:
    count: 2
    type: RGB
    note: Two RGB LED eyes running knob-selected light programs.
  display: none
  connectivity: []
  battery: CR2032 (optional; also runs from host SAO/GAT header power)
  sao_version: none
get_one:
  price: $35
  price_usd: 35
  quantity: ''
  availability: limited
  distribution:
  - purchase
  - contest
  where: Assembled units were available in person at Supercon 7 (2023) and later entered in the Supercon 8 SAO contest; also sold assembled through trueControl's own webshop (shop.truecontrol.org), which showed only 1 unit in stock as of 2026-09-07. Blank boards/BOM for self-assembly were also offered.
make_your_own:
  open_source: yes
  hardware_url: https://basic.truecontrol.org/sc7/testo-dev/
  firmware_url: https://basic.truecontrol.org/sc7/testo-dev/
  eda_tool: null
links:
- label: hackaday.io/project/198571-test-o-the-test-robot-addon
  url: https://hackaday.io/project/198571-test-o-the-test-robot-addon
  kind: hackaday
- label: basic.truecontrol.org
  url: https://basic.truecontrol.org
  kind: website
- label: shop.truecontrol.org
  url: https://shop.truecontrol.org
  kind: store
- label: 'shop.truecontrol.org: TEST-O Robot Buddy Addon Continuity Tester (product page)'
  url: https://shop.truecontrol.org/index.php?route=product/product&path=59&product_id=148
  kind: store
- label: 'basic.truecontrol.org: TEST-O code, schematics, etc'
  url: https://basic.truecontrol.org/sc7/testo-dev/
  kind: doc
images:
- file: assets/images/badges/supercon-2023/supercon-2023-test-o-the-test-robot-addon/6bd3f9fc97.jpg
  source: "https://hackaday.io/project/198571-test-o-the-test-robot-addon"
  credit: "true (trueControl)"
  caption: "TEST-O Robot Buddy addon with RGB eyes and alligator-clip probe arms"
- file: assets/images/badges/supercon-2023/supercon-2023-test-o-the-test-robot-addon/cd08fc0c58.jpg
  source: "https://shop.truecontrol.org/index.php?route=product/product&path=59&product_id=148"
  credit: "trueControl"
  caption: "TEST-O product photo showing knob, switches and probe leads"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198571-test-o-the-test-robot-addon
  title: TEST-O the Test Robot Addon
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/198571-test-o-the-test-robot-addon
  title: TEST-O the Test Robot Addon (Hackaday.io project page)
  accessed: '2026-09-07'
  note: Confirmed function (diode/continuity/LED tester, RGB eyes), event history (Supercon 7 release, Supercon 8 SAO contest entry), open-source code/schematics, and provided the hero image URL.
- kind: url
  url: https://basic.truecontrol.org
  title: trueControl BASIC (badge/addon documentation hub)
  accessed: '2026-09-07'
  note: Identified maker "true" as part of the Whiskey Pirates DEF CON crew and located the TEST-O documentation section under Supercon 7 (2023).
- kind: url
  url: https://shop.truecontrol.org/index.php?route=product/product&path=59&product_id=148
  title: 'trueControl Shop: TEST-O Robot Buddy Addon Continuity Tester'
  accessed: '2026-09-07'
  note: Source for price ($35), SKU, MCU (PY32F003), PlatformIO/end-user-programmable firmware, GAT/SAO or CR2032 power, package contents, credits (concept by rCON, circuit/layout/design/code by true, hand-assembled in Las Vegas), and two additional product photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'The maker''s own webshop and documentation hub confirm the core facts. Could not reach the dedicated sub-pages basic.truecontrol.org/sc7/testo-dev/ or /sc7/testo-qs/ directly (403/404 depending on client) to pull firmware repo specifics or exact quantity made, so hardware_url/firmware_url point to the listed doc page but its content was not independently verified; quantity made is unstated anywhere found. Shop listed only 1 unit in stock at time of check, so availability is recorded as "limited" rather than a firm sold_out/available call.'
last_modified_date: '2026-09-07'
---

TEST-O is a robot-shaped Simple Add-On (SAO) made by "true" of trueControl, part of the Whiskey Pirates DEF CON crew, for Hackaday Supercon 7 in 2023. It is a working test tool built into a badge addon: alligator-clip "arms" let the user check circuits for continuity and test diodes and LEDs (current-limited to keep them safe), while a pair of RGB "eyes" run knob-selected light shows. A bottom switch chooses between continuity test, diode test, and light-show-only modes; a top button toggles the continuity beep and brightness; and a rear switch picks between an onboard CR2032 battery or power from a host badge's GAT/SAO header, so it works stand-alone or plugged in.

Under the hood it runs on a PY32F003 microcontroller and is described by the maker as end-user programmable over a cheap TTL UART or DapLink probe, with a PlatformIO project, schematics, and datasheets published on trueControl's documentation site. The original concept and art came from rCON, with true handling the circuit, PCB layout, firmware, and hand-assembly (with some machine assistance) in Las Vegas; proceeds from badge sales fund Whiskey Pirates' other projects. It sold assembled for $35 through trueControl's own webshop (which does not accept PayPal, preferring crypto or Amazon gift purchases), with blank boards and a BOM offered for self-assembly. The badge was also entered in the Supercon 8 SAO contest the following year.

## Make your own

Hardware (schematic/BOM) and firmware are published by the maker at basic.truecontrol.org's TEST-O documentation page, described as a PlatformIO project intended to be end-user reprogrammable via TTL UART or a DapLink debug probe. The specific sub-pages (quick-start guide and "code, schematics, etc") returned access errors when checked directly, so their exact contents were not verified here; the top-level shop listing and Hackaday.io project page were used as the source of record instead.
