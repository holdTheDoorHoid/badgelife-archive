---
title: LAN PARTY EVENT BADGE
id: saintcon-2023-lan-party-event-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: SHIFTY
summary: 'A SAINTCON 2023 event minibadge for the con''s LAN Party room, handed out to attendees who came to play.'
functions: 'Two onboard LEDs light up when powered through the host badge''s pin header; otherwise decorative, marking the wearer as a LAN Party attendee.'
look:
  colors: [black, white]
  shape: rectangle
  themes: [retro computer, text]
tech:
  mcu: none
  leds:
    count: 2
    type: reverse-mount
    note: 'Two LEDs (D1, D2) and a single resistor (R1); no microcontroller.'
  display: none
  connectivity: []
  battery: null
  sao_version: null
  power: powered by host badge
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution: [free_drop]
  where: 'Given out at the LAN Party room at SAINTCON 2023; not sold.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023
  url: https://minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023
  kind: website
images:
- file: assets/images/badges/saintcon-2023/lan-party-event-badge/3565a94c76.png
  source: "https://minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023"
  credit: "SHIFTY"
  caption: "LAN Party Event Badge, front"
- file: assets/images/badges/saintcon-2023/lan-party-event-badge/8d1855ab87.png
  source: "https://minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023"
  credit: "SHIFTY"
  caption: "LAN Party Event Badge, back"
contact: {}
notes:
- 'category: Event; rarity: Rare'
- 'Soldering difficulty listed as Beginner: solder the two LEDs and the resistor using the single-pad method, then the pin headers.'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=LAN%20PARTY%20EVENT%20BADGE&year=2023
  title: LAN PARTY EVENT BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2023''.'
- kind: url
  url: https://minibadge.wiki/2023.json
  title: 'MiniBadge Wiki 2023 data feed (LAN PARTY EVENT BADGE entry)'
  accessed: '2026-09-07'
  note: 'Underlying JSON record for the badge: maker SHIFTY, description, soldering instructions/difficulty, category Event, rarity Rare, front/back image paths, "how to acquire" text. The page itself is a JS single-page app that renders from this feed.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source is the minibadge.wiki community database (a fan-run archive of SAINTCON minibadges, not the maker''s own page); no maker storefront, repo, or social post was found for SHIFTY or this specific badge, so hardware/PCB files and open-source status are unknown. quantityMade in the source feed is 0, which is minibadge.wiki''s default/unset value for many entries rather than a stated print run, so get_one.quantity is left blank rather than reported as zero. The badge''s description lists the LAN party''s game lineup (StarCraft, Cursed Halo, Battlefield 1942, Minecraft, Overwatch 2, League of Legends, Rocket League, Payday 2) as event flavor text, not badge features.'
last_modified_date: '2026-09-07'
---

The LAN Party Event Badge is a SAINTCON 2023 minibadge made by SHIFTY for the convention's LAN Party room, a dedicated space where attendees played games together — StarCraft, Cursed Halo, Battlefield 1942, Minecraft, Overwatch 2, League of Legends, Rocket League, and Payday 2, among others. It was not sold; attendees got one simply by showing up to the LAN Party.

The badge is a black PCB with white silkscreen art of a hooded gamer flanked by controllers, framed by an arc and the words "LAN PARTY" in a blocky pixel font. Electrically it is simple: two LEDs (D1, D2) and a single current-limiting resistor (R1), with no microcontroller, wired to light up when the badge draws power through its host badge's pin header — standard for a SAINTCON minibadge that plugs onto a larger master badge rather than carrying its own battery. The back is marked "SAINTCON 2023 / SHIFTY." Soldering is rated Beginner: the LEDs and resistor go on first using the single-pad hand-soldering method, followed by the pin headers.

The only source located for this badge is the minibadge.wiki community database, a fan-maintained catalog of SAINTCON minibadges; no storefront, repository, or social post from SHIFTY was found, so it isn't known whether design files were ever published.
