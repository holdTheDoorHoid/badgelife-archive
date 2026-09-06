---
title: Tipsy Badge
id: dc33-tipsy-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: seeess
  url: https://github.com/seeess
summary: 'A bottle-shaped DEF CON 33 electronic badge that uses galvanic vestibular stimulation: conductive pads held behind the wearer''s ears by a headband carry a few milliamps that shift the sense of balance left or right, or make the wearer wobble. Sold at the Hacker Warehouse booth for $100, with half the profits going to the Tor Project.'
functions: 'Calibration mode (checks that at least 0.12 mA is flowing through the pads); Steering mode to push the wearer''s balance left or right; Wobble mode that pushes back and forth quickly; a Stroop-effect color game that zaps you on right or wrong answers to test positive versus negative reinforcement; Bling mode that shows pictures, with custom 128x160 .tga images loaded over USB mass storage; a waterfall graph of pad voltage and current; a low-battery warning. Zapping only happens while the in-line ZAP button is held, and is blocked while USB is plugged in. ~5 mA hardware current limit with 2, 3 and 4 mA software targets.'
look:
  colors:
  - black
  - yellow
  shape: bottle
  themes:
  - drink
  - text
  form_factor: pcb badge
tech:
  mcu: RP2040
  leds:
    count: null
    type: null
    note: Rear-mounted LEDs per the maker's forum post; count and type not stated.
  display: '1.77" 160x128 RGB565 color TFT'
  connectivity:
  - usb
  inputs:
  - buttons
  power: 2x AAA or USB-C (zap modes are meant to run on batteries only)
  battery: 2x AAA
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: '$100'
  price_usd: 100.0
  quantity: ''
  availability: sold_out
  availability_note: 'hackerwarehouse.com listing (read 2026-09-06) shows the badge marked down from $100 to $75 and Out of stock; SKU SS-TB.'
  distribution:
  - purchase
  where: In person at the Hacker Warehouse booth in the DEF CON 33 vendor area (the maker posted on X on 8 Aug 2025 that it was going on sale the next day); later listed on hackerwarehouse.com.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/seeess/Defcon-Tipsy-33-Badge/tree/main/tipsy
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: CC BY-NC 4.0
  fab_url: null
  notes: The repo has the Arduino sketch (tipsy.ino), a prebuilt UF2, the data partition contents (sample .tga pictures), STLs for the headband triglide and a "wings" part, and Arduino IDE flashing instructions. No schematic, PCB design files, Gerbers or BOM are published as of 2026-09-06.
links:
- label: github.com/seeess
  url: https://github.com/seeess
  kind: repo
- label: Defcon-Tipsy-33-Badge repo (README, firmware, STLs)
  url: https://github.com/seeess/Defcon-Tipsy-33-Badge
  kind: repo
- label: Tipsy Electronic Badge thread on the DEF CON forums
  url: https://forum.defcon.org/node/253193
  kind: social
- label: Hacker Warehouse listing
  url: https://hackerwarehouse.com/product/tipsy-badge/
  kind: store
- label: seeess on X, sale announcement
  url: https://x.com/see_ess/status/1953718808105169371
  kind: social
- label: Defcon Tipsy Electronic Badge Overview (maker's video)
  url: https://www.youtube.com/watch?v=kScSm-BZAsY
  kind: video
- label: DEF CON 33 Video Team - TipsyBadge
  url: https://www.youtube.com/watch?v=hKLow2hkLxQ
  kind: video
- label: Electronic Tipsy Badge at DEF CON (Deviant Ollam)
  url: https://www.youtube.com/watch?v=lD6AmXMeXt0
  kind: video
images:
- file: assets/images/badges/dc33/tipsy-badge/readme-front.png
  source: https://github.com/seeess/Defcon-Tipsy-33-Badge
  credit: seeess
  caption: 'Front of the badge from the project README: bottle-shaped black PCB with yellow edge, yellow ZAP!! button, A/B buttons, 1.77" TFT, four-button d-pad and SAO header.'
- file: assets/images/badges/dc33/tipsy-badge/hw-headon.jpg
  source: https://hackerwarehouse.com/product/tipsy-badge/
  credit: Hacker Warehouse
  caption: Head-on product photo of the front, with the "Volt 4.5" silkscreen and the striped bottle-cap at the neck.
- file: assets/images/badges/dc33/tipsy-badge/hw-1490.jpg
  source: https://hackerwarehouse.com/product/tipsy-badge/
  credit: Hacker Warehouse
  caption: Back of the badge showing the 2x AAA holder, USB-C port and the 3.5mm electrode jack at the neck.
contact:
  emails:
  - seeess@riseup.net
notes:
- Will be sold at the hacker warehouse vendor booth
- 'The community sheet listed the maker as "seeess + <redacted> / seeess + g"; the second person is not named in any public source read. The README speaks of "we" and "the creators".'
- The PCB silkscreen reads "Volt 4.5" and the repo is described as "Defcon Tipsy Badge / Volt 4.5 ma"; the maker calls it the Tipsy Badge / Tipsy Electronic Badge.
status: released
sources:
- kind: sheet
  event: dc33
  row: 4
  updated: 6/1/2025 1:33:06
- kind: url
  url: https://github.com/seeess
  title: seeess - GitHub profile
  accessed: '2026-09-06'
  note: Pinned Defcon-Tipsy-33-Badge repo; profile links to twitter.com/see_ess; other DEF CON badge repos by the same maker.
- kind: url
  url: https://github.com/seeess/Defcon-Tipsy-33-Badge
  title: 'GitHub - seeess/Defcon-Tipsy-33-Badge: Defcon Tipsy Badge / Volt 4.5 ma'
  accessed: '2026-09-06'
  note: README supported the modes, hardware specs (RP2040, 2 MB flash, 2x AAA, one 1.69bis SAO port, USB-C, 1.77" 160x128 TFT), safety limits, included items, Tor donation, custom-photo and flashing steps; file tree and CC BY-NC 4.0 LICENSE; repo created 2025-07-18.
- kind: url
  url: https://forum.defcon.org/node/253193
  title: Tipsy Electronic Badge - DEF CON Forums
  accessed: '2026-09-06'
  note: Maker's post of 23 July 2025 (user seeess) in #Badge Life / Buying and Selling; $100 price, Hacker Warehouse booth, rear-mounted LEDs, Arduino compatible, open source, code to be released during DEF CON, half of profits to Tor. No replies.
- kind: url
  url: https://hackerwarehouse.com/product/tipsy-badge/
  title: Tipsy Badge - Hacker Warehouse
  accessed: '2026-09-06'
  note: 'Product listing: $100 marked down to $75, Out of stock, SKU SS-TB, RP2040, color TFT, 1x SAO 1.69bis port, 2 MB flash with USB mass storage, open source; source of two product photos. Read via WebFetch; direct curl was blocked by Cloudflare.'
- kind: url
  url: https://x.com/see_ess/status/1953718808105169371
  title: seeess on X, 8 Aug 2025 - Defcon Tipsy Badge is going on sale tomorrow
  accessed: '2026-09-06'
  note: Sale timing; quotes the 23 July 2025 post announcing $100 at the Hacker Warehouse booth with half of profits to the Tor Project. Read through the X syndication endpoint.
- kind: url
  url: https://www.youtube.com/watch?v=kScSm-BZAsY
  title: Defcon Tipsy Electronic Badge Overview (YouTube, channel 533ess)
  accessed: '2026-09-06'
  note: Maker's overview video linked from the README and forum post; title and channel confirmed via YouTube oEmbed only, video not watched.
- kind: url
  url: https://www.youtube.com/watch?v=hKLow2hkLxQ
  title: DEF CON 33 Video Team - TipsyBadge (YouTube, DEFCONConference)
  accessed: '2026-09-06'
  note: Published 2025-09-09; description says the badge can set your gait to wobble mode using Galvanic Vestibular Stimulation. Video not watched.
- kind: url
  url: https://www.youtube.com/watch?v=lD6AmXMeXt0
  title: Electronic Tipsy Badge at DEF CON (YouTube, DeviantOllam)
  accessed: '2026-09-06'
  note: Third-party video about the badge; title and channel confirmed via YouTube oEmbed only, video not watched.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core facts confirmed from the maker''s own README, forum post and X posts. Not found: number made, LED count/type, the second collaborator''s name (redacted on the sheet), and any schematic/PCB files (the repo has firmware and STLs only, so open_source is partial even though the maker describes it as open source). Price is $100 from the maker; Hacker Warehouse later showed it marked down to $75 and out of stock. Videos were identified by title only, not watched. No Hackaday.io, Tindie, PCBWay/OSH Park or press coverage turned up in searches.'
last_modified_date: '2026-09-06'
---

The Tipsy Badge is seeess's DEF CON 33 badge, a follow-on to the Tor badges the same maker sold at DEF CON 31 and 32. It is shaped like a bottle, with a striped cap at the neck and "Volt 4.5" in large script down the front, and the joke is in the name: it makes you tipsy. A headband holds two conductive pads behind your ears, a 3.5 mm lead plugs into the neck of the bottle, and while you hold the yellow ZAP!! button the badge drives a small current (a hardware limit of about 5 mA, with 2, 3 and 4 mA software targets) across your vestibular system. Steering mode pushes your balance left or right so you can "drive" yourself around; wobble mode rocks you back and forth. There is also a Stroop-effect color game that zaps you on right or wrong answers so you can find out whether reward or punishment improves your score.

Under the hood it is an RP2040 with 2 MB of flash, a 1.77" 160x128 color TFT, rear-mounted LEDs, a four-way d-pad plus A and B buttons, a single 1.69bis SAO header, USB-C and two AAA cells. Half of the flash is exposed as a USB mass-storage drive holding pictures for the bling mode; you can add your own as 128x160 RLE-compressed TGA files. The maker built in several safeguards: the zap button sits in line with the pad power, zapping is disabled when USB is connected, and the README opens with a long disclaimer (adults only, sit down the first time, stay away from stairs). Electrodes, headband, lube, a lanyard, spare batteries and a battery clip came in the box.

It was announced on the DEF CON forums on 23 July 2025 and sold for $100 at the Hacker Warehouse booth in the DEF CON 33 vendor area, with half of the profits donated to the Tor Project; the maker says they fronted all development costs and charge nothing for their time. Hacker Warehouse later listed it online at $75, out of stock. The DEF CON Video Team and Deviant Ollam both posted short videos of people trying it on the con floor.

## Make your own

The PCB design has not been published, so you cannot fabricate the board, but everything needed to reflash or modify a badge you own is in the repo (CC BY-NC 4.0): install the Arduino IDE and the earlephilhower arduino-pico core, add the Adafruit GFX and ST7735/ST7789 libraries, select the Raspberry Pi Pico board, set the flash size to 2 MB (1 MB sketch / 1 MB FS), then compile and flash tipsy/tipsy.ino; a prebuilt UF2 and the contents of the data partition are also included. The repo carries STLs for the headband triglide (modified from a Printables model) and a "wings" part.
