---
title: compukidmike/minibadge10x10
id: saintcon-2023-compukidmike-minibadge10x10
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: compukidmike
summary: 'A learn-to-solder practice board for SAINTCON: a 10x10 grid of 200 8-pin headers (1,600+ solder joints) that also doubles as a display/holder for other SAINTCON minibadges once built.'
functions: No electronic function of its own beyond the header grid; it is a soldering exercise and a physical holder for plugging in other 8-pin SAINTCON minibadges.
look:
  colors: []
  shape: rectangle
  themes:
  - learn to solder
  - village badge
tech:
  mcu: PIC (2023 version, requires a programmer); replaced by a 74LV4060D binary ripple-counter/oscillator in the 2024 version, removing the need to program a chip
  leds: null
  display: none
  connectivity:
  - usb
  battery: null
  sao_version: none
get_one:
  price: $30
  price_usd: 30
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold assembled/kit through the MKFactor storefront (mkfactor.com); listed as out of stock when checked 2026-09-07. Produced in batches with restocks after sellouts, per the listing.
make_your_own:
  open_source: true
  hardware_url: https://github.com/compukidmike/minibadge10x10
  firmware_url: https://github.com/compukidmike/minibadge10x10/tree/main/Firmware
  eda_tool: KiCad
links:
- label: github.com/compukidmike/minibadge10x10
  url: https://github.com/compukidmike/minibadge10x10
  kind: repo
- label: 'MKFactor store listing: Saintcon Minibadge 10x10 Board'
  url: https://mkfactor.com/shop/index.php?rt=product/product&product_id=133
  kind: store
images:
- file: assets/images/badges/saintcon-2023/compukidmike-minibadge10x10/dbbbca41ed.jpg
  source: https://mkfactor.com/shop/index.php?rt=product/product&product_id=133
  credit: compukidmike / MKFactor
  caption: Assembled Saintcon Minibadge 10x10 board, front view
- file: assets/images/badges/saintcon-2023/compukidmike-minibadge10x10/d3c734bbf0.jpg
  source: https://mkfactor.com/shop/index.php?rt=product/product&product_id=133
  credit: compukidmike / MKFactor
  caption: Saintcon Minibadge 10x10 board, back view showing solder jumpers
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/compukidmike/minibadge10x10
  title: compukidmike/minibadge10x10
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/minibadge10x10/main/README.md
  title: minibadge10x10 README (2023 version)
  accessed: '2026-09-07'
  note: Confirms it is a SAINTCON soldering project, 200 8-pin headers/1600+ joints, PIC microcontroller, A3910 clock-driver chips, KiCad/Gerber files included.
- kind: url
  url: https://raw.githubusercontent.com/compukidmike/minibadge10x10/main/2024Version/README.md
  title: minibadge10x10 2024 version README
  accessed: '2026-09-07'
  note: 'Documents the 2024 revision: pre-soldered USB-C, solder jumpers removed, TPM8837C clock driver replacing the A3910, and a 74LV4060D oscillator/counter in place of the PIC microcontroller.'
- kind: url
  url: https://mkfactor.com/shop/index.php?rt=product/product&product_id=133
  title: Saintcon Minibadge 10x10 Board - MKFactor shop
  accessed: '2026-09-07'
  note: $30 price, out-of-stock status, batch-production note, shipping details, and product photos (front/back, kit and assembled).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No LED specifics were found in any source; the board appears to have no onboard LEDs of its own (it is a header-grid soldering practice board / minibadge holder). Exact production quantity and license were not stated anywhere found. The repo has both a 2023 version (PIC-based, root of repo) and a 2024 version (74LV4060D-based, in /2024Version); event is set to saintcon-2023 for the original release, with the 2024 revision noted here. No maker profile page (Hackaday.io, social) was found beyond the GitHub account and the MKFactor storefront.
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/compukidmike-minibadge10x10/
model:
  file: assets/models/saintcon-2023/compukidmike-minibadge10x10.glb
  method: gerber
  source_file: SaintconMinibadge10x10-2023Gerbers.zip
  generated: '2026-09-10'
  bytes: 387016
  size_mm:
  - 264.2
  - 264.2
---

The Minibadge 10x10 Board is a SAINTCON learn-to-solder project by compukidmike: a rectangular PCB laid out with 200 8-pin through-hole headers in a 10x10 grid, for a total of more than 1,600 solder joints. Surface-mount parts (including the clock-driver chip and, from 2023 on, the USB connector) come pre-soldered, and the builder solders in the through-hole headers, a button, a power switch, and a screw-terminal block. Once assembled it doubles as a display board: because SAINTCON minibadges plug into 8-pin headers, the finished 10x10 board serves as a rack to hold and show off other minibadges collected at the con.

The board went through at least two revisions. The 2023 version uses a PIC microcontroller (which needs to be programmed) and A3910 clock-driver chips that are tricky to hand-solder without a stencil and reflow oven. The 2024 version simplifies the design: the CLK-driver chip was swapped for the hand-solderable TPM8837C, the PIC was replaced with a 74LV4060D binary ripple-counter/oscillator that needs no programming, and a USB load-switch IC (AP22818BKAWT) was added for overcurrent/short-circuit protection. Full KiCad projects, Gerbers, schematics, and BOMs for both versions are published on GitHub.

The board was sold, assembled or as a kit, through the MKFactor storefront for $30, with production run in batches and restocked after selling out; it was listed as out of stock as of this check. No LED count, onboard display, or a Hackaday/maker-profile page beyond the GitHub repository and store listing were found.
