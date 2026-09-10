---
title: Professor Plum minibadge (SAINTCON 2018)
id: saintcon-2018-professor-plum-minibadge-saintcon-2018
layout: badge
parent: SAINTCON 2018
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2018
year: 2018
makers:
- name: Professor Plum
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: raw.githubusercontent.com/compukidmike/Saintcon2018/master/Minibadges/Readme.md
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2018/master/Minibadges/Readme.md
  kind: website
images: []
contact: {}
notes:
- Reserved I2C address 0x41 in the official 2018 badge repo's minibadge table; Professor Plum is a known Utah badge maker (later did the BSidesSLC 2019 and SAINTCON 2021 badges) but no separate 2018-specific product page was found. Found by the event-year sweep, task saintcon-2018.
status: rumored
sources:
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2018/master/Minibadges/Readme.md
  title: Professor Plum minibadge (SAINTCON 2018)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2018); event read as ''saintcon-2018''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/Saintcon2018/master/Minibadges/Readme.md
  title: 'compukidmike/Saintcon2018: Minibadges/Readme.md (I2C address table)'
  accessed: '2026-09-10'
  note: 'Confirms the only mention: a table row "Professor Plum | 0x41 | ATTiny" reserving an I2C address and chip family in the 2018 SAINTCON badge''s minibadge spec. No description, image, price, or standalone product listing for this minibadge exists in the doc.'
- kind: url
  url: https://minibadge.wiki/
  title: MiniBadge Wiki
  accessed: '2026-09-10'
  note: 'Community-submitted minibadge wiki; searched for "Professor Plum" and found no matching entry for 2018 or any year.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-10'
  notes: >-
    Could not confirm this minibadge was ever actually produced. The only source is a line
    in the 2018 SAINTCON badge's public minibadge-maker spec (compukidmike/Saintcon2018 repo)
    reserving I2C address 0x41 for a minibadge named "Professor Plum" using an ATTiny chip —
    that table is where makers claimed an address before building, not a record of a finished
    product. No maker post, photo, storefront listing, or entry on the community minibadge.wiki
    site could be found confirming a physical Professor Plum minibadge exists for SAINTCON 2018.
    Professor Plum (compukidmike's collaborator, later ran their own GitHub as Professor-plum)
    is a real and prolific Utah badge maker credited on the BSides SLC 2019 badge, an
    "stm8_minibadges" project, SAINTCON 2021 badge, and a SAINTCON 2022 D6 roller minibadge —
    so the person and general activity are well documented, just not this specific 2018 item.
    Marked status: rumored per the research guide's no-page-confirms-it rule.
last_modified_date: '2026-09-10'
---

An I2C address (0x41) and chip family (ATTiny) reserved under the name "Professor Plum" appear in the public minibadge-maker specification for the 2018 SAINTCON badge (compukidmike/Saintcon2018 repository), alongside similar reservations from other makers that year. That table records addresses claimed for planned minibadges, not necessarily finished, distributed products — no accompanying description, photo, price, or standalone listing for a "Professor Plum" minibadge could be found anywhere else, including the community-run minibadge.wiki archive.

Professor Plum (also credited as Professor-plum) is a well-documented Utah-area badge maker who worked with compukidmike (the 2018 SAINTCON main badge designer) and later produced or contributed to the BSides SLC 2019 badge, an "stm8_minibadges" line, the SAINTCON 2021 badge, and a SAINTCON 2022 D6 roller minibadge. Given that track record, a 2018 minibadge under this name is plausible, but without a confirming page this entry is marked rumored rather than released.

