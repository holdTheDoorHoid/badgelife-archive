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
  availability: unknown
  distribution:
  - purchase
  where: Sold in person at DEF CON 25; buyers could also reach the maker by email or on Twitter (@dorkengine).
make_your_own:
  open_source: 'yes'
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
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): re-fetched the Hackaday article and confirmed the original shiftj.is post still fails DNS resolution. Verified maker handle "dorkengine" (Hackaday''s own bracket notation, not an artifact), event/year, VoCore2 chip, wifi, USB port, serial console, GPIO, blinkenlights, $40/40-unit price and quantity, and the exact repo URL text ("has the KiCad files and software available" at gitla.in/darkengine/puffy — note the repo path reads "darkengine", not "dorkengine"; both are the same maker per the article, not a separate person). Corrected make_your_own.open_source from "partial" to "yes": the article states the same repo held both the KiCad (hardware) files and the software together, meeting the guide''s bar for "yes"; hardware_url/firmware_url remain empty since the repo itself is dead. Corrected get_one.availability from "sold_out" to "unknown": the cited article is contemporaneous (published as the maker was about to sell at the con) and never states the run actually sold out; no other source was found confirming final sales status. Removed an invented body detail ("roughly inch-square") describing the VoCore2''s size that was not supported by either cited source. Both saved images were confirmed to be from the cited Hackaday article and both show the actual badge. PCB soldermask color, LED count/type, display, battery, and SAO header presence remain unstated in the sources and are correctly left empty.'
last_modified_date: '2026-09-08'
---

The Puffy Badge is an independent hardware badge created by a maker known as dorkengine for DEF CON 25 (2017). Its design riffs on "Puffy," the pufferfish mascot of the OpenBSD project, rendered in soldermask and silkscreen with an exaggerated, stylized pout. Unlike most SAO-style blinky badges of that era, Puffy is built around a VoCore2 — a small Linux-capable system-on-module with WiFi — meaning the badge boots a full Linux userspace rather than running MCU firmware. It exposes a USB port, a serial console, and GPIO pins for further hacking, plus onboard "blinkenlights."

Dorkengine had 40 working PCBs made and planned to sell them for $40 apiece in person at the con, with the VoCore2 module itself costing around $17 to source. The maker made the KiCad design files and software available together in a public repository (gitla.in/darkengine/puffy) at the time, though that repository link no longer resolves as of this research pass, so whether any units remained unsold is unknown.

The community sheet's own source page for this entry (shiftj.is/post/puffy) could not be reached during this research (DNS failure), so the details above are drawn from Hackaday's contemporaneous write-up, which independently corroborates the sweep's one-line description of a fish-shaped, Linux-running badge made in a run of 40.
