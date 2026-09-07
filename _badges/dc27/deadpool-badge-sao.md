---
title: DeadPool Badge SAO
id: dc27-deadpool-badge-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: TeamID64F (s3gfault)
  url: https://www.tindie.com/stores/s3gfault/
summary: A Deadpool-themed SAO with 16 blue LEDs driven by an MCP23017 expander and an ATtiny85, part of a small superhero/pop-culture SAO line by TeamID64F.
functions: 'Glows blue; the maker''s listing says it "can be programmed to light up any of the leds" via the onboard MCP23017 LED driver.'
look:
  colors:
  - black
  shape: null
  themes:
  - pop culture
  - movie
tech:
  mcu: ATtiny85
  leds:
    count: 16
    type: discrete
    note: 16x blue 1206 LEDs driven through an MCP23017 I/O expander/LED driver
  display: none
  connectivity:
  - i2c
  battery: CR2032
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing shows retired/no longer available, checked 2026-09-07.'
  distribution:
  - purchase
  where: Sold via the maker's Tindie store (TeamID64F / s3gfault), now retired.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/s3gfault/deadpool-badge-sao
  url: https://www.tindie.com/products/s3gfault/deadpool-badge-sao/
  kind: store
- label: www.tindie.com/stores/s3gfault
  url: https://www.tindie.com/stores/s3gfault/
  kind: store
images:
  - file: assets/images/badges/dc27/deadpool-badge-sao/11fe14b79a.jpg
    source: "https://www.tindie.com/products/s3gfault/deadpool-badge-sao/"
    credit: "TeamID64F (s3gfault)"
    caption: "DeadPool Badge SAO, LEDs off"
  - file: assets/images/badges/dc27/deadpool-badge-sao/305ab5af90.jpg
    source: "https://www.tindie.com/products/s3gfault/deadpool-badge-sao/"
    credit: "TeamID64F (s3gfault)"
    caption: "DeadPool Badge SAO, LEDs lit up blue"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/s3gfault/deadpool-badge-sao/
  title: DeadPool Badge SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc27''.'
- kind: url
  url: https://www.tindie.com/products/s3gfault/team-id64f-deadpool-badge-sao/
  title: DeadPool Badge SAO (alternate Tindie listing URL)
  accessed: '2026-09-07'
  note: Same listing content mirrored under a second slug; used to double-check description and part list.
- kind: url
  url: https://www.tindie.com/stores/s3gfault/
  title: TeamID64F on Tindie
  accessed: '2026-09-07'
  note: Store page confirms the maker also sold sibling SAOs (Punisher, Pickle Rick, Red Stapler, Windows Logo) in the same series.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The Tindie listing itself does not name a specific event, only "Shitty Add-on capable
    Badges" at 3.3V/SAO v1.69bis. Kept event as dc27/year 2019 from the existing entry,
    supported by the product photo timestamps (July 2019, i.e. just before DEF CON 27) and
    the maker's other same-series SAOs (Punisher, Pickle Rick, Red Stapler, Windows Logo)
    being sold as DC27-era badgelife. No price, quantity made, or design files were found;
    the listing is retired with no archived price shown. Second product photo is only
    available from Tindie at a small 114x76 thumbnail size.
last_modified_date: '2026-09-07'
---

The DeadPool Badge SAO is a Shitty Add-On made by TeamID64F (maker handle s3gfault, based in Los Angeles) and sold through their Tindie store. It is one of several pop-culture-themed SAOs the team released around the same time, alongside Punisher, Pickle Rick, Red Stapler, and Windows Logo versions, all built to the same basic pattern: an ATtiny85 microcontroller driving an MCP23017 I/O expander that lights 16 blue 1206 LEDs, powered by a CR2032 coin cell with an on/off switch, on a SAO v1.69bis (6-pin) connector.

The listing describes the board as able to "glow and be programmed to light up any of the leds," suggesting the LED pattern is firmware-controllable rather than fixed, though no source code or hardware files were published or linked from the store page. The product is now retired on Tindie with no price or quantity information retained; product photos are dated late July 2019, consistent with the badge's DEF CON 27 timeframe already recorded for this entry.

No design files, GitHub repo, or press coverage beyond the Tindie storefront were found for this specific SAO.
