---
title: CactusCon 2014 PCB Badge (Cactar)
id: cactuscon-2014-cactuscon-2014-pcb-badge
layout: badge
parent: CactusCon 2014
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cactuscon-2014
year: 2014
makers:
- name: Erik Wilson
  url: https://github.com/erikwilson
- name: HeatSync Labs
  url: https://heatsynclabs.org
  role: booth host / assembly kits
summary: A solderable, human-figure-shaped PCB badge given away at CactusCon 2014, with arms and legs wired as a Throwing Star LAN Tap and a head that doubles as a USB 3.0 breakout.
functions: 'No onboard logic: it is a soldering-practice kit and passive hardware tool. Arms/legs form an Ethernet LAN tap (Throwing Star LAN Tap design); the head is a USB 3.0 breakout; the body has mounting holes and breadboard space for a Teensy 2.0 and other add-ons.'
look:
  colors:
  - green
  shape: humanoid
  themes:
  - hardware tool
  - learn to solder
  - mascot
tech:
  mcu: none
  leds:
    count: null
    type: discrete
    note: Attendees soldered on their own LEDs and resistors at the booth; not populated on the bare board.
  display: none
  connectivity:
  - none
  battery: coin cell (CR-series, added by builder)
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: '300'
  availability: free
  distribution:
  - free_drop
  where: Given away and soldered on-site at the HeatSync Labs booth at CactusCon 2014 (April 4, 2014, Arizona).
make_your_own:
  open_source: true
  hardware_url: https://github.com/erikwilson/cactuscon2014
  firmware_url: null
  eda_tool: Eagle
  gerbers_url: https://github.com/erikwilson/cactuscon2014
  license: MIT
  notes: Repo includes Eagle schematic/board files, a gerber/ directory, and custom Eagle libraries; no BOM or firmware is included (the badge has no MCU by default beyond the optional Teensy mounting area).
links:
- label: badge.gallery/badges/cactuscon-2014-pcb-badge
  url: https://badge.gallery/badges/cactuscon-2014-pcb-badge
  kind: website
- label: erikwilson/cactuscon2014 (GitHub)
  url: https://github.com/erikwilson/cactuscon2014
  kind: repo
- label: 'Robot Ambassador: CactusCon PCB Badges'
  url: https://www.azrobotambassador.com/2014/04/cactuscon-pcb-badges.html
  kind: article
images:
- file: assets/images/badges/cactuscon-2014/cactuscon-2014-pcb-badge/1271845127.jpg
  source: https://www.azrobotambassador.com/2014/04/cactuscon-pcb-badges.html
  credit: Robot Ambassador blog / HeatSync Labs
  caption: Assembled CactusCon 2014 PCB badge
- file: assets/images/badges/cactuscon-2014/cactuscon-2014-pcb-badge/c1efc3dd4c.jpg
  source: https://www.azrobotambassador.com/2014/04/cactuscon-pcb-badges.html
  credit: Robot Ambassador blog / HeatSync Labs
  caption: CactusCon 2014 badge fully assembled with acrylic and LEDs
- file: assets/images/badges/cactuscon-2014/cactuscon-2014-pcb-badge/148740f9e0.jpg
  source: https://github.com/erikwilson/cactuscon2014
  credit: Erik Wilson
  caption: Illuminated Cactar badge showing the cactus-shaped PCB
- file: assets/images/badges/cactuscon-2014/cactuscon-2014-pcb-badge/a35b92e98d.jpg
  source: https://github.com/erikwilson/cactuscon2014
  credit: Erik Wilson
  caption: CactusCon 2014 Cactar badge, bare PCB
contact: {}
notes:
- The discovery sweep's original title was "CactusCon 2014 PCB Badge"; the maker's GitHub repo names the design "cactar" (a portmanteau referencing the CactusCon logo it is built around). Kept the sweep's title as primary and added "(Cactar)" since that is the repo/informal name, not a formally marketed product name.
- No LED count, resistor values, or specific battery part number are documented anywhere found; attendees supplied/soldered these themselves from a kit HeatSync Labs provided (acrylic, LEDs, resistors, coin battery, lanyard), so tech.leds.count and battery specifics are left unset.
- Sweep's sources list only named the GitHub repo; this pass fetched it and confirmed the item.
- This is the same badge already documented in more depth under cactuscon-2014-cactuscon-2014-pcb-badge (same repo, "Order of the Cactar"); that entry has fuller field detail (quantity 300, free distribution, LED/battery notes from a second source).
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/cactuscon-2014-pcb-badge
  title: CactusCon 2014 PCB Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-layerone); event read as ''CactusCon 2014''.'
- kind: url
  url: https://github.com/erikwilson/cactuscon2014
  title: erikwilson/cactuscon2014
  accessed: '2026-09-10'
  note: Maker's own repo; confirms design name "cactar", MIT license, Eagle files and gerbers, LAN-tap/USB3/Teensy features, no firmware.
- kind: url
  url: https://www.azrobotambassador.com/2014/04/cactuscon-pcb-badges.html
  title: 'Robot Ambassador: CactusCon PCB Badges'
  accessed: '2026-09-10'
  note: First-hand account of the HeatSync Labs soldering booth; confirms 300 badges made, Erik Wilson design credit, free giveaway, and provided the two saved photos.
- kind: url
  url: https://raw.githubusercontent.com/erikwilson/cactuscon2014/master/README.md
  title: erikwilson/cactuscon2014 README ("Order of the Cactar")
  accessed: '2026-09-10'
  note: Confirmed the item, maker, event, manufacturing/assembly story, design tools, and function as LAN tap + USB 3.0 breakout + Teensy 2.0 mount.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Maker's own GitHub repo and a first-hand attendee blog post both confirm the badge, quantity (300), designer, and giveaway; the two accounts agree on all core facts. No BOM, firmware, LED count, or price beyond "free" was ever published. Merged with duplicate entry 'CactusCon 2014 Badge (Cactar)' (cactuscon-2014-cactuscon-2014-badge).
last_modified_date: '2026-09-10'
redirect_from:
- /badges/cactuscon-2014/cactuscon-2014-badge/
model:
  file: assets/models/cactuscon-2014/cactuscon-2014-pcb-badge.glb
  method: kicad
  source_file: cactar.brd
  generated: '2026-09-10'
  bytes: 316564
---

The CactusCon 2014 PCB badge, nicknamed "cactar" in its designer's own repo, was a free giveaway soldered together by hand at the HeatSync Labs booth during CactusCon's April 2014 event in Arizona. Erik Wilson designed the board as a humanoid shape built around the CactusCon logo: the arms and legs double as a Throwing Star-style Ethernet LAN tap, the head works as a USB 3.0 breakout, and the torso leaves mounting holes and breadboard space for a Teensy 2.0 or other add-ons. HeatSync Labs manufactured 300 of the boards through Advanced Circuits and ran a soldering station where attendees of all skill levels — from complete beginners to experienced hackers — assembled their own badge with an acrylic backing, LEDs, resistors, a coin cell battery, and a lanyard.

The badge itself carries no microcontroller or firmware out of the box; it is a bare, passive PCB whose value is the soldering exercise and the LAN-tap/USB-breakout hardware, with the Teensy footprint left open for anyone who wanted to add their own logic. Erik Wilson published the full hardware design — Eagle schematic and board files, gerbers, and custom component libraries — under an MIT license on GitHub, though no bill of materials or firmware was ever included since the board doesn't require any.

## Make your own

The hardware files (Eagle `.sch`/`.brd`, a `gerber/` directory, and supporting libraries) are on GitHub at erikwilson/cactuscon2014 under an MIT license. There is no published BOM; component choices (LED type/count, resistor values, coin cell type) were left up to whoever built the kit and are not documented in the repo or the contemporary coverage found.

## Notes merged from the duplicate entry "CactusCon 2014 Badge (Cactar)"

The Cactar is a cactus-shaped, human-figure PCB badge that Erik Wilson designed for CactusCon 2014, Arizona's community-run security conference. It was funded through Kickstarter backer donations and conference sponsors, manufactured by Advanced Circuits in Aurora, Colorado, and assembled and tested on site by attendees with help from HeatSync Labs members, making it as much a soldering exercise as a badge.

Functionally the board does triple duty: the arms and legs are wired as a Throwing Star LAN tap (Michael Ossmann's design), letting data flow in through the arms and out through the feet for passive Ethernet tapping; the head serves as a USB 3.0 breakout and test board; and the body has mounting holes plus a breadboard area sized for a Teensy 2.0 or similar microcontroller, with room for extras like a USB host shield. The board carries hidden symbolism throughout, including an Eye of Providence, the maker's initials worked into the artwork, Tau and Phi glyphs, a Conway's Game of Life glider, and a Jolly Roger, alongside sponsor and HeatSync Labs branding.

## Make your own

The hardware is open source (MIT license) at github.com/erikwilson/cactuscon2014. The board was designed in the free version of Eagle, using a custom ULP script to import vector art from Inkscape; Gerber files are included in the repo and are viewable through the MayhewLabs WebGL Gerber renderer.
