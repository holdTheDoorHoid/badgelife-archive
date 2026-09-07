---
title: Arc Badge
id: dc27-arc-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/twinkletwinkie
- name: Wire (@wireengineer)
  url: https://github.com/Wireb
  role: software and bulk of the KiCad hardware design
summary: An Infinity War-era Arc Reactor badge/prop made as a DEF CON 27 indie badge by TwinkleTwinkie (hardware, assembly) with Wire/@wireengineer (software, KiCad), built around a PIC16F15344 with RGB LEDs under an FR4 diffuser layer, two SAO connectors and 2xAA power through a boost converter; roughly 200 were sold on Tindie at $90 plus 20 kept for donation/trading, each shipped with the Iron Gauntlet SAO, a red lanyard and batteries.
functions: 30 selectable color/animation modes (modes 0-29 per the published firmware; default "classic blue" arc-reactor look plus other colors and animated patterns), selected with a mode button that remembers the last-used display across power cycles; on/off toggle switch.
look:
  colors:
  - red
  - blue
  shape: triangle
  themes:
  - sci-fi
  - movie
  - cyberpunk
  - wearable
tech:
  mcu: PIC16F15344
  leds:
    count: null
    type: 3528 RGB (non-addressable, overvolted to 5V)
    note: Programmed in assembly; creator has said a redesign would use 5050 addressable RGB LEDs instead.
  display: none
  connectivity: []
  battery: 2xAA
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: $90 + $10 USPS Priority shipping
  price_usd: 90
  quantity: ~200 for sale, plus 20 kept for donation/trading
  availability: sold_out
  availability_note: 'Tindie listing checked 2026-09-07: ''This product is no longer available for sale.'''
  distribution:
  - purchase
  where: Sold exclusively on TwinkleTwinkie's Tindie store; reportedly also available at Hacker Warehouse during DEF CON 27. Each unit shipped with the exclusive Iron Gauntlet SAO, a red lanyard, and batteries.
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
  firmware_url: https://github.com/Wireb/TwinkleTwinkie_Arc_badge
  eda_tool: KiCad
links:
- label: hackaday.io/project/165320-arc-badge-dc27-indie-badge
  url: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260523064150/https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
- label: www.tindie.com/stores/twinkletwinkie
  url: https://www.tindie.com/stores/twinkletwinkie/
  kind: store
  archived: https://web.archive.org/web/20260503111119/https://www.tindie.com/stores/twinkletwinkie/
- label: 'Tindie product listing: Arc Badge - DC27 Indie Badge'
  url: https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
  kind: store
  archived: https://web.archive.org/web/20260510025611/https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
- label: 'GitHub: Wireb/TwinkleTwinkie_Arc_badge (firmware)'
  url: https://github.com/Wireb/TwinkleTwinkie_Arc_badge
  kind: repo
- label: 'Hackaday.io build log: Arc Badge Part 1'
  url: https://hackaday.io/page/6518-arc-badge-part-1-biting-off-more-than-you-can-chew
  kind: doc
  archived: https://web.archive.org/web/20260309033027/https://hackaday.io/page/6518-arc-badge-part-1-biting-off-more-than-you-can-chew
- label: 'Hackaday.com: Pictorial Guide to the Unofficial Electronic Badges of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
images:
- file: assets/images/badges/dc27/arc-badge/28fe7d1534.jpg
  source: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
  credit: TwinkleTwinkie
  caption: Arc Badge project cover photo showing the illuminated arc reactor badge
  archived: https://web.archive.org/web/20260523064150/https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
- file: assets/images/badges/dc27/arc-badge/f28cdfee64.jpg
  source: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
  credit: TwinkleTwinkie
  caption: Arc Badge gallery photo showing the assembled badge with LED lighting
  archived: https://web.archive.org/web/20260523064150/https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
  title: Arc Badge - DC27 Indie Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260523064150/https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
  title: Arc Badge - DC27 Indie Badge (Tindie product listing)
  accessed: '2026-09-07'
  note: Confirmed price ($90), that it shipped with the Iron Gauntlet SAO and a red lanyard, the sold-out status, the two SAOv169bis connectors, on/off switch, and 30 display modes claim (vs. 32 elsewhere).
  archived: https://web.archive.org/web/20260510025611/https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
- kind: url
  url: https://hackaday.io/page/6518-arc-badge-part-1-biting-off-more-than-you-can-chew
  title: 'Arc Badge - Part 1: Biting off more than you can chew.'
  accessed: '2026-09-07'
  note: Confirmed triangle shape with two 'ear' SAO mounts, three-layer construction (art board / 3D-printed spacer / electronics board), ~260 spacers printed.
  archived: https://web.archive.org/web/20260309033027/https://hackaday.io/page/6518-arc-badge-part-1-biting-off-more-than-you-can-chew
- kind: url
  url: https://github.com/Wireb/TwinkleTwinkie_Arc_badge
  title: Wireb/TwinkleTwinkie_Arc_badge (GitHub)
  accessed: '2026-09-07'
  note: Confirmed firmware is published (PIC16F15344, PicKit 4 programming) and credited Wire's KiCad hardware work.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass (2026-09-07) corrected two errors from the prior draft.
    "Hot-glue diffuser" was unsupported; Hackaday.com actually describes
    0.8mm FR4 as the diffuser, and the build log does not mention a diffuser
    material at all. The mode count was listed as 32, but the two most
    authoritative sources (the published GitHub firmware, whose code covers
    modes 0 through 0x1D, i.e. 30 modes, and the maker's own Tindie listing)
    both say 30; only the Hackaday.com press write-up says 32. Both fields
    are now fixed to match the firmware and storefront. Quantity is hedged
    as "~200 for sale, plus 20" per the maker's own stated goal on
    Hackaday.io ("I'm aiming for 200 to sell and 20 for donations and
    trading, final numbers will depend on final yield"); Hackaday.com press
    coverage separately claims 248 were produced as a final count, which
    cannot be confirmed against a maker source, so the maker's stated
    target is kept and the discrepancy is flagged here rather than in the
    summary. LED count still not stated anywhere found (only LED type and
    size, 3528 non-addressable); tech.leds.count left empty. Checked the
    GitHub repo directly via the GitHub API, which confirms it has no
    LICENSE file, so make_your_own.license is correctly left empty. The
    Hackaday.io project page does list downloadable Gerber and BOM/parts
    list files, but only as attachments within the project page itself,
    with no distinct URL beyond hardware_url to point gerbers_url or
    bom_url at, so those stay empty rather than inventing a link. The
    Tindie store page (https://www.tindie.com/stores/twinkletwinkie/)
    returned 403 to automated fetch; the individual product page worked
    fine. All other non-empty fields and sentences were checked against
    their cited sources and confirmed.
last_modified_date: '2026-09-07'
---

The Arc Badge was an unofficial "indie" badge sold for DEF CON 27 (2019) by TwinkleTwinkie, reimagining Iron Man's Mk85 Nano Suit arc reactor as a wearable electronic prop. TwinkleTwinkie handled hardware sourcing and assembly while Wire (@wireengineer) wrote the firmware and did most of the KiCad layout. The badge is built as three stacked layers — a translucent "art" board on top, a 3D-printed spacer in the middle, and the electronics board underneath — with a triangular outline and two raised "ears" carrying a pair of SAOv1.69bis (6-pin) add-on headers. A PIC16F15344 microcontroller drives non-addressable 3528 RGB LEDs, overvolted to 5V for brightness, through roughly 30 selectable color and animation modes, defaulting to the reactor's familiar blue glow; a mode button remembers the last setting across power cycles, and the badge runs off two AA batteries.

TwinkleTwinkie sold about 200 units exclusively through their Tindie store at $90 plus shipping, with an additional 20 units set aside for donations and trades; the listing is now marked as no longer available. Each purchase included an exclusive Iron Gauntlet SAO, a red lanyard, and batteries, and the badge reportedly could also be picked up in person at Hacker Warehouse during the con. Both the firmware (published on GitHub) and the hardware design work are documented publicly, making it one of the more thoroughly open-sourced indie badges of that year's DEF CON.
