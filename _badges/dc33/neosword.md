---
title: NeoSword
id: dc33-neosword
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: Untitled Electronics
  url: https://untitledelec.com
  role: '@wrickert from the discord, per the community sheet'
summary: A sword-shaped 3-port SAO totem with programmable lights and sound effects, running MicroPython.
functions: 'SAO totem (hosts up to 3 SAO modules); programmable LED patterns and sound effects (e.g. plays the Wilhelm Scream); user-scriptable via MicroPython'
look:
  colors: []
  shape: sword
  themes:
  - sci-fi
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: 4x AA (in the handle)
  sao_version: null
get_one:
  price: $140
  price_usd: 140.0
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - free_drop
  where: Sold via untitledelec.com; also free pickup available at the Badgelife Village at DEF CON 33
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: null
  eda_tool: null
  license: CERN OHL-S
  notes: 'Maker states: "All source code, CAD, and anything else we can think of will be freely available." No specific repo/CAD link found yet.'
links:
- label: untitledelec.com/products/defcon-33-indy-badge-the-neosword
  url: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  kind: website
- label: bsky.app/profile/untitledelec.bsky.social
  url: https://bsky.app/profile/untitledelec.bsky.social
  kind: social
images:
- file: assets/images/badges/dc33/neosword/6b5490302a.jpg
  source: "https://untitledelec.com/products/defcon-33-indy-badge-the-neosword"
  credit: "Untitled Electronics"
  caption: "The NeoSword DC33 SAO totem"
- file: assets/images/badges/dc33/neosword/9191db8430.jpg
  source: "https://untitledelec.com/products/defcon-33-indy-badge-the-neosword"
  credit: "Untitled Electronics"
  caption: "NeoSword handle and blade detail"
contact: {}
notes: []
status: released
sources:
- kind: sheet
  event: dc33
  row: 24
  updated: 7/14/2025 15:02:31
- kind: url
  url: https://untitledelec.com/products/defcon-33-indy-badge-the-neosword
  title: "Defcon 33 Indy badge: The NeoSword!"
  accessed: '2026-09-06'
  note: Primary source for price, description, features, battery, license, images, and pickup/shipping details.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The maker's storefront confirms this is a badge-side SAO totem (not itself an SAO plugging into a badge) with 3 SAO ports, MicroPython, CERN OHL-S open-source licensing, and 4xAA power. Could not find an MCU model, LED count/type, quantity made, or a specific GitHub/CAD repo link despite the maker's stated intent to publish source; the Bluesky profile page yielded no readable post content. A companion accessory, "3 Stones SAO," is sold separately by the same maker for DC33 but was not researched as part of this entry.
last_modified_date: '2026-09-06'
---

The NeoSword is a sword-shaped SAO totem made by Untitled Electronics for DEF CON 33 (2025), sold as an "Indy badge" (independent, unofficial badge) rather than an SAO that plugs into someone else's badge. It hosts up to three SAO modules of its own, runs MicroPython so owners can reflash its behavior without exploiting anything, and combines programmable LED lighting with sound effects (the maker specifically calls out the Wilhelm Scream as a stock effect). It runs on four AA batteries housed in the sword's handle rather than USB power.

Untitled Electronics sold the NeoSword for $140, with badges either shipped by August 1, 2025 or available for free pickup at the Badgelife Village at DEF CON 33; a few early pickups were announced via the maker's Bluesky account. The maker also offered a $20 bundle discount when purchased together with a separate "3 Stones SAO" accessory. As of research, the listing shows the item sold out.

The maker states the hardware design, firmware source, and CAD files will be released under the CERN OHL-S open-source hardware license, though a specific repository or file link was not found during this pass. The same maker (as "Untitled Electronics") also had an unnamed badge/SAO entry on the DC31 community sheet, suggesting a history of DEF CON badge releases prior to the NeoSword.
