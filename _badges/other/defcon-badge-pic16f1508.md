---
title: DEFCON_BADGE (PIC16F1508)
id: other-defcon-badge-pic16f1508
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: InfinityBuzz
  url: https://github.com/InfinityBuzz
summary: A single-file MPLAB X firmware project for a PIC16F1508 driving a single seven-segment display, named "DEFCON_BADGE" by its author.
functions: Cycles a single seven-segment digit through 0-9 and a handful of hex-style characters on a timer interrupt; no other behavior is implemented.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: PIC16F1508
  leds: null
  display: 7-segment
  connectivity: []
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/InfinityBuzz/DEFCON_BADGE
  eda_tool: null
links:
- label: github.com/InfinityBuzz/DEFCON_BADGE
  url: https://github.com/InfinityBuzz/DEFCON_BADGE
  kind: repo
images: []
contact: {}
notes: []
status: unknown
sources:
- kind: url
  url: https://github.com/InfinityBuzz/DEFCON_BADGE
  title: DEFCON_BADGE (PIC16F1508)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://api.github.com/repos/InfinityBuzz/DEFCON_BADGE
  title: InfinityBuzz/DEFCON_BADGE - repo metadata
  accessed: '2026-09-07'
  note: 'Repo created 2018-07-28, last pushed 2018-07-29; description field just reads "PIC16F1508"; no README.'
- kind: url
  url: https://raw.githubusercontent.com/InfinityBuzz/DEFCON_BADGE/master/DEFCON_BADGE.X/main.c
  title: DEFCON_BADGE.X/main.c
  accessed: '2026-09-07'
  note: 'Source shows a PIC16F1508 driving one 7-segment display via discrete port pins (RA-RG), cycling through 0-9, A-F, H on a TMR1 interrupt. No schematic, BOM, gerbers, photos, or README anywhere in the repo.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    This repository is firmware only (an MPLAB X / XC8 project for a PIC16F1508
    driving a single 7-segment display) with no README, schematic, PCB files, BOM,
    or photos. There is nothing in the repo or findable online that confirms which
    DEF CON (or other event) this was built for, who besides the GitHub account
    "InfinityBuzz" was involved, whether it was ever built as physical hardware,
    or whether it was distributed to anyone beyond the author. The repo was created
    2018-07-28 and last touched 2018-07-29, which sits just before DEF CON 26
    (Aug 2018), but that is timing coincidence, not a stated fact, so event/year
    are left unset. Web searches for "InfinityBuzz" plus badge/DEF CON turned up
    no independent coverage, storefront, or Hackaday post. Given the complete
    absence of a physical product, a distribution channel, or an image of the
    item, this reads more like a personal firmware sketch than a badge that
    reached other people; leaving type as badge as most items in this archive
    do, but confidence is low across the board and most fields are left empty
    rather than guessed. No image was available to save.
last_modified_date: '2026-09-07'
---

"DEFCON_BADGE" is a small MPLAB X firmware project by the GitHub user InfinityBuzz, targeting a Microchip PIC16F1508 microcontroller. The single source file drives one seven-segment display through discrete GPIO pins, cycling it through the digits 0-9 and a few hex-style characters (A-F, H) once per timer tick. There is no README, schematic, PCB layout, bill of materials, or photograph anywhere in the repository, so nothing here confirms which convention or year it was built for, whether it was ever assembled into a wearable badge, or whether anyone besides the author ever had one.

The repository was created on 2018-07-28 and last modified the following day, a window that falls shortly before DEF CON 26 (August 2018). That proximity is circumstantial rather than documented, so no event or year has been set on this entry. No independent write-up, storefront listing, or social media mention of the project could be found.

## Make your own

The firmware source is on GitHub at the link above (`DEFCON_BADGE.X`, an MPLAB X / XC8 project). No hardware design files (schematic, PCB, or BOM) are published alongside it, so only the firmware side of "make your own" is possible from what's here.
