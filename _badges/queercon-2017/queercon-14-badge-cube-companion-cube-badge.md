---
title: Queercon 14 Badge ("The Cube")
id: queercon-2017-queercon-14-badge-cube-companion-cube-badge
layout: badge
parent: Queercon 14 (2017)
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: queercon-2017
year: 2017
makers:
- name: George Louthan (duplico)
  url: https://github.com/duplico
- name: Evan Mackay
- name: Jonathan Nelson
  role: UI/UX designer
summary: A modular square electronic badge for Queercon 14 (DEF CON 25, 2017), nicknamed "The Cube," built around an ARM-based BLE SoC with a 7x7 matrix of 73 RGB LEDs and hermaphroditic edge connectors that let badges snap together into panels and 3D cube structures.
functions: Runs an Alchemy-style crafting game where players combine basic elements (air, fire, water, earth) into new ones by linking badges through their edge connectors, with a Bluetooth Low Energy link syncing progress to a shared display. A limited run of ten Starbucks-sponsored badges added a fifth "coffee" element.
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - ctf
  - wearable
tech:
  mcu: TI CC2650 (BLE SoC, ARM Cortex-M3)
  leds:
    count: 73
    type: RGB
    note: 0604-size RGB LEDs in a 7x7 matrix, driven via a TI LED driver chip with two shift registers and 15 FETs managing LED commons.
  display: LED matrix 7x7
  connectivity:
  - ble
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to Queercon attendees at DEF CON 25; demand outstripped supply after a 200% jump in attendance, so not everyone who wanted one received one.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/duplico/qc14
  firmware_url: https://github.com/duplico/qc14
  eda_tool: null
links:
- label: hackaday.com/2017/08/07/inside-this-years-queercon-badge
  url: https://hackaday.com/2017/08/07/inside-this-years-queercon-badge/
  kind: article
- label: github.com/duplico/qc14
  url: https://github.com/duplico/qc14
  kind: repo
images:
- file: assets/images/badges/queercon-2017/queercon-14-badge-cube-companion-cube-badge/9038abd137.jpg
  source: https://hackaday.com/2017/08/07/inside-this-years-queercon-badge/
  credit: Hackaday
  caption: A single 2017 Queercon 14 badge (The Cube)
- file: assets/images/badges/queercon-2017/queercon-14-badge-cube-companion-cube-badge/e1994074e1.jpg
  source: https://hackaday.com/2017/08/07/inside-this-years-queercon-badge/
  credit: Hackaday
  caption: Close-up of the badge's hermaphroditic edge connector
- file: assets/images/badges/queercon-2017/queercon-14-badge-cube-companion-cube-badge/b0c96f0c8d.jpg
  source: https://hackaday.com/2017/08/07/inside-this-years-queercon-badge/
  credit: Hackaday
  caption: Queercon 14 badges linked into a panel via their edge connectors
- file: assets/images/badges/queercon-2017/queercon-14-badge-cube-companion-cube-badge/9038abd137.jpg
  source: https://hackaday.com/2017/08/07/inside-this-years-queercon-badge/
  credit: Hackaday
  caption: A single 2017 Queercon 14 badge
contact: {}
notes:
- Modular cube-shaped badge with 73 tiny RGB LEDs, a 7x7 RGB matrix, an ARM Cortex-M3, hermaphroditic edge connectors letting badges interlock into 3D structures, and an Alchemy-style crafting game; a Starbucks-sponsored variant added a "coffee" element. Found by the event-year sweep, task queercon.
- The sweep's title called this the "cube/Companion Cube badge"; the maker's own GitHub repo names the project simply "The Cube" (a reference to the badge's interlocking cube geometry, not to Portal's Companion Cube). Retitled to match the maker's usage.
- 'DEF CON 25''s Queercon badge: ARM Cortex-M3, 73 RGB LEDs, hermaphroditic edge connectors letting badges combine into panels/cubes, plus an on-badge ''Alchemy'' game and crypto challenge. Found by the event-year sweep, task dc25-badges.'
status: released
sources:
- kind: url
  url: https://hackaday.com/2017/08/07/inside-this-years-queercon-badge/
  title: Queercon 14 badge (cube/Companion Cube badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:queercon); event read as ''queercon-2017''.'
- kind: url
  url: https://github.com/duplico/qc14
  title: 'duplico/qc14: Queercon 14 electronic badge, "The Cube"'
  accessed: '2026-09-08'
  note: Maker's own repo; confirms creator (George Louthan / duplico), BLE connectivity, open-source hardware (CC BY-SA 4.0) and firmware (BSD 3-clause), and the badge's real name.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: This entry duplicates queercon-2017-queercon-14-badge, an existing entry for the same physical badge (same Hackaday article, same maker team, same specs). Price and exact quantity produced were not stated by any source found and are left blank. EDA tool used for the PCB was not stated in the repo (only a CCS/TI firmware workspace and schematic PDFs were found, no explicit KiCad/Eagle/Altium mention). Merged with duplicate entry 'Queercon 14 Badge' (queercon-2017-queercon-14-badge).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/queercon-2017/queercon-14-badge/
---

Queercon 14's badge for DEF CON 25 (2017) was a square, modular electronic badge that the design team calls "The Cube," built around a TI CC2650 Bluetooth Low Energy SoC (an ARM Cortex-M3-based chip). Its face carries a 7x7 matrix of 73 tiny RGB LEDs driven through a TI LED driver chip, two shift registers, and 15 FETs. Hermaphroditic edge connectors on all four sides let badges plug into one another and rotate through 180 degrees, so a crowd of attendees could link their badges into flat panels or three-dimensional cube structures.

The badge ran an Alchemy-inspired crafting game: players combined base elements — air, fire, water, and earth — by connecting badges, discovering new elements such as "beer" (water plus fire) along the way. A Bluetooth Low Energy link let the badges sync progress to a shared display. Ten specially sponsored badges added a fifth element, "coffee," tied to a Starbucks promotion. Demand for badges outpaced supply that year, since attendance grew roughly 200% and not everyone who wanted a badge received one; the team reported a 0.7% fabrication failure rate on the units that were built.

The hardware design (CC BY-SA 4.0) and firmware (BSD 3-clause) are published on GitHub by lead designer George Louthan, alongside contributions credited to Evan Mackay and UI/UX designer Jonathan Nelson.

## Make your own

Schematics, a designator guide, MCU pinout notes, and the TI Code Composer Studio firmware workspace (including the TI BLE SDK it builds against) are in the maker's repository at github.com/duplico/qc14.

## Notes merged from the duplicate entry "Queercon 14 Badge"

Queercon 14 was the badge given to attendees of Queercon at DEF CON 25 in 2017. It runs on an ARM Cortex-M3 and lights 73 individually addressable RGB LEDs, including a 7x7 matrix used to display pixel-art graphics. Hermaphroditic edge connectors on all four sides let two badges join at any 90-degree rotation, so a crowd of them could be snapped together into panels, cubes, and other 3D structures.

On top of the light show, the badge ran an Alchemy-style crafting game where wearers combined base elements (air, fire, water, earth) to unlock new ones, plus a cryptographic challenge tied to arranging badges into cube formations. A limited batch of ten badges carried a Starbucks-sponsored "coffee" element as an extra. Hackaday's writeup noted a 0.7% badge failure rate and roughly 200% growth in demand over the prior year's badge, but did not report a price, total production quantity, or whether hardware/firmware files were released.
