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
functions: 'Trading-card-style SAO-format board plugged into the SAINTCON badge; part of the official minibadge set attendees collect and trade at the conference.'
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
  open_source: yes
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
  note: Confirms the Attendee-Minibadge-2024 folder sits among 40+ official/community minibadge folders for SAINTCON 2024; design-file archive only, no README with specs, no photos.
- kind: url
  url: https://saintcon.org/minibadges/
  title: MiniBadges - SAINTCON
  accessed: '2026-09-10'
  note: General program description - minibadges are ~1in SAO-format trading-card boards, ranging from a single LED to microcontroller-driven displays, collected/traded at SAINTCON (17,000+ show up in a typical year); no attendee-2024-specific details.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-10'
  notes: 'Confirmed real: the repo folder holds KiCad schematic/PCB, Gerbers, and Illustrator/SVG artwork for this specific badge, so it is a genuine design, not just a search snippet. Could not find a README, build guide entry, or photo specific to this badge, so mcu/leds/display/price/quantity/availability/colors/shape are left empty rather than guessed - the repo contents (KiCad + gerbers only, no firmware) suggest a passive/simple board but that is not stated outright. No raster photo of the finished board was found (repo has only vector/CAD files); a 2024 SAINTCON MiniBadge Guide PDF exists (github.com/utahsaint-org/saintcon.zip.files) that likely documents it but was not opened, staying within the research budget.'
last_modified_date: '2026-09-10'
---

Attendee Minibadge 2024 is the official attendee-tier minibadge for SAINTCON 2024, published by the UtahSAINT organizers in the conference's `MiniBadges2024` GitHub repository. SAINTCON's minibadge program is an open-hardware trading-card system: roughly 1-inch SAO-format boards that plug into the main conference badge, ranging from a bare LED to full microcontroller-driven displays, which attendees collect and trade throughout the event (organizers cite 17,000+ minibadges circulating in a typical year).

The repository folder for this badge contains a complete KiCad project (schematic, PCB layout, and project files), Gerber fabrication files, and Adobe Illustrator/SVG artwork for each board layer, confirming it is a real, fabricated design rather than a placeholder. No README, build-guide entry, or photograph specific to this badge turned up in the sources checked, so technical specifics (chip, LEDs, display, colors, price, and quantity) are left blank rather than guessed.

## Make your own

Hardware files are published in the official repo: `github.com/utahsaint-org/MiniBadges2024/tree/main/Attendee-Minibadge-2024`, including the KiCad source and ready-to-fab Gerbers.

