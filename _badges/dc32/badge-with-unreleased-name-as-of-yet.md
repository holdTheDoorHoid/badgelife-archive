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
summary: An edge-lit acrylic-and-PCB badge shaped like the Hylian Crest from The
  Legend of Zelda, made by Ironwood Cyber as the prize for a DEF CON 32 CTF
  challenge and paired with a companion mobile app for a Zelda-themed
  exploration and puzzle game.
functions: Touch-pad controls, RGB lighting, and audio/haptic feedback drive
  a game tied to the "Ironwood Cyber Valet" mobile app (iOS/Android), which
  handles badge customization, Bluetooth Wi-Fi setup, a visual game-status
  and leaderboard display, and a hybrid 3D/CTF/puzzle game with a
  music-note-guessing element. The badge also plays with all of Ironwood
  Cyber's prior-year badges (the TRON disc badge lacks audio).
look:
  colors:
  - gold
  - clear
  - black
  shape: hylian crest
  themes:
  - fantasy
  - pop culture
  - puzzle
  - ctf
  - video game
  form_factor: pcb badge
tech:
  mcu: null
  leds:
    count: null
    type: RGB
    note: Edge-lit clear acrylic wings light up in color around the gold
      PCB crest; exact LED type/count not published.
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
  quantity: '20 (first 20 CTF finishers)'
  availability: limited
  availability_note: Contest concluded at DEF CON 32 (Aug 2024); not sold at
    retail. Checked 2026-09-06.
  distribution:
  - contest
  where: Awarded to the first 20 finishers of Ironwood Cyber's DEF CON 32
    "Crest Badge" CTF challenge.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: No hardware or firmware repo found specifically for the Crest
    Badge. Ironwood Cyber's GitHub (github.com/Ironwood-Cyber) hosts
    dc30-badge-hw (KiCad schematics for an earlier badge), but nothing for
    DC32.
links:
- label: go.rallyup.com/6c981b/Auction/Details
  url: https://go.rallyup.com/6c981b/Auction/Details
  kind: website
- label: discord.gg/cCnWsFvgHz
  url: https://discord.gg/cCnWsFvgHz
  kind: social
- label: 'YouTube: Introducing the Ironwood Cyber DC32 "Crest Badge"'
  url: https://www.youtube.com/watch?v=8ILt5zcA9lQ
  kind: video
- label: Ironwood Cyber Valet (companion app site)
  url: https://ironwoodcybervalet.com/
  kind: website
- label: 'reznok.com: Gotta Go Fast - Hacking the IWC DEFCON32 Game''s Obstacle
    Course'
  url: https://reznok.com/gotta-go-fast-hacking-the-iwc-defcon32-games-obstacle-course/
  kind: article
- label: Ironwood Cyber on X
  url: https://x.com/IronwoodCyber
  kind: social
images:
- file: assets/images/badges/dc32/badge-with-unreleased-name-as-of-yet/0217f9c50c.jpg
  source: "https://www.youtube.com/watch?v=8ILt5zcA9lQ"
  credit: "Ironwood Cyber"
  caption: "Thumbnail from Ironwood Cyber's DC32 Crest Badge announcement video"
- file: assets/images/badges/dc32/badge-with-unreleased-name-as-of-yet/dc2fa1af05.jpg
  source: "https://reznok.com/gotta-go-fast-hacking-the-iwc-defcon32-games-obstacle-course/"
  credit: "reznok.com"
  caption: "Photo of the Ironwood Cyber Crest Badge from a writeup on hacking the companion game"
contact:
  handles:
  - '@IronwoodCyber'
  raw:
  - Follow  on Twitter for details or join our game discord server
notes:
- "Mobile app (officially released in app stores) allows badge customization, configuring wifi settings over ble, provides visual interface for game status, leaderboard access, etc, and contains a hybrid game with mix of 3d game mechanics, ctf/puzzle and badge music and social games. \n \nBadge hardware uses touch pads for user interface, and has audio and haptic feedback. One part of the badge game is to figure out short musical notes. \n \n We will also be back porting this software release to be compatible with all previous year‚Äôs badges (though tron badge has no audio). All badges can play together"
status: released
sources:
- kind: sheet
  event: dc32
  row: 72
  updated: '2024-06-03'
- kind: url
  url: https://www.youtube.com/watch?v=8ILt5zcA9lQ
  title: 'SPECIAL RELEASE: Introducing the Ironwood Cyber DC32 "Crest Badge"'
  accessed: '2026-09-06'
  note: Confirms the badge's real name (Crest Badge), that it was a CTF prize
    for the first 20 winners, and its Zelda Hylian Crest design.
- kind: url
  url: https://reznok.com/gotta-go-fast-hacking-the-iwc-defcon32-games-obstacle-course/
  title: Gotta Go Fast - Hacking the IWC Defcon32 Game's Obstacle Course
  accessed: '2026-09-06'
  note: Confirms the badge connects over Bluetooth to the companion mobile
    app as a game controller, and provided a real photo of the badge.
- kind: url
  url: https://ironwoodcybervalet.com/
  title: Ironwood Cyber Valet (companion app landing page)
  accessed: '2026-09-06'
  note: Confirms the app name and that it links out to DC30/DC31/DC32 badge
    pages (page content is a JS app shell that could not be fully read).
- kind: url
  url: https://github.com/Ironwood-Cyber
  title: Ironwood Cyber GitHub org
  accessed: '2026-09-06'
  note: Checked for hardware/firmware; only found dc30-badge-hw (a different
    year's badge), nothing for the Crest Badge.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Maker's own video and a third-party technical writeup confirm the
    badge's real name (Crest Badge), Hylian Crest design, Bluetooth link to
    the companion app, and that it was a 20-winner CTF prize rather than a
    retail item. Could not confirm MCU/chip, exact LED count/part, or
    power source/battery - not published anywhere found. The RallyUp
    "2024 Hacker Bake Sale" auction link in the sheet appears to be an
    unrelated charity fundraiser page, not a listing for this badge; could
    not confirm a connection. eda_tool/open-source status unknown - no
    DC32-specific repo found.
last_modified_date: '2026-09-06'
---

Ironwood Cyber, a cybersecurity company that has fielded a DEF CON badge every year since DC30's TRON disc, built the Crest Badge for DEF CON 32 as a Zelda-themed CTF prize rather than a sale item: the first 20 people to finish their "Crest Badge" capture-the-flag challenge won one. The badge takes the shape of Zelda's Hylian Crest, with a gold PCB core surrounded by edge-lit clear acrylic wings that light up in color, and pairs over Bluetooth with Ironwood Cyber's "Ironwood Cyber Valet" companion app (iOS and Android) for a hybrid 3D/puzzle/CTF game with leaderboards, badge customization, and a short musical-note guessing mechanic.

The badge itself uses capacitive touch pads for input and adds audio and haptic feedback, a step up from the company's earlier, screen-and-app-free TRON and Arc Reactor badges. Ironwood Cyber has said the companion software would be back-ported to work with all of its previous badges so every year's hardware can play together, though the original TRON badge lacks the audio hardware needed for the music portion of the game.

No hardware or firmware for the Crest Badge specifically has turned up in Ironwood Cyber's GitHub org (which does host KiCad schematics for an earlier badge), and neither the maker's site nor third-party coverage publishes the MCU, LED part, or power details, so those fields are left blank rather than guessed.
