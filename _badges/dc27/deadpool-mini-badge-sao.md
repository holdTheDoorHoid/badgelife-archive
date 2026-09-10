---
title: DEADPOOL Mini Badge / SAO
id: dc27-deadpool-mini-badge-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: s3gfault
  url: https://www.tindie.com/stores/s3gfault/
summary: A Deadpool-themed SAO (shitty add-on) with 16 blue LEDs driven by an ATtiny85 and an MCP23017 I2C LED driver, made for DEF CON 27.
functions: Powers on and lights all 16 blue LEDs; the ATtiny85 drives simple lighting patterns through the MCP23017 constant-current LED driver over I2C.
look:
  colors:
  - black
  - blue
  shape: skull
  themes:
  - pop culture
  - movie
  - skull
tech:
  mcu: ATtiny85
  leds:
    count: 16
    type: 1206 blue LED
    note: driven by an MCP23017 I2C constant-current LED driver commanded by the ATtiny85
  display: none
  connectivity:
  - i2c
  battery: coin cell (listed as CR2032 on Tindie; Hackaday's coverage says CR2450)
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: '200'
  availability: sold_out
  distribution:
  - purchase
  where: Sold by s3gfault (TeamID64F) on Tindie around DEF CON 27 (2019); the listing is no longer active.
  availability_note: Tindie listing shows retired/no longer available, checked 2026-09-07.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/s3gfault/deadpool-sao-with-attiny85-microcontroller
  url: https://www.tindie.com/products/s3gfault/deadpool-sao-with-attiny85-microcontroller/
  kind: store
- label: www.tindie.com/products/s3gfault/team-id64f-deadpool-badge-sao
  url: https://www.tindie.com/products/s3gfault/team-id64f-deadpool-badge-sao/
  kind: store
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- label: www.tindie.com/products/s3gfault/deadpool-badge-sao
  url: https://www.tindie.com/products/s3gfault/deadpool-badge-sao/
  kind: store
- label: www.tindie.com/stores/s3gfault
  url: https://www.tindie.com/stores/s3gfault/
  kind: store
images:
- file: assets/images/badges/dc27/deadpool-mini-badge-sao/1acb925732.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday
  caption: DEADPOOL mini badge SAO, front, lit blue
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- file: assets/images/badges/dc27/deadpool-mini-badge-sao/a24b26d075.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday
  caption: DEADPOOL mini badge SAO, rear showing ATtiny85 and MCP23017
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- file: assets/images/badges/dc27/deadpool-mini-badge-sao/11fe14b79a.jpg
  source: https://www.tindie.com/products/s3gfault/deadpool-badge-sao/
  credit: TeamID64F (s3gfault)
  caption: DeadPool Badge SAO, LEDs off
- file: assets/images/badges/dc27/deadpool-mini-badge-sao/305ab5af90.jpg
  source: https://www.tindie.com/products/s3gfault/deadpool-badge-sao/
  credit: TeamID64F (s3gfault)
  caption: DeadPool Badge SAO, LEDs lit up blue
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/s3gfault/deadpool-sao-with-attiny85-microcontroller/
  title: DEADPOOL Mini Badge / SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://www.tindie.com/products/s3gfault/team-id64f-deadpool-badge-sao/
  title: DeadPool Badge SAO from TeamID64F on Tindie
  accessed: '2026-09-07'
  note: Second Tindie listing for the same item (found via web search); confirmed maker (TeamID64F/s3gfault, Los Angeles), ATtiny85 + MCP23017, 16 blue 1206 LEDs, SAO v1.69bis, coin cell (CR2032 per this listing), 2019, retired/no longer sold.
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27
  accessed: '2026-09-07'
  note: Confirms DEF CON 27, describes it as a "mini badge" with CR2450 coin cell, MCP23017 driver over I2C commanded by ATtiny85, and states 200 were produced. Source of the two saved photos (front and rear).
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- kind: url
  url: https://www.tindie.com/products/s3gfault/deadpool-badge-sao/
  title: DeadPool Badge SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc27''.'
- kind: url
  url: https://www.tindie.com/stores/s3gfault/
  title: TeamID64F on Tindie
  accessed: '2026-09-07'
  note: Store page confirms the maker also sold sibling SAOs (Punisher, Pickle Rick, Red Stapler, Windows Logo) in the same series.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'The original Tindie listing (tindie.com/products/s3gfault/deadpool-sao-with-attiny85-microcontroller/) is blocked by Cloudflare bot-detection and could not be fetched directly; details instead confirmed via a second Tindie listing for the same product (team-id64f-deadpool-badge-sao) found by web search, plus the Hackaday DEF CON 27 badge roundup. The two sources disagree on the coin cell: Tindie lists CR2032, Hackaday says CR2450 - both are noted. Price and exact date within 2019 were not found in any reachable source. No hardware/firmware files were found, so open_source and related fields are left null. Merged with duplicate entry ''DeadPool Badge SAO'' (dc27-deadpool-badge-sao).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc27/deadpool-badge-sao/
---

The DEADPOOL Mini Badge / SAO is a Deadpool-themed "shitty add-on" made by s3gfault (Tindie/Twitter handle, part of TeamID64F, based in Los Angeles) for DEF CON 27 in 2019. It plugs into a host badge's SAO header (v1.69bis, 3.3V) and lights up 16 blue 1206 LEDs arranged to form the character's mask/logo, run by an ATtiny85 microcontroller that commands an MCP23017 constant-current LED driver over I2C. It runs from its own coin cell battery rather than drawing all its power from the host badge.

Hackaday's DEF CON 27 badge roundup reports that 200 units were produced. It was sold through s3gfault's Tindie store alongside other TeamID64F pop-culture SAOs from the same era (Punisher, Pickle Rick, Red Stapler, Windows Logo); both Tindie listings for it are no longer active, and no hardware or firmware files were found to be published for it.

## Notes merged from the duplicate entry "DeadPool Badge SAO"

The DeadPool Badge SAO is a Shitty Add-On made by TeamID64F (maker handle s3gfault, based in Los Angeles) and sold through their Tindie store. It is one of several pop-culture-themed SAOs the team released around the same time, alongside Punisher, Pickle Rick, Red Stapler, and Windows Logo versions, all built to the same basic pattern: an ATtiny85 microcontroller driving an MCP23017 I/O expander that lights 16 blue 1206 LEDs, powered by a CR2032 coin cell with an on/off switch, on a SAO v1.69bis (6-pin) connector.

The listing describes the board as able to "glow and be programmed to light up any of the leds," suggesting the LED pattern is firmware-controllable rather than fixed, though no source code or hardware files were published or linked from the store page. The product is now retired on Tindie with no price or quantity information retained; product photos are dated late July 2019, consistent with the badge's DEF CON 27 timeframe already recorded for this entry.

No design files, GitHub repo, or press coverage beyond the Tindie storefront were found for this specific SAO.
