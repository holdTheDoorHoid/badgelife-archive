---
title: Minirack Minibadge Display
id: saintcon-2026-minirack-minibadge-display
layout: badge
parent: Saintcon 2026
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: saintcon-2026
year: 2026
makers:
- name: Herushan
  url: https://github.com/Herushan
summary: An unofficial 4x4 minibadge display board that holds sixteen SAO-style minibadges and can be daisy-chained to other display boards over a repurposed Ethernet (RJ45) connector for shared power and I2C.
functions: Holds 16 minibadges in 8-pin headers arranged in a 4x4 grid; front-panel LEDs (including a small "clock" LED circuit built from Schmitt-trigger inverters) light up when powered; can be powered stand-alone over USB-C or chained to other boards over the MDNC RJ45 link so only one board in a chain needs its own USB-C connection.
look:
  colors:
  - white
  - black
  shape: rectangle
  themes:
  - minibadge
  - kit
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: '8x orange 0805 LEDs plus a small red/green "clock" indicator pair driven by 74AHC1G14GW Schmitt-trigger inverter ICs; no microcontroller'
  display: none
  connectivity:
  - i2c
  - usb
  battery: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Not sold; a DIY board the maker documents with a parts list and an assembly video. Featured in SAINTCON 2026''s community YouTube playlist.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Herushan/4x4minibadgedisplay
  firmware_url: null
  eda_tool: null
links:
- label: github.com/Herushan/MDNC---Unofficial_minibadge_display_rj45port
  url: https://github.com/Herushan/MDNC---Unofficial_minibadge_display_rj45port
  kind: repo
- label: www.youtube.com/watch?v=Lw8Jp5DrFOU
  url: https://www.youtube.com/watch?v=Lw8Jp5DrFOU
  kind: video
- label: github.com/Herushan/4x4minibadgedisplay
  url: https://github.com/Herushan/4x4minibadgedisplay
  kind: repo
images:
  - file: assets/images/badges/saintcon-2026/minirack-minibadge-display/d35970f48c.jpg
    source: "https://github.com/Herushan/4x4minibadgedisplay"
    credit: "Herushan"
    caption: "Assembled 4x4 minibadge display board (special DC801 version), front"
  - file: assets/images/badges/saintcon-2026/minirack-minibadge-display/ba96c41c38.jpg
    source: "https://github.com/Herushan/4x4minibadgedisplay"
    credit: "Herushan"
    caption: "Assembled 4x4 minibadge display board (special DC801 version), back with MDNC RJ-45 port"
contact: {}
notes:
- 'Sweep found this only via a search snippet naming the YouTube video "2026 Minirack Minibadge Display Assembly"; confirmed real by finding that video in the official SAINTCON 2026 YouTube playlist. The maker''s own name for the underlying board design is "4x4minibadgedisplay" (its README does not use the name "Minirack"); the two appear to be the same board family (identical parts list and assembly steps: Schmitt-trigger ICs, AZ1117CR regulators, orange 0805 LEDs, MDNC RJ45 back port, USB-C front port), so this entry keeps the sweep''s "Minirack" title since that is the name used for the SAINTCON 2026 assembly video, and treats it as the same board covered by the 4x4minibadgedisplay repo.'
status: listed
sources:
- kind: url
  url: https://github.com/Herushan/MDNC---Unofficial_minibadge_display_rj45port
  title: Minirack Minibadge Display
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2026); event read as ''saintcon-2026''.'
- kind: url
  url: https://www.youtube.com/watch?v=Lw8Jp5DrFOU
  title: 2026 Minirack Minibadge Display Assembly
  accessed: '2026-09-10'
  note: 'Assembly walkthrough video; confirms the item exists and appears in the SAINTCON 2026 YouTube playlist. Description and chapter list identify parts: Schmitt-trigger ICs, AZ1117CR regulators, orange LEDs, red/green clock LEDs, MDNC RJ-45 port, USB-C.'
- kind: url
  url: https://github.com/Herushan/4x4minibadgedisplay
  title: 4x4minibadgedisplay
  accessed: '2026-09-10'
  note: 'The maker''s repo for what appears to be the same 4x4 minibadge display board design (matching parts list, MDNC RJ45 port, USB-C, Schmitt-trigger ICs, AZ1117CR regulators); source of the two saved photos and the parts list. No gerbers/schematic files in the repo, only a README with photos and a BOM.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed as a real item (not just a search snippet) via the SAINTCON 2026 YouTube playlist. Could not find a GitHub repo or page using the exact name "Minirack Minibadge Display"; the closest match, and likely the same board, is Herushan''s "4x4minibadgedisplay" repo. Price, quantity, and whether any were distributed at SAINTCON 2026 (versus just documented for home builders) were not stated anywhere found. No PCB color/finish confirmed for the specific SAINTCON 2026 build; colors here are read off the "special DC801" board photos in the 4x4minibadgedisplay repo, which may differ from the 2026 SAINTCON version''s finish.'
last_modified_date: '2026-09-10'
---

The Minirack Minibadge Display is an unofficial, community-built board for showing off SAINTCON minibadges: a 4x4 grid of 8-pin headers that holds sixteen minibadges at once, built by Herushan (who also posts as "Soldering&3Dprinting" on YouTube). It has no microcontroller — a pair of 74AHC1G14GW Schmitt-trigger inverter chips and a small red/green LED pair form a simple blinking "clock" circuit, while eight orange 0805 LEDs light the board. Power comes from a front USB-C port.

What sets it apart from a plain display board is the "MDNC" (Minibadge Display Network Connector) on the back: a standard RJ45 Ethernet jack wired to carry 5V, ground, and I2C's SDA/SCL lines, letting builders daisy-chain multiple display boards together with ordinary Ethernet cable instead of the official 20-pin minibadge connector. Only one board in a chain should have its USB-C plugged in at a time; the rest are powered over the RJ45 link. Herushan documented the MDNC pinout and warning in a separate repository, and posted a full soldering assembly video for the board, which appears in SAINTCON 2026's official YouTube playlist.

No design files (schematic, PCB layout, or gerbers) are published for the display board itself, only a parts list, photos, and the assembly video, so it is only partially open source. It does not appear to be sold; it reads as a maker's own project that others can build from the documented BOM.
