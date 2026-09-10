---
title: 503 Party Bike Badge
id: other-bike-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2015
makers:
- name: securelyfitz
  url: https://github.com/securelyfitz
summary: An ATtiny85-based donor badge for the 503 party fund, shaped like two bicycle wheels that appear to spin using reverse-mount LEDs and capacitive touch controls on the handlebars and pedals.
functions: Two capacitive-touch pads (handlebars and pedals) let the wearer speed up or slow down an animated "spinning wheel" LED effect; braking on the handlebars slows the animation, pedaling speeds it up.
look:
  colors:
  - yellow
  shape: null
  themes:
  - vehicle
tech:
  mcu: ATtiny85
  leds:
    count: 14
    type: reverse-mount
    note: OSRAM reverse-gullwing yellow LEDs (LYT776), wired in opposite polarity pairs across just 2 GPIOs and driven with PWM to fake a rotating wheel.
  display: none
  connectivity: []
  inputs:
  - touch
  - capacitive
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to donors of the 503 party fund in 2015; not sold commercially.
make_your_own:
  open_source: true
  hardware_url: https://github.com/securelyfitz/bikebadge/tree/master/hardware
  firmware_url: https://github.com/securelyfitz/bikebadge/tree/master/software
  eda_tool: Eagle
  fab_url: https://github.com/securelyfitz/bikebadge/tree/master/hardware/gerbers
  notes: Repo includes Eagle schematic/board files, custom library parts for the bike shape and LEDs, exported gerbers, and an Arduino sketch using Paul Stoffregen's CapacitiveSensor library.
links:
- label: github.com/securelyfitz/bikebadge
  url: https://github.com/securelyfitz/bikebadge
  kind: repo
- label: blog.oshpark.com/tag/dc503
  url: https://blog.oshpark.com/tag/dc503/
  kind: fab
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- Sweep found this via blog.oshpark.com/tag/dc503, which is titled 'DC503 Badge' and links this OSH Park tag; that tag page, though, actually documents a later, unrelated 2018 DEF CON 26 DC503 project (Nisha Kumar's "Banglet"), not the 2015 bicycle badge described in the sweep's own notes line. The bicycle badge itself (ATtiny85, 14 reverse-mount LEDs, capacitive pedal/brake controls) is confirmed instead by securelyfitz's GitHub repo (github.com/securelyfitz/bikebadge), whose README dates it to the "503 party fund" in 2015 — DEF CON 23 year — matching the sweep's description closely.
- 'Duplicate of an existing entry, other-bike-badge (event: other), which already carries this same GitHub repo as its source and full detail (open-source hardware/firmware, gerbers, quantity/price not stated anywhere found). Title corrected from the sweep''s generic "DC503 Badge" to the maker-used project name "503 Party Bike Badge" (from the GitHub repo name/README), matching the other entry.'
- Could not find any stated quantity made or price; the sweep note's "100 boards" and "crowdfunded" framing was not corroborated by any source read (GitHub README says only that it was a badge for 503-party-fund donors in 2015).
- No photo of the physical badge was found; only a GitHub social-preview placeholder image and unrelated 2018 Banglet photos on the OSH Park tag page.
status: released
sources:
- kind: url
  url: https://github.com/securelyfitz/bikebadge
  title: Bike Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/securelyfitz/bikebadge/master/README.md
  title: 503 party bike badge - 2015 (README)
  accessed: '2026-09-07'
  note: Primary source for maker's description, hardware theory, BOM, MCU, LED count/type, capacitive sensor design, battery, and event/year (503 party fund, 2015).
- kind: url
  url: https://api.github.com/repos/securelyfitz/bikebadge/contents/hardware
  title: bikebadge repo hardware directory listing
  accessed: '2026-09-07'
  note: Confirmed Eagle (.sch/.brd) files and a gerbers folder are present; no photos of the assembled badge exist anywhere in the repo.
- kind: url
  url: https://blog.oshpark.com/tag/dc503/
  title: DC503 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc23-all); event read as ''dc23''. On inspection this page documents a different, later (2018) DC503 project, not the 2015 bike badge.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three cited sources (repo root, raw README.md, hardware directory listing) and confirmed every non-empty field and body sentence against them -- MCU, LED count/type/part number (LYT776), resistor values, battery, capacitive-touch design, Sparkfun TinyAVR programmer, CapacitiveSensor library, Eagle .sch/.brd/.lbr files, gerbers folder contents, software/ sketch folder, BOM cost ($2-5), and event/year (503 party fund, 2015). One clarification made: the body originally said the trick produces a "16-LED" effect; the README actually says the design was spec''d for 16 LEDs but the final board uses 14 (matching tech.leds.count) -- reworded to state both numbers so it does not read as contradicting the LED count. The badge was made for "the 503 party fund" (503.party) in 2015, a donor/party fundraiser rather than a specific hacker convention, so it does not map to any id in events.yml; left under "other". No photos of the physical badge exist
    in the repo (confirmed again), so images[] stays empty and look.shape stays null. Price, quantity made, and current availability are not stated anywhere in the sources; it reads as a one-time giveaway to donors rather than a sold item. Merged with duplicate entry ''503 Party Bike Badge'' (dc23-dc503-badge).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/dc23/dc503-badge/
model:
  file: assets/models/other/bike-badge.glb
  method: kicad
  source_file: bikebadge.brd
  generated: '2026-09-10'
  bytes: 125988
---

The Bike Badge is a 2015 electronic badge by securelyfitz, made as a thank-you for donors to "the 503 party fund" (503.party). It is built around a bare ATtiny85 microcontroller and 14 yellow OSRAM reverse-gullwing surface-mount LEDs arranged in two bicycle-wheel patterns, powered by a single CR2032 coin cell. Rather than a display or radio, its interactivity comes from two capacitive touch zones standing in for a bike's handlebars and pedals: touching the "pedals" speeds up an animated spinning-wheel LED effect, while touching the "handlebars" (braking) slows it down.

The clever part of the design, as documented by the maker, is squeezing a rotating-wheel LED effect (originally spec'd for 16 LEDs, trimmed to the final 14 for aesthetic reasons) out of only two GPIO pins on the tiny chip, which were needed elsewhere for the capacitive sensing. Opposite LED pairs are wired with reversed polarity across shared pins so that PWM duty cycles that sum to 100% light one LED while dimming its opposite, producing the illusion of a wheel spinning as the duty cycle sweeps. The firmware is a straightforward Arduino sketch, flashed via a Sparkfun TinyAVR programmer, that layers this PWM trick with Paul Stoffregen's CapacitiveSensor library for the touch inputs.

The project's GitHub repository is fully open: Eagle schematic and board files, custom library parts for the bike-wheel LED layout, exported gerbers, and the Arduino source are all included, with a bill of materials the maker estimated at $2-5 in quantity. No photos of an assembled unit, sales listing, or production-quantity figures could be found, so it reads as a small, one-off giveaway rather than a commercially distributed badge.

## Make your own

Hardware and firmware are both published in the repo. To build one: fabricate the board from the gerbers in `hardware/gerbers` (or open `bikebadge.sch`/`bikebadge.brd` in Eagle), populate the ATtiny85, 14 reverse-gullwing LEDs, matching 200-ohm resistors, two 10M-ohm resistors for the capacitive sense lines, and a CR2032 holder, then flash the Arduino sketch in `software/` using an AVR programmer such as the Sparkfun TinyAVR Programmer.

## Notes merged from the duplicate entry "503 Party Bike Badge"

This is an ATtiny85-based novelty badge made by securelyfitz (Joe Fitzpatrick) as a thank-you for donors to the DC503 party fund at DEF CON 23 in 2015. The board is shaped like two bicycle wheels, each ringed with reverse-mount LEDs; clever wiring lets a single ATtiny85 drive all 14 LEDs in phased pairs across just two GPIO pins, PWM-faking a spinning-wheel animation. Two capacitive-touch pads stand in for the handlebars and pedals — touching the "pedals" speeds the animation up, touching the "brakes" on the handlebars slows it down — so there are no physical buttons on the board at all. It runs on a single CR2032 coin cell.

The hardware (Eagle schematics, board files, and gerbers) and firmware (an Arduino sketch built on Paul Stoffregen's CapacitiveSensor library) are published on the maker's GitHub. No price or production quantity for the badge could be confirmed from available sources.

This entry duplicates another archive entry, `other-bike-badge`, filed under the "other" event since the original researcher didn't tie it to a specific year at the time; that entry carries the same design details and is a good candidate to merge with this one.
