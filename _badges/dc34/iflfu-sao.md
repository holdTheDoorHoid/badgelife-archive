---
title: IFLFU SAO
id: dc34-iflfu-sao
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc34
year: 2026
makers:
- name: BigFuckingBadge
  url: https://www.bigfuckingbadge.com
summary: A simple backlit rectangle SAO that flashes a raunchy/romantic two-word message at random; the first entry in BigFuckingBadge's "OffensiveSAO" lineup.
functions: Illuminates the words "I FUCKING LOVE FUCKING YOU" but both "FUCKING"s are illuminated randomly.
look:
  colors: []
  shape: rectangle
  themes:
  - meme
  - text
tech:
  mcu: PFC161
  leds:
    count: 2
    type: discrete
    note: Two LEDs (active-low, current-sink) backlight the two "FUCKING" words; a Padauk PFC161 runs an LFSR-seeded pseudo-random pattern to flash them independently.
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $20
  price_usd: 20.0
  quantity: ''
  availability: limited
  distribution:
  - purchase
  - preorder
  where: 'BigFuckingBadge''s DEF CON 34 presale (email bfb.team.public@gmail.com to arrange a presale/drop) and at drops in the BadgeLife Village during the con.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hexum064/iflfu-hardware
  firmware_url: https://github.com/Hexum064/iflfu-v2-pfc161
  eda_tool: KiCad
links:
- label: www.bigfuckingbadge.com
  url: https://www.bigfuckingbadge.com
  kind: store
- label: github.com/Hexum064/iflfu-v2-pfc161
  url: https://github.com/Hexum064/iflfu-v2-pfc161
  kind: repo
- label: github.com/Hexum064/iflfu-hardware
  url: https://github.com/Hexum064/iflfu-hardware
  kind: repo
images:
  - file: assets/images/badges/dc34/iflfu-sao/ddb85b588f.jpg
    source: "https://www.bigfuckingbadge.com"
    credit: "BigFuckingBadge"
    caption: "The IFLFY/IFLFU SAO, a backlit rectangle SAO from BigFuckingBadge's OffensiveSAO lineup"
contact:
  discord: Hexum064
  emails:
  - bfb.team.public@gmail.com
notes:
- "BigFuckingBadge's own site (bigfuckingbadge.com) lists and photographs this item as the \"IFLFY SAO\" (image file images/ifly.jpg), one letter different from the community sheet's \"IFLFU\". The maker's two GitHub repos both use \"iflfu\" in their names, matching the sheet, so the title here was kept as IFLFU; the site's spelling may be a typo. Description and price match on both sources, so this is very likely the same item under a one-letter spelling discrepancy."
status: listed
sources:
- kind: sheet
  event: dc34
  row: 40
  updated: 7/7/2026 11:20:56
  listing: Update to Existing
- kind: url
  url: https://www.bigfuckingbadge.com
  title: "BIGFUCKINGBADGE.COM — Defcon 34 Badges and SAOs"
  accessed: '2026-09-06'
  note: "Maker's own presale page: confirms this is the \"IFLFY SAO\" ($20), 'the original and first SAO in BigFuckingBadge's OffensiveSAO lineup', a simple backlit rectangle sending a random romantic/raunchy message; presale open for DEF CON 34, Aug 2026, quantities limited, drops scheduled in the BadgeLife Village."
- kind: url
  url: https://github.com/Hexum064/iflfu-v2-pfc161
  title: "Hexum064/iflfu-v2-pfc161"
  accessed: '2026-09-06'
  note: "Firmware source: targets a Padauk PFC161 MCU, drives two active-low LEDs on PA4/PA5 with independent LFSR-seeded pseudo-random flash timers — confirms the 'both FUCKINGs illuminated randomly' behavior and the MCU."
- kind: url
  url: https://github.com/Hexum064/iflfu-hardware
  title: "Hexum064/iflfu-hardware"
  accessed: '2026-09-06'
  note: "Hardware repo: KiCad schematic/PCB files, gerbers, BOM, and a PFC161 datasheet reference — confirms open hardware and the EDA tool."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: "No maker's-page price for quantity made, or LED color, was found. Availability is 'limited' per the presale page rather than a clean available/sold-out state (unlike the lineup's 'fuck Note' SAO, which the same page marks sold out); no direct purchase link is live, only an email-to-arrange-a-drop presale. The 'IFLFY' vs 'IFLFU' spelling discrepancy between the site and the sheet/GitHub repos could not be resolved with certainty; see the note above."
last_modified_date: '2026-09-06'
---

The IFLFU SAO is a small backlit rectangle SAO from BigFuckingBadge (maker Hexum064), and by the team's own account the first entry in their "OffensiveSAO" lineup, predating the DFIU and PORTAL Gun SAOs from the same DEF CON 34 lineup. It lights up the phrase "I FUCKING LOVE FUCKING YOU," but a Padauk PFC161 microcontroller drives the two "FUCKING" words on independent LFSR-seeded pseudo-random timers, so each one flashes on its own unpredictable schedule rather than in sync — turning a simple two-LED backlight into a small novelty of random romantic/raunchy phrasing.

It sold for $20 as part of BigFuckingBadge's DEF CON 34 presale alongside the DFIU SAO, PORTAL Gun SAO, "fuck" Note SAO, and the oversized PORTAL badge, with quantities described as limited and drops arranged by emailing the team or catching them at the BadgeLife Village. Both hardware (KiCad schematic, PCB, gerbers, BOM) and firmware (C source targeting the PFC161 via the easypdk toolchain) are published on the maker's GitHub, making it a fully open build.

## Make your own

The hardware repo (`iflfu-hardware`) has KiCad source files and gerbers ready to send to a fab, plus a bill of materials. The firmware repo (`iflfu-v2-pfc161`) builds with the `easypdk` open toolchain for Padauk MCUs; the LED driver logic sinks current on two GPIO pins (PA4/PA5) and uses a linear-feedback shift register seeded from uninitialized RAM to randomize each LED's flash timing independently.
