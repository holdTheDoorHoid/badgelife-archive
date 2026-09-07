---
title: DEF CON 29 SAO with 58 kHz Security Tag
id: dc29-dc29-makeithackin-58khz-security-tag-sao
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc29
year: 2021
makers:
- name: MakeItHackin
  url: https://github.com/MakeItHackin
summary: 'Free companion SAO to MakeItHackin''s DEF CON 29 "Security Tag" badge, made for fans who did not get one of the 25 hand-numbered badges: a small board with a 2x3 SAO header, 4 NeoPixels and an LED, with a real 58 kHz Sensormatic security tag applied to it so it sets off retail anti-theft alarms.'
functions: 'Passive novelty add-on: drives 4 NeoPixels and an LED off the host badge''s SAO power/data lines. The applied 58 kHz Sensormatic tag will trip a store''s security gates, same as the badge.'
look:
  colors: []
  shape: null
  themes:
  - security
  - retail
tech:
  mcu: none
  leds:
    count: 4
    type: NeoPixel
    note: plus one additional LED, per the maker's DEF CON forum post; driven by the host badge, no onboard MCU
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v2
get_one:
  price: 'free'
  price_usd: 0
  quantity: 'unstated (badge run was 25; SAO quantity not given)'
  availability: sold_out
  distribution:
  - free_drop
  where: Handed out at DEF CON 29 (2021) to fans who followed the maker's TikTok/security-tag content but did not receive one of the 25 numbered badges; announced on the DEF CON forums.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/MakeItHackin/DEFCON29Badge/tree/main/PCBFiles
  firmware_url: null
  eda_tool: Eagle
notes: []
links:
- label: github.com/MakeItHackin/DEFCON29Badge
  url: https://github.com/MakeItHackin/DEFCON29Badge
  kind: repo
- label: github.com/MakeItHackin/DEFCON29Badge/tree/main/PCBFiles
  url: https://github.com/MakeItHackin/DEFCON29Badge/tree/main/PCBFiles
  kind: repo
- label: 'DEF CON Forums: "The MakeItHackin Security Tag Badge and SAO"'
  url: https://forum.defcon.org/node/238085
  kind: article
- label: 'Tindie: MakeItHackin DEF CON 29 Electronic Badge (sibling badge listing)'
  url: https://www.tindie.com/products/makeithackin/makeithackin-def-con-29-electronic-badge/
  kind: store
images:
  - file: assets/images/badges/dc29/dc29-makeithackin-58khz-security-tag-sao/39e613ed34.jpg
    source: "https://github.com/MakeItHackin/DEFCON29Badge"
    credit: "MakeItHackin"
    caption: "The DEF CON 29 SAO with 58 kHz Sensormatic security tag footprint"
contact: {}
status: released
sources:
- kind: url
  url: https://github.com/MakeItHackin/DEFCON29Badge
  title: DC 29 Badge and SAO (MakeItHackin/DEFCON29Badge)
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://forum.defcon.org/node/238085
  title: The MakeItHackin Security Tag Badge and SAO - DEF CON Forums
  accessed: '2026-09-07'
  note: Maker's own July 2021 announcement post; confirms 25-badge run, free SAO given to fans who missed the badge, SAO features (4 NeoPixels + LED), and both security tags.
- kind: url
  url: https://raw.githubusercontent.com/MakeItHackin/DEFCON29Badge/main/README.md
  title: DEFCON29Badge README
  accessed: '2026-09-07'
  note: Confirms ATTiny85/OLED/NeoPixel badge, Checkpoint 8.2MHz and Sensormatic 58kHz security tags, credit-card badge shape.
- kind: url
  url: https://github.com/MakeItHackin/DEFCON29Badge/tree/main/PCBFiles
  title: PCBFiles directory listing
  accessed: '2026-09-07'
  note: Confirms Eagle .sch/.brd files for SAO_3 and a dated archive SAO_3v2_2021-07-21.zip; no separate Gerber files found.
- kind: url
  url: https://www.tindie.com/products/makeithackin/makeithackin-def-con-29-electronic-badge/
  title: MakeItHackin DEF CON 29 Electronic Badge - Tindie
  accessed: '2026-09-07'
  note: Sibling storefront listing for the assembled badge/kit (not the SAO specifically); used only to confirm the badge's product photo/branding.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    Core facts (maker's own words) confirmed via the maker's July 14, 2021 DEF CON
    forum post announcing the project: 25 badges made and handed to fans at DEF CON
    29, with SAOs (also carrying a security tag) made as a free alternative for fans
    who didn't get a badge. The GitHub repo (README and PCBFiles/ReadMe.md) confirms
    the badge/SAO pairing, the two security tags (Checkpoint 8.2 MHz on the badge,
    Sensormatic 58 kHz — this SAO's tag), and that Eagle schematic/board files plus
    dated zips (SAO_3v2_2021-07-21.zip) are published, though no separate Gerber
    (.gbr) files were found, only Eagle source. Exact SAO quantity, firmware (the
    SAO appears passive, driven by the badge), and whether it was ever sold
    separately (vs. only given away) were not stated anywhere found. The Tindie
    listing found is for the full assembled badge/kit, not the SAO alone.
last_modified_date: '2026-09-07'
---

MakeItHackin's DEF CON 29 project paired a credit-card-shaped badge with a matching SAO, both carrying real retail anti-theft security tags — a nod to the maker's TikTok content about security tags. The badge got a Checkpoint 8.2 MHz tag and a Sensormatic 58 kHz tag; this SAO carries the 58 kHz Sensormatic tag on its own small board, alongside a 2x3 SAO header, four NeoPixels, and an LED, all powered from the host badge.

Per the maker's own July 2021 DEF CON forum post, this was their first badge design: 25 badges were hand-made and given to fans encountered at the con, and the SAO was created as a free consolation piece for fans who didn't land one of the 25 badges — "LIMITED EDITION... lol," in the maker's words. Both the badge and SAO Eagle design files (schematic and board, with a dated `SAO_3v2_2021-07-21.zip`) are published on GitHub, though no separately exported Gerber files were found in the repo, only the Eagle CAD source.

## Make your own

The repo's `PCBFiles/` directory holds Eagle `.sch`/`.brd` files for `SAO_3` plus a dated archive (`SAO_3v2_2021-07-21.zip`); load these in Eagle (or a compatible EDA tool) to regenerate manufacturing files. No firmware is published, consistent with the SAO having no onboard microcontroller — the NeoPixels/LED are driven by the host badge over the SAO header.
