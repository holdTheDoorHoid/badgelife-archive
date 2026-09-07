---
title: nyanSAO
id: other-nyansao
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: Nyan Devices
  url: https://nyandevices.com
summary: An ESP32-powered SAO with multiple RGB LEDs, in development by Nyan Devices for DEF CON.
functions: ''
look:
  colors: []
  shape: null
  themes:
  - cat
tech:
  mcu: ESP32
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/jbohack/nyanSAO
  url: https://github.com/jbohack/nyanSAO
  kind: repo
- label: nyandevices.com
  url: https://nyandevices.com
  kind: website
images: []
contact: {}
notes:
- ESP32 powered SAO
status: announced
sources:
- kind: url
  url: https://github.com/jbohack/nyanSAO
  title: nyanSAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/jbohack/nyanSAO
  title: 'GitHub - jbohack/nyanSAO'
  accessed: '2026-09-07'
  note: 'README confirms it is an ESP32-powered DEF CON SAO (v1.69bis standard) by Nyan Devices, status "In Development", with details to be announced via Discord.'
- kind: url
  url: https://nyandevices.com
  title: Nyan Devices
  accessed: '2026-09-07'
  note: 'Maker''s storefront; sells nyanBOX ($220) but does not yet mention nyanSAO, confirming it is unreleased.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The repo README confirms nyanSAO is an ESP32-powered SAO (v1.69bis) made for DEF CON, but is explicitly "In Development" with no specs, price, quantity, or release date announced yet (maker says details will post to their Discord). No specific DEF CON year is stated anywhere, so event is left as "other" rather than guessed. No photos of the physical item exist yet; the only image on the GitHub page is a generic auto-generated OpenGraph card, not a photo of the SAO, so no images were saved. LED count/type and battery/power details are not published.'
last_modified_date: '2026-09-07'
---

nyanSAO is an ESP32-powered Shitty Add-On (SAO) being developed by Nyan Devices, the same maker behind the nyanBOX wireless-security toolkit. It follows the SAO v1.69bis (6-pin) standard and is built around multiple RGB LEDs, giving it programmable lighting driven by the onboard ESP32.

As of this research pass the board is explicitly labeled "In Development" on its GitHub repository, with no public specs, pricing, production quantity, or release date. The maker says further details — features, specs, and availability — will be announced through their Discord server as the project progresses. No specific DEF CON year is named, so it isn't yet clear which con it is targeted at.
