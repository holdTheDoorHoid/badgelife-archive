---
title: Thereminion SAO (bare board)
id: dc26-thereminion-sao-bare-board
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: Harbinger LTD (Andrew Nicholson)
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
summary: An optical theremin built as a "Shitty Add-On", using a photoresistor and buzzer so the wearer can point it at other blinking badges and "play" them like a light-controlled instrument.
functions: 'Photoresistor-driven audio: pointing it at a light source (including other badges'' LEDs) changes pitch/tone through an onboard buzzer, based on a modification of Forrest Mims'' audible light meter circuit. Has an on-off toggle switch and an open 6-pin matrix area for circuit-bending mods (extra capacitors, switches, pots).'
look:
  colors: []
  shape: null
  themes:
  - music
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $5.00
  price_usd: 5.00
  quantity: '100'
  availability: sold_out
  distribution:
  - purchase
  where: Sold on Tindie (awkwardai/Harbinger LTD store, Atlanta, GA) as a bare, unassembled board; listing shows sold out and the seller "on a break."
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/awkwardai/thereminion-sao-bare-board
  url: https://www.tindie.com/products/awkwardai/thereminion-sao-bare-board/
  kind: store
- label: Hackaday.io - The Harbinger Shitty Add-On Badges
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges
  kind: hackaday
images:
- file: assets/images/badges/dc26/thereminion-sao-bare-board/9399a652f0.jpg
  source: "https://www.tindie.com/products/awkwardai/thereminion-sao-bare-board/"
  credit: "Harbinger LTD (awkwardai)"
  caption: "Thereminion SAO bare board, unassembled"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/awkwardai/thereminion-sao-bare-board/
  title: Thereminion SAO (bare board)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc26''.'
- kind: url
  url: https://hackaday.io/project/159952-the-harbinger-shitty-add-on-badges/details
  title: The Harbinger Shitty Add-on Badges | Hackaday.io
  accessed: '2026-09-07'
  note: Confirms the Thereminion's design basis (Forrest Mims audible light meter), parts (photoresistor, buzzer, toggle switch, 6-pin mod matrix), and that it was one of five SAOs Harbinger LTD made for DEF CON 26.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No MCU or LEDs are used; it is a purely analog light-to-sound circuit. Gerber/BOM files were mentioned by the maker in comments but no direct download link was found, so hardware_url/gerbers_url are left empty. Maker's real name (Andrew Nicholson) carried over from the sheet; not independently confirmed on Tindie or Hackaday, which credit "Awkward Intelligence"/awkwardai/Harbinger LTD.
last_modified_date: '2026-09-07'
---

The Thereminion is a "Shitty Add-On" that Harbinger LTD (the Atlanta-based maker behind the Tindie store awkwardai) built for DEF CON 26 in 2018. Rather than an MCU-driven badge, it's a small analog circuit adapted from Forrest Mims' classic audible light meter: a photoresistor feeds a buzzer, so pointing the SAO at a light source — including the blinking LEDs on other attendees' badges — changes the pitch and lets the wearer "play" nearby hardware like an instrument. It has a toggle switch to turn it on and off, and the maker left an open 6-pin matrix pad on the board for people who wanted to circuit-bend it further with their own capacitors, switches, or potentiometers.

It was one of five SAOs and badges Harbinger LTD made for that year's DEF CON, documented together on a single Hackaday.io project page. The bare (unassembled) board sold on Tindie for $5 in a limited run of 100 units; the listing is now sold out and the seller's store shows as inactive ("on a break").
