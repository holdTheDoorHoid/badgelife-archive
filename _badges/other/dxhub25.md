---
title: DXHub25
id: other-dxhub25
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: NerdFlare
  url: https://github.com/NerdFlare
summary: A simple wearable LED blinky badge made by NerdFlare for the 2025 "DX Hub" hackathon, with AWS and NerdFlare branding.
functions: 'Push-button switch lights three yellow LEDs; no microcontroller or programmable logic.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 3
    type: discrete
    note: 3-pin SMD yellow LEDs (XL-3210SYGC), lit via a momentary push-button, no driver IC
  display: none
  connectivity: []
  battery: coin cell (BS-24-B4AK014 holder)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/NerdFlare/DXHub25
  firmware_url: null
  eda_tool: EasyEDA
  gerbers_url: https://raw.githubusercontent.com/NerdFlare/DXHub25/main/pcb/V2/Compiled/Gerber.zip
  bom_url: https://raw.githubusercontent.com/NerdFlare/DXHub25/main/pcb/V2/Compiled/bom.csv
  notes: 'Repo has two board revisions (V1, V2): KiCad schematic/PCB files (converted from EasyEDA via easyeda2kicad), compiled Gerbers, BOM and position files for V2. No firmware repo since the board has no MCU.'
links:
- label: github.com/NerdFlare/DXHub25
  url: https://github.com/NerdFlare/DXHub25
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/NerdFlare/DXHub25
  title: DXHub25
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://api.github.com/repos/NerdFlare/DXHub25/contents/pcb/V2/Compiled/bom.csv
  title: DXHub25 V2 bill of materials
  accessed: '2026-09-07'
  note: 'BOM lists 1 coin-cell holder (BS-24-B4AK014), 3 resistors, 1 pushbutton switch, 3 yellow SMD LEDs (XL-3210SYGC) -- no MCU.'
- kind: url
  url: https://api.github.com/repos/NerdFlare/DXHub25/commits
  title: DXHub25 commit history
  accessed: '2026-09-07'
  note: 'Commits dated June 2025; messages mention "new gerbers ready for prototype of v0" and "added hole for lanyard", confirming a 2025, wearable board.'
- kind: url
  url: https://api.github.com/repos/NerdFlare/DXHub25/contents/svg/layers
  title: DXHub25 SVG art layers
  accessed: '2026-09-07'
  note: 'Layer filenames include "DX hackathon", "aws", "nerdflare", and "Noyce", indicating AWS and NerdFlare branding on a board made for a "DX Hub"-named hackathon.'
research:
  status: verified
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Fact-check (2026-09-07) re-fetched all four cited GitHub sources directly (repo root, bom.csv, commits, svg/layers) plus the pcb/V1 and pcb/V2 directory listings and the raw gerbers_url/bom_url links; every field and body sentence is supported: BOM matches exactly (1 BS-24-B4AK014 coin-cell holder, 3 resistors, 1 MSK12C02 pushbutton, 3 XL-3210SYGC yellow LEDs, no MCU), commit dates/messages match (June 2025, "added hole for lanyard"), SVG layer filenames match (DX hackathon/aws/nerdflare/Noyce), V1 and V2 folders exist with V2 containing a re-exported easyeda2kicad.kicad_sym library, and the gerbers/BOM raw URLs both return HTTP 200. Confirmed the repo has no README/description and no matching "DX Hub" event exists in events.yml, so event=other and the unresolved fields (price, quantity, availability, distribution, where, images) are correctly left empty/unknown rather than guessed. Confidence stays low only because the sole source is the repo itself -- no press, social, or storefront coverage was checked (researcher''s stated web-search budget was exhausted), so the event''s host/name and distribution details are not independently corroborated.'
last_modified_date: '2026-09-07'
---

DXHub25 is a simple, non-programmable LED badge made by NerdFlare for a 2025 hackathon whose branding reads "DX Hub" alongside AWS and NerdFlare logos (seen in the repo's SVG art-layer filenames). The board carries a coin-cell holder, a momentary push-button, and three yellow SMD LEDs wired straight to the switch through current-limiting resistors -- there is no microcontroller, so it functions purely as a manual blinky rather than a programmable badge or SAO. Commit messages from June 2025 mention adding a lanyard hole, confirming it was meant to be worn.

The GitHub repository (NerdFlare/DXHub25) publishes two board revisions. V1 is the initial design; V2 adds a re-exported EasyEDA symbol library alongside KiCad schematic/PCB files (the whole project was drawn in EasyEDA and converted to KiCad via easyeda2kicad) and includes compiled Gerbers, a BOM, and component position files, making the hardware straightforward to reproduce. No firmware is published because the board has no chip to program.

Beyond the repository itself, no press coverage, storefront listing, or photo of the finished board could be located, so price, quantity made, and how it was distributed at the event remain unknown.
