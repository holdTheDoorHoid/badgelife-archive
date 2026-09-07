---
title: Power Glove
id: dc32-power-glove
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: NilbinSec
  url: https://x.com/nilbinsec/
summary: A passive, LED-only SAO shaped after the Nintendo Power Glove, with flashing RGB and red LEDs and no microcontroller.
functions: Blinks three RGB LEDs (fast- or slow-flashing variants) plus one red THT LED; purely decorative, no logic or games.
look:
  colors:
  - grey
  - black
  shape: glove
  themes:
  - console
  - pop culture
tech:
  mcu: none
  leds:
    count: 4
    type: RGB SMD + discrete
    note: 3x 0805/0807 flashing RGB SMD LEDs (slow or fast variant) and 1x 5mm red THT LED; no driver IC, LEDs self-flash.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v2
  sao_ports: 1
get_one:
  price: Free!!
  price_usd: 0.0
  quantity: '250'
  availability: free
  availability_note: Checked 2026-09-06; not a storefront item, was a free con drop.
  distribution:
  - free_drop
  where: Given away at DEF CON 32 (2024); the maker also posted a firmware-free re-release of the design for DC34.
make_your_own:
  open_source: true
  hardware_url: https://github.com/NilbinSec/DC32-Power-Glove-SAO
  firmware_url: null
  gerbers_url: https://github.com/NilbinSec/DC32-Power-Glove-SAO/tree/main/gerbers
  bom_url: https://github.com/NilbinSec/DC32-Power-Glove-SAO/blob/main/README.md
  eda_tool: null
  license: null
  notes: No firmware — the board is a passive LED circuit with no MCU. Gerber layer naming (F_Cu/B_Cu/.gbrjob) looks like standard KiCad export, but the repo does not state the EDA tool, so it is left blank.
links:
- label: x.com/nilbinsec
  url: https://x.com/nilbinsec/
  kind: social
- label: DC32-Power-Glove-SAO (GitHub)
  url: https://github.com/NilbinSec/DC32-Power-Glove-SAO
  kind: repo
images:
- file: assets/images/badges/dc32/power-glove/0848dc141a.jpg
  source: https://github.com/NilbinSec/DC32-Power-Glove-SAO
  credit: NilbinSec
  caption: Assembled Power Glove SAO
- file: assets/images/badges/dc32/power-glove/a957c1f4cb.jpg
  source: https://github.com/NilbinSec/DC32-Power-Glove-SAO
  credit: NilbinSec
  caption: Power Glove SAO, alternate angle showing LEDs
contact: {}
notes:
- Badge drops will be regularly announced via our twitter https://x.com/nilbinsec/ and other social media.
status: released
sources:
- kind: sheet
  event: dc32
  row: 79
  updated: '2024-05-31'
- kind: url
  url: https://github.com/NilbinSec/DC32-Power-Glove-SAO
  title: NilbinSec/DC32-Power-Glove-SAO
  accessed: '2026-09-06'
  note: Primary source for description, BOM, LED count, assembly notes, SAO header type, gerbers, and photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: The community sheet listed this as type "badge" but the maker's own repo describes it as an SAO (2x3 shrouded SAO header, no independent power/enclosure), so type was corrected to sao. No firmware exists — it is a passive blinky circuit, so tech.mcu is none and firmware_url is empty. EDA tool and license are not stated in the repo and were left blank rather than guessed. Could not confirm exact quantity beyond the sheet's "250" or find independent press coverage; the GitHub repo and its README were the only source located. The maker later did a "Power Glove Re-release" at DC34 (separate existing entry, not this one).
last_modified_date: '2026-09-06'
related:
- dc34-power-glove-re-release
---

The Power Glove is a free SAO NilbinSec gave away at DEF CON 32 (2024), styled after the classic Nintendo Power Glove accessory. It has no microcontroller: three flashing RGB SMD LEDs and one red through-hole LED do all the work, wired directly off the host badge's power through a standard 2x3 shrouded SAO header, so it just blinks on its own once plugged in.

NilbinSec published the full hardware — gerbers, BOM, and assembly photos — on GitHub, recommending a grey soldermask with black silkscreen (HASL, with ENIG as a gold-accent option) and noting PCBBuy.com as the fab they found with the right color options at a reasonable price. There is no firmware repository because the board carries no programmable chip.

## Make your own

1. Fabricate from the [gerbers](https://github.com/NilbinSec/DC32-Power-Glove-SAO/tree/main/gerbers) in the repo; grey soldermask with black silkscreen matches the original (HASL finish, or ENIG if you want gold text).
2. Populate per the BOM: 2x 0805 470Ω resistors, 3x 0807 flashing RGB SMD LEDs (fast or slow variant both work), 1x 5mm red THT LED, and 1x 2x3 shrouded SAO header.
3. Watch LED orientation: the SMD LED cathodes face right, the THT LED's cathode faces left.
4. Plug into any badge with a standard SAO header — no programming needed.
