---
title: Unofficial fan-made 2020 Remoticon badge design
id: other-unofficial-fan-made-2020-remoticon-badge-design
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2020
makers:
- name: Thomas Flummer
  url: https://github.com/flummer
summary: A community-made, unofficial badge PCB designed for Hackaday's 2020 Remoticon (the virtual replacement for Hackaday Superconference), shared as open-source KiCad files for anyone to order and build.
functions: Mostly a prototyping/decoration board with an area of exposed copper pads for freeform soldering, plus an SMD hand-soldering challenge (by MakersBox) built around an ATtiny85. It has optional headers on the back to mount on an Adafruit Feather board for power/logic.
look:
  colors: []
  shape: null
  themes:
  - badgelife
tech:
  mcu: null
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Never sold; shared as open design files (KiCad + Gerbers, also posted to OSH Park's shared-projects page) for anyone to fabricate their own copy.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/flummer/remoticon2020-badge
  firmware_url: null
  eda_tool: KiCad
  license: CC-BY-SA-4.0
links:
- label: flummer/remoticon2020-badge on GitHub
  url: https://github.com/flummer/remoticon2020-badge
  kind: repo
- label: hackaday.io/project/174089-2020-remoticon-pandemic-creativity-start-here
  url: https://hackaday.io/project/174089-2020-remoticon-pandemic-creativity-start-here
  kind: hackaday
images:
- file: assets/images/badges/other/unofficial-fan-made-2020-remoticon-badge-design/9af32c17fa.jpg
  source: https://github.com/flummer/remoticon2020-badge
  credit: Thomas Flummer
  caption: Render of the unofficial fan-made Remoticon 2020 badge PCB design
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: mentioned on https://hackaday.io/project/174089-2020-remoticon-pandemic-creativity-start-here (GitHub repo URL not confirmed/located)
  title: Unofficial fan-made 2020 Remoticon badge design
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''supercon-2020''.'
- kind: url
  url: https://hackaday.io/project/174089-2020-remoticon-pandemic-creativity-start-here
  title: '2020 Remoticon: Pandemic Creativity, Start Here! - Hackaday.io'
  accessed: '2026-09-07'
  note: Hackaday.io project page where Thomas Flummer posted about designing an unofficial badge for the virtual 2020 Remoticon and linked his GitHub repo.
- kind: url
  url: https://github.com/flummer/remoticon2020-badge
  title: flummer/remoticon2020-badge
  accessed: '2026-09-07'
  note: Maker's own repo confirming design details, KiCad/Gerber files, CC-BY-SA-4.0 license, SMD challenge by MakersBox, optional Feather mounting, and the render image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Made for Hackaday's 2020 Remoticon, a virtual event (no in-person con and no official badge that year), which has no matching id in _data/events.yml, so event is left as 'other'. Specific MCU/LED counts are not stated beyond the optional Adafruit Feather mount and an ATtiny85-based SMD soldering-practice component; price/quantity are not applicable since it was never sold, only shared as open design files.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/unofficial-fan-made-2020-remoticon-badge-design.glb
  method: kicad
  source_file: remoticon_badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 245648
---

Thomas Flummer designed this PCB as an unofficial badge for Hackaday's 2020 Remoticon, the virtual, distributed event that replaced the in-person Hackaday Superconference during the pandemic. With no official hardware badge for the online con, Flummer built one himself, inspired by the event's graphics, and released it as an open-source KiCad design on GitHub so other attendees could fabricate and modify their own copies.

The board is largely a prototyping and decoration piece: most of its surface is exposed copper pads meant for freeform hand-soldering rather than a fixed circuit. It includes an SMD soldering-challenge section contributed by MakersBox, built around an ATtiny85, for practicing fine hand-soldering. The back carries optional headers so the badge can be mounted onto and powered by an Adafruit Feather board, though it works as a standalone piece without one.

## Make your own

Full KiCad schematics, PCB layout, and Gerber files are published in the GitHub repo under a CC-BY-SA-4.0 license, and the design was also shared to OSH Park's shared-projects page for one-click ordering. Flummer explicitly invited others to fork it, remix it, and post their own variants under the #badgelife hashtag; no assembled units were sold.
