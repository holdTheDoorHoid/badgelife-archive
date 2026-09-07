---
title: Space Grand Challenge Badge
id: dc31-sgc-aerospace-corporation
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: California Cyber Institute CalPoly SLO
  url: https://cci.calpoly.edu/
  role: 'commissioned the badge, runs the Space Grand Challenge'
- name: The Aerospace Corporation
  url: https://aerospace.org/
  role: 'co-sponsor, named in the schematic title block and the board silkscreen'
- name: Alpenglow Industries
  url: https://www.alpenglowindustries.com/
  role: 'PCB design (original 2022 KiCad project, reused for this DC31 board)'
summary: 'A satellite-shaped blinky badge made for the Cal Poly California Cybersecurity Institute and The Aerospace Corporation, built from Alpenglow Industries'' 2022 satellite PCB design. Thirteen 1206 LEDs on the body and solar-panel wings blink from a two-transistor oscillator; there is no microcontroller.'
functions: 'A two-transistor astable-multivibrator oscillator alternately flashes two groups of LEDs on the solar panels while one LED at the dish stays lit. Two slide switches are visible on the board (on/off and a blink/solid mode per the shared design); there is no microcontroller or firmware.'
look:
  colors: []
  shape: satellite
  themes:
  - space
  - sci-fi
  - security
  form_factor: pcb badge
tech:
  mcu: none
  leds:
    count: 13
    type: discrete
    note: '1206 SMD LEDs (footprint "Alpenglow:LED_1206+"), driven by two SOT-23 transistors (Q1, Q2) in an astable-multivibrator arrangement rather than a microcontroller'
  display: none
  connectivity:
  - none
  inputs:
  - slide switches
  battery: CR2032 (SMT holder)
  sao_version: none
  sao_ports: 0
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Made for DEF CON 31; no storefront or attendee report found. See the fuller duplicate entry for distribution details.'
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.
  firmware_url: null
  eda_tool: KiCad
  license: MIT
  notes: 'The DC31 repo itself holds only a KiCad 6 PCB file and a demo video; the full schematic, Gerbers and BOM live in the original 2022 Alpenglow Industries design (MIT licensed), which this board reuses component-for-component.'
links:
- label: github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.#readme
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.#readme
  kind: repo
- label: 'AlpenglowIndustries/Space_Grand_Challenge (GitHub) - original 2022 design with schematic, Gerbers and BOM, MIT license'
  url: https://github.com/AlpenglowIndustries/Space_Grand_Challenge
  kind: repo
- label: 'SGC badge Satellite23.mp4 (demo video in the DC31 repo)'
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/SGC%20badge%20Satellite23.mp4
  kind: video
images: []
contact: {}
notes:
- 'This is the same badge as dc31-space-grand-challenge-satellite-badge, which the community sheet listed separately under maker "Aerospace Village." That entry has photos and much more extensive sourcing (forum posts, the challenge website, the full BOM); this entry was filled in independently from the same GitHub repos and kept intentionally lighter to avoid duplicating that work.'
status: announced
sources:
- kind: sheet
  event: dc31
  row: 20
  updated: '2023-02-14'
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.
  title: 'SGC-2023-Badge-Aerospacecorp. (GitHub)'
  accessed: '2026-09-07'
  note: 'The link from the sheet. README says the board was created for CCI and DEFCON 31; repo holds only the README, a KiCad 6 PCB file and a video.'
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/defcon-badge-hw.kicad_pcb
  title: 'defcon-badge-hw.kicad_pcb (PCB file)'
  accessed: '2026-09-07'
  note: 'Parsed for footprints: 13 x LED_1206, 2 SOT-23 transistors (Q1/Q2), CR2032 SMT holder, 2 slide switches, satellite-shaped board outline, Cal Poly CCI and Alpenglow logo footprints; no IC/MCU footprint present.'
- kind: url
  url: https://github.com/AlpenglowIndustries/Space_Grand_Challenge
  title: 'AlpenglowIndustries/Space_Grand_Challenge (GitHub)'
  accessed: '2026-09-07'
  note: 'Original repo: description confirms "a PCB in the shape of a satellite with a transistor oscillator circuit which creates alternating blinking LEDs, developed for the Aerospace Corp. and California Cybersecurity Institute"; MIT LICENSE dated 2022; includes schematic PDF, Gerbers and BOM matching the footprints seen in the DC31 PCB file. Artwork folder holds design mockups and logos, not photos of the finished physical board.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Duplicate of dc31-space-grand-challenge-satellite-badge (same badge, same event, listed twice on the community sheet under different maker names). No solder-mask/board color, price, quantity, or availability confirmed from sources reached in this pass; left empty rather than guessed. No photos of the finished physical board were found in the repos reached (only design artwork/logos and a video not extracted as stills), so images is left empty here - see the sibling entry for saved photos.'
last_modified_date: '2026-09-07'
---

This satellite-shaped badge was built for the Cal Poly California Cybersecurity Institute's Space Grand Challenge, sponsored by The Aerospace Corporation, for DEF CON 31. Rather than a microcontroller, the board runs a two-transistor astable-multivibrator oscillator that alternately blinks two groups of thirteen 1206 LEDs spread across the satellite's body and solar-panel wings, powered by a coin-cell battery. The design itself dates back to a 2022 project by Alpenglow Industries, released under the MIT license with full KiCad schematic, PCB, Gerbers and BOM; the DC31-specific repo linked from the community sheet only carries the PCB layout and a short demo video, but the underlying circuit and component list match the original Alpenglow project component-for-component.

This entry duplicates dc31-space-grand-challenge-satellite-badge, which the community sheet also listed (under the maker name "Aerospace Village") with photographs and considerably deeper sourcing, including the challenge website printed on the badge's back and contemporary forum posts. That entry should be treated as the primary record for this badge.

## Make your own

The original Alpenglow Industries repository (github.com/AlpenglowIndustries/Space_Grand_Challenge) has the complete KiCad 6 project - schematic, PCB layout, a footprint library, Gerbers and a bill of materials - under the MIT license. Since the board has no firmware, replicating it is a matter of fabricating the PCB from the supplied Gerbers and hand-soldering the BOM parts (LEDs, resistors, two transistors, switches and a CR2032 holder).
