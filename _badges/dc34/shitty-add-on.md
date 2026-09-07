---
title: defcon-34-shitty-add-on
id: dc34-shitty-add-on
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: narengogi
  url: https://github.com/narengogi
summary: 'A small single-LED Shitty Add-On shaped like an auto-rickshaw, designed for DEF CON 34.'
functions: 'Lights a single LED when plugged into a host badge''s SAO header; no other function evident.'
look:
  colors: []
  shape: rickshaw
  themes: []
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: 'One through-hole/SMD LED (schematic ref D1) with a single series resistor (R1); no driver IC.'
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
  open_source: partial
  hardware_url: https://github.com/narengogi/defcon-34-shitty-add-on
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/narengogi/defcon-34-shitty-add-on
  url: https://github.com/narengogi/defcon-34-shitty-add-on
  kind: repo
images: []
contact: {}
notes:
- 'No finished-board photos, storefront, or press coverage found; only design files are public.'
status: listed
sources:
- kind: url
  url: https://github.com/narengogi/defcon-34-shitty-add-on
  title: defcon-34-shitty-add-on
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 34''.'
- kind: url
  url: https://api.github.com/repos/narengogi/defcon-34-shitty-add-on/contents/Untitled
  title: 'GitHub API listing: Untitled/ (KiCad project + gerbers)'
  accessed: '2026-09-07'
  note: 'Repo contains a KiCad project (Untitled.kicad_sch/.kicad_pcb) and generated gerbers/drill files for a single small PCB.'
- kind: url
  url: https://raw.githubusercontent.com/narengogi/defcon-34-shitty-add-on/master/Untitled/Untitled.kicad_sch
  title: 'Untitled.kicad_sch (raw schematic)'
  accessed: '2026-09-07'
  note: 'Schematic shows exactly three components: a 6-pin SAO connector (Conn_02x03_Odd_Even, J1), one LED (D1), and one resistor (R1) — a passive single-LED SAO with no microcontroller.'
- kind: url
  url: https://raw.githubusercontent.com/narengogi/defcon-34-shitty-add-on/master/vectors/silk.svg
  title: 'vectors/silk.svg'
  accessed: '2026-09-07'
  note: 'Board art vectors are derived from an SVG Repo icon file named auto-rickshaw-svgrepo-com.svg, confirming the board is shaped/silkscreened as an auto-rickshaw (tuk-tuk).'
- kind: url
  url: https://api.github.com/repos/narengogi/defcon-34-shitty-add-on/commits
  title: 'Commit history'
  accessed: '2026-09-07'
  note: 'Single commit ("init"), dated 2026-07-24, ahead of DEF CON 34 (Aug 6-9, 2026); no further activity, issues, or releases.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'This appears to be a personal/hobby SAO design published on GitHub rather than a released or distributed product: no README, no storefront listing, no press coverage, no photos of an assembled board, and only a single "init" commit with design files (KiCad project, gerbers, and SVG art). Could not confirm it was ever fabricated, distributed, or handed out at DEF CON 34, or find price/quantity/availability. Hardware files (schematic, PCB, gerbers) are public in the repo, so open_source is marked partial; no firmware repo exists (design appears MCU-less). Maker''s GitHub profile (narengogi / Narendranath Gogineni) has no bio, blog, or other badge-related repos.'
last_modified_date: '2026-09-07'
---

This is a small Shitty Add-On (SAO) published on GitHub by narengogi, apparently designed for DEF CON 34 (2026) based on the repository name. The schematic shows a minimal, passive design: a standard 6-pin SAO header, a single LED, and one series resistor — no microcontroller, display, or other components. The board's silkscreen and outline art are derived from a stock "auto rickshaw" icon (credited to SVG Repo in the source files), giving the SAO its shape and theme: a small tuk-tuk-style vehicle.

The repository contains a complete KiCad project (schematic and PCB layout) along with generated Gerber and drill files, suggesting the board was laid out for fabrication, but there is no README, no photos of an assembled unit, no storefront or distribution listing, and no press or forum coverage to confirm it was actually built, handed out, or sold at DEF CON 34. The single commit is dated a couple of weeks before the con with no later updates, so its final status (built vs. design-only) could not be confirmed from available sources.

## Make your own

Hardware files are public: a KiCad schematic and PCB (`Untitled/Untitled.kicad_sch`, `Untitled.kicad_pcb`) plus ready-to-fab Gerbers and NC drill files in the same folder, and the source SVG artwork (silkscreen, mask, copper, edge-cuts layers) in the `vectors/` folder. No firmware is applicable since the design has no microcontroller; no license was stated in the repository.
