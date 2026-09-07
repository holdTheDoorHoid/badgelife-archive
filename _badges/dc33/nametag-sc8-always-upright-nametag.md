---
title: Nametag SC8 - Always Upright Nametag
id: dc33-nametag-sc8-always-upright-nametag
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: trueControl
  url: https://basic.truecontrol.org
summary: A GAT-standard SAO nametag whose name text stays upright no matter how the badge is oriented, with a ring of 12 addressable RGB LEDs for animations.
functions: A nametag where the letters are always upright (with optional waving/wiggling/static display modes). Programmable RGB border animations via 12 RGB LEDs. Planned (not fully working) IR message syncing between units, USB for power/data/firmware updates, and on-board menu navigation via recessed buttons.
look:
  colors: []
  shape: null
  themes:
  - text
  - wearable
tech:
  mcu: CH592
  leds:
    count: 12
    type: RGB
    note: Driven by an Awinic AW20054 RGB LED controller.
  display: OLED
  connectivity:
  - ir
  - usb
  battery: USB-powered
  sao_version: null
get_one:
  price: '40'
  price_usd: 40.0
  quantity: about 70-80 units
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://git.trueserve.org/trueControl/sc8-nametag
  firmware_url: https://git.trueserve.org/trueControl/sc8-nametag
  eda_tool: null
links:
- label: basic.truecontrol.org
  url: https://basic.truecontrol.org
  kind: website
- label: hackaday.io/project/198536-gat-nametag-sc8
  url: https://hackaday.io/project/198536-gat-nametag-sc8
  kind: hackaday
- label: basic.truecontrol.org/database/sc8/nametag
  url: https://basic.truecontrol.org/database/sc8/nametag/
  kind: website
- label: git.trueserve.org/trueControl/sc8-nametag.git
  url: https://git.trueserve.org/trueControl/sc8-nametag.git
  kind: repo
- label: hackaday.io/project/198536/files
  url: https://hackaday.io/project/198536/files
  kind: hackaday
images:
- file: assets/images/badges/dc33/nametag-sc8-always-upright-nametag/b3ce3434a9.jpg
  source: "https://hackaday.io/project/198536-gat-nametag-sc8"
  credit: "trueControl (true)"
  caption: "GAT Nametag SC8 main project image"
- file: assets/images/badges/dc33/nametag-sc8-always-upright-nametag/5abe6ce4a3.jpg
  source: "https://hackaday.io/project/198536-gat-nametag-sc8"
  credit: "trueControl (true)"
  caption: "GAT Nametag SC8 hardware detail photo"
contact:
  emails:
  - true_dc33list@trueserve.org
notes: []
status: released
sources:
- kind: sheet
  event: dc33
  row: 28
  updated: 7/15/2025 22:14:54
- kind: url
  url: https://hackaday.io/project/198536-gat-nametag-sc8
  title: "GAT Nametag SC8 - Hackaday.io"
  accessed: '2026-09-06'
  note: "Project description, maker (trueControl/true), MCU, LEDs, features, images."
- kind: url
  url: https://basic.truecontrol.org/database/sc8/nametag/
  title: "About true's Nametag SC8 - trueControl BASIC"
  accessed: '2026-09-06'
  note: "Full spec sheet (MCU, sub-MCU, LED driver, IrDA module), feature list, and confirmation the addon was made for Hackaday Supercon 8 (2024)."
- kind: url
  url: https://basic.truecontrol.org
  title: "trueControl BASIC (site index)"
  accessed: '2026-09-06'
  note: "Site navigation confirms the GAT Nametag SC8 is filed under 'Hackaday Supercon > Supercon 8 (2024)', not under any DC33 project listing; trueControl's separate DC33 project is 'Retro Tech DC33 Addon'."
- kind: url
  url: https://git.trueserve.org/trueControl/sc8-nametag
  title: "trueControl/sc8-nametag - trueserve Git"
  accessed: '2026-09-06'
  note: "Confirms open hardware+firmware repo ('Firmware for true's GAT Nametag, released at Supercon 8'), includes a hardware/ folder (KiCad-style project files) and firmware, with a licenses.txt."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    Important discrepancy: this item was designed for and released at Hackaday
    Supercon 8 (November 2024), not DEF CON 33. The maker's own site
    (basic.truecontrol.org) files it exclusively under "Hackaday Supercon >
    Supercon 8 (2024)"; their DC33 (2025) project listed separately on the same
    site is an unrelated addon called "Retro Tech DC33 Addon." It appears on
    the DC33 community badge sheet likely because the maker (or someone else)
    wore/brought this SAO to DEF CON 33 as well, but no DC33-specific source
    was found. Left event as dc33 per the archive's stub/file location since
    moving entries between events is out of scope for this pass; flagging for a
    maintainer to consider whether it should be re-homed under a "sc8" event
    or cross-referenced. Price of $40 and battery type carried over from the
    original sheet import were not independently confirmed by any source found
    (no store/preorder page was located); price left as-is since it is
    plausible but unverified, and could not find a definitive battery
    chemistry/capacity (device appears USB-powered per the maker's usage
    notes, so `battery` is left as "USB-powered" rather than invented).
    Availability, quantity precision, and whether any units remain
    unclaimed/for sale could not be determined - no storefront or auction
    listing was found.
last_modified_date: '2026-09-06'
---

The Nametag SC8 is a SAO-style badge addon built to the GAT ("Generic Addon Type") standard by the maker trueControl (going by "true"), designed and rushed to fabrication in about four and a half days for Hackaday Supercon 8 in November 2024. Its core trick is an accelerometer-driven display that keeps your printed name upright and readable no matter which way the badge (or you) is oriented, with optional wiggling, waving, or static rendering modes shown on a small OLED screen. A ring of 12 addressable RGB LEDs, driven by an Awinic AW20054 controller, adds programmable animations around the nametag.

Under the hood it runs a WCH CH592 BLE-capable MCU (448K flash / 26K SRAM) paired with a smaller CH32V003 co-processor, plus a Zilog IrDA transceiver intended for future badge-to-badge messaging. At the time of the maker's write-up, IR linking and BLE features were implemented but untested, and a scrolling-name mode was still on the wishlist. The addon can be powered and reprogrammed over USB.

Both hardware (schematics/PCB files) and firmware are published in a public git repository (git.trueserve.org/trueControl/sc8-nametag) alongside a Hackaday.io project page with build photos. The entry's presence on the DEF CON 33 community badge sheet appears to reflect the maker (or an attendee) bringing this Supercon 8 addon to DC33 as well - the item itself was not designed for or first released at DEF CON, and the maker's own site lists a separate, different addon ("Retro Tech DC33 Addon") as their DC33-specific project.

## Make your own

Hardware and firmware source are both available:

- `git clone https://git.trueserve.org/trueControl/sc8-nametag.git`
- The repo includes a `hardware/` directory with the PCB design files and a `licenses.txt` covering the project's licensing.
- Pre-built firmware images were noted by the maker as "available later" at time of writing; check the repo for current release artifacts.
