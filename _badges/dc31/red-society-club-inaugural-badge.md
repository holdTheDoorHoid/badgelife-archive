---
title: RSC Jellyfish Badge
id: dc31-red-society-club-inaugural-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Red Society Club
  url: https://lightfootlabs.io/blog/rsc-badgelife-journey
- name: Jaime Lightfoot
  url: https://lightfootlabs.io
  role: designer (Lightfoot Labs)
summary: A hand-assembled jellyfish-themed PCB art badge made by Jaime Lightfoot (Lightfoot Labs) for the Red Society Club Discord group's debut at DEF CON 31.
functions: Decorative PCB art badge; lights up in rainbow/UV-reactive patterns via onboard NeoPixels, USB-chargeable, battery powered, no interactive game or CTF.
look:
  colors:
  - black
  - copper
  - white
  shape: jellyfish
  themes:
  - animal
  - art
tech:
  mcu: ATtiny85
  leds:
    count: 10
    type: WS2812B/SK6812-compatible (NeoPixel)
    note: Arranged around the jellyfish artwork; brightness limited in firmware to conserve battery.
  display: none
  connectivity: []
  battery: LiPo, charged via micro USB, with a boost converter for the LED supply
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '50 (hand-assembled; made from a batch of 100 blank PCBs)'
  availability: unknown
  distribution:
  - purchase
  where: Sold via Ko-fi with pickup in person at DEF CON 31 in Las Vegas; also announced on the Red Society Club Discord.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/lightfoot-labs/rsc-badge-programming
  eda_tool: KiCad
links:
- label: ko-fi.com/s/ccfd6f4176
  url: https://ko-fi.com/s/ccfd6f4176
  kind: store
- label: 'RSC Badge Part 1: The Journey to Building the RSC Badge'
  url: https://lightfootlabs.io/blog/rsc-badgelife-journey
  kind: article
  note: Design goals, artwork process, PCB-art background.
- label: 'RSC Badge Part 2: Artwork, Prototyping, and Solving Complexity'
  url: https://lightfootlabs.io/blog/rsc-badge-part-2-prototyping-and-solving-complexity/
  kind: article
  note: Prototyping and design-constraint decisions.
- label: 'RSC Badge Part 3: KiCad, Manufacturing, and DEFCON 31'
  url: https://lightfootlabs.io/blog/rsc-badge-part-3-kicad/
  kind: article
  note: Schematic/layout, board house selection, manufacturing issues, final assembly, quantity made.
- label: rsc-badge-programming (reprogramming guide)
  url: https://github.com/lightfoot-labs/rsc-badge-programming
  kind: repo
  note: Confirms ATtiny85 MCU, 10 NeoPixel LEDs, and Arduino-based reprogramming steps; no hardware/Gerber files published here.
images:
- file: assets/images/badges/dc31/red-society-club-inaugural-badge/e326fc2ca7.jpg
  source: "https://lightfootlabs.io/blog/rsc-badge-part-3-kicad/"
  credit: "Jaime Lightfoot / Lightfoot Labs"
  caption: "The finished RSC jellyfish badge showing exposed copper and epoxy coating"
- file: assets/images/badges/dc31/red-society-club-inaugural-badge/beebb15003.png
  source: "https://lightfootlabs.io/blog/rsc-badgelife-journey"
  credit: "Jaime Lightfoot / Lightfoot Labs"
  caption: "The jellyfish artwork, drawn in Procreate, that became the badge design"
contact: {}
notes:
- 'The event-year sweep found this only as a Ko-fi listing title, "Red Society Club Inaugural Badge"; the maker''s own blog series and GitHub repo call it the "RSC Jellyfish Badge" / "RSC badge," which this entry now uses as the title.'
- Two Ko-fi listings exist for the same badge (ccfd6f4176 and 6f27d9fb7f), both "pickup at DEF CON" variants; only the one already on file is kept in links.
- Price and current stock status were not stated on any reachable page (the Ko-fi store itself returns a Cloudflare challenge to automated fetches); quantity made (50, from 100 blank PCBs) came from the maker's manufacturing writeup.
status: released
sources:
- kind: url
  url: https://ko-fi.com/s/ccfd6f4176
  title: RSC DEFCON 2023 Badge (Pickup in Person at DEFCON Las Vegas) - Red Society Club's Ko-fi Shop
  accessed: '2026-09-10'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc31-indie); confirmed via search snippet (page itself blocked by Cloudflare); event read as ''dc31''.'
- kind: url
  url: https://lightfootlabs.io/blog/rsc-badgelife-journey
  title: 'The Journey to Building the RSC Badge: Part 1'
  accessed: '2026-09-10'
  note: Maker, event, jellyfish theme, design goals.
- kind: url
  url: https://lightfootlabs.io/blog/rsc-badge-part-2-prototyping-and-solving-complexity/
  title: 'RSC Badge Part 2: Artwork, Prototyping, and Solving Complexity'
  accessed: '2026-09-10'
  note: Prototyping details.
- kind: url
  url: https://lightfootlabs.io/blog/rsc-badge-part-3-kicad/
  title: 'RSC Badge Part 3: KiCad, Manufacturing, and DEFCON 31'
  accessed: '2026-09-10'
  note: MCU, LED count, power design, colors, quantity made (50 of 100 blanks), final assembly photo.
- kind: url
  url: https://github.com/lightfoot-labs/rsc-badge-programming
  title: rsc-badge-programming
  accessed: '2026-09-10'
  note: Confirms ATtiny85 and 10 NeoPixel LEDs; reprogramming guide, no license stated.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Core facts (maker, MCU, LEDs, power, quantity, theme) confirmed via the maker's own three-part blog series and GitHub repo. Price, current availability, and a hardware (KiCad/Gerber) repo link were not found; the Ko-fi storefront itself could not be fetched directly due to a Cloudflare bot check, so availability is left unknown. No hardware source files were located, only the firmware reprogramming guide, so open_source is marked partial rather than yes.
last_modified_date: '2026-09-10'
---

The RSC Jellyfish Badge was the debut hardware release from the Red Society Club, a Discord community, designed by member Jaime Lightfoot of Lightfoot Labs for DEF CON 31 in 2023. It is a piece of PCB art in the shape of a jellyfish: an ATtiny85 drives ten NeoPixel-style addressable RGB LEDs arranged through the tentacles and body, with a LiPo battery, micro-USB charging, and a boost converter powering the lighting. The board leans into exposed-copper and black solder-mask contrasts, with white silkscreen detailing and an epoxy coating over the art side to protect and enhance the lit effect.

Lightfoot documented the entire process in a three-part blog series, from the original Procreate artwork and SVG2Shenzhen conversion, through prototyping and KiCad schematic/layout work, to final manufacturing at JLCPCB. The badge went through three board revisions, and unexpected FR4 watermarking on the purchased blanks meant only 50 of 100 ordered boards were usable as finished badges; each was hand-assembled and reflowed on a T-962 oven. Badges were distributed via Ko-fi listings for pickup in person at DEF CON 31 in Las Vegas, and announced to the group's Discord server.

A companion GitHub repository documents how to reprogram the badge's ATtiny85 using an Arduino as an ISP, confirming the MCU and LED count, but no hardware design files (KiCad project or Gerbers) were published publicly, so the badge is only partially open source. Price and current stock status were not confirmed, since the Ko-fi storefront returns a bot-check page to automated access.
