---
title: Core64 Interactive Core Memory Kit
id: other-core64-interactive-core-memory-kit
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 0
makers:
- name: ageppert
summary: A DIY kit that lets you hand-weave 64 bits of real magnetic core memory over an LED array, then read and write those bits directly with a magnetic wand.
functions: Weave 64 cores by hand, then use the included magnetic styli to flip individual bits; each core's state is shown live on the LED behind it, recreating a hands-on, physical version of 1960s core memory.
look:
  colors:
  - white
  - black
  shape: rectangle
  themes:
  - retro computer
  - learn to solder
  - kit
  form_factor: pcb badge
tech:
  mcu: RP2040
  leds:
    count: 64
    type: null
    note: One LED sits behind each of the 64 hand-woven cores.
  display: null
  connectivity:
  - usb
  inputs: []
  battery: included battery pack (LED Array Board)
  sao_version: null
  sao_ports: null
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ageppert/Core64
  firmware_url: https://github.com/ageppert/Core64
  eda_tool: null
get_one:
  price: $199 (Core64 full-size, Pico W) / $179 (Core64c compact)
  price_usd: 199
  quantity: ''
  availability: available
  availability_note: 'Both the full-size and compact kits were listed as purchasable on core64.io as of 2026-09-07.'
  distribution:
  - purchase
  - kit
  where: Sold directly from core64.io; local pickup offered at shows the maker attends, with shipping otherwise.
links:
- label: github.com/ageppert/Core64
  url: https://github.com/ageppert/Core64
  kind: repo
- label: core64.io - Core64 full-size kit
  url: https://www.core64.io/buy/p/core64-interactive-core-memory-full-size-kit
  kind: store
- label: core64.io - Core64c compact kit
  url: https://www.core64.io/buy/p/core64c-interactive-core-memory-compact-kit
  kind: store
images:
  - file: assets/images/badges/other/core64-interactive-core-memory-kit/f234c87142.jpg
    source: "https://www.core64.io/buy/p/core64-interactive-core-memory-full-size-kit"
    credit: "Core64.io / ageppert"
    caption: "Core64 Interactive Core Memory Kit, Pico W version V0.8"
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07). Also sold at https://www.core64.io/buy/p/core64-interactive-core-memory-full-size-kit and https://www.core64.io/buy/p/core64c-interactive-core-memory-compact-kit
status: released
sources:
- kind: url
  url: https://github.com/ageppert/Core64
  title: Core64 Interactive Core Memory Kit
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://www.core64.io/buy/p/core64-interactive-core-memory-full-size-kit
  title: Core64 - Interactive Core Memory Full Size Kit
  accessed: '2026-09-07'
  note: Confirmed price ($199), sub-kit contents, RP2040 (Pico W) microcontroller, and current V0.8 hardware revision.
- kind: url
  url: https://www.core64.io/buy/p/core64c-interactive-core-memory-compact-kit
  title: Core64c - Interactive Core Memory Compact Kit
  accessed: '2026-09-07'
  note: Confirmed price ($179), that it shares the same firmware/functionality as the full-size kit on a Raspberry Pi Pico, compact form factor V0.6.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a standalone kit sold directly by the maker (core64.io), not tied to one specific convention; it is offered for local pickup at shows the maker attends and shipped otherwise, so no single event/year applies and it is left under "other". Hardware has gone through several revisions (Teensy 3.2-based V0.5/V0.6, then RP2040/Pico-based V0.8 and Core64c V0.4/V0.6); tech.mcu/leds reflect the current Pico-based version. Exact LED part number, number-made, and first-release date were not found on the fetched pages. GitHub repo hosts firmware; no separate hardware/Gerbers repo link was confirmed, so make_your_own.open_source is left as "partial".'
last_modified_date: '2026-09-07'
---

Core64 is a kit built around a very literal idea: instead of simulating old magnetic-core computer memory, it makes you build a working 64-bit core memory plane by hand, threading wire through 64 tiny magnetic cores mounted over an LED array. Once assembled, two magnetic styli let the builder flip individual bits directly, and each core's LED lights up to show its current state, turning an obscure piece of 1960s computer history into something you can poke at with your own hands.

The kit is made and sold by ageppert directly through core64.io, and it comes as several sub-boards — a core matrix board, an LED array board with its own battery pack, and a logic board built around a Raspberry Pi Pico W, plus the two styli — with all surface-mount work done so the builder only has to weave the cores, solder through-hole headers, and assemble the parts. A smaller Core64c variant shares the same Pico-based firmware and nearly all the functionality of the full-size kit in a more compact board. Both are aimed at hobbyists who want a genuine hands-on soldering and weaving project rather than a pre-built badge, and both remain sold on an ongoing basis, with the maker also offering in-person pickup at the shows they attend.
