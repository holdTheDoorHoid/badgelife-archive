---
title: Fifth Element Stones Badge (DEF CON 27)
id: dc27-fifth-element-stones-badge-def-con-27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: GoonBoxBadge team
  url: https://mkfactor.com/
summary: A base badge with four detachable "element stone" SAOs, inspired by The Fifth Element, that spring open and light up when placed in their correct spots.
functions: 'Each of the four element stones opens via a spring-loaded mechanism when placed on the base. Correctly placing all four stones in their matching positions lights a center LED for the "5th Element." A blinky mode cycles through all the LEDs. The stones are also standard SAOs and can be plugged into other badges'' SAO headers.'
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - movie
  - puzzle
tech:
  mcu: ATtiny84
  leds: null
  display: null
  connectivity: []
  battery: 2x AA
  sao_version: v1
get_one:
  price: $100 assembled / $60 kit
  price_usd: 100
  quantity: '200'
  availability: sold_out
  distribution:
  - purchase
  - kit
  where: Pre-sold directly by MKFactor/GoonBoxBadge ahead of DEF CON 27 (2019), with local pickup at 801 Labs in Salt Lake City; later listed and sold out on Tindie (last stock gone by August 2020).
make_your_own:
  open_source: yes
  hardware_url: https://github.com/compukidmike/dc27
  firmware_url: https://github.com/compukidmike/dc27
  eda_tool: null
links:
- label: www.tindie.com/products/compukidmike/fifth-element-stones-badge-from-defcon-27
  url: https://www.tindie.com/products/compukidmike/fifth-element-stones-badge-from-defcon-27/
  kind: store
- label: mkfactor.com - Goon Box Badge Defcon 27 Presale
  url: https://mkfactor.com/?p=67
  kind: article
- label: github.com/compukidmike/dc27
  url: https://github.com/compukidmike/dc27
  kind: repo
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
images:
- file: assets/images/badges/dc27/fifth-element-stones-badge-def-con-27/8e56933de9.jpg
  source: "https://www.tindie.com/products/compukidmike/fifth-element-stones-badge-from-defcon-27/"
  credit: "MKFactor / CompuKidMike"
  caption: "The assembled Fifth Element Stones badge with element stones"
- file: assets/images/badges/dc27/fifth-element-stones-badge-def-con-27/6d925b65cb.jpg
  source: "https://mkfactor.com/?p=67"
  credit: "MKFactor"
  caption: "The Fifth Element base badge with all four stones in place"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/compukidmike/fifth-element-stones-badge-from-defcon-27/
  title: Fifth Element Stones Badge (DEF CON 27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://mkfactor.com/?p=67
  title: Goon Box Badge Defcon 27 Presale
  accessed: '2026-09-07'
  note: Maker's own presale post; confirms pricing ($100 assembled / $60 kit), features, and includes maker photos.
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: 'Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  accessed: '2026-09-07'
  note: Confirms ATtiny84 MCU, resistive-divider stone detection, and a hand-assembled run of 200 by the two-person GoonBoxBadge team.
- kind: url
  url: https://github.com/compukidmike/dc27
  title: 'GitHub - compukidmike/dc27: DEFCON 27 Projects'
  accessed: '2026-09-07'
  note: Confirms this is the design-files repo for the DEF CON 27 badges (including the Fifth Element badge) and that kit assembly instructions are included; page excerpt did not surface further README detail.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'LED count/type and exact quantities of stone circuit boards (11 per stone) were not independently confirmed with a spec sheet; the badge platform itself is largely passive (an ATtiny84 base with resistive-divider stone detection), and no display or wireless connectivity is present. Storefront (Tindie) shows the badge as an "out of stock" leftover of the original 200-unit run rather than a separate release.'
last_modified_date: '2026-09-07'
---

The Fifth Element Stones Badge was made for DEF CON 27 (2019) by the two-person GoonBoxBadge team (MKFactor / CompuKidMike, based in Riverton, Utah), riding the same year's wave of independent SAO-heavy badges. It reimagines the glowing "element stones" from the 1997 film *The Fifth Element* as a base badge with four separate stone add-ons: each stone is built from 11 small circuit boards that let it spring open when set into its matching slot on the base, and each stone quotes the movie character who originally "opened" that element. An ATtiny84 on the base badge reads a resistive divider for each slot to sense which stone has been placed and where; getting all four stones into their correct spots lights up a white "5th Element" LED at the center, and a separate blinky mode cycles all the LEDs. Each stone also doubles as a standalone SAO that plugs into any badge with a compatible SAO header.

The team hand-assembled a run of 200 sets over several months and pre-sold them ahead of DEF CON 27 at $100 fully assembled (with the four stones, base, and lanyard) or $60 as a solder-it-yourself kit with a pre-assembled base, shipping in a custom box styled after the film's element-stone case; local pickup was offered at 801 Labs in Salt Lake City. Leftover units were later listed on Tindie for $80, going fully out of stock by August 2020. Design files and kit-assembly instructions for the badge are published on GitHub under compukidmike/dc27.
