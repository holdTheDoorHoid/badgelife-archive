---
title: A - Luke (official minibadge)
id: saintcon-2017-a-luke-official-minibadge
layout: badge
parent: Saintcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2017
year: 2017
makers:
- name: lukejenkins
summary: 'One of nine official SAINTCON 2017 minibadges, themed on badge team member Luke Jenkins.'
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
- label: saintcon.gitlab.io/Badge2017/officialminibadge
  url: http://saintcon.gitlab.io/Badge2017/officialminibadge/
  kind: website
- label: lukejenkins/minibadge (minibadge connector standard, GitHub)
  url: https://github.com/lukejenkins/minibadge
  kind: repo
images: []
contact: {}
notes:
- Official SAINTCON 2017 minibadge themed on badge designer Luke Jenkins. Found by the event-year sweep, task saintcon-2017.
status: listed
sources:
- kind: url
  url: http://saintcon.gitlab.io/Badge2017/officialminibadge/
  title: A - Luke (official minibadge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2017); event read as ''saintcon-2017''.'
- kind: url
  url: http://saintcon.gitlab.io/Badge2017/officialminibadge/
  title: Official Mini-badges - SaintCon 2017 Badge
  accessed: '2026-09-10'
  note: 'Confirms "A - Luke" as item 2 of 9 in the official 2017 minibadge list; page is a bare list with no per-item detail, image, price, or quantity.'
- kind: url
  url: https://github.com/lukejenkins/minibadge
  title: lukejenkins/minibadge
  accessed: '2026-09-10'
  note: 'The SAINTCON minibadge connector/protocol standard (v2.0: VBATT, CLK, I2C, PROG pins) linked from the badge site homepage as "Mini Badge Specs"; documents the shared minibadge header used across the 2017 line, not this specific themed design. Open hardware (Eagle/KiCad).'
- kind: url
  url: http://saintcon.gitlab.io/Badge2017/assembly/
  title: Badge Assembly - SaintCon 2017 Badge
  accessed: '2026-09-10'
  note: 'Confirms the 2017 main conference badge (which the minibadges plug into) was built around a Raspberry Pi Zero W, supporting the body text''s mention of that host badge.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: >-
    The only page documenting this item (the maker/badge-team's own SAINTCON 2017 site) is a bare
    numbered list of nine official minibadges ("X - Jupiter", "A - Luke", "HHV - Protoboard", etc.)
    with no per-item detail, image, price, quantity, or maker credit beyond the list itself. This
    confirms the badge is real (part of the documented official 2017 set) rather than a search-snippet
    rumor, but nothing further could be found: no photo, no specific chip/LED/battery info for this
    variant, no price or quantity. The linked "Mini Badge Specs" repo (github.com/lukejenkins/minibadge)
    documents the general minibadge connector standard shared by the whole 2017 line, not this badge's
    own design, so tech fields were left empty rather than guessed. makers.name is kept as
    "lukejenkins" per the sheet, matching the GitHub handle behind the linked spec repo; no separate
    maker page was found confirming they personally designed this specific "A" badge (it may simply be
    named after them by the badge team). No image URL was found for this item.
    Fact-check pass (2026-09-10): re-fetched all three cited sources and confirmed each claim
    they support (item #2 of 9 on the official list; the minibadge repo's connector standard,
    pins, and open-hardware status; the "Mini Badge Specs" link's presence on the site
    homepage). The body's mention of the 2017 host badge being a Raspberry Pi Zero W build was
    previously uncited; added a citation to the site's own Badge Assembly page, which confirms
    it. No unsupported claims or bad images found; nothing removed.
last_modified_date: '2026-09-10'
---

"A - Luke" is the second entry in a numbered list of nine official minibadges distributed at SAINTCON 2017, alongside others named for con features and staff roles ("X - Jupiter," "HHV - Protoboard," "LPV - Lock Pick," "Vault - Key Hole," "Speaker," "TFHT - Alien Head," "Staff - Block S," and "Hackers Challenge"). The list appears on the badge team's own documentation site with no further write-up for any individual item — no photos, pricing, quantities, or per-badge specs are given.

SAINTCON's 2017 minibadges plugged into that year's main conference badge (a Raspberry Pi Zero W build) over a shared minibadge connector standard, documented separately in a GitHub repo by lukejenkins that defines the header's power, clock, I2C, and programming pins. That repo describes the connector shared across the whole minibadge line rather than this specific badge's own circuit or artwork, so no chip, LED, or battery detail could be confirmed for "A - Luke" itself. Whether the badge is literally themed on badge-team member Luke Jenkins, as its title suggests, is not stated outright on the source page.
