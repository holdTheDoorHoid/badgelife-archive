---
title: SAO Up / SAO Bridge (Supercon 2024 badge adapter PCBs)
id: supercon-2024-sao-up-sao-bridge-supercon-2024-badge-adapter-pcbs
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2024
year: 2025
makers:
- name: Adrian Studer
  url: https://github.com/astuder
summary: A pair of small open-source PCBs that fix awkward SAO port placement on the Hackaday Supercon 2024 badge, reorienting or adding SAO slots.
functions: 'SAO Up rotates a badge SAO port 90 degrees so an add-on sits upright instead of at an angle; SAO Bridge spans the two midline SAO ports to add a seventh, center-mounted SAO slot (wired to power and I2C from the left-side bus) and uprights the two side ports it bridges.'
look:
  colors: [green]
  shape: null
  themes: [hardware tool]
tech:
  mcu: none
  leds: null
  display: null
  connectivity: [i2c]
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not sold; design files published on GitHub for anyone to fabricate themselves.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/astuder/supercon8-sao-adapters
  firmware_url: null
  eda_tool: KiCad
  license: CERN-OHL-P
  notes: 'Repo includes both board designs; boards were manufactured in green rather than the badge''s black due to production timeline constraints.'
links:
- label: hackaday.com/2025/01/13/clever-pcbs-straighten-out-the-supercon-sao-badge
  url: https://hackaday.com/2025/01/13/clever-pcbs-straighten-out-the-supercon-sao-badge/
  kind: article
- label: github.com/astuder/supercon8-sao-adapters
  url: https://github.com/astuder/supercon8-sao-adapters
  kind: repo
images:
- file: assets/images/badges/supercon-2024/sao-up-sao-bridge-supercon-2024-badge-adapter-pcbs/bf18e124c4.jpg
  source: "https://hackaday.com/2025/01/13/clever-pcbs-straighten-out-the-supercon-sao-badge/"
  credit: "Adrian Studer / Hackaday"
  caption: "SAO Up and SAO Bridge adapter PCBs mounted on the Supercon 2024 badge"
- file: assets/images/badges/supercon-2024/sao-up-sao-bridge-supercon-2024-badge-adapter-pcbs/1c22d9689e.jpg
  source: "https://github.com/astuder/supercon8-sao-adapters"
  credit: "Adrian Studer"
  caption: "SAO Up and SAO Bridge adapters installed on the Supercon 2024 badge, comparison view"
contact: {}
notes:
- 'Two adapter designs: ''SAO Up'' rotates a port 90°, ''SAO Bridge'' adds a 7th port across two midline ports'
status: released
sources:
- kind: url
  url: https://hackaday.com/2025/01/13/clever-pcbs-straighten-out-the-supercon-sao-badge/
  title: SAO Up / SAO Bridge (Supercon 2024 badge adapter PCBs)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''Hackaday Supercon 2024 badge''.'
- kind: url
  url: https://hackaday.com/2025/01/13/clever-pcbs-straighten-out-the-supercon-sao-badge/
  title: 'Clever PCBs Straighten Out The Supercon SAO Badge'
  accessed: '2026-09-07'
  note: 'Confirmed maker, what each board does, CERN-OHL-P license, and pulled feature/detail image URLs.'
- kind: url
  url: https://github.com/astuder/supercon8-sao-adapters
  title: 'astuder/supercon8-sao-adapters'
  accessed: '2026-09-07'
  note: 'Confirmed the badge had 6 SAO slots (4 awkwardly angled, center unused), how SAO Bridge wires its center port, and that boards were fabbed green instead of black due to timeline.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Verification pass 2026-09-07: re-fetched both cited sources (Hackaday article and the astuder/supercon8-sao-adapters GitHub README) and confirmed maker, both boards'' functions, the power/I2C wiring of the SAO Bridge center port, CERN-OHL-P license, KiCad files (sao-up.kicad_pcb/sao-bridge.kicad_pcb present in-repo), and the green-vs-black JLCPCB timeline detail, all word-for-word consistent with the entry. Both saved images were confirmed against their source pages: image 1 matches hackaday.com/wp-content/uploads/2025/01/saoadapt_feat.jpg exactly (same photo, same resolution) and image 2 matches a higher-resolution version of the GitHub repo''s img/s8-badge.jpg (same composite photo, downscaled) - both genuinely depict this item. Removed tech.sao_version (was set to v1.69bis): neither cited source names a SAO spec version, and the 2024 Supercon badge repo README/hardware folder available online does not confirm that label either, so it was an unsupported inference and has been blanked per the no-invent rule. No price, quantity, or sale listing found; these appear to be a design the maker published for others to fabricate rather than a sold product, so get_one fields are left mostly empty. No LED/display info applies (passive adapter PCBs, no MCU). Could not find a personal site/Hackaday.io profile for Adrian Studer beyond the GitHub repo link. Everything else in the entry is supported by the cited sources.'
last_modified_date: '2026-09-07'
---

Adrian Studer designed these two small adapter PCBs to fix a layout quirk on the Hackaday Supercon 8 (2024) conference badge, whose "organic flower" shape left several of its six SAO (Simple Add-On) header slots pointing at awkward angles, with the center of the board unused. **SAO Up** is a simple right-angle board that rotates a single SAO port 90 degrees so an add-on sits upright; because the pinout is symmetric, the same board works on either side of the badge depending on which header rows get populated. **SAO Bridge** is a wavier board that bridges the badge's two midline SAO ports, straightening both of them while adding a brand-new seventh SAO connector in the center, powered and addressed over the same I2C bus as the left-side port it taps.

Both designs are released as open hardware under the CERN-OHL-P license via Studer's GitHub repository, with KiCad source files anyone can fabricate for themselves; there's no indication these were sold or distributed as finished kits. The published boards were run in green PCB rather than the badge's black finish, a compromise the write-up attributes to manufacturing lead time.

Hackaday covered the project in a January 2025 article shortly after that year's Supercon, which is where this entry's images and most of the descriptive detail come from.
