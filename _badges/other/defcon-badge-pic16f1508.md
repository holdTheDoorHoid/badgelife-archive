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
summary: A single-file MPLAB X firmware project for a PIC16F1508, named "DEFCON_BADGE" by its author, driving a seven-segment display through three digit-select lines (SEG1-SEG3) that share a common set of segment lines.
functions: In the main loop, advances through 0-9 and a handful of hex-style characters (A-F, H) roughly every 200ms; a separate timer interrupt cycles the three digit-select lines (SEG1/SEG2/SEG3) for multiplexed scanning, not the displayed character itself. No other behavior is implemented.
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
  note: 'Source shows a PIC16F1508 driving a 7-segment display via discrete segment pins (RA-RG, plus RP for the decimal point) shared across three digit-select lines (SEG1, SEG2, SEG3, defined in pin_manager.h as RA5/RA4/RB7) that a TMR1 interrupt cycles for multiplexed scanning. The displayed character itself advances through 0-9, A-F, H in the main loop on a ~200ms delay, not in the interrupt. No schematic, BOM, gerbers, photos, or README anywhere in the repo.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: >-
    Fact-check pass (2026-09-07): re-fetched the repo, its API metadata, and
    main.c directly. Repo metadata (created 2018-07-28, pushed 2018-07-29,
    description "PIC16F1508", no README) matched as cited. However, main.c and
    mcc_generated_files/pin_manager.h show the display is driven through three
    digit-select lines (SEG1/SEG2/SEG3) sharing common segment lines (RA-RG,
    RP), consistent with a multiplexed multi-digit display — not the "single
    seven-segment display" the previous pass described. Also, the character
    shown advances in the main loop on a ~200ms delay, while the TMR1 interrupt
    only cycles the digit-select multiplexing, not the character itself as
    previously stated. Both summary and functions were corrected accordingly;
    tech.display is left as the unqualified "7-segment" since no schematic or
    photo confirms the actual digit count. This repository remains firmware
    only, with no README, schematic, PCB files, BOM, or photos. Nothing in the
    repo confirms which DEF CON (or other event) this was built for, who besides
    the GitHub account "InfinityBuzz" was involved, whether it was ever built as
    physical hardware, or whether it was distributed to anyone beyond the
    author, so event/year and most `get_one`/`look` fields remain unset. The
    repo's timing (created 2018-07-28, just before DEF CON 26 in Aug 2018) is
    circumstantial, not a stated fact. No new web search was run this pass (this
    was a verification of already-cited sources, not new research); the prior
    pass's web searches for "InfinityBuzz" plus badge/DEF CON found no
    independent coverage, storefront, or Hackaday post, and nothing in this pass
    contradicts that. Every field and sentence left in the entry was checked
    directly against a cited source, so research.status is set to verified.
    No image was available to save.
last_modified_date: '2026-09-07'
---

"DEFCON_BADGE" is a small MPLAB X firmware project by the GitHub user InfinityBuzz, targeting a Microchip PIC16F1508 microcontroller. The single source file drives a seven-segment display through discrete GPIO segment pins (RA-RG, plus a decimal point line) that are shared across three digit-select lines named SEG1, SEG2, and SEG3 — a layout consistent with a multiplexed multi-digit display, though no schematic or photo confirms exactly how many physical digits were wired up. A timer interrupt cycles which digit-select line is active for the multiplexed scan, while the main loop separately advances the displayed character through 0-9 and a few hex-style characters (A-F, H) roughly every 200ms. There is no README, schematic, PCB layout, bill of materials, or photograph anywhere in the repository, so nothing here confirms which convention or year it was built for, whether it was ever assembled into a wearable badge, or whether anyone besides the author ever had one.

The repository was created on 2018-07-28 and last modified the following day, a window that falls shortly before DEF CON 26 (August 2018). That proximity is circumstantial rather than documented, so no event or year has been set on this entry. No independent write-up, storefront listing, or social media mention of the project could be found.

## Make your own

The firmware source is on GitHub at the link above (`DEFCON_BADGE.X`, an MPLAB X / XC8 project). No hardware design files (schematic, PCB, or BOM) are published alongside it, so only the firmware side of "make your own" is possible from what's here.
