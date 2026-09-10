---
title: Attendee Minibadge 2024
id: saintcon-2024-attendee-minibadge-2024
layout: badge
parent: Saintcon 2024
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2024
year: 2024
makers:
- name: UtahSAINT
  url: https://github.com/utahsaint-org
summary: The official attendee minibadge for SAINTCON 2024, part of the conference's open-hardware minibadge trading program.
functions: 'Trading-card-style minibadge plugged into the SAINTCON badge via SAINTCON''s own open-hardware minibadge connector (not the DEF-CON-style SAO standard); part of the official minibadge set attendees collect and trade at the conference.'
look:
  colors: []
  shape: null
  themes:
  - security
  - village badge
tech:
  mcu: null
  leds: null
  display: null
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
  hardware_url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Attendee-Minibadge-2024
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/utahsaint-org/MiniBadges2024/tree/main/Attendee-Minibadge-2024
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Attendee-Minibadge-2024
  kind: repo
- label: saintcon.org/minibadges
  url: https://saintcon.org/minibadges/
  kind: website
images: []
contact: {}
notes:
- Official attendee minibadge design in the SAINTCON 2024 community MiniBadges repo. Found by the event-year sweep, task saintcon-2024.
- 'Sweep title was "Attendee-Minibadge-2024" (the repo folder name); rendered here in normal case as "Attendee Minibadge 2024".'
status: listed
sources:
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024/tree/main/Attendee-Minibadge-2024
  title: Attendee-Minibadge-2024
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2024); event read as ''saintcon-2024''.'
- kind: url
  url: https://github.com/utahsaint-org/MiniBadges2024
  title: MiniBadges2024 repository (utahsaint-org)
  accessed: '2026-09-10'
  note: Confirms the Attendee-Minibadge-2024 folder sits among 29 other official/community minibadge folders in the repo for SAINTCON 2024 (corrected from an earlier overstated "40+"); design-file archive only, no README with specs, no photos.
- kind: url
  url: https://saintcon.org/minibadges/
  title: MiniBadges - SAINTCON
  accessed: '2026-09-10'
  note: General program description - minibadges are ~1in trading-card boards using SAINTCON's own proprietary open-hardware edge connector (not the DEF-CON-style SAO standard), ranging from a single LED to microcontroller-driven displays, collected/traded at SAINTCON (17,000+ show up in a typical year); no attendee-2024-specific details.
- kind: url
  url: https://github.com/lukejenkins/minibadge
  title: lukejenkins/minibadge (community pinout documentation)
  accessed: '2026-09-10'
  note: Community-maintained writeup of the SAINTCON minibadge connector - a proprietary pinout (VBATT, 3.3V, GND, SDA/SCL for I2C/EEPROM ID, a badge-driven CLK line, and 4 PROG pins), distinct from the DEF CON SAO standard; used to correct an earlier "SAO-format" claim in this entry.
research:
  status: verified
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Fact-check pass (2026-09-10): verified the repo folder contents directly via the GitHub API - confirmed KiCad schematic/PCB/project files, a Gerbers subfolder, and Illustrator/SVG layer artwork for this badge, so it is a genuine fabricated design. Corrected two overstated claims from the prior pass: (1) the entry called the minibadge format "SAO-format" in several places, but SAINTCON''s own program page and a community pinout writeup (github.com/lukejenkins/minibadge) describe a proprietary open-hardware connector distinct from the DEF-CON-style SAO standard - reworded functions/body/source notes accordingly. (2) a source note said the repo held "40+" other minibadge folders; the actual repo root has 29. Also downgraded make_your_own.open_source from yes to partial: the folder publishes hardware only (KiCad + Gerbers + artwork), no firmware/code, and the guide''s "yes" requires both hardware and firmware to be published. Opened the "2024" SAINTCON MiniBadge Guide PDF (github.com/utahsaint-org/saintcon.zip.files) referenced but not read in the prior pass: despite its 2024 filename, its content is entirely the 2023 assembly guide (cover reads "Assembly Guide 2023", and it describes "the official attendee minibadge for 2023" - EEPROM-based, no LED, bundled with the badge for a badge game) - not used for any 2024 field since it documents a different year''s board. Still no README, build guide, or photo specific to the 2024 Attendee-Minibadge-2024 design, so mcu/leds/display/price/quantity/availability/colors/shape remain empty rather than guessed.'
last_modified_date: '2026-09-10'
---

Attendee Minibadge 2024 is the official attendee-tier minibadge for SAINTCON 2024, published by the UtahSAINT organizers in the conference's `MiniBadges2024` GitHub repository. SAINTCON's minibadge program is an open-hardware trading-card system: roughly 1-inch boards that plug into the main conference badge over SAINTCON's own proprietary edge connector (not the DEF-CON-style SAO standard), ranging from a bare LED to full microcontroller-driven displays, which attendees collect and trade throughout the event (organizers cite 17,000+ minibadges circulating in a typical year).

The repository folder for this badge contains a complete KiCad project (schematic, PCB layout, and project files), Gerber fabrication files, and Adobe Illustrator/SVG artwork for each board layer, confirming it is a real, fabricated design rather than a placeholder. No firmware or code is included in the folder, no README, build-guide entry, or photograph specific to this badge turned up in the sources checked, so technical specifics (chip, LEDs, display, colors, price, and quantity) are left blank rather than guessed.

## Make your own

Hardware files are published in the official repo: `github.com/utahsaint-org/MiniBadges2024/tree/main/Attendee-Minibadge-2024`, including the KiCad source and ready-to-fab Gerbers.

