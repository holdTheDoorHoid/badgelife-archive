---
title: CoD_Segfault (listed for DEF CON 32, no details)
id: dc32-cod-segfault-listed-for-def-con-32-no-details
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: unknown
event: dc32
year: 2024
makers:
- name: CoD_Segfault
  url: https://github.com/CoD-Segfault
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
- kind: repo
  label: GitHub (CoD-Segfault)
  url: https://github.com/CoD-Segfault
- kind: social
  label: X / Twitter (@CoD_Segfault)
  url: https://twitter.com/CoD_Segfault
- kind: social
  label: Bluesky (@se.gfau.lt)
  url: https://bsky.app/profile/se.gfau.lt
images: []
contact: {}
notes: []
status: unknown
sources:
- kind: sheet
  event: dc32
  row: 38
  updated: ''
- kind: url
  url: https://github.com/CoD-Segfault
  title: CoD-Segfault (GitHub profile)
  accessed: '2026-09-06'
  note: Identified the maker's real GitHub identity, bio ("hardware hacker"), pinned repos, and social links (X, Bluesky, Ko-fi). No DEF CON 32 (2024) badge/SAO repo appears among their public repositories.
- kind: url
  url: https://github.com/CoD-Segfault/DefCon27badge
  title: DefCon27badge (CoD-Segfault)
  accessed: '2026-09-06'
  note: Contains only a single firmware image (human.bin, commit "Human badge dump", 2019-08-08) with no README or description -- a raw dump of the *official* DC27 badge, not something they made or sold.
- kind: url
  url: https://github.com/CoD-Segfault/DefCon29Badge
  title: DefCon29Badge (CoD-Segfault)
  accessed: '2026-09-06'
  note: A short SWD firmware-dump writeup (Bus Blaster v2 + OpenOCD/GDB via the Tag-Connect port) plus binaries from the official DC29 badge (SAMD21), not a maker project.
- kind: url
  url: https://github.com/CoD-Segfault/mini_wardriver_rev2
  title: mini_wardriver_rev2 (CoD-Segfault)
  accessed: '2026-09-06'
  note: 'Repo created March 2024 (before DC32 in August 2024), described only as "KiCad files for the mini wardriver rev2" -- the repository itself is empty, so hardware details, price, and any DC32 connection could not be confirmed.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Fact-check 2026-09-07: identity, location, social links, repo dates and the
    empty mini_wardriver_rev2 repo were re-confirmed against GitHub's API and
    the Bluesky public API. Corrected two overstatements: the DC27 repo is a
    bare firmware binary (no writeup), and USBArmyKnife is a fork, not the
    maker's project.
    The community sheet only lists the maker's handle for DEF CON 32 with no
    further detail, and no source found ties a specific badge/SAO to that year.
    Identified the real person behind the handle: a Chicagoland-area hardware
    hacker (GitHub: CoD-Segfault, X/Bluesky: CoD_Segfault / se.gfau.lt) whose
    public work is mostly wardriving hardware (wardriver_rev3, mini_wardriver_rev2)
    and WiFi tooling (wifi-shuriken, BW16-Open-AT), plus firmware dumps of the
    official DEF CON 27 and 29 badges (the DC29 repo documents the SWD process;
    the DC27 repo is just the binary). Their "mini_wardriver_rev2" KiCad repo was created in March
    2024, months before DC32, making it a plausible candidate for what they
    brought, but the repo is empty and no source confirms it was sold, given
    away, or shown at DC32 specifically. Their later, better-documented WiFi Shuriken project (repo created March
    2026) postdates DC32 and is not it; the USBArmyKnife repo on their account is
    a fork of i-am-shodan/USBArmyKnife, not their own project. Left status as
    unknown per the research guide's rule for listed-with-no-details entries
    where the specific item can't be confirmed. A companion stub,
    dc31-i-have-no-idea (same maker, DEF CON 31), is also unresearched but out
    of scope for this task.
last_modified_date: '2026-09-07'
---

The community badge sheet for DEF CON 32 lists only the maker's handle, CoD_Segfault, with no description of what they brought that year. Research turned up the person behind the handle -- a Chicago-area hardware hacker active on GitHub, X, and Bluesky whose public projects center on WiFi/Bluetooth wardriving hardware (the wardriver_rev3 and mini_wardriver_rev2 boards) and related WiFi tooling, alongside firmware dumps of the official DEF CON 27 and 29 badges (the DC29 repo includes a short SWD writeup; the DC27 repo is only the binary).

None of the available sources connect a specific badge or SAO to DEF CON 32 (August 2024) by name. The closest candidate is "mini_wardriver_rev2," a KiCad-files repository the maker created in March 2024, but the repository is empty and nothing confirms it was actually distributed at DC32. Their more prominent later project, WiFi Shuriken, was created well after DC32 and is not it.

This entry is left as an unresearched maker listing: the identity is now known, but what they specifically brought to DEF CON 32 is not confirmed by any source found.
