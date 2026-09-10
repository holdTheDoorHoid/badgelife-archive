---
title: JD-HITBSecConf2018 Beijing Badge
id: hitb-2018-jd-hitbsecconf2018-beijing-badge
layout: badge
parent: Hitbsecconf 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitb-2018
year: 2018
makers:
- name: Hack In The Box
- name: UnicornTeam
  url: https://github.com/UnicornTeam
  role: hardware design
summary: The official electronic badge for JD-HITBSecConf2018 Beijing (HITB2018PEK), built on an MTK-series platform and designed for attendees to reprogram and unlock hidden features at the CommSec Village.
functions: Runs a mini game/challenge called "Are You Human Or Are You Hacker," plus hidden challenges and secret features unlocked at the CommSec Village Badge Village, where organizers taught attendees to reprogram it.
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - hardware tool
tech:
  mcu: MTK series
  leds: null
  display: null
  connectivity:
  - uart
  battery: null
  sao_version: null
get_one:
  price: $35 on-site for non-attendees
  price_usd: 35
  quantity: ''
  availability: sold_out
  availability_note: Distributed at a 2018 event; on-site quantities were described as "extremely limited." Checked 2026-09-08.
  distribution:
  - free_drop
  - purchase
  where: Given to JD-HITBSecConf2018 Beijing attendees; non-attendees could buy one on-site at the free CommSec Village exhibition (Nov 1-2, 2018) for $35 while supplies lasted.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/UnicornTeam/hitb2018pek-badge
  firmware_url: null
  eda_tool: Eagle
links:
- label: badge.gallery/series/hitb
  url: https://badge.gallery/series/hitb
  kind: website
- label: UnicornTeam/hitb2018pek-badge (GitHub)
  url: https://github.com/UnicornTeam/hitb2018pek-badge
  kind: repo
- label: JD-HITBSecConf2018 Beijing - CommSec Village (archived)
  url: https://archive.conference.hitb.org/hitbsecconf2018pek/commsec-village/
  kind: doc
- label: JD-HITBSecConf2018 Beijing (archived event page)
  url: https://archive.conference.hitb.org/hitbsecconf2018pek/
  kind: website
images: []
contact: {}
notes:
- Special-edition HITB2018PEK electronic badge with MTK-series hardware. Found by the event-year sweep, task con-troopers.
- Sweep listed the title as "JD-HITBSecConf2018 Beijing Badge"; the maker/organizer refers to it as the "HITB2018PEK" special edition badge. Kept the sweep title since it matches how badge.gallery indexes it.
status: released
sources:
- kind: url
  url: https://badge.gallery/series/hitb
  title: JD-HITBSecConf2018 Beijing Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-troopers); event read as ''HITBSecConf 2018 Beijing''.'
- kind: url
  url: https://archive.conference.hitb.org/hitbsecconf2018pek/commsec-village/
  title: Technology Exhibition / CommSec Village « JD-HITBSecConf2018 - Beijing
  accessed: '2026-09-08'
  note: 'Official HITB event page: confirms the badge exists, MTK-series platform with 32M flash / 128MB RAM, a display, UART; open-source intent; on-site sale price $35 for non-attendees, limited supply; Badge Village dates Nov 1-2 2018.'
- kind: url
  url: https://github.com/UnicornTeam/hitb2018pek-badge
  title: UnicornTeam/hitb2018pek-badge
  accessed: '2026-09-08'
  note: GitHub repo published by UnicornTeam containing Eagle schematic/board files (HITB_PEK_2018_V1.2.sch/.brd) and a PDF for the badge; identifies UnicornTeam as the hardware designer. No firmware source or images found in the repo.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed as a real item via HITB''s own archived CommSec Village page and a GitHub hardware-design repo published by the org UnicornTeam (unicorn.team). Correction: an earlier draft of this entry claimed UnicornTeam was "the same Qihoo360-affiliated hacker team" credited on the related HITBSecConf2018 Amsterdam badge; checked directly and found unsupported -- the Amsterdam badge''s own repo (github.com/hackersbadge/hitb2018ams) is under a different GitHub org entirely, and UnicornTeam''s own GitHub org profile makes no mention of Qihoo 360. Removed that claim from the body. HITB''s CommSec Village page states the badge "is fully open sourced (both the hardware and software will be provided along with the firmware)" -- a pre-event promise; the actual GitHub repo found contains only Eagle .sch/.brd/.pdf hardware files, no firmware or README, so make_your_own.open_source is kept as partial to reflect what was actually published, not what was promised. Exact LED count, display size/type,
    and battery/power were not stated by any source found, so left empty rather than guessed. No usable photos of the physical badge were found; could not save any images.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/hitb-2018/jd-hitbsecconf2018-beijing-badge.glb
  method: kicad
  source_file: HITB_PEK_2018_V1.2.brd
  generated: '2026-09-10'
  bytes: 294924
---

The JD-HITBSecConf2018 Beijing Badge (HITB2018PEK) was the official electronic badge for the first Hack In The Box Security Conference held in Beijing, co-organized with JD Security in late 2018. Built on an MTK-series microcontroller platform with 32MB of flash and 128MB of RAM, plus a display and a UART header, it was designed from the outset to be opened up and reprogrammed rather than just worn. Hardware design credit on GitHub goes to the org UnicornTeam (unicorn.team), which published the schematic/board files under that name.

At the conference's free CommSec Village / Technology Exhibition (November 1-2, 2018), organizers ran a "Badge Village" where attendees could learn to reprogram the badge and unlock secret features, including a mini game framed as "Are You Human Or Are You Hacker" along with other hidden challenges. Conference attendees received the badge as part of admission; non-attendees could buy one on-site for $35, though HITB described the on-site stock as extremely limited.

## Make your own

UnicornTeam published the hardware design for the badge on GitHub (`UnicornTeam/hitb2018pek-badge`) as Eagle schematic and board files (`HITB_PEK_2018_V1.2.sch` / `.brd`) along with a PDF. No firmware source or bill of materials was found in that repository, so treat the release as hardware-only unless a firmware repo turns up elsewhere.
