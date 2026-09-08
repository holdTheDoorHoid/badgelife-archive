---
title: Heart Tap Sensor SAO
id: dc30-heart-tap-sensor-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Nerfhammer
summary: An SAO by Nerfhammer that uses a tap sensor to trigger an LED animation mimicking a heartbeat, sold from their Tindie store around DEF CON 30.
functions: Tapping or sharply moving the board triggers an LED to pulse in a heartbeat-like pattern.
look:
  colors: []
  shape: null
  themes:
  - heart
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Nerfhammer's Tindie store, alongside their other DEF CON 30 SAOs.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  kind: store
images: []
contact: {}
notes:
- Nerfhammer SAO using a tap sensor to trigger an LED animation mimicking a heartbeat, featured at DEF CON 30. Found by the event-year sweep, task dc30-saos.
status: listed
sources:
- kind: url
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  title: Heart Tap Sensor SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc30-saos); event read as ''dc30''.'
- kind: url
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  title: 'Badge me if you can: DEF CON 30 - Tindie Blog'
  accessed: '2026-09-08'
  note: 'Only source found that mentions the item: one sentence describing a Nerfhammer SAO with "a tap sensor to control an LED to mimic the beating of a heart," available on their Tindie store. No dedicated product page, chip/LED specs, price, or image could be found; Nerfhammer''s Tindie store page (tindie.com/stores/nerfhammer) is blocked by Cloudflare bot-checks and could not be fetched or searched.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-08'
  notes: 'Likely a duplicate of dc30-heart-beat-sao, which the sweep created separately for the same Nerfhammer/DC30/tap-sensor-heartbeat SAO from the same Tindie blog sentence. Could not confirm the maker''s actual product name, MCU, LED count/type, price, quantity, or current availability - Nerfhammer''s Tindie storefront returned a Cloudflare challenge page on every fetch attempt, and no dedicated product listing or press coverage beyond the single roundup sentence turned up in search. Left tech.*, get_one.price/quantity, and look.colors/shape empty rather than guess.'
last_modified_date: '2026-09-08'
---

Nerfhammer, a regular DEF CON 30 badgelife maker, produced an add-on (SAO) that uses a tap sensor: tapping or sharply jostling the board triggers an LED to flash in a pattern mimicking a heartbeat. It was one of several Nerfhammer pieces (alongside a Skully SAO and other DC30 add-ons) sold through their Tindie store around the August 2022 DEF CON 30 timeframe, per Tindie's own "badge me if you can" roundup post covering that year's badgelife scene.

Beyond that one-sentence description, no dedicated product page, image, or maker interview specific to this item could be located. Nerfhammer's Tindie storefront blocks automated fetches with a Cloudflare challenge, and searches turned up no press coverage, Hackaday post, or repo for it. This entry is very likely describing the same object as the separately-swept `dc30-heart-beat-sao` entry - both cite the same maker, event, and tap-to-heartbeat behavior from the same source sentence - so no chip, LED, or pricing details have been guessed here.
