---
title: un1eet SAO
id: dc26-hashtag-un1eet-sao
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc26
year: 2018
makers:
- name: drydenmaker
summary: A no-frills, humorous SAO reading "ur #un1eet", made as a first PCB-design project for DEF CON 26.
functions: Exposes through-hole pads for a resistor and an LED on the back, letting the builder choose standard or reverse-mount LED placement; also breaks out I2C and SPI for further hacking.
look:
  colors:
  - black
  shape: rectangle
  themes:
  - meme
  - text
  - learn to solder
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: SMD LED pads support standard or reverse-mount installation; some units left unpopulated for the buyer to solder.
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: $5
  price_usd: 5
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold on Tindie by "|)3vice Makers |{its"; listing marked out of stock since 2019-07-28.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/drydenmaker/hashtag_un1eet_sao
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/drydenmaker/hashtag_un1eet_sao
  url: https://github.com/drydenmaker/hashtag_un1eet_sao
  kind: repo
- label: Tindie listing (un1eet SAO #badgelife addon)
  url: https://www.tindie.com/products/dMaker/un1eet-sao-badgelife-addon/
  kind: store
- label: "Hackaday.io: #un1eet Shitty Add On"
  url: https://hackaday.io/project/160043-un1eet-shitty-add-on
  kind: hackaday
- label: "Hackster.io: #badgelife for the #un1eet"
  url: https://www.hackster.io/drydenmaker/badgelife-for-the-un1eet-854186
  kind: article
images:
  - file: assets/images/badges/dc26/hashtag-un1eet-sao/cd3864cf3f.png
    source: "https://github.com/drydenmaker/hashtag_un1eet_sao"
    credit: "drydenmaker"
    caption: "un1eet SAO front, KiCad render"
  - file: assets/images/badges/dc26/hashtag-un1eet-sao/50233dbd13.png
    source: "https://github.com/drydenmaker/hashtag_un1eet_sao"
    credit: "drydenmaker"
    caption: "un1eet SAO back, KiCad render"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/drydenmaker/hashtag_un1eet_sao
  title: hashtag_un1eet_sao
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/drydenmaker/hashtag_un1eet_sao
  title: "GitHub: drydenmaker/hashtag_un1eet_sao README"
  accessed: '2026-09-07'
  note: "README text; confirms Tindie/OSHPark links, MIT-licensed KiCad files, and front/back render images."
- kind: url
  url: https://www.tindie.com/products/dMaker/un1eet-sao-badgelife-addon/
  title: un1eet SAO #badgelife addon from |)3vice Makers |{its
  accessed: '2026-09-07'
  note: "Confirms $5 price, LED backlighting, out-of-stock since 2019-07-28, seller name."
- kind: url
  url: https://hackaday.io/project/160043-un1eet-shitty-add-on
  title: "#un1eet Shitty Add On"
  accessed: '2026-09-07'
  note: "Confirms DEF CON as the intended event, project logged 2018-07-28 (DEF CON 26), maker's first custom PCB, SMD LED/resistor pads with I2C/SPI breakout, made as a soldering-practice teaching piece."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: "Event and year inferred from the Hackaday.io project log date (2018-07-28) and the maker's own statement that it was made for DEF CON, which lines up with DEF CON 26 (Aug 2018); no source names the specific year explicitly, so confidence is medium rather than high. LED count and exact quantity made are not stated anywhere found; left as best-available estimate (1 LED position) per the README/Hackaday description of a single SMD LED pad set. Maker identity: the GitHub/Hackaday/Hackster handle is 'drydenmaker', while the Tindie seller name is styled '|)3vice Makers |{its' ('device Makers kits') - likely the same person's storefront brand, not verified as a separate collaborator."
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/hashtag-un1eet-sao/
---

The un1eet SAO is a small, unpowered add-on board for the SAO (Shitty Add-On) badge header, reading "ur #un1eet" across its face. Maker drydenmaker built it as their first custom PCB design, using it as a hands-on introduction to KiCad and surface-mount soldering ahead of DEF CON 26 in 2018. Rather than a polished gadget, it was explicitly framed as a teaching piece for the #badgelife community: the back of the board exposes through-hole pads for a resistor and an LED, letting a builder choose a standard or reverse-mount LED placement, plus breakouts for I2C and SPI for anyone who wants to extend it further.

The board was sold on Tindie for $5 through the seller storefront "|)3vice Makers |{its," alongside stickers and other small designs; that listing has shown as out of stock since July 2019. The hardware is open source under the MIT license, with KiCad source files published on GitHub, and OSHPark share links included in the README for anyone who wants to order their own boards (a non-LED variant is linked directly; other order options point to a Tindie storefront and sticker shop).
