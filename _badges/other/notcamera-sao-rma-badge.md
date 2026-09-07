---
title: NotCamera SAO (RMA Badge)
id: other-notcamera-sao-rma-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: wrickert
  url: https://github.com/wrickert
summary: A small PCB SAO cut into the silhouette of a security camera, silkscreened "This is not a Camera" on the front, with a single LED hidden behind the fake lens.
functions: 'A single LED behind the "lens" pad blinks on its own via a two-transistor astable flasher circuit (no microcontroller); a small slide switch (SW1) is also on the board.'
look:
  colors:
  - green
  - gold
  shape: camera
  themes:
  - security
  - meme
  form_factor: pcb sao
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Reverse-mounted LED behind a gold lens pad, blinked by a two-transistor (Q1/Q2) astable multivibrator rather than a microcontroller.
  display: none
  connectivity: []
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/wrickert/RMABadge/tree/master/SAO/NotCamera
  firmware_url: null
  eda_tool: KiCad
  notes: Full KiCad project (schematic, PCB, footprints, gerbers, and an interactive BOM) is in the repo under SAO/NotCamera/Schematics; no firmware since the board has no MCU.
links:
- label: github.com/wrickert/RMABadge/tree/master/SAO/NotCamera
  url: https://github.com/wrickert/RMABadge/tree/master/SAO/NotCamera
  kind: repo
images:
- file: assets/images/badges/other/notcamera-sao-rma-badge/09bbb80e3f.jpg
  source: "https://github.com/wrickert/RMABadge/tree/master/SAO/NotCamera"
  credit: "wrickert"
  caption: "NotCamera SAO, front and back of the assembled board"
- file: assets/images/badges/other/notcamera-sao-rma-badge/5f9530cd04.jpg
  source: "https://github.com/wrickert/RMABadge/tree/master/SAO/NotCamera"
  credit: "wrickert"
  caption: "3D render of the NotCamera SAO PCB, styled as a small security camera"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: unknown
sources:
- kind: url
  url: https://github.com/wrickert/RMABadge/tree/master/SAO/NotCamera
  title: NotCamera SAO (RMA Badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/wrickert/RMABadge/tree/master/SAO/NotCamera/Schematics
  title: NotCamera KiCad schematics and gerbers
  accessed: '2026-09-07'
  note: 'Confirmed no MCU (passive transistor-flasher circuit), single LED, 6-pin SAO connector (Conn_02x03), SW1 switch; found full KiCad project including gerbers and an interactive BOM.'
- kind: url
  url: https://raw.githubusercontent.com/wrickert/RMABadge/master/SAO/NotCamera/Documents/NotCameraFrontBack.jpg
  title: NotCamera front/back photo
  accessed: '2026-09-07'
  note: Source photo for the saved front/back image; shows the camera-silhouette PCB shape and "This is not a Camera" silkscreen.
- kind: url
  url: https://github.com/wrickert/RMABadge/commits/master/SAO/NotCamera
  title: Commit history for SAO/NotCamera
  accessed: '2026-09-07'
  note: Commits from 2019-2022 touch this folder; a 2022 commit message "Re-started BsidesIA" is the only hint tying this repo's SAO work to BSides Iowa (Des Moines), but it is not specific enough to the NotCamera folder alone to set an event with confidence.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The GitHub repo (wrickert/RMABadge, "Repo for ongoing Badge work") has no README
    or project description beyond the file tree, so maker's-own-words context for why
    this SAO was made is thin. What's confirmed directly from the KiCad files: it's a
    6-pin ("v1.69bis"/v2) SAO with no microcontroller, a single reverse-mounted LED behind
    a gold "lens" pad driven by a two-transistor astable flasher, and a small switch.
    The repo otherwise centers on wrickert's BSidesIA (BSides Iowa/Des Moines) badge line
    and a "SecDSM" kit line, but nothing in the NotCamera folder or its commit messages
    states which specific con (if any) this SAO was made for or handed out at, so event
    is left as "other" rather than guessed. No store listing, price, quantity, or
    distribution info was found anywhere; get_one fields are left empty. No matching
    "BSides Iowa" / "BSides Des Moines" event exists in _data/events.yml to correct to
    even if the con link were confirmed.
last_modified_date: '2026-09-07'
---

The NotCamera SAO is a small joke PCB by the hobbyist maker wrickert (GitHub handle wrickert), shaped like the silhouette of a tiny dome security camera and silkscreened "This is not a Camera" on the front — a nod to Magritte's "this is not a pipe." Despite the name, it does have a functioning gimmick: a single LED sits behind a gold "lens" pad and blinks on its own, driven by a simple two-transistor astable flasher circuit rather than a microcontroller, so the "camera" appears to have a live status light.

It plugs into a host badge as a 6-pin SAO (the "v1.69bis"/v2 connector standard) and carries a small slide switch on the board. The project lives inside wrickert's larger `RMABadge` GitHub repository, a personal, multi-year archive of badge work ("Repo for ongoing Badge work") that also contains a full BSidesIA (BSides Iowa) badge line and a "SecDSM" kit line; a 2022 commit touching this folder is captioned "Re-started BsidesIA," but nothing in the NotCamera files themselves ties it to a specific convention, year, giveaway, or sale, so those details are left unconfirmed here.

The full KiCad design — schematic, PCB layout, footprints, gerbers, and an interactive BOM — is published in the repo under `SAO/NotCamera/Schematics` and `SAO/NotCamera/Footprints`, along with renders, an assembled front/back photo, and a couple of demo videos/GIFs showing the LED blinking.

## Make your own

- Schematic and PCB: `SAO/NotCamera/Schematics/NotCamera.sch` and `Camera.kicad_pcb` (KiCad).
- Footprints: `SAO/NotCamera/Footprints/NotCamera.pretty` (includes the custom "Camera" silhouette footprint).
- Fabrication files: ready-made gerbers and drill files are in `SAO/NotCamera/Schematics/gerbers/`.
- Bill of materials: an interactive BOM (`bom/ibom.html`) is included in the same folder.
