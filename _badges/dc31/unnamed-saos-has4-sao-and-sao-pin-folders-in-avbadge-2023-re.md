---
title: Unnamed SAOs (HAS4_SAO and SAO_pin folders in avBadge_2023 repo)
id: dc31-unnamed-saos-has4-sao-and-sao-pin-folders-in-avbadge-2023-re
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Aerospace Village
  url: https://github.com/AerospaceVillage
summary: 'Two small SAO designs from the Aerospace Village''s DEF CON 31 badge repo: HAS4_SAO, a 6-pin add-on with two LEDs, battery holder and switch, and SAO_pin, a near-identical board without the LEDs.'
functions: HAS4_SAO lights two LEDs, switched on/off, powered by its own coin cell rather than the host badge. SAO_pin appears to be the same battery-and-switch board without any LEDs (a wearable pin form rather than a lit add-on).
look:
  colors: []
  shape: null
  themes:
  - space
tech:
  mcu: none
  leds:
    count: 2
    type: null
    note: HAS4_SAO schematic includes two Device:LED symbols (D1, D2) with two resistors (R1, R2), a coin-cell holder and an SPDT switch. SAO_pin's schematic has the battery holder and switch but no LEDs or resistors.
  display: null
  connectivity: []
  battery: coin cell (Battery_Cell footprint, on-board, not powered from the host badge)
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/HAS4_SAO
  firmware_url: null
  eda_tool: KiCad
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'The avBadge_2023 repo also contains three other, separate SAO folders not covered by this entry: "crew SAO", "space_shuttle_SAO", and "speaker SAO" — each looks like its own item and is reported separately below.'
- HAS4 refers to Hack-A-Sat 4, the space-CTF competition (using Aerospace's Moonlighter satellite) that the Aerospace Village ran at DEF CON 31; this SAO appears to commemorate that event, though no page or README states this explicitly.
- No repo README, project page, or press coverage describes either board by name; there are no photos of the assembled boards, only KiCad source files and a footprint/SVG art asset for HAS4_SAO ("HAS4_bug.svg").
status: unknown
sources:
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2023/tree/main/HAS4_SAO
  title: Unnamed SAOs (HAS4_SAO and SAO_pin folders in avBadge_2023 repo)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc31''.'
- kind: url
  url: https://raw.githubusercontent.com/AerospaceVillage/avBadge_2023/main/README.md
  title: AerospaceVillage/avBadge_2023 README
  accessed: '2026-09-07'
  note: 'One-line repo description: badges + a number of SAOs the Village made for DEF CON 2023.'
- kind: url
  url: https://raw.githubusercontent.com/AerospaceVillage/avBadge_2023/main/HAS4_SAO/HAS4_SAO.kicad_sch
  title: HAS4_SAO.kicad_sch (schematic source)
  accessed: '2026-09-07'
  note: 'Confirms components: 6-pin SAO connector, coin-cell holder, SPDT switch, two LEDs (D1, D2), two resistors (R1, R2).'
- kind: url
  url: https://raw.githubusercontent.com/AerospaceVillage/avBadge_2023/main/SAO_pin/SAO_pin.kicad_sch
  title: SAO_pin.kicad_sch (schematic source)
  accessed: '2026-09-07'
  note: Same connector, coin-cell holder and switch as HAS4_SAO, but no LED or resistor components in the schematic.
- kind: url
  url: https://www.aerospacevillage.org/defcon-31
  title: DEF CON 31 (2023) | Aerospace Village
  accessed: '2026-09-07'
  note: DEF CON 31 event page for the Aerospace Village; no mention of these SAOs specifically.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: Only source is the repo itself (KiCad design files); no README section, project page, forum post, or storefront names either board, so title, price, quantity, availability, colors, and distribution could not be filled in. Confirmed from the schematics that both boards use a 6-pin SAO connector, an on-board coin cell, and an SPDT switch, and that HAS4_SAO alone adds two LEDs (D1, D2) and two resistors (R1, R2) — the researcher's prior write-up said "one LED and one resistor," which the raw schematic source contradicts; corrected on fact-check by reading the file directly rather than a page summary. "v1.69bis" is inferred from the 6-pin header plus a "badgelife_shitty_addon_v169bis.lib" symbol library sitting in the HAS4_SAO folder (not actually wired into the placed connector symbol, which is a generic KiCad part) — plausible but not stated outright, so kept as a low-confidence read. "HAS4" plausibly ties to the Village's Hack-A-Sat 4 CTF at DEF CON 31, but no source states this
    link outright, so it is noted as a guess only.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc31/unnamed-saos-has4-sao-and-sao-pin-folders-in-avbadge-2023-re.glb
  method: kicad
  source_file: HAS4_SAO/HAS4_SAO.kicad_pcb
  generated: '2026-09-07'
  bytes: 70508
---

The avBadge_2023 repository, published by the DEF CON Aerospace Village for its 2023 (DEF CON 31) badges, includes two small SAO (add-on) designs that were never named or documented beyond their folder names: `HAS4_SAO` and `SAO_pin`. Both share the same basic layout — a 6-pin SAO connector, an on-board coin-cell battery holder, and an SPDT switch — but HAS4_SAO adds two LEDs and their current-limiting resistors that SAO_pin's schematic does not have. Neither is described in the repo's README, which only says the project "contains a number of SAOs the Village is making" alongside its two main badges, "The Wright Flyer" and "The Wright Stuff."

The name HAS4 likely nods to Hack-A-Sat 4, the space-focused CTF the Aerospace Village ran at DEF CON 31 using Aerospace Corporation's Moonlighter satellite test platform, but no source directly ties this SAO to that competition — it is a plausible reading of the folder name, not a confirmed fact. No photos, project write-ups, price, quantity, or distribution details for either board could be found; only the raw KiCad schematic, PCB, and library files are in the repository, along with a footprint and SVG art file ("HAS4_bug") for HAS4_SAO's silkscreen.

## Make your own

Both boards' full KiCad source (schematic, PCB, project, and footprint library files) is in the repo, so it is open-source at least on the hardware side: [HAS4_SAO](https://github.com/AerospaceVillage/avBadge_2023/tree/main/HAS4_SAO) and [SAO_pin](https://github.com/AerospaceVillage/avBadge_2023/tree/main/SAO_pin). No firmware is present for either (neither has an MCU in its schematic), and no rendered gerbers or fab-house share links were found — the `gerbers` and `gerbers_zipped` subfolders exist but were not checked file-by-file.
