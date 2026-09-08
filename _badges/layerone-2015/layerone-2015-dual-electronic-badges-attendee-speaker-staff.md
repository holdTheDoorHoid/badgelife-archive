---
title: LayerOne 2015 Dual Electronic Badges (Attendee + Speaker/Staff)
id: layerone-2015-layerone-2015-dual-electronic-badges-attendee-speaker-staff
layout: badge
parent: LayerOne 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: layerone-2015
year: 2015
makers:
- name: charliex, null space labs
  url: https://hackaday.io/project/4207-layerone-2015-badge
summary: LayerOne 2015 issued two distinct electronic badges instead of one - a solder-it-yourself blinky badge for general attendees, and a far more powerful Linux-on-a-board badge for speakers and staff.
functions: 'Attendee badge: hand-solder your own badge (QFP/SOT-23 parts) to earn entry, then run WS2812B LED animations over a PSoC4 with ESP8266 Wi-Fi control. Speaker/staff badge: a full Linux box with dual Ethernet ports running OpenWRT, with a LuCI web interface and USB/microSD storage.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
tech:
  mcu: PSoC4 + ESP8266 (attendee badge); VoCore (RT5350F) running OpenWRT (speaker/staff badge)
  leds:
    count: 22
    type: WS2812B
    note: Individually addressable RGB LEDs on the attendee badge, driven by the PSoC4.
  display: none
  connectivity:
  - wifi
  battery: 2x CR123A (attendee badge)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Given to conference attendees (as a bare PCB + parts bag to solder) and separately to speakers/staff (pre-built) at LayerOne 2015, May 23-24, 2015, Sheraton Gateway LAX, Los Angeles.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/charlie-x/psoc4-esp8266-ws1812
  firmware_url: https://github.com/charlie-x/psoc4-esp8266-ws1812
  eda_tool: null
  notes: 'GitHub repo (charlie-x/psoc4-esp8266-ws1812, released under The Unlicense) covers the attendee LED badge only; no public repo found for the speaker/staff VoCore/OpenWRT badge.'
links:
- label: badge.gallery/badges/layerone-2015-dual-electronic-badges
  url: https://badge.gallery/badges/layerone-2015-dual-electronic-badges
  kind: website
- label: LayerOne 2015 Badge - Hackaday.io project
  url: https://hackaday.io/project/4207-layerone-2015-badge
  kind: hackaday
- label: charlie-x/psoc4-esp8266-ws1812 (GitHub)
  url: https://github.com/charlie-x/psoc4-esp8266-ws1812
  kind: repo
- label: 'LayerOne Hardware Hacking Village - Hackaday.com'
  url: https://hackaday.com/2015/05/24/layerone-hardware-hacking-village/
  kind: article
images:
- file: assets/images/badges/layerone-2015/layerone-2015-dual-electronic-badges-attendee-speaker-staff/081c72176a.jpg
  source: "https://hackaday.io/project/4207-layerone-2015-badge"
  credit: "charlie-x / Hackaday.io"
  caption: "LayerOne 2015 attendee badge with PSoC4, ESP8266, and WS2812B LEDs"
- file: assets/images/badges/layerone-2015/layerone-2015-dual-electronic-badges-attendee-speaker-staff/9b14ab5718.jpg
  source: "https://hackaday.io/project/4207/gallery"
  credit: "charlie-x / Hackaday.io"
  caption: "LayerOne 2015 badge project gallery photo"
contact: {}
notes:
- Attendee badge used a PSoC4 driving 22 addressable RGB LEDs plus an ESP8266, while the speaker/staff badge was a Linux-on-a-badge with two Ethernet ports running OpenWRT. Found by the event-year sweep, task con-layerone.
- 'Sweep''s source title matched the maker''s own naming closely; title kept as-is.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/layerone-2015-dual-electronic-badges
  title: LayerOne 2015 Dual Electronic Badges (Attendee + Speaker/Staff)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''LayerOne 2015''.'
- kind: url
  url: https://hackaday.io/project/4207-layerone-2015-badge
  title: LayerOne 2015 Badge - Hackaday.io
  accessed: '2026-09-08'
  note: 'Maker''s own project page; confirms PSoC4/ESP8266/WS2812B attendee badge and VoCore/OpenWRT RT5350F speaker/staff badge, and provided the gallery photos.'
- kind: url
  url: https://github.com/charlie-x/psoc4-esp8266-ws1812
  title: charlie-x/psoc4-esp8266-ws1812
  accessed: '2026-09-08'
  note: 'Open-source hardware/firmware repo (The Unlicense) for the attendee LED badge only.'
- kind: url
  url: https://hackaday.com/2015/05/24/layerone-hardware-hacking-village/
  title: LayerOne Hardware Hacking Village
  accessed: '2026-09-08'
  note: 'Press coverage confirming distribution split (attendees solder their own; speakers/staff receive the Linux badge) and the "earn your hacker cred" soldering-village framing.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): all four cited sources (Hackaday.io project 4207, the charlie-x/psoc4-esp8266-ws1812 GitHub repo, the Hackaday.com Hardware Hacking Village article, and badge.gallery''s own writeup) were re-fetched and independently confirm every non-empty field and body sentence - PSoC4+ESP8266+22x WS2812B+2x CR123A on the attendee badge, VoCore/RT5350F+OpenWRT+dual Ethernet on the speaker/staff badge, the solder-it-yourself vs pre-built distribution split, and the Unlicense on the attendee badge''s repo. No contradictions found. Price and production quantity remain unstated anywhere found, correctly left blank. Both saved images were re-verified against their source pages and correctly show only the attendee LED badge (no speaker/staff photo exists in any source found).'
last_modified_date: '2026-09-08'
---

LayerOne 2015 broke from the usual one-badge-per-attendee model and ran two different electronic badges side by side. General attendees got a bare PCB and a bag of parts, and had to hand-solder their own badge - including fine-pitch QFP and SOT-23 components - at the con's Hardware Hacking Village before it would work, in keeping with LayerOne's ethos of earning your badge rather than buying pre-made "hacker cred." That attendee badge is built around a Cypress PSoC4 paired with an ESP8266 Wi-Fi module, driving 22 individually addressable WS2812B RGB LEDs and running off two CR123A batteries.

Speakers and staff instead received a considerably more capable badge: a VoCore module (RT5350F) running OpenWRT Linux, with two Ethernet ports, a LuCI web interface, and USB/microSD storage - effectively a small Linux router worn as a badge. Both designs were created by charliex of null space labs, LayerOne's home hackerspace, and documented on a shared Hackaday.io project page.

Only the attendee LED badge's design has been published openly, in charlie-x's `psoc4-esp8266-ws1812` GitHub repository under The Unlicense; no public hardware or firmware release was found for the speaker/staff network badge. Neither badge's price or exact production quantity is documented in the sources found.

## Make your own

The attendee LED badge's hardware and firmware are on GitHub at [charlie-x/psoc4-esp8266-ws1812](https://github.com/charlie-x/psoc4-esp8266-ws1812), released under The Unlicense. The repo covers the PSoC4 + ESP8266 + WS2812B design; there is no equivalent public release for the VoCore/OpenWRT speaker/staff badge.
