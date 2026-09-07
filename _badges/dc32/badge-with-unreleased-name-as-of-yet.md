---
title: Crest Badge
id: dc32-badge-with-unreleased-name-as-of-yet
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
summary: A light-up acrylic badge shaped like the Hylian Crest from The Legend of Zelda, made by Ironwood Cyber as the prize for a DEF CON 32 CTF challenge and paired with a companion mobile app for a Zelda-themed game.
functions: Touch pads on the rear edges of the wings, feet and tail drive the badge; the maker's badge page lists touch-pad combos for a battery meter, Bluetooth pairing on/off, next/previous LED sequence, a synth mode and a network check. It pairs with Ironwood Cyber's companion app (iOS/Android) as a controller for a Zelda-themed game. The maker's sheet listing adds that the app handles badge customization, Wi-Fi setup over BLE, game status and a leaderboard, that the game mixes 3D mechanics with CTF/puzzle and music-note guessing, that the badge has audio and haptic feedback, and that the software was to be back-ported so all prior-year Ironwood Cyber badges can play together (the TRON badge has no audio).
look:
  colors:
  - clear
  - white
  - black
  shape: hylian crest
  themes:
  - fantasy
  - pop culture
  - puzzle
  - ctf
  form_factor: acrylic
tech:
  mcu: null
  leds:
    count: null
    type: null
    note: Lights up in more than one color and has selectable LED sequences; LED part and count not published.
  display: none
  connectivity:
  - wifi
  - ble
  inputs:
  - touch
  battery: null
  sao_version: null
get_one:
  price: free (contest prize)
  price_usd: 0.0
  quantity: 20 (first 20 CTF finishers)
  availability: limited
  availability_note: Contest concluded at DEF CON 32 (Aug 2024); not sold at retail. Checked 2026-09-07.
  distribution:
  - contest
  where: Awarded to the first 20 winners of Ironwood Cyber's DEF CON 32 "Crest Badge" CTF challenge.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: No hardware or firmware repo found for the Crest Badge. Ironwood Cyber's GitHub org hosts dc30-badge-hw (KiCad schematics for an earlier badge), nothing for DC32.
links:
- label: go.rallyup.com/6c981b/Auction/Details
  url: https://go.rallyup.com/6c981b/Auction/Details
  kind: website
- label: discord.gg/cCnWsFvgHz
  url: https://discord.gg/cCnWsFvgHz
  kind: social
- label: 'YouTube (The Cyber Distortion Podcast): Introducing the Ironwood Cyber DC32 "Crest Badge"'
  url: https://www.youtube.com/watch?v=8ILt5zcA9lQ
  kind: video
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
- file: assets/images/badges/dc32/badge-with-unreleased-name-as-of-yet/dc2fa1af05.jpg
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
- "Mobile app (officially released in app stores) allows badge customization, configuring wifi settings over ble, provides visual interface for game status, leaderboard access, etc, and contains a hybrid game with mix of 3d game mechanics, ctf/puzzle and badge music and social games. \n \nBadge hardware uses touch pads for user interface, and has audio and haptic feedback. One part of the badge game is to figure out short musical notes. \n \n We will also be back porting this software release to be compatible with all previous year‚Äôs badges (though tron badge has no audio). All badges can play together"
- Sheet title was "Badge with unreleased name as of yet"; the maker later named it the "Crest Badge".
status: released
sources:
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
  url: https://www.youtube.com/watch?v=8ILt5zcA9lQ
  title: 'SPECIAL RELEASE: Introducing the Ironwood Cyber DC32 "Crest Badge"'
  accessed: '2026-09-07'
  note: Video on The Cyber Distortion Podcast channel (not the maker's). Title and description confirm the name, the CTF, and that the first 20 winners received the badge.
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
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check 2026-09-07: maker''s own DC32 badge page confirms the name, touch-pad controls, battery meter, pairing, LED sequences and synth mode; the CTF/first-20-winners facts come from the announcement video (on The Cyber Distortion Podcast channel, not the maker''s own) and the Zelda theme and photo from reznok.com. Removed unsupported claims: "gold PCB core", "edge-lit" and "RGB" (photo shows clear/white acrylic with black print lit in several colors; construction not published), the companion app name "Ironwood Cyber Valet" (only the domain uses that word; the Play Store package is com.ironwoodcyber.iwcdc31), and body claims about a TRON/Arc Reactor badge lineage. Removed the YouTube thumbnail image (stylized artwork on a third-party channel, not a photo of the badge). Not published anywhere found: MCU, LED part/count, battery type, open-source status. The RallyUp link from the sheet is a "2024 Hacker Bake Sale" fundraiser page with no visible mention of this badge. Maker photos
    exist on the DC32 page (dc32-front-gray-scaled.png, dc32-back-gray-scaled.png under ironwoodcybervalet.com/_next/static/media/) and could replace the third-party photo.'
last_modified_date: '2026-09-07'
---

Ironwood Cyber, a cybersecurity company, built the Crest Badge for DEF CON 32 as a prize rather than a sale item: a CTF challenge was announced ahead of the con, and the first 20 winners received the badge. The badge takes the shape of Zelda's Hylian Crest, cut from clear and white acrylic with black printed detail, and lights up in several colors with selectable LED sequences. It pairs over Bluetooth with the company's companion app (iOS and Android), acting as a controller for a Zelda-themed game; the maker's sheet listing describes the game as a mix of 3D mechanics, CTF/puzzle content and a short musical-note guessing element, with a leaderboard and badge customization in the app.

Input is by touch pads on the rear edges of the wings, feet and tail. The maker's badge page lists touch combinations for enabling touch mode, checking the battery meter, toggling Bluetooth pairing, stepping through LED sequences, a synth mode and a network check, and the sheet listing says the badge also has audio and haptic feedback. Ironwood Cyber said the software would be back-ported to its previous badges so every year's hardware can play together, though its TRON badge lacks audio.

No hardware or firmware for the Crest Badge has turned up in Ironwood Cyber's GitHub org (which hosts KiCad schematics for an earlier badge), and neither the maker's pages nor third-party coverage publish the MCU, LED part or battery details, so those fields are left blank.
