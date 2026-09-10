---
title: Hardware Hacking Community Badge
id: saintcon-2023-hardware-hacking-community-badge-2023-portal-theme
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: rogu3bull3t
summary: A soldering-practice minibadge from SAINTCON 2023's Hardware Hacking Community, made as the companion project for the Beginning Soldering class, with a Portal-game-styled ring design.
functions: No onboard logic; it lights two LEDs (a blue SMD 1206 and a flexible filament LED) once soldered, and its purpose is to teach basic through-hole and SMD hand-soldering.
look:
  colors:
  - black
  shape: circle
  themes:
  - hardware tool
  - learn to solder
  - sci-fi
tech:
  mcu: 'none'
  leds:
    count: 2
    type: 'SMD 1206, flexible filament LED'
    note: One blue 1206 SMD LED plus a 38mm 2200K flexible filament LED tracing the ring; a 1206 10-ohm resistor sets the SMD LED current.
  display: 'none'
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Handed out at the Hardware Hacking Community table at SAINTCON 2023 as the kit for the Beginning Soldering class.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: website
- label: 'Hardware Hacking Community Build Guide for Saintcon 2023 (YouTube)'
  url: https://youtu.be/_L1SkQZLtTE
  kind: video
- label: SAINTCON Hardware Hacking Community page
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/com-hardware-community/
  kind: website
images: []
contact: {}
notes:
- 2023 Hardware Hacking Community minibadge companion to the beginner soldering class, Portal-game themed with a flexible filament LED. Found by the event-year sweep, task saintcon-2023.
- 'The sweep-imported title appended "(2023, Portal theme)"; the SAINTCON minibadge guide itself just calls it "Hardware Hacking Community Badge" under the "Community Minibadge" category, so the title was trimmed to match.'
status: listed
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: Hardware Hacking Community Badge (2023, Portal theme)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: 2023 Minibadge Guide, page 20 (Community Minibadge - Hardware Hacking Community Badge)
  accessed: '2026-09-10'
  note: Confirmed maker (rogu3bull3t), description, difficulty/rarity, assembly steps, parts list (38mm 2200K flexible filament LED, blue SMD 1206 LED, 1206 10R resistor), and "visit the Hardware Hacking Community table" as the distribution method.
- kind: url
  url: https://youtu.be/_L1SkQZLtTE
  title: Hardware Hacking Community Build Guide for Saintcon 2023
  accessed: '2026-09-10'
  note: 'Corroborating build-guide video by rogu3bull3t linked from the same PDF page; only checked the title card, no usable photo of the finished badge (thumbnail is a generic title slide).'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/com-hardware-community/
  title: COM - Hardware Community - SAINTCON
  accessed: '2026-09-10'
  note: Confirms the Hardware Hacking Community's general description; no badge-specific detail beyond what the PDF already gave.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Price, quantity made, and open-source status are not stated anywhere in the guide or the linked build video, so those fields are left empty. No standalone photo of the assembled badge could be found outside the PDF page itself (a rendered scan of the PDF page is not a maker photo, so no image was saved). A similar third-party badge-archive site (badge.gallery) turned up in search but was not used as a source per the research guide''s preference for maker/organizer sources, and none of its content was treated as instructions.'
last_modified_date: '2026-09-10'
---

The Hardware Hacking Community Badge is SAINTCON 2023's "Community Minibadge," designed by rogu3bull3t as the companion kit for the con's Beginning Soldering class. It carries a Portal-game-styled design: a black PCB with a brown ring motif (echoing the game's portal effect) around a Portal character silhouette on the front, and "SAINTCON 2023" plus the Hardware Hacking Community's name on the back.

Electrically it is simple by design, since its job is teaching soldering rather than doing anything on its own: a blue SMD 1206 LED with a 1206 10-ohm current-limiting resistor, and a 38mm 2200K flexible filament LED bent to trace part of the ring, wired to pin headers that connect it to a host badge for power. The official guide rates it "Intermediate" difficulty and "Common" rarity, and a companion build-guide video walks through the assembly (solder the LEDs and resistor using the single-pad method, then the filament LED — anode side marked by a hole — then the pin headers).

It was distributed by visiting the Hardware Hacking Community's table at SAINTCON 2023 rather than sold or raffled; no price or production quantity is stated in the available sources, and no hardware files were found published for it.
