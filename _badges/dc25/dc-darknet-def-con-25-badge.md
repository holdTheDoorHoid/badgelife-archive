---
title: DC Darknet DEF CON 25 badge
id: dc25-dc-darknet-def-con-25-badge
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: Krux
  url: https://oshpark.com/profiles/Krux
summary: A rotary-phone-shaped badge for the DC Darknet contest at DEF CON 25, sold as an unassembled solder-it-yourself kit.
functions: 'Serves as the key/communicator for the DarkNet (DCDN) contest, themed on Daniel Suarez''s Daemon/Freedom novels: players build reputation by solving ciphers, exploits, and other quests. The badge itself has four capacitive-touch sensors on the dial numbers, with LEDs behind the copper illuminating numerals and letters.'
look:
  colors: []
  shape: rotary phone
  themes:
  - cyberpunk
  - security
  - ctf
tech:
  mcu: STM32
  leds: null
  display: null
  connectivity: []
  battery: LiPo
  sao_version: null
get_one:
  price: $25
  price_usd: 25
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - contest
  where: Sold at DEF CON 25 (2017) as an unassembled kit; solvers of the DarkNet casefile got a two-hour early-purchase window before it went on sale to the general conference and sold out.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/thedarknet/defcon25-badge
  firmware_url: https://github.com/thedarknet/defcon25-badge
  eda_tool: null
links:
- label: github.com/thedarknet/defcon25-badge
  url: https://github.com/thedarknet/defcon25-badge
  kind: repo
- label: dcdark.net 2017 badge assembly page
  url: http://dcdark.net/2017/badge/index.html
  kind: doc
- label: 'Hackaday: All The Hardware Badges Of DEF CON 25'
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  kind: article
images:
- file: assets/images/badges/dc25/dc-darknet-def-con-25-badge/c029fc2193.jpg
  source: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  credit: Krux / Hackaday
  caption: Front of the DC Darknet DEF CON 25 badge, resembling a rotary phone
- file: assets/images/badges/dc25/dc-darknet-def-con-25-badge/6436d93fe1.jpg
  source: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  credit: Krux / Hackaday
  caption: Back of the DC Darknet badge showing LEDs and LiPo battery connection
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/thedarknet/defcon25-badge
  title: DC Darknet DEF CON 25 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc25''.'
- kind: url
  url: http://dcdark.net/2017/badge/index.html
  title: DC Darknet 2017 badge assembly page
  accessed: '2026-09-07'
  note: Referenced from the GitHub repo README as the assembly-instructions page; the site's TLS cert did not match its hostname so the page could not be fetched directly, only cited.
- kind: url
  url: https://hackaday.com/2017/08/04/all-the-hardware-badges-of-def-con-25/
  title: All The Hardware Badges Of DEF CON 25
  accessed: '2026-09-07'
  note: Confirmed designer (Krux), rotary-phone form factor, capacitive touch sensors, kit assembly (SMD LEDs, screen connector, LiPo), early-access sale mechanic, and supplied front/back photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own assembly page (dcdark.net) could not be fetched due to a TLS hostname mismatch on that server, so most detail comes from the GitHub repo (STM32-based, MIT-licensed hardware/software/firmware repo) and Hackaday's DEF CON 25 badge roundup. LED count/type, display, and exact quantity made are not stated anywhere found; price of $25 and the sold-out status come from web search snippets (Worthpoint listings, secondary) rather than a primary storefront, so confidence is medium rather than high. The DarkNet badge series continued in later years (DC30-DC34 per the archive's existing titles) as a recurring "Darknet" line, but this dc25 entry covers only the 2017 badge.
last_modified_date: '2026-09-11'
model:
  file: assets/models/dc25/dc-darknet-def-con-25-badge.glb
  method: kicad
  source_file: dc25-darknet-dialer-eaglev8.2.brd
  generated: '2026-09-11'
  bytes: 281052
---

The DC Darknet badge was the key artifact for DEF CON 25's DarkNet contest, one of the con's most popular puzzle tracks, themed on Daniel Suarez's novels *Daemon* and *Freedom*. Players ("agents") built reputation by solving ciphers, exploits, and other challenges, and the badge itself doubled as a prop and communicator for that story. Designed by Krux, it takes the shape of an old rotary telephone dial, with four capacitive-touch sensors standing in for the dial's numbers and LEDs mounted on the back shining forward through cutouts in the copper to light up numerals and letters.

It shipped as an unassembled solder-it-yourself kit built around an STM32 microcontroller, requiring buyers to place surface-mount LEDs, attach a connector for a small screen, and wire up a LiPo battery on the back — a deliberate learn-to-solder element alongside the puzzle. Access was staged: anyone who had already solved the DarkNet casefile got a two-hour early-purchase window before the badge went on sale to the wider conference, and it sold out from there. Hardware, software, and STM32Cube firmware sources are published on GitHub under an MIT license, though the assembly walkthrough itself lives on the maker's own dcdark.net site rather than in the repo.

## Make your own

Hardware, firmware, and STM32Cube framework files are in the [defcon25-badge GitHub repo](https://github.com/thedarknet/defcon25-badge) (MIT-licensed). The original assembly instructions are linked from that repo's README at dcdark.net/2017/badge/index.html.
