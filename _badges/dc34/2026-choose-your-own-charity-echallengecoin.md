---
title: 2026 “Choose Your Own Charity” eChallengeCoin
id: dc34-2026-choose-your-own-charity-echallengecoin
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
  url: https://aosc.cc/eccn2026
summary: A brass challenge-coin-shaped electronic badge that runs a text adventure game, "Sara and the Missing Artifacts," over a USB serial terminal, given as a thank-you for a $100+ donation to a youth STEM charity of the recipient's choosing.
functions: All new text adventure game, "Sara and the Missing Artifacts", played over a USB serial terminal; also usable as a general CircuitPython dev board via its capacitive touch pad, NeoPixels, and speaker
look:
  colors:
  - copper
  shape: coin
  themes:
  - coin
  - charity
  - puzzle
  - learn to solder
tech:
  mcu: ATSAMD21G1A (Cortex-M0+)
  leds:
    count: null
    type: NeoPixel
    note: three groups of NeoPixels around the coin's perimeter
  display: none
  connectivity:
  - usb
  inputs:
  - touch
  battery: none (USB powered when connected; functions as a plain brass coin when disconnected)
  sao_version: none
get_one:
  price: proof of a $100+ donation to a youth STEM charity of the person's choosing
  price_usd: null
  quantity: '40 brass units planned (first 20 recipients get blanks machined by local high school engineering students)'
  availability: limited
  distribution:
  - free_drop
  - contest
  where: 'Free gift for donating $100 or more to a youth-focused STEM education charity of your choice; claimed in person at DEF CON or by U.S. mail after submitting proof of donation via an online form, or by contacting the maker on X/Twitter, Bluesky, or Discord'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://circuitpython.org/board/bradanlanestudio_coin_m0/
  eda_tool: null
links:
- label: aosc.cc/eccn2026
  url: https://aosc.cc/eccn2026
  kind: store
- label: circuitpython.org board page
  url: https://circuitpython.org/board/bradanlanestudio_coin_m0/
  kind: doc
images:
- file: assets/images/badges/dc34/2026-choose-your-own-charity-echallengecoin/70ad594ed4.jpg
  source: "https://aosc.cc/eccn2026"
  credit: "Bradán Lane STUDIO"
  caption: "Front face of the 2026 eChallengeCoin brass coin"
- file: assets/images/badges/dc34/2026-choose-your-own-charity-echallengecoin/d5e7309bc6.jpg
  source: "https://aosc.cc/eccn2026"
  credit: "Bradán Lane STUDIO"
  caption: "Back face of the 2026 eChallengeCoin brass coin"
contact:
  discord: bradanlane
  emails:
  - bradanlane@outlook.com
notes: []
status: listed
sources:
- kind: sheet
  event: dc34
  row: 2
  updated: 5/25/2026 12:01:01
  listing: New
- kind: url
  url: https://aosc.cc/eccn2026
  title: "2026 eChallengeCoin — AoSC"
  accessed: '2026-09-06'
  note: Primary source for description, features, donation-based distribution, quantity (40 brass units, first 20 as student-machined blanks), and photos.
- kind: url
  url: https://circuitpython.org/board/bradanlanestudio_coin_m0/
  title: "Bradán Lane STUDIO Coin M0 — CircuitPython board page"
  accessed: '2026-09-06'
  note: Confirms MCU (ATSAMD21G1A / SAMD21, Cortex-M0+), CircuitPython support, NeoPixels, touch pads, and speaker.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'This entry duplicates dc34-2026-echallengecoin (same item, same maker, same aosc.cc links, from a different sheet row) — see other_items_found in the research report. Minor source disagreement: aosc.cc/eccn2026 text mentions "micro-USB serial connectivity" while the circuitpython.org board page lists native USB-C; left tech.connectivity as generic "usb" rather than guessing the connector. LED count not stated numerically ("three groups of Neopixels"), so tech.leds.count left null. price_usd left null since the donation is a minimum, not a fixed price.'
last_modified_date: '2026-09-06'
---

The 2026 eChallengeCoin, "Choose Your Own Charity," is a brass, coin-shaped electronic badge from Bradán Lane STUDIO made with T.E.C. (Tod Troche, Lory Ester, and Sara Cladlow) for DEF CON 34. Rather than being sold, it is given away as a thank-you to anyone who donates $100 or more to a youth-focused STEM education charity of their own choosing, with proof of donation exchanged for the coin either in person at the con or by U.S. mail. The maker planned a run of 40 brass units, with the first 20 recipients receiving blanks machined by local high school engineering students before final assembly.

Functionally the coin is a small CircuitPython board built around a SAMD21 (Cortex-M0+) microcontroller. Its headline feature is a new text adventure game, "Sara and the Missing Artifacts," played over a USB serial terminal connection — no display is built in. Beyond the game, the coin doubles as a general-purpose dev board, with a large capacitive touch pad, three groups of NeoPixel LEDs around its perimeter, and a small speaker. It needs no battery: unplugged, it functions as a genuine brass coin, and it only powers up when connected over USB.

The board is registered with the official CircuitPython project (as "bradanlanestudio_coin_m0"), so firmware support is public even though no separate hardware/Gerber repository was found. This entry is a duplicate of another sheet import for the same item (`dc34-2026-echallengecoin`), pulled from a different row of the community badge sheet.
