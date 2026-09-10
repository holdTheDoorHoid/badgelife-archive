---
title: The Jolly Tagger SAO
id: supercon-2024-jolly-tagger-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Phil Weasel
  url: https://hackaday.io/hacker/1498391-phil-weasel
summary: An NFC-tag SAO built around an M24LR64E IC with a PCB-trace coil antenna, holding contact data writable by NFC app or I2C, with PWM-lit reverse-mount LED eyes on a gold ENIG black PCB that can be converted into a keychain pendant or pin after the con; entered in the Supercon 8 SAO Contest.
functions: Stores contact info on an onboard NFC tag, readable/writable by phone NFC apps or over I2C from a host badge; PWM-driven reverse-mount LEDs light up the eyes. After the con it can be desoldered from its SAO header and reused as a keychain pendant or pin.
look:
  colors:
  - black
  - gold
  shape: null
  themes:
  - nfc
  - jewelry
tech:
  mcu: none
  leds:
    count: 2
    type: reverse-mount
    note: PWM-dimmed, draw ~10mA each, run below 10% duty in the final design
  display: none
  connectivity:
  - nfc
  - i2c
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Entered in the Supercon 8 SAO Contest (2024); maker notes manufacturing was limited by budget and the cost of producing in Europe. No storefront found.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/197952-the-jolly-tagger-sao
  firmware_url: null
  gerbers_url: https://cdn.hackaday.io/files/1979528469178368/KiCad_Project.zip
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: KiCad project (Gerbers/schematic) published as a zip on the Hackaday.io project page; no firmware needed since the IC handles NFC autonomously.
links:
- label: hackaday.io/project/197952-the-jolly-tagger-sao
  url: https://hackaday.io/project/197952-the-jolly-tagger-sao
  kind: hackaday
  archived: https://web.archive.org/web/20260516204100/https://hackaday.io/project/197952-the-jolly-tagger-sao
- label: hackaday.io/project/197952-the-jolly-tagger-sao/logs
  url: https://hackaday.io/project/197952-the-jolly-tagger-sao/logs
  kind: hackaday
- label: cdn.hackaday.io/files/1979528469178368/KiCad_Project.zip
  url: https://cdn.hackaday.io/files/1979528469178368/KiCad_Project.zip
  kind: hackaday
images:
- file: assets/images/badges/supercon-2024/jolly-tagger-sao/64001c804c.jpg
  source: https://hackaday.io/project/197952-the-jolly-tagger-sao
  credit: Phil Weasel
  caption: The Jolly Tagger SAO, black ENIG PCB with reverse-mount LED eyes
  archived: https://web.archive.org/web/20260516204100/https://hackaday.io/project/197952-the-jolly-tagger-sao
- file: assets/images/badges/supercon-2024/jolly-tagger-sao/1b4f0d51dd.png
  source: https://hackaday.io/project/197952-the-jolly-tagger-sao/logs
  credit: Phil Weasel
  caption: Jolly Tagger SAO prototype during build/testing
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197952-the-jolly-tagger-sao
  title: The Jolly Tagger SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260516204100/https://hackaday.io/project/197952-the-jolly-tagger-sao
- kind: url
  url: https://hackaday.io/project/197952-the-jolly-tagger-sao
  title: The Jolly Tagger SAO
  accessed: '2026-09-07'
  note: Maker, chip (M24LR64E-RDW6T/2), LED, PCB finish, BOM, and design-file details.
  archived: https://web.archive.org/web/20260516204100/https://hackaday.io/project/197952-the-jolly-tagger-sao
- kind: url
  url: https://hackaday.io/project/197952-the-jolly-tagger-sao/logs
  title: The Jolly Tagger SAO - build logs
  accessed: '2026-09-07'
  note: 'Build log details: antenna design, LED current/PWM behavior, ENIG finish, and note that manufacturing was budget-limited.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts confirmed on the maker''s own Hackaday.io project page and build logs. One minor discrepancy: the project summary names the IC "M24LR64E" while a build log calls it "M24LR04E" — kept the summary''s M24LR64E as primary since it is the project''s stated part number. No storefront, price, or quantity-made figures found; maker states manufacturing was limited by budget/European production cost, so likely a small contest-run quantity rather than a general sale. No SAO header pin-count stated on the page, so sao_version left null. PCB shape not explicitly described as a specific silhouette beyond the "eyes" motif, so look.shape left null.'
last_modified_date: '2026-09-07'
---

The Jolly Tagger SAO is an NFC-based add-on built by Phil Weasel for the Supercon 8 SAO Contest in 2024. At its core is an ST M24LR64E NFC tag IC paired with an antenna etched directly into the PCB as a spiral coil trace tuned to 13.56MHz, so the board needs no separate antenna component. The design stores contact information that can be read or written either wirelessly via a phone's NFC app or over I2C from a host badge, and a pair of reverse-mount LEDs in the board's "eyes" light up under PWM control, dimmed below 10% duty cycle to keep current draw around 10mA per LED.

The board itself is a two-layer PCB finished in black solder mask with ENIG (gold-plated) contacts, chosen partly for its look and partly because the maker discovered mid-project that the silkscreen showed up better on the finish. Beyond the NFC IC and LEDs, the circuit is minimal: two SOT-23 NPN transistors, five 0-ohm bridges, and two 68-ohm resistors. The maker's build logs (NFC antenna design, design changes, arrival of the ENIG boards, first power-up, and LED testing) describe a straightforward path from prototype to a working badge that, after the conference, can be desoldered from its SAO header and worn as a keychain pendant or pin.

The maker notes that producing the boards was constrained by budget and the added cost of manufacturing in Europe, so this reads as a small contest-run batch rather than a boards-for-sale product; no storefront or listed price was found. The full KiCad project (schematic and PCB layout) is published as a downloadable zip on the Hackaday.io project page, making the design straightforward to reproduce for anyone wanting to build their own.
