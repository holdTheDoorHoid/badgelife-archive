---
title: SECKC Bob mascot coin
id: dc26-seckc-bob-mascot-coin
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc26
year: 2018
makers:
- name: BadgePirates / SecKC
  url: https://badgepirates.com/
summary: A small PCB "poker chip" token made by BadgePirates for SecKC's DEF CON 26 party fundraiser, cut in the shape of BadgePirates' pirate-skull logo with circuit-trace artwork. It is a separate, smaller item from the crew's large round "Bob" mascot wreath badge made for the same event.
functions: 'Passive novelty PCB coin/token with no onboard electronics of its own; carries a footprint for a BadgeLife-style SAO header on the back so a buyer can solder on their own LED.'
look:
  colors:
  - red
  - black
  shape: circle
  themes:
  - skull
  - coin
  form_factor: coin
tech:
  mcu: none
  leds:
    count: null
    type: none
    note: 'Unpopulated SAO-header footprint for an optional single LED; design files also include gold and gray colorway art, but only red and black are confirmed as physically sold.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $7
  price_usd: 7
  quantity: ''
  availability: limited
  availability_note: 'Tindie listing showed 4 units left in stock as of check on 2026-09-07; listing dates to 2018 and may not reflect current stock.'
  distribution:
  - purchase
  where: 'Sold by BadgePirates on Tindie ("SecKC Party Tokens"); proceeds helped fund the "SecKC the World" party thrown at DEF CON 26. Orders included both color variants; the token could originally be redeemed for a free shot at the party.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Coin
  firmware_url: null
  eda_tool: null
  notes: 'The repo''s Coin/ folder has raster/vector artwork (PNG, SVG) and a DXF outline (BPSkull_Black.dxf) but no schematic or Gerber files specific to this coin; the repo''s Gerbers/ folder is for the separate, larger main "Bob" wreath badge.'
links:
- label: github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Coin
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Coin
  kind: repo
- label: SecKC Party Tokens on Tindie
  url: https://www.tindie.com/products/badgepirates/seckc-party-tokens/
  kind: store
- label: BadgePirates
  url: https://badgepirates.com/
  kind: website
images:
  - file: assets/images/badges/dc26/seckc-bob-mascot-coin/2281fe716a.png
    source: "https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Coin"
    credit: "BadgePirates"
    caption: "Coin design: poker-chip-shaped PCB outline with BadgePirates pirate-skull logo and circuit-trace artwork, red and black"
  - file: assets/images/badges/dc26/seckc-bob-mascot-coin/9a1ce88ec1.jpg
    source: "https://www.tindie.com/products/badgepirates/seckc-party-tokens/"
    credit: "BadgePirates"
    caption: "Physical PCB tokens as sold on Tindie, red and black colorways with the BadgePirates pirate-skull logo"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26/tree/master/Coin
  title: SECKC Bob mascot coin
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc26''.'
- kind: url
  url: https://github.com/BadgePiratesLLC/DefCon_SecKC_26
  title: 'BadgePiratesLLC/DefCon_SecKC_26 (archived Dec 2023)'
  accessed: '2026-09-07'
  note: 'Repo root; confirms the Coin/ folder is separate from the Gerbers/ and Photos/ material for the main round "Bob" wreath badge (see sibling entry dc26-defcon-seckc-26). No README found describing the coin.'
- kind: url
  url: https://www.tindie.com/products/badgepirates/seckc-party-tokens/
  title: SecKC Party Tokens from BadgePirates on Tindie
  accessed: '2026-09-07'
  note: 'Matches the Coin/ artwork (PCB tokens with pirate-skull design, red/black, BadgeLife SAO header on back); gives price ($7), stock count, and that it funded the "SecKC the World" DEF CON 26 party and originally came with a free shot.'
- kind: url
  url: https://badgepirates.com/
  title: Badge Pirates — Making badges for fun and no profit
  accessed: '2026-09-07'
  note: 'Maker''s site; confirms "Badge Pirates" branding and DEF CON/SecKC 26 portfolio entry, but no coin-specific detail.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    No source actually calls this item "Bob" or a "mascot coin" — the design files in the linked
    Coin/ folder (BPSkull_Black/Gold/Gray/Red.png, drawing-1.svg, etc.) all show BadgePirates'
    pirate-skull logo on a poker-chip-shaped outline, not the fedora-and-cigar "Bob" silhouette that
    is SecKC's actual mascot. "Bob" appears instead on a separate, much larger round badge from the
    same repo/event (see sibling entry dc26-defcon-seckc-26, which already documents that board and
    notes "a matching commemorative coin" of uncertain relationship). This entry is kept as a
    distinct item — the small skull-logo PCB token/coin sold on Tindie as "SecKC Party Tokens" to
    fund the DEF CON 26 SecKC party — since it is a physically different product from the wreath
    badge, but the title's "Bob mascot" attribution is not supported by any source found and may be
    a mix-up from the original automated sweep. Left empty: exact quantity made, SAO header pin
    count/version, and whether the gold/gray colorway artwork was ever actually produced as physical
    coins (only red and black are confirmed via the Tindie photo).
last_modified_date: '2026-09-07'
---

BadgePirates, the crew behind SecKC's (Kansas City's security meetup) DEF CON 26 badge, also produced a small circuit-board novelty coin shaped like a poker chip and cut with their pirate-skull logo, picked out in red and black soldermask with circuit-trace decoration. It was sold through BadgePirates' Tindie store as "SecKC Party Tokens" for $7 an order (both colors included) to help fund "SecKC the World," the group's official DEF CON 26 hotel party — the token could originally be redeemed there for a free shot. The bare board carries an unpopulated BadgeLife-style SAO header footprint on the back so a buyer could solder on their own indicator LED, but has no other electronics.

Despite this entry's title, no source found calls the piece "Bob" or a mascot coin. The name "Bob" actually belongs to a different, much larger round badge the same BadgePirates/SecKC team built for DEF CON 26 — a wreath of 42 charlieplexed LEDs surrounding a silhouette of Bob, SecKC's fedora-and-cigar mascot (see the separate archive entry for that badge). The design files for this smaller coin, found in the same GitHub repository's `Coin/` folder, show only the pirate-skull logo, with no trace of the Bob silhouette. The two items likely got conflated during an earlier automated sweep of the repository.

## Make your own

The `Coin/` folder in the DEF CON 26 SecKC GitHub repo has the coin's artwork as PNG and SVG files plus a DXF cutting outline (`BPSkull_Black.dxf`), enough to reproduce the shape and graphics, but no schematic or Gerber files specific to this piece — the repo's `Gerbers/` folder is for the separate main wreath badge instead.
