---
title: DEFCON 18 Badge Image Editor for Python / Image Writer
id: dc18-defcon-18-badge-image-editor-for-python-image-writer
layout: badge
parent: DC18
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc18
year: 2010
makers:
- name: pflarr / Brad Isbell
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
- label: www.musatcha.com/software/DC18BadgeImageWriter
  url: https://www.musatcha.com/software/DC18BadgeImageWriter/
  kind: website
  archived: https://web.archive.org/web/20260510194420/https://www.musatcha.com/software/DC18BadgeImageWriter/
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- This is a Windows software utility for writing images to a DEFCON 18 badge's LCD, not a badge or SAO itself; kept as a non-item record per research guide.
status: unknown
sources:
- kind: url
  url: https://www.musatcha.com/software/DC18BadgeImageWriter/
  title: DEFCON 18 Badge Image Writer
  accessed: '2026-09-10'
  note: Maker's own page describing the tool, author, purpose, and system requirements.
  archived: https://web.archive.org/web/20260510194420/https://www.musatcha.com/software/DC18BadgeImageWriter/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Not a hardware item. musatcha.com/software/DC18BadgeImageWriter is a small Windows/.NET 2.0 utility (DC18BadgeImageWriter.exe, ~25KB) by Brad Isbell that writes custom images to the LCD of a DEFCON 18 badge over its virtual serial port, using functions built into the stock badge firmware. It is a companion tool for the DC18 badge, not a badge/SAO/accessory in its own right, so no entry fields beyond links/sources were filled.
last_modified_date: '2026-09-10'
---

[DC18BadgeImageWriter](https://www.musatcha.com/software/DC18BadgeImageWriter/) is a small Windows utility by Brad Isbell (musatcha.com) for writing custom images to the LCD screen of the DEFCON 18 (2010) electronic badge. It connects to the badge over a virtual serial port and calls image-display functions already built into the stock DC18 badge firmware, letting owners push their own graphics to the display without modifying the badge's code.

The tool requires Windows and the .NET 2.0 Framework and ships as a single ~25KB executable, `DC18BadgeImageWriter.exe`. Isbell's own description calls it "ugly, and probably buggy, but good enough for now" — a quick utility written to take advantage of the badge's accessible serial interface rather than a polished release.

This is a software accessory for the DEFCON 18 badge rather than a badge, SAO, or other physical item, so it does not fit the archive's item schema; it is retained here only as a record of the tool and its source page.
