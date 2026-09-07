---
title: PRND SAO
id: dc32-prnd-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: Car Hacking Village
  url: https://www.carhackingvillage.com
summary: A $50 CAN-based SAO from the Car Hacking Village for DEF CON 32, die-cut like a top hat with a small LCD display that simulates a car's PARK/REVERSE/NEUTRAL/DRIVE shifter, wrapped around its own CTF challenge.
functions: |-
  LCD Display
  Simulated PARK, REVERSE, NEUTRAL, DRIVE
  CTF Challenges
look:
  colors:
  - green
  - white
  - blue
  - black
  shape: top hat
  themes:
  - security
  - ctf
tech:
  mcu: null
  leds: null
  display: LCD
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $50.00
  price_usd: 50.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold at the Car Hacking Village booth at DEF CON 32 (2024), alongside the CHV Main Badge, Speedometer SAO, and Key Fob SAO.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.carhackingvillage.com
  url: https://www.carhackingvillage.com
  kind: website
  archived: https://web.archive.org/web/20260810193641/https://www.carhackingvillage.com/
- label: car-hacking-village/CHV_SAO_Specification (GitHub)
  url: https://github.com/car-hacking-village/CHV_SAO_Specification
  kind: repo
images:
- file: assets/images/badges/dc32/prnd-sao/e82bc1f0fe.png
  source: http://web.archive.org/web/20240811090612/https://www.carhackingvillage.com/
  credit: Car Hacking Village
  caption: 2024 PRND SAO product photo from the Car Hacking Village site
contact: {}
notes:
- CHV's SAO headers are CAN-based rather than the usual I2C SAO bus (3.3V/GND plus CAN TX/RX), per the CHV SAO Specification repo, so "sao_version" above is left null rather than mapped to the standard v1/v1.69bis vocabulary.
status: listed
sources:
- kind: sheet
  event: dc32
  row: 37
  updated: ''
- kind: url
  url: http://web.archive.org/web/20240811090612/https://www.carhackingvillage.com/
  title: Car Hacking Village (Wayback Machine capture, 11 Aug 2024)
  accessed: '2026-09-07'
  note: Archived DC32 badge lineup page listing the "2024 PRND sao" at $50 with CTF Challenges, LCD Display, and Simulated PARK/REVERSE/NEUTRAL/DRIVE, alongside the $100 CHV Main Badge, the $50 Speedometer SAO, and the $50 Key Fob SAO. Source of the product photo.
- kind: url
  url: https://www.carhackingvillage.com/
  title: Car Hacking Village
  accessed: '2026-09-07'
  note: Current site no longer lists the DC32 badge/SAO lineup or a price; only a general note that the SAO standard was updated to include CAN TX/RX remains.
  archived: https://web.archive.org/web/20260810193641/https://www.carhackingvillage.com/
- kind: url
  url: https://github.com/car-hacking-village/CHV_SAO_Specification
  title: car-hacking-village/CHV_SAO_Specification
  accessed: '2026-09-07'
  note: Documents CHV's CAN-based SAO header (3.3V, GND, CAN TX, CAN RX in place of I2C), which the PRND SAO plugs into on the CHV Main Badge.
- kind: url
  url: https://github.com/car-hacking-village
  title: car-hacking-village GitHub organization
  accessed: '2026-09-07'
  note: Org repo list includes DC32_CHV_Badge_Firmware, DC32_CHV_Badge_Board, and DC32_CHV_Speedometer_Firmware, but no repository specific to the PRND SAO was found, so hardware/firmware links and open-source status are left blank.
  archived: https://web.archive.org/web/20260824134823/https://github.com/car-hacking-village
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Confirmed via an archived (Wayback Machine) copy of carhackingvillage.com from August 2024, which matches the sheet row exactly (title, $50 price, and all three listed functions) and supplied the product photo. The photo shows the SAO die-cut in the shape of a top hat, green and white on the front with a physical shifter-style switch and a small black display window, and a blue PCB back carrying the Car Hacking Village skull logo and a 6-pin (J1) connector; look.shape and look.colors come from viewing that photo directly. The live site no longer carries this page, and no dedicated GitHub repo for the PRND SAO specifically was found (the org's public repos cover the Main Badge and Speedometer SAO/CTF, but not this one), so mcu, LED count, open-source status, and quantity/current availability remain unconfirmed.
last_modified_date: '2026-09-07'
---

The PRND SAO was one of four add-ons the Car Hacking Village sold at its DEF CON 32 (2024) booth, built around CHV's own CAN-based SAO standard rather than the usual I2C SAO bus. Its board is die-cut into the shape of a top hat, printed green and white on the front around a physical shifter-style switch and a small LCD display window that simulates a car's PARK/REVERSE/NEUTRAL/DRIVE selector; the blue PCB back carries the Car Hacking Village skull logo and a 6-pin connector for its CTF challenge. It plugged into one of the four SAO headers on that year's $100 CHV Main Badge (an RP2040 board with four onboard CAN networks and a dry CAN connector for tapping real vehicle buses), sitting in a lineup alongside a Key Fob SAO and a Speedometer SAO, each also $50.

No dedicated hardware or firmware repository specific to the PRND SAO turned up in CHV's public GitHub organization, so its MCU, LED count, and open-source status are left blank rather than guessed. Its current availability is also unconfirmed: the con-year page that documented it has since been removed from the live carhackingvillage.com and the item does not appear in CHV's current online store.
</content>
