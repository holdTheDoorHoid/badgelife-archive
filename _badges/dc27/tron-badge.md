---
title: Tron Badge
id: dc27-tron-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Sodium_Hydrogen (@sodium_hydrogen)
  url: https://hackaday.io/project/164774-def-con-27-tron-badge
summary: An independent DEF CON 27 badge themed after a Recognizer from Tron, built around a full Bus Pirate implementation for hacking other badges' hardware.
functions: Implements a Bus Pirate v3.6 (a debugging/protocol-analysis tool), operable from a terminal app on an Android phone; drives an 8x12 white LED matrix for scrolling text plus 16 RGB LEDs for animated lighting; pairs with a separate "identity disk" SAO that stores the wearer's information and doubles as a hands-on teaching tool for listening to and injecting data on an I2C bus.
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - movie
  - security
  - hardware tool
tech:
  mcu: ATmega328
  leds:
    count: null
    type: null
    note: 8x12 white LED matrix for scrolling messages, plus 16 RGB LEDs for animation patterns
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - crowdfunding
  where: Funded via a Kickstarter campaign ahead of DEF CON 27; no storefront or current availability found.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Sodium-Hydrogen/TRON-Badge
  firmware_url: https://github.com/Sodium-Hydrogen/TRON-Badge
  eda_tool: null
links:
- label: hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
- label: hackaday.io/project/164774-def-con-27-tron-badge
  url: https://hackaday.io/project/164774-def-con-27-tron-badge
  kind: hackaday
- label: github.com/Sodium-Hydrogen/TRON-Badge
  url: https://github.com/Sodium-Hydrogen/TRON-Badge
  kind: repo
- label: hackster.io - The DEF CON TRON Indie Badge Is Designed to Hack Other Badges
  url: https://www.hackster.io/news/the-def-con-tron-indie-badge-is-designed-to-hack-other-badges-4afecd4ca066
  kind: article
images:
- file: assets/images/badges/dc27/tron-badge/20d3e71a4c.jpg
  source: https://hackaday.io/project/164774-def-con-27-tron-badge
  credit: Sodium_Hydrogen
  caption: Assembled TRON badge with LED matrix and identity disk SAO
- file: assets/images/badges/dc27/tron-badge/93153fdb13.jpg
  source: https://hackaday.io/project/164774-def-con-27-tron-badge
  credit: Sodium_Hydrogen
  caption: TRON badge PCB render
- file: assets/images/badges/dc27/tron-badge/beb9df8e53.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday
  caption: Front of the Sodium_Hydrogen Tron/Recognizer-themed DEF CON 27 badge
- file: assets/images/badges/dc27/tron-badge/8588cc610f.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday
  caption: Identity disk add-on accessory for the Tron/Recognizer badge
contact: {}
notes:
- Independent DC27 badge whose production was delayed past the conference, per Hackaday's DC27 roundup. Found by the event-year sweep, task dc27-indie.
- This entry duplicates dc27-tron-badge-recognizer (same maker, same badge, same core Hackaday source, found by a different sweep pass under task dc27-saos). The sheet listed this one simply as "Tron Badge"; the maker's own Hackaday.io project is titled "DEF CON 27 TRON Badge."
- Tron-Recognizer-themed unofficial badge shown in Hackaday's DEF CON 27 badge roundup. Found by the event-year sweep, task dc27-saos.
- This entry duplicates dc27-tron-badge (same maker, same badge, same source article, found by a different sweep pass under task dc27-indie).
status: listed
sources:
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Tron Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-indie); event read as ''dc27''.'
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide to the Unofficial Electronic Badges of DEF CON 27
  accessed: '2026-09-08'
  note: Confirmed maker (Sodium_Hydrogen), Tron/Recognizer theme, Bus Pirate implementation, ATmega328 MCU, LED matrix + RGB LEDs, identity disk accessory, and that production was delayed past the con by an incorrect-parts problem.
- kind: url
  url: https://hackaday.io/project/164774-def-con-27-tron-badge
  title: DEF CON 27 TRON Badge - Hackaday.io
  accessed: '2026-09-08'
  note: 'Maker''s own project page: confirms Bus Pirate v3.6 integration, identity disk SAO for storing user info and teaching I2C sniffing/injection, and that the badge was funded via Kickstarter; provided the two saved images.'
- kind: url
  url: https://github.com/Sodium-Hydrogen/TRON-Badge
  title: Sodium-Hydrogen/TRON-Badge - GitHub
  accessed: '2026-09-08'
  note: Official repo for the badge (also referred to as "Bus Pirate vTRON"); confirms design files were published, though no explicit license was found in the accessible content.
- kind: url
  url: https://www.hackster.io/news/the-def-con-tron-indie-badge-is-designed-to-hack-other-badges-4afecd4ca066
  title: The DEF CON TRON Indie Badge Is Designed to Hack Other Badges - Hackster.io
  accessed: '2026-09-08'
  note: Search snippet confirms the badge launched a Kickstarter campaign that exceeded its funding goal; full article was blocked by Cloudflare and could not be read directly.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Duplicate of dc27-tron-badge-recognizer (same badge, same maker, same primary source, created by a different sweep task). Price, exact quantity, current availability, LED pixel counts, and any display are not stated in any source found and are left empty/null. The GitHub repo could not be fully read (only its landing page and a snippet were accessible), so hardware/firmware open-source status is marked "partial" on the strength of a public repo existing, not a confirmed license. Hackster.io's full article was blocked by a bot-detection page; only the search snippet was usable. Merged with duplicate entry 'Tron Badge (Recognizer)' (dc27-tron-badge-recognizer).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc27/tron-badge-recognizer/
---

An independently made ("indie"/unofficial) badge for DEF CON 27 (2019), created by a maker known as Sodium_Hydrogen and themed after a Recognizer, the enforcer vehicle/being from the Tron films. The badge is built around an ATmega328 microcontroller and combines an 8x12 white LED matrix (for scrolling text) with 16 RGB LEDs for animated lighting patterns.

Its headline feature was a fully integrated Bus Pirate v3.6, a well-known open-source debugging and protocol-analysis tool, operable from a terminal app on an Android phone rather than requiring a separate computer. This let the badge be used to probe the hardware of other DEF CON badges. It shipped with a companion "identity disk" SAO accessory, referencing the disc weapon/data-storage prop from the films, which stored the wearer's information and doubled as a teaching aid for listening to and injecting data on an I2C bus.

The project was funded through a Kickstarter campaign that exceeded its goal ahead of the con, with hardware and firmware published in a GitHub repository. According to Hackaday's DEF CON 27 badge roundup, production began in June 2019 but was delayed by incorrectly supplied parts during assembly, so finished badges were not ready until after the convention had ended. No pricing, production quantity, or post-con availability details were found in the sources checked.

## Make your own

Design files and firmware are published at [github.com/Sodium-Hydrogen/TRON-Badge](https://github.com/Sodium-Hydrogen/TRON-Badge), under the "Bus Pirate vTRON" name; the repo's wiki is referenced for general badge information, though its full contents (schematics, BOM, license) were not accessible during this research pass.

## Notes merged from the duplicate entry "Tron Badge (Recognizer)"

An independently made ("indie"/unofficial) badge for DEF CON 27 (2019), created by a maker known as Sodium_Hydrogen and themed after a Recognizer, the enforcer vehicle/being from the Tron films. The badge is built around an ATmega328 microcontroller and combines an 8x12 white LED matrix (for scrolling text) with 16 RGB LEDs for animated lighting patterns, giving it a distinct in-universe look on top of its blinky-badge functionality.

Its standout feature was a fully integrated Bus Pirate, a well-known open-source debugging and protocol-analysis tool, which could be operated from a terminal app on an Android phone rather than requiring a separate computer. The badge also had a companion "identity disk" add-on accessory, referencing the disc weapon/data-storage prop from the films.

According to Hackaday's DEF CON 27 badge roundup, production began in June 2019 but was delayed by incorrectly supplied parts during assembly, so finished badges were not ready until after the convention had ended. No pricing, production quantity, or distribution details were found in available sources.
