---
title: Enterprise Badge (DC27)
id: dc27-enterprise-badge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Enterprise Badge team
  url: https://twitter.com/enterprisebadge
summary: An unofficial DEF CON 27 badge shaped like a Star Trek starship, using exposed FR4 as a light diffuser at the edges of its warp nacelles for reverse-mount LEDs.
functions: Lights up via reverse-mount LEDs, with the bare FR4 at the leading edge of the warp nacelles acting as a diffuser for a glowing effect.
look:
  colors: []
  shape: spaceship
  themes:
  - sci-fi
  - space
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '150'
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: twitter.com/enterprisebadge
  url: https://twitter.com/enterprisebadge
  kind: social
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- label: Source files (GitHub)
  url: https://github.com/seeigecannon/DC27EnterpriseBadge
  kind: hardware
images:
- file: assets/images/badges/dc27/enterprise-badge-dc27/280d61384a.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday / Enterprise Badge team
  caption: Enterprise Badge, front
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- file: assets/images/badges/dc27/enterprise-badge-dc27/d457854cee.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday / Enterprise Badge team
  caption: FR4 diffuser detail on the edge of the warp drive nacelle
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://twitter.com/enterprisebadge
  title: Enterprise Badge (DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27
  accessed: '2026-09-07'
  note: Primary source for description, construction details, quantity made (150), and photos; links the badge to @enterprisebadge on Twitter/X.
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Confirmed via Hackaday''s DC27 badge roundup (quantity made, FR4-diffuser LED trick, double-sided assembly by skillet reflow). The @enterprisebadge Twitter/X account (linked from the Hackaday article and the original sheet) could not be read directly: x.com returned HTTP 403 to automated fetches, and a Wayback Machine snapshot from 2021-07-06 rendered as an empty React shell with no extractable bio, tweet text, or photos. Maker''s real name/team, MCU, LED count/type, price, and availability remain unknown. No repo, store listing, or design files were found.'
last_modified_date: '2026-09-07'
---

The Enterprise Badge is an unofficial hardware badge made for DEF CON 27 (2019), shaped like a Star Trek starship. Its standout trick is using bare, unmasked FR4 substrate as a light diffuser: at the leading edge of the ship's warp nacelles, exposed fiberglass catches light from reverse-mount LEDs mounted underneath, producing a soft glow along those edges rather than a sharp point source — a variation on a diffuser technique that was already common in the 2019 badgelife scene, but applied in a novel spot.

150 badges were produced in total, split evenly between bare kits and fully populated units. The populated half were hand-soldered using a skillet-reflow process, complicated by the fact that the board carries components on both sides: Teflon blocks were used to prop the PCB above the skillet surface so the already-soldered bottom side wouldn't be damaged during the second reflow pass.

Beyond the DEF CON forum and Hackaday coverage of that year's unofficial badge crop, the only maker-side presence found was the @enterprisebadge account on Twitter (now X), which could not be read by this pass — the live site blocks automated fetches and the one available Wayback snapshot is a JavaScript shell with no recoverable content. As a result, the maker's identity, the badge's MCU, LED count and type, and its price or distribution method are not confirmed by any source read here.
