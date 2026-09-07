---
title: OBD-Kill - Car Hacking Village Badge for DEFCON 30
id: dc30-obd-kill-car-hacking-village-badge-for-defcon-30
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Intrepid Control Systems
  url: https://intrepidcs.com/
summary: 'The official DEF CON 30 Car Hacking Village badge, built around a Raspberry Pi Pico with a CAN transceiver so wearers can generate arbitrary CAN bus traffic.'
functions: 'Generates arbitrary CAN messages/waves over its onboard CAN channel (with 8ns timing resolution via a companion USB console app), drives 12 programmable LEDs, makes noise through a built-in PWM buzzer, and is fully hackable via the Raspberry Pi Pico (C/C++, MicroPython, or the CANHack MicroPython SDK). Has 2 programmable buttons and a DIP switch.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - radio
tech:
  mcu: Raspberry Pi Pico
  leds:
    count: 12
    type: null
    note: 'Programmable LEDs; exact type not stated by the maker.'
  display: none
  connectivity:
  - usb
  - uart
  battery: 'CR2032 (optional; badge also runs from Micro USB)'
  sao_version: null
get_one:
  price: '$50 cash / $55 credit card'
  price_usd: 50
  quantity: ''
  availability: sold_out
  availability_note: 'Store listing (store.intrepidcs.com/product/chv-badge-30) returns "Product Not Found" as of 2026-09-07; sold at DEF CON 30 Car Hacking Village in person.'
  distribution:
  - purchase
  - village
  where: 'Sold in person at the Car Hacking Village at DEF CON 30 (Las Vegas, 2022).'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/intrepidcs/obd-kill
  firmware_url: https://github.com/intrepidcs/obd-kill
  eda_tool: null
  notes: 'Maker publishes an open-source schematic and example MicroPython/C programs via GitHub and a GitBook-style guide; no Gerbers or full CAD files were found.'
links:
- label: store.intrepidcs.com/product/chv-badge-30
  url: https://store.intrepidcs.com/product/chv-badge-30
  kind: store
- label: 'Intrepid Control Systems - Defcon 30 Car Hacking Village Official Badge'
  url: https://intrepidcs.com/defcon-30-car-hacking-village-official-badge/
  kind: article
- label: 'OBD-Kill guide: Introduction and Overview'
  url: https://guide.intrepidcs.com/docs/obd-kill/introduction-and-overview/
  kind: doc
- label: 'GitHub: intrepidcs/obd-kill'
  url: https://github.com/intrepidcs/obd-kill
  kind: repo
images:
- file: assets/images/badges/dc30/obd-kill-car-hacking-village-badge-for-defcon-30/ac1abddcf2.png
  source: "https://guide.intrepidcs.com/docs/obd-kill/introduction-and-overview/"
  credit: "Intrepid Control Systems"
  caption: "OBD-Kill badge, front view"
- file: assets/images/badges/dc30/obd-kill-car-hacking-village-badge-for-defcon-30/f7c13e7c88.png
  source: "https://guide.intrepidcs.com/docs/obd-kill/introduction-and-overview/"
  credit: "Intrepid Control Systems"
  caption: "OBD-Kill badge, back view"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://store.intrepidcs.com/product/chv-badge-30
  title: OBD-Kill - Car Hacking Village Badge for DEFCON 30
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc30''. Listing now returns "Product Not Found."'
- kind: url
  url: https://intrepidcs.com/defcon-30-car-hacking-village-official-badge/
  title: Defcon 30 Car Hacking Village Official Badge
  accessed: '2026-09-07'
  note: 'Maker announcement post; gave price ($50 cash / $55 card) and confirmed in-person sale at DEF CON 30 Car Hacking Village.'
- kind: url
  url: https://guide.intrepidcs.com/docs/obd-kill/introduction-and-overview/
  title: 'Introduction and Overview | OBD-Kill'
  accessed: '2026-09-07'
  note: 'Maker documentation: confirms Raspberry Pi Pico MCU, 12 LEDs, 1 CAN channel, PWM buzzer, 2 buttons, DIP switch, CR2032/USB power, and open-source schematic/example programs. Source of both saved images.'
- kind: url
  url: https://github.com/intrepidcs/obd-kill
  title: 'GitHub - intrepidcs/obd-kill: Defcon 30 Offical Badge documentation'
  accessed: '2026-09-07'
  note: 'Repository hosting the badge documentation/guide source and example code; confirms CANHack MicroPython SDK.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event, year, MCU, LED count, price, functions) confirmed on the maker''s own guide and announcement pages. Could not find: exact LED part number, SAO header presence (none mentioned in maker docs, so likely absent), quantity produced, or a Gerbers/EDA-file link (only a schematic and example code are published). The original store listing is dead as of this check.'
last_modified_date: '2026-09-07'
---

The OBD-Kill badge is the official Car Hacking Village badge for DEF CON 30 (2022), made by Intrepid Control Systems, an automotive network tools company based in Troy, Michigan. Rather than a passive wearable, it's a functional CAN bus hacking tool built around a Raspberry Pi Pico: a single CAN channel lets the wearer generate arbitrary CAN messages (down to 8ns timing resolution, via a companion USB console app), while 12 programmable LEDs, a PWM buzzer, two programmable buttons, and a DIP switch round out the interactive side. It runs from either a Micro USB cable or an onboard CR2032 coin cell.

It was sold in person at the Car Hacking Village at DEF CON 30 in Las Vegas for $50 cash or $55 by credit card. Intrepid Control Systems published an open-source schematic and example programs (C/C++ and MicroPython, including a CANHack MicroPython SDK) through a GitHub repository and an accompanying documentation site, positioning the badge as a teaching platform for automotive network security rather than a one-off giveaway. The original storefront listing has since gone dead, and no information on total production quantity was found.

## Make your own

Intrepid Control Systems' guide (linked above) and the `intrepidcs/obd-kill` GitHub repository provide an open-source schematic and example firmware for the Raspberry Pi Pico, along with a CANHack MicroPython SDK for driving the badge's CAN channel. No Gerbers or full CAD/BOM files were found published alongside the schematic.
