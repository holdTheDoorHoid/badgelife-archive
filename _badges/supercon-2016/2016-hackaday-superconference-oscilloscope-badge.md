---
title: 2016 Hackaday SuperConference Oscilloscope Badge
id: supercon-2016-2016-hackaday-superconference-oscilloscope-badge
layout: badge
parent: Hackaday Supercon 2016
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2016
year: 2016
makers:
- name: Ben Hencke
summary: ''
functions: ''
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/18039-2016-hackaday-superconference-oscilloscope-badge
  url: https://hackaday.io/project/18039-2016-hackaday-superconference-oscilloscope-badge
  kind: hackaday
- label: 'GitHub: simap/2016-Hackaday-SuperConference-Oscilloscope-Badge'
  url: https://github.com/simap/2016-Hackaday-SuperConference-Oscilloscope-Badge
  kind: repo
  archived: false
images: []
contact: {}
notes:
- A hardware hack turning the official 2016 Supercon badge into a 1-channel oscilloscope by wiring probes to the expansion port. Found by the event-year sweep, task supercon-2016.
- 'Sweep title matches the maker''s own project title, so no change was needed there.'
status: not_an_item
sources:
- kind: url
  url: https://hackaday.io/project/18039-2016-hackaday-superconference-oscilloscope-badge
  title: 2016 Hackaday SuperConference Oscilloscope Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2016); event read as ''supercon-2016''.'
- kind: url
  url: https://hackaday.io/project/18039-2016-hackaday-superconference-oscilloscope-badge
  title: 2016 Hackaday SuperConference Oscilloscope Badge
  accessed: '2026-09-08'
  note: Confirmed this is a firmware hack (by Ben Hencke) that repurposes the official 2016 Supercon badge as a single-channel scope; not a separate physical badge/SAO/accessory.
- kind: url
  url: https://github.com/simap/2016-Hackaday-SuperConference-Oscilloscope-Badge
  title: 'GitHub: simap/2016-Hackaday-SuperConference-Oscilloscope-Badge'
  accessed: '2026-09-08'
  note: Repo confirms it is firmware/software only (compatible with stock kernel/bootloader, no custom PCB); wiring a probe to expansion pin B4 + ground is the only physical step.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: This is a firmware hack for the stock, official 2016 Hackaday SuperConference badge, not a separate maker-produced badge/SAO/accessory — it adds no hardware of its own (just wires to the badge's existing expansion port) and was never sold or distributed independently. Marked not_an_item rather than filled in as a catalog entry. The GitHub repo (simap/2016-Hackaday-SuperConference-Oscilloscope-Badge) has the C source and a compiled firmware .hex if this is ever reconsidered for a "hacks/mods" section instead.
last_modified_date: '2026-09-08'
---

This is a firmware modification, not a standalone badge or accessory: Ben Hencke wrote it after forgetting his oscilloscope at Supercon 2016, turning the official conference badge into a working single-channel scope. The write-up describes wiring a probe to pin B4 on the badge's expansion connector along with a ground reference — no added hardware, no custom PCB.

The firmware (posted on GitHub as `simap/2016-Hackaday-SuperConference-Oscilloscope-Badge`) runs on the stock kernel and bootloader, and supports rising-edge triggering at 50%, a continuous scan mode, and eight selectable sample rates from 100 to 20,000 samples/second. Because it modifies the behavior of the official badge rather than being a distinct item that was designed, produced, or distributed on its own, it doesn't fit the archive's badge/SAO/accessory catalog and is recorded here as `not_an_item`.
