---
title: HTP Graffiti
id: dc34-htp-graffiti
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: HogFillet
  url: https://uberflux.com/product/HTP-DC34
summary: An analog SAO shaped like a piece of graffiti art, with eight LEDs shining through cutouts in the artwork and driven by a 555-timer/ripple-counter circuit instead of a microcontroller.
functions: A 555 timer clocks a 10-bit ripple counter to flash eight LEDs through holes cut in the graffiti artwork; an onboard trimmer potentiometer adjusts the flash speed from a slow chase to a rapid strobe. A button shorts to the host badge's SAO header with effects that depend on (and may be unpredictable on) whatever badge it's plugged into.
look:
  colors: []
  shape: null
  themes:
  - art
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: Driven by a 555 timer clocking a 10-bit ripple counter, not a microcontroller.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $24
  price_usd: 24.0
  quantity: '31 made (21 sold, 10 remaining as of 2026-09-06)'
  availability: limited
  distribution:
  - purchase
  where: 'Sold via Uberflux (uberflux.com), listed for pre-ship pickup at DEF CON 34 per the badge.life schedule; mail shipping ($4.99) or refund offered to buyers who could not attend.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: uberflux.com/product/HTP-DC34
  url: https://uberflux.com/product/HTP-DC34
  kind: store
- label: youtu.be/ufYH1n0A5JY
  url: https://youtu.be/ufYH1n0A5JY
  kind: video
images:
  - file: assets/images/badges/dc34/htp-graffiti/36c8893632.jpg
    source: "https://uberflux.com/product/HTP-DC34"
    credit: "HogFillet"
    caption: "SAO HackThePlanet (HTP-DC34) product photo showing the graffiti artwork with LED cutouts"
  - file: assets/images/badges/dc34/htp-graffiti/35d8b4ea81.jpg
    source: "https://uberflux.com/product/HTP-DC34"
    credit: "HogFillet"
    caption: "SAO HackThePlanet (HTP-DC34) alternate product photo"
contact:
  discord: Hogfillet
  emails:
  - Dc34@fakebobby.com
  handles:
  - '@hogfillet'
notes: []
status: listed
sources:
- kind: sheet
  event: dc34
  row: 43
  updated: 7/18/2026 15:28:20
  listing: New
- kind: url
  url: https://uberflux.com/product/HTP-DC34
  title: "SAO HackThePlanet (HTP-DC34) - Uberflux"
  accessed: '2026-09-06'
  note: "Maker name, price, circuit description (555 timer + 10-bit ripple counter, 8 LEDs, trimmer pot), button behavior, quantity sold/remaining, distribution/shipping terms, and product photos."
- kind: url
  url: https://youtu.be/ufYH1n0A5JY
  title: "HTP SAO v2 DC34"
  accessed: '2026-09-06'
  note: "Video linked from the store page demoing the SAO; page title only, video content itself could not be retrieved via fetch."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'The community sheet listed the maker as "FakeBobby" but the storefront and video credit "HogFillet" (matching the entry''s own Discord/handle contact fields), so makers was corrected to HogFillet. Store listing is titled "SAO HackThePlanet"; kept the sheet''s "HTP Graffiti" title since it plainly refers to the same graffiti-themed HTP-DC34 item and no maker page uses a different name outright. Could not confirm MCU family beyond "none" (it is 555-timer based, not microcontroller-driven), SAO header version, open-source status, or design files -- the store page does not mention schematics or a repo. Could not view the YouTube video content directly (fetch only returned page chrome), so functional details rely on the store page alone.'
last_modified_date: '2026-09-06'
---

The HTP Graffiti (sold by maker HogFillet as "SAO HackThePlanet", model HTP-DC34) is a small analog SAO built around a piece of graffiti-style artwork with eight LEDs peeking out through cutouts in the design. Rather than a microcontroller, it runs on pure 555-timer logic: the timer clocks a 10-bit ripple counter that drives the LED pattern, and an onboard trimmer potentiometer lets the wearer dial the flash speed anywhere from a slow chase to a rapid strobe. A button on the board shorts to the host badge's SAO header, with effects that vary (and are described as unpredictable) depending on what badge it's plugged into.

It was sold through Uberflux for $24 ahead of DEF CON 34, with 31 units made; as of the September 2026 check, 21 had sold and 10 remained. The listing was set up for in-person pickup at the con via the badge.life schedule, with a $4.99 mail-shipping option or a refund for buyers who couldn't make it. No hardware files, firmware, or schematics are published alongside the listing.

