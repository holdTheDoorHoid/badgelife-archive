---
title: SAO Bridge
id: supercon-2024-sao-bridge
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2024
year: 2024
makers:
- name: astuder
  url: https://github.com/astuder
summary: A bridge PCB adapter for the Hackaday Supercon 8 Add-On Badge that spans the empty center of the badge to add a seventh SAO slot there while also rotating the left and right SAO slots into an upright orientation; open hardware under CERN-OHL-P-2.0.
functions: Adds a center SAO slot wired to power and I2C from the badge's left-side bus (slot 2), and re-orients the badge's existing left and right SAO slots to sit upright instead of sideways.
look:
  colors:
  - green
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - i2c
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
  open_source: true
  hardware_url: https://github.com/astuder/supercon8-sao-adapters/tree/main/sao-bridge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/astuder/supercon8-sao-adapters
  url: https://github.com/astuder/supercon8-sao-adapters
  kind: repo
  archived: https://web.archive.org/web/20260222141231/https://github.com/astuder/supercon8-sao-adapters
- label: github.com/astuder/supercon8-sao-adapters/tree/main/sao-bridge
  url: https://github.com/astuder/supercon8-sao-adapters/tree/main/sao-bridge
  kind: repo
- label: github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  url: https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  kind: repo
images:
- file: assets/images/badges/supercon-2024/sao-bridge/5938ba1915.jpg
  source: https://github.com/astuder/supercon8-sao-adapters
  credit: astuder
  caption: SAO Bridge adapter mounted on a Hackaday Supercon 8 Add-On Badge
  archived: https://web.archive.org/web/20260222141231/https://github.com/astuder/supercon8-sao-adapters
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/astuder/supercon8-sao-adapters
  title: astuder/supercon8-sao-adapters - Adapters for the Hackaday Supercon 8 SAO Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260222141231/https://github.com/astuder/supercon8-sao-adapters
- kind: url
  url: https://github.com/astuder/supercon8-sao-adapters
  title: astuder/supercon8-sao-adapters README
  accessed: '2026-09-07'
  note: Confirmed function (center SAO slot wired to slot 2's power/I2C bus, rotates left/right slots upright), green PCB color (chosen for JLCPCB turnaround time over the maker's preferred black), CERN-OHL-P license, and the list of SAOs shown mounted on the demo badge (duckGLOW, Hack-Man, Featuring You!, Yo Dawg, Infinity Mirror, Wolverine).
  archived: https://web.archive.org/web/20260222141231/https://github.com/astuder/supercon8-sao-adapters
- kind: url
  url: https://raw.githubusercontent.com/astuder/supercon8-sao-adapters/main/img/s8-sao-bridge.jpg
  title: s8-sao-bridge.jpg
  accessed: '2026-09-07'
  note: Photo of the assembled adapter on a Supercon 8 badge, saved to images.
  archived: https://web.archive.org/web/20260222141233/https://raw.githubusercontent.com/astuder/supercon8-sao-adapters/main/img/s8-sao-bridge.jpg
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own repo confirms design, function, and license. Not offered for sale (no store link, no price/quantity found) -- appears to be a personal/DIY open-hardware project shared for others to fabricate themselves, so get_one fields are left empty and status is set to released (design published, boards fabricated and shown assembled) rather than listed. No chip, LEDs, or display -- it is a passive bridge/adapter board, not an SAO itself.
last_modified_date: '2026-09-07'
---

The SAO Bridge is a small PCB adapter by GitHub user astuder for the Hackaday Supercon 8 Add-On Badge, the official badge for Supercon 2024. The stock Supercon 8 badge has two SAO slots on its left and right edges, oriented sideways, with unused space in the middle. The bridge spans that center gap, adding a seventh SAO connector there wired to the power and I2C lines of the badge's slot 2 bus, and doubles as a mechanical adapter that rotates the existing left and right slots into an upright orientation.

Boards were fabricated in green rather than the maker's preferred black, chosen because it offered the fastest turnaround at JLCPCB ahead of the October 2024 event. Photos from the repository show one assembled on a badge carrying six SAOs at once (duckGLOW, Hack-Man, Featuring You!, Yo Dawg, Infinity Mirror, and Wolverine), demonstrating the extra slot in use.

## Make your own

The design is open hardware, released under CERN-OHL-P-2.0, with KiCad schematic and PCB files published in the `sao-bridge` folder of the `astuder/supercon8-sao-adapters` repository. The maker explicitly invites others to duplicate, adapt, or reuse the design. No indication was found that finished boards were sold or distributed as kits -- this appears to be a share-the-files project rather than a product, so `get_one` fields are left blank.
