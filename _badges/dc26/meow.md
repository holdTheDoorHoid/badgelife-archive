---
title: DEF CON 26 Maneki-neko Badge
id: dc26-meow
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Sean McCabe (devoopes)
  url: https://github.com/devoopes
- name: Daniel Samarin
summary: An unofficial DEF CON 26 badge shaped like a maneki-neko (beckoning cat), with a servo-driven 3D-printed arm that waves while dual 16-segment LED displays blink.
functions: Waves a 3D-printed cat arm via a servo motor; drives two 16-segment LED displays that blink in time with the arm's motion.
look:
  colors: []
  shape: cat
  themes:
  - cat
  - animal
tech:
  mcu: STM32
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: v1
get_one:
  price: $80 cash
  price_usd: 80
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: 'Sold in person at DEF CON 26 for $80 cash, via a "drop" system: buyers had to follow @ManekiNekoDC on Twitter and wait for announcements of when/where the badge would be sold. It sold out quickly.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/devoopes/defcon26-meow/tree/master/pcb/eagle
  firmware_url: https://github.com/devoopes/defcon26-meow
  eda_tool: Eagle
  fab_url: https://oshpark.com/shared_projects/X3Hxcson
  notes: The board was originally started in KiCad but the design was redone in Eagle once more experienced help came aboard; Eagle files are in the repo's pcb/eagle directory. A build guide is in the repo's guide directory. Gerbers are in the repo and the board is also shared on OSH Park.
links:
- label: github.com/devoopes/defcon26-meow
  url: https://github.com/devoopes/defcon26-meow
  kind: repo
- label: 'Engadget: This cute Def Con badge beckons you to hack it'
  url: https://www.engadget.com/2018/08/15/this-cute-def-con-badge-beckons-you-to-hack-it/
  kind: article
- label: 'Hackaday: All the Badges of DEF CON 26 (Vol 1)'
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  kind: article
- label: 'BadgeLife - A Hackaday Documentary (YouTube)'
  url: https://www.youtube.com/watch?v=G2fHKRONc6U
  kind: video
- label: OSH Park shared project
  url: https://oshpark.com/shared_projects/X3Hxcson
  kind: fab
images:
- file: assets/images/badges/dc26/meow/7200b6b6c8.jpg
  source: "https://github.com/devoopes/defcon26-meow"
  credit: "devoopes / Sean McCabe"
  caption: "First look at the fabricated PCB boards from the fab house"
- file: assets/images/badges/dc26/meow/850ce03276.gif
  source: "https://www.engadget.com/2018/08/15/this-cute-def-con-badge-beckons-you-to-hack-it/"
  credit: "Roberto Baldwin"
  caption: "The finished Maneki-neko badge with its waving 3D-printed arm, worn at DEF CON 26"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/devoopes/defcon26-meow
  title: defcon26-meow
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 26''.'
- kind: url
  url: https://github.com/devoopes/defcon26-meow
  title: 'GitHub: SeanLeftBelow/devoopes - defcon26-meow README'
  accessed: '2026-09-07'
  note: 'README confirms name (Maneki-neko Badge), STM32 MCU, servo + dual 16-segment LEDs, art by Jeff Chang, Eagle/KiCad history, OSH Park fab link, SAO write-up, and press links.'
- kind: url
  url: https://www.engadget.com/2018/08/15/this-cute-def-con-badge-beckons-you-to-hack-it/
  title: 'Engadget: This cute Def Con badge beckons you to hack it'
  accessed: '2026-09-07'
  note: 'Confirmed creators Sean McCabe and Daniel Samarin, $80 cash price, Twitter-drop distribution, sold out, and design intent quotes.'
- kind: url
  url: https://hackaday.com/2018/08/14/all-the-badges-of-def-con-26-vol-1/
  title: 'Hackaday: All the Badges of DEF CON 26 (Vol 1)'
  accessed: '2026-09-07'
  note: 'Listed as press coverage in the repo README; not separately fetched.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Sheet slug/title was generic ("meow"); actual maker name for the badge is "DEF CON 26 Maneki-neko Badge". The repo README also describes a matching SAO ("Special Addons") that copies the main badge design, documented at https://github.com/devoopes/defcon26-meow/tree/master/addon - this looks like a separate item worth its own entry (see other_items_found). Quantity made and exact LED part number/count were not stated in any source found; left empty. tech.sao_version set to v1 as an inference from "SAO" terminology of the 2018 era but the repo does not state pin count explicitly, so treat with some caution.'
last_modified_date: '2026-09-07'
---

The DEF CON 26 Maneki-neko Badge is an unofficial conference badge made for DEF CON 26 (2018) by Sean McCabe (devoopes) and Daniel Samarin, with artwork by Jeff Chang. Styled after the Japanese "beckoning cat," the badge's signature feature is a 3D-printed cat arm driven by a small servo motor, controlled by an onboard STM32 microcontroller, which waves while two 16-segment LED displays on the front blink along with the motion.

The badge was sold in person at DEF CON 26 for $80 cash. Rather than a fixed table, the makers ran the sale as a "drop": interested buyers followed the @ManekiNekoDC Twitter account and waited for in-person sale announcements. It sold out. The project got press coverage from Engadget and Hackaday, and appeared in Hackaday's "BadgeLife" documentary.

All hardware and firmware are open source. The PCB design was originally started in KiCad but rebuilt in Eagle once more experienced collaborators joined; Eagle files, Gerbers, and a build guide are published in the GitHub repo, and the board is also shared on OSH Park for anyone to order. The same repository documents a matching SAO ("Special Addon") that mirrors the main badge's design.
