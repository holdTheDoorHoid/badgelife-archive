---
title: DefCon 27 SecKC Party Star
id: dc27-seckc-defcon-party-badge-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: BadgePirates
  url: https://www.tindie.com/stores/badgepirates/
summary: A sheriff-star-shaped party badge BadgePirates made for the SecKC gathering at DEF CON 27, gold-plated on black PCB with "SECKC" and "The World Again" artwork and lights at the star's points.
functions: Blinking LED lights arranged around the star shape (no MCU, LED count/driver not documented).
look:
  colors:
  - black
  - gold
  shape: star
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: '$4.99 (2021 resale of leftover broken/unpopulated stock; original event price not documented)'
  price_usd: null
  quantity: ''
  availability: limited
  distribution: []
  where: Originally distributed at the SecKC party at DEF CON 27 (2019); a small remainder of non-working assembled units and bare boards was later resold by BadgePirates on Tindie.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27
  firmware_url: null
  eda_tool: KiCad
links:
- label: store.badgepirates.com/product/preorder-seckc-defcon-party-badge-sao
  url: https://store.badgepirates.com/product/preorder-seckc-defcon-party-badge-sao/
  kind: store
- label: www.tindie.com/products/badgepirates/defcon-27-seckc-party-star
  url: https://www.tindie.com/products/badgepirates/defcon-27-seckc-party-star/
  kind: store
- label: github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27
  url: https://github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27
  kind: repo
images:
  - file: assets/images/badges/dc27/seckc-defcon-party-badge-sao/9aa7d92c03.jpg
    source: "https://www.tindie.com/products/badgepirates/defcon-27-seckc-party-star/"
    credit: "BadgePirates"
    caption: "Photo of salvaged/broken Party Star badges as resold on Tindie"
  - file: assets/images/badges/dc27/seckc-defcon-party-badge-sao/c7089c58bf.jpg
    source: "https://github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27"
    credit: "BadgePirates"
    caption: "Promotional banner image of the Party Star badge design"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
- 'Sweep imported this as "SecKC Defcon Party Badge - SAO"; the maker''s own naming (Tindie listing and GitHub repo) is "DefCon 27 SecKC Party Star", used here as the title.'
- 'This appears to be the same item as another archive stub, dc27-seckc-party-star ("DefCon 27 SecKC Party Star"), which links the identical Tindie page and was found by the same sweep under a different title.'
- 'The original store.badgepirates.com listing (a preorder page) no longer resolves; the domain does not respond as of 2026-09-08. Content could not be verified from it directly.'
- 'Set type to "badge" rather than "sao": the Tindie listing and GitHub repo describe it as a standalone party badge/keepsake with no SAO header, despite the promotional image being filed as "SAO_Twitter_Banner.jpg" in the repo.'
status: released
sources:
- kind: url
  url: https://store.badgepirates.com/product/preorder-seckc-defcon-party-badge-sao/
  title: SecKC Defcon Party Badge - SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''dc27''.'
- kind: url
  url: https://www.tindie.com/products/badgepirates/defcon-27-seckc-party-star/
  title: DefCon 27 SecKC Party Star from BadgePirates on Tindie
  accessed: '2026-09-08'
  note: Confirms the item, maker, event, and a 2021 resale of leftover non-working/bare-board units at $4.99; provided the product photo.
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27
  title: BadgePiratesLLC/DefCon_SecKCPartyStar_27
  accessed: '2026-09-08'
  note: Maker's own repo; contains a full KiCad schematic, PCB layout, footprints, gerbers, and a BOM (ibom.html), but no firmware; describes it as the "Party Star 'badge' for the DEFCON 27 SecKC Party"; source of the promo banner image.
- kind: url
  url: https://docs.badgepirates.com/catalog/
  title: Catalog - BadgePirates Documents
  accessed: '2026-09-08'
  note: BadgePirates' own catalog lists this as a "Conference badge variant" / "Party variant of the DC27 SecKC badge", supporting type badge rather than sao.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): confirmed Tindie listing (product name, $4.99 price, broken/bare-board resale stock, star shape with blinking LEDs), GitHub repo (archived, "Party Star ''badge''" per README), and docs.badgepirates.com catalog ("Party Star variant" of the DC27 conference badge). Corrected a factual error: the prior draft claimed the GitHub repo held only KiCad footprints with no schematic or BOM; the repo actually contains a full schematic, PCB layout, gerbers, and a BOM (ibom.html) -- only firmware is genuinely absent, consistent with the board carrying no MCU. store.badgepirates.com still does not resolve (confirmed again). Original production quantity, price, and exact distribution method at the 2019 SecKC party remain undocumented; LED count/driver type undocumented (left blank rather than read off raw schematic files, which would be new research beyond this pass). Likely a duplicate of the dc27-seckc-party-star stub entry, which points at the same Tindie listing -- flagged for a human to dedupe, not resolved here.'
last_modified_date: '2026-09-08'
---

BadgePirates made this sheriff-star-shaped party badge for the SecKC crew's gathering at DEF CON 27 in 2019. The design is a gold-plated star on black PCB reading "SECKC" and "The World Again" around a circuit-board-styled crest, with lights built into the star's points; BadgePirates' own project catalog files it as a "party variant" of that year's SecKC conference badge rather than as a plug-in SAO, despite the promotional artwork in the GitHub repo being named as if it were one.

The hardware files (KiCad schematic, PCB layout, footprints, gerbers, and a bill of materials, but no firmware) are published on GitHub; the repo is archived and gives no further build narrative. In 2021, BadgePirates resold a small remaining stock of these badges on Tindie at $4.99 each — some non-working assembled units, some bare unpopulated boards — as leftovers found in storage, rather than as new production. The original 2019 preorder page on BadgePirates' own storefront is referenced in the archive but the domain no longer resolves, so its listed price and quantity could not be confirmed independently.

## Make your own

The maker's repo (github.com/BadgePiratesLLC/DefCon_SecKCPartyStar_27) includes a KiCad schematic, PCB layout, custom footprints, gerbers, and a bill of materials (as an interactive BOM HTML file), but no firmware — consistent with the board carrying no MCU.
