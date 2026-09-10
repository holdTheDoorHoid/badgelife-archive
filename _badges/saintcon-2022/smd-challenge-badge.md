---
title: SMD Challenge BADGE
id: saintcon-2022-smd-challenge-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Jup1t3r
summary: 'A SAINTCON 2022 minibadge built to challenge advanced surface-mount soldering skills, with fine-pitch SMD footprints down to 0603/0402.'
functions: 'No electronic function beyond lighting its LEDs once assembled; the point is the soldering challenge itself, working down through 1206/0805/0603/0402-size SMD pads and a "UC Counter" SOIC chip footprint.'
look:
  colors:
  - black
  - yellow
  shape: rectangle
  themes:
  - learn to solder
  - puzzle
tech:
  mcu: null
  leds:
    count: null
    type: SMD
    note: 'LEDs solder to a "Golden Ratio" curve silkscreened as the shared negative/cathode side; exact count not stated in the source.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $5
  price_usd: 5
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: 'Purchased at the SAINTCON store on-site for $5, covering the cost of components and the special tools (Solder Paste Stencil) borrowed at the Circuit Assembly Center to build it.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
images: []
contact: {}
notes:
- Official 2022 surface-mount soldering challenge minibadge from the assembly guide. Found by the event-year sweep, task saintcon-2022.
status: released
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SMD Challenge BADGE
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON MiniBadge Assembly Guide 2022 (page 27)
  accessed: '2026-09-10'
  note: 'Primary source: designer credit "Jup1t3r", $5 store price, difficulty ADVANCED / rarity RARE, assembly instructions describing the LED "Golden Ratio" curve, SMD footprints (1206/0805/0603/0402), a "UC Counter" SOIC chip footprint, and 4x 2-position headers.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'The event''s own official assembly guide confirms the badge, its designer, price, and construction details directly (a primary source, so confidence is high despite most tech fields staying empty). No maker storefront, repo, or social profile for "Jup1t3r" was found, so LED count, PCB shape name, quantity made, and open-source status are left unknown rather than guessed. The two board-face images (extracted from the PDF page) could not be saved with fetch_image.py because they have no standalone image URL -- they are embedded pages inside the single PDF already listed as the source, not separately hosted files.'
last_modified_date: '2026-09-10'
---

The SMD Challenge Badge is a SAINTCON 2022 minibadge designed by Jup1t3r specifically to test and teach advanced surface-mount soldering. Rather than performing any particular function once built, its whole point is the build itself: the board carries a shrinking sequence of SMD pad sizes (1206, 0805, 0603, 0402) and a "UC Counter" SOIC chip footprint, and the official assembly guide rates it ADVANCED difficulty and RARE rarity among the year's minibadges.

Attendees bought it at the SAINTCON store for $5, a price the guide says covers the components and the special tools -- notably a solder paste stencil -- available on loan at the Circuit Assembly Center. LEDs solder down first, oriented against a "Golden Ratio" curve that the silkscreen uses as the shared negative/cathode rail; the remaining passives and 4x 2-position headers (used to chain minibadges together, as is standard for the SAINTCON minibadge system) go on afterward.

No independent maker page, repository, or storefront listing for Jup1t3r turned up beyond the con's own guide, so quantity made, exact LED count, and whether any design files were published remain unknown.

