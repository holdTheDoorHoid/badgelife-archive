---
title: JoCo 2018 Badge (Pirate Monkey)
id: other-joco-2018-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: Open Research Institute
  url: https://github.com/OpenResearchInstitute
summary: An unofficial electronic badge built for JoCo Cruise 2018, adapting AND!XOR's DEF CON 25 "Bender" badge hardware and firmware into a pirate-monkey mascot design nicknamed "PirateMonkey" (firmware codename "manbearpig").
functions: Runs LED/LCD "bling" animations (regular, backer, and user-added "BYOB" modes loaded from an SD card) through a menu system inherited from the Bender badge. Includes an NFC reader/tag subsystem and a companion "Wall of JoCo" tool that logs badges tapped against a reader.
look:
  colors: []
  shape: null
  themes:
  - pirate
  - animal
  - mascot
tech:
  mcu: nRF52832
  leds:
    count: 14
    type: RGB
    note: 12 RGB LEDs in a 4x3 grid plus one dedicated "eye" LED and one "tooth" LED, per the repo's LED-Layout.md
  display: LCD (ZIF connector; same small color LCD approach as the AND!XOR Bender badge)
  connectivity:
  - nfc
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/OpenResearchInstitute/joco-2018-badge
  firmware_url: https://github.com/OpenResearchInstitute/joco-2018-badge
  eda_tool: KiCad
  license: Apache License 2.0
  notes: Board design files are under board/ (KiCad libraries plus an older "Eagle Libraries" folder, proto1/proto2 revisions with gerbers, and a Production BOM.pdf). Silkscreen artwork is credited "PirateMonkey" in the artwork/ folder. All files were embargoed until Feb 26, 2018, then released under Apache 2.0.
links:
- label: github.com/phase4ground/joco-2018-badge
  url: https://github.com/phase4ground/joco-2018-badge
  kind: repo
- label: github.com/OpenResearchInstitute/joco-2018-badge (canonical repo location)
  url: https://github.com/OpenResearchInstitute/joco-2018-badge
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- No matching event id exists in _data/events.yml for JoCo Cruise; event left as "other". The badge was made for JoCo Cruise 2018 (an annual cruise convention associated with musician Jonathan Coulton), not a hacker con.
- No photographs of an assembled/finished badge were found in the repo or via search; only PCB silkscreen artwork files (.BMP/.ai) and an NFC antenna design PNG were present, which are design files rather than photos of the item, so no images were saved.
- The README explicitly credits the design as based on the AND!XOR DEF CON 25 "Bender" badge; the bling/menu system, LCD approach, and file formats (RAW/PRV/ICO/RGB) are carried over from that project.
status: released
sources:
- kind: url
  url: https://github.com/phase4ground/joco-2018-badge
  title: joco-2018-badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''other (JoCo Cruise 2018, no matching event id)''.'
- kind: url
  url: https://github.com/OpenResearchInstitute/joco-2018-badge
  title: joco-2018-badge (OpenResearchInstitute, canonical org - phase4ground redirects here)
  accessed: '2026-09-07'
  note: Repo README, LED-Layout.md, Bling.md, and file listing confirmed maker, event, nRF52832 MCU, LED count/layout, NFC and LCD hardware, KiCad/Eagle design files, and Apache 2.0 licensing.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, chip, LED layout, NFC/LCD hardware, open-source status) come from the maker''s own repo. Could not find: price, quantity produced, distribution method, exact display size/part number, PCB color, or any photo of a finished/assembled unit. "phase4ground/joco-2018-badge" appears to be a fork or old link that now redirects to the OpenResearchInstitute org, which is treated here as the canonical source.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/joco-2018-badge.glb
  method: kicad
  source_file: board/proto1/proto1.kicad_pcb
  generated: '2026-09-10'
  bytes: 324036
---

An unofficial electronic badge built for JoCo Cruise 2018 by Open Research Institute, directly adapting the hardware and firmware of AND!XOR's DEF CON 25 "Bender" badge for a pirate-monkey mascot design the repo calls "PirateMonkey" (the firmware directory is named "manbearpig"). It runs on a Nordic nRF52832 and drives 14 LEDs — a 4x3 RGB grid plus a dedicated eye LED and tooth LED — alongside a small LCD wired through a ZIF connector, following the same screen approach as the Bender badge it was forked from.

The badge carries over the Bender badge's "bling" animation system: LED/LCD animation packages can be built into the firmware's menus, added as "backer" bling, or side-loaded from an SD card as "BYOB" (Bring Your Own Bling) content using RAW/PRV/ICO/RGB file formats. It also has an NFC subsystem, paired with a "Wall of JoCo" Python tool in the repo that logs badges as they're tapped against a reader — likely used to build a running roster of attendees at the event.

Hardware and firmware are fully open source under Apache License 2.0 (embargoed until February 26, 2018, per the README). The repo includes KiCad and older Eagle library files, two prototype board revisions with gerbers, a production BOM, and PCB silkscreen artwork credited to the "PirateMonkey" design. No information was found on price, production quantity, or how badges were distributed to cruise attendees, and no photos of an assembled unit turned up — only design files.

## Make your own

The repo is a complete build environment: install the Nordic nRF5 SDK v12.3.0 and the GNU ARM Embedded toolchain, set `SDK_ROOT`, then build with `cd firmware/manbearpig && make`. Flashing requires a Segger J-Link (a J-Link EDU Mini was used by the original team) and either `firmware/provision.sh` or `make flash_softdevice && make flash` from the firmware/manbearpig directory. Board design files (KiCad/Eagle, two proto revisions, gerbers, and a production BOM) are under `board/`.
