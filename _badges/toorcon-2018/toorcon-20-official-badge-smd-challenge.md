---
title: ToorCon 20 Official Badge (SMD Challenge)
id: toorcon-2018-toorcon-20-official-badge-smd-challenge
layout: badge
parent: ToorCon 20
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: toorcon-2018
year: 2018
makers:
- name: MakersBox
summary: The official ToorCon 20 (2018) badge, built as a deliberately hard SMD-soldering challenge with hidden codes to decode once assembled.
functions: 'Doubles as a wearable event badge and a soldering challenge: builders hand-solder eight SMD LEDs (down to a 0201 package) and other fine-pitch parts, then hunt for hidden codes and messages worked into the board.'
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - learn to solder
  - ctf
tech:
  mcu: ATtiny84
  leds:
    count: 8
    type: discrete
    note: Includes SMD LEDs down to a 0201 package; LED orientation varies by placement.
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '400 kits'
  availability: unknown
  distribution:
  - kit
  where: Distributed as badge kits at ToorCon 20 (San Diego, 2018).
make_your_own:
  open_source: 'no'
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: The maker (MakersBox) states the gerber files were intentionally destroyed after the run; no public repo or files were found.
links:
- label: hackaday.io/project/25265-an-unfortunate-smd-project/log/152898-official-toorcon-badge
  url: https://hackaday.io/project/25265-an-unfortunate-smd-project/log/152898-official-toorcon-badge
  kind: hackaday
- label: hackaday.io/project/25265-an-unfortunate-smd-project
  url: https://hackaday.io/project/25265-an-unfortunate-smd-project
  kind: hackaday
images:
  - file: assets/images/badges/toorcon-2018/toorcon-20-official-badge-smd-challenge/32009ce5f5.jpg
    source: "https://hackaday.io/project/25265-an-unfortunate-smd-project/log/152898-official-toorcon-badge"
    credit: "MakersBox"
    caption: "Official ToorCon 20 SMD challenge badge"
  - file: assets/images/badges/toorcon-2018/toorcon-20-official-badge-smd-challenge/4592f6758c.jpg
    source: "https://hackaday.io/project/25265-an-unfortunate-smd-project"
    credit: "MakersBox"
    caption: "Project thumbnail, An Unfortunate SMD Project (ToorCon 20 badge)"
contact: {}
notes:
- Official ToorCon 20 (2018) badge built around an ATtiny84 and eight SMD LEDs (including a 0201) as a soldering/SMD challenge. Found by the event-year sweep, task con-toorcon.
- The sweep's sources listed the title as "ToorCon 20 Official Badge (SMD Challenge)"; the maker calls the umbrella Hackaday.io project "An Unfortunate SMD Project" and the badge itself the "Official Toorcon Badge" within it. Kept the sheet's more descriptive title.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/25265-an-unfortunate-smd-project/log/152898-official-toorcon-badge
  title: ToorCon 20 Official Badge (SMD Challenge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-toorcon); event read as ''ToorCon 2018''.'
- kind: url
  url: https://hackaday.io/project/25265-an-unfortunate-smd-project/log/152898-official-toorcon-badge
  title: 'Official Toorcon Badge - log entry, An Unfortunate SMD Project'
  accessed: '2026-09-08'
  note: Confirmed maker (MakersBox), event/year (ToorCon 20, 2018), ATtiny84 MCU, 8 SMD LEDs incl. a 0201, 400 kits made, gerbers destroyed post-run.
- kind: url
  url: https://hackaday.io/project/25265-an-unfortunate-smd-project
  title: An Unfortunate SMD Project (Hackaday.io project page)
  accessed: '2026-09-08'
  note: Parent project page; used for a project thumbnail image and to confirm maker identity.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: Fact-check pass (2026-09-08) re-read both cited Hackaday.io pages and confirmed maker (MakersBox), ATtiny84 MCU, 8 SMD LEDs (one 0201), 400 kits, gerbers destroyed, hidden codes/puzzle framing, and the heart/cat artwork with per-side LED orientation. Corrected get_one.availability from "sold_out" (unsupported by any source) to "unknown" — no source states current availability; this was a one-time 2018 con kit distribution, not an ongoing storefront listing. Confirmed San Diego as the event location via a web search of toorcon.net. Display, connectivity, battery, and price remain genuinely unknown; left empty rather than guessed. Both saved images verified present on disk and matched to their cited source pages.
last_modified_date: '2026-09-08'
---

The Official ToorCon 20 badge, made by MakersBox for the 2018 ToorCon conference in San Diego, is both a wearable event badge and a deliberately punishing SMD soldering challenge. Roughly 400 kits were produced, each built around an ATtiny84 microcontroller driving eight surface-mount LEDs of varying, awkward sizes — down to a 0201 package — with LED orientation changing depending on where each part sits on the board's heart/cat artwork.

Beyond the soldering difficulty itself, the badge hides "codes in all sorts of places" for builders to find once assembled, turning the SMD challenge into a small puzzle on top of a hardware-skills test. The maker has said the badge's gerber files were intentionally destroyed after the ToorCon 20 run, so the design was never open-sourced and no build files are publicly available.

Pricing was not stated in the source material, and no independent (non-maker) coverage of the badge was found; the account here rests on MakersBox's own Hackaday.io project log.
