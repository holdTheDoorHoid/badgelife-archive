---
title: Furbymin Defcon 27 SOA
id: dc27-dc27-furbymin-theremin-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: Harbinger LTD (Andrew Nicholson)
  url: https://www.tindie.com/stores/awkwardai/
summary: An Area 51-themed DEF CON 27 SAO shaped like a lobotomized Furby that works as a dual photoresistive theremin with capacitive touch pads to modify the sound, switched on by touching the beak, using 2 of 6 available oscillators with a spring-jack spot on one ear for a signal out to a modular synth and a raid meme on the back.
functions: 'Dual photoresistive theremin (2 of 6 available oscillators used, leaving room to hack/modify); capacitive touch pads modify the sound; touch the beak to power on/off; unused ear position for a spring jack signal-out to a modular synth.'
look:
  colors: [red, purple]
  shape: null
  themes: [animal, meme, music]
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: "$30"
  price_usd: 30
  quantity: ''
  availability: sold_out
  distribution: [purchase]
  where: Sold assembled through Harbinger LTD's Tindie store (awkwardai); listing now shows the seller "taking a break" and unavailable.
make_your_own:
  open_source: partial
  hardware_url: https://www.pcbway.com/project/shareproject/Furbymin_Defcon_27_SOA.html
  firmware_url: null
  eda_tool: null
links:
- label: www.pcbway.com/project/shareproject/Furbymin_Defcon_27_SOA.html
  url: https://www.pcbway.com/project/shareproject/Furbymin_Defcon_27_SOA.html
  kind: fab
- label: www.tindie.com/products/awkwardai/red-furbymin-theremin-soa-dc27-full-assembled
  url: https://www.tindie.com/products/awkwardai/red-furbymin-theremin-soa-dc27-full-assembled/
  kind: store
- label: www.tindie.com/stores/awkwardai
  url: https://www.tindie.com/stores/awkwardai/
  kind: store
images:
  - file: assets/images/badges/dc27/dc27-furbymin-theremin-sao/6b05bcbb14.jpg
    source: "https://www.tindie.com/products/awkwardai/red-furbymin-theremin-soa-dc27-full-assembled/"
    credit: "Harbinger LTD (Andrew Nicholson)"
    caption: "The Furbymin theremin SAO, assembled, showing the modified Furby face and Area 51 theming"
  - file: assets/images/badges/dc27/dc27-furbymin-theremin-sao/ff15ac0dd9.png
    source: "https://www.pcbway.com/project/shareproject/Furbymin_Defcon_27_SOA.html"
    credit: "Andrew Nicholson (PCBWay shared project)"
    caption: "PCB render of the Furbymin theremin SAO board"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://www.pcbway.com/project/shareproject/Furbymin_Defcon_27_SOA.html
  title: Furbymin Defcon 27 SOA - Share Project - PCBWay
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://www.pcbway.com/project/shareproject/Furbymin_Defcon_27_SOA.html
  title: Furbymin Defcon 27 SOA - Share Project - PCBWay
  accessed: '2026-09-07'
  note: "Confirmed maker (Andrew Nicholson), published Nov 24 2019, board specs (2-layer, 65x64mm FR-4, purple soldermask, immersion gold), CC BY-SA gerbers, and 1.69 SAO connector."
- kind: url
  url: https://www.tindie.com/products/awkwardai/red-furbymin-theremin-soa-dc27-full-assembled/
  title: Red Furbymin Theremin SOA DC27 (full assembled) - Harbinger LTD - Tindie
  accessed: '2026-09-07'
  note: "Confirmed price ($30), assembled-only sale, listing now unavailable (seller taking a break), and pulled the product photo."
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges/details
  title: The Harbinger Shitty Add-on Badges - Hackaday.io
  accessed: '2026-09-07'
  note: "Background on the maker's SAO line; describes a related DC26 'Thereminion' badge (same photoresistive-theremin concept) but does not mention Furbymin by name, so the Furby rehousing appears specific to the DC27 version."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Maker's own PCBWay and Tindie listings confirm the core facts. MCU/chip is not named on either page (the design is described only by oscillator count, suggesting a discrete/analog oscillator circuit rather than a named microcontroller), so tech.mcu is left null. No LEDs mentioned anywhere. Quantity made is not stated. The maker (Harbinger LTD / Andrew Nicholson / @awkwardai) sells a related line of DEF CON SAOs (Thereminion bare board, TV3Y3 Indie Badge, DC27 Flavin Detector, DC26/27 Air SAO, DC27 Taco Drone, DC27 Dumpster Fire) that are not yet in the archive - see other_items_found."
last_modified_date: '2026-09-07'
---

The Furbymin is a DEF CON 27 (2019) SAO by Harbinger LTD (Andrew Nicholson, @awkwardai on Tindie), built around an Area 51 theme that was running hot that summer ahead of the "Storm Area 51" internet meme. It rehouses a photoresistive theremin circuit inside a modified Furby shell, with a raid-themed graphic on the back. Touching the beak turns it on, and a pair of capacitive touch pads let the wearer shape the tone while playing. The board only uses 2 of its 6 available oscillators, leaving headroom for hacking, and one ear has an unused spot for a spring jack that can send the theremin's signal out to a modular synth.

It shipped fully assembled through the Harbinger LTD Tindie store for $30, with the PCB design (2-layer, 65x64mm FR-4, purple soldermask with immersion gold finish) shared publicly on PCBWay under a CC BY-SA license, including Gerbers. It uses the 1.69 (6-pin) SAO connector. The Tindie listing is no longer available; the seller's store currently shows as on a break.

## Make your own

Gerber files ("W203948ASN76_Finalfurbytofab2000.zip") are available from the PCBWay shared-project page under a CC BY-SA license, sufficient to fabricate the bare board. No firmware or schematic source files were found — the circuit appears to be discrete/analog rather than microcontroller-driven, consistent with the "oscillators" framing on both listings.
