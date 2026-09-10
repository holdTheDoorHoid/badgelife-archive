---
title: Simple Solder (2017 learn-to-solder kit)
id: ruxcon-2017-simple-solder-2017-learn-to-solder-kit
layout: badge
parent: Ruxcon 2017
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: ruxcon-2017
year: 2017
makers:
- name: Morgan Reed (darkglade)
  role: designer
- name: Ruxcon Hardware Hacking Village
  role: organizer / distributor
summary: A free beginner soldering-practice kit handed out at the Ruxcon 2017 Hardware Hacking Village, teaching through-hole and SMD technique on a small two-LED flasher board.
functions: An astable multivibrator (two-transistor flip-flop) that alternately flashes a through-hole red 5mm LED and an SMD green 0805 LED once a CR2032 battery is installed. No firmware or microcontroller; it is a discrete analog circuit chosen purely to teach soldering.
look:
  colors:
  - blue
  shape: rectangle
  themes:
  - learn to solder
  - kit
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: 1x through-hole 5mm red LED (D1) and 1x SMD 0805 green LED (D2), alternately flashed by a two-transistor astable multivibrator.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 120 ordered / 111 handed out over the weekend
  availability: free
  distribution:
  - village
  - kit
  - free_drop
  where: Given out free to attendees at the Ruxcon 2017 Hardware Hacking Village (HHV); not otherwise sold.
make_your_own:
  open_source: partial
  hardware_url: https://ruxconhhv.darkglade.com/2017/SimpleSolderPanel-v1.3.zip
  firmware_url: null
  eda_tool: null
  gerbers_url: https://ruxconhhv.darkglade.com/2017/SimpleSolderPanel-v1.3.zip
  notes: Fabrication files published as panelised (6-up) Gerbers for board revision v1.3; no schematic/PCB source (e.g. KiCad project) found, only the Gerber panel and the build-doc schematic image.
links:
- label: ruxconhhv.darkglade.com/2017/SimpleSolder.pdf
  url: https://ruxconhhv.darkglade.com/2017/SimpleSolder.pdf
  kind: website
- label: Simple Solder Gerbers (v1.3 panelised 6-up)
  url: https://ruxconhhv.darkglade.com/2017/SimpleSolderPanel-v1.3.zip
  kind: fab
- label: 'darkglade.com: Ruxcon 2017 Hardware Hacking Village Wrap'
  url: https://darkglade.com/2017/10/23/ruxcon-2017-hardware-hacking-village-wrap/
  kind: article
images: []
contact: {}
notes:
- The community sheet spaced the name as two words ("Simple Solder"); the maker's own build doc and PCB silkscreen render it as one word, "SimpleSolder".
- Not to be confused with the separate, more advanced "RuxBadge 2017" HHV badge (ruxcon-2017-ruxcon-2017-hhv-badge) by the same designer, which the Simple Solder instructions explicitly point learners toward next.
status: released
sources:
- kind: url
  url: https://ruxconhhv.darkglade.com/2017/SimpleSolder.pdf
  title: Simple Solder (2017 learn-to-solder kit)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://ruxconhhv.darkglade.com/2017/SimpleSolder.pdf
  title: SimpleSolder instruction sheet (Ruxcon Hardware Hacking Village 2017)
  accessed: '2026-09-10'
  note: Maker's build doc/BOM/schematic; source for parts list, circuit function, designer name via silkscreen (Morgan Reed 2017), and board revision v1.3.
- kind: url
  url: https://ruxconhhv.darkglade.com/2017/
  title: Ruxcon 2017 Hardware Hacking Village file index
  accessed: '2026-09-10'
  note: Confirms the Gerbers link for the Simple Solder panel and that no separate firmware exists (unlike RuxBadge 2017).
- kind: url
  url: https://darkglade.com/2017/10/23/ruxcon-2017-hardware-hacking-village-wrap/
  title: Ruxcon 2017 Hardware Hacking Village Wrap
  accessed: '2026-09-10'
  note: Source for quantity (120 ordered, 111 distributed) and that kits were given away free at the village.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Core facts (designer, BOM, circuit, distribution numbers) confirmed on the maker's own site. No price was ever stated (it was a free village giveaway, not sold). No standalone photo URL of the assembled kit was found; the only images are embedded inside the PDF build doc, which fetch_image.py cannot pull from directly, so no images were saved. EDA tool used to design it is unknown; only fabrication Gerbers were published, not source design files.
last_modified_date: '2026-09-10'
---

The Simple Solder kit was Ruxcon Hardware Hacking Village's 2017 learn-to-solder giveaway, designed by Morgan Reed (darkglade) and handed out free to conference attendees. Each panel is actually two identical boards joined down the middle, so a first-timer could populate the left half under HHV staff supervision at the con and practice the right half later on their own. The circuit is a simple two-transistor astable multivibrator with no microcontroller, deliberately chosen so the only "programming" involved is soldering technique: it mixes through-hole parts (a 5mm LED, an electrolytic capacitor, metal-film resistors, a TO-92 transistor) with SMD parts (an 0805 LED, an MLC capacitor, 0805 resistors, a SOT-23 transistor) so builders practice both. Powered by a CR2032 cell in a bargain eBay holder the build doc apologizes for, a working board alternately flashes its red through-hole LED and green SMD LED.

Ruxcon's own recap of the village reports 120 kits ordered and 111 actually distributed over the weekend, roughly double the prior year's uptake. The build doc closes by pointing successful solderers toward the separate, more advanced RuxBadge 2017 HHV badge as a next step.

## Make your own

The maker published panelised (6-up) Gerbers for board revision v1.3 alongside the illustrated build doc (which includes the full BOM and schematic). No schematic/PCB source project (e.g. KiCad files) was found, only the fabrication Gerbers and the build doc's schematic image.
