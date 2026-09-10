---
title: THEFREEMAN - DEF CON 26 Indie Badge
id: dc26-thefreeman-def-con-26-indie-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
summary: A passive, battery-powered indie badge shaped like a Vortigaunt (from Half-Life 2), with red and orange LEDs shining through the board to light up its eyes.
functions: No interactivity or MCU; the badge lights up via coin-cell power the moment a battery is installed, illuminating the Vortigaunt-style eyes.
look:
  colors:
  - green
  - red
  - orange
  shape: null
  themes:
  - pop culture
  - sci-fi
tech:
  mcu: none
  leds:
    count: 5
    type: discrete
    note: 3 red OSRAM T776-P2S1-1-Z and 2 orange OSRAM T776-Q2T1-24-Z LEDs, placed to shine through the PCB and light the eyes.
  display: none
  connectivity:
  - none
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ~40
  availability: sold_out
  availability_note: 'Checked 2026-09-07: Tindie listing shows "this product is no longer available for sale."'
  distribution:
  - purchase
  where: Sold via TwinkleTwinkie's Tindie store around DEF CON 26 (2018); included a green lobster-claw lanyard and 2 CR2032 batteries with the assembled badge.
make_your_own:
  open_source: true
  hardware_url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  firmware_url: null
  eda_tool: KiCad
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/thefreeman-def-con-26-indie-badge/
  title: THEFREEMAN - DEF CON 26 Indie Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc26''.'
- kind: url
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  title: THEFREEMAN - DEF CON 26 INDIE BADGE | Hackaday.io
  accessed: '2026-09-07'
  note: 'Maker''s project page: Vortigaunt theme, LED part numbers, KiCad/Gerber files, ~40 boards made, passive/no-MCU design.'
- kind: url
  url: https://hackaday.io/project/158663/log/146964-a-quick-summary
  title: A quick summary (project log)
  accessed: '2026-09-07'
  note: Confirms ~40 boards for DEF CON 26; notes it is the second board revision, added copper fill for grounding, removed an unneeded resistor to improve battery life, and mentions a misspelled Twitter handle on this run.
- kind: url
  url: https://hackaday.io/project/158663/files
  title: THEFREEMAN project files
  accessed: '2026-09-07'
  note: Lists two downloadable zips - "THE_FREEMAN_Badge_hackaday.zip" (KiCad/Gerbers for the badge) and "THE_FREEMAN_SAO_hackaday.zip" (KiCad/Gerbers for a matching SAO) - both free downloads, license not stated on the page.
images:
- file: assets/images/badges/dc26/thefreeman-def-con-26-indie-badge/796d295e58.jpg
  source: https://www.tindie.com/products/twinkletwinkie/thefreeman-def-con-26-indie-badge/
  credit: TwinkleTwinkie
  caption: THEFREEMAN badge lit up, showing the Vortigaunt-inspired glowing eyes
- file: assets/images/badges/dc26/thefreeman-def-con-26-indie-badge/60f3a6ff41.jpg
  source: https://www.tindie.com/products/twinkletwinkie/thefreeman-def-con-26-indie-badge/
  credit: TwinkleTwinkie
  caption: THEFREEMAN badge, unlit, showing PCB artwork
- file: assets/images/badges/dc26/thefreeman-def-con-26-indie-badge/312168004e.jpg
  source: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  credit: Twinkle Twinkie
  caption: THEFREEMAN indie badge, Vortigaunt-head PCB with reverse-mount LED eyes
  archived: https://web.archive.org/web/20260519083607/https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
contact: {}
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched both cited sources and confirmed every remaining sentence and field, including the "first DEF CON indie badge" and "learn KiCad / PCB as art medium" claims (direct quotes on the Hackaday.io project log). Corrected look.colors from [black, red, orange] to [green, red, orange] -- the saved photos show a green PCB, not black, and no source called it black. Corrected look.themes from "video games" (not in the guide''s vocabulary) to "pop culture". Both saved images were confirmed present on disk and show this badge on its Tindie listing. Core facts (maker, event, LED count/parts, battery, open-source status, ~40 units made) confirmed on the maker''s own Hackaday.io project page and Tindie store listing. Exact original price and precise quantity beyond "approximately 40" were not stated anywhere found. Merged with duplicate entry ''THEFREEMAN - DEF CON 26 Indie Badge'' (dc26-thefreeman-dc26-indie-badge).'
last_modified_date: '2026-09-07'
links:
- label: hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  url: https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260519083607/https://hackaday.io/project/158663-thefreeman-def-con-26-indie-badge
- label: hackaday.io/project/158663/log/146964-a-quick-summary
  url: https://hackaday.io/project/158663/log/146964-a-quick-summary
  kind: hackaday
- label: hackaday.io/project/158663/files
  url: https://hackaday.io/project/158663/files
  kind: hackaday
redirect_from:
- /badges/dc26/thefreeman-dc26-indie-badge/
---

THEFREEMAN is TwinkleTwinkie's first DEF CON indie badge, made for DEF CON 26 (2018). It is a passive, single-layer PCB badge shaped after the Vortigaunt aliens from Valve's Half-Life 2, with three red and two orange OSRAM SMD LEDs mounted so their light shines through the board and out the character's eyes. There is no microcontroller; a single CR2032 coin cell powers the LEDs directly. The maker built the project partly to learn KiCad and to treat the PCB itself as an art medium, and released the KiCad schematic and Gerber files for both a full badge and a smaller SAO version.

Roughly 40 boards were made and sold through TwinkleTwinkie's Tindie store, with the assembled badge shipping alongside a green lobster-claw lanyard and two CR2032 batteries meant to last the length of the conference. The listing is now retired and no longer available for purchase.

## Notes merged from the duplicate entry "THEFREEMAN - DEF CON 26 Indie Badge"

THEFREEMAN is an indie DEF CON 26 (2018) badge by Twinkle Twinkie, shaped like the Vortigaunt head from Half-Life 2. It's a deliberately single-layer PCB, used partly as a learning exercise in KiCad and partly as an experiment in treating a bare circuit board as an art medium - the absence of a second copper layer is what lets the board's traces and silkscreen read as the creature's face. Five reverse-mounted OSRAM TOPLED LEDs (three red, two orange) sit behind the board and shine through it to light the Vortigaunt's eyes, powered by a single CR2032 coin cell. About 40 were made for the con.

The project log describes this as the second board revision: the first prototype skipped a copper ground fill on purpose so the maker could understand the circuit before adding it back, and this run adds that fill along with removing an unnecessary resistor, which the maker says meaningfully improved battery life. The run wasn't perfect - the log notes a misspelled Twitter handle on the boards - and the maker mentions plans to share build lessons via video.

## Make your own

KiCad and Gerber files for the badge are posted as a free download on the Hackaday.io project's Files tab ("THE_FREEMAN_Badge_hackaday.zip"). A second archive on the same page, "THE_FREEMAN_SAO_hackaday.zip", holds KiCad/Gerber files for a matching SAO version of the same Vortigaunt-head design - it is not described as part of this badge and may be a separate item (see report).
