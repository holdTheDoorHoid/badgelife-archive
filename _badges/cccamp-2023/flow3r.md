---
title: flow3r
id: cccamp-2023-flow3r
layout: badge
parent: Chaos Communication Camp 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cccamp-2023
year: 2023
makers:
- name: CCCamp23 Badge Team (Süd Ost Chaos)
  url: https://flow3r.garden/
summary: 'The official badge of Chaos Communication Camp 2023: a flower-shaped electronic instrument that turns touch and gesture across its petals into sound and light.'
functions: 'Touch- and gesture-controlled synth/light instrument, programmable in MicroPython; plays audio through built-in speakers and drives a 40-LED illuminated edge; can be re-flashed with custom apps.'
look:
  colors: [multicolor]
  shape: flower
  themes: [music, art]
tech:
  mcu: ESP32-S3
  leds:
    count: 40
    type: RGB
    note: LEDs positioned along the badge's edge/petals
  display: round color display, 240x240
  connectivity: [usb]
  battery: 'optional battery pack, MCH2022-compatible connector; otherwise USB power (computer or power bank)'
  sao_version: null
get_one:
  price: '€32'
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'checked 2026-09-08: was sold alongside camp tickets in 2023, advance reservation required, covering ~50% of attendees; camp is over so no longer available'
  distribution: [purchase]
  where: 'Reserved and paid for (€32, manufacturing/assembly cost only) during CCCamp 2023 ticket purchase'
make_your_own:
  open_source: yes
  hardware_url: https://git.flow3r.garden/flow3r
  firmware_url: https://git.flow3r.garden/flow3r
  eda_tool: null
  notes: 'Maker states electrical and mechanical design plus firmware are open source; docs at https://docs.flow3r.garden/, assembly guide at https://flow3r.garden/assembly'
links:
- label: events.ccc.de/camp/2023/hub/camp23/en/assembly/CCCamp23-BadgeTeam
  url: https://events.ccc.de/camp/2023/hub/camp23/en/assembly/CCCamp23-BadgeTeam/
  kind: website
- label: 'CCC Event Blog: Camp 2023 - The flow3r Badge'
  url: https://events.ccc.de/en/2023/06/05/camp23-the-flow3r-badge/
  kind: article
- label: flow3r.garden
  url: https://flow3r.garden/
  kind: website
- label: flow3r docs
  url: https://docs.flow3r.garden/
  kind: doc
- label: flow3r git (hardware + firmware)
  url: https://git.flow3r.garden/flow3r
  kind: repo
- label: 'How to grow your flow3r (assembly instructions video)'
  url: https://media.ccc.de/v/camp2023-101-the-flow3r-badge-assembly-i
  kind: video
images:
  - file: assets/images/badges/cccamp-2023/flow3r/b7616412b3.jpg
    source: "https://events.ccc.de/en/2023/06/05/camp23-the-flow3r-badge/"
    credit: "CCCamp23 Badge Team"
    caption: "flow3r badge, flower-shaped with illuminated edge"
  - file: assets/images/badges/cccamp-2023/flow3r/4515a02e0f.jpg
    source: "https://events.ccc.de/en/2023/06/05/camp23-the-flow3r-badge/"
    credit: "CCCamp23 Badge Team"
    caption: "flow3r badge, worn/held view"
contact:
  mastodon: '@flow3rbadge@chaos.social'
  matrix: '#flow3rbadge:events.ccc.de'
notes:
- Original sweep summary: "Official ESP32-S3 flower-shaped touch/gesture badge of Chaos Communication Camp 2023 that turns touch and motion into sound and light. Found by the event-year sweep, task cccamp."
status: released
sources:
- kind: url
  url: https://events.ccc.de/camp/2023/hub/camp23/en/assembly/CCCamp23-BadgeTeam/
  title: flow3r
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:cccamp); event read as ''cccamp-2023''.'
- kind: url
  url: https://events.ccc.de/en/2023/06/05/camp23-the-flow3r-badge/
  title: 'Camp 2023 - The flow3r Badge'
  accessed: '2026-09-08'
  note: 'Official CCC blog post: price (€32), sale mechanism via ticket reservation for ~50% of attendees, open-source statement, contact handles, images.'
- kind: url
  url: https://flow3r.garden/
  title: flow3r
  accessed: '2026-09-08'
  note: 'Maker landing page; links to docs, assembly guide, and git repo.'
- kind: url
  url: https://docs.flow3r.garden/
  title: flow3r docs (referenced)
  accessed: '2026-09-08'
  note: 'Referenced from flow3r.garden as the hardware/firmware documentation site; not separately fetched.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts (chip, LEDs, display, price, open-source status) confirmed on the CCC event blog and flow3r.garden. Exact production quantity not stated anywhere found (only that badges covered roughly half of camp tickets); left empty. Precise LED note (edge vs petal placement) is paraphrased from press description, not an exact maker spec sheet. A separate community-modified variant, "anal0g flow3r" by wenzellabs, already has its own entry (cccamp-2023-anal0g-flow3r) and is distinct from this one.'
last_modified_date: '2026-09-08'
---

flow3r was the official badge of Chaos Communication Camp 2023, built by the CCCamp23 Badge Team (part of Süd Ost Chaos) as an optional add-on to camp tickets rather than a Camp-price-funded giveaway. Shaped like a flower, it is an electronic instrument built around an ESP32-S3: a round 240x240 color display sits at its center, a ring of 40 RGB LEDs runs along its illuminated edge, and its petals can sense touch and gesture simultaneously across the whole surface. Two built-in speakers and a 3.5mm audio jack let it turn those touches into sound as well as light, and it is programmed in MicroPython so owners can modify the built-in apps or write new ones.

Roughly half of camp attendees were able to reserve one in advance for €32, a price the team said covered manufacturing and assembly only. Power comes from USB-C (a computer or power bank) or an optional battery pack using an MCH2022-compatible connector, and a microSD slot allows for expansion. The hardware, mechanical design, and firmware are all published as open source, with documentation, an assembly guide, and the full git repository hosted on the team's own flow3r.garden site.

## Make your own

The maker publishes electrical, mechanical, and firmware sources at https://git.flow3r.garden/flow3r, with build documentation at https://docs.flow3r.garden/ and a step-by-step assembly guide at https://flow3r.garden/assembly; the team also released an official "How to grow your flow3r" assembly-instructions video (media.ccc.de).
