---
title: Voltage Multiplier / Spark Gap Badge
id: supercon-2015-voltage-multiplier-spark-gap-badge
layout: badge
parent: Hackaday SuperConference 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2015
year: 2015
makers:
- name: Sprite_TM (Jeroen Domburg)
summary: A hand-built deadbug badge that turns a 9V battery into roughly 1000V for a small spark gap, built on-site at the 2015 Hackaday SuperConference workshop.
functions: Steps a 9V battery up to about 1000V through a hex Schmitt trigger oscillator, a hand-wound transformer, and a diode/capacitor voltage multiplier, driving a spark gap.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: 9V battery
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2015/12/09/the-best-badges-of-the-supercon
  url: https://hackaday.com/2015/12/09/the-best-badges-of-the-supercon/
  kind: article
images:
  - file: assets/images/badges/supercon-2015/voltage-multiplier-spark-gap-badge/7cb36205f1.jpg
    source: "https://hackaday.com/2015/12/09/the-best-badges-of-the-supercon/"
    credit: "Sprite_tm (Jeroen Domburg)"
    caption: "The deadbug-built voltage multiplier / spark gap badge"
  - file: assets/images/badges/supercon-2015/voltage-multiplier-spark-gap-badge/73dac1cfb9.jpg
    source: "https://hackaday.com/2015/12/09/the-best-badges-of-the-supercon/"
    credit: "Sprite_tm (Jeroen Domburg)"
    caption: "Sprite_tm's schematic for the voltage multiplier circuit"
contact: {}
notes:
- Won "Best Deadbug" at the 2015 Supercon badge contest. Found by the event-year sweep, task supercon-2015; the sweep's one-line note matches Hackaday's coverage.
status: released
sources:
- kind: url
  url: https://hackaday.com/2015/12/09/the-best-badges-of-the-supercon/
  title: Voltage Multiplier / Spark Gap Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2015); event read as ''supercon-2015''.'
- kind: url
  url: https://hackaday.com/2015/12/09/the-best-badges-of-the-supercon/
  title: "The Best Badges Of The Supercon"
  accessed: '2026-09-08'
  note: "Confirmed the item: description of the circuit (hex Schmitt trigger + modified relay-as-transformer, cap/diode voltage multiplier to ~1000V from a 9V battery), photo credited to Sprite_tm, and schematic image."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: This was a one-off hand-built ("deadbug") entry in the 2015 Supercon badge contest, not a distributed/manufactured badge — no PCB, no repo, no storefront, no price or quantity exist to find. Hackaday's contest recap is the only source located; no maker's-own page (Hackaday.io project log, tweet, or blog post) turning up further detail was found. Sprite_tm also built a related, separate "tiny Tesla coil" badge that day with Radu Motisan; that is a different item and is not this entry.
last_modified_date: '2026-09-08'
---

At the 2015 Hackaday SuperConference, a badge-hacking workshop gave attendees loose parts and little else. Sprite_tm (Jeroen Domburg) used the time to deadbug-build a voltage multiplier: a hex Schmitt trigger oscillator drives a transformer he wound himself from magnet wire around a modified relay, and the resulting few hundred volts is stepped up further through a chain of capacitors and diodes acting as a voltage multiplier. The finished circuit turned a single 9V battery into roughly 1000V, enough to draw a visible spark across a small gap. It won "Best Deadbug" in that year's Supercon badge contest.

The same day, Sprite_tm also collaborated with Radu Motisan on a second, separate build attempting a very small Tesla coil with a Kynar-wire secondary; that project was left unfinished and is not part of this entry.

No hardware files, firmware, or storefront exist for this piece — it was a one-off contest build rather than a distributed badge, and Hackaday's contest recap is the only documentation of it found during research.
