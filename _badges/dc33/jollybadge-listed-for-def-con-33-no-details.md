---
title: JollyBadge [V2] - DC33 Final Batch
id: dc33-jollybadge-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
series: JollyBadge
makers:
- name: Steve Jabs
  url: https://github.com/stevejabs
  role: maker (Jolly Media Group, LLC)
summary: JollyBadge [V2] is a standalone electronic puzzle badge with eight sequential challenges spanning observational, programming, OSINT, and hardware-hacking skills; the DC33 run raised the difficulty and shipped as "the final batch" of 50 units.
functions: Eight sequential puzzle challenges covering observation, programming/software tooling, OSINT, and hardware hacking; DC33 firmware increases challenge complexity over the original V2 release.
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - ctf
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 50 (final batch)
  availability: sold_out
  distribution:
  - purchase
  where: Sold directly via jollybadge.com; shipped, no in-person pickup orders.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/stevejabs/jollybadge-v2
  eda_tool: null
links:
- kind: website
  label: JollyBadge site
  url: https://jollybadge.com
  archived: https://web.archive.org/web/20260422054154/https://www.jollybadge.com/
- kind: repo
  label: jollybadge-v2 (firmware builds + flashing instructions)
  url: https://github.com/stevejabs/jollybadge-v2
images:
- file: assets/images/badges/dc33/jollybadge-listed-for-def-con-33-no-details/22d1aeb739.jpg
  source: https://jollybadge.com
  credit: Jolly Media Group, LLC
  caption: JollyBadge V2 (DC33 firmware batch) hero photo
  archived: https://web.archive.org/web/20260422054154/https://www.jollybadge.com/
contact: {}
notes:
- The community sheet listed only the maker name "JollyBadge" for DC33 with no other details; retitled after finding the maker's own site and GitHub repo.
- Part of a recurring JollyBadge series; see also dc30-jollybadge, dc31-jolly-roger-listed-for-def-con-31-no-details, and dc32-name-not-released-as-of-yet (also credited to "JollyBadge"/"Jolly Roger").
status: released
sources:
- kind: sheet
  event: dc33
  row: 55
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://jollybadge.com
  title: JollyBadge [V2] - The Final Batch
  accessed: '2026-09-06'
  note: Maker's storefront page; confirms DC33 firmware upgrade, final batch of 50, sold out, free shipping, ships-before-Aug-1 shipping-only terms, and hero photo.
  archived: https://web.archive.org/web/20260422054154/https://www.jollybadge.com/
- kind: url
  url: https://github.com/stevejabs/jollybadge-v2
  title: stevejabs/jollybadge-v2
  accessed: '2026-09-06'
  note: Repo README with flashing instructions confirms USB-C programming interface, UF2 bootloader at first 8 KiB, bossac-based flashing, and multi-color LEDs (freeze in bootloader mode); repo holds compiled firmware builds and docs only, not hardware files or firmware source.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Maker's own site and GitHub repo confirm this is a real, released, sold-out badge (not a stub) and give the puzzle theme, batch size, and firmware/flashing details. Could not confirm exact MCU family, LED count/type, price, PCB color, physical shape, or SAO header presence/absence from any source read -- the repo ships only compiled .bin firmware and a flashing README, no schematic, BOM, or hardware source, so make_your_own.open_source is set to "partial" (firmware binaries and flashing docs public; hardware design and firmware source not published). No press coverage or third-party photos were found in the sources checked.
last_modified_date: '2026-09-06'
---
JollyBadge [V2] is a self-contained electronic puzzle badge built around eight
sequential challenges that test observation, basic programming/tooling, OSINT
research, and hardware-hacking skills. For DEF CON 33 the maker, Steve Jabs of
Jolly Media Group LLC, released a "final batch" of 50 units with the puzzle
difficulty turned up over the earlier V2 release, sold directly through
jollybadge.com with free shipping and no in-person pickup option. The listing
had sold out by the time it was checked.

The badge is field-updatable: it exposes a USB-C port and a recessed reset
button (reachable through a hole in the back enclosure) that drops it into a
UF2 bootloader, at which point new firmware can be flashed with the open-source
`bossac` tool. The maker's GitHub repository (stevejabs/jollybadge-v2) publishes
the compiled DC33 firmware image and detailed cross-platform flashing
instructions, but not hardware design files or firmware source, so it counts
only as partially open. Owners of the earlier V2 badge could upgrade to DC33
firmware once it became available.

JollyBadge is a recurring name/series in the DEF CON badge scene: the archive
already has entries for a DC30 JollyBadge and DC31/DC32 rows crediting "Jolly
Roger" / "JollyBadge" as maker, though none of those record the same DC33
release documented here.
