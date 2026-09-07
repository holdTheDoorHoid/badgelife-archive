---
title: DC32-SAO
id: dc32-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: Cyber Professionals Enthusiast Club
  url: https://github.com/Cyber-Professionals-Enthusiast-Club
summary: A simple passive SAO with five red flashing LEDs, published as open KiCad design files by the Cyber Professionals Enthusiast Club (CPEC) for DEF CON 32.
functions: Five discrete 3mm red flashing LEDs light up when plugged into a badge's SAO header; no microcontroller or programmable behavior.
look:
  colors: [red]
  shape: null
  themes: [minimalist]
tech:
  mcu: none
  leds:
    count: 5
    type: discrete
    note: 3mm round-top red flashing LEDs (self-flashing, no driver needed), each with a 510 ohm series resistor
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC32-SAO
  firmware_url: null
  gerbers_url: null
  bom_url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC32-SAO/blob/main/README.md
  eda_tool: KiCad
  license: null
  fab_url: null
  notes: KiCad schematic and PCB files (plus a panelized variant) are in the repo; no license file is present and no firmware is needed since the board is a passive LED circuit.
links:
- label: github.com/Cyber-Professionals-Enthusiast-Club/DC32-SAO
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC32-SAO
  kind: repo
- label: Cyber Professionals Enthusiast Club (GitHub org)
  url: https://github.com/Cyber-Professionals-Enthusiast-Club
  kind: repo
images:
- file: assets/images/badges/dc32/sao/33ffa2bba6.jpg
  source: "https://github.com/Cyber-Professionals-Enthusiast-Club/DC32-SAO"
  credit: "Cyber Professionals Enthusiast Club"
  caption: "DC32-SAO board, KiCad render"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://github.com/Cyber-Professionals-Enthusiast-Club/DC32-SAO
  title: DC32-SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc32''.'
- kind: url
  url: https://raw.githubusercontent.com/Cyber-Professionals-Enthusiast-Club/DC32-SAO/main/README.md
  title: DC32-SAO README (bill of materials)
  accessed: '2026-09-07'
  note: Confirms 5x 3mm red flashing LEDs, 5x 510 ohm resistors, 1x PH2-06-UA 6-pin connector; source of the board photo.
- kind: url
  url: https://api.github.com/repos/Cyber-Professionals-Enthusiast-Club/DC32-SAO
  title: DC32-SAO repository metadata
  accessed: '2026-09-07'
  note: Confirmed no license file is present in the repo.
- kind: url
  url: https://github.com/orgs/Cyber-Professionals-Enthusiast-Club/repositories
  title: Cyber-Professionals-Enthusiast-Club organization repositories
  accessed: '2026-09-07'
  note: Maker's org also built DEF CON 34 badge/SAO projects (DC-34-Badge, DC-34-Mech-SAO, etc.); no separate DC32 press coverage found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The repo (KiCad files + BOM) is the only source found; no press coverage, storefront listing, price, quantity, or distribution details turned up in web searches. Treated as released since the design and BOM are finished/published, but there is no confirmation people actually received it at DC32.
last_modified_date: '2026-09-07'
---

The DC32-SAO is a small, purely passive Shitty Add-On built by the Cyber Professionals Enthusiast Club (CPEC) for DEF CON 32 in 2024. It has no microcontroller: five 3mm red flashing LEDs, each wired through its own 510-ohm resistor, light up as soon as the board is powered through a standard 6-pin SAO connector plugged into a host badge. The maker published complete KiCad schematic and PCB files for both a single board and a panelized version, but did not attach a license, and no build guide, storefront listing, or price/quantity information was found alongside the repository.

CPEC is a badge-making group that also produced DEF CON 34 hardware (a full badge, mech-themed SAO "weapons," and demo firmware for a hot-pluggable SAO concept), suggesting the DC32-SAO was an earlier, simpler outing before their later, more elaborate projects.

## Make your own

The repository (github.com/Cyber-Professionals-Enthusiast-Club/DC32-SAO) contains the KiCad 6 schematic and PCB layout for both the standard board and a panelized variant. The bill of materials is three line items: five CF14JT510R 510-ohm resistors, five 3mm round-top red flashing LEDs, and one PH2-06-UA 6-pin connector for the SAO header.
