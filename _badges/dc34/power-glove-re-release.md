---
title: Power Glove Re-release
id: dc34-power-glove-re-release
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: NilbinSec
  url: https://x.com/nilbinsec
summary: A free re-release of NilbinSec's DC32 Power Glove SAO, a passive Nintendo-Power-Glove-shaped add-on with RGB and red LED accents.
functions: Decorative/blinky SAO; no MCU or interactivity, just LED accents (no known badge-challenge tie-in for this specific reprint).
look:
  colors:
  - grey
  - black
  - red
  shape: glove
  themes:
  - console
  - pop culture
  - retro computer
tech:
  mcu: none
  leds:
    count: 4
    type: RGB
    note: 3x 0807 SMD slow/fast-flashing RGB LEDs plus 1x 5mm red cloudy THT LED.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: FREE! We are giving away 500x Power Glove SAOs at DEF CON. Drops will be announced on Social Media as well as at the Badgelife VIllage.
  price_usd: 0.0
  quantity: '500'
  availability: free
  availability_note: 'Checked 2026-09-06: no separate storefront listing found; distributed as a free con drop, not sold.'
  distribution:
  - free_drop
  where: Free drops announced via NilbinSec's social media (@NilbinSec) and in person at the Badgelife Village at DEF CON 34.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/NilbinSec/DC32-Power-Glove-SAO
  firmware_url: null
  gerbers_url: https://github.com/NilbinSec/DC32-Power-Glove-SAO/tree/main/gerbers
  eda_tool: null
  license: null
  notes: Gerbers and a BOM are published under the original DC32-Power-Glove-SAO repo; no schematic/PCB source files or firmware are included (the board has no MCU).
links:
- label: DC32-Power-Glove-SAO (GitHub, hardware source for this design)
  url: https://github.com/NilbinSec/DC32-Power-Glove-SAO
  kind: repo
- label: x.com/nilbinsec
  url: https://x.com/nilbinsec/
  kind: social
images:
- file: assets/images/badges/dc34/power-glove-re-release/0848dc141a.jpg
  source: "https://github.com/NilbinSec/DC32-Power-Glove-SAO"
  credit: "NilbinSec"
  caption: "Assembled Power Glove SAO"
- file: assets/images/badges/dc34/power-glove-re-release/a957c1f4cb.jpg
  source: "https://github.com/NilbinSec/DC32-Power-Glove-SAO"
  credit: "NilbinSec"
  caption: "Power Glove SAO PCB, assembled"
contact:
  discord: '@nferno2'
  emails:
  - nilbinsec@gmail.com
  handles:
  - '@nilbinsec'
  raw:
  - on all the socials
notes:
- 'Sheet listed this as a "Re-release"; it is the same board as the maker''s dc32-power-glove entry (id: dc32-power-glove), reprinted and given away again at DC34.'
status: listed
sources:
- kind: sheet
  event: dc34
  row: 6
  updated: 5/25/2026 19:58:39
  listing: New
- kind: url
  url: https://github.com/NilbinSec/DC32-Power-Glove-SAO
  title: NilbinSec/DC32-Power-Glove-SAO
  accessed: '2026-09-06'
  note: Confirms this is a re-release of the DC32 Power Glove SAO; source of BOM, PCB fab notes (grey soldermask/black silkscreen), LED count/type, 6-pin shrouded SAO header, and gerbers/photos.
- kind: url
  url: https://forum.defcon.org/node/253031
  title: 'Introducing Hack ''Em Crack ''Em Robots! - DEF CON Forums'
  accessed: '2026-09-06'
  note: NilbinSec's own DC34 announcement (badge + SAO plans, ~800 SAOs planned, drops announced over social media); does not name the Power Glove reprint specifically but corroborates the free social-media-drop distribution model.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: No dedicated DC34 page or storefront listing for this specific reprint was found; all technical detail comes from the original DC32-Power-Glove-SAO GitHub repo, which the sheet listing's "Re-release" title matches. No MCU, no firmware, no functions/game tie-in confirmed for the DC34 batch specifically -- treated as identical hardware to DC32. eda_tool and license are not stated in the repo (only gerbers + a README are published, no schematic source).
last_modified_date: '2026-09-06'
---

NilbinSec's Power Glove SAO is a small, passive add-on shaped after the Nintendo Power Glove, first produced for DEF CON 32 and reprinted for a free giveaway at DEF CON 34. The board carries no microcontroller: three SMD RGB LEDs (slow/fast-flashing) and a single 5mm red LED provide the blinky effect, powered entirely through the host badge's 6-pin SAO connector. NilbinSec fabricated the original run on a grey soldermask with black silkscreen (HASL finish) and published the BOM and Gerbers on GitHub.

For DEF CON 34, NilbinSec planned to give away 500 of these SAOs for free, with drops announced over social media (@NilbinSec) and in person at the Badgelife Village, alongside their other DC34 SAOs and their first full badge, "Hack 'Em Crack 'Em Robots." No DC34-specific storefront listing, firmware, or new functionality was found for this particular reprint; it appears to be the same hardware as the maker's DC32 release, given a new production run.

## Make your own

Gerbers and a bill of materials are published in the `DC32-Power-Glove-SAO` GitHub repo: 2x 0805 470-ohm resistors, 3x 0807 slow/fast-flashing RGB SMD LEDs, 1x 5mm red cloudy THT LED, and a 2x3 shrouded SAO header. The README notes PCBWay as a fab that could match the intended grey/black color scheme, and gives LED orientation (SMD cathodes facing right, the through-hole LED's cathode facing left). No schematic source file or firmware is included, since the board has no active components.
