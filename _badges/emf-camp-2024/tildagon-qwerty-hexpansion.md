---
title: Tildagon QWERTY Hexpansion
id: emf-camp-2024-tildagon-qwerty-hexpansion
layout: badge
parent: EMF Camp 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: emf-camp-2024
year: 2024
makers:
- name: Alex (EastMakes)
  url: https://www.youtube.com/@EastMakes
summary: A fan-built BlackBerry-style QWERTY keyboard hexpansion for the 2024 EMF Camp Tildagon badge, using salvaged AliExpress keyboard buttons and a custom RP2040 board.
functions: Provides text-entry hardware for the Tildagon badge; the keyboard's serial output is decoded by a custom application Alex wrote since the badge's stock firmware had no native keyboard support.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - retro computer
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity:
  - uart
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not sold; a one-off DIY build documented by the maker on YouTube.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: Fusion 360
links:
- label: www.youtube.com/watch?v=5mLt09UtY2E
  url: https://www.youtube.com/watch?v=5mLt09UtY2E
  kind: video
- label: "hackaday.com — Keebin' with Kristina: the One with the Batwing Typewriter"
  url: https://hackaday.com/2025/03/11/keebin-with-kristina-the-one-with-the-batwing-typewriter/
  kind: article
images:
- file: assets/images/badges/emf-camp-2024/tildagon-qwerty-hexpansion/6748bccef5.jpg
  source: "https://hackaday.com/2025/03/11/keebin-with-kristina-the-one-with-the-batwing-typewriter/"
  credit: "EastMakes / Hackaday"
  caption: "The QWERTY hexpansion attached to a 2024 EMF Tildagon badge, RP2040 visible through the 3D-printed backplate"
contact: {}
notes:
- Fan-made BlackBerry-style QWERTY keyboard hexpansion for the Tildagon badge, RP2040-based with a 3D-printed backplate, covered by Hackaday. Found by the event-year sweep, task emf-addons.
- Sweep's title matched the maker's own wording exactly; no change needed.
status: released
sources:
- kind: url
  url: https://www.youtube.com/watch?v=5mLt09UtY2E
  title: Tildagon QWERTY Hexpansion
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''EMF Camp 2024''.'
- kind: url
  url: https://hackaday.com/2025/03/11/keebin-with-kristina-the-one-with-the-batwing-typewriter/
  title: "Keebin' with Kristina: the One with the Batwing Typewriter"
  accessed: '2026-09-08'
  note: Confirmed maker (Alex/EastMakes), RP2040 MCU, BlackBerry-style AliExpress keyboard, Fusion 360-designed 3D-printed backplate, custom decoding app, and PCB meander to align the connector; supplied the photo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real, built project via a Hackaday writeup and the maker''s own YouTube video title, but this is a personal DIY build rather than a distributed product: no evidence it was sold, kitted, or open-sourced (no GitHub repo or hardware files found under EastMakes). LED info, display, price/quantity, and open-source status could not be confirmed and are left empty.'
last_modified_date: '2026-09-08'
---

Alex, who runs the YouTube channel EastMakes, built a full QWERTY keyboard hexpansion for the 2024 EMF Camp Tildagon badge. The keyboard itself is a salvaged BlackBerry-style unit sourced from AliExpress, wired to a custom RP2040 board that Alex designed to slot into one of the Tildagon's hexagonal expansion ports. Because the connector on the badge and the buttons on the keyboard don't share the same orientation, Alex routed a deliberate meander into the PCB traces to reconcile the mismatch.

The backplate was modeled in Fusion 360 and 3D-printed, leaving the RP2040 visible through the plastic on the back of the unit. Since the Tildagon's stock firmware had no built-in support for a keyboard hexpansion, Alex also wrote a companion application that reads the serial data coming off the board and decodes it into keystrokes.

The project was covered by Hackaday (via its "Keebin' with Kristina" column) shortly after EMF Camp 2024, and Alex documented the full build process in a video on the EastMakes channel. It appears to be a one-off personal build rather than something distributed to other badge holders — no store listing, kit, or public repository for the hardware or firmware was found.
