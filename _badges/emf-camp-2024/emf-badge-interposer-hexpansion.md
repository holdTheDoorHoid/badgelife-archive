---
title: EMF Badge Interposer Hexpansion
id: emf-camp-2024-emf-badge-interposer-hexpansion
layout: badge
parent: EMF Camp 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: emf-camp-2024
year: 2024
makers:
- name: Gavin's Creations (gjchester)
  url: https://www.tindie.com/stores/gjchester/
summary: A pass-through hexpansion kit for the 2024 Tildagon badge that breaks out the badge's hexpansion GPIO connections for probing and debugging.
functions: Sits between the Tildagon badge and another hexpansion, exposing the GPIO pins on the connector so the traffic passing between badge and hexpansion can be monitored/probed. An optional 0603 resistor and 0805 LED (not included) can be added as a power indicator.
look:
  colors:
  - green
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing shows "This product is no longer available for sale" as of 2026-09-08.'
  distribution:
  - purchase
  where: Sold (now retired) as a self-assembly kit on Tindie by seller gjchester (Gavin's Creations).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/gjchester/emf-badge-interposer-hexpansion
  url: https://www.tindie.com/products/gjchester/emf-badge-interposer-hexpansion/
  kind: store
images:
- file: assets/images/badges/emf-camp-2024/emf-badge-interposer-hexpansion/dff5e85382.jpg
  source: "https://www.tindie.com/products/gjchester/emf-badge-interposer-hexpansion/"
  credit: "Gavin's Creations (gjchester)"
  caption: "The EMF Badge Interposer Hexpansion kit"
contact: {}
notes:
- Pass-through hexpansion kit for the 2024 Tildagon that breaks out GPIO and lets you monitor traffic between the badge and another hexpansion; sold (now retired) on Tindie. Found by the event-year sweep, task emf-addons.
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/gjchester/emf-badge-interposer-hexpansion/
  title: EMF Badge Interposer Hexpansion
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''EMF Camp 2024''.'
- kind: url
  url: https://www.tindie.com/products/gjchester/emf-badge-interposer-hexpansion/
  title: EMF Badge Interposer Hexpansion by Gavin's Creations on Tindie
  accessed: '2026-09-08'
  note: 'Confirmed the item, maker, event/badge, kit contents, and sold-out status.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Tindie listing does not state original list price or quantity produced beyond noting the seller ordered a batch of PCBs above manufacturing minimums. No repo, Gerbers, or firmware link found; the listing credits the original interposer design to a community member known as "The Untitled Goose," who created it for the EMF Night Market, with gjchester selling an assembled kit derived from that design. Could not confirm an independent hardware/design-files URL for either party.'
last_modified_date: '2026-09-08'
---

The EMF Badge Interposer Hexpansion is a small pass-through accessory for the Tildagon badge given out at EMF Camp 2024. It plugs into one of the badge's hexpansion slots and lets another hexpansion plug in behind it, breaking out the GPIO lines on that connector so a user can probe or monitor the data passing between the badge and the downstream hexpansion. It ships as a self-assembly kit: a 1mm ENIG PCB plus pins and an edge connector, with pads for an optional 0603 resistor and 0805 LED (not included) if the buyer wants a power indicator.

It was sold by Gavin's Creations (Tindie seller gjchester), based in Harlow, UK, who has since retired the listing — the Tindie page now shows the product as no longer available. According to the listing, the underlying interposer design was originally created by a community member known as "The Untitled Goose" for the EMF Night Market and later shared with the community; gjchester produced and sold an assembled-kit version after ordering more PCBs than needed to meet a fab's minimum order quantity.

No design files, price, or exact production quantity could be confirmed from the sources found; a Tildagon badge is required separately to use it.
