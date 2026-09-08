---
title: NorthSec 2022 Badge
id: northsec-2022-northsec-2022-badge
layout: badge
parent: NorthSec 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: northsec-2022
year: 2022
makers:
- name: NorthSec
  url: https://nsec.io/
summary: 'The official electronic badge for NorthSec 2022, the conference''s return to in-person format at Marché Bonsecours in Montreal.'
functions: 'Runs conference challenges/CTF content on the ESP32; RGB LED effects.'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - security
tech:
  mcu: ESP32-WROOM-32
  leds:
    count: 24
    type: WS2811/5050 RGB
    note: Plus additional discrete 0805 red status LEDs.
  display: none
  connectivity:
  - wifi
  - ble
  battery: LiPo (MCP73831 charge controller)
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
  hardware_url: https://github.com/nsec/nsec-badge/tree/2024/hw/2022
  firmware_url: https://github.com/nsec/nsec-badge
  eda_tool: Eagle
links:
- label: badge.gallery/events/northsec-2022
  url: https://badge.gallery/events/northsec-2022
  kind: website
- label: nsec/nsec-badge (hw/2022 on 2024 branch)
  url: https://github.com/nsec/nsec-badge/tree/2024/hw/2022
  kind: repo
- label: NorthSec
  url: https://nsec.io/
  kind: website
images: []
contact: {}
notes:
- Official NorthSec 2022 badge with SAO hardware directories archived in the nsec-badge repo. Found by the event-year sweep, task northsec.
- Sheet/sweep title matched the maker's own wording ("NorthSec 2022 Badge"); no change needed.
status: released
sources:
- kind: url
  url: https://badge.gallery/events/northsec-2022
  title: NorthSec 2022 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:northsec); event read as ''northsec-2022''.'
- kind: url
  url: https://github.com/nsec/nsec-badge
  title: 'nsec/nsec-badge: Software from the NorthSec badge'
  accessed: '2026-09-08'
  note: 'Repository root; no dedicated 2022 branch exists (branches are 2017/2018/2019/2021/2024/master), but the 2024 branch contains a hw/2022 directory with Eagle schematics/boards and per-revision BOMs for the 2022 badge (versions 3e/3f/3g/3j), confirming ESP32 WROOM32 + CH340C USB serial + MCP73831 LiPo charging + AP2112 3.3V regulator + 24x WS2811/5050 RGB LEDs.'
- kind: url
  url: https://badge.gallery/issues/northsec-2022-badge/retrospective-archive-caveat
  title: Retrospective archive caveat for the 2022 badge record
  accessed: '2026-09-08'
  note: 'Confirms the 2022 hardware files were recovered from the repo''s 2024 branch rather than a dedicated 2022 branch, and that NorthSec''s official past-editions page documents 2022 as the return-to-in-person edition at Marché Bonsecours.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'No maker-published photo of the physical 2022 badge was found (badge.gallery explicitly states none is published there for licensing reasons, and no photo turned up in the hw/2022 repo directory - only schematics, BOM spreadsheets, and unrelated challenge-puzzle images). Price, quantity made, and current availability are not stated anywhere found; SAO header version/count not confirmed. The nsec-badge GitHub repo has no branch literally named 2022 - the 2022 hardware lives under hw/2022/ on the 2024 branch, so treat hardware provenance as repository-archive-backed rather than a contemporaneous 2022 release tag.'
last_modified_date: '2026-09-08'
---

The 2022 NorthSec badge was the conference's electronic badge for its return to an in-person event at Marché Bonsecours in Montreal after the pandemic disruption. It is built around an ESP32-WROOM-32 module with a CH340C USB-serial chip, MCP73831 LiPo charge management, and an AP2112 3.3V regulator, and it carries twenty-four WS2811/5050 RGB LEDs alongside smaller discrete status LEDs.

Hardware for the badge (Eagle schematics and board files, several production revisions from V3e through V3j, JLCPCB manufacturing exports, and bills of materials) along with challenge assets are preserved in NorthSec's `nsec-badge` GitHub repository, filed under `hw/2022` on the project's `2024` branch rather than a dedicated 2022 branch. No maker photo of the assembled badge, pricing, or production quantity could be confirmed from the sources checked.
