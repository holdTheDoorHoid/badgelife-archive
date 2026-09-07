---
title: DEF CON 29 Badge (2021)
id: dc29-badge-2021
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: MK Factor (Michael and Katie Whiteley), with The Dark Tangent
  url: https://mkfactor.com/
summary: 'The official human badge for DEF CON 29 (2021): a stacked-board electronic badge built around a networked "Simon Says"-style game with four RGB keys and touch sensors.'
functions: A networked Simon Says game that scales across badges connected via the side male/female connectors or a special USB-A/USB-C lanyard cable; players sync progress through a web console reachable from a phone or laptop, and the badge hides an extensive CTF (ROT13/Vigenere/Ottendorf ciphers, solder-pad hardware hacking, and physical-design Easter eggs).
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - ctf
  - wearable
tech:
  mcu: MC56F8006VLC
  leds: null
  display: null
  connectivity:
  - usb
  battery: rechargeable, chargeable via USB-A or USB-C
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to DEF CON 29 attendees as the standard human conference badge.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: defcon.org/html/defcon-29/dc-29-index.html
  url: https://defcon.org/html/defcon-29/dc-29-index.html
  kind: website
- label: DEFCON 29 - Badge Writeup (Science Viking Labs)
  url: https://sciencevikinglabs.com/blog/hardware/2021-08-14-DEFCON29-Badge-Writeup/
  kind: article
  archived: https://web.archive.org/web/20260524035125/https://sciencevikinglabs.com/blog/hardware/2021-08-14-DEFCON29-Badge-Writeup/
- label: Making the DEF CON 29 Badge (talk, InfoconDB)
  url: https://infocondb.org/con/def-con/def-con-29/making-the-def-con-29-badge
  kind: video
- label: MK Factor
  url: https://mkfactor.com/
  kind: website
  archived: https://web.archive.org/web/20260614164003/http://mkfactor.com/
images:
- file: assets/images/badges/dc29/badge-2021/5a5251d376.jpg
  source: https://sciencevikinglabs.com/blog/hardware/2021-08-14-DEFCON29-Badge-Writeup/
  credit: Science Viking Labs
  caption: Front of the DEF CON 29 (2021) official badge
  archived: https://web.archive.org/web/20260524035125/https://sciencevikinglabs.com/blog/hardware/2021-08-14-DEFCON29-Badge-Writeup/
- file: assets/images/badges/dc29/badge-2021/8e2a0129d5.jpg
  source: https://sciencevikinglabs.com/blog/hardware/2021-08-14-DEFCON29-Badge-Writeup/
  credit: Science Viking Labs
  caption: Back of the DEF CON 29 (2021) official badge
  archived: https://web.archive.org/web/20260524035125/https://sciencevikinglabs.com/blog/hardware/2021-08-14-DEFCON29-Badge-Writeup/
contact: {}
notes:
- Confirmed this session via defcon.org DC29 index page text and linked Hacker Hangouts video 'Designing the DEF CON 29 and 30 Badges (featuring MK Factor)'.
status: released
sources:
- kind: url
  url: https://defcon.org/html/defcon-29/dc-29-index.html
  title: DEF CON 29 Badge (2021)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''DEF CON 29''.'
- kind: url
  url: https://sciencevikinglabs.com/blog/hardware/2021-08-14-DEFCON29-Badge-Writeup/
  title: DEFCON 29 - Badge Writeup | Science Viking Labs
  accessed: '2026-09-07'
  note: 'Primary source for physical description: stacked boards, four RGB keys, three touch sensors, USB-A/USB-C ports and lanyard, battery/USB charging, Simon Says game, CTF ciphers and hardware-hacking challenge; front/back photos.'
  archived: https://web.archive.org/web/20260524035125/https://sciencevikinglabs.com/blog/hardware/2021-08-14-DEFCON29-Badge-Writeup/
- kind: url
  url: https://infocondb.org/con/def-con/def-con-29/making-the-def-con-29-badge
  title: Making the DEF CON 29 Badge
  accessed: '2026-09-07'
  note: Confirms makers Michael and Katie Whiteley of MK Factor and the presence of a companion DEF CON talk on the badge's design and manufacture.
- kind: url
  url: https://mkfactor.com/
  title: MK Factor
  accessed: '2026-09-07'
  note: Maker's own site, used for the makers URL.
  archived: https://web.archive.org/web/20260614164003/http://mkfactor.com/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: MCU (MC56F8006VLC) is stated by the Science Viking Labs writeup, which says it is the same part used in the DC17/DC18 badges; not independently cross-checked against a maker teardown. LED count/type, display, colors, and shape were not stated by any source found and are left empty. Price and quantity are not published anywhere found; distribution was free as the standard attendee badge. Two other DC29 badges exist as separate community entries (AND!XOR's electronic badge, Whiskey Pirates' RISC-V badge) and are not this one.
last_modified_date: '2026-09-07'
---

The DEF CON 29 (2021) official human badge was designed and built by MK Factor — the husband-and-wife badgemaking team of Michael and Katie Whiteley — working with The Dark Tangent, and was handed out to attendees as the standard conference badge. It is a stacked-board electronic badge with four RGB keys and three touch sensors on the front, side male/female connectors for daisy-chaining badges together, and USB-A and USB-C ports on the bottom; a special lanyard cable terminated in USB-A and USB-C plugs let badges talk to each other directly. It runs on a rechargeable battery that can be topped up through either USB port.

The badge's core game is a networked version of Simon Says that scales as more badges are linked together, with progress tracked through a web console reachable from a phone or laptop. Underneath that sits a much larger CTF: classic ciphers (ROT13, Vigenère, Ottendorf), a hardware-hacking step that requires soldering onto specific pads, and Easter eggs worked into the badge's physical design that require reverse engineering to find. The Whiteleys detailed the badge's creation — including pandemic-era chip shortages and delayed parts — in a DEF CON 29 talk, "Making the DEF CON 29 Badge."

This is the official DEF CON 29 human badge; two other well-known DC29 badges from the same year (AND!XOR's electronic badge and the Whiskey Pirates' RISC-V badge) are separate community badges and are not covered by this entry.
