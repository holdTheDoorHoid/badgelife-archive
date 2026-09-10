---
title: UTAH HOME LABS BADGE
id: saintcon-2022-utah-home-labs-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: bfcoder
- name: klipper
  url: https://github.com/klipperx
- name: v0rtex
summary: A passive stackable minibadge for the Utah Home Labs (UHL) community, sold for donations at SAINTCON 2022's HomeLabs Community Booth.
functions: 'Passive: four LEDs light up when the minibadge is powered through its edge-connector pins. No microcontroller or interactive behavior.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: Each LED wired in series with its own resistor, straight across the power rail supplied through an 8-pad edge connector; no driver IC.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Sold for donations to Utah Home Labs at the HomeLabs Community Booth, SAINTCON 2022.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/klipperx/UHL-minibadge-2022
  firmware_url: null
  eda_tool: null
  notes: 'Repo published under MIT license (James Carbine, 2022) but contains only a hand-drawn schematic image (drawio export), not a full KiCad project, Gerbers, or BOM.'
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
- label: github.com/klipperx/UHL-minibadge-2022
  url: https://github.com/klipperx/UHL-minibadge-2022
  kind: repo
images: []
contact: {}
notes:
- Personal Utah Home Labs group minibadge, separate entry from the official Homelabs community/CAT6 badges already catalogued. Found by the event-year sweep, task saintcon-2022.
- 'Duplicate of an existing entry, other-uhl-minibadge-2022-utah-home-labs-minibadge, found by an earlier sweep under event "other" (no SAINTCON tie was known at the time). The official 2022 minibadge assembly-guide PDF found in this pass confirms both entries describe the same physical board and ties it to SAINTCON 2022. Left in place per instructions; not merged or deleted.'
status: listed
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: UTAH HOME LABS BADGE
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: SAINTCON 2022 MiniBadge Assembly Guide, p.50
  accessed: '2026-09-10'
  note: 'Confirms entry "UTAH HOME LABS BADGE — Designed by: bfcoder, klipper, v0rtex. This is the UHL Group Minibadge. We will be selling these for donations to UHL at the HomeLabs Community Booth." Rated difficulty BEGINNER, rarity UNCOMMON.'
- kind: url
  url: https://github.com/klipperx/UHL-minibadge-2022
  title: UHL-minibadge-2022 — Utah Home Labs Minibadge
  accessed: '2026-09-10'
  note: 'Klipper''s (James Carbine) own repo for "Utah Home Labs Minibadge for 2022"; matches this item by name and maker. MIT licensed; contains only a README, LICENSE, and one schematic image, no KiCad project or Gerbers.'
- kind: url
  url: https://raw.githubusercontent.com/klipperx/UHL-minibadge-2022/main/Circuit_Diagram_A.drawio.png
  title: UHL-minibadge-2022 circuit diagram
  accessed: '2026-09-10'
  note: 'Viewed directly: shows 4 LEDs, each with its own series resistor, wired to power/ground across an 8-pad edge connector (4 pairs of pads) — a passive lighting circuit, no MCU. Diagram only, not a photo of the item, so not saved as an image.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'The official SAINTCON 2022 minibadge assembly guide confirms this item exists, names its three makers, and its purpose (sold for UHL donations at the HomeLabs Community Booth) — matching the sheet entry exactly, so the sweep''s facts are solid (confidence would be higher only with the maker''s own page independently naming SAINTCON). It appears to be the same physical board as klipperx''s (James Carbine''s) GitHub repo "UHL-minibadge-2022", whose name, maker, and 2022 date all line up, and which supplies the LED/circuit detail (no MCU; 4 LEDs, each with a series resistor, across an 8-pad edge connector) filled in above. That repo is also cited by an existing separate entry, other-uhl-minibadge-2022-utah-home-labs-minibadge (event "other", since that earlier pass had no source tying it to a convention) — reported as a duplicate rather than merged, per instructions. No price, quantity, or photo of the assembled board was found anywhere; get_one.price/quantity and images are left empty. functions/tech were carried from the repo''s schematic on the assumption the GitHub repo and the PDF listing are the same board, which is well supported (identical name, makers overlap, same year) but not stated in so many words on either page.'
last_modified_date: '2026-09-10'
---

The UTAH HOME LABS BADGE is a minibadge made for SAINTCON 2022 by bfcoder, klipper (James Carbine), and v0rtex, representing the Utah Home Labs (UHL) group — a personal/community minibadge distinct from the event's official HomeLabs community minibadge and HomeLabs CAT6 minibadge, which are catalogued separately. Per the official 2022 minibadge assembly guide, it was sold for donations to UHL at the HomeLabs Community Booth, rated beginner difficulty and uncommon rarity.

The board appears to be the same item published on GitHub by klipper (James Carbine, GitHub handle klipperx) as "UHL-minibadge-2022" under the MIT license. That repository's schematic shows a purely passive circuit — four LEDs, each with its own current-limiting resistor, wired across the power and ground rails supplied through an 8-pad edge connector — so the badge simply lights up when powered, with no microcontroller or interactive behavior. The repo contains only that one schematic image, a short README, and the license file; no full KiCad project, Gerbers, bill of materials, or photos of the assembled board were published. No price, production quantity, or ongoing availability information could be found.

## Make your own

The hardware is partially open: a hand-drawn schematic (drawio export) is published at github.com/klipperx/UHL-minibadge-2022 under the MIT license, but there is no complete PCB design file, Gerbers, or BOM to build directly from.
