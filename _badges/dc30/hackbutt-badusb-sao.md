---
title: Hackbutt badUSB SAO
id: dc30-hackbutt-badusb-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: rot13labs
  url: https://rot13labs.com/
summary: An ATtiny85-based badUSB SAO shaped like a "dickbutt" with flashing red eyes, sold by rot13labs for DEF CON 30.
functions: Plugs into a host badge's SAO header (or a USB port via its own connector) as a programmable badUSB. Its default payload targets macOS, opening a terminal and using it to load setup instructions in the user's browser. It is reprogrammable via the Arduino IDE, and its ATtiny85 chip is compatible with existing community ATtiny85 Ducky Script payloads without modification.
look:
  colors:
  - black
  shape: null
  themes:
  - meme
  - security
  - hardware tool
tech:
  mcu: ATtiny85
  leds:
    count: 2
    type: null
    note: Flashing red LED "eyes"
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shows the product retired and no longer available for sale, checked 2026-09-07.
  distribution:
  - purchase
  where: Sold by rot13labs on Tindie; stickers were included with orders when available.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: The maker publishes setup/reprogramming instructions (Arduino IDE) at rot13labs.com but does not appear to publish hardware design files (schematic/Gerbers) for this specific SAO.
links:
- label: www.tindie.com/products/rot13labs/hackbutt-badusb-sao
  url: https://www.tindie.com/products/rot13labs/hackbutt-badusb-sao/
  kind: store
- label: rot13labs.com/setup/hackbutt
  url: https://rot13labs.com/setup/hackbutt
  kind: doc
images:
- file: assets/images/badges/dc30/hackbutt-badusb-sao/56183c0049.png
  source: "https://www.tindie.com/products/rot13labs/hackbutt-badusb-sao/"
  credit: "rot13labs"
  caption: "Hackbutt badUSB SAO, ATtiny85-based badUSB with flashing red eyes"
- file: assets/images/badges/dc30/hackbutt-badusb-sao/2c6f16f0e6.png
  source: "https://www.tindie.com/products/rot13labs/hackbutt-badusb-sao/"
  credit: "rot13labs"
  caption: "Hackbutt badUSB SAO, alternate view"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/rot13labs/hackbutt-badusb-sao/
  title: Hackbutt badUSB SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc30''.'
- kind: url
  url: https://rot13labs.com/setup/hackbutt
  title: 'rot13labs - setup - Hackbutt'
  accessed: '2026-09-07'
  note: Confirms ATtiny85 chip, Arduino IDE reprogramming, and Ducky Script compatibility.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own Tindie listing and setup page confirm the core facts (chip, function, retirement). No price or quantity-made figure was found on the archived listing. No dedicated hardware/Gerber repo was located, so open_source is marked partial (setup/firmware guidance published, hardware files not found). LED count of 2 (the "eyes") is inferred from the product description ("flashing red eyes") rather than a stated spec, so it is left without further LED type detail.
last_modified_date: '2026-09-07'
---

The Hackbutt badUSB SAO is a novelty security tool made by rot13labs (also known as c0ldbru) for DEF CON 30 in 2022. Shaped like an angry "dickbutt" character with flashing red LED eyes, it is built around an ATtiny85 microcontroller and functions as a programmable badUSB: plugged into a host machine, its default payload targets macOS by opening a terminal and loading setup instructions in the browser.

Because it uses the widely-supported ATtiny85 chipset, the Hackbutt is compatible out of the box with the existing community of ATtiny85 Ducky Script payloads, and owners can load their own attacks using the Arduino IDE following rot13labs' published setup guide. It was sold through the maker's Tindie storefront, with stickers included when in stock; the listing is now retired and no longer available for purchase.

rot13labs went on to release related badges in later years, including the "Hackbutt v.3 wifi testing badge" for DEF CON 31 and a "Duckbutt wireless testing SAO," both separate items from this original DEF CON 30 badUSB SAO.
