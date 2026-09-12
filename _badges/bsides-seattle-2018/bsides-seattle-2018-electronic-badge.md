---
title: BSides Seattle 2018 electronic badge
id: bsides-seattle-2018-bsides-seattle-2018-electronic-badge
layout: badge
parent: BSides Seattle 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-seattle-2018
year: 2018
makers:
- name: Black Lodge Research
  url: https://github.com/BlackLodgeResearch
summary: An ATmega328P-based electronic badge built for BSides Seattle 2018's Hardware Hacking Village, distributed to over 470 participants.
functions: Runs an Arduino sketch on assembly; a community-contributed enhanced firmware adds extra features on top of the basic build.
look:
  colors: []
  shape: null
  themes:
  - village badge
  - learn to solder
  - hardware tool
tech:
  mcu: ATmega328P
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
  distribution:
  - village
  where: Distributed through the Hardware Hacking Village at BSides Seattle 2018.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/BlackLodgeResearch/bsides_2018_badge
  firmware_url: https://github.com/BlackLodgeResearch/bsides_2018_badge
  eda_tool: null
links:
- label: www.bsidesseattle.com/history.html
  url: https://www.bsidesseattle.com/history.html
  kind: website
  archived: https://web.archive.org/web/20260622143130/https://www.bsidesseattle.com/history.html
- label: BlackLodgeResearch/bsides_2018_badge
  url: https://github.com/BlackLodgeResearch/bsides_2018_badge
  kind: repo
images: []
contact: {}
notes:
- The con's own history page states new electronic badges were introduced in 2018 and integrated with the Hardware Hacking Village for over 470 participants; no maker or design specifics given beyond that. Found by the event-year sweep, task bsides-las-vegas.
- The sweep's notes field described only what the con's history page said; the maker and hardware details below came from a separate GitHub repo (BlackLodgeResearch/bsides_2018_badge) found via search, which is presumed to be the same 2018 badge given the matching event, year, and Hardware Hacking Village hand-off. Eagle schematic file present but not fetched for further tech.mcu confirmation beyond what the README states.
status: released
sources:
- kind: url
  url: https://www.bsidesseattle.com/history.html
  title: BSides Seattle 2018 electronic badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-las-vegas); event read as ''BSides Seattle 2018''.'
  archived: https://web.archive.org/web/20260622143130/https://www.bsidesseattle.com/history.html
- kind: url
  url: https://github.com/BlackLodgeResearch/bsides_2018_badge
  title: BlackLodgeResearch/bsides_2018_badge
  accessed: '2026-09-10'
  note: Repo README and file listing; identifies the maker (Black Lodge Research), MCU (ATmega328P), Eagle schematic, Arduino sketches, and a build guide docx.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: No LED count, display, price, or quantity-made figures found in any source; the "over 470 participants" figure describes village attendance, not units produced. No photo of the assembled badge was found in the repo (only schematic/sketch/docx files, no image assets) or elsewhere, so no images could be saved. Maker attribution rests on the repo matching event/year/village context rather than an explicit statement tying Black Lodge Research to BSides Seattle by name.
last_modified_date: '2026-09-10'
---

BSides Seattle introduced its first electronic conference badge in 2018, built around an ATmega328P microcontroller (the same chip used in classic Arduino boards) and distributed through the con's Hardware Hacking Village, which that year drew over 470 participants.

Design files for the badge were published on GitHub by Black Lodge Research: an Eagle schematic for the PCB, a basic Arduino sketch (`b_sides_2018.ino`), an enhanced firmware variant contributed by a community member (`BSides_Seattle-2018.ino`, credited to @pandatrax), and a Word document build guide walking through assembly. No details on LED count, display, price, or units produced were found in any available source.

## Make your own

The hardware and firmware are on GitHub at [BlackLodgeResearch/bsides_2018_badge](https://github.com/BlackLodgeResearch/bsides_2018_badge): open `badge_schematic.sch` in Eagle for the PCB design, flash either `.ino` sketch to an ATmega328P with the Arduino IDE, and follow `Badge_Build_Guide.docx` for assembly steps.
