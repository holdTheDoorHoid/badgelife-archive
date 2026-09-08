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
summary: 'The official electronic badge for DEF CON 20 (2012), built around a Parallax Propeller P8X32A multicore chip and issued in eight role-based variants as part of a running puzzle.'
functions: 'Runs a badge puzzle/unlock sequence, tracking progress in an onboard EEPROM read over i2c; drives 8 onboard LEDs by PWM to reflect EEPROM state; supports infrared badge-to-badge communication and USB programming/reflashing.'
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
- label: 'Defcon 20 Badge Revisited - Part 2'
  url: https://020d.github.io/blog/2024/08/16/Defcon_20_badge_revisited_part_II
  kind: article
- label: badge.gallery - DEF CON 20
  url: https://badge.gallery/events/def-con-20
  kind: website
- label: 'DEF CON 20 Hacking Conference index (defcon.org)'
  url: https://defcon.org/html/defcon-20/dc-20-index.html
  kind: website
images: []
contact: {}
notes:
- Propeller P8X32A-based electronic badge issued in 8 color/role variants (Human, Contest, Goon, Artist, Press, Vendor, Speaker, CFP) with the Human badge alone in 21 shapes, designed by Ryan Clarke for DEF CON 20. Found by the event-year sweep, task dc20-all.
- 'Sources disagree on the exact 8th variant name: the sweep''s note says "CFP", while a 2024 retrospective blog post lists "Uber" instead of CFP. Neither claim about a "21 shapes" Human badge count could be independently confirmed within this research pass.'
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
  note: 'Confirms Propeller P8X32A chip and badge origin; page itself was gated behind a captcha redirect at fetch time, cited via search snippet only.'
- kind: url
  url: https://020d.github.io/blog/2024/08/16/Defcon_20_badge_revisited_part_II
  title: 'Defcon 20 Badge Revisited - Part 2'
  accessed: '2026-09-08'
  note: 'Confirms 8 badge-type variants, 8 onboard LEDs driven by PWM reflecting an EEPROM-tracked puzzle state read over i2c, and that firmware was released by Defcon/1o57.'
- kind: url
  url: https://badge.gallery/events/def-con-20
  title: 'badge.gallery - DEF CON 20'
  accessed: '2026-09-08'
  note: 'Confirms Parallax as manufacturer, Ryan Clarke as designer, and infrared badge-to-badge communication plus USB programming; also references an optional VGA/PS2 expansion.'
- kind: url
  url: https://defcon.org/html/defcon-20/dc-20-index.html
  title: 'DEF CON 20 Hacking Conference'
  accessed: '2026-09-08'
  note: 'Confirms official Human badges were later sold online via hackerstickers.com (product page now 404) and that firmware/materials were included on the official conference DVD.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (designer, chip, variant count, LED/EEPROM puzzle mechanic, IR/USB connectivity) confirmed across the maker-adjacent Parallax forum, a detailed 2024 retrospective, and badge.gallery''s catalog entry, but no single maker-published spec sheet was found. Price, quantity made, PCB color/shape, and display were not found. A likely duplicate exists in the archive (dc20-badge, "DEF CON 20 Badge") describing the same item with the same maker attribution - flagged rather than merged since this pass touches only one entry. Could not confirm an image that specifically and verifiably shows the DEF CON 20 badge (a candidate Wikimedia Commons photo covers "multiple DefCon badges" across unspecified years, so it was not used) within the research budget.'
last_modified_date: '2026-09-08'
---

The DEF CON 20 (2012) official badge was designed by Ryan Clarke, known as LosT, and manufactured by Parallax around its Propeller P8X32A multicore microcontroller. As with other LosT-era DEF CON badges, it doubled as a running puzzle: eight onboard LEDs, driven by PWM, reflected a progress value tracked in an onboard EEPROM that attendees worked to unlock over the course of the con, with state read back over i2c. The badge also supported infrared badge-to-badge communication and could be reprogrammed over USB, and an optional VGA/PS2 expansion has been referenced in later write-ups of the hardware.

The badge was issued in eight role-based variants tied to attendee type (Human, Contest, Goon, Artist, Press, Vendor, Speaker, and an eighth role that sources disagree on - named "CFP" in the archive's original sweep note but "Uber" in a 2024 retrospective). Firmware for the badge was released by Defcon/1o57, and badge materials were distributed on the official conference DVD; DEF CON's own site later noted that official Human badges were made available for purchase online through hackerstickers.com, though that specific product listing is no longer live.

This entry appears to duplicate another archive entry for the same badge (`dc20-badge`, "DEF CON 20 Badge," same maker attribution); that overlap is reported here rather than resolved, since this research pass is scoped to a single entry.
