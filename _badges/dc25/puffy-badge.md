---
title: Puffy Badge
id: dc25-puffy-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: dorkengine
summary: A pufferfish-shaped independent badge for DEF CON 25 that boots real Linux on an embedded VoCore2 module, styled after the OpenBSD "Puffy" mascot.
functions: Boots Linux on the onboard VoCore2 SoC; exposes a USB port, serial console, and GPIO pins for tinkering; connects over WiFi; has onboard "blinkenlights."
look:
  colors: []
  shape: fish
  themes:
  - animal
  - security
  - hardware tool
tech:
  mcu: VoCore2
  leds: null
  display: none
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: $40
  price_usd: 40
  quantity: '40'
  availability: sold_out
  distribution:
  - purchase
  where: Sold in person at DEF CON 25; buyers could also reach the maker by email or on Twitter (@dorkengine).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: shiftj.is/post/puffy
  url: https://shiftj.is/post/puffy/
  kind: website
- label: 'Hackaday: DEF CON Badgelife: The Puffy That Runs Linux'
  url: https://hackaday.com/2017/07/07/def-con-badgelife-the-puffy-that-runs-linux/
  kind: article
images:
  - file: assets/images/badges/dc25/puffy-badge/61240e5736.jpg
    source: "https://hackaday.com/2017/07/07/def-con-badgelife-the-puffy-that-runs-linux/"
    credit: "dorkengine / Hackaday"
    caption: "Puffy badge PCB with OpenBSD pufferfish artwork"
  - file: assets/images/badges/dc25/puffy-badge/86424b630c.jpg
    source: "https://hackaday.com/2017/07/07/def-con-badgelife-the-puffy-that-runs-linux/"
    credit: "dorkengine / Hackaday"
    caption: "Puffy badge header photo"
contact: {}
notes:
- Fish-shaped Linux-running badge (40 units, router-chipset SoC) shown at DEF CON 25. Found by the event-year sweep, task dc25-saos.
- The sweep's source page (shiftj.is/post/puffy) did not resolve during research (DNS failure); details below come from Hackaday's contemporaneous coverage instead, which corroborates the sweep's one-line summary.
status: released
sources:
- kind: url
  url: https://shiftj.is/post/puffy/
  title: Puffy Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc25-saos); event read as ''dc25''.'
- kind: url
  url: https://hackaday.com/2017/07/07/def-con-badgelife-the-puffy-that-runs-linux/
  title: 'DEF CON Badgelife: The Puffy That Runs Linux'
  accessed: '2026-09-08'
  note: Primary source for maker, event, chip, price, quantity, connectivity, and repo link.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via Hackaday''s 2017 coverage rather than the original shiftj.is post, which no longer resolves (DNS failure at time of research). Maker is credited only by the handle "dorkengine" (also seen as Twitter @dorkengine); no real name or personal site found. The KiCad/software repo the article links to (gitla.in/darkengine/puffy) also does not resolve today, so hardware_url/firmware_url are left empty rather than pointing to a dead link; open_source is marked "partial" on the article''s word alone. PCB soldermask color, LED count, and SAO header presence are not stated in the source and are left empty. Price/quantity are the maker''s stated plan ($40 each, 40 boards) at time of the DEF CON 25 con; not confirmed whether all sold.'
last_modified_date: '2026-09-08'
---

The Puffy Badge is an independent hardware badge created by a maker known as dorkengine for DEF CON 25 (2017). Its design riffs on "Puffy," the pufferfish mascot of the OpenBSD project, rendered in soldermask and silkscreen with an exaggerated, stylized pout. Unlike most SAO-style blinky badges of that era, Puffy is built around a VoCore2 — a roughly inch-square Linux-capable system-on-module with WiFi — meaning the badge boots a full Linux userspace rather than running MCU firmware. It exposes a USB port, a serial console, and GPIO pins for further hacking, plus onboard "blinkenlights."

Dorkengine had 40 working PCBs made and planned to sell them for $40 apiece in person at the con, with the VoCore2 module itself costing around $17 to source. The maker made the KiCad design files and software available in a public repository at the time, though that repository link no longer resolves as of this research pass.

The community sheet's own source page for this entry (shiftj.is/post/puffy) could not be reached during this research (DNS failure), so the details above are drawn from Hackaday's contemporaneous write-up, which independently corroborates the sweep's one-line description of a fish-shaped, Linux-running badge made in a run of 40.
