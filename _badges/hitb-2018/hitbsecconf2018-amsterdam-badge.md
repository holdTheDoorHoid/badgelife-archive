---
title: HITBSecConf2018 Amsterdam Badge
id: hitb-2018-hitbsecconf2018-amsterdam-badge
layout: badge
parent: Hitbsecconf 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitb-2018
year: 2018
makers:
- name: Qihoo360 Unicorn Team
  url: https://github.com/hackersbadge/hitb2018ams
summary: The official electronic badge for HITBSecConf2018 Amsterdam, built around an STM32F103 with a 1.3" OLED, RF/IR receivers, and six RGB LEDs for a packet-decoding badge game.
functions: Badge Village game involving decoding 433MHz and IR packets, plus mini-games and hidden challenges; firmware is reprogrammable.
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - village badge
tech:
  mcu: STM32F103
  leds:
    count: 6
    type: RGB
    note: ''
  display: 1.3" OLED
  connectivity:
  - ir
  - sub-ghz
  battery: null
  sao_version: null
get_one:
  price: Free to registered attendees; €35 on-site for non-attendees (extremely limited supply)
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  - purchase
  where: Distributed to all registered HITBSecConf2018 Amsterdam attendees at the CommSec Village; a limited number sold on-site to walk-ins.
make_your_own:
  open_source: true
  hardware_url: https://github.com/hackersbadge/hitb2018ams/tree/master/pcb
  firmware_url: https://github.com/hackersbadge/hitb2018ams/tree/master/src
  eda_tool: null
links:
- label: badge.gallery/series/hitb
  url: https://badge.gallery/series/hitb
  kind: website
- label: hackersbadge/hitb2018ams (GitHub)
  url: https://github.com/hackersbadge/hitb2018ams
  kind: repo
- label: 'HITBSecConf2018 Amsterdam: Technology Exhibition / CommSec Village'
  url: https://archive.conference.hitb.org/hitbsecconf2018ams/commsec-village/
  kind: website
images:
- file: assets/images/badges/hitb-2018/hitbsecconf2018-amsterdam-badge/3718a11278.jpg
  source: https://github.com/hackersbadge/hitb2018ams
  credit: hackersbadge (WhiteA10n3/KLKS/xwings)
  caption: Assembled HITB2018 Amsterdam badge PCB
- file: assets/images/badges/hitb-2018/hitbsecconf2018-amsterdam-badge/c1ddd67424.jpg
  source: https://github.com/hackersbadge/hitb2018ams
  credit: hackersbadge (WhiteA10n3/KLKS/xwings)
  caption: HITB2018 Amsterdam badge, alternate angle
contact: {}
notes:
- Electronic HITB Amsterdam 2018 badge tied to the Badge Village games. Found by the event-year sweep, task con-troopers.
- Sheet/sweep wording matched the maker's own naming; no title change needed.
status: released
sources:
- kind: url
  url: https://badge.gallery/series/hitb
  title: HITBSecConf2018 Amsterdam Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-troopers); event read as ''HITBSecConf 2018 Amsterdam''.'
- kind: url
  url: https://archive.conference.hitb.org/hitbsecconf2018ams/commsec-village/
  title: Technology Exhibition / CommSec Village « HITBSecConf2018 - Amsterdam
  accessed: '2026-09-08'
  note: Official conference page confirming maker, free distribution to attendees, €35 walk-in price, and Badge Village game concept.
- kind: url
  url: https://github.com/hackersbadge/hitb2018ams
  title: 'hackersbadge/hitb2018ams: Badge for Hack In The Box 2018 Amsterdam'
  accessed: '2026-09-08'
  note: Open-source hardware/firmware repo; confirmed STM32F103 MCU, W25Q32 flash, 1.3" OLED, 433MHz/IR receivers, six buttons, six RGB LEDs, and design credits (WhiteA10n3 hardware; KLKS/xwings firmware). Source of the two saved photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (maker, hardware, distribution) confirmed by the official HITB conference page and the maker's own open-source GitHub repo. Exact production quantity and post-event availability status not stated anywhere found, left empty/unknown.
last_modified_date: '2026-09-10'
model:
  file: assets/models/hitb-2018/hitbsecconf2018-amsterdam-badge.glb
  method: kicad
  source_file: HITB_AMS_V1.3.brd
  generated: '2026-09-10'
  bytes: 175328
---

The HITBSecConf2018 Amsterdam badge was the official electronic badge for the conference's CommSec Village, designed by the Qihoo360 Unicorn Team and given free to every registered attendee (a limited run was also sold on-site to walk-ins for €35). Built around an STM32F103 microcontroller with a 1.3" OLED display, W25Q32 flash, a 433MHz RF receiver, an IR receiver, six directional buttons, and six RGB LEDs, the badge doubled as a game piece: attendees used it in the Badge Village to decode 433MHz and IR packets, chase hidden challenges, and unlock mini-games.

Hardware and firmware were fully open-sourced on GitHub under the `hackersbadge` account, with PCB design credited to WhiteA10n3 and firmware to KLKS (with a partial contribution from xwings). The repo includes schematics/layout, firmware source, and photos of the assembled board.

## Make your own

The `hackersbadge/hitb2018ams` GitHub repository (https://github.com/hackersbadge/hitb2018ams) contains the PCB design files under `pcb/` and the firmware source under `src/`, along with a README describing the hardware. No specific EDA tool or license was stated in the material reviewed.
