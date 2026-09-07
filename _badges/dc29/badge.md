---
title: DEF CON 29 Badge
id: dc29-badge
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: MK Factor
  url: https://mkfactor.com/
summary: The official DEF CON 29 human badge, a four-key RGB mechanical macro pad that plugs into a computer over USB-C and doubles as a badge-hacking puzzle.
functions: Four hot-swappable Gateron Blue mechanical switches with custom relegendable keycaps, plus three capacitive touch pads wired as a volume slider. Ships pre-configured to work with Discord (mic mute, emotes). Firmware updates via UF2 drag-and-drop. Edge connectors on each side let badges link to one another (or via USB) as part of an on-badge hacking challenge for attendees.
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
tech:
  mcu: ATSAMD21G16B
  leds:
    count: 4
    type: RGB
    note: one per keyswitch
  display: none
  connectivity:
  - usb
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to registered in-person ("human") attendees at DEF CON 29 as the official conference badge; not sold as a separate product.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: podcasts.apple.com/us/podcast/designing-the-def-con-29-30-badges-feat-mk-factor/id1631571024?i=1000570121133
  url: https://podcasts.apple.com/us/podcast/designing-the-def-con-29-30-badges-feat-mk-factor/id1631571024?i=1000570121133
  kind: video
- label: Hands On - DEF CON 29 Badge Embraces The New Normal (Hackaday)
  url: https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
  kind: article
  archived: https://web.archive.org/web/20260825225844/https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
- label: Making the DEF CON 29 Badge - Michael & Katie Whiteley (DEF CON talk slides, InfoconDB)
  url: https://infocondb.org/con/def-con/def-con-29/making-the-def-con-29-badge
  kind: doc
- label: DEF CON 29 Badge Hacking (DEF CON forums thread)
  url: https://forum.defcon.org/node/238291
  kind: website
  archived: https://web.archive.org/web/20250917120037/https://forum.defcon.org/node/238291
- label: MK Factor
  url: https://mkfactor.com/
  kind: website
  archived: https://web.archive.org/web/20260614164003/http://mkfactor.com/
images:
- file: assets/images/badges/dc29/badge/4933adf90d.jpg
  source: https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
  credit: Hackaday
  caption: Front of the DEF CON 29 badge, a four-key RGB macro pad
  archived: https://web.archive.org/web/20260825225844/https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
- file: assets/images/badges/dc29/badge/69e96466e4.jpg
  source: https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
  credit: Hackaday
  caption: Rear of the DEF CON 29 badge showing the PCB
  archived: https://web.archive.org/web/20260825225844/https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
contact: {}
notes:
- Hacker Hangouts podcast episode 'Designing the DEF CON 29 & 30 Badges (feat. MK Factor)', released 2022-07-16; covers the DEF CON Call for Badge Makers process, idea generation, hardware/software design and logistics for the official DEF CON 29 badge.
status: released
sources:
- kind: url
  url: https://podcasts.apple.com/us/podcast/designing-the-def-con-29-30-badges-feat-mk-factor/id1631571024?i=1000570121133
  title: DEF CON 29 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: video-podcast); event read as ''DEF CON 29''.'
- kind: url
  url: https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
  title: 'Hands On: DEF CON 29 Badge Embraces The New Normal'
  accessed: '2026-09-07'
  note: Primary hands-on writeup; source for MCU (ATSAMD21G16B), switches, keycaps, touch volume slider, USB-C, CR2032, UF2 firmware, and badge images.
  archived: https://web.archive.org/web/20260825225844/https://hackaday.com/2021/08/05/hands-on-def-con-29-badge-embraces-the-new-normal/
- kind: url
  url: https://infocondb.org/con/def-con/def-con-29/making-the-def-con-29-badge
  title: Making the DEF CON 29 Badge (DEF CON 29 talk)
  accessed: '2026-09-07'
  note: Confirms makers Michael and Katie Whiteley (MK Factor) gave an official talk on designing the badge.
- kind: url
  url: https://mkfactor.com/
  title: MK Factor
  accessed: '2026-09-07'
  note: Maker studio site (Michael and Katie Whiteley); page did not list the DC29 badge specifically but confirms the studio and its other con badges.
  archived: https://web.archive.org/web/20260614164003/http://mkfactor.com/
- kind: url
  url: https://github.com/SkarDude/DC29-Badge
  title: SkarDude/DC29-Badge (GitHub)
  accessed: '2026-09-07'
  note: Checked for an official hardware/firmware repo; this is a third-party puzzle-solving writeup, not MK Factor's own files, so make_your_own fields were left empty.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core hardware facts (MCU, switches, battery, USB-C, touch volume slider) confirmed by Hackaday's hands-on writeup. No maker-published hardware/firmware repo, price, or production quantity found, so those fields are left empty. Badge was included with in-person conference admission rather than sold separately, hence get_one fields are sparse. look.colors/shape and tech.sao_version left null/empty; no source described the badge's color scheme, exact shape, or confirmed an SAO header. Distinct from the later "Lie Detector Badge" (DC31), which the archive already lists as a re-release of this DC29 badge concept.
last_modified_date: '2026-09-07'
---

The DEF CON 29 (2021) human badge was designed by MK Factor, the husband-and-wife badge-making studio of Michael and Katie Whiteley, for the first in-person DEF CON held after the pandemic shutdown. Rather than the usual purely decorative PCB, it doubled as a working accessory: a four-key mechanical macro pad with hot-swappable Gateron Blue switches under custom relegendable keycaps (attendees could slot in their own printed artwork), plus three capacitive touch pads wired up as a volume slider. Out of the box it was configured to work with Discord, letting remote and in-person attendees alike mute a microphone or fire off emotes with a keypress, which suited a con that ran in a hybrid format that year.

Under the hood is an Atmel/Microchip ATSAMD21G16B, a 32-bit ARM Cortex-M0+ microcontroller, running on a CR2032 coin cell and updated via drag-and-drop UF2 firmware files. Edge connectors on the badge's sides let units link to each other (or connect over USB) as part of an on-badge hacking puzzle that attendees worked through during the conference, and MK Factor later discussed the badge's design and production, including chip-shortage era manufacturing constraints, on the DEF CON 29 stage and in a 2022 podcast interview.

No maker-published hardware or firmware repository, retail price, or production quantity was found; the badge was distributed to registered in-person attendees as their conference badge rather than sold as a separate product. The GitHub repo often linked alongside this badge (`SkarDude/DC29-Badge`) is a third party's writeup of solving the badge puzzle, not MK Factor's own design files.
