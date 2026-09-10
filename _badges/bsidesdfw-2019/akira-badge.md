---
title: AKIRA Badge
id: bsidesdfw-2019-akira-badge
layout: badge
parent: BSides Dfw 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsidesdfw-2019
year: 2019
makers:
- name: alt_bier (gowenrw)
  url: https://twitter.com/alt_bier
summary: The official BSidesDFW 2019 conference badge, themed on the anime film Akira, depicting Kaneda's motorcycle in motion against Neo-Tokyo destruction artwork.
functions: LEDs on the bike's tires animate to give the illusion of motion; the badge also carries an onboard cryptography challenge.
look:
  colors: []
  shape: null
  themes:
  - anime
  - movie
  - motorcycle
tech:
  mcu: CH552G
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
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/gowenrw/BSidesDFW_2019_Badge
  firmware_url: https://github.com/gowenrw/BSidesDFW_2019_Badge
  eda_tool: null
links:
- label: akirabadge.com
  url: https://akirabadge.com/
  kind: website
- label: altbier.us
  url: https://altbier.us/
  kind: website
- label: gowenrw/BSidesDFW_2019_Badge
  url: https://github.com/gowenrw/BSidesDFW_2019_Badge
  kind: repo
images:
  - file: assets/images/badges/bsidesdfw-2019/akira-badge/e0ef4e3c8d.gif
    source: "https://akirabadge.com/"
    credit: "alt_bier (gowenrw)"
    caption: "Animated view of the Akira badge, Kaneda's motorcycle with LEDs on the tires"
  - file: assets/images/badges/bsidesdfw-2019/akira-badge/c58fe1cfad.jpg
    source: "https://akirabadge.com/"
    credit: "alt_bier (gowenrw)"
    caption: "Akira-themed pill-shaped lanyard"
contact: {}
notes:
- 'Sweep imported the title as "Akira Badge"; the maker''s own site and repo call it "AKIRA Badge" (all caps) — corrected here.'
- Official BSidesDFW 2019 conference badge themed on the film Akira, with Kaneda's motorcycle rendered in LEDs on a CH552G microcontroller, the badge's first use of surface-mount assembly, plus an onboard crypto challenge. Found by the event-year sweep, task bsides-bsidesdfw.
status: released
sources:
- kind: url
  url: https://akirabadge.com/
  title: AKIRA Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsidesdfw); event read as ''BSides DFW 2019''.'
- kind: url
  url: https://akirabadge.com/
  title: AKIRA Badge
  accessed: '2026-09-10'
  note: Maker's project site; confirmed event, maker, CH552G MCU, LED-animated tires, SMD assembly, crypto challenge, and matching lanyard concept; source of both saved images.
- kind: url
  url: https://altbier.us/
  title: Alt_Bier badge portfolio
  accessed: '2026-09-10'
  note: Maker's badge index page; confirms alt_bier made the badge and links it to akirabadge.com under BSidesDFW 2019.
- kind: url
  url: https://github.com/gowenrw/BSidesDFW_2019_Badge
  title: gowenrw/BSidesDFW_2019_Badge
  accessed: '2026-09-10'
  note: Public GitHub repo hosting the badge's code, art, CAD, and fab files; used to fill make_your_own fields.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Maker''s own project site and GitHub repo confirmed the core facts (event, maker, MCU, theme, assembly, crypto challenge). Price, quantity made, LED count/type, display, and distribution details were not stated on any source found and are left empty. No press coverage or storefront listing was found in the time budgeted.'
last_modified_date: '2026-09-10'
---

The AKIRA Badge was the official BSidesDFW 2019 conference badge, designed by alt_bier (Richard Gowen, gowenrw) with concept input from @0isac0 and artwork by @unspecific. It depicts Kaneda's motorcycle from the anime film *Akira* riding past artwork of Neo-Tokyo's destruction, with LEDs mounted on the bike's tires to create the illusion of motion. The badge is built around a CH552G microcontroller, an inexpensive chip the maker chose partly because documentation for it was scarce at the time, and the project site doubles as a CH552G resource for other hobbyists.

This was the first badge alt_bier designed using surface-mount components, a choice that required borrowing an industrial reflow oven and enlisting volunteers at assembly parties to hand-place hundreds of parts. The badge also includes an onboard cryptography challenge. A matching pill-shaped lanyard echoes the bike's tail-light silhouette, a design choice made after the team decided against showing the back of Kaneda's jacket directly on the badge.

## Make your own

Hardware, art, CAD, and firmware files are published on GitHub at [gowenrw/BSidesDFW_2019_Badge](https://github.com/gowenrw/BSidesDFW_2019_Badge), and mirrored for browsing at [akirabadge.com](https://akirabadge.com/), which also includes CH552G reference material and details on the badge's cryptography challenge.
