---
title: 2026 eChallengeCoin - Sara and the Missing Artifacts
id: dc34-2026-echallengecoin-sara-and-the-missing-artifacts
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
series: eChallengeCoin
makers:
- name: Bradán Lane STUDIO
  url: https://aosc.cc/eccn2026.php
summary: A brass challenge-coin-shaped electronic badge that runs a text adventure game, "Sara and the Missing Artifacts," over a USB serial terminal, given as a thank-you for a $100+ donation to a youth STEM charity of the recipient's choosing.
functions: All new text adventure game, "Sara and the Missing Artifacts", played over a USB serial connection; also usable as a general CircuitPython dev board via its capacitive touch pad, NeoPixels, and speaker
look:
  colors:
  - copper
  shape: coin
  themes:
  - coin
  - charity
  - puzzle
tech:
  mcu: ATSAMD21G1A (Cortex-M0+)
  leds:
    count: null
    type: NeoPixel
    note: three groups of NeoPixels around the coin's perimeter
  display: none
  connectivity:
  - usb
  battery: none (USB powered when connected; functions as a plain brass coin when disconnected)
  sao_version: none
get_one:
  price: proof of a $100+ donation to a youth STEM charity of the person's choosing
  price_usd: null
  quantity: 40 brass units (first 20 recipients get brass blanks manufactured by students from a local high school engineering program)
  availability: limited
  distribution:
  - free_drop
  where: Free gift for donating $100 or more to a youth-focused STEM education charity of your choice; claimed in person at DEF CON or by U.S. mail after submitting proof of donation via an online form
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: aosc.cc/eccn2026.php
  url: https://aosc.cc/eccn2026.php
  kind: website
images: []
contact: {}
notes:
- 'Duplicate of dc34-2026-choose-your-own-charity-echallengecoin, which already carries the full research, images, and merged notes for this item (same maker, same aosc.cc source, same 2026 eChallengeCoin). See that entry for the canonical write-up.'
status: listed
sources:
- kind: url
  url: https://aosc.cc/eccn2026.php
  title: 2026 eChallengeCoin - Sara and the Missing Artifacts
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''2026 (unclear which con, if any)''.'
- kind: url
  url: https://aosc.cc/eccn2026.php
  title: 2026 eChallengeCoin — AoSC
  accessed: '2026-09-07'
  note: 'Confirms this is the 2026 eChallengeCoin, "Sara and the Missing Artifacts," a brass CircuitPython coin from Bradán Lane STUDIO made with T.E.C. (Tod Troche, Lory Ester, Sara Cladlow) for DEF CON 34, given as a thank-you for $100+ charity donations; limited to 40 brass units; ATSAMD21G1A MCU, three groups of NeoPixels, speaker, capacitive touch pad, micro-USB, no battery.'
- kind: url
  url: https://aosc.cc/
  title: AoSC — Adventures of Sara Cladlow
  accessed: '2026-09-07'
  note: Background on the eChallengeCoin series (annual since 2020, text-adventure format since 2024) and the T.E.C. fictional team behind the "Sara Cladlow" story.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This entry is a duplicate of dc34-2026-echallengecoin.md (id dc34-2026-choose-your-own-charity-echallengecoin), which already has the full, verified research for this exact item (same aosc.cc/eccn2026 source, same maker, same 2026 eChallengeCoin/"Sara and the Missing Artifacts" game). Event corrected from other/2026 to dc34/2026 since the coin was made for DEF CON 34 and distributed there. Filled in the fields the two sources support; deferred to the canonical entry for anything not directly confirmed here (e.g. exact quantity split, donation-form details). No new images fetched since the canonical entry already carries the maker''s front/back photos.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/2026-echallengecoin-sara-and-the-missing-artifacts/
---

The 2026 eChallengeCoin, "Sara and the Missing Artifacts," is a brass, coin-shaped electronic badge from Bradán Lane STUDIO, made with the fictional T.E.C. team (Tod Troche, Lory Ester, and Sara Cladlow) for DEF CON 34. It is not sold; it is given as a thank-you to anyone who donates $100 or more to a youth-focused STEM education charity of their choosing, collected in person at the con or by U.S. mail. The maker planned a run of 40 brass units, with the first 20 struck from blanks manufactured by students in a local high school engineering program.

The coin is a small CircuitPython board built around an ATSAMD21G1A (Cortex-M0+) microcontroller. Its main feature is a new text adventure game, "Sara and the Missing Artifacts," played over a USB serial connection with no built-in display. It also works as a general CircuitPython dev board, with a large capacitive touch pad, three groups of NeoPixel LEDs around its perimeter, and a small speaker. It has no battery, functioning as an inert brass coin until connected over USB.

This entry duplicates `dc34-2026-choose-your-own-charity-echallengecoin`, which carries the fuller verified write-up (including CircuitPython board-registry confirmation and photos) for the same item pulled from a different row of the community sheet.
