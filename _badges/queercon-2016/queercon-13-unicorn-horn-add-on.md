---
title: Queercon 13 unicorn horn add-on
id: queercon-2016-queercon-13-unicorn-horn-add-on
layout: badge
parent: Queercon 13 (2016)
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: queercon-2016
year: 2016
makers:
- name: Queercon badge team
summary: A unicorn-horn hat accessory with a rainbow LED that plugs into one of the two powered head expansion ports on the 2016 Queercon (squid/cuttlefish) badge.
functions: 'Lights a rainbow LED when plugged into the host badge''s head port; purely decorative, no interactivity beyond that.'
look:
  colors: [multicolor]
  shape: null
  themes: [fantasy, wearable]
tech:
  mcu: none
  leds:
    count: 1
    type: RGB
    note: Described only as "a rainbow LED inside"; driver IC and exact part not stated by sources.
  display: none
  connectivity: [i2c]
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge
  url: https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/
  kind: article
- label: 'Hackaday.io: An oral history of the shitty add-on standard'
  url: https://hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  kind: article
  accessed: '2026-09-10'
  note: 'Confirms the 2016 Queercon badge had two head expansion ports (power, ground, I2C on a 1x4 connector) that carried hats including a unicorn horn, an emo haircut, and a top hat studded with LEDs.'
images:
- file: assets/images/badges/queercon-2016/queercon-13-unicorn-horn-add-on/9033fac38e.jpg
  source: "https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/"
  credit: "Hackaday"
  caption: "The 2016 Queercon badge wearing two head-port hats, including a unicorn horn"
contact: {}
notes:
- 'Sweep''s wording ("Unicorn-horn hat accessory ... plugging into the squid badge''s head expansion ports") matches what sources confirm; the badge is more often called the "cuttlefish" or "cuttlebadge" than "squid" in later sources, but Hackaday''s original piece does use "squid."'
- 'Neither source names who specifically designed the unicorn horn (as opposed to the main badge, credited elsewhere to Evan Mackay, George Louthan, Jonathan Nelson, and Jason Painter). The expansion port connector spec was published ahead of the event, so hats may have been built by the badge team or by attendees/other hackers using that spec; could not confirm which for this specific hat.'
- 'The Hackaday.io oral-history log also mentions an emo-haircut hat and an LED-studded top hat for the same badge, neither of which has its own archive entry yet.'
status: listed
sources:
- kind: url
  url: https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/
  title: Queercon 13 unicorn horn add-on
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:queercon); event read as ''queercon-2016''.'
- kind: url
  url: https://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/
  title: What We Learned From The 2016 Queercon Badge
  accessed: '2026-09-10'
  note: 'Confirms the unicorn horn: "The badge had two expansion ports on the squid''s head for adding hats... Our favourite? A unicorn horn with a rainbow LED inside." No maker, price, or quantity given.'
- kind: url
  url: https://hackaday.io/project/52950-shitty-add-ons/log/151626-an-oral-history-of-the-shitty-add-on-standard
  title: An oral history of the shitty add-on standard
  accessed: '2026-09-10'
  note: 'Independent confirmation: "The 2016 Queercon badge came with hats, powered by two small expansion ports... giving these cuttlebadges unicorn horns, an emo haircut, or a top hat studded with LEDs."'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Existence confirmed by two independent third-party sources (Hackaday article and a Hackaday.io oral history), not by a maker''s own page or storefront, so confidence is medium rather than high. Could not find who specifically designed this hat, price, quantity made, or whether it was an official Queercon-team accessory or an attendee-built one using the published connector spec. No repo or storefront found specific to the hat itself; the main badge''s GitHub (Queercon/QC13-Badge) was located but not confirmed to include hat design files.'
last_modified_date: '2026-09-10'
---

The unicorn horn add-on was one of two "hat" accessories built for the 2016 Queercon 13 badge (a squid/cuttlefish-shaped board), plugging into either of two small expansion ports on the top of the badge's head. Those ports carried power, ground, and an I2C bus over a 1x4 connector, and Queercon published the connector spec ahead of the event so that hats could be built independently of the main badge. The horn itself lit a single rainbow LED when plugged in; Hackaday singled it out as their favorite of the head-port accessories in their write-up of that year's badge.

Beyond its existence and basic description, little else is documented publicly: no source names a specific designer for the horn (as distinct from the main badge, credited to Evan Mackay, George Louthan, Jonathan Nelson, and Jason Painter), and no price, production quantity, or distribution method is recorded. A companion Hackaday.io oral history of the "shitty add-on" standard independently confirms the same badge also supported an emo-haircut hat and an LED-studded top hat through the same ports, neither of which is yet documented in this archive.
