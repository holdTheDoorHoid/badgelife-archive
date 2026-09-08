---
title: RoadSec Black Badge Customization
id: roadsec-2017-roadsec-black-badge-customization
layout: badge
parent: Roadsec 2017
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: roadsec-2017
year: 2017
makers:
- name: Londrina Hacker Club
summary: An Arduino-driven character-LCD modification added to a RoadSec Black Badge trophy device by Brazil's Londrina Hacker Club.
functions: Drives a 16x2-style character LCD with custom bitmap characters that animate scrolling text (the source spells out "JULIO", likely a name or in-joke) via a looping Arduino sketch.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: Arduino-compatible
  leds: null
  display: character LCD (LiquidCrystal library)
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
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/LondrinaHackerClub/RoadSecBlackBadge/blob/master/TETANTIVALOOPLCD.ino
  eda_tool: null
links:
- label: github.com/LondrinaHackerClub/RoadSecBlackBadge
  url: https://github.com/LondrinaHackerClub/RoadSecBlackBadge
  kind: repo
images:
  - file: assets/images/badges/roadsec-2017/roadsec-black-badge-customization/1684b13fbc.jpg
    source: "https://github.com/LondrinaHackerClub/RoadSecBlackBadge"
    credit: "Londrina Hacker Club"
    caption: "The modified RoadSec Black Badge with an added character LCD"
contact: {}
notes:
- Arduino/LCD hardware modification of RoadSec's Black Badge trophy device, built by Londrina Hacker Club for security events. Found by the event-year sweep, task con-ekoparty.
status: listed
sources:
- kind: url
  url: https://github.com/LondrinaHackerClub/RoadSecBlackBadge
  title: RoadSec Black Badge Customization
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''RoadSec''.'
- kind: url
  url: https://github.com/LondrinaHackerClub/RoadSecBlackBadge
  title: 'GitHub: LondrinaHackerClub/RoadSecBlackBadge'
  accessed: '2026-09-08'
  note: Confirmed repo contents (README, Arduino sketch TETANTIVALOOPLCD.ino, one photo dated January 2017); source of MCU/display and photo details.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-08'
  notes: Only source is the maker's own GitHub repo, a small one-off project (README, single Arduino sketch, single photo) with no further coverage found. No maker website, storefront, price, quantity, or distribution details exist anywhere. The sketch's own comment shows two different LiquidCrystal pin wirings ("PARA A BADGE"), suggesting the badge's wiring differs from the sketch's default test setup, but no schematic or hardware files were published, so make_your_own.open_source is 'partial' (firmware only). Repo has no releases/tags to pin an exact date beyond the January 2017 photo filename, consistent with the roadsec-2017 event id already on the entry.
last_modified_date: '2026-09-08'
---

Londrina Hacker Club, a Brazilian hacker/makerspace group, modified a RoadSec "Black Badge" trophy device by wiring in a character LCD driven by an Arduino-compatible microcontroller. The single public artifact is a GitHub repository holding a short README (in Portuguese: "Customization of the Black Badge (RoadSec) for security events"), one Arduino sketch, and one photo of the finished badge, dated January 2017.

The sketch (`TETANTIVALOOPLCD.ino`) uses the `LiquidCrystal` library and defines a set of custom 5x8 bitmap characters that assemble into scrolling large-format letters, spelling out what appears to be a name or greeting, looped continuously on the display. A code comment lists an alternate pin wiring "for the badge" different from the sketch's default test wiring, indicating the badge's actual LCD connection differs from how the sketch was originally developed and tested on a breadboard.

No storefront, pricing, quantity, or broader distribution information exists for this project; it reads as a one-off customization built and documented by a single club rather than a badge produced for wide distribution.

## Make your own

The Arduino sketch is published in the repo linked above. No schematic, wiring diagram, or bill of materials was published, so replicating the hardware side would require reverse-engineering the pin assignments from the sketch's comments and matching them to a standard Arduino-plus-character-LCD wiring.
