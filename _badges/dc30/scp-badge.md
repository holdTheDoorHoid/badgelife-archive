---
title: SCP Badge
id: dc30-scp-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: K4r4koyun
  url: https://github.com/k4r4koyun
summary: 'An SCP Foundation-themed badge K4r4koyun designed for DEF CON 30, using neopixels for lighting; the maker says the design is flawed and was never built.'
functions: 'RGB lighting via neopixels (WS2812-style addressable LEDs); no other interactive functions described.'
look:
  colors: []
  shape: null
  themes:
  - security
tech:
  mcu: null
  leds:
    count: null
    type: neopixel
    note: 'Maker misplaced/misrouted the capacitors for the neopixels, per the repo README.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/k4r4koyun/DEFCON-30-SCP-Badge
  url: https://github.com/k4r4koyun/DEFCON-30-SCP-Badge
  kind: repo
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: cancelled
sources:
- kind: url
  url: https://github.com/k4r4koyun/DEFCON-30-SCP-Badge
  title: SCP Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc30''.'
- kind: url
  url: https://raw.githubusercontent.com/k4r4koyun/DEFCON-30-SCP-Badge/main/README.md
  title: 'DEFCON-SCP-Badge README'
  accessed: '2026-09-07'
  note: 'Maker''s own description: design intended for DEF CON 30, uses neopixels, AA-battery power was flawed, caps for neopixels misrouted; KiCad files withheld because of the flaw.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The GitHub repo (by K4r4koyun, who also made the dc32-teethernet-sao entry) is a design-only project: it holds a schematic PNG, an Inkscape board drawing, and a PDF, but no KiCad source, no gerbers, and no photos of a built/assembled badge. The maker states in the README that the power design (AA batteries feeding neopixels through no LDO) and the neopixel decoupling capacitor placement are both flawed, and that they withheld the KiCad files as a result — implying the badge was designed for DEF CON 30 but not actually fabricated or worn. No independent web search results (maker profile, forums, press) turned up evidence it was built or distributed, so price, quantity, MCU, colors, and shape are left empty. Marked status "cancelled" (designed, not realized) rather than "released"; happy to be corrected if the maker later confirms units were built.'
last_modified_date: '2026-09-07'
---

K4r4koyun designed the SCP Badge as an SCP Foundation-themed piece for DEF CON 30 (2022), planning to light it with a strip of neopixel (WS2812-style) addressable RGB LEDs. The project lives in a public GitHub repository as a schematic image, an Inkscape board drawing, and a PDF export, built in KiCad and Inkscape.

By the maker's own account, the design never made it past this stage. The README explains that the original AA-battery power supply dropped voltage too quickly to reliably drive the neopixels, and that even a LiPo swap would need the power routed through an LDO to avoid frying other components; separately, the decoupling capacitors for the neopixels were misplaced or misrouted on the board. Because of these flaws, K4r4koyun did not publish the underlying KiCad source files, and no photos of an assembled badge exist in the repo or turned up in a web search — so this entry is recorded as a cancelled/unbuilt design rather than a badge that was fabricated or distributed at DEF CON 30.
