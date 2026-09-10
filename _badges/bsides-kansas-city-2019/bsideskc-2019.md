---
title: BSidesKC 2019 Shark Badge
id: bsides-kansas-city-2019-bsideskc-2019
layout: badge
parent: BSidesKC 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-kansas-city-2019
year: 2019
makers:
- name: BadgePirates
  url: https://github.com/BadgePiratesLLC
summary: The main conference ("Participant") badge for BSidesKC 2019, a shark-shaped ESP8266 PCB with an IR laser-tag game, a Baby Shark tune, and an SAO header.
functions: 'An IR-based "laser tag" battle game: a "pewpew" button fires an IR blast and counts shots fired at other badges; a piezo speaker plays the Baby Shark tune on power-up; a small vibrating disc motor; and a chase animation across onboard RGB LEDs.'
look:
  colors:
  - white
  - black
  - gold
  shape: shark
  themes:
  - animal
  - security
  - pirate
tech:
  mcu: ESP8266 (ESP-WROOM-02)
  leds:
    count: 3
    type: RGB (Adafruit NeoPixel)
    note: 'Driven via the Adafruit_NeoPixel library on pin 14; a separate Kids Badge variant in the same repo uses Charlieplexed LEDs instead.'
  display: none
  connectivity:
  - ir
  battery: null
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/BadgePiratesLLC/BSidesKC_2019
  firmware_url: https://github.com/BadgePiratesLLC/BSidesKC_2019
  eda_tool: null
links:
- label: github.com/BadgePiratesLLC/BSidesKC_2019
  url: https://github.com/BadgePiratesLLC/BSidesKC_2019
  kind: repo
images:
- file: assets/images/badges/bsides-kansas-city-2019/bsideskc-2019/b7a2607e78.jpg
  source: "https://github.com/BadgePiratesLLC/BSidesKC_2019"
  credit: "BadgePirates"
  caption: "Close-up of the BSidesKC 2019 shark badge PCB (Participant version) showing the SAO header and silkscreen"
contact: {}
notes:
- BSidesKC's 2019 electronic badge from BadgePirates' catalog. Found by the event-year sweep, task bsides-any.
- 'The sweep''s generic title "BSidesKC 2019" has been narrowed to "BSidesKC 2019 Shark Badge" (the maker''s repo calls it simply the shark-shaped conference/"Participant" badge, distinct from the "Kids Badge" variant in the same repo).'
status: released
sources:
- kind: url
  url: https://github.com/BadgePiratesLLC/BSidesKC_2019
  title: BSidesKC 2019
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides Kansas City 2019''.'
- kind: url
  url: https://github.com/BadgePiratesLLC/BSidesKC_2019
  title: BadgePiratesLLC/BSidesKC_2019 (README, source, gerbers, docs)
  accessed: '2026-09-10'
  note: 'Confirmed the badge exists (a photo in photos/ shows a populated "PARTICIPANT" shark PCB), read shark-badge/src/main.ino for MCU/features (ESP8266, NeoPixels, IR pewpew game, piezo Baby Shark tune, vibration motor), platformio.ini for the target chip, docs/ for the ESP-WROOM-02 datasheet, and gerber/ for the SAO/add-on boards. Repo is archived (read-only) as of 2021-09-28; dual-licensed CC-BY-4.0 (hardware) / MIT (software).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed via the maker''s own GitHub repo (source code, gerbers, docs, and a photo of the assembled "PARTICIPANT" badge). Price, quantity made, and distribution method (free vs. included in registration) are not stated anywhere in the repo, so get_one fields are left empty/unknown. SAO pin count (v1 vs v1.69bis) is inferred from a 4-pad schematic screenshot in photos/SAO_1.PNG, not from a written spec, so treat tech.sao_version as a reasonable read rather than certain. A second, related entry already exists for the "Kids Badge" variant documented in the same repo (id bsides-kansas-city-2019-bsides-kc-shark-laser-tag-badge-kids-badge); this entry covers the main "Participant"/conference badge instead, which uses NeoPixels + ESP8266 + IR rather than the Kids Badge''s Charlieplexed LEDs.'
last_modified_date: '2026-09-10'
---

BadgePirates (the crew behind SecKC's DEF CON badges) built the 2019 BSidesKC conference badge as a shark-shaped PCB around an ESP8266 (ESP-WROOM-02) module. The headline feature is an IR "laser tag" game: a front "pewpew" button fires an infrared blast that other badges can receive, with an interrupt-driven counter tracking shots fired. On power-up the badge plays the Baby Shark tune through a small piezo speaker, backed by a vibrating disc motor and a chase animation across three onboard RGB (NeoPixel) LEDs. The board also carries a 4-pin SAO header (labeled, in the maker's usual joke branding, a "Shitty Add-On" port).

The same repository documents a second, simpler "Kids Badge" for the event, built around a Charlieplexed-LED driver (`Chaplex`) rather than the NeoPixel/ESP8266 combination used here; that variant is cataloged separately in this archive. The repo also includes gerbers for a couple of small SAO/add-on boards (a bee-shaped SAO and WS2812/cap-touch add-ons) that appear to be extras from the same badge drop rather than part of the main shark board.

All hardware and firmware are published on GitHub under CC-BY-4.0 (hardware) and MIT (firmware) licenses, including multiple rounds of gerbers (prototype v0.3 through the final production run) and a bill of materials, though the repository itself was archived by its owner in September 2021. No price, production quantity, or distribution details (e.g., whether it came free with registration) are stated in the available documentation.
