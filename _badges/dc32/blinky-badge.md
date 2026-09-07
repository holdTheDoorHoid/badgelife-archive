---
title: Blinky Badge
id: dc32-blinky-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: GothCon
  url: https://x.com/dcgothcon
summary: 'A limited-run LED "blinky" badge sold by GothCon as a fundraiser for their annual dance party at DEF CON 32, themed around a randomized "Spirit Board" (Ouija-style) design.'
functions: 'Lights up with LED patterns; each badge shows a randomized "Spirit Board" themed design/graphic. Wearing it is not required for GothCon party entry.'
look:
  colors: []
  shape: null
  themes:
  - horror
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $40.00
  price_usd: 40.0
  quantity: '300'
  availability: unknown
  distribution:
  - purchase
  where: Sold through the GothCon Shopify store and at the GothCon party during DEF CON 32; proceeds fund the party, which receives no support from DEF CON itself.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: store
  label: Gothcon Badge Store (Shopify)
  url: https://gothconbadge.myshopify.com/
- kind: social
  label: GothCon on X (@dcgothcon)
  url: https://x.com/dcgothcon
- kind: doc
  label: GOTHCON 2024 - DEF CON Forums
  url: https://forum.defcon.org/node/249561
images: []
contact:
  raw:
  - More to follow
notes: []
status: released
sources:
- kind: sheet
  event: dc32
  row: 62
  updated: ''
- kind: url
  url: https://x.com/defcon/status/1811963602175152441
  title: 'DEF CON on X: "Presenting GothCon 2024''s Blinky Badge... Grab your randomized Spirit..."'
  accessed: '2026-09-07'
  note: Confirms the badge name ("GothCon 2024's Blinky Badge"), event year, and the randomized "Spirit Board" theme; announced via GothCon's own account and retweeted by DEF CON.
- kind: url
  url: https://gothconbadge.myshopify.com/
  title: Gothcon Badge Store
  accessed: '2026-09-07'
  note: GothCon's official storefront, used across years; confirms GothCon sells badges as a party fundraiser. Current content on the page describes the 2026 (DC34) badge, not 2024, so its technical specs (LED count, MCU, shape) were not applied to this entry.
- kind: url
  url: https://forum.defcon.org/node/249561
  title: GOTHCON 2024 - DEF CON Forums
  accessed: '2026-09-07'
  note: DEF CON forum thread announcing the 2024 GothCon party; page could not be fully retrieved (connection reset), listed for reference.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Confirmed via GothCon's own X announcement that a "Blinky Badge" with a randomized
    "Spirit Board" theme existed for DEF CON 32 (2024), matching the sheet's title, price
    ($40), and quantity (300). Could not confirm technical specifics (LED count/type, MCU,
    shape, colors, SAO support, availability status) for the 2024 badge specifically: the
    only detailed technical writeup found (44 RGB LEDs, ESP32-C3, bat-shaped PCB) is on
    GothCon's current storefront describing the 2026/DC34 badge, and that same page states
    GothCon's badges for "the past 3 years" (i.e. roughly 2023-2025) were laser-cut acrylic
    rather than custom LED PCBs — so those 2026 specs were deliberately NOT copied onto this
    2024 entry to avoid misattributing a later design. A companion sheet row, dc32-standard-art-badge,
    lists a second non-blinky GothCon badge for the same year, suggesting GothCon offered both
    an LED ("Blinky") and a plain art variant at DC32. No maker photo of the 2024 badge itself
    was found to save. X/Twitter posts with likely photos returned HTTP 402 and could not be
    fetched by tooling.
last_modified_date: '2026-09-07'
---

GothCon is the crew behind the long-running goth-themed dance party held during DEF CON, and each year they sell a fundraiser badge to help cover the cost of throwing the (free, DEF-CON-unaffiliated) event. For DEF CON 32 in 2024, that badge was the "Blinky Badge," an LED badge whose design centered on a randomized "Spirit Board" (Ouija-board-style) graphic — GothCon announced it saying attendees could "grab your randomized Spirit..." badge, with each one carrying a different variant of the theme. The sheet records a $40 price and a run of 300 units, and GothCon also offered a second, non-illuminated "Standard Art Badge" that year for buyers who wanted the artwork without the electronics.

Wearing the badge was never required to get into the GothCon party itself; it functioned primarily as merchandise supporting the event, sold both through GothCon's Shopify storefront and in person at the party during the convention. Specific technical details for this particular year's board — LED count and type, microcontroller, exact shape, and case materials — were not confirmed by any maker source found during research; GothCon's current storefront describes a very different, more elaborate bat-shaped 2026 badge, and explicitly notes that the "past 3 years" of badges (which would include 2024) were simpler laser-cut acrylic designs rather than custom PCBs, so those newer specs are not carried over here.
