---
title: CarolinaCon 15 Badge
id: carolinacon-2019-carolinacon-15-badge
layout: badge
parent: CarolinaCon 15
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: carolinacon-2019
year: 2019
makers:
- name: 49th Security Division
  url: https://github.com/49thSecurityDivision
summary: A crown-shaped, solder-it-yourself electronic badge for CarolinaCon 15 (2019), lighting 16 blue LEDs across a "15" and crown motif via an ATTINY84 and MAX7219 LED driver.
functions: Lights a pattern of 16 blue LEDs (crown/"15" shape) via ATTINY84 firmware driving a MAX7219 LED driver; hackable/reprogrammable over ISP.
look:
  colors:
  - green
  - white
  - blue
  shape: crown
  themes:
  - hardware tool
  - learn to solder
  - kit
tech:
  mcu: ATTINY84
  leds:
    count: 16
    type: reverse-mount
    note: Clear blue THT LEDs, driven by a MAX7219 LED driver chip under ATTINY84 control.
  display: LED matrix
  connectivity: []
  battery: 4x AAA (external holder)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  - kit
  where: Handed out to CarolinaCon 15 attendees in 2019 as a solder-it-yourself kit (bag of parts plus bare PCB, assembled at the con).
make_your_own:
  open_source: true
  hardware_url: https://github.com/49thSecurityDivision/CC-15-Badges
  firmware_url: https://github.com/49thSecurityDivision/CC-15-Badges/blob/master/Carolina_Con_15.ino.ino
  eda_tool: null
  notes: Build guide (BadgeGuide.pdf) and Arduino-IDE firmware are in the repo; programming the ATTINY84 requires a second Arduino set up as an ISP programmer.
links:
- label: github.com/49thSecurityDivision/CC-15-Badges
  url: https://github.com/49thSecurityDivision/CC-15-Badges
  kind: repo
  archived: https://web.archive.org/web/20260912175248/https://github.com/49thSecurityDivision/CC-15-Badges
- label: BadgeGuide.pdf (build guide)
  url: https://github.com/49thSecurityDivision/CC-15-Badges/blob/master/BadgeGuide.pdf
  kind: doc
  archived: https://web.archive.org/web/20260912175352/https://github.com/49thSecurityDivision/CC-15-Badges/blob/master/BadgeGuide.pdf
images:
- file: assets/images/badges/carolinacon-2019/carolinacon-15-badge/7344968254.jpg
  source: https://github.com/49thSecurityDivision/CC-15-Badges/blob/master/BadgeGuide.pdf
  credit: 49th Security Division
  caption: Assembled CarolinaCon 15 badge, crown-shaped PCB with blue LEDs lit, on the workbench
  archived: https://web.archive.org/web/20260912175352/https://github.com/49thSecurityDivision/CC-15-Badges/blob/master/BadgeGuide.pdf
- file: assets/images/badges/carolinacon-2019/carolinacon-15-badge/b3cdd00cd7.jpg
  source: https://github.com/49thSecurityDivision/CC-15-Badges/blob/master/BadgeGuide.pdf
  credit: 49th Security Division
  caption: 'Solder-it-yourself kit contents: bare crown-shaped PCB, 16 blue LEDs, ATTINY84, MAX7219, battery pack, and other parts'
  archived: https://web.archive.org/web/20260912175352/https://github.com/49thSecurityDivision/CC-15-Badges/blob/master/BadgeGuide.pdf
contact: {}
notes:
- ATTINY84-based badge with an LED matrix display, distributed at CarolinaCon 15 (2019), with build guide and firmware in the linked repo. Found by the event-year sweep, task carolinacon.
- The sweep's sheet title matched the maker's own wording ("CarolinaCon 15 Badge"); no correction needed.
status: released
sources:
- kind: url
  url: https://github.com/49thSecurityDivision/CC-15-Badges
  title: CarolinaCon 15 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:carolinacon); event read as ''CarolinaCon 2019''.'
  archived: https://web.archive.org/web/20260912175248/https://github.com/49thSecurityDivision/CC-15-Badges
- kind: url
  url: https://github.com/49thSecurityDivision/CC-15-Badges/blob/master/BadgeGuide.pdf
  title: Carolina Con 15 Badge Guide
  accessed: '2026-09-08'
  note: 'Build guide PDF: confirms crown-shaped PCB with "15" tag, 16 blue LEDs, ATTINY84 + MAX7219, 4x AAA battery pack, power switch; distributed as a solder-it-yourself kit; designer credited as "wm & mt". Source of both saved photos.'
  archived: https://web.archive.org/web/20260912175352/https://github.com/49thSecurityDivision/CC-15-Badges/blob/master/BadgeGuide.pdf
- kind: url
  url: https://raw.githubusercontent.com/49thSecurityDivision/CC-15-Badges/master/README.md
  title: CC-15-Badges README
  accessed: '2026-09-08'
  note: Confirms ATTINY84 target, Arduino IDE + LedControl library toolchain, and ISP-programming-via-second-Arduino build process.
  archived: https://web.archive.org/web/20260912175412/https://raw.githubusercontent.com/49thSecurityDivision/CC-15-Badges/master/README.md
- kind: url
  url: http://carolinacon.org/pages/cc-history.html
  title: CarolinaCon history
  accessed: '2026-09-08'
  note: Confirms 49th Security Division is the UNC Charlotte ethical-hacking club that has organized CarolinaCon since it moved to Charlotte; corroborates event attribution.
  archived: https://web.archive.org/web/20260912175436/http://carolinacon.org/pages/cc-history.html
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: No price or quantity-made figures found anywhere; left empty rather than guessed. No maker photo of the badge was hosted as a standalone image online — both saved photos were extracted from the build-guide PDF in the repo. Designers are credited in the guide only by initials ("wm & mt"); full names not published, so makers.name kept as the org.
last_modified_date: '2026-09-08'
---

The CarolinaCon 15 badge is a crown-shaped PCB handed out as a solder-it-yourself kit to attendees of CarolinaCon 15, held in Charlotte, NC in April 2019. It was designed and produced by members of the 49th Security Division, the UNC Charlotte ethical-hacking club that has run CarolinaCon since it relocated to Charlotte. Each kit bag held the bare PCB, 16 clear blue through-hole LEDs, an ATTINY84 microcontroller, a MAX7219 LED driver, a 4xAAA battery holder, a power switch, and the handful of passives needed to complete the circuit; attendees soldered it themselves at the con, with staff on hand to help first-time solderers.

Once assembled, the ATTINY84 drives the LEDs (via the MAX7219) in a crown/"15" pattern on the board, with a small stamped "15" tag riveted at the top like a keychain fob. The badge reads "Carolina Con" in silkscreen across the bottom of the crown.

## Make your own

The GitHub repo (github.com/49thSecurityDivision/CC-15-Badges) publishes the Arduino-IDE firmware (`Carolina_Con_15.ino.ino`, built against the LedControl library) and a build guide PDF with soldering-order photos and a bill of materials. Reflashing the ATTINY84 requires wiring a second Arduino as an ISP programmer, per the linked Instructables tutorial in the README; no separate hardware/Gerber files are published beyond the guide's photos of the finished board.
