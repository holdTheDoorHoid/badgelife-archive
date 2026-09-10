---
title: hakinthebox.com minibadge
id: saintcon-2018-hakinthebox-com-minibadge
layout: badge
parent: SAINTCON 2018
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2018
year: 2018
makers:
- name: hakinthebox.com
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ATtiny
  leds: null
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: raw.githubusercontent.com/compukidmike/Saintcon2018/master/Minibadges/Readme.md
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2018/master/Minibadges/Readme.md
  kind: website
images: []
contact: {}
notes:
- Listed with a reserved I2C address (0x01) in the official SAINTCON 2018 badge repo's minibadge registration table, indicating a hakinthebox.com-branded minibadge was built for the 2018 badge. Found by the event-year sweep, task saintcon-2018.
status: listed
sources:
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2018/master/Minibadges/Readme.md
  title: hakinthebox.com minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2018); event read as ''saintcon-2018''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2018/master/Minibadges/Readme.md
  title: 'Registered Minibadges table, SAINTCON 2018 (compukidmike/Saintcon2018)'
  accessed: '2026-09-10'
  note: 'Full registration table confirms "hakinthebox.com" at I2C address 0x01, chip listed as ATTiny. No further description, image, or maker link is given in the repo.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: >-
    Only source found is the official SAINTCON 2018 badge repo's minibadge I2C
    address registry, which lists an entry named "hakinthebox.com" at address
    0x01 built on an ATtiny. This is a real, primary-source page (not just a
    search snippet), so the item is treated as a real minibadge rather than a
    rumor, but the registry gives no maker page, description, image, price,
    or quantity. The domain hakinthebox.com resolves in DNS (to an AWS-hosted
    IP) but does not respond to HTTP or HTTPS requests, so no live site could
    be checked. A web search turned up no maker site, storefront, Hackaday
    page, or forum post about this specific minibadge (only unrelated
    similarly-named sites like hackthebox.com and hackinthebox.com, which are
    not the same maker). Left summary, functions, look, LED/display/battery
    fields, pricing, availability, and images empty because no source
    supports them. All remaining non-empty fields and sentences are
    supported by the primary-source registry table.
last_modified_date: '2026-09-10'
---

A minibadge built by a maker or team going by "hakinthebox.com" for SAINTCON 2018, one of dozens of independently made minibadges attendees could collect and plug into that year's official conference badge. It is documented only as a line in the SAINTCON 2018 badge repository's I2C address registry, which reserved address `0x01` for it and lists its microcontroller as an ATtiny.

Beyond that registration entry, no maker page, storefront, photo, or writeup for this specific minibadge could be located; the `hakinthebox.com` domain resolves in DNS but does not respond to web requests, so no live site exists to check. It is included here as a confirmed line item from the official badge documentation rather than a rumor, but most descriptive details remain unknown.
