---
title: USB-C Power Back for SAOs
id: dc34-usb-c-power-back-for-saos
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc34
year: 2026
makers:
- name: caelyb (trueControl)
summary: 'A USB-C powered breakout board that steps 5V down to 3.3V so SAOs can run off a wall adapter or battery pack instead of a host badge.'
functions: 'Powers one or more SAOs independently of a badge, letting them run continuously (e.g. for desk/shelf display) from any USB-C power source; maker notes it can drive three "#NoICE" SAOs at once, more than a CR2032 coin cell can sustain.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: "$7 (2+ units $6 each)"
  price_usd: 7
  quantity: '75'
  availability: sold_out
  distribution:
  - purchase
  where: 'Sold by Uberflux at DEF CON 34 (2026): the Badgelife Village (Fri 11:30am and Sat 2:00pm), LineCon (all day), and the Queercon Mixer (Fri and Sat 4:00pm). Shipped after the con to continental US buyers for $5.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/DC34-powerback
  url: https://uberflux.com/product/DC34-powerback
  kind: store
images:
  - file: assets/images/badges/dc34/usb-c-power-back-for-saos/b52e35816c.jpg
    source: "https://uberflux.com/product/DC34-powerback"
    credit: "caelyb / trueControl"
    caption: "USB-C Power Back for SAOs product photo"
  - file: assets/images/badges/dc34/usb-c-power-back-for-saos/ea8c36a349.jpg
    source: "https://uberflux.com/product/DC34-powerback"
    credit: "caelyb / trueControl"
    caption: "USB-C Power Back for SAOs, alternate view"
contact: {}
notes:
- 'Uberflux listing was found by the archive''s discovery sweep; event was initially unknown and has been corrected to DC34 based on the product page.'
status: released
sources:
- kind: url
  url: https://uberflux.com/product/DC34-powerback
  title: USB-C Power Back for SAOs
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/DC34-powerback
  title: USB-C Power Back for SAOs
  accessed: '2026-09-07'
  note: 'Confirmed maker (caelyb / trueControl), event (DEF CON 34, 2026), price, quantity (75), sold-out status, distribution points, and product photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found was the maker''s own Uberflux storefront listing; no separate maker post, Hackaday page, or repo was located (web search budget for this session was exhausted before a second round of searches could be run). No open-source hardware/firmware files are mentioned on the listing. LED and display fields left empty since this is a passive power-conversion accessory, not documented with an MCU.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/usb-c-power-back-for-saos/
---

The USB-C Power Back for SAOs is a small accessory sold by Uberflux at DEF CON 34 (2026), made by caelyb of trueControl. It steps 5V USB power down to the 3.3V that SAOs (Simple Add-Ons) expect, letting one or more SAOs run continuously from a USB-C wall adapter or battery pack rather than being limited to whatever power a host badge or coin cell battery provides. The maker highlights that it can keep three "#NoICE" SAOs lit simultaneously, a load a standard CR2032 button cell can't sustain, making it useful for people who want to display their SAO collection on a desk or shelf outside of badge season.

It sold for $7 ($6 each at two or more), with 75 units made; the listing shows it as sold out. It was distributed in person at DC34's Badgelife Village, LineCon, and the Queercon Mixer, with post-con shipping offered to continental US buyers for $5. No hardware or firmware files are published for it, and no additional coverage beyond the maker's own storefront page was found.
