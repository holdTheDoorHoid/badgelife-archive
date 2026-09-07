---
title: LHC Badge for DC 26
id: dc26-lhc-badge-for-dc-26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: TechGirl
  url: https://hackaday.io/TechGirl
summary: A simple, learn-to-solder blinky badge made for the Lonely Hackers Club (LHC), an online group for solo travelers and first-time DEF CON attendees, so members could identify each other at DEF CON 26.
functions: A 555 timer in astable mode drives a 4017 decade counter that sequentially lights 12 3mm LEDs around the edge of the badge; no microcontroller.
look:
  colors: [green, white]
  shape: circle
  themes: [meme, learn to solder, blinky]
tech:
  mcu: none
  leds:
    count: 12
    type: discrete
    note: 3mm LEDs, sequenced by a 4017 decade counter clocked by a 555 timer astable oscillator
  display: none
  connectivity: []
  battery: 2x CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Hand-soldered by TechGirl for LHC members at DEF CON 26 (2018); a possible future Tindie presale was mentioned but not confirmed as having happened.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  gerbers_url: https://cdn.hackaday.io/files/1591926810870528/Gerber_LHC_noIMAge.zip
  eda_tool: null
links:
- label: hackaday.io/project/159192-lhc-badge-for-dc-26
  url: https://hackaday.io/project/159192-lhc-badge-for-dc-26
  kind: hackaday
images:
  - file: assets/images/badges/dc26/lhc-badge-for-dc-26/d025680fcc.jpg
    source: "https://hackaday.io/project/159192-lhc-badge-for-dc-26"
    credit: "TechGirl"
    caption: "Front of the round PCB badge, DC26 with LHC 'crossbones' logo"
  - file: assets/images/badges/dc26/lhc-badge-for-dc-26/e4219f41cb.jpg
    source: "https://hackaday.io/project/159192-lhc-badge-for-dc-26"
    credit: "TechGirl"
    caption: "Assembled badge with LEDs lit and CR2032 battery holder wired on"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159192-lhc-badge-for-dc-26
  title: LHC Badge for DC 26
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''DEF CON 26''.'
- kind: url
  url: https://hackaday.io/project/159192-lhc-badge-for-dc-26/log/150338-gerber-available
  title: "Gerber available - project log"
  accessed: '2026-09-07'
  note: Confirms gerber files were posted (artwork removed) and gives a rough build timeline (badges soldered late July/early Aug 2018).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io project page and log confirm what the badge is, who made it, and why. No price, quantity made, or confirmed sales channel found — TechGirl mentions a possible future Tindie presale but there is no evidence it happened. No separate firmware/hardware repo; only a Gerber zip (artwork removed) was published, so open_source is set to partial rather than yes.'
last_modified_date: '2026-09-07'
---

TechGirl designed this round PCB badge in 2018 for the Lonely Hackers Club (LHC), an online community for solo travelers and first-time DEF CON attendees. The idea was twofold: give LHC members a way to spot each other on the DEF CON 26 floor, and give newcomers an easy, low-cost entry into "badgelife" blinky culture. The badge is deliberately simple — no microcontroller — built around a 555 timer running in astable mode to generate a clock signal that a 4017 decade counter uses to sequentially light 12 3mm LEDs around the badge's edge. It runs on two CR2032 coin cells, good for roughly 96 hours of continuous blinking, and doubles as an approachable first soldering project.

TechGirl hand-soldered a batch of these in late July/early August 2018 in the run-up to DEF CON 26, later posting on the project log about "so much soldering." She released the Gerber files (with the LHC artwork itself stripped out) so others could fabricate or adapt their own version for other learn-to-solder or blinky projects. A Tindie presale was floated as a possibility for the following year but is not confirmed to have happened.

## Make your own

Gerber files (LHC artwork removed) are posted on the project page: [Gerber_LHC_noIMAge.zip](https://cdn.hackaday.io/files/1591926810870528/Gerber_LHC_noIMAge.zip). No schematic, BOM, or EDA source files were found published alongside them.
