---
title: maibadge-cab
id: dc34-maibadge-cab
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Hackin7 (HCKBADGES)
  url: https://github.com/maibadge
summary: A maimai arcade-cabinet-shaped electronic badge from the MaiBadge project, sold by Hackin7 (HCKBADGES) via Uberflux for DEF CON 34.
functions: 'OLED models cycle through character face art and GIFs and can play back songs; non-OLED models play simple tones. Two buttons ("ADVANCE" and "SELECT") drive an on-badge face/menu UI.'
look:
  colors: []
  shape: arcade cabinet
  themes:
  - arcade
  - music
tech:
  mcu: ESP32-S3 (YD ESP32-S3 N16R8)
  leds:
    count: 1
    type: addressable RGB
    note: single addressable pixel driven from a dedicated GPIO
  display: OLED (SPI, on OLED variant only)
  inputs:
  - buttons
get_one:
  price: $40 (OLED) / $20 (no-OLED)
  price_usd: 40
  quantity: ''
  availability: available
  availability_note: 'Checked 2026-09-07: Uberflux listed 19 of 22 OLED units and all 10 no-OLED units still in stock.'
  distribution:
  - purchase
  where: Sold directly through the Uberflux online store (uberflux.com), listed under the HCKBADGES/Hackin7 storefront.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/maibadge/maibadge_machine_pcb
  firmware_url: https://github.com/maibadge/maibadge/tree/main/code/circuitpython-full-slop-port
  eda_tool: KiCad
  notes: 'Firmware is CircuitPython; select the "machine_v2" board profile (vs. the bear-shaped "bear_v1") in settings.toml before uploading. See MANUAL_UPLOAD.md in the firmware repo for install steps.'
links:
- label: uberflux.com/product/HCK-maibadge-cab
  url: https://uberflux.com/product/HCK-maibadge-cab
  kind: store
- label: github.com/maibadge/maibadge
  url: https://github.com/maibadge/maibadge
  kind: repo
  note: Main MaiBadge firmware/PCB monorepo (covers both bear- and machine-shaped boards).
- label: github.com/maibadge/maibadge_machine_pcb
  url: https://github.com/maibadge/maibadge_machine_pcb
  kind: repo
  note: KiCad PCB source for the machine (arcade-cabinet)-shaped variant that "maibadge-cab" is.
images:
  - file: assets/images/badges/dc34/maibadge-cab/96a0a30ca5.jpg
    source: "https://uberflux.com/product/HCK-maibadge-cab"
    credit: "Hackin7 / Uberflux"
    caption: "maibadge-cab (machine-shaped MaiBadge) product listing photo"
contact: {}
notes:
- 'Uberflux. $40, status: upcoming drop.'
status: released
sources:
- kind: url
  url: https://uberflux.com/product/HCK-maibadge-cab
  title: maibadge-cab
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/HCK-maibadge-cab
  title: maibadge-cab - Uberflux product page
  accessed: '2026-09-07'
  note: 'Confirmed DEF CON 34 event, $40/$20 two-variant pricing (OLED vs no-OLED), stock counts, and product photo.'
- kind: url
  url: https://github.com/maibadge/maibadge
  title: maibadge/maibadge - GitHub
  accessed: '2026-09-07'
  note: 'Confirms open-source CircuitPython firmware, two board shapes (bear_v1, machine_v2), and project name "MaiBadge".'
- kind: url
  url: https://github.com/maibadge/maibadge/blob/main/code/circuitpython-full-slop-port/boards/machine_v2.py
  title: machine_v2.py board profile
  accessed: '2026-09-07'
  note: 'Source of MCU (ESP32-S3 / YD ESP32-S3 N16R8), display/LED/buzzer pinout, and two-button (ADVANCE/SELECT) control scheme for the machine-shaped board.'
- kind: url
  url: https://github.com/maibadge/maibadge_machine_pcb
  title: maibadge/maibadge_machine_pcb - GitHub
  accessed: '2026-09-07'
  note: 'KiCad PCB source repo for the machine-shaped variant.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'maibadge-cab is the machine (arcade-cabinet)-shaped variant of the open-source "MaiBadge" project (maimai rhythm-game themed), made by Hackin7/HCKBADGES for DEF CON 34 (Aug 2026) and sold via Uberflux. The other shape in the same project, "bear_v1", is not this listing. Exact LED part number, battery/power source, and total production quantity were not stated by any source and are left blank. Confidence is medium: the store listing and GitHub repos corroborate each other well, but no independent (press/forum) coverage of this specific item was found.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/maibadge-cab/
---

The maibadge-cab is the arcade-cabinet-shaped variant of MaiBadge, an open-source electronic badge project themed after Sega's maimai rhythm-game cabinets. It was made by Hackin7, operating the HCKBADGES storefront, and sold for DEF CON 34 (August 2026) through the Uberflux marketplace in two configurations: a $40 version with an OLED display that shows character faces and animated GIFs, and a cheaper $20 version without a display that instead plays simple tones through an onboard buzzer.

Under the hood the machine-shaped board runs on an ESP32-S3 (YD ESP32-S3 N16R8 module) with CircuitPython firmware shared with a second, bear-shaped MaiBadge variant from the same project; the firmware picks between the two via a board-profile setting. The badge is controlled with two buttons (labeled ADVANCE and SELECT) that step through faces and menus, and carries a single addressable RGB LED alongside the buzzer.

Both the PCB design (KiCad) and the CircuitPython firmware are published on GitHub under the maibadge GitHub org, making this a fully open-source badge; the machine-shaped PCB has its own repository separate from the shared firmware/bear-PCB monorepo.
