---
title: Vixy
id: dc31-vixy
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: DEFCON Furs
  url: https://donate.defconfurs.org
summary: A community electronic badge from the DEFCON Furs group for DEF CON 31, built around an RP2040 and 48 RGB LEDs with capacitive touch points and two SAO ports.
functions: Runs LED animations via MicroPython scripting; has touch/capacitive "booping" points; hosts two Shitty Add-Ons (SAO v1.69bis).
look:
  colors: []
  shape: null
  themes:
  - animal
  - furry
  - community
tech:
  mcu: RP2040
  leds:
    count: 48
    type: RGB
    note: driven via an IS31FL3737 LED controller
  display: none
  connectivity: []
  battery: null
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: $75 donation minimum (fully assembled w/ lanyard); a PCB-blank tier was also offered
  price_usd: 75
  quantity: Quantities limited (exact number not stated)
  availability: sold_out
  availability_note: Gumroad listing shows "Sold Out" as of 2026-09-07.
  distribution:
  - purchase
  - free_drop
  where: Sold via DEFCON Furs' Gumroad-hosted donation store (donate.defconfurs.org), as a fundraiser for the group and the charities they support; also required to get into the DEFCON Furs 2023 hospitality suite.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/defconfurs/dcfurs-badge-dc31-public
  firmware_url: https://github.com/defconfurs/dcfurs-badge-dc31-public
  eda_tool: null
  notes: Repo includes a schematic PDF, a BOM (Google Sheets link), firmware (.uf2 builds including MicroPython and an Arduino IS31FL3737 LED-driver library), and CTF challenge hints. No Gerbers or EDA source files were found in the linked repo.
links:
- label: donate.defconfurs.org
  url: https://donate.defconfurs.org
  kind: website
- label: Vixy badge listing (Gumroad)
  url: https://donate.defconfurs.org/l/pohyz
  kind: store
- label: dcfurs-badge-dc31-public (GitHub)
  url: https://github.com/defconfurs/dcfurs-badge-dc31-public
  kind: repo
images:
- file: assets/images/badges/dc31/vixy/cfd3bdd145.jpg
  source: "https://donate.defconfurs.org/l/pohyz"
  credit: "DEFCON Furs"
  caption: "Vixy badge, fully assembled, product photo"
contact: {}
notes:
- Please go to the link and see the different badge levels they have. These folks are awesome!! Show them love!!
- "Sheet's 'where' text was a generic pitch to the donation page; replaced with what the Gumroad listing actually says."
status: released
sources:
- kind: sheet
  event: dc31
  row: 37
  updated: '2023-07-13'
- kind: url
  url: https://donate.defconfurs.org
  title: DEFCON Furs (Gumroad storefront)
  accessed: '2026-09-07'
  note: Confirmed "DEFCON Furs 2023 Badge: Vixy - Fully Assembled" as a real product, $75, sold-out.
- kind: url
  url: https://donate.defconfurs.org/l/pohyz
  title: "DEFCON Furs 2023 Badge: Vixy - Fully Assembled (Gumroad listing)"
  accessed: '2026-09-07'
  note: Source of description, price, shipping details, tech specs (RP2040, 48 RGB LEDs, MicroPython, touch/booping, 2x SAO v1.69bis), and GitHub link.
- kind: url
  url: https://github.com/defconfurs/dcfurs-badge-dc31-public
  title: defconfurs/dcfurs-badge-dc31-public
  accessed: '2026-09-07'
  note: Confirmed publicly released schematic, BOM, and firmware (Arduino + MicroPython) for the badge; used for make_your_own fields.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (MCU, LED count/driver, SAO version, price, sold-out status, GitHub repo) come from the maker's own Gumroad listing and GitHub repo. No PCB color/shape photos beyond the one product image were found, so look.colors/shape are left empty. Exact production quantity was not stated anywhere found. A separate "PCB Blank" tier of the same badge also existed on the same storefront but was not made a separate entry per instructions.
last_modified_date: '2026-09-07'
---

Vixy is the DEFCON Furs group's electronic badge for DEF CON 31 (2023), sold as a fundraiser through their Gumroad-hosted donation store. The fully-assembled badge (with lanyard) went for a $75 minimum donation, with a separate PCB-blank tier for those who wanted to build it themselves; both were sold to support the group and the charities it backs, and owning one also got attendees into the DEFCON Furs hospitality suite that year (it does not substitute for an official DEF CON badge).

Technically, Vixy is built around an RP2040 microcontroller driving 48 RGB LEDs through an IS31FL3737 LED controller, scriptable in MicroPython. It has capacitive touch points, continuing the group's "booping" interaction from prior badges, and carries two SAO v1.69bis (Shitty Add-On) headers for accessories. DEFCON Furs publicly released the badge's schematic, bill of materials, and firmware (both Arduino-based LED tests and MicroPython builds) on GitHub.

As of this research pass the Gumroad listing shows the item sold out, and no exact production quantity was published.
