---
title: DC27 Taco Drone SAO (fully assembled)
id: dc27-taco-drone-sao-fully-assembled
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: Harbinger LTD (Andrew Nicholson)
  url: https://hackaday.io/project/166344-defcon-27-shitty-add-ons
summary: A DEF CON 27 SAO with a small low-power fan and a bumper, built as a tribute to the taco-delivery drone Andrew "securelyfitz" flew at Toorcamp 2018.
functions: Spins a small onboard fan/propeller when powered from a host badge's SAO header; purely decorative, no other electronics.
look:
  colors: []
  shape: null
  themes:
  - food
  - drone
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: "$20.00"
  price_usd: 20
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold assembled on Tindie (seller awkwardai / Harbinger LTD); as of the September 2026 check the seller listed itself as "on a break" and not accepting orders.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/awkwardai/dc27-taco-drone-sao-fully-assembled
  url: https://www.tindie.com/products/awkwardai/dc27-taco-drone-sao-fully-assembled/
  kind: store
- label: hackaday.io/project/166344-defcon-27-shitty-add-ons
  url: https://hackaday.io/project/166344-defcon-27-shitty-add-ons/details
  kind: hackaday
images:
- file: assets/images/badges/dc27/taco-drone-sao-fully-assembled/275c6c0e83.jpg
  source: "https://www.tindie.com/products/awkwardai/dc27-taco-drone-sao-fully-assembled/"
  credit: "Harbinger LTD"
  caption: "The DC27 Taco Drone SAO, fully assembled"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/awkwardai/dc27-taco-drone-sao-fully-assembled/
  title: DC27 Taco Drone SAO (fully assembled) - Tindie
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27''.'
- kind: url
  url: https://hackaday.io/project/166344-defcon-27-shitty-add-ons/details
  title: "DEFCON 27 Shitty Add-Ons - Hackaday.io"
  accessed: '2026-09-07'
  note: "Maker's own project writeup; describes the taco-drone fan design, its Toorcamp 2018 inspiration, and the 3.3V host-badge power requirement."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: "The Hackaday project page (Harbinger LTD's own writeup of the full DEF CON 27 Shitty Add-Ons set) confirms the design intent, the fan/motor safety tuning, and that it needs a stable 3.3V supply from the host badge, but does not state a production quantity. The Tindie listing gives the price and shows the seller is currently on a hiatus (not accepting orders), so current availability is unknown rather than confirmed sold out. No PCB/firmware files were found; this appears to be a purely mechanical/decorative SAO with no publicly shared design files."
last_modified_date: '2026-09-07'
---

The Taco Drone SAO was part of Harbinger LTD's (Andrew Nicholson's) "DEF CON 27 Shitty Add-Ons" line, a set of SAOs built for DEF CON 27 in 2019. Rather than lights or a game, this one is a small mechanical tribute: it carries a tiny low-power fan/propeller, tuned down so it spins without posing any risk, and a bumper guard around it for safety. The concept nods to a real-world stunt from Toorcamp 2018, where fellow hacker Andrew "securelyfitz" ran a taco-delivery drone service at the camp.

The SAO has no microcontroller or LEDs of its own — it draws power straight from the host badge's SAO header, and Harbinger's own project notes warn that the fan won't spin at all if the host badge's 3.3V supply is weak or the batteries are low. It was sold fully assembled on Tindie for $20, separate from the "TV3Y3" badge it plugs into. No hardware or firmware files have been published for it; as of this check the Tindie shop was on a break and not taking new orders, so it is unclear whether stock remains.

