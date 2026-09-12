---
title: DEF CON 20 Official Badge
id: dc20-official-badge
layout: badge
parent: DC20
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc20
year: 2012
makers:
- name: Ryan Clarke (LosT)
summary: The official electronic badge for DEF CON 20 (2012), built around a Parallax Propeller P8X32A multicore chip and issued in eight role-based variants as part of a running puzzle.
functions: Runs a badge puzzle/unlock sequence, tracking progress in an onboard EEPROM read over i2c; drives 8 onboard LEDs by PWM to reflect EEPROM state; supports infrared badge-to-badge communication and USB programming/reflashing.
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - security
tech:
  mcu: Propeller P8X32A
  leds:
    count: 8
    type: null
    note: PWM-driven, reflect EEPROM puzzle state
  display: null
  connectivity:
  - ir
  - usb
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: infocondb.org/con/def-con/def-con-20/welcome-making-the-def-con-20-badge
  url: https://infocondb.org/con/def-con/def-con-20/welcome-making-the-def-con-20-badge
  kind: website
- label: Parallax Propeller on DEF CON 20 Badge (forum thread)
  url: https://forums.parallax.com/discussion/141494/article-parallax-propeller-on-def-con-20-badge-start-here
  kind: article
- label: Defcon 20 Badge Revisited - Part 2
  url: https://020d.github.io/blog/2024/08/16/Defcon_20_badge_revisited_part_II
  kind: article
- label: badge.gallery - DEF CON 20
  url: https://badge.gallery/events/def-con-20
  kind: website
- label: DEF CON 20 Hacking Conference index (defcon.org)
  url: https://defcon.org/html/defcon-20/dc-20-index.html
  kind: website
  archived: https://web.archive.org/web/20260728164322/https://defcon.org/html/defcon-20/dc-20-index.html
- label: badge.gallery/badges/def-con-20-badge
  url: https://badge.gallery/badges/def-con-20-badge
  kind: website
images:
- file: assets/images/badges/dc20/official-badge/b1bf347d2b.jpg
  source: https://badge.gallery/badges/def-con-20-badge
  credit: Wikimedia Commons (CC BY-SA 4.0), via badge.gallery
  caption: DEF CON 20 badge (Human variant), Propeller-based IR puzzle badge
contact: {}
notes:
- Propeller P8X32A-based electronic badge issued in 8 color/role variants (Human, Contest, Goon, Artist, Press, Vendor, Speaker, CFP) with the Human badge alone in 21 shapes, designed by Ryan Clarke for DEF CON 20. Found by the event-year sweep, task dc20-all.
- 'Sources disagree on the exact 8th variant name: the sweep''s note says "CFP", while a 2024 retrospective blog post lists "Uber" instead of CFP. Neither claim about a "21 shapes" Human badge count could be independently confirmed within this research pass.'
- Propeller P8X32A-based badge with IR badge-to-badge comms, 21 Human-badge variants, and a VGA/PS2-expandable HHV platform. Found by the event-year sweep, task general-2006.
- This entry duplicates dc20-official-badge, which covers the same DEF CON 20 official badge (Ryan Clarke/LosT, Parallax). Both entries filled in independently per research-guide instructions; consider merging.
status: listed
sources:
- kind: url
  url: https://infocondb.org/con/def-con/def-con-20/welcome-making-the-def-con-20-badge
  title: DEF CON 20 Official Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc20-all); event read as ''dc20''.'
- kind: url
  url: https://forums.parallax.com/discussion/141494/article-parallax-propeller-on-def-con-20-badge-start-here
  title: 'Article: Parallax Propeller on DEF CON 20 Badge - Start Here!'
  accessed: '2026-09-08'
  note: Confirms Propeller P8X32A chip and badge origin; page itself was gated behind a captcha redirect at fetch time, cited via search snippet only.
- kind: url
  url: https://020d.github.io/blog/2024/08/16/Defcon_20_badge_revisited_part_II
  title: Defcon 20 Badge Revisited - Part 2
  accessed: '2026-09-08'
  note: Confirms 8 badge-type variants, 8 onboard LEDs driven by PWM reflecting an EEPROM-tracked puzzle state read over i2c, and that firmware was released by Defcon/1o57.
- kind: url
  url: https://badge.gallery/events/def-con-20
  title: badge.gallery - DEF CON 20
  accessed: '2026-09-08'
  note: Confirms Parallax as manufacturer, Ryan Clarke as designer, and infrared badge-to-badge communication plus USB programming; also references an optional VGA/PS2 expansion.
- kind: url
  url: https://defcon.org/html/defcon-20/dc-20-index.html
  title: DEF CON 20 Hacking Conference
  accessed: '2026-09-08'
  note: Confirms official Human badges were later sold online via hackerstickers.com (product page now 404) and that firmware/materials were included on the official conference DVD.
  archived: https://web.archive.org/web/20260728164322/https://defcon.org/html/defcon-20/dc-20-index.html
- kind: url
  url: https://badge.gallery/badges/def-con-20-badge
  title: DEF CON 20 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2006); event read as ''dc20''.'
- kind: url
  url: https://badge.gallery/badges/def-con-20-badge
  title: DEF CON 20 Badge
  accessed: '2026-09-08'
  note: Confirmed designer (Ryan Clarke/LosT), manufacturer (Parallax), chip (Propeller P8X32A), LED count, IR/USB features, VGA/PS2 expansion, and 21 Human-badge variants. Price, quantity, and availability were not stated.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Core facts (designer, chip, variant count, LED/EEPROM puzzle mechanic, IR/USB connectivity) confirmed across the maker-adjacent Parallax forum, a detailed 2024 retrospective, and badge.gallery's catalog entry, but no single maker-published spec sheet was found. Price, quantity made, PCB color/shape, and display were not found. A likely duplicate exists in the archive (dc20-badge, "DEF CON 20 Badge") describing the same item with the same maker attribution - flagged rather than merged since this pass touches only one entry. Could not confirm an image that specifically and verifiably shows the DEF CON 20 badge (a candidate Wikimedia Commons photo covers "multiple DefCon badges" across unspecified years, so it was not used) within the research budget. Merged with duplicate entry 'DEF CON 20 Badge' (dc20-badge).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/dc20/badge/
---

The DEF CON 20 (2012) official badge was designed by Ryan Clarke, known as LosT, and manufactured by Parallax around its Propeller P8X32A multicore microcontroller. As with other LosT-era DEF CON badges, it doubled as a running puzzle: eight onboard LEDs, driven by PWM, reflected a progress value tracked in an onboard EEPROM that attendees worked to unlock over the course of the con, with state read back over i2c. The badge also supported infrared badge-to-badge communication and could be reprogrammed over USB, and an optional VGA/PS2 expansion has been referenced in later write-ups of the hardware.

The badge was issued in eight role-based variants tied to attendee type (Human, Contest, Goon, Artist, Press, Vendor, Speaker, and an eighth role that sources disagree on - named "CFP" in the archive's original sweep note but "Uber" in a 2024 retrospective). Firmware for the badge was released by Defcon/1o57, and badge materials were distributed on the official conference DVD; DEF CON's own site later noted that official Human badges were made available for purchase online through hackerstickers.com, though that specific product listing is no longer live.

This entry appears to duplicate another archive entry for the same badge (`dc20-badge`, "DEF CON 20 Badge," same maker attribution); that overlap is reported here rather than resolved, since this research pass is scoped to a single entry.

## Notes merged from the duplicate entry "DEF CON 20 Badge"

The DEF CON 20 badge (2012, Rio Hotel, Las Vegas) was designed by Ryan Clarke (LosT) and manufactured by Parallax, built around Parallax's own Propeller P8X32A multicore microcontroller. It shipped in 21 different "Human" badge shape variants, each tied to one of eight attendee-role color schemes, and used eight onboard LEDs for visual feedback. Firmware lived in onboard EEPROM and could be reprogrammed in Assembly, C, or Spin over USB.

Functionally, the badge combined an infrared badge-to-badge link (used to track and record encounters between attendees) with an embedded secret-society narrative woven from hieroglyphics, binary codes, venue-based clues, and social puzzles for attendees to work out over the course of the con. It also exposed VGA and PS/2 expansion, letting sufficiently motivated attendees turn the badge into a small standalone computer system — a hallmark of the DEF CON hardware-hacking-village (HHV) badges of this era.

Price, production quantity, and current availability were not stated on the source consulted. This entry substantially duplicates `dc20-official-badge`, which was already filled in separately for the same badge, designer, and maker.
