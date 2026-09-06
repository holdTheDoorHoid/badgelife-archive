---
title: Flare Blinky Badge
id: dc34-flare-blinky-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Abhinav Panda / Hackerware.io
  url: https://hackerware.io
summary: A rectangular acrylic-faced PCB badge Hackerware.io made for the threat-intelligence company Flare (flare.io) for DEF CON 34, pairing a "light the letters" LED mechanic with a built-in CTF.
functions: Five puzzles correspond to the letters F, L, A, R, E; solving one produces an 8-bit binary flag that is entered on 0/1 buttons, which lights that letter's LED. Lighting all five unlocks a sixth, undocumented secret puzzle.
look:
  colors:
  - black
  - red
  - pink
  shape: rectangle
  themes:
  - skull
  - ctf
  - security
  form_factor: pcb badge
tech:
  mcu: Nuvoton
  leds:
    count: 5
    type: null
    note: One LED per letter of FLARE, lit as each CTF stage is solved; a sixth, secret stage is not shown on the badge.
  display: none
  connectivity: []
  inputs:
  - buttons
  battery: 2x CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: LinkedIn - Flare Blinky Badge post
  url: https://www.linkedin.com/posts/abhinavpandagale_badgelife-ugcPost-7491636243009744897-nu2v/?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAB3fw5gBqJoYA61FQdWI5EpucBJXh1UrtDQ
  kind: video
- label: "FLARE — CTF Badge (Hackerware.io project page)"
  url: https://www.hackerware.io/flare
  kind: website
images:
- file: assets/images/badges/dc34/flare-blinky-badge/f87e2e21e1.jpg
  source: "https://www.linkedin.com/posts/abhinavpandagale_badgelife-ugcPost-7491636243009744897-nu2v/"
  credit: "Hackerware.io / Abhinav Panda"
  caption: "The Flare Blinky Badge: a black PCB badge with a skeleton motif in magenta silkscreen, LEDs behind the acrylic overlay, and FLARE printed vertically"
contact:
  discord: abhinav_panda
  emails:
  - abhinav@hackerwares.in
  raw:
  - 'Twitter: TweetsFromPanda'
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 65
  updated: 8/7/2026 18:32:40
  listing: New
- kind: url
  url: https://www.linkedin.com/posts/abhinavpandagale_badgelife-ugcPost-7491636243009744897-nu2v/
  title: "Abhinav Pandagale on LinkedIn: Flare Blinky Badge #badgelife"
  accessed: '2026-09-06'
  note: Confirms the title and maker; the post is a video with a still frame showing the badge (black PCB, magenta skeleton graphic, vertical FLARE wordmark) - no other specs given in the post text itself.
- kind: url
  url: https://www.hackerware.io/flare
  title: "FLARE — CTF Badge"
  accessed: '2026-09-06'
  note: Maker's dedicated project microsite for the Flare badge. Describes a Nuvoton MCU, 2x CR2032 coin cells, a laser-cut acrylic skeleton overlay over the PCB, one LED per letter of F-L-A-R-E lit by solving five CTF puzzles (each yielding an 8-bit binary flag entered via 0/1 buttons plus a CTF-mode button), and an undocumented sixth "secret" puzzle. Page footer credits "a CTF badge by Hackerware, flare.io - 2026" but does not separately name a "blinky" variant.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The sheet lists "Flare Blinky Badge" (this entry, row 65) and "Flare CTF Badge" (dc34-flare-ctf-badge, row 66) as separate rows, and a maker tweet cited on the CTF entry calls the pair a single "Blinky & CTF Badge" release. The only dedicated technical source found, hackerware.io/flare, describes one physical badge combining both the letter-lighting "blinky" LED behavior and the CTF puzzle mechanic - it is unclear whether "blinky" and "CTF" were sold/distributed as two distinct physical items or are two names for the same badge's two functions. Treated as a separate entry per the sheet, with duplicate_of dc34-flare-ctf-badge noted. Could not find price, quantity made, availability, exact LED part number, or design files from any source.
last_modified_date: '2026-09-06'
---

Hackerware.io (Abhinav Panda) built this badge for Flare, the threat-intelligence company behind flare.io, for DEF CON 34. It runs on a Nuvoton microcontroller powered by two CR2032 coin cells, with a laser-cut acrylic layer bearing a skeleton graphic bonded over a full-colour printed PCB so the badge's LEDs bleed light up through the artwork.

The badge doubles as a small CTF: five puzzles correspond to the letters F, L, A, R and E, and solving one yields an 8-bit binary flag. Holding a dedicated CTF button and entering the flag's eight bits on paired 0/1 buttons lights the matching letter if correct. Lighting all five letters unlocks a sixth, secret puzzle that the maker's own project page does not document anywhere.

The sheet also lists a separate "Flare CTF Badge" entry from the same maker and event, and a tweet cited there describes the release as a single "Blinky & CTF Badge." It was not possible to confirm from available sources whether "blinky" and "CTF" are two distinct physical badges or two names for the same board's two behaviors; this entry follows the sheet in treating them separately. Price, quantity made, availability, and design files were not found.
