---
title: Cyber Clippy Badge
id: dc30-cyber-clippy-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: El Jefe De Security
  url: https://github.com/eljefedsecurit
- name: Adrian Bonar
  url: https://github.com/adrianwyatt
  role: contributor
summary: A Clippy-shaped PCB badge made by Microsoft's Office of the CTO Maker Incubation Team for DEF CON 30. Fifty of the 500 badges made came bundled with a full Azure Sphere kit running an Altair 8800 emulator for a hacking/puzzle contest with prizes.
functions: 'The plain art badge is a Clippy-shaped PCB. The 50 "competition" units each shipped with an Azure Sphere board, an "8800 Retro-click" Altair 8800 emulator, a 32GB SD card, standoffs, and a 5000mAh USB power pack; entrants connected to a web terminal over a socket server to explore a CP/M-based Altair emulator, solve hidden ciphers and morse-code clues, and race to be one of the first 5 (or next 5) to finish for prizes.'
look:
  colors: []
  shape: paperclip (Clippy mascot)
  themes:
  - pop culture
  - meme
tech:
  mcu: Azure Sphere (MT3620) - competition units only; plain art badges have no onboard MCU
  leds: null
  display: none (challenge is worked through an external web terminal, not an onboard display)
  connectivity:
  - wifi
  - usb
  battery: 5000mAh USB power pack (competition units only)
  sao_version: null
get_one:
  price: Free; no contest entry fee per the maker's own posting (a $25 fee is noted on the community
    sheet but not corroborated elsewhere - see research notes)
  price_usd: 0.0
  quantity: 500 PCB badges made in assorted colors; 50 of those included the full Azure Sphere
    competition kit (over $168 of hardware per competition unit)
  availability: free
  distribution:
  - contest
  - free_drop
  where: 'Competition badges: guaranteed preregistration for the first 24 who solved a posted riddle,
    with the rest given out in a one-time 30-minute window at 11:30 AM on Friday, August 12, 2022 at
    DEF CON 30; unclaimed badges then went first-come first-served. Plain Clippy art badges (350 of
    the 500 made) were handed out in person by "El Jefe" around the con, and possibly sold for charity
    at the vendor pit.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: repo
  label: Cyber-Clippy (badge/contest info, GitHub)
  url: https://github.com/eljefedsecurit/Cyber-Clippy
- kind: repo
  label: Clippy-Challenge (contest walkthrough, GitHub)
  url: https://github.com/eljefedsecurit/Clippy-Challenge
- kind: social
  label: El Jefe De Security (GitHub profile)
  url: https://github.com/eljefedsecurit
images: []
contact:
  mastodon: eljefedsecurit@infosec.exchange
  bluesky: eljefe.social
notes:
- The badge is free but the contest has a $25 fee. Only 50 badges w/10 prizes.
- 'The maker''s own GitHub README (accessed 2026-09-07) describes entry as free ("no fee, but there''s
  a riddle") and does not mention a $25 fee; the origin of the $25 figure on the community sheet is
  unclear.'
status: released
sources:
- kind: sheet
  event: dc30
  row: 25
  updated: '2022-07-18'
- kind: url
  url: https://github.com/eljefedsecurit/Cyber-Clippy
  title: 'ElJefeDSecurIT/Cyber-Clippy: Clippy badge start page.'
  accessed: '2026-09-07'
  note: Maker's own README - what the badge is, who made it (Microsoft Office of the CTO Maker Incubation
    Team), quantities made (500 PCBs / 50 Azure Sphere competition kits), contest rules, distribution
    time/place, and how to get a plain art badge.
- kind: url
  url: https://github.com/eljefedsecurit/Clippy-Challenge
  title: 'ElJefeDSecurIT/Clippy-Challenge: CyberClippy Challenge start page.'
  accessed: '2026-09-07'
  note: Contest walkthrough - confirms the Azure Sphere/Altair 8800/CP/M puzzle mechanic, the web
    terminal, and the ciphers/clues used.
- kind: url
  url: https://github.com/eljefedsecurit
  title: ElJefeDSecurIT (GitHub profile)
  accessed: '2026-09-07'
  note: Confirms maker identity and that the same person also made the DEFCON26 middle-finger badge
    (DC26fingerbadge repo); lists contact handles the maker published themselves.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core facts (maker, quantities, Azure Sphere competition mechanic, distribution details) come
    straight from the maker's own GitHub repos, but no photo of the physical badge could be located
    (no Hackaday.io, storefront, press, or social-media image turned up in search), so look.colors and
    tech.leds are left empty rather than guessed, and look.shape/themes are inferred from "Clippy" in
    the name rather than a photo. The $25 entry fee on the original community sheet is not corroborated
    by the maker's own posting and may be a sheet error or refer to something else; flagged rather than
    resolved. No hardware/gerber files were found, so make_your_own fields are left null.
last_modified_date: '2026-09-07'
---

The Cyber Clippy badge was made for DEF CON 30 (2022) by El Jefe De Security, working with Adrian Bonar under Microsoft's Office of the CTO Maker Incubation Team. It came in two forms: a plain Clippy-shaped PCB art badge (350 of the 500 made), and 50 "competition" units that bundled a full Azure Sphere developer kit - an MT3620-based Azure Sphere board, an "8800 Retro-click" Altair 8800 emulator, a 32GB SD card, mounting standoffs, and a 5000mAh USB power pack - worth over $168 per kit.

The competition badges powered a puzzle contest: entrants connected to a web-based terminal that tunneled into a CP/M environment running on the Altair 8800 emulator, and worked through a chain of hidden ciphers and morse-code-style clues to reach a hidden prize code. The first five to finish won an Adafruit LoBe kit with a Raspberry Pi 4; the next five got a three-month Xbox Game Pass. Entry was free, though a riddle posted ahead of time guaranteed the first 24 solvers a spot; the rest of the badges were given out in a single 30-minute window at 11:30 AM on Friday, August 12, 2022, then opened up first-come first-served. The plain Clippy art badges were distributed informally by "El Jefe" in person around the convention, with a possible charity sale at the vendor pit.

No photos of the finished badge or the competition kit were found in this pass, and the badge's own hardware design files do not appear to have been published (the maker's GitHub repos cover only the contest instructions, not schematics or gerbers).
