---
title: SGC Aerospace Corporation
id: dc31-sgc-aerospace-corporation
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: California Cybersecurity Institute (Cal Poly)
  url: https://cci.calpoly.edu/
  role: commissioned the badge; runs the Space Grand Challenge program
- name: The Aerospace Corporation
  url: https://aerospace.org/
  role: co-sponsor; logo and name appear on the board and the schematic title block
- name: Alpenglow Industries
  url: https://www.alpenglowindustries.com/
  role: original PCB design (2022), reused for this 2023 run
summary: A satellite-shaped, microcontroller-free blinky badge built for Cal Poly's California Cybersecurity Institute (CCI) and The Aerospace Corporation, made for DEF CON 31's Aerospace Village. Yellow LEDs on the two solar-panel wings flash in alternating groups from a two-transistor oscillator, and a ROT13 line on the dish points to a beginner satellite-hacking challenge.
functions: A two-transistor astable-multivibrator oscillator alternately flashes two groups of six yellow 1206 LEDs on the solar-panel wings; a further LED at the dish feed stays lit whenever the badge is powered. No microcontroller or firmware. One slide switch is ON/OFF; the PCB silkscreen also carries a BLINK/SOLID label. The dish carries the ROT13-encoded text "ZNL RZVG QVTVGNY QHFG" (decodes to "MAY EMIT DIGITAL DUST"), and the board points to a web-based beginner satellite/cybersecurity challenge.
look:
  colors:
  - purple
  - gold
  - yellow
  shape: satellite
  themes:
  - space
  - puzzle
  - ctf
  - security
  - logo
  form_factor: pcb badge
tech:
  mcu: none
  leds:
    count: 13
    type: discrete
    note: Yellow 1206 LEDs, six per solar-panel wing wired as two alternating groups of six from the two-transistor oscillator, plus one at the dish feed powered directly from the battery.
  display: none
  connectivity:
  - none
  inputs:
  - slide switches
  power: CR2032
  battery: CR2032 in an SMT holder
  sao_version: none
  sao_ports: 0
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  availability_note: No storefront found; checked 2026-09-07.
  distribution:
  - village
  where: Made for the DEF CON Aerospace Village at DEF CON 31; no price, quantity, or confirmation it was actually sold or handed out was found in any source.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries
  firmware_url: null
  gerbers_url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries/tree/main/Gerbers
  bom_url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries/blob/main/Satellite_PCB_BOM.csv
  eda_tool: KiCad
  license: MIT
  notes: The repo linked from this entry's sheet row (SGC-2023-Badge-Aerospacecorp.) holds only a KiCad 6 PCB file and a short video, no schematic or BOM. The full 2022 KiCad project (schematic, PCB, Gerbers, BOM), from which this 2023 board is derived, is under MIT license in the linked Alpenglow-Industries fork.
links:
- label: github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.
  kind: repo
- label: Space_Grand_Challenge-AlpenglowIndustries (GitHub) - full KiCad project, Gerbers, BOM, MIT
  url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries
  kind: repo
- label: AlpenglowIndustries/Space_Grand_Challenge (GitHub) - original 2022 design repo
  url: https://github.com/AlpenglowIndustries/Space_Grand_Challenge
  kind: repo
- label: Short video of the badge blinking (in the 2023 repo)
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/SGC%20badge%20Satellite23.mp4
  kind: video
- label: Satellite Badge Challenge site (URL printed on the back of the badge)
  url: https://spacecybernautctf.wixsite.com/badge
  kind: website
images:
- file: assets/images/badges/dc31/sgc-aerospace-corporation/badge-lit.jpg
  source: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.
  credit: California Cybersecurity Institute (Cal Poly), frame from the repo video
  caption: Assembled badge lit up, showing the satellite shape, dish LED, one group of panel LEDs, and the CCI and Aerospace Corporation logos
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- This is the same physical badge as dc31-space-grand-challenge-satellite-badge, which the community sheet also listed (under maker "Aerospace Village") and which carries much deeper sourcing (forum posts, the challenge website, the full BOM, three photos). That entry's research treats it as the primary record and its notes say the two were merged; this entry is kept filled in but intentionally lighter per the archive's duplicate-handling rule.
status: announced
sources:
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp.
  title: SGC Aerospace Corporation
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc31''.'
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/README.md
  title: SGC-2023-Badge-Aerospacecorp. (GitHub README)
  accessed: '2026-09-07'
  note: 'README: "Created for CCI and DEFCON 31," open the PCB with KiCad 6 not 7. Repo holds only a README, a KiCad PCB file and a video.'
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/defcon-badge-hw.kicad_pcb
  title: defcon-badge-hw.kicad_pcb
  accessed: '2026-09-07'
  note: 'Parsed footprints: 13 LED_1206, 17 resistors, 2 capacitors, 2 SOT-23 transistors, 1 slide switch, CR2032 SMT holder, plus Aerospace Corp and CCI logo footprints and a satellite-dish footprint; confirms no MCU.'
- kind: url
  url: https://github.com/cal-poly-cci/SGC-2023-Badge-Aerospacecorp./blob/main/SGC%20badge%20Satellite23.mp4
  title: SGC badge Satellite23.mp4
  accessed: '2026-09-07'
  note: Phone video of the finished purple/gold board with LEDs alternating; source of the saved image (a cropped frame) and of the decoded ROT13 dish text.
- kind: url
  url: https://github.com/cal-poly-cci/Space_Grand_Challenge-AlpenglowIndustries
  title: Space_Grand_Challenge-AlpenglowIndustries (GitHub)
  accessed: '2026-09-07'
  note: Fork of the original Alpenglow Industries repo; full 2022 KiCad 6 project (schematic, PCB, Gerbers, BOM) under MIT license; description names The Aerospace Corporation and CCI as the badge's sponsors.
- kind: url
  url: https://mustangnews.net/california-cybersecurity-institute-hosts-space-grand-challenge-for-middle-and-high-school-students/
  title: California Cybersecurity Institute hosts "Space Grand Challenge" for middle and high school students - Mustang News
  accessed: '2026-09-07'
  note: Describes the Space Grand Challenge as an annual game-based cybersecurity competition for middle/high schoolers built by Cal Poly students; no mention of this PCB badge specifically.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No price, quantity, or confirmation that the badge was actually distributed at DEF CON 31 was found in any source; get_one fields left empty/unknown accordingly. The 2023 repo linked from this entry's own sheet row has no schematic or BOM, only a PCB file and a video; hardware/BOM links above point to the fuller 2022 Alpenglow-derived repo, which matches the 2023 board's footprints component-for-component. This entry duplicates dc31-space-grand-challenge-satellite-badge (same badge, listed separately on the community sheet under maker "Aerospace Village"); that entry has more extensive sourcing including the challenge website and forum announcements.
last_modified_date: '2026-09-07'
---

This satellite-shaped badge was built for Cal Poly's California Cybersecurity Institute (CCI) and sponsored by The Aerospace Corporation, made for the DEF CON Aerospace Village at DEF CON 31 in 2023. The design traces back to a 2022 project by Alpenglow Industries of San Luis Obispo: a purple PCB shaped like a satellite, with gold solar-panel wings carrying yellow 1206 LEDs. There is no microcontroller — a two-transistor oscillator (an astable multivibrator) alternately flashes two groups of six LEDs on the wings, while a further LED at the dish feed stays lit as long as the CR2032 coin cell is connected. A ROT13-encoded line, "ZNL RZVG QVTVGNY QHFG" (which decodes to "MAY EMIT DIGITAL DUST"), curves across the dish, and the board points to a web-based beginner satellite/cybersecurity challenge.

The GitHub repository linked from this entry's own sheet row holds only a KiCad 6 PCB file and a short phone video of a finished, lit-up unit — no schematic or bill of materials. A companion repository in the same cal-poly-cci GitHub organization carries the fuller 2022 KiCad project (schematic, PCB, Gerbers, and a BOM with Digi-Key part numbers) under the MIT license; its footprint set matches this 2023 board component-for-component, indicating the 2023 run reused the 2022 Alpenglow design with updated branding rather than a fresh circuit. No source found gives a price, a quantity made, or confirmation that the badge was actually sold or handed out at the con.

## Make your own

The complete KiCad 6 project — schematic, PCB layout, Gerbers, and a BOM — is published under the MIT license in the linked Alpenglow-Industries fork. The board has no firmware, so replicating it is a matter of fabricating the PCB from the Gerbers and hand-soldering the BOM parts (1206 LEDs, resistors, two SOT-23 transistors, a slide switch, and a CR2032 holder). The 2023 repo's own README notes the PCB file should be opened in KiCad 6, not KiCad 7.
