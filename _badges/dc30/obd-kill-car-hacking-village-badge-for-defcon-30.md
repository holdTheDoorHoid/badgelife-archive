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
  hardware_url: null
  firmware_url: https://github.com/intrepidcs/obd-kill
  eda_tool: null
  notes: 'The GitHub repo and GitBook guide contain example MicroPython programs (Pin/Signal/UART usage) and the CANHack MicroPython SDK writeup, confirmed by direct inspection. The maker''s feature list claims an "open source schematic" but no schematic, PCB/CAD files, Gerbers, or BOM could be found in the repo, its assets folder, or on the guide site - only two block-diagram illustrations and product photos. Only a compiled UF2 firmware image is downloadable (cdn.intrepidcs.net), not firmware source.'
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
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Verification pass (2026-09-07): confirmed maker, event, year, MCU, price, functions, battery, connectivity, and DIP switch/buzzer/button details directly against the maker''s GitHub-hosted guide source (introduction-and-overview.md, a-tour-of-obd-kill-hardware.md, hardware-and-software-setup.md) and the intrepidcs.com announcement post. Corrected two issues: (1) removed "uart" from tech.connectivity - the only UART reference found is a generic RP2040/MicroPython library tutorial snippet, not documentation of a UART interface on the badge itself; (2) blanked make_your_own.hardware_url and revised its notes - the repo and guide contain no schematic, PCB/CAD, Gerber, or BOM files despite the maker''s feature list claiming an "open source schematic" (only two block-diagram graphics and product photos exist). Noted but did not change: the maker''s own "Summary of Key Features" list states 12 LEDs (matches this entry), but a-tour-of-obd-kill-hardware.md says "13 LEDs" in its opening sentence - a genuine disagreement between two of the maker''s own pages; 12 is kept as it comes from the canonical feature-list page. Both images verified to match product photos hosted in the maker''s own GitHub repo (front = DIP-switch/button side, back = Pico-mounted side). Store listing (store.intrepidcs.com/product/chv-badge-30) re-confirmed dead. Still could not find: exact LED part number, SAO header presence (none shown in pinout diagrams, so likely absent), quantity produced, or any Gerbers/EDA-file link.'
last_modified_date: '2026-09-07'
---

The OBD-Kill badge is the official Car Hacking Village badge for DEF CON 30 (2022), made by Intrepid Control Systems, an automotive network tools company based in Troy, Michigan. Rather than a passive wearable, it's a functional CAN bus hacking tool built around a Raspberry Pi Pico: a single CAN channel lets the wearer generate arbitrary CAN messages (down to 8ns timing resolution, via a companion USB console app), while 12 programmable LEDs, a PWM buzzer, two programmable buttons, and a DIP switch round out the interactive side. It runs from either a Micro USB cable or an onboard CR2032 coin cell.

It was sold in person at the Car Hacking Village at DEF CON 30 in Las Vegas for $50 cash or $55 by credit card. Intrepid Control Systems published example MicroPython programs and a CANHack MicroPython SDK (C/C++ and MicroPython) through a GitHub repository and an accompanying documentation site, positioning the badge as a teaching platform for automotive network security rather than a one-off giveaway. The maker's own feature list also advertises an "open source schematic," but no schematic, PCB/CAD files, or BOM were actually found published anywhere. The original storefront listing has since gone dead, and no information on total production quantity was found.

## Make your own

Intrepid Control Systems' guide (linked above) and the `intrepidcs/obd-kill` GitHub repository provide example MicroPython programs for the Raspberry Pi Pico, along with a CANHack MicroPython SDK for driving the badge's CAN channel. The maker advertises an open-source schematic as a feature, but no schematic, Gerbers, or other CAD/BOM files could be located in the repository, its guide site, or elsewhere.
