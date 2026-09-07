---
title: The Call Center Village Telephone Booth SAO
id: dc34-the-call-center-village-telephone-booth-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: Call Center Village
  url: https://www.callcentervillage.com/
  role: Patrick Labbett (design)
summary: A minimal, power-only SAO shaped like a British telephone booth; a single LED lights up when it is plugged into a badge's SAO header.
functions: Small, light-up telephone booth
look:
  colors: []
  shape: telephone booth
  themes:
  - retro computer
  - village badge
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: single 1206 SMD indicator LED (LCSC C49018), lit whenever the SAO is powered
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v2
get_one:
  price: $5.00 kit, $10.00 pre-soldered
  price_usd: 5.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold via a Stripe payment link (billing.calltheory.com) linked from the Call Center Village community sheet entry; page did not render enough for automated review to confirm stock.
make_your_own:
  open_source: yes
  hardware_url: https://git.calltheory.com/callcentervillage/shitty-add-on
  firmware_url: null
  eda_tool: KiCad
links:
- label: billing.calltheory.com/b/cNi8wOdNw213b1X5yj3VC05
  url: https://billing.calltheory.com/b/cNi8wOdNw213b1X5yj3VC05
  kind: store
- label: git.calltheory.com/callcentervillage/shitty-add-on
  url: https://git.calltheory.com/callcentervillage/shitty-add-on
  kind: repo
- label: Call Center Village
  url: https://www.callcentervillage.com/
  kind: website
images: []
contact:
  discord: Patrick
  emails:
  - patrick.labbett@callcentervillage.com
  - callcentervillage@defcon.social
notes: []
status: listed
sources:
- kind: sheet
  event: dc34
  row: 12
  updated: 6/2/2026 0:44:14
  listing: New
- kind: url
  url: https://git.calltheory.com/callcentervillage/shitty-add-on
  title: 'callcentervillage/shitty-add-on: Call Center Village SAO (Forgejo repo)'
  accessed: '2026-09-06'
  note: Maker's own README and KiCad project; confirms it is a passive, power-only SAO (no MCU, no I2C) with one indicator LED, SAO v2 6-pin header, phone-booth-shaped board outline, CC BY-SA 4.0, designed in KiCad 10, with gerbers and a PCBWay-ready fabrication package.
- kind: url
  url: https://billing.calltheory.com/b/cNi8wOdNw213b1X5yj3VC05
  title: Stripe Checkout payment link
  accessed: '2026-09-06'
  note: Storefront link from the sheet; page is a JS-rendered Stripe Checkout and did not expose product text, price breakdown, or stock status to automated fetch.
- kind: url
  url: https://www.callcentervillage.com/
  title: Call Center Village
  accessed: '2026-09-06'
  note: Confirms Call Center Village as a DEF CON village/contest (social engineering call-center challenge) run by Patrick Labbett of Call Theory; no separate SAO page found there.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The repo README is the maker's own primary source and confirms the technical description. Could not find a photo of the assembled physical SAO (repo contains only KiCad files and vector board-outline artwork, no raster photos); could not confirm quantity made or current stock/availability since the storefront is a JavaScript Stripe Checkout page that did not return readable content to fetch. Price on the sheet ($5 kit / $10 pre-soldered) is unverified against the storefront but is plausible for a simple one-LED SAO and was kept as-is.
last_modified_date: '2026-09-06'
---

Call Center Village is a DEF CON village/contest run by Patrick Labbett of Call Theory, built around a social-engineering challenge staged through a British-style telephone booth and vintage phones. For DEF CON 34 the group made a matching SAO: a small PCB cut into the outline of a phone booth. It is deliberately minimal — there is no microcontroller and no I2C logic, just a single 1206 SMD LED and a current-limiting resistor wired straight across the SAO v2 header's power pins, so the badge lights up simply because it is plugged in.

The design is fully open, published on the group's own Forgejo instance under CC BY-SA 4.0, with KiCad 10 source files, a bill of materials (LCSC part numbers), and ready-to-order fabrication packages for both PCBWay and a generic board house. The sheet lists it for sale as a $5 kit or $10 pre-soldered through a Stripe payment link; that storefront could not be independently confirmed by automated fetch, and no photo of an assembled unit was found, so those two points are noted as unverified.
