---
title: Noob Village Name Tag Badge
id: dc34-noob-village-name-tag-badge
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
summary: A "hello, my name is" tag, a beginner learn-to-solder kit, and a tap-to-flash NFC card on one small PCB, given away free at Noob Village.
functions: Name Tag + Learn To Solder Kit + NFC Tag
look:
  colors:
  - black
  - yellow
  - pink
  - blue
  - green
  - purple
  shape: rectangle
  themes:
  - learn to solder
  - village badge
  - text
  - jewelry
tech:
  mcu: none
  leds:
    count: 4
    type: through-hole
    note: Four through-hole (PTH type-3) LEDs the wearer solders themselves at D5-D8, bent flat to shine through a laser-cut acrylic name plate.
  display: none
  connectivity:
  - nfc
  battery: CR2032 coin cell (pre-fitted)
  sao_version: none
get_one:
  price: Free giveaway at Noob Village
  price_usd: 0.0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  - village
  where: Free giveaway at Noob Village at DEF CON 34; badge color signals role (pink attendee, yellow staff, blue volunteer, green speaker, magenta for the Octopus Game).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.noobvillage.org/badges
  url: https://www.noobvillage.org/badges
  kind: repo
- label: Noob Village Badge microsite (Hackerware)
  url: https://sites.google.com/view/noobvillage/badges
  kind: website
- label: Hackerware.io
  url: https://hackerware.io
  kind: website
  archived: https://web.archive.org/web/20260523123718/https://hackerware.io/
images:
- file: assets/images/badges/dc34/noob-village-name-tag-badge/a333a5a030.jpg
  source: https://www.noobvillage.org/badges
  credit: Hackerware.io
  caption: 'Five Noob Village badge color variants: staff (yellow), attendee (pink), volunteer (blue), speaker (green), and Octopus Game (magenta)'
- file: assets/images/badges/dc34/noob-village-name-tag-badge/628b1bc1de.jpg
  source: https://www.noobvillage.org/badges
  credit: Hackerware.io
  caption: PCB layout render showing the solder points (D5-D8 LEDs, R1-R5 resistors), coin cell holder, slide switch, and NFC tag area
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
  row: 62
  updated: 8/7/2026 18:08:13
  listing: New
- kind: url
  url: https://www.noobvillage.org/badges
  title: NOOBVILLAGE.ORG - Badges
  accessed: '2026-09-06'
  note: Confirms the badge redirects to a Hackerware-built microsite; page itself is a Google Sites shell.
- kind: url
  url: https://sites.google.com/view/noobvillage/badges
  title: Noob Village Badge · Hackerware
  accessed: '2026-09-06'
  note: 'Full product microsite: features, build steps, LED/resistor placement, NFC behavior, coin cell power, five role-based color variants, and both photos used above.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Maker's own microsite (embedded in the Noob Village site) fully describes the badge; no third-party coverage found. Quantity made and any hardware/firmware file releases are not stated anywhere found, so those fields are left empty. No open-source design files (Gerbers, BOM, etc.) were located.
last_modified_date: '2026-09-06'
---

The Noob Village Name Tag Badge is a beginner-friendly PCB badge Hackerware.io (Abhinav Panda) built for DEF CON 34's Noob Village, aimed at attendees who have never picked up a soldering iron. The board does three jobs at once: it's a wearable "Hello, my name is" tag, a learn-to-solder kit (four through-hole LEDs and three resistors placed at marked pads), and a rewritable NFC tag that can be tapped to share a link, socials, text, or a rickroll. A CR2032 coin cell comes pre-installed on the back, so there's no battery to source — flip the slide switch and the badge lights up.

The badge doubles as a role indicator at the village: everyone builds the same PCB, but the color of the board signals what the wearer is doing there — pink for attendees (the majority), yellow for staff, blue for volunteers, green for speakers, and a magenta variant tied to an "Octopus Game." A laser-cut acrylic name plate sits over the board's middle; once the bent-over LED legs are soldered flat against it, the plate glows with the wearer's handwritten, drawn, or printed name. Hackerware's own microsite for the badge walks through the seven-step build (roughly 15 minutes) with clear polarity guidance for the LEDs, and separately explains how to write and re-flash the onboard NFC tag.

No public repository, BOM, or Gerber files for the design were found, and neither the quantity produced nor a firm build date beyond "DEF CON 34" is stated on the maker's page.
