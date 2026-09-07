---
title: Galactic Power Badge Kit
id: dc32-galactic-power-badge-kit
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc32
year: 2024
makers:
- name: HackerBoxes
  url: https://hackerboxes.com/
summary: A coin-cell-powered SAO host badge from HackerBox #0104 "Engage" (June 2024), with a full-color PCB, several white LED "stars," and a single SAO header.
functions: Lights several onboard white LED "stars" and supplies power to one plugged-in SAO through its SAO header. No microcontroller of its own.
look:
  colors:
  - multicolor
  shape: null
  themes:
  - space
  - sci-fi
  - kit
  - village badge
tech:
  mcu: none
  leds:
    count: null
    type: null
    note: 'Several white "star" LEDs (a mix of two whitish LED types per the build guide); exact count not stated by the maker.'
  display: none
  connectivity: []
  battery: 2x coin cell (CR-series, exact model not stated)
  sao_version: null
get_one:
  price: $19
  price_usd: 19.0
  quantity: ''
  availability: unknown
  distribution:
  - kit
  - purchase
  where: 'Sold as an add-on kit in the HackerBoxes store (hackerboxes.com), and included as one of several kits inside HackerBox #0104 "Engage," the June 2024 monthly subscription box themed around DEF CON 32 / Hacker Summer Camp. The standalone product page returned a 404 when rechecked on 2026-09-07; it was live and orderable as of a June 2025 archive snapshot at $19 with free domestic shipping.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.instructables.com/HackerBox-0104-Engage/#step6
  url: https://www.instructables.com/HackerBox-0104-Engage/#step6
  kind: website
- label: hackerboxes.com/products/galactic-power-badge-kit
  url: https://hackerboxes.com/products/galactic-power-badge-kit
  kind: store
- label: hackerboxes.com/products/hackerbox-0104-engage
  url: https://hackerboxes.com/products/hackerbox-0104-engage
  kind: store
images:
  - file: assets/images/badges/dc32/galactic-power-badge-kit/8653f4e69f.png
    source: "https://hackerboxes.com/products/galactic-power-badge-kit"
    credit: "HackerBoxes"
    caption: "Galactic Power Badge Kit, assembled, with LED stars lit"
  - file: assets/images/badges/dc32/galactic-power-badge-kit/ccd9a3fcdc.jpg
    source: "https://www.instructables.com/HackerBox-0104-Engage/#step6"
    credit: "HackerBoxes / Instructables"
    caption: "Galactic Power Badge Kit build step, showing coin cell holder, LED stars, and SAO header"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://www.instructables.com/HackerBox-0104-Engage/#step6
  title: Galactic Power Badge Kit
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc32''.'
- kind: url
  url: https://www.instructables.com/HackerBox-0104-Engage/
  title: 'HackerBox 0104: Engage : 10 Steps - Instructables'
  accessed: '2026-09-07'
  note: 'Build-guide step 6 confirms the kit uses a single coin cell to light LED "stars" and power an SAO header; step 1 ties the box to DEF CON 32 / Hacker Summer Camp, June 2024.'
- kind: url
  url: https://hackerboxes.com/products/hackerbox-0104-engage
  title: 'HackerBox #0104 - Engage – HackerBoxes'
  accessed: '2026-09-07'
  note: 'Confirms the Galactic Power Badge Kit shipped as one of several kits (alongside the Alien Robot Badge Kit, Tie-Dye BitHead SAO, Phreakin'' Clowns SAO, All Your Base SAO, and mystery HighRollerCon Quacked-Out SAO kits) in the June 2024 box.'
- kind: url
  url: https://web.archive.org/web/20250620041651/https://hackerboxes.com/products/galactic-power-badge-kit
  title: 'Galactic Power Badge Kit – HackerBoxes (archived)'
  accessed: '2026-09-07'
  note: 'Archived June 2025 snapshot of the live product page: $19, free domestic shipping, "Full Color PCB / Multiple White LED stars / Powers One SAO," included an exclusive Engage-themed lanyard and two coin cells. Current live page (checked 2026-09-07) returns 404, so it may since have been discontinued or delisted as a standalone add-on.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Core facts (price, contents, coin-cell power, single SAO header, LED stars) come from
    HackerBoxes' own product copy (via an archived snapshot, since the live page 404s) and
    the maker's own Instructables build guide, so treated as reliable despite the page being
    gone. Could not confirm: exact LED count/part number, exact coin-cell model (CR2032 vs.
    other), SAO header version (v1 vs v2), quantity made, current availability, or whether
    hardware/firmware files were published (none found; likely a passive/no-firmware kit
    since it has no MCU). "kit" was chosen over "sao"/"badge" because it hosts a SAO rather
    than being one, and is sold/assembled as a build-it-yourself kit. Other kits from the
    same HackerBox #0104 box (Tie-Dye BitHead SAO, Phreakin' Clowns SAO, All Your Base SAO,
    and the HighRollerCon "Quacked-Out" duck SAOs) are not yet in the archive and are
    reported separately; the Alien Robot Badge Kit from the same box already has its own
    entry (dc32-alien-robot-badge).
last_modified_date: '2026-09-07'
---

The Galactic Power Badge Kit is a small SAO-hosting board that HackerBoxes included in HackerBox #0104, "Engage" — their monthly subscription box for June 2024, themed around Hacker Summer Camp and DEF CON 32 in Las Vegas. Unlike the box's other headline kit, the microcontroller-driven Alien Robot Badge, the Galactic Power Badge has no chip of its own: it runs on two coin cells, lights a handful of white "star" LEDs, and exists mainly to supply power to a single Simple Add-On plugged into its header. It shipped with an exclusive "Engage"-themed lanyard.

HackerBoxes sold it both bundled into the box and as a standalone $19 add-on kit with free domestic shipping, alongside three other SAOs from the same box (Tie-Dye BitHead, Phreakin' Clowns, and All Your Base) and a set of mystery "Quacked-Out" duck SAOs tied to that August's HighRollerCon party. The standalone product listing was still live and orderable as of a June 2025 web archive snapshot; the same URL returns a 404 as of this research pass, so it appears to have since been pulled from the current storefront.
