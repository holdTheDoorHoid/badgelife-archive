---
title: Flying Skull Badge
id: dc26-flying-skull-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: b1uN7
  url: https://github.com/b1uN7
summary: A DEF CON 26 wearable badge, shaped like a skull and crossbones, that doubles as a flying quadcopter built around a modified Syma 5X mini-drone platform.
functions: Worn as a normal badge with blinking LED patterns; can be flown as a quadcopter using a Syma 5X-based Flight Control Unit (FCU), detachable motor pods, and 3D-printed motor mounts. Supports an "Addon board" expansion header for extra add-ons.
look:
  colors:
  - red
  - black
  shape: skull
  themes:
  - skull
  - robot
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: LiPo (Syma 5X quadcopter battery)
  sao_version: null
get_one:
  price: "$65+ (Kickstarter pledge, badge board + Arduino Leonardo dev board)"
  price_usd: 65
  quantity: ''
  availability: sold_out
  distribution:
  - crowdfunding
  where: Funded via Kickstarter (May 23 - June 4, 2018); shipped to 109 backers who pledged an average of $177. A prior version, the DEF CON 25 "Friends of b1un7" Flying Skull, was hand-made in a run of 25 and given only to friends/mentors.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/b1uN7/DEFCON-26-Flying-Skull-Badge
  firmware_url: https://github.com/b1uN7/DEFCON-26-Flying-Skull-Badge/tree/master/Code
  eda_tool: null
links:
- label: github.com/b1uN7/DEFCON-26-Flying-Skull-Badge
  url: https://github.com/b1uN7/DEFCON-26-Flying-Skull-Badge
  kind: repo
- label: "DEFCON 26 Flying Electronic Quad Copter Skull Badge (Kickstarter)"
  url: https://www.kickstarter.com/projects/1011964033/defcon-26-flying-electronic-quad-copter-skull-badg
  kind: store
- label: "Awesome DEFCON 26 Flying Quad Copter Skull Badge (Geeky Gadgets)"
  url: https://www.geeky-gadgets.com/defcon-26-flying-quad-copter-skull-badge-24-05-2018/
  kind: article
images:
  - file: assets/images/badges/dc26/flying-skull-badge/649e458419.jpg
    source: "https://github.com/b1uN7/DEFCON-26-Flying-Skull-Badge"
    credit: "b1uN7"
    caption: "Top view of the Flying Skull Badge PCB (skull and crossbones shape)"
  - file: assets/images/badges/dc26/flying-skull-badge/12ec6e822d.jpg
    source: "https://github.com/b1uN7/DEFCON-26-Flying-Skull-Badge"
    credit: "b1uN7"
    caption: "Bottom view of the Flying Skull Badge PCB"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/b1uN7/DEFCON-26-Flying-Skull-Badge
  title: Flying Skull Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc26''.'
- kind: url
  url: https://github.com/b1uN7/DEFCON-26-Flying-Skull-Badge
  title: b1uN7/DEFCON-26-Flying-Skull-Badge README and repo contents
  accessed: '2026-09-07'
  note: Confirmed it is a quadcopter-based badge for DEF CON 26 (2018), built on the Syma 5X platform with a Flight Control Unit board, 3D-printed motor mounts, and an addon-board header; found the Skull_badge_V2/Images photos used above.
- kind: url
  url: https://www.kickstarter.com/projects/1011964033/defcon-26-flying-electronic-quad-copter-skull-badg
  title: "DEFCON 26 Flying Electronic Quad Copter Skull Badge by b1un7 (Kickstarter)"
  accessed: '2026-09-07'
  note: Pledge price ($65+), 109 backers, $19,292 raised of a $1,000 goal, funded May 23-Jun 4 2018 (page itself returned 403 to direct fetch; details via Kicktraq mirror and search results).
- kind: url
  url: https://www.kicktraq.com/projects/1011964033/defcon-26-flying-electronic-quad-copter-skull-badg/
  title: "DEFCON 26 Flying Electronic Quad Copter Skull Badge :: Kicktraq"
  accessed: '2026-09-07'
  note: Mirror of the Kickstarter stats (backers, funding total, dates, creator).
- kind: url
  url: https://www.geeky-gadgets.com/defcon-26-flying-quad-copter-skull-badge-24-05-2018/
  title: "Awesome DEFCON 26 Flying Quad Copter Skull Badge - Geeky Gadgets"
  accessed: '2026-09-07'
  note: Confirmed Arduino Leonardo-based FCU and the DEF CON 25 predecessor run of 25 hand-made badges; page itself blocked direct fetch by Cloudflare, summarized via search snippet.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >
    A web search snippet (Hackster.io, not independently re-verified because the page returned
    403) additionally described the badge as having an ATmega32U4 MCU, 16 WS2812B LEDs along the
    crossbones, a piezo buzzer, and 6 switches — plausible and consistent with the Arduino
    Leonardo board mentioned elsewhere, but left out of tech./look. fields here because it could
    not be confirmed against a source actually read. LED count/type, MCU, display, and SAO
    fields are left empty for that reason. Quantity made for DC26 specifically was not found
    (only the DC25 predecessor's run of 25 is documented). License is not stated in the repo.
last_modified_date: '2026-09-07'
---

The Flying Skull Badge is b1uN7's DEF CON 26 (2018) follow-up to a hand-made DEF CON 25 badge he had given only to 25 close friends and mentors. Where most badges are static PCBs, this one is a wearable skull-and-crossbones board built around a modified Syma 5X mini quadcopter: a red Flight Control Unit board, a pair of motor pods with 3D-printed mounts, and matched A/B propellers, so the badge can be taken apart and actually flown. It also carries an add-on expansion header for further attachments.

b1uN7 crowdfunded the DC26 run on Kickstarter in May-June 2018, offering the badge board bundled with an Arduino Leonardo-compatible development board starting at $65; the campaign drew 109 backers and raised roughly $19,300 against a $1,000 goal. Hardware files (PCB designs, 3D-printable motor mounts, and firmware/code) are published on GitHub, though the README is written as an informal, still-evolving build guide rather than a polished manual, and repeatedly warns builders about specific soldering hazards on the Syma FCU board.

Some third-party coverage describes further electrical specifics (an ATmega32U4 MCU and 16 WS2812B LEDs along the crossbones) that could not be independently confirmed from a source this pass could actually read in full, so those fields are left blank rather than guessed.
