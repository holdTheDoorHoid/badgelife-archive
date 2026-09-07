---
title: mirror-minibadge — infinity mirror minibadge
id: saintcon-2023-mirror-minibadge-infinity-mirror-minibadge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: JonDegn
  url: https://github.com/JonDegn
summary: 'A SAINTCON 2023 minibadge by Jonathon Degn: a square 3D-printed frame with a two-way mirror and window film over 8 white LEDs, creating an infinity-mirror effect. 30 were made.'
functions: 'Lights up 8 white LEDs behind a mirror and reflective window film to create an infinity-mirror effect when powered.'
look:
  colors:
  - black
  shape: square
  themes:
  - minibadge
tech:
  mcu: 'none'
  leds:
    count: 8
    type: 'discrete'
    note: '8x 1206 white LEDs, each with its own 82Ω resistor (no driver chip).'
  display: 'none'
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 30
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: github.com/JonDegn/mirror-minibadge
  url: https://github.com/JonDegn/mirror-minibadge
  kind: repo
- label: github.com/JonDegn/Saintcon2023-minibages (infinity-mirror build guide)
  url: https://github.com/JonDegn/Saintcon2023-minibages/tree/main/infinity-mirror
  kind: repo
- label: 'Infinity Mirror minibadge build guide (Saintcon 2023) — YouTube'
  url: https://www.youtube.com/watch?v=Mz0T67Czk88
  kind: video
images:
- file: assets/images/badges/saintcon-2023/mirror-minibadge-infinity-mirror-minibadge/d0815eb98b.png
  source: "https://github.com/JonDegn/Saintcon2023-minibages/blob/main/infinity-mirror/readme.md"
  credit: "JonDegn (Jonathon Degn)"
  caption: "Assembled infinity mirror minibadge, powered on, showing the mirrored LED reflection"
contact: {}
notes:
- 'The maker''s repo named directly on the community sheet (github.com/JonDegn/mirror-minibadge) is only a placeholder ("Instructions coming...", single commit 2023-09-18) and was never filled in. The actual build guide, photo, parts list, and video live in a second repo on the same GitHub account, github.com/JonDegn/Saintcon2023-minibages, under an "infinity-mirror" subfolder, alongside four other SAINTCON 2023 minibadges by the same maker (delicate-arch, elizabeth-butterfly, emily-robot, lego-spaceman) — each may deserve its own entry.'
status: released
sources:
- kind: url
  url: https://github.com/JonDegn/mirror-minibadge
  title: mirror-minibadge — infinity mirror minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''SAINTCON 2023''.'
- kind: url
  url: https://github.com/JonDegn/mirror-minibadge
  title: 'JonDegn/mirror-minibadge: Instructions on assembling the infinity mirror minibadge for Saintcon 2023'
  accessed: '2026-09-07'
  note: 'Verified via GitHub API: repo description and single commit ("Create readme.md", 2023-09-18) confirmed. readme.md content decodes to "# Infinity Mirror Minibadge / Instructions coming..." — this repo is indeed just a placeholder, as the prior research pass found.'
- kind: url
  url: https://github.com/JonDegn/Saintcon2023-minibages/tree/main/infinity-mirror
  title: 'JonDegn/Saintcon2023-minibages — infinity-mirror build guide'
  accessed: '2026-09-07'
  note: 'A second, separate repo on the same maker''s account (not previously found), listed on JonDegn''s GitHub profile with the description "Instructions and resources on my minibadge designs for Saintcon 2023." Its infinity-mirror/readme.md gives a full build guide: "30 produced," a materials list (8x 1206 white LED, 8x 1206 82Ω resistor, 1x 2cm acrylic, 1x 2cm mirror, 1x reflective window film, 4x 2-pin header), assembly steps, a warning about reversed polarity, and a photo of the finished badge (square black 3D-printed frame, LEDs reflected in a mirror). This directly contradicts the prior pass''s conclusion that "no images, specs, price, or design files were ever published."'
- kind: url
  url: https://www.youtube.com/watch?v=Mz0T67Czk88
  title: 'Infinity Mirror minibadge build guide (Saintcon 2023) - YouTube (oEmbed)'
  accessed: '2026-09-07'
  note: 'Confirmed via YouTube oEmbed API that the video linked from the build guide exists, is titled "Infinity Mirror minibadge build guide (Saintcon 2023)," and is by a channel called "Kingbob" (not independently tied to JonDegn, but the title matches this exact badge).'
- kind: url
  url: https://github.com/JonDegn
  title: JonDegn (Jonathon Degn) GitHub profile
  accessed: '2026-09-07'
  note: 'Re-checked via GitHub API. The prior pass said this profile showed "none" for other SAINTCON/badgelife work, but the profile in fact lists Saintcon2023-minibages ("Instructions and resources on my minibadge designs for Saintcon 2023") right alongside mirror-minibadge — that repo was missed, not absent.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Corrected a fact-check failure in the prior pass: it checked only the placeholder mirror-minibadge repo and missed a second repo on the same GitHub account (Saintcon2023-minibages) that holds the real build guide, parts list, quantity (30 made), and a photo for this exact badge, even though that repo is listed on the maker''s profile under a matching description. Filled in functions, tech.leds, quantity, a photo, and two new source links from that guide. Left mcu as none (no driver chip described - LEDs and resistors are wired directly), display as none, and sao_version/connectivity/battery/price/availability/open_source empty because the guide describes 4x plain 2-pin headers (not a documented SAO or standard power spec) and never states price, sale channel, or whether hardware files (as opposed to an assembly write-up) are published. Four sibling minibadges from the same maker/repo (delicate-arch, elizabeth-butterfly, emily-robot, lego-spaceman) were noticed but not researched, per scope; flagged in notes and other_items_found for a separate pass.'
last_modified_date: '2026-09-07'
---

The infinity mirror minibadge is a SAINTCON 2023 minibadge by Jonathon Degn (JonDegn), part of the con's tradition of small pluggable add-on badges ("minibadges"). The maker made 30 of them. It is a square, 3D-printed frame holding a piece of acrylic backed with reflective mirror film on one side and one-way window film on the other, with 8 white 1206 LEDs (each on its own 82Ω resistor, no driver chip) arranged around the edge on a small PCB. Powered on, the LEDs bounce between the mirror and the film to produce a classic "infinity tunnel" of receding lights.

The maker's most-visible repo for this badge, `mirror-minibadge`, never grew past a placeholder readme ("Instructions coming...") posted September 18, 2023. The actual documentation lives in a separate repo on the same account, `Saintcon2023-minibages`, which collects build guides for five SAINTCON 2023 minibadges Jonathon Degn made that year. Its infinity-mirror page gives a full parts list, step-by-step assembly instructions (including a warning that the badge is easy to plug in upside-down, since all four sides look alike), a photo of the finished piece, and a link to a build-guide video on YouTube.

## Make your own

The build guide at [github.com/JonDegn/Saintcon2023-minibages/tree/main/infinity-mirror](https://github.com/JonDegn/Saintcon2023-minibages/tree/main/infinity-mirror) walks through soldering 2 LEDs to each of 4 frame boards, soldering 8 resistors and headers to the main board, gluing the frame around a mirror-and-film sandwich, and fitting the assembly into a 3D-printed frame. No schematic, PCB design files, or gerbers are linked — only the written guide, parts list, and a companion [video](https://www.youtube.com/watch?v=Mz0T67Czk88).
