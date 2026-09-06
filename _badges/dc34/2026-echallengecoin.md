---
title: 2026 eChallengeCoin
id: dc34-2026-echallengecoin
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
  url: https://aosc.cc/
summary: A brass electronic coin badge running a text-adventure game, given to donors of DEF CON 34-year youth STEM charity drives rather than sold.
functions: 'Full Text Adventure Game - Sara and the Missing Artifacts, played over a Micro-USB serial connection; also a CircuitPython-compatible dev board with a touch pad and Neopixels when not running the game'
look:
  colors:
  - gold
  shape: circle
  themes:
  - coin
  - puzzle
  - charity
tech:
  mcu: ATSAMD21G1A (Cortex-M0+)
  leds:
    count: null
    type: Neopixel
    note: three groups of Neopixels around the coin's perimeter
  display: none
  connectivity:
  - usb
  battery: none (USB-powered when connected; passive coin otherwise)
  sao_version: none
get_one:
  price: 'not for sale: given for $100+ donations to youth STEM charities (2025 coin at $50+)'
  price_usd: null
  quantity: 40 brass coins (first 20 with student-manufactured brass blanks)
  availability: free
  distribution:
  - free_drop
  - charity
  where: Given in person at DEF CON 34 in Las Vegas or mailed to US donors, in exchange for a qualifying donation to youth STEM charities via the maker's online form.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: Runs CircuitPython; the underlying board ("Coin M0") has a public CircuitPython.org board page, but no schematic/firmware repo was found.
links:
- label: aosc.cc/cyoc.html
  url: https://aosc.cc/cyoc.html
  kind: store
- label: aosc.cc/eccn2026
  url: https://aosc.cc/eccn2026
  kind: video
- label: CircuitPython.org board page (Coin M0)
  url: https://circuitpython.org/board/bradanlanestudio_coin_m0/
  kind: doc
images:
  - file: assets/images/badges/dc34/2026-echallengecoin/70ad594ed4.jpg
    source: "https://aosc.cc/eccn2026"
    credit: "Bradán Lane STUDIO"
    caption: "Front face of the 2026 eChallengeCoin brass badge"
  - file: assets/images/badges/dc34/2026-echallengecoin/d5e7309bc6.jpg
    source: "https://aosc.cc/eccn2026"
    credit: "Bradán Lane STUDIO"
    caption: "Back of the 2026 eChallengeCoin showing the touch pad and Neopixels"
contact:
  discord: bradanlane
  emails:
  - bradanlane@outlook.com
  handles:
  - '@bradanlane'
notes: []
status: released
sources:
- kind: sheet
  event: dc34
  row: 17
  updated: 6/13/2026 6:13:57
  listing: New
- kind: url
  url: https://aosc.cc/eccn2026
  title: 2026 eChallengeCoin
  accessed: '2026-09-06'
  note: Primary source for description, features, MCU hint, quantity, and distribution terms.
- kind: url
  url: https://aosc.cc/cyoc.html
  title: eChallengeCoin donation/submission form
  accessed: '2026-09-06'
  note: Confirms the coin is a charity-donation reward, not sold, and gives pickup/mailing options and donation thresholds.
- kind: url
  url: https://circuitpython.org/board/bradanlanestudio_coin_m0/
  title: 'Bradán Lane STUDIO: Coin M0 - CircuitPython.org'
  accessed: '2026-09-06'
  note: Identifies the coin's MCU as an ATSAMD21G1A (Cortex-M0+, 48 MHz, 256KB flash / 32KB RAM).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: No GitHub repo, Hackaday.io project, or Gerber/schematic share was found for this specific coin, so make_your_own.open_source and file URLs are left empty. Exact Neopixel count and the touch pad's exact function beyond "custom projects" were not stated on the maker's page. This is a repeat/annual series (a 2025 eChallengeCoin exists per the same donation page); only the 2026 edition is covered by this entry.
last_modified_date: '2026-09-06'
---

The 2026 eChallengeCoin is a brass coin-shaped electronic badge made by Bradán Lane STUDIO as a thank-you gift for donors to youth STEM charities during DEF CON 34. Rather than being sold, it is given to anyone who donates $100 or more (a companion 2025-dated coin is available at the $50 tier, and donations can be combined to receive both), collected in person in Las Vegas or mailed to a US address. The maker planned a run of 40 coins, with the first 20 struck from student-manufactured brass blanks.

Functionally, the coin runs a self-contained text adventure game, "Sara and the Missing Artifacts," playable over a Micro-USB serial connection. Underneath the game it is a small CircuitPython-compatible development board (documented on CircuitPython.org as the "Coin M0"), built around a SAMD21-family ATSAMD21G1A Cortex-M0+ microcontroller, with three groups of Neopixel LEDs around its perimeter, a small speaker, and a large capacitive touch pad usable for other projects. It needs no battery: it functions as an inert coin when disconnected and comes alive over USB.

No hardware or firmware repository was found for this specific edition, so it is not confirmed to be open source; the CircuitPython board-support entry suggests the underlying platform is documented, but no schematic, Gerbers, or game source were located during this research pass.
