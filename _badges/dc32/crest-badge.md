---
title: DC32 Crest Badge
id: dc32-crest-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Ironwood Cyber
  url: https://www.ironwoodcyber.com/
summary: A two-board electronic badge (an ESP32-based "rear board" plus a "front board") built for Ironwood Cyber's DEF CON 32 "Crest Badge" CTF prize; this repository holds its PCB, mechanical CAD and firmware source.
functions: Firmware is an ESP-IDF ("2024-badge-app") project with a 2nd-stage bootloader and a flashable application, built to run on the front/rear board stack.
look:
  colors:
  - clear
  - white
  - black
  shape: hylian crest
  themes:
  - fantasy
  - pop culture
  - ctf
  form_factor: acrylic
tech:
  mcu: ESP32-WROVER-E
  leds:
    count: null
    type: null
    note: Lights up in more than one color and has selectable LED sequences; LED part and count not published.
  display: none
  connectivity:
  - wifi
  - ble
  battery: null
  sao_version: null
  inputs:
  - touch
get_one:
  price: free (contest prize)
  price_usd: 0.0
  quantity: 20 (first 20 CTF finishers)
  availability: limited
  distribution:
  - contest
  where: Awarded to the first 20 winners of Ironwood Cyber's DEF CON 32 "Crest Badge" CTF challenge.
  availability_note: Contest concluded at DEF CON 32 (Aug 2024); not sold at retail. Checked 2026-09-07.
make_your_own:
  open_source: true
  hardware_url: https://github.com/badgelife/dc32-crest-badge
  firmware_url: https://github.com/badgelife/dc32-crest-badge/tree/main/firmware
  eda_tool: KiCad
  notes: No hardware or firmware repo found for the Crest Badge. Ironwood Cyber's GitHub org hosts dc30-badge-hw (KiCad schematics for an earlier badge), nothing for DC32.
links:
- label: github.com/badgelife/dc32-crest-badge
  url: https://github.com/badgelife/dc32-crest-badge
  kind: repo
- label: 'PCBWay: DC32 Crest Badge Front Board Prototype'
  url: https://www.pcbway.com/project/share/DC32_Crest_Badge_Front_Board_Prototype_53a9e1d2.html
  kind: fab
- label: 'YouTube (The Cyber Distortion Podcast): Introducing the Ironwood Cyber DC32 "Crest Badge"'
  url: https://www.youtube.com/watch?v=8ILt5zcA9lQ
  kind: video
- label: go.rallyup.com/6c981b/Auction/Details
  url: https://go.rallyup.com/6c981b/Auction/Details
  kind: website
- label: discord.gg/cCnWsFvgHz
  url: https://discord.gg/cCnWsFvgHz
  kind: social
- label: Ironwood Cyber badge site (companion app links, DC32 badge page)
  url: https://ironwoodcybervalet.com/DC32
  kind: website
- label: 'reznok.com: Gotta Go Fast - Hacking the IWC DEFCON32 Game''s Obstacle Course'
  url: https://reznok.com/gotta-go-fast-hacking-the-iwc-defcon32-games-obstacle-course/
  kind: article
  archived: https://web.archive.org/web/20251014110412/https://reznok.com/gotta-go-fast-hacking-the-iwc-defcon32-games-obstacle-course/
- label: Ironwood Cyber on X
  url: https://x.com/IronwoodCyber
  kind: social
images:
- file: assets/images/badges/dc32/crest-badge/81ae305d23.jpg
  source: https://www.pcbway.com/project/share/DC32_Crest_Badge_Front_Board_Prototype_53a9e1d2.html
  credit: Jose Rodriguez / PCBWay
  caption: Assembled two-board badge stack with ESP32-WROVER module and U.FL antenna, next to the main board's underside
- file: assets/images/badges/dc32/crest-badge/45b383e4ff.jpg
  source: https://www.pcbway.com/project/share/DC32_Crest_Badge_Front_Board_Prototype_53a9e1d2.html
  credit: Jose Rodriguez / PCBWay
  caption: Main board detail showing USB-C port, battery header, and the Ironwood Cyber tree logo silkscreen
- file: assets/images/badges/dc32/crest-badge/dc2fa1af05.jpg
  source: https://reznok.com/gotta-go-fast-hacking-the-iwc-defcon32-games-obstacle-course/
  credit: reznok.com
  caption: The Ironwood Cyber Crest Badge held in hand, lit up, from a writeup on hacking the companion game
  archived: https://web.archive.org/web/20251014110412/https://reznok.com/gotta-go-fast-hacking-the-iwc-defcon32-games-obstacle-course/
contact:
  handles:
  - '@IronwoodCyber'
  raw:
  - Follow  on Twitter for details or join our game discord server
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- This appears to be the same badge as dc32-badge-with-unreleased-name-as-of-yet (Ironwood Cyber's "Crest Badge", a DEF CON 32 CTF prize shaped like Zelda's Hylian Crest). That entry was researched from the maker's own DC32 page and third-party coverage and found no public hardware/firmware repo; this repo was found separately and is not explicitly branded to Ironwood Cyber, but several details line up closely - the repo's only mechanical CAD file is "Triforce.f3d", its PCB prototypes folder has "triforce_sao" and "link_sao" subfolders (Zelda's Triforce and the character Link), its two boards are named "front-board" and "rear-board" (matching the PCBWay share titled "DC32 Crest Badge Front Board Prototype"), and its ESP32-WROVER-E MCU supports the wifi/BLE connectivity the other entry's maker page describes. Treat this as a likely duplicate of that entry rather than a confirmed one.
- "Mobile app (officially released in app stores) allows badge customization, configuring wifi settings over ble, provides visual interface for game status, leaderboard access, etc, and contains a hybrid game with mix of 3d game mechanics, ctf/puzzle and badge music and social games. \n \nBadge hardware uses touch pads for user interface, and has audio and haptic feedback. One part of the badge game is to figure out short musical notes. \n \n We will also be back porting this software release to be compatible with all previous year‚Äôs badges (though tron badge has no audio). All badges can play together"
- Sheet title was "Badge with unreleased name as of yet"; the maker later named it the "Crest Badge".
status: listed
sources:
- kind: url
  url: https://github.com/badgelife/dc32-crest-badge
  title: DC32 Crest Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc32''.'
- kind: url
  url: https://github.com/badgelife/dc32-crest-badge/tree/main/pcb
  title: badgelife/dc32-crest-badge - pcb directory
  accessed: '2026-09-07'
  note: Two boards (front-board, rear-board) built around an ESP32-WROVER-E module, KiCad library format (.lib/.pretty); prototypes folder includes triforce_sao and link_sao subfolders.
- kind: url
  url: https://github.com/badgelife/dc32-crest-badge/tree/main/cad
  title: badgelife/dc32-crest-badge - cad directory
  accessed: '2026-09-07'
  note: Only mechanical CAD file present is Triforce.f3d.
- kind: url
  url: https://raw.githubusercontent.com/badgelife/dc32-crest-badge/main/firmware/README.md
  title: firmware/README.md
  accessed: '2026-09-07'
  note: 'ESP-IDF project named "2024-badge-app": 2nd-stage bootloader plus application, flashed with idf.py; no branding or feature description beyond build/flash instructions.'
- kind: url
  url: https://www.pcbway.com/project/share/DC32_Crest_Badge_Front_Board_Prototype_53a9e1d2.html
  title: DC32 Crest Badge Front Board Prototype - PCBWay
  accessed: '2026-09-07'
  note: Shared by Jose Rodriguez, June 2024; provided the two saved photos of the assembled front/rear board stack.
- kind: url
  url: https://www.youtube.com/watch?v=8ILt5zcA9lQ
  title: 'SPECIAL RELEASE: Introducing the Ironwood Cyber DC32 "Crest Badge"'
  accessed: '2026-09-07'
  note: Third-party channel video title/description found via search; confirms the "Crest Badge" name is Ironwood Cyber's, tied to a CTF where the first 20 finishers won the badge (not independently re-verified here beyond the search snippet).
- kind: sheet
  event: dc32
  row: 72
  updated: '2024-06-03'
- kind: url
  url: https://ironwoodcybervalet.com/DC32
  title: Ironwood Cyber DC32 Badge page
  accessed: '2026-09-07'
  note: Maker's own page (client-rendered; text read from its JS bundle). Confirms the name "DEF CON 32 Crest Badge", touch pads on the rear edges of wings/feet/tail, touch combos for battery meter, pairing, LED sequences, synth mode and network check, and the companion app/Discord.
- kind: url
  url: https://reznok.com/gotta-go-fast-hacking-the-iwc-defcon32-games-obstacle-course/
  title: Gotta Go Fast - Hacking the IWC Defcon32 Game's Obstacle Course
  accessed: '2026-09-07'
  note: Third-party writeup; calls it a Zelda-themed badge that connects to the game as a controller, and provides the photo (Hylian Crest shape, clear/white acrylic with black print, multi-color lighting).
  archived: https://web.archive.org/web/20251014110412/https://reznok.com/gotta-go-fast-hacking-the-iwc-defcon32-games-obstacle-course/
- kind: url
  url: https://ironwoodcybervalet.com/
  title: Ironwood Cyber badge site landing page
  accessed: '2026-09-07'
  note: Links to the DC30/DC31/DC32 badge pages and to the Android/iOS companion app (Play Store package com.ironwoodcyber.iwcdc31).
- kind: url
  url: https://github.com/Ironwood-Cyber
  title: Ironwood Cyber GitHub org
  accessed: '2026-09-07'
  note: Only dc30-badge-hw (KiCad schematics for an earlier badge); nothing for the Crest Badge.
  archived: https://web.archive.org/web/20260208081048/https://github.com/Ironwood-Cyber
- kind: url
  url: https://www.ironwoodcyber.com/
  title: Ironwood Cyber company site
  accessed: '2026-09-07'
  note: Confirms Ironwood Cyber is a cybersecurity (penetration testing) company; the site itself does not mention the badges.
  archived: https://web.archive.org/web/20260611104800/https://www.ironwoodcyber.com/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No page found states outright that this GitHub repo is Ironwood Cyber's; the link is inferred from the Zelda-themed folder/file names (Triforce, Link) and the front/rear board split matching the PCBWay listing, cross-checked against research already on file for dc32-badge-with-unreleased-name-as-of-yet. quantity, availability, LED and battery details were left blank here since this repo and the PCBWay page do not state them; see the other entry for what the maker's own page and third-party coverage say about the CTF/prize mechanics, look, and touch controls. Merged with duplicate entry 'Crest Badge' (dc32-badge-with-unreleased-name-as-of-yet).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc32/badge-with-unreleased-name-as-of-yet/
---

This repository holds the hardware and firmware for what looks like the same
badge documented at `dc32-badge-with-unreleased-name-as-of-yet`: Ironwood
Cyber's "Crest Badge," given out to the first 20 finishers of a Capture the
Flag challenge at DEF CON 32. The repo itself carries no Ironwood Cyber
branding, but its contents point the same direction — a KiCad-designed
two-board stack (a "front-board" and "rear-board") built around an
ESP32-WROVER-E module, a single mechanical CAD file named "Triforce.f3d," and
PCB prototype folders named "triforce_sao" and "link_sao," all Legend of
Zelda references that match the other entry's description of a badge shaped
like Hyrule's crest.

Firmware is an ESP-IDF project titled "2024-badge-app," with a second-stage
bootloader and a flashable application built and monitored with `idf.py`; its
README has no feature description beyond build and flash commands, so it adds
no detail about the badge's controls or game beyond what the maker's own page
already provided in the other entry.

Two photos from a PCBWay fabrication share (posted by Jose Rodriguez, June
2024) show the assembled electronics: a rectangular board with a USB-C port,
a battery header, an antenna connector, an ESP32-WROVER-E module, and a
"tree" logo etched into the silkscreen, stacked on brass standoffs above a
second board. No price, quantity or availability information is published
here beyond what is already recorded on the other entry.

## Notes merged from the duplicate entry "Crest Badge"

Ironwood Cyber, a cybersecurity company, built the Crest Badge for DEF CON 32 as a prize rather than a sale item: a CTF challenge was announced ahead of the con, and the first 20 winners received the badge. The badge takes the shape of Zelda's Hylian Crest, cut from clear and white acrylic with black printed detail, and lights up in several colors with selectable LED sequences. It pairs over Bluetooth with the company's companion app (iOS and Android), acting as a controller for a Zelda-themed game; the maker's sheet listing describes the game as a mix of 3D mechanics, CTF/puzzle content and a short musical-note guessing element, with a leaderboard and badge customization in the app.

Input is by touch pads on the rear edges of the wings, feet and tail. The maker's badge page lists touch combinations for enabling touch mode, checking the battery meter, toggling Bluetooth pairing, stepping through LED sequences, a synth mode and a network check, and the sheet listing says the badge also has audio and haptic feedback. Ironwood Cyber said the software would be back-ported to its previous badges so every year's hardware can play together, though its TRON badge lacks audio.

No hardware or firmware for the Crest Badge has turned up in Ironwood Cyber's GitHub org (which hosts KiCad schematics for an earlier badge), and neither the maker's pages nor third-party coverage publish the MCU, LED part or battery details, so those fields are left blank.
