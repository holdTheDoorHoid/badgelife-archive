---
title: Sam-badge — Dulces Sueños
id: other-sam-badge-dulces-suenos
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 2020
makers:
- name: Electronic Cats
  url: https://electroniccats.com
summary: A soldering-practice kit shaped like a sleeping cat ("Sam"), built around an STM8 microcontroller and four RGB LEDs, made by Electronic Cats for Talent Land 2020.
functions: Once assembled and programmed over its SWD/SWIM port, the board's RGB LEDs blink and cycle colors in patterns until the CR2032 battery is depleted. A reset button restarts the microcontroller.
look:
  colors: []
  shape: cat
  themes:
  - cat
  - learn to solder
  - kit
tech:
  mcu: STM8S003F3P
  leds:
    count: 4
    type: RGB
    note: Model 156120M173000; two-LED light patterns described in marketing copy, four LEDs listed in the bill of materials.
  display: null
  connectivity: []
  battery: CR2032 (not included)
  sao_version: null
get_one:
  price: free (shipping cost only)
  price_usd: null
  quantity: '200'
  availability: free
  distribution:
  - free_drop
  - contest
  where: Given away by Electronic Cats, Wurth Electronics, Talent Land and PCBWay to the first 200 people who requested one and paid shipping, as part of an assembly/soldering challenge tied to the "Iron Land @ Home" virtual event (July 8-9, 2020).
make_your_own:
  open_source: true
  hardware_url: https://github.com/ElectronicCats/Sam-badge
  firmware_url: https://github.com/ElectronicCats/Sam-badge
  eda_tool: KiCad
  license: 'Firmware: GNU AGPL v3.0; Hardware: CERN Open Hardware Licence v1.2'
links:
- label: github.com/ElectronicCats/Sam-badge
  url: https://github.com/ElectronicCats/Sam-badge
  kind: repo
- label: Electronic Cats store listing
  url: https://electroniccats.com/store/badge-sam-dulces-suenos/
  kind: store
- label: Assembly video (YouTube)
  url: https://www.youtube.com/watch?v=UkvUJHmSHjA
  kind: video
images: []
contact: {}
notes:
- Sheet/repo title uses an em dash; kept as "Sam-badge — Dulces Sueños".
status: released
sources:
- kind: url
  url: https://github.com/ElectronicCats/Sam-badge
  title: Sam-badge — Dulces Sueños
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/ElectronicCats/Sam-badge
  title: Sam-badge README (raw)
  accessed: '2026-09-07'
  note: 'Maker''s own README: describes the kit as a soldering challenge board for Talent Land 2020 (Iron Land @ Home virtual event, 8-9 July 2020), STM8S003F3P MCU, 4x RGB LED 156120M173000, CR2032 battery holder (batteries not included), SWD/SWIM programming (LEDs blink/change color until the battery is depleted; reset button restarts the STM8), 200 units given free (shipping only) via Electronic Cats/Wurth Electronics/Talent Land/PCBWay, open hardware (CERN OHL v1.2) and firmware (AGPL v3.0). Confirms "Placa PCB Sam Durmiendo" ("Sam Sleeping PCB board").'
- kind: url
  url: https://raw.githubusercontent.com/ElectronicCats/Sam-badge/master/Hardware/BadgeSam.svg
  title: BadgeSam.svg (KiCad board outline export)
  accessed: '2026-09-07'
  note: PCB outline render from the maker's own KiCad hardware files confirms the board is physically shaped like a sleeping cat curled in a star-patterned bed. Also confirms the EDA tool is KiCad (repo contains .kicad_pcb/.kicad_mod/.kicad_sch files).
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for "Talent Land 2020" (Guadalajara, Mexico), an innovation/tech event with no matching entry in events.yml, so event is left as "other". The event went virtual in 2020 as "Iron Land @ Home" (8-9 July 2020) due to the pandemic; the badge kit was distributed as part of a soldering challenge tied to that virtual event rather than sold. Marketing copy says "two LEDs with different light patterns" while the bill of materials lists 4x RGB LED — both figures are recorded in tech.leds.note since sources disagree. The electroniccats.com store page (electroniccats.com/store/badge-sam-dulces-suenos/) returned 404 on re-check; price and quantity come from the GitHub README only. Corrected get_one.availability from "not_released" (contradicted by the README, which documents an actual 2020 giveaway of 200 units) to "free". Added make_your_own.eda_tool: KiCad, directly evidenced by the .kicad_pcb/.kicad_sch files in the repo''s Hardware folder. Removed the one saved image: it was Electronic
    Cats'' generic "AVAILABLE AT OUR STORE" button graphic (electroniccats.com/wp-content/uploads/badge_store.png), not a photo of the assembled badge, so it failed the guide''s "not a logo" rule; no photo of an assembled unit could be found, though the maker''s own KiCad board-outline SVG (see sources) independently confirms the cat shape. Removed the "Everlight" brand attribution for the LED (part no. 156120M173000) from the body: the README/BOM and Mouser link give only the part number, and attempts to confirm the manufacturer independently (Mouser US/MX, Octopart, DigiKey) all failed (timeouts or 403s), so the brand name is left out as unsupported while the part number itself (which the maker does state) is kept. All other fields and body sentences checked against the maker''s README, the GitHub repo page, and the repo file listing and were confirmed.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/sam-badge-dulces-suenos.glb
  method: kicad
  source_file: Hardware/BadgeSam.kicad_pcb
  generated: '2026-09-10'
  bytes: 70736
---

Sam — Dulces Sueños ("Sam, sweet dreams") is a beginner soldering-practice kit from Electronic Cats, shaped like a sleeping cat and built to teach surface-mount soldering. It was originally designed to be taught as an in-person workshop at Talent Land 2020 in Guadalajara, Mexico, but when the pandemic forced that event online, Electronic Cats partnered with Wurth Electronics, PCBWay and Talent Land to distribute 200 of the kits for free (recipients paid only shipping) so people could assemble the board at home and take part in a companion challenge tied to the virtual "Iron Land @ Home" event held July 8-9, 2020.

The board is built around an STM8S003F3P microcontroller and four RGB LEDs (part no. 156120M173000), a CR2032 coin-cell holder (batteries not included), a reset button, and passive components. After soldering the SMD parts, builders program the board over its SWD/SWIM header using an ST-Link V2, J-Link, or any SWIM-compatible programmer; once running, the LEDs cycle through colors and patterns until the battery runs down. Electronic Cats published full schematics and firmware on GitHub, with hardware under the CERN Open Hardware Licence v1.2 and firmware under GNU AGPL v3.0.

## Make your own

Hardware (schematics, PCB) and firmware are both published at github.com/ElectronicCats/Sam-badge. Building one requires SMD soldering skill and an SWD/SWIM-capable programmer (ST-Link V2, J-Link, or equivalent) to flash the STM8S003F3P over its SWD port.
