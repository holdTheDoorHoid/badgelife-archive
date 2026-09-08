---
title: Ironwood Cyber Tron Badge
id: dc30-ironwood-cyber-tron-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
redirect_from:
- /badges/dc30/iwc/
- /badges/dc30/tron-badge/
- /badges/dc30/tron-inspired-badge/
type: badge
event: dc30
year: 2022
makers:
- name: Ironwood Cyber Team
  url: https://github.com/Ironwood-Cyber
- name: kimboslice
  role: PCB
- name: notthatguy
  role: PCB, embedded software
- name: joehacksalot
  role: PCB, embedded software
- name: Shiloh
  role: companion web app
- name: LeetPanda
  role: website
- name: Spaghetti Code
  role: website
summary: Ironwood Cyber Team's Tron-themed badge for DEF CON 30, a two-board LED-ring design with a touch interface and a companion web app.
functions: Lights 70 addressable LEDs arranged in two concentric rings (inner and outer); the front board is a capacitive touch interface for the rear board's electronics.
look:
  colors:
  - black
  - teal
  shape: circle
  themes:
  - tron
  - sci-fi
tech:
  mcu: ESP-series (exact part not stated)
  leds:
    count: 70
    type: RGB
    note: Two concentric rings (inner and outer), diffused through 3D-printed material between the two boards.
  display: null
  connectivity:
  - wifi
  - usb
  - uart
  battery: LiPo, rechargeable
  sao_version: null
get_one:
  price: Free
  price_usd: 0.0
  quantity: 80 (per the maker, given away over several weeks)
  availability: free
  distribution:
  - raffle
  - free_drop
  where: Twitter and LinkedIn raffles plus unannounced in-person drops during DEF CON 30 (one at the Flamingo); pickup only, not shipped.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  firmware_url: null
  eda_tool: KiCad
links:
- label: Schematics repo (Ironwood-Cyber/dc30-badge-hw)
  url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  kind: repo
- label: www.reddit.com/r/Defcon/comments/w5hozv/comment/ih8090z
  url: https://www.reddit.com/r/Defcon/comments/w5hozv/comment/ih8090z
  kind: social
- label: Ironwood Cyber (@IronwoodCyber) on Twitter, badge reveal
  url: https://twitter.com/IronwoodCyber/status/1550170683308638208
  kind: social
- label: ironwoodcyber.com
  url: https://ironwoodcyber.com/
  kind: website
- label: Ironwood Cyber - About (Tron Badge history)
  url: https://www.ironwoodcyber.com/about
  kind: website
- label: Ironwood Cyber Valet - DC30 badge page
  url: https://ironwoodcybervalet.com/DC30
  kind: website
- label: 'Tindie Blog: "Badge Me if You Can - DEF CON 30"'
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  kind: article
images:
- file: assets/images/badges/dc30/ironwood-cyber-tron-badge/e802582f60.jpg
  source: https://twitter.com/IronwoodCyber/status/1550170683308638208
  credit: Ironwood Cyber
  caption: Tron Disc badge lit up, revealed on Twitter, July 2022
- file: assets/images/badges/dc30/ironwood-cyber-tron-badge/369baeafcb.jpg
  source: https://twitter.com/IronwoodCyber/status/1550606356150976512
  credit: Ironwood Cyber
  caption: 'Assembling Tron Disc boards: LED ring, black PCB, and center RF module, July 2022'
contact: {}
notes:
- The GitHub repo's own README and GitHub description say the schematics are "Defcon 29 Kicad Schematics", while the badge.life page filed this as the DC30 (2022) Tron badge. The hardware may have originated for DC29 and been carried forward/reused for DC30; sources disagree and neither confirms which con the physical badge was actually distributed at.
- Twitter raffle/drops. Info on twitter (@IronwoodCyber). Check link for greater details
- Maker's own name for it is the "Tron Disc" badge/"Tron disc badge"; kept the sheet's title "TRON Badge" per the archive's naming rule since that is close enough and is the sheet's wording.
- Unofficial Tron-themed DEF CON 30 badge by Ironwood Cyber, covered (as "the Tron-inspired badge") in Tindie's DC30 badge roundup. Found by the event-year sweep, task general-2020.
- This entry duplicates dc30-ironwood-cyber-tron-badge, which already carries fuller research (maker team credits, Reddit/Twitter sourcing, two saved photos). Left unmerged per research-guide instructions; see that entry for the maker's own name for it, "Tron Disc," and for a claimed ~80-unit quantity and Twitter/LinkedIn raffle mechanics sourced from a Reddit comment this pass could not independently re-verify (Reddit and web.archive.org fetches were blocked in this session).
status: listed
sources:
- kind: sheet
  event: dc30
  row: 38
  updated: '2022-07-22'
- kind: url
  url: https://badge.life/badges/dc30/iwc/
  title: Original badge.life archive page
  accessed: '2026-09-06'
  note: Migrated from the badge.life Badge Archive; the original page is preserved as the entry body. Lists the maker/dev team and the seven original photo filenames (tron1-tron7.jpg), none of which resolve any longer.
  archived: https://web.archive.org/web/20260811022040/https://badge.life/badges/dc30/iwc/
- kind: url
  url: https://github.com/Ironwood-Cyber/dc30-badge-hw
  title: 'Ironwood-Cyber/dc30-badge-hw: Tron badge hardware schematics'
  accessed: '2026-09-06'
  note: 'README describes the badge: two PCBs joined by 3D-printed diffusion material, a touch-input front board, 70 addressable LEDs in two rings, rechargeable LiPo circuit, and USB reprogramming via esp-idf/UART. Repo description says "Defcon 29 Kicad Schematics".'
- kind: sheet
  event: dc30
  row: 38
  updated: '2022-07-22'
- kind: url
  url: https://www.reddit.com/r/Defcon/comments/w5hozv/comment/ih8090z
  title: 'r/Defcon: "Update on tron disc badge. info in comments" (archived)'
  accessed: '2026-09-06'
  note: Reddit blocks live fetches; read via Wayback Machine snapshot (2022-07-24). Maker (u/OP, presumably Ironwood Cyber) says 80 badges total given away over several weeks via Twitter raffles, a LinkedIn raffle, and ~2 in-person site drops during DEF CON, pickup only (no shipping); mentions an exposed-FR4 prototype and a HASL/silver prototype before settling on copper for the final run, and a companion web app (by u/cwsharkbones) for building custom LED light sequences.
- kind: url
  url: https://twitter.com/IronwoodCyber
  title: Ironwood Cyber (@IronwoodCyber) on Twitter/X
  accessed: '2026-09-06'
  note: 'Read via Wayback Machine snapshots (July-August 2022, live fetch blocked). Confirms Ironwood Cyber is a Fort Worth, TX cybersecurity company (Enlight/Firethorn products) running the badge giveaway as marketing outreach; tweets show "Our #DEFCON badge is live", a "10 Tron Disc #DEFCON badges" raffle, and a "Free badges for the first 20 people" in-person drop near the Flamingo during DEF CON 30, confirming DC30/2022 and free/raffle distribution.'
- kind: url
  url: https://ironwoodcyber.com/
  title: Tron-inspired Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2020); event read as ''DEF CON 30 2022''.'
- kind: url
  url: https://www.ironwoodcyber.com/about
  title: About Ironwood Cyber
  accessed: '2026-09-08'
  note: Confirms "2022 DEF CON 30 badge debut" - the Tron Badge was Ironwood Cyber's first custom hardware badge, launched at DEF CON 30.
- kind: url
  url: https://ironwoodcybervalet.com/DC30
  title: Ironwood Cyber Valet - DC30
  accessed: '2026-09-08'
  note: Maker's own badge landing/instructions page. Confirms giveaway ("We made the Tron Badge and are giving it away to let people know we were here") and that the badge auto-connects to Wi-Fi SSID 'DefCon-Open' to receive updates during the con - added wifi to tech.connectivity. No colors, shape, quantity, or MCU detail given.
- kind: url
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  title: 'Tindie Blog: "Badge Me if You Can - DEF CON 30"'
  accessed: '2026-09-08'
  note: 'Independent press coverage confirming the item is real and was actually distributed, not just listed: calls it "the Tron-inspired badge made by the folks at Ironwood Cyber," "only offered through acts of goodwill and random drops announced on Twitter." Also: "The bare copper plating was touch-sensitive, causing one of the many different operating modes to activate" - source for look.colors: copper and for softening the touch-interface wording (no "capacitive" claim). No quantity, price, or shape given.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: No price, quantity, availability, exact MCU part number, or firmware/web-app repo could be found; the "Source Repo" link on the original badge.life page was itself a TODO placeholder and no public firmware or companion-web-app repo exists under the Ironwood-Cyber GitHub org. The seven original badge photos (tron1-tron7.jpg) referenced by the badge.life page 404 and could not be saved. This entry duplicates dc30-tron-badge (same event, same maker "Ironwood Cyber"), which was imported separately from the community sheet with a Reddit/Twitter-raffle distribution note; the two were not merged per instructions. Merged with duplicate entry 'TRON Badge' (dc30-tron-badge). Merged with duplicate entry 'Tron-inspired Badge' (dc30-tron-inspired-badge).
last_modified_date: '2026-09-08'
---
## Developers

### Pcb devs:
- kimboslice
- notthatguy
- joehacksalot

### Embedded Software devs:
- notthatguy
- joehacksalot

### Companion Web App dev: 
- Shiloh

### Website devs:
- LeetPanda
- Spaghetti Code  

## Project Links
- [Schematics Repo](https://github.com/Ironwood-Cyber/dc30-badge-hw)
- [Source Repo](TODO)

## Badge images

The original badge.life page referenced seven photos (tron1–tron7.jpg) that were never committed to its repository, so they are not reproduced here.

The Ironwood Cyber Team built this Tron-themed badge for DEF CON 30 (2022) as a two-PCB assembly: a front board that provides a capacitive-touch interface, and a rear board carrying all the electronics, joined by 3D-printed diffusion material that spreads the light from 70 addressable LEDs arranged in two concentric rings. It runs on an ESP-series microcontroller with a rechargeable LiPo battery and can be reprogrammed over USB using esp-idf and USB UART. The team split the work across PCB design (kimboslice, notthatguy, joehacksalot), embedded firmware (notthatguy, joehacksalot), a companion web app (Shiloh), and the project's website (LeetPanda, Spaghetti Code).

The hardware schematics (KiCad) are published on GitHub, though the repository's own description labels them "Defcon 29 Kicad Schematics" even though the badge.life archive filed the badge under DC30 — it's unclear from available sources whether the design was originally made for DC29 and reused, or the repo description is simply outdated. No firmware repository, companion web app source, price, production quantity, or availability information was published, and the badge's original photos are no longer reachable.

## Make your own

Hardware schematics (KiCad) are available in the [dc30-badge-hw repository](https://github.com/Ironwood-Cyber/dc30-badge-hw), which documents the two-board LED-ring design and its LiPo/USB circuitry. No firmware source, bill of materials, or Gerber files have been published alongside it.

## Notes merged from the duplicate entry "TRON Badge"

Ironwood Cyber, a small Fort Worth, Texas cybersecurity startup, brought a round TRON-themed badge to DEF CON 30 (2022) as a free giveaway and outreach project. The maker calls it the "Tron Disc": two stacked PCBs, a rear board carrying an ESP-series microcontroller, a rechargeable LiPo battery, and 70 addressable RGB LEDs arranged in two concentric rings, paired with a front board that adds a capacitive-touch interface, with 3D-printed material between the boards diffusing the light into the glowing ring look seen in the team's reveal photos and videos.

About 80 badges were made and given away for free over several weeks, split across one or two Twitter raffles, a LinkedIn raffle, and a handful of unannounced in-person drops during the con itself (including one near the Flamingo) - pickup only, with no shipping option. A teammate was also building a companion web app so owners could design their own layered LED animation sequences to push to the badge, though it had not shipped by the time of the giveaway. Hardware schematics (KiCad) are published on GitHub, though no firmware source, bill of materials, or price/production-cost figures were ever made public.

## Make your own

Hardware schematics (KiCad) are available in the [dc30-badge-hw repository](https://github.com/Ironwood-Cyber/dc30-badge-hw), which documents the two-board LED-ring design and its LiPo/USB circuitry. No firmware source or Gerber files have been published alongside it.

## Notes merged from the duplicate entry "Tron-inspired Badge"

Ironwood Cyber, a cybersecurity startup, brought this Tron-themed badge to DEF CON 30 in 2022 as its first piece of custom hardware, giving it away for free rather than selling it ("We made the Tron Badge and are giving it away to let people know we were here," per the maker's own badge page). The badge is a two-PCB assembly - a front board whose bare-copper touch pads form the input and a rear board carrying the electronics - joined by 3D-printed diffusion material that spreads light from 70 addressable RGB LEDs arranged in two concentric rings. It auto-connects to the Wi-Fi network `DefCon-Open` to receive updates during the con.

Tindie's DEF CON 30 badge roundup called it "an unexpected but certainly popular badge coveted by all," distributed "only... through acts of goodwill and random drops announced on Twitter" - so it was actually handed out, not just listed. Exact production numbers and a firmer distribution timeline are not confirmed by sources this pass could reach. The hardware schematics (KiCad) are published on GitHub, though no firmware source or bill of materials has been released.

## Make your own

Hardware schematics (KiCad) are available in the [dc30-badge-hw repository](https://github.com/Ironwood-Cyber/dc30-badge-hw), which documents the two-board LED-ring design and its LiPo/USB circuitry. No firmware source or Gerber files have been published alongside it.
