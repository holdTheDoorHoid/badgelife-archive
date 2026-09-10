---
title: DC801-SAINTCON2017-Minibadge
id: saintcon-2017-dc801-saintcon2017-minibadge
layout: badge
parent: Saintcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2017
year: 2017
makers:
- name: hamster
  url: https://github.com/hamster
summary: A small DC801-themed SAINTCON 2017 minibadge with two automatic slow-cycling RGB LEDs, usable as a minibadge or a shirt pin.
functions: 'No interactivity: two 3mm RGB LEDs with built-in auto-color-cycling ICs light up automatically when powered, no MCU or programming involved.'
look:
  colors:
  - black
  shape: skull
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 2
    type: discrete (3mm auto-cycling RGB, self-contained IC per LED)
    note: 'LED brightness set by choice of R1: 0 ohm (brightest, 20-55mA), 470 ohm (bright, 3-4mA), or 1k ohm (dim, 1.5-2mA).'
  display: none
  connectivity: []
  battery: none (minibadge mode, powered by host SAINTCON badge); optional coin-cell holder board included for standalone shirt-pin mode
  sao_version: none
get_one:
  price: ~$0.91 per unit (100-unit BOM cost, October 2017)
  price_usd: 0.91
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed at SAINTCON 2017 by DC801; exact distribution method (free drop vs. sold) not stated in the source.
make_your_own:
  open_source: true
  hardware_url: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  firmware_url: null
  eda_tool: KiCad
  license: MIT
  notes: Repo includes KiCad PCB files, 3D renders, a BOM (per-unit cost ~$0.91 at 100-unit pricing as of 10/2017), assembly instructions, instruction cards, and a separate battery-holder board for shirt-pin mode.
  bom_url: https://github.com/DC801/DC801-SAINTCON2017-Minibadge
links:
- label: github.com/hamster/DC801-SAINTCON2017-Minibadge
  url: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  kind: repo
  archived: https://web.archive.org/web/20260510061812/https://github.com/hamster/DC801-SAINTCON2017-Minibadge
- label: github.com/DC801/DC801-SAINTCON2017-Minibadge
  url: https://github.com/DC801/DC801-SAINTCON2017-Minibadge
  kind: repo
images:
- file: assets/images/badges/saintcon-2017/dc801-saintcon2017-minibadge/1530c0055b.jpg
  source: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  credit: hamster
  caption: Front of the assembled DC801 SAINTCON 2017 minibadge
  archived: https://web.archive.org/web/20260510061812/https://github.com/hamster/DC801-SAINTCON2017-Minibadge
- file: assets/images/badges/saintcon-2017/dc801-saintcon2017-minibadge/e54e04fd37.jpg
  source: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  credit: hamster
  caption: Powered DC801 minibadge showing the RGB LEDs lit
  archived: https://web.archive.org/web/20260510061812/https://github.com/hamster/DC801-SAINTCON2017-Minibadge
- file: assets/images/badges/saintcon-2017/dc801-saintcon2017-minibadge/d7ed242a2f.jpg
  source: https://github.com/DC801/DC801-SAINTCON2017-Minibadge
  credit: DC801 / hamster
  caption: Assembled DC801 sheep-skull minibadges with LEDs and pin headers
- file: assets/images/badges/saintcon-2017/dc801-saintcon2017-minibadge/85fdcef82e.png
  source: https://github.com/DC801/DC801-SAINTCON2017-Minibadge
  credit: DC801 / hamster
  caption: 3D render of the DC801 sheep minibadge front
contact: {}
notes:
- The community sheet listed this as "DC801 Sheep - Hampster (unofficial SAINTCON 2017 minibadge)"; the maker's own repo does not use "Sheep" in its title, so the title here follows the design (a sheep skull-and-crossbones) and drops the sheet's awkward phrasing.
- This appears to be the same item as saintcon-2017-dc801-saintcon2017-minibadge, whose links point to a fork of the same repo under hamster's personal GitHub account rather than the DC801 org.
status: released
sources:
- kind: url
  url: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  title: DC801-SAINTCON2017-Minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''SAINTCON 2017''.'
  archived: https://web.archive.org/web/20260510061812/https://github.com/hamster/DC801-SAINTCON2017-Minibadge
- kind: url
  url: https://github.com/hamster/DC801-SAINTCON2017-Minibadge
  title: DC801-SAINTCON2017-Minibadge README
  accessed: '2026-09-07'
  note: 'README and BOM: confirms DC801 theme, two auto-cycling RGB LEDs, minibadge/shirt-pin modes, KiCad files, MIT license, BOM cost ~$0.91/unit at 100 qty (10/2017), battery holder board for shirt-pin mode.'
  archived: https://web.archive.org/web/20260510061812/https://github.com/hamster/DC801-SAINTCON2017-Minibadge
- kind: url
  url: https://github.com/DC801/DC801-SAINTCON2017-Minibadge
  title: DC801 Sheep - Hampster (unofficial SAINTCON 2017 minibadge)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://raw.githubusercontent.com/DC801/DC801-SAINTCON2017-Minibadge/master/README.md
  title: DC801-SAINTCON2017-Minibadge README
  accessed: '2026-09-10'
  note: 'Primary source: design description, LED/resistor specs, assembly instructions, full BOM with pricing, and image links.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own repo confirms design and BOM. No quantity manufactured, sale price, or distribution method (e.g. free drop vs. sold) is stated anywhere in the repo, so get_one fields are left empty. No MCU is used; the LEDs are self-contained auto-cycling parts, not driven by a controller. Merged with duplicate entry 'DC801 Sheep Minibadge (unofficial SAINTCON 2017 minibadge)' (saintcon-2017-dc801-sheep-hampster-unofficial-saintcon-2017-minibadge).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/saintcon-2017/dc801-sheep-hampster-unofficial-saintcon-2017-minibadge/
---

This is a DC801-themed minibadge made for SAINTCON 2017 by a GitHub user going by "hamster." It plugs into the pin headers of the main SAINTCON 2017 conference badge (or can be worn on its own as a shirt pin) and lights up with two 3mm RGB LEDs that cycle color automatically on their own, without any microcontroller or firmware involved. Builders choose one of three resistor values for R1 to set the LED brightness, from a bright 20-55mA down to a dim 1.5-2mA.

The project is fully open source, with KiCad PCB files, 3D renders, a bill of materials, and printed instruction cards all published in the maker's GitHub repository under the MIT license. The BOM shows an estimated cost of about $0.91 per unit at 100-unit component pricing as of October 2017. A companion board is also included for mounting a coin-cell battery so the minibadge can run standalone as a shirt pin instead of drawing power from the host badge.

No source found states how many units were actually built, whether it was sold or given away, or its retail price, so those fields are left blank.

## Make your own

1. Insert the two LEDs into the back of the board (shorter leg toward the top), bend the legs over the pads, trim, and solder.
2. Choose and solder resistor R1: 0 ohm for brightest (20-55mA), 470 ohm for bright (3-4mA), or 1k ohm for dim (1.5-2mA).
3. For minibadge mode: break pin headers and 8-pin sockets to size, insert the socket pins into the SAINTCON badge, place the minibadge on top, and solder both sides.
4. For shirt-pin mode: skip the pin headers and instead solder the included tie-tack pin to the large pad at the top; optionally add the battery-holder board from the "Shirt Pin Battery" folder for standalone power.

Source: https://github.com/hamster/DC801-SAINTCON2017-Minibadge (KiCad files, BOM, renders, MIT license).

## Notes merged from the duplicate entry "DC801 Sheep Minibadge (unofficial SAINTCON 2017 minibadge)"

DC801 designed this unofficial minibadge for SAINTCON 2017: a small black PCB silkscreened with a sheep skull-and-crossbones and the DC801 name. It carries no microcontroller. Instead, two 3mm RGB LEDs (Chanzon AA0018x100) wired for automatic slow color-cycling light up on their own whenever the board is powered, with a user-selected resistor (0, 470, or 1k ohm) setting the brightness and current draw.

The board was built to work two ways: soldered onto pin headers and sockets so it plugs into the official SAINTCON badge as an add-on minibadge, or built without headers and finished with a butterfly-clutch tie tack so it can be worn as a standalone shirt pin. A companion coin-cell holder board (in the repo's "Shirt Pin Battery" folder) lets the pin mode run independently of a host badge.

Hardware files, a 3D render, assembly photos, and a full bill of materials are published in DC801's GitHub repo, credited to designer "hamster." The BOM (dated October 2017) puts per-unit parts cost at about $0.91 in 100-unit quantities, covering the PCB, LEDs, resistor, headers/sockets, a butterfly clutch, packaging, and an instruction card - but the repo does not say how many were actually produced or whether they were given away or sold at the con.
