---
title: SAINTCON 2016 Badge
id: saintcon-2016-saintcon-2016-badge
layout: badge
parent: SAINTCON 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2016
year: 2016
makers:
- name: SAINTCON (badge team)
  url: https://gitlab.com/saintcon/SaintCon2016Badge
summary: The official SAINTCON 2016 conference badge, an ESP8266-based board assembled by attendees at the Hardware Hacking Village and used to display a live score for the con's "Hackers Challenge" game.
functions: Displays a live, updating score (refreshed roughly every 30 seconds) for SAINTCON's "Hackers Challenge" game after the wearer registers their badge's unique ID; also shows a UUID/link code at flashing time.
look:
  colors:
  - green
  shape: rectangle
  themes:
  - security
  - ctf
tech:
  mcu: ESP8266 (Wemos D1 Mini)
  leds:
    count: 8
    type: 7-segment
    note: Two 4-digit 7-segment LED modules driven by a MAX7219 IC; displays were offered in yellow, green, red, white, and blue.
  display: 2x 4-digit 7-segment LED (MAX7219-driven)
  connectivity:
  - wifi
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Assembled by attendees from a kit at SAINTCON 2016's Hardware Hacking Village; parts included a bag of resistors/capacitors/fuses/headers, a Wemos D1 Mini, and a 7-segment LED display in the buyer's choice of color.
make_your_own:
  open_source: true
  hardware_url: https://gitlab.com/saintcon/SaintCon2016Badge
  firmware_url: https://gitlab.com/saintcon/SaintCon2016Badge
  eda_tool: null
links:
- label: saintcon2016badge.readthedocs.io/en/latest
  url: https://saintcon2016badge.readthedocs.io/en/latest/
  kind: website
- label: saintcon.gitlab.io/SaintCon2016Badge (assembly + flashing docs mirror)
  url: http://saintcon.gitlab.io/SaintCon2016Badge/
  kind: doc
- label: SaintCon2016Badge on GitLab (hardware + firmware source)
  url: https://gitlab.com/saintcon/SaintCon2016Badge
  kind: repo
images:
- file: assets/images/badges/saintcon-2016/saintcon-2016-badge/8588118774.jpg
  source: http://saintcon.gitlab.io/SaintCon2016Badge/assembly/
  credit: SAINTCON badge team
  caption: Finished assembled SAINTCON 2016 badge, ESP8266 D1 Mini with dual 4-digit 7-segment LED displays
- file: assets/images/badges/saintcon-2016/saintcon-2016-badge/563308bfa1.png
  source: http://saintcon.gitlab.io/SaintCon2016Badge/assembly/
  credit: SAINTCON badge team
  caption: SAINTCON 2016 badge PCB drawing
contact: {}
notes:
- The official SAINTCON 2016 electronic conference badge, an ESP8266 (Wemos D1 Mini)-based badge with a MAX7219-driven 7-segment LED display, assembled at the con's Hardware Hacking Village; official assembly docs and firmware are hosted on GitLab and readthedocs. Found by the event-year sweep, task saintcon-2016.
status: released
sources:
- kind: url
  url: https://saintcon2016badge.readthedocs.io/en/latest/
  title: SAINTCON 2016 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2016); event read as ''saintcon-2016''.'
- kind: url
  url: http://saintcon.gitlab.io/SaintCon2016Badge/assembly/
  title: Badge Assembly - SaintCon 2016 Badge - saintcon.gitlab.io
  accessed: '2026-09-08'
  note: GitLab Pages mirror of the readthedocs site (which returns HTTP 500 for its images); confirmed MCU, MAX7219 display driver, BOM, assembly steps, and provided both images.
- kind: url
  url: http://saintcon.gitlab.io/SaintCon2016Badge/registration/
  title: Badge Registration - SaintCon 2016 Badge - saintcon.gitlab.io
  accessed: '2026-09-08'
  note: Confirmed the "Hackers Challenge" game function - badge shows a live score after registering the badge's UUID.
- kind: url
  url: https://gitlab.com/saintcon/SaintCon2016Badge
  title: SAINTCON / SaintCon2016Badge on GitLab
  accessed: '2026-09-08'
  note: Confirmed the repo holds both firmware (src/) and hardware (plans/) for the badge, i.e. hardware and firmware are both published.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: The primary readthedocs.io site is up but serves HTTP 500 for every image under /img/ (site-wide, not just this badge); a GitLab Pages mirror of the same mkdocs site (saintcon.gitlab.io/SaintCon2016Badge) serves the identical content and working images, so that mirror was used for images and to double-check text. Price, quantity made, and current availability are not stated on the sweep target or its mirrors and were left empty. Colors listed are for the LED digit displays offered (yellow/green/red/white/blue), not necessarily the PCB soldermask; PCB color itself was not stated, so only the LED-visible green from the sample photo is recorded and look.colors/look.shape/look.themes are inferred loosely from the photos rather than a maker style statement - treat these three fields as lower confidence than the rest.
last_modified_date: '2026-09-10'
model:
  file: assets/models/saintcon-2016/saintcon-2016-badge.glb
  method: gerber
  source_file: plans/gerbers
  generated: '2026-09-10'
  bytes: 300960
  size_mm:
  - 145.0
  - 120.0
---

The SAINTCON 2016 badge is an ESP8266-based board (Wemos D1 Mini) that attendees soldered together themselves at SAINTCON's Hardware Hacking Village. A MAX7219 LED driver chip runs two 4-digit, 7-segment LED modules, which buyers could pick in yellow, green, red, white, or blue when they assembled their kit. Beyond the through-hole basics (resistors, capacitors, PolySwitch fuses, an IC socket for the MAX7219, and headers), the badge's electronics are entirely off-the-shelf modules soldered onto a custom PCB.

Functionally, the badge ties into SAINTCON's "Hackers Challenge" game: after flashing, each badge reports a UUID (shown both at the flashing station and over serial on boot), and once a participant registers that UUID the badge's display updates every 30 seconds or so to show their current game score. The ESP8266's Wi-Fi radio is what lets the badge phone home for that live score feed.

## Make your own

Both the hardware (PCB/BOM under `plans/`) and firmware (under `src/`) are published in the `SaintCon2016Badge` GitLab repository, alongside the RPi-based flash station tooling SAINTCON used to program badges at the con and the mkdocs source for the assembly/flashing documentation itself. The published assembly guide covers component placement (soldering the small passives first, then headers, IC socket, D1 Mini, and finally the LED digit displays with correct orientation), and the flashing guide documents using `esptool.py` to write firmware over USB.
