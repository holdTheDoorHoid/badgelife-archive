---
title: CHV Badge
id: dc30-from-their-cfp-it-seems-they-will-have-one
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: Car Hacking Village
  url: https://carhackingvillage.com
summary: An RP2040-based badge from DEF CON 30's Car Hacking Village that generates CAN bus waveforms and other digital-protocol traffic, including deliberately malformed frames, to test vehicle network defenses.
functions: Generates CAN bus waveforms and other digital protocols, including versions with injected errors, to disrupt or probe vehicle networks. Rather than acting only as a passive CAN analyzer, its generation is interactive and adjusts based on how the target network responds.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: $50
  price_usd: 50.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: In Person at the con
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- kind: website
  label: Car Hacking Village
  url: https://carhackingvillage.com
- kind: doc
  label: 'DEF CON 30 talks: Getting naughty on CAN bus with CHV Badge'
  url: https://carhackingvillage.com/defcon30-talks
images: []
contact: {}
notes:
- $50 in person (later online)
- 'The sheet only carried the note "From their CFP, it seems they will have one" with no title; the actual item is the Car Hacking Village''s DEF CON 30 badge, confirmed via a DC30 talk abstract titled "Getting naughty on CAN bus with CHV Badge."'
status: released
sources:
- kind: sheet
  event: dc30
  row: 15
  updated: '2022-07-31'
- kind: url
  url: https://carhackingvillage.com/defcon30-talks
  title: 'DEF CON 30 Talks - Car Hacking Village'
  accessed: '2026-09-06'
  note: Talk abstract for "Getting naughty on CAN bus with CHV Badge" confirming the badge exists, runs an RP2040, and generates CAN/digital-protocol waveforms with injectable errors.
- kind: url
  url: https://carhackingvillage.com
  title: Car Hacking Village
  accessed: '2026-09-06'
  note: Maker homepage; confirms CHV as the organization and its ongoing SAO/badge program, but no DC30-specific product page or images found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    Title was a sheet placeholder ("From their CFP, it seems they will have one") naming only the
    maker. Found the actual item via a DEF CON 30 talk description on carhackingvillage.com titled
    "Getting naughty on CAN bus with CHV Badge," which confirms it is an RP2040-based badge that
    generates CAN waveforms and other digital protocols (including ones with deliberate errors) to
    disrupt vehicle networks, and that its waveform generation is interactive rather than a plain
    analyzer. Could not find a dedicated product/store page, quantity made, LED/display specs, or
    photos of the DC30 badge itself; CHV's public GitHub org (car-hacking-village) has badge
    hardware/firmware repos starting at DC31 (DC31_CHV_Badge_Board etc.) but nothing for DC30, so
    make_your_own is left empty rather than guessed. Web search quota was exhausted mid-task; only
    WebFetch and curl were used for the later checks.
last_modified_date: '2026-09-06'
---

The Car Hacking Village's DEF CON 30 badge showed up on the community sheet only as an unlabeled row with the note "From their CFP, it seems they will have one" — someone had seen the village's call-for-papers listing a badge before the con and hadn't yet confirmed what it was. It turns out to be an RP2040-based board built around CHV's core theme: generating CAN bus traffic. A DC30 talk, "Getting naughty on CAN bus with CHV Badge," describes it as capable of producing CAN waveforms and other digital protocols, including versions with deliberately injected errors, to disrupt or probe vehicle networks — and notes that its generation is interactive, changing based on how the target network responds, rather than acting as a simple passive analyzer.

Beyond that talk description, little else about the DC30 badge specifically is documented publicly. Car Hacking Village's GitHub organization hosts open hardware and firmware for its badges starting with DEF CON 31 (the "Engine block badge," a separate entry in this archive) and continuing through DEF CON 34, but no DC30-specific repository was found, so it's unclear whether this earlier badge's design files were ever published. The community sheet records it as $50, sold in person at the con with a later online option, consistent with how CHV has sold its badges in other years.
