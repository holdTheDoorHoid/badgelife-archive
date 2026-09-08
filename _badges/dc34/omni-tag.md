---
title: Omni-Tag
id: dc34-omni-tag
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc34
year: 2026
makers:
- name: Coruscant Productions, LLC
  url: https://tropicsquirrel.github.io/shop/
summary: A 3D-printable physical scan tag sold as an optional add-on with Clip-Boy Mk2 orders, used to unlock in-badge collectibles by scanning it instead of entering a code by hand.
functions: Physical scan target for Clip-Boy Mk2's 3D-scanning collectible system; an alternative to typing collectible codes manually.
look:
  colors: []
  shape: null
  themes:
  - kit
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: '+$15'
  price_usd: 15
  quantity: '152 units shipped (first run, bundled with Clip-Boy Mk2 orders)'
  availability: sold_out
  availability_note: 'Bundled only with Clip-Boy Mk2 pre-orders, which closed/sold out; checked 2026-09-08 on the maker storefront.'
  distribution:
  - preorder
  - kit
  where: Add-on option during Clip-Boy Mk2 pre-orders at the maker's storefront (tropicsquirrel.github.io/shop).
make_your_own:
  open_source: partial
  hardware_url: https://github.com/SafeHazard/Clip-Boy
  firmware_url: null
  eda_tool: null
  notes: '3D-printable design file distributed as "omnitag.3mf" in the Clip-Boy GitHub repo; no PCB or firmware involved since this is a passive printed part.'
links:
- label: tropicsquirrel.github.io/shop
  url: https://tropicsquirrel.github.io/shop/
  kind: store
- label: SafeHazard/Clip-Boy (GitHub)
  url: https://github.com/SafeHazard/Clip-Boy
  kind: repo
images: []
contact: {}
notes:
- 3D-printable physical scan tag accessory shipped as an optional add-on with Clip-Boy Mk2 orders for scanning in-badge collectibles. Found by the event-year sweep, task dc34-indie.
- 'Sweep title matched the maker''s own naming ("Omni-Tag"); no correction needed.'
status: released
sources:
- kind: url
  url: https://tropicsquirrel.github.io/shop/
  title: Omni-Tag
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc34-indie); event read as ''dc34''.'
- kind: url
  url: https://tropicsquirrel.github.io/shop/
  title: 'Clip-Boy: The Unofficial DEF CON 34 Electronic Badge — Pre-Order'
  accessed: '2026-09-08'
  note: 'Confirmed Omni-Tag as an optional add-on to Clip-Boy Mk2 orders; maker, price (+$15), 3D-printable design file (omnitag.3mf), and that the first run of 152 units shipped.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own storefront that Omni-Tag is a real, shipped accessory (not just a search snippet). Could not find a dedicated photo of the physical tag itself — the storefront page has no Omni-Tag-specific image, and the GitHub repo file tree for the "omnitag.3mf" design file could not be browsed without authentication (GitHub code search requires sign-in). No chip/electronics involved since this is a passive 3D-printed part. Could not independently verify the exact repo subfolder path for the design file.'
last_modified_date: '2026-09-08'
---

The Omni-Tag is a small, 3D-printable accessory sold by Coruscant Productions, LLC alongside their Clip-Boy Mk2 wrist-mounted badge for DEF CON 34. Clip-Boy Mk2's headline feature is a 3D-scanning system that unlocks in-badge collectibles; the Omni-Tag exists as a purpose-made physical object for people to scan, so they don't have to enter collectible codes by hand. It shipped as a +$15 optional add-on during Clip-Boy Mk2 pre-orders, and the maker's storefront states the first run of 152 units shipped alongside badge orders.

There is no electronics in the Omni-Tag itself — it is a passive printed part, not a powered device — and the design file (`omnitag.3mf`) is shared in the same GitHub repository as the rest of the Clip-Boy Mk2 project, making the accessory itself effectively open-source even though the badge it accompanies is offered in a more limited research-build capacity.

## Make your own

The design is distributed as a 3D-printable `.3mf` file (`omnitag.3mf`) in the `SafeHazard/Clip-Boy` GitHub repository; no PCB fabrication or firmware is involved, since the Omni-Tag is a purely physical scan target.
