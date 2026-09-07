---
title: 3d6 Badge
id: dc29-3d6-badge
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: Alt_Bier
  url: https://twitter.com/alt_bier
summary: A GURPS player-character-sheet badge with three seven-LED dice that light up to show values one through six.
functions: 'Hitting the "Roll Dice" button (wired to the chip reset pin) re-rolls the three onboard LED dice, each showing a value 1-6.'
look:
  colors:
  - blue
  - red
  - pink
  - multicolor
  shape: card
  themes:
  - fantasy
tech:
  mcu: CH552G
  leds:
    count: 21
    type: discrete
    note: Seven LEDs per die (three dice, 21 total), grouped into pairs plus a single LED so each die needs only 4 MCU pins.
  display: none
  connectivity: []
  battery: 3xAAA
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as a badge kit (assembled badge, lanyard, 3xAAA batteries, clip-on pencil, stickers) around DEF CON 29 (2021).
make_your_own:
  open_source: yes
  hardware_url: https://github.com/gowenrw/3d6_badge/tree/main/eda
  firmware_url: https://github.com/gowenrw/3d6_badge/tree/main/code
  eda_tool: KiCad
  license: MIT
  notes: Repo also includes the art directory (silkscreen art) and reference_parts.
links:
- label: 3d6badge.altbier.us
  url: https://3d6badge.altbier.us/
  kind: website
- label: gowenrw/3d6_badge
  url: https://github.com/gowenrw/3d6_badge
  kind: repo
- label: '@alt_bier on Twitter/X'
  url: https://twitter.com/alt_bier
  kind: social
- label: 'Intro to the CH552G Microcontroller (YouTube)'
  url: https://www.youtube.com/watch?v=EKhntUyfqhQ
  kind: video
images:
- file: assets/images/badges/dc29/3d6-badge/ffcf792f51.jpg
  source: "https://3d6badge.altbier.us/"
  credit: "Alt_Bier"
  caption: "3d6 Badge assembled and lit, showing the three LED dice"
- file: assets/images/badges/dc29/3d6-badge/9996c59b79.jpg
  source: "https://3d6badge.altbier.us/"
  credit: "Alt_Bier"
  caption: "Front and back of the 3d6 Badge with kit accessories"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- 'Maker''s site attributes the concept to discussions in the "3000 Society" tabletop gaming group: two dice were planned originally, and adding a third suggested a GURPS (Generic Universal Role Play System) character sheet layout.'
- Event/year inferred from the badge kit page, which describes a sticker "using the DEFCON 29 theme colors" and battery life lasting "the entire DEFCON conference" — the site itself does not state the con/year outside that context.
status: released
sources:
- kind: url
  url: https://3d6badge.altbier.us/
  title: 3d6 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''3000 Society / DEF CON 2021''.'
- kind: url
  url: https://3d6badge.altbier.us/
  title: 3d6_badge | All files related to the 3d6 badge
  accessed: '2026-09-07'
  note: Maker's project homepage; concept origin (3000 Society gaming group), silkscreen/art details, CH552G MCU choice, LED dice wiring, KiCad EDA, repo link.
- kind: url
  url: https://3d6badge.altbier.us/badgekit.html
  title: 3d6 Badge Kit
  accessed: '2026-09-07'
  note: Badge kit contents (assembled badge, lanyard, 3xAAA batteries, pencil, stickers), LED color variants (mostly blue, limited red/pink/multicolor), and the "DEFCON 29 theme colors" sticker detail used to confirm event/year.
- kind: url
  url: https://github.com/gowenrw/3d6_badge
  title: gowenrw/3d6_badge
  accessed: '2026-09-07'
  note: Confirms MIT license and KiCad/code/art/eda repo structure.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Price, quantity made, and exact distribution mechanism (free vs. sold) were not stated on any source; get_one fields left mostly empty. Event/year (DEF CON 29, 2021) is inferred from the "DEFCON 29 theme colors" sticker description on the badge-kit page rather than an explicit statement, so confidence is medium rather than high.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/3d6-badge/
---

The 3d6 Badge, made by Alt_Bier (gowenrw), reimagines the classic six-sided-die roller as a GURPS (Generic Universal Role Play System) player character sheet. The concept grew out of discussions in the "3000 Society" tabletop gaming group: what started as a two-die roller became a three-die badge once the maker realized a 3d6 layout doubled as a GURPS stat block. The front silkscreen carries writable character-sheet fields (with an included clip-on pencil), dice-shaped outlines forming the 3000 Society logo, and a hand-drawn RPG-module-style art block made by the maker's son; the back carries two character portraits drawn by the maker's daughter.

Each of the three dice is built from seven LEDs arranged to display values one through six, wired in pairs plus a single LED so each die needs only four microcontroller pins — twelve pins total, which maxed out the CH552G MCU the badge is built around. With no pins left for a dedicated button, "rolling" the dice is done by pressing a button tied to the chip's reset pin, power-cycling the badge to re-randomize the display. The badge runs on 3xAAA batteries sized to last a multi-day DEF CON conference.

Badges were distributed as a kit — assembled unit, lanyard, batteries, pencil, and stickers — with most boards in blue and limited runs in red, pink, and multicolor (one color per die). A kit-page sticker described as using "DEFCON 29 theme colors" places the badge at DEF CON 29 (2021). Hardware, firmware, and artwork are published under the MIT license in the maker's GitHub repository, including KiCad source files and Gerbers used for fabrication.
