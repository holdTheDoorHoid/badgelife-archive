---
title: DCNextGen 2025 IR CTF Wristband
id: dc33-bradan-lane-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
series: DCNextGen
makers:
- name: Bradán Lane
  url: https://gitlab.com/bradanlane
summary: 'A wearable wristband badge for the DCNextGen program at DEF CON 33 that doubles as the key to a scavenger-hunt-style CTF: it transmits and receives an identity over IR, tallies points on a 12-LED score card, and gives audio/RGB feedback through two buttons.'
functions: Transmits its identity over IR; receives other badges' identities over IR and tallies points; shows collected identities and total score on the green Score Card LEDs and via buzzer tones; left button shows/transmits identity, right button shows score/listens for others; long presses sound out collected identities or the full score; hidden admin mode for setting badge type/value and factory reset; serial console for admin functions plus raw IR send/receive.
look:
  colors:
  - green
  shape: null
  themes:
  - ctf
  - wearable
  - village badge
  - puzzle
  form_factor: pcb badge
tech:
  mcu: ATtiny1616
  leds:
    count: 14
    type: discrete
    note: 12 green 'Score Card' LEDs plus two RGB LEDs (RGB1 near top center, RGB2 on the left edge).
  display: none
  connectivity:
  - ir
  - uart
  inputs:
  - buttons
  power: CR2032
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed to DCNextGen participants, staff, and villages at DEF CON 33 (Las Vegas, August 2025); the README does not say it was sold.
make_your_own:
  open_source: true
  hardware_url: https://gitlab.com/bradanlane/dcng02/-/tree/main/hardware
  firmware_url: https://gitlab.com/bradanlane/dcng02
  eda_tool: KiCad
  license: MIT
  notes: hardware/ has a KiCad project (project.kicad_pcb, project.kicad_sch) plus rendered schematic.pdf and pcb.pdf. files/ has a STEP model of the 3D-printed case ('dcng wrist badge.step') and renders. badge/ has the printed badge/info-sheet PDFs (DCNG_DC33-badge.pdf, badge_info_sheet.pdf). No separate firmware source folder was found in the repository tree; only hardware, files, badge and workshops directories are present.
links:
- label: GitLab repo (hardware, docs, renders)
  url: https://gitlab.com/bradanlane/dcng02
  kind: repo
- label: Maker's link page
  url: https://bradanlane.com
  kind: website
images:
- file: assets/images/badges/dc33/bradan-lane-listed-for-def-con-33-no-details/a91fba0c04.png
  source: https://gitlab.com/bradanlane/dcng02
  credit: Bradán Lane
  caption: Rendering of the DCNextGen 2025 IR CTF Wristband PCB
- file: assets/images/badges/dc33/bradan-lane-listed-for-def-con-33-no-details/2271dbcfa9.jpg
  source: https://gitlab.com/bradanlane/dcng02
  credit: Bradán Lane
  caption: Render of the assembled wristband with 3D-printed case and strap
contact: {}
notes:
- Sheet listed only the maker's name for DC33 with no other details; this entry was retitled after finding the maker's DCNextGen wristband project for that year.
status: released
sources:
- kind: sheet
  event: dc33
  row: 22
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://gitlab.com/bradanlane/dcng02
  title: DCNG02 (DCNextGen 2025 IR CTF Wristband) - GitLab
  accessed: '2026-09-06'
  note: 'Full README: what the badge is, PCB anatomy, ATtiny1616 MCU, CR2032 power, LED layout, button functions, scoring system, admin mode, serial console commands. Created 2025-07-11, MIT license.'
- kind: url
  url: https://gitlab.com/bradanlane/dcng02/-/raw/main/badge/badge_info_sheet.pdf
  title: badge_info_sheet.pdf
  accessed: '2026-09-06'
  note: One-page quick reference for the two buttons; confirms button function names but adds no price/quantity/distribution details.
- kind: url
  url: https://bradanlane.com
  title: Bradán Lane - link directory
  accessed: '2026-09-06'
  note: Maker's personal link page (studio, GitLab, Tindie, social); did not itself mention the DC33 project by name.
- kind: url
  url: https://hackaday.io/BradanLane
  title: Bradán Lane - Hackaday.io
  accessed: '2026-09-06'
  note: Only project listed is 'Pocket Enigma' (2022); no DC33 project posted there.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'The community sheet listed only the maker''s name with no title for DC33. Found the item via the maker''s GitLab account (gitlab.com/bradanlane): a repository named DCNG02 created 2025-07-11, whose README identifies it as ''DCNextGen 2025 IR CTF Wristband'' for DEF CON 33. Retitled the entry accordingly (id/filename left unchanged per instructions). Hardware (KiCad schematic/PCB) and a 3D-printed case STEP file are published under MIT; no firmware source directory was found in the repo tree (only hardware/, files/, badge/, workshops/), so firmware_url points at the repo root and open_source is marked yes on the strength of the hardware being complete and the license covering the whole repo, but firmware source itself was not located. Price, quantity, and exact distribution mechanics (e.g. whether DCNextGen registration was required) are not stated anywhere found; get_one.price/quantity left empty rather than guessed. Tindie store (tindie.com/stores/bradanlane) and a Google/DuckDuckGo
    web search were blocked by Cloudflare/CAPTCHA and a search-engine block respectively, so could not check for a listed sale price there. LED count of 14 (12 Score Card + 2 RGB) is read directly from the README anatomy section; look.shape left null since no straight-on photo of the assembled wristband''s outline was reviewed beyond the renders already saved.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc33/bradan-lane-listed-for-def-con-33-no-details.glb
  method: kicad
  source_file: hardware/project.kicad_pcb
  generated: '2026-09-07'
  bytes: 226136
---

The DCNextGen 2025 IR CTF Wristband is a wearable badge Bradán Lane built for the DCNextGen program at DEF CON 33 in August 2025. Rather than a traditional standalone badge, it is the access token for a scavenger-hunt-style capture-the-flag: participants, staff ("goons"), villages, and special activity badges each broadcast a distinct identity over infrared, and wristbands earn points by receiving identities from other wristbands they meet. A row of 12 green "Score Card" LEDs plus two RGB LEDs communicate collected identities and running score, with a buzzer sounding out tunes and digit counts for players who prefer audio feedback to reading LEDs.

The PCB is built around a Microchip ATtiny1616, runs from a single CR2032 coin cell, and is protected inside a 3D-printed PETG case worn on a color-coded velcro strap (green for players, red for staff, blue for villages, yellow for the special/activity badge, black for a rare bonus badge). Two buttons drive nearly all the functionality: a left "identity" button shows and transmits the wristband's own identity, and a right "score" button shows the total score and listens for incoming IR transmissions. A hidden button-sequence unlocks an admin mode for reassigning a wristband's type and value or factory-resetting it, and a serial console exposed on an edge header adds the same controls plus raw IR send/receive commands, useful for testing against DC32's earlier "DCNextGen Graffiti Badge."

Hardware design files (KiCad schematic and PCB, plus a STEP model of the 3D-printed case) are published on the maker's GitLab under an MIT license. No price, production quantity, or details of exactly how wristbands were handed out to DCNextGen participants were found in the repository or the maker's other public pages.

## Make your own

The `bradanlane/dcng02` GitLab repository (MIT licensed) has everything needed to reproduce the PCB: `hardware/project.kicad_pcb` and `hardware/project.kicad_sch` are the KiCad source files, with rendered `schematic.pdf` and `pcb.pdf` copies alongside them. The `files/` directory has a STEP model of the 3D-printed case for reproducing it on a printer, plus rendered images of the finished board and wristband. A firmware source directory was not found in the repository tree that was inspected; only `hardware/`, `files/`, `badge/`, and `workshops/` are present, so building your own would require writing firmware for the ATtiny1616 from the README's documented button and IR behavior.
