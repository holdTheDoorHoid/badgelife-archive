---
title: BSidesKC 2018
id: bsides-kansas-city-2018-bsideskc-2018
layout: badge
parent: BSides Kansas City 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-kansas-city-2018
year: 2018
makers:
- name: BadgePirates
  url: https://www.badgepirates.com/
summary: The electronic badge for the first BSidesKC (2018), an ATtiny85 board that charlieplexes 20 LEDs into a 4x5 grid to scroll text and run simple animations.
functions: Scrolls the text "BSIDES KC" and, when a jumper/pin is set, "SECKC"; otherwise cycles through animations (a race, a bounce, a falling effect, snow, and scan lines) across the LED grid at random.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: ATtiny85
  leds:
    count: 20
    type: charlieplexed
    note: 5 ATtiny85 pins charlieplexed to drive 20 LEDs (GREEN/ORANGE/WHITE/BLUE/YELLOW) arranged as a 4x5 grid, with per-LED fading by duty-cycle.
  display: LED matrix 4x5
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold/distributed at the BSidesKC 2018 conference (April 20-21, 2018, Cerner Innovations Campus, Kansas City, MO); BadgePirates' event-specific badges are typically only available at the event itself.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/BadgePiratesLLC/BSidesKC_2018
  eda_tool: null
links:
- label: github.com/BadgePiratesLLC/BSidesKC_2018
  url: https://github.com/BadgePiratesLLC/BSidesKC_2018
  kind: repo
- label: BadgePirates catalog entry
  url: https://docs.badgepirates.com/catalog/
  kind: doc
  archived: https://web.archive.org/web/20260910225903/https://docs.badgepirates.com/catalog/#help-us-fill-the-gaps
- label: BSidesKC 2018 - Badge Pirates - Electronic Badge Overview (YouTube)
  url: https://www.youtube.com/watch?v=siB8sA0lMDc
  kind: video
- label: Badge Pirates
  url: https://www.badgepirates.com/
  kind: website
  archived: https://web.archive.org/web/20260810184033/https://badgepirates.com/
images: []
contact: {}
notes:
- First public BSidesKC badge, listed in BadgePirates' full catalog. Found by the event-year sweep, task bsides-any.
- BadgePirates' own catalog (docs.badgepirates.com) titles this entry "BSidesKC 18" and calls it the "First BSidesKC badge in the public archive"; the maker's GitHub repo and conference talk both call it the BSidesKC 2018 badge, which this entry keeps as the title.
status: released
sources:
- kind: url
  url: https://github.com/BadgePiratesLLC/BSidesKC_2018
  title: BSidesKC 2018
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-any); event read as ''BSides Kansas City 2018''.'
- kind: url
  url: https://raw.githubusercontent.com/BadgePiratesLLC/BSidesKC_2018/master/PROGRAMMING.md
  title: BSidesKC_2018 PROGRAMMING.md
  accessed: '2026-09-10'
  note: Confirms ATtiny85 target, 3.3V AVR-ISP programming, four/many LEDs blink during bootloader burn.
- kind: url
  url: https://raw.githubusercontent.com/BadgePiratesLLC/BSidesKC_2018/master/bsides/bsides.ino
  title: BSidesKC_2018 firmware (bsides.ino)
  accessed: '2026-09-10'
  note: Confirms charlieplexed 20-LED 4x5 grid driven from 5 ATtiny85 pins, scrolling text strings, and random animation modes (race, bounce, fallingAnimation, snow, scanLines); a jumper pin selects the SECKC string.
- kind: url
  url: https://docs.badgepirates.com/catalog/
  title: Badge Catalog - BadgePirates Documents
  accessed: '2026-09-10'
  note: Lists this badge as "BSidesKC 18", "First BSidesKC badge in the public archive", linking the same GitHub repo.
  archived: https://web.archive.org/web/20260910225903/https://docs.badgepirates.com/catalog/#help-us-fill-the-gaps
- kind: url
  url: https://allbsides.com/talk/siB8sA0lMDc.html
  title: BSidesKC 2018 - Badge Pirates - Electronic Badge Overview
  accessed: '2026-09-10'
  note: Transcript of the BadgePirates conference talk about this badge; confirms AVR/ATtiny microcontroller choice, charlieplexing rationale, and CR2032 battery power; does not state price or quantity made.
- kind: url
  url: https://www.2018.bsideskc.org/
  title: BSidesKC 2018 event page
  accessed: '2026-09-10'
  note: Confirms event dates (April 20-21, 2018) and venue (Cerner Innovations Campus, Kansas City, MO).
research:
  status: verified
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Fact-check pass (2026-09-10): re-fetched every cited source directly. Firmware source (bsides.ino/bsides.h) and PROGRAMMING.md, read from the maker''s own repo, confirm ATtiny85 @ 8MHz, CR2032, the exact GREEN/ORANGE/WHITE/BLUE/YELLOW pin-color assignment, 20 LEDs charlieplexed on 5 pins in a 4x5 grid, the literal strings "BSIDES KC" and "SECKC" (macro SKCS), the six animation routines named, the jumper/pin-read logic selecting SECKC vs. the random mix, and that the repo contains only firmware (no schematic/PCB/BOM), supporting open_source=partial. GitHub tree listing confirms no hardware files exist. docs.badgepirates.com catalog text matches verbatim ("BSidesKC 18" / "First BSidesKC badge in the public archive"). The 2018.bsideskc.org event page confirms Apr 20-21, 2018 at Cerner Innovations Campus, KC, MO. The conference-talk transcript on allbsides.com is machine-generated and garbled on some words (e.g. renders the MCU name as "artemis" and the LED-count math awkwardly, though
    "25 minus 5 [pins]" does resolve to 20 LEDs) -- it is corroborating background only, and every fact actually placed in the entry is backed by the maker''s own repo/docs, not by parsing the garbled transcript. Price, quantity made, and current availability remain unstated in every source checked and are correctly left empty. No photo of the physical badge exists in any source found (only the event logo and GitHub''s generic repo card), so look.colors/shape/themes and images correctly remain empty.'
last_modified_date: '2026-09-10'
---

The BSidesKC 2018 badge was BadgePirates' first badge made for BSidesKC, the Kansas City regional security conference held April 20-21, 2018 at the Cerner Innovations Campus. The team wanted something "simple and quick to prototype" rather than a second full-scale badge, so they built it around a single ATtiny85 running at 8 MHz off a CR2032 coin cell, chosen for being cheap and simple to debug and program.

The badge charlieplexes 20 LEDs (in green, orange, white, blue, and yellow) from just 5 microcontroller pins, arranging them as a 4x5 grid that scrolls text and runs small animations. By default it randomly cycles between a race, a bounce, a falling effect, snow, and scan lines, and scrolls "BSIDES KC"; a solder-jumper/pin option switches it to scroll "SECKC" instead, tying the badge to the local SecKC hacker group that runs BSidesKC. Firmware is written in the Arduino IDE against the ATtiny board package, and BadgePirates published both the firmware source and a programming guide (AVR-ISP at 3.3V, not 5V) so owners could reflash it themselves; no hardware files (schematic, PCB, BOM) were published alongside it, so it is only partially open source.

No price, production quantity, or current availability were stated in any source found. BadgePirates' own badge catalog lists this as the first BSidesKC badge in their public archive, calling it "BSidesKC 18."

## Make your own

- Load the ATtiny board package into the Arduino IDE (`Additional Boards Manager URLs`: `https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json`).
- Select Board: ATtiny25/45/85, Processor: ATtiny85, Clock: Internal 8 MHz.
- Connect an AVR-ISP-compatible programmer (BadgePirates used a USBasp) at **3.3V**, not 5V.
- Burn the bootloader once via `Tools > Burn Bootloader`, then upload `bsides/bsides.ino` from the [firmware repo](https://github.com/BadgePiratesLLC/BSidesKC_2018).
