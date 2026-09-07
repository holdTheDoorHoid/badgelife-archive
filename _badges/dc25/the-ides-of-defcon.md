---
title: The Ides of Defcon
id: dc25-the-ides-of-defcon
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: John Adams
  url: https://twitter.com/netik
  role: lead / hardware
- name: Bill Paul
- name: Egan Hirvela
- name: Matthew Harris
summary: An independent, Roman-themed wearable badge for DEF CON 25, funded on Kickstarter and built by "Team Ides." It has a color touchscreen, RGB LEDs, a speaker, and a sub-1GHz radio used for on-badge games and battles.
functions: Roman battle/CTF-style games played over the badge's sub-1GHz radio, plus a menu-driven UI with audio and video playback from a microSD card.
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - wearable
tech:
  mcu: NXP/Freescale MKW01Z128 (ARM Cortex-M0+)
  leds:
    count: 12
    type: WS2812
    note: RGB addressable LEDs
  display: 2.8" TFT touchscreen, 320x240 (ER-TFTM-028-4)
  connectivity:
  - sub-ghz
  battery: LiPo 1200mAh (JST connector), USB rechargeable
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  distribution:
  - crowdfunding
  - purchase
  where: Funded via Kickstarter in 2017 (raised over $23,000); boards were manufactured and shipped by Macrofab, with additional units sold at DEF CON 25.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/netik/dc25_spqr_badge
  firmware_url: https://github.com/netik/chibios-orchard
  eda_tool: KiCad
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
links:
- label: ides.team
  url: https://ides.team/
  kind: website
- label: dc25spqr.com (badge project page)
  url: https://dc25spqr.com/
  kind: website
- label: Hackaday.io project log
  url: https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge
  kind: hackaday
- label: PCB layout (GitHub)
  url: https://github.com/netik/dc25_spqr_badge
  kind: repo
- label: Firmware source (GitHub)
  url: https://github.com/netik/chibios-orchard
  kind: repo
- label: Kickstarter campaign
  url: https://www.kickstarter.com/projects/1887776662/indie-defcon-badge-the-ides-of-defcon
  kind: store
- label: 'Post-mortem: "Ides of Def Con Badge Post-Mortem" (Medium)'
  url: https://medium.com/@spqrbadge/ides-of-def-con-badge-post-mortem-ba9d7855b85f
  kind: article
images:
  - file: assets/images/badges/dc25/the-ides-of-defcon/99a32247b6.jpg
    source: "https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge"
    credit: "Team Ides / John Adams"
    caption: "The Ides of Defcon DC25 badge"
  - file: assets/images/badges/dc25/the-ides-of-defcon/281275930c.jpg
    source: "https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge"
    credit: "Team Ides / John Adams"
    caption: "Display module used on the Ides of Defcon badge"
contact: {}
status: released
sources:
- kind: url
  url: https://ides.team/
  title: The Ides of Defcon
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc25''.'
- kind: url
  url: https://dc25spqr.com/
  title: The Ides of DEF CON
  accessed: '2026-09-07'
  note: 'Maker project page: makers, features, Kickstarter, firmware/hardware repo links, MCU.'
- kind: url
  url: https://hackaday.io/project/14756-the-ides-of-defcon-an-unofficial-electronic-badge
  title: 'The Ides of DEFCON: An Unofficial Electronic Badge - Hackaday.io'
  accessed: '2026-09-07'
  note: 'LED count/type, display, quantity estimate, form factor, badge cover image.'
- kind: url
  url: https://github.com/netik/dc25_spqr_badge
  title: netik/dc25_spqr_badge (README)
  accessed: '2026-09-07'
  note: 'Confirmed 2.8" 320x240 touchscreen part, LiPo 1200mAh battery, KiCad EDA tool, approximate per-unit fab cost.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts (maker team, event/year, MCU, display, battery, open-source repos) confirmed directly on the maker's own project page, GitHub README, and Hackaday.io log. Exact quantity produced and per-unit price were not stated on any source found, so left blank. Availability set to sold_out since this was a one-time 2017 Kickstarter/DEF CON run with no ongoing storefront found.
last_modified_date: '2026-09-07'
---

The Ides of Defcon was an independently produced, Roman-themed electronic badge built for DEF CON 25 (2017) by a team calling itself "Team Ides" — John Adams, Bill Paul, Egan Hirvela, and Matthew Harris. The project was funded through a 2017 Kickstarter campaign that raised over $23,000, with boards manufactured and shipped by Macrofab in time for the con.

The badge is built around an NXP/Freescale MKW01Z128 (ARM Cortex-M0+) microcontroller with a built-in sub-1GHz radio, which it used to run Roman battle/game mechanics between badges. It carries a 2.8" 320x240 TFT touchscreen, 12 WS2812 RGB LEDs, a small speaker, and a rechargeable 1200mAh LiPo battery, with game and media assets (audio, video, graphics) loaded from a microSD card.

Team Ides released both the PCB design (KiCad) and firmware (built on ChibiOS/Orchard) as open source on GitHub, along with a public post-mortem write-up of lessons learned from the build and a Hackaday.io project log documenting the design process. The team went on to build a follow-up badge, "da Bomb," for DEF CON 27 in 2019.

## Make your own

The full KiCad PCB layout and BOM are published at `netik/dc25_spqr_badge` on GitHub (fabrication files sized for a MacroFab run, roughly $180/board at low volume), with the firmware source in `netik/chibios-orchard`. Building a copy also requires a 2.8" ER-TFTM-028-4 resistive touchscreen module, a 3.7V 1200mAh LiPo with JST connector, an SWD-capable ARM programmer (e.g. an Olimex ARM-USB-OCD-H with a JTAG-to-SWD adapter), and a microSD card loaded with the game/media image distributed from the project page.
