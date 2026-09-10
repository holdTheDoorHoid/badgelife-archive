---
title: Penguin Learn to Solder Badge
id: other-penguin-learn-to-solder-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2020
makers:
- name: Ayan Pahwa
  url: https://github.com/iayanpahwa
summary: An open-source PCB art badge designed as a beginner soldering practice piece, shaped like a penguin.
functions: 'A soldering-practice board: through-hole pads laid out over penguin artwork for beginners to solder. No onboard electronics function beyond the practice pads in the released version.'
look:
  colors:
  - black
  - white
  shape: penguin
  themes:
  - animal
  - bird
  - learn to solder
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Made for beginner soldering workshops at India Linux User Group Delhi and Hardware Hackers Club Delhi; not sold commercially as far as sources show.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/iayanpahwa/penguin-learn-to-solder-badge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/iayanpahwa/penguin-learn-to-solder-badge
  url: https://github.com/iayanpahwa/penguin-learn-to-solder-badge
  kind: repo
- label: OSHWA certification IN000014
  url: https://certification.oshwa.org/in000014.html
  kind: doc
  archived: https://web.archive.org/web/20251213170853/https://certification.oshwa.org/in000014.html
images:
- file: assets/images/badges/other/penguin-learn-to-solder-badge/71580afb99.jpg
  source: https://github.com/iayanpahwa/penguin-learn-to-solder-badge
  credit: Ayan Pahwa
  caption: Front of the Penguin Learn to Solder Badge PCB
- file: assets/images/badges/other/penguin-learn-to-solder-badge/6d8f5d240a.jpg
  source: https://github.com/iayanpahwa/penguin-learn-to-solder-badge
  credit: Ayan Pahwa
  caption: Back of the Penguin Learn to Solder Badge PCB
contact:
  email: codensolder@gmail.com
notes: []
status: released
sources:
- kind: url
  url: https://github.com/iayanpahwa/penguin-learn-to-solder-badge
  title: penguin-learn-to-solder-badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/iayanpahwa/penguin-learn-to-solder-badge
  title: GitHub README - penguin-learn-to-solder-badge
  accessed: '2026-09-07'
  note: Confirmed it was made for beginner soldering workshops at India Linux User Group Delhi and Hardware Hackers Club Delhi; KiCad v4 design; black solder mask/white silk recommended; through-hole, 555-blinky and SAO variants were listed as "coming soon" (not confirmed built).
- kind: url
  url: https://certification.oshwa.org/in000014.html
  title: OSHWA Certification IN000014
  accessed: '2026-09-07'
  note: Confirms maker name (Ayan Pahwa), certification date May 11 2020, and description as a "PCB Art soldering badge for workshops" from India.
  archived: https://web.archive.org/web/20251213170853/https://certification.oshwa.org/in000014.html
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Not made for a specific hacker convention; the repo and OSHWA record both describe it as made for beginner soldering workshops at two India-based hardware/Linux user groups (India Linux User Group Delhi, Hardware Hackers Club Delhi), so it is kept under the "other" event. Price, quantity made, and availability are not stated anywhere found. The repo lists through-hole, 555-timer blinky, and SAO versions as "coming soon" as of the README's last update, so tech.mcu/leds are left null since no built electronic variant is documented — only the plain PCB-art soldering-practice board is confirmed to exist (see Images/front.JPG, back.JPG in the repo).
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/penguin-learn-to-solder-badge.glb
  method: kicad
  source_file: KiCad/_autosave-Penguin_Learn_to_Solder_Badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 140156
---

The Penguin Learn to Solder Badge is an open-source PCB art badge made by Ayan Pahwa (GitHub: iayanpahwa) for beginner soldering workshops run by the India Linux User Group Delhi and the Hardware Hackers Club Delhi. It is OSHWA-certified (UID IN000014, certified May 11, 2020) and registered as a "PCB Art soldering badge for workshops."

The board is designed in KiCad v4 using the SVG2Shenzhen plugin to convert vector penguin artwork (a modified version of a Freepik illustration by Brgfx) into board outline and silkscreen art, and is recommended for fabrication in black solder mask with white silkscreen and ENIG-RHOS finish. The released design is a plain soldering-practice board; the maker's README lists a through-hole version, a 555-timer blinky circuit, and an SAO variant as planned future additions, but none of these are confirmed as completed in the sources found, so no MCU, LED, or SAO details are recorded here.

All design files (KiCad source, Gerbers, SVG artwork, and 3D models) are published in the GitHub repository under an open hardware license, making it a build-your-own resource for other groups running similar workshops.
