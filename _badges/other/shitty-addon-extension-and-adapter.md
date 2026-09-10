---
title: Shitty Addon extension and adapter
id: other-shitty-addon-extension-and-adapter
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: other
year: 2019
makers:
- name: Killergeek
  url: https://hackaday.io/killergeek
summary: A pair of prototype SAO accessories -- an SAO-to-QWIIC adapter and an SAO extension cable -- for testing add-ons and hooking SparkFun QWIIC devices into the shitty-addon ecosystem.
functions: Extends an SAO connection with a cable, or adapts an SAO port to two SparkFun QWIIC (I2C) connectors for prototyping; carries two user-controllable LEDs (red and green).
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: red and green LEDs with 330-ohm resistors, user-controllable
  display: none
  connectivity:
  - i2c
  battery: null
  sao_version: v1.69bis
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/166838-shitty-addon-extension-and-adapter
  url: https://hackaday.io/project/166838-shitty-addon-extension-and-adapter
  kind: hackaday
  archived: https://web.archive.org/web/20260515025030/https://hackaday.io/project/166838-shitty-addon-extension-and-adapter
images:
- file: assets/images/badges/other/shitty-addon-extension-and-adapter/374a1d0e48.jpg
  source: https://hackaday.io/project/166838-shitty-addon-extension-and-adapter
  credit: Killergeek
  caption: 3D CAD render of the SAO extension cable board's connectors (J1/J2), from the project's Hackaday.io log
  archived: https://web.archive.org/web/20260515025030/https://hackaday.io/project/166838-shitty-addon-extension-and-adapter
contact: {}
notes:
- Includes SAO-to-QWIIC adapter.
status: unknown
sources:
- kind: url
  url: https://hackaday.io/project/166838-shitty-addon-extension-and-adapter
  title: Shitty Addon extension and adapter
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
  archived: https://web.archive.org/web/20260515025030/https://hackaday.io/project/166838-shitty-addon-extension-and-adapter
- kind: url
  url: https://hackaday.io/project/166838-shitty-addon-extension-and-adapter
  title: Shitty Addon extension and adapter - Hackaday.io project page
  accessed: '2026-09-07'
  note: Project description, components (SAO to QWIIC adapter with two QWIIC connectors, extension cable with male/female connectors, 6-pin IDC 2.54mm header, JST connectors, two LEDs with 330-ohm resistors), creation date (2019-07-30), and photos.
  archived: https://web.archive.org/web/20260515025030/https://hackaday.io/project/166838-shitty-addon-extension-and-adapter
- kind: url
  url: https://hackaday.io/killergeek
  title: killergeek - Hackaday.io profile
  accessed: '2026-09-07'
  note: Maker identity (student embedded systems engineer, Netherlands); no event/con affiliation given for this project.
  archived: https://web.archive.org/web/20260517091103/https://hackaday.io/Killergeek
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'This is a personal prototyping tool, not a badge made for a specific conference or event -- the maker''s own page ties it to no con, so it stays under "other". No price, quantity, or availability info was published; it reads as a one-off/small-batch prototype (first iteration, maker notes it "needs improvement" before wider release) rather than a sold or distributed item. No hardware/firmware files, BOM, or fab-share links were found on the project page despite logs mentioning schematics and a 3D PCB model. Year (2019) taken from the project''s creation date. Verification pass (2026-09-07): corrected tech.sao_version from v1 to v1.69bis -- a project photo shows the physical board silkscreened "AJG SAO V1.69bis", not v1. Corrected the body, which claimed both boards carry the two LEDs; project photos show the LEDs (and their two 330-ohm resistors, R1/R2) are populated only on the SAO-to-QWIIC adapter board -- the extension board''s photos show bare header pads with no LEDs. Changed
    status from "released" to "unknown": "released" implies others have it, but no source shows this was given away, sold, or used by anyone besides the maker; only a working self-built prototype is confirmed. Corrected the saved image''s caption, which claimed to show "the adapter and extension cable prototypes" -- it is actually a 3D CAD render of only the extension cable''s connector layout, not a photo, and does not show the adapter or the LEDs. All other fields and sentences were checked against the cited Hackaday.io project page, its component/BOM list, and the maker''s profile, and are supported.'
last_modified_date: '2026-09-07'
---

The Shitty Addon extension and adapter is a small pair of prototype accessories made by the Hackaday.io user Killergeek in July 2019 for the SAO ("shitty add-on") ecosystem that badgelife popularized. Rather than being a badge itself, it is a piece of infrastructure: an extension cable that lets an SAO sit further from its host badge, and an adapter that turns an SAO connector into two SparkFun QWIIC ports, so a QWIIC sensor or breakout board can be tested against a badge's add-on header. The SAO-to-QWIIC adapter board carries a red and a green LED (each with its own 330-ohm resistor) that a user can drive directly; the extension board is a plain pass-through with no LEDs.

The maker describes it as a first iteration that still needed refinement, and the project log mentions schematics and a 3D PCB model without publishing downloadable files or a BOM. There is no indication it was sold, given away, or tied to a specific conference; it reads as a personal prototyping aid shared on Hackaday.io rather than a con-distributed item, which is why it remains filed under "other" here.
