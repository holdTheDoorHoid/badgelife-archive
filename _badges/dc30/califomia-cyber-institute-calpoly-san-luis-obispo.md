---
title: Space Grand Challenge Badge
id: dc30-califomia-cyber-institute-calpoly-san-luis-obispo
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: California Cybersecurity Institute (Cal Poly)
  url: https://cci.calpoly.edu/
  role: commissioned the badge, runs the Space Grand Challenge
- name: The Aerospace Corporation
  url: https://aerospace.org/
  role: co-sponsor, named in the schematic title block and board silkscreen
- name: Alpenglow Industries
  url: https://www.alpenglowindustries.com/
  role: PCB design (San Luis Obispo)
summary: A satellite-shaped blinky badge commissioned by the Cal Poly California Cybersecurity Institute and The Aerospace Corporation, designed by Alpenglow Industries, and announced for the DEF CON 30 Aerospace Village. Thirteen 1206 LEDs on the solar-panel wings and dish blink from a two-transistor oscillator; there is no microcontroller.
functions: A two-transistor astable-multivibrator oscillator alternately flashes two groups of yellow 1206 LEDs on the solar-panel wings while a thirteenth LED at the dish feed stays lit. Two slide switches select ON/OFF and BLINK/SOLID; there is no microcontroller or firmware. The badge carries a ROT13 message and was meant to lead to a beginner satellite-hacking challenge website.
look:
  colors:
  - purple
  - gold
  - yellow
  shape: satellite
  themes:
  - space
  - sci-fi
  - security
  - puzzle
  - ctf
  form_factor: pcb badge
tech:
  mcu: none
  leds:
    count: 13
    type: discrete
    note: 1206 SMD LEDs driven by two transistors in an astable-multivibrator arrangement rather than a microcontroller
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
  availability_note: No storefront, price or quantity found; checked 2026-09-07.
  distribution:
  - village
  where: Announced on the DEF CON forums (2022-06-10) as coming to the Aerospace Village at DEF CON 30; no attendee report or price was found.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/AlpenglowIndustries/Space_Grand_Challenge
  firmware_url: null
  gerbers_url: https://github.com/AlpenglowIndustries/Space_Grand_Challenge/tree/main/Gerbers
  bom_url: null
  eda_tool: KiCad
  license: MIT
  notes: No firmware; the board is a passive transistor oscillator. The Alpenglow Industries repo (created 2022) has the full KiCad 6 schematic, PCB, Gerbers, BOM and artwork under MIT. This same design was reused for a DC31 (2023) run of the badge.
links:
- label: AlpenglowIndustries/Space_Grand_Challenge (GitHub) - original design, schematic, Gerbers, BOM, MIT license
  url: https://github.com/AlpenglowIndustries/Space_Grand_Challenge
  kind: repo
- label: DEF CON forums - 2022 BadgeLife List (June 2022 announcement with a render)
  url: https://forum.defcon.org/node/240869
  kind: article
- label: California Cybersecurity Institute / Space Grand Challenge (now under Noyce School of Applied Computing)
  url: https://noyce.calpoly.edu/cybersecurity/space-grand-challenge-program/
  kind: website
  archived: https://web.archive.org/web/20260607204329/https://noyce.calpoly.edu/cybersecurity/space-grand-challenge-program/
images:
- file: assets/images/badges/dc30/califomia-cyber-institute-calpoly-san-luis-obispo/43310a462e.jpg
  source: https://forum.defcon.org/node/240869
  credit: hdanielson on the DEF CON forums (3D render)
  caption: 3D render of the satellite-shaped Space Grand Challenge badge, posted with the June 2022 DEF CON 30 badgelife-list announcement
contact: {}
notes:
- 'The community sheet''s maker and item columns appear swapped for this row: the sheet listed the maker as "Space Grand Challenge Badge" and the item title as "Califomia Cyber Institute Calpoly San Luis Obispo". The forum announcement this row is drawn from reads "Califomia Cyber Institute Calpoly San Luis Obispo has a Space Grand Challenge Badge!" - the badge''s actual name is "Space Grand Challenge Badge" and the maker is the California Cybersecurity Institute (Cal Poly), so this entry retitles accordingly and keeps the sheet''s wording noted here.'
- 'The same satellite PCB design was reused for a DC31 (2023) run, documented in two other archive entries: dc31-space-grand-challenge-satellite-badge (the fuller, more deeply sourced record, with photos of a built unit and the challenge website) and dc31-sgc-aerospace-corporation (a lighter duplicate). This DC30 entry covers the original 2022 announcement; no photo of a physically built DC30-era unit or a DC30 challenge-site URL was found, only the 3D render attached to the forum post.'
- No evidence was found that the badge was actually distributed at DEF CON 30 (the forum post says only that it "will be at around" the Aerospace Village); Alpenglow Industries has since closed and the California Cybersecurity Institute has been "temporarily discontinued" per Cal Poly's Noyce School of Applied Computing.
status: announced
sources:
- kind: sheet
  event: dc30
  row: 30
  updated: '2022-06-11'
- kind: url
  url: https://forum.defcon.org/node/240869
  title: 2022 BadgeLife List has Started!! - DEF CON Forums
  accessed: '2026-09-07'
  note: 'Post #3 by hdanielson, 2022-06-10, 16:21 PT: "Califomia Cyber Institute Calpoly San Luis Obispo has a Space Grand Challenge Badge! The badge is a satellite and will be at around at Aerospace Village. The badge will have a website with some beginner challenges." Attached a 3D render (image ID 241905), saved to this entry.'
- kind: url
  url: https://github.com/AlpenglowIndustries/Space_Grand_Challenge
  title: AlpenglowIndustries/Space_Grand_Challenge (GitHub)
  accessed: '2026-09-07'
  note: 'Repo description: "A PCB in the shape of a satellite with a transistor oscillator circuit which creates alternating blinking LEDs, developed for the Aerospace Corp. and California Cybersecurity Institute"; MIT license; full KiCad 6 project (schematic, PCB, Gerbers, BOM, artwork); no microcontroller footprint.'
- kind: url
  url: https://noyce.calpoly.edu/cybersecurity/space-grand-challenge-program/
  title: Space Grand Challenge Program - Noyce School of Applied Computing
  accessed: '2026-09-07'
  note: Describes Space Grand Challenge as a free, virtual, game-based cybersecurity competition for middle/high schoolers built by Cal Poly students - the educational program behind the badge, not a description of the physical badge itself. Notes the Cybersecurity Institute has been "temporarily discontinued".
  archived: https://web.archive.org/web/20260607204329/https://noyce.calpoly.edu/cybersecurity/space-grand-challenge-program/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Retitled from the sheet-import placeholder using the forum post the row was drawn from (see notes). Hardware and maker details for this exact design are well documented via the Alpenglow Industries GitHub repo and a sibling DC31 entry (dc31-space-grand-challenge-satellite-badge) that verified the built board in depth; those details are reused here since it is the same PCB design. Not confirmed for the DC30 run specifically: price, quantity, whether it was actually handed out at DEF CON 30, and whether a DC30-specific challenge website existed (the sibling DC31 entry''s Wix challenge site postdates this by about a year). No photo of a physically assembled DC30-era unit was found, only the 3D render attached to the forum announcement.'
last_modified_date: '2026-09-07'
related:
- dc31-space-grand-challenge-satellite-badge
model:
  file: assets/models/dc30/califomia-cyber-institute-calpoly-san-luis-obispo.glb
  method: kicad
  source_file: Satellite_PCB.kicad_pcb
  generated: '2026-09-07'
  bytes: 207316
---

The Space Grand Challenge is a game-based cybersecurity competition built by Cal Poly students and run by the university's California Cybersecurity Institute (CCI) for middle- and high-school students. To promote space and cybersecurity to newcomers at DEF CON 30, CCI and The Aerospace Corporation had Alpenglow Industries of San Luis Obispo design a satellite-shaped PCB badge in 2022. It was announced on the DEF CON forums on 2022-06-10 - the post this entry's sheet row was drawn from - as coming to the Aerospace Village, with a website planned to carry beginner challenges.

The badge has no microcontroller: a two-transistor astable-multivibrator oscillator alternately flashes two groups of yellow 1206 LEDs across the solar-panel wings while a thirteenth LED at the dish feed stays lit continuously, powered by a CR2032 cell. One slide switch is ON/OFF and the other selects BLINK/SOLID. A ROT13 message is worked into the design. The full KiCad 6 project - schematic, PCB layout, Gerbers, BOM and artwork - is published under the MIT license by Alpenglow Industries on GitHub.

No source found confirms a price, a production quantity, or that the badge was actually handed out at DEF CON 30 rather than merely announced; the forum post itself is noncommittal ("will be at around at Aerospace Village"). The same design was reused for a DC31 (2023) run of the badge, which is documented much more fully - including photos of a built unit and its beginner-challenge website - in the separate archive entries dc31-space-grand-challenge-satellite-badge and dc31-sgc-aerospace-corporation.
