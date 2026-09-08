---
title: 503 Party Bike Badge
id: dc23-dc503-badge
layout: badge
parent: DC23
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc23
year: 2015
makers:
- name: securelyfitz (Joe Fitzpatrick)
  url: https://github.com/securelyfitz
summary: An ATtiny85-based donor badge for the DC503 party fund at DEF CON 23, shaped like two bicycle wheels that appear to spin using reverse-mount LEDs and capacitive touch controls on the handlebars and pedals.
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
  where: Given to donors of the DC503 party fund at DEF CON 23 in 2015; not sold commercially.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/securelyfitz/bikebadge/tree/master/hardware
  firmware_url: https://github.com/securelyfitz/bikebadge/tree/master/software
  eda_tool: Eagle
  fab_url: https://github.com/securelyfitz/bikebadge/tree/master/hardware/gerbers
  notes: Repo includes Eagle schematic/board files, custom library parts for the bike shape and LEDs, exported gerbers, and an Arduino sketch using Paul Stoffregen's CapacitiveSensor library.
links:
- label: blog.oshpark.com/tag/dc503
  url: https://blog.oshpark.com/tag/dc503/
  kind: fab
- label: github.com/securelyfitz/bikebadge
  url: https://github.com/securelyfitz/bikebadge
  kind: repo
images: []
contact: {}
notes:
- 'Sweep found this via blog.oshpark.com/tag/dc503, which is titled ''DC503 Badge'' and links this OSH Park tag; that tag page, though, actually documents a later, unrelated 2018 DEF CON 26 DC503 project (Nisha Kumar''s "Banglet"), not the 2015 bicycle badge described in the sweep''s own notes line. The bicycle badge itself (ATtiny85, 14 reverse-mount LEDs, capacitive pedal/brake controls) is confirmed instead by securelyfitz''s GitHub repo (github.com/securelyfitz/bikebadge), whose README dates it to the "503 party fund" in 2015 — DEF CON 23 year — matching the sweep''s description closely.'
- 'Duplicate of an existing entry, other-bike-badge (event: other), which already carries this same GitHub repo as its source and full detail (open-source hardware/firmware, gerbers, quantity/price not stated anywhere found). Title corrected from the sweep''s generic "DC503 Badge" to the maker-used project name "503 Party Bike Badge" (from the GitHub repo name/README), matching the other entry.'
- Could not find any stated quantity made or price; the sweep note's "100 boards" and "crowdfunded" framing was not corroborated by any source read (GitHub README says only that it was a badge for 503-party-fund donors in 2015).
- No photo of the physical badge was found; only a GitHub social-preview placeholder image and unrelated 2018 Banglet photos on the OSH Park tag page.
status: released
sources:
- kind: url
  url: https://blog.oshpark.com/tag/dc503/
  title: DC503 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc23-all); event read as ''dc23''. On inspection this page documents a different, later (2018) DC503 project, not the 2015 bike badge.'
- kind: url
  url: https://github.com/securelyfitz/bikebadge
  title: 'securelyfitz/bikebadge: hardware and software files for attiny-based bicycle badge'
  accessed: '2026-09-08'
  note: Maker's own repo; confirms the badge design, ATtiny85 chip, LED count/type, capacitive touch controls, 2015 date, and that hardware/firmware are open source.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core design facts confirmed by the maker''s own GitHub repo (high confidence for those). Quantity made, price, and the specific "crowdfunded"/"100 boards" claim from the original sweep note could not be corroborated by any source read, so those fields are left empty. This entry duplicates other-bike-badge (filed under event: other); the two should likely be merged by a human editor.'
last_modified_date: '2026-09-08'
---

This is an ATtiny85-based novelty badge made by securelyfitz (Joe Fitzpatrick) as a thank-you for donors to the DC503 party fund at DEF CON 23 in 2015. The board is shaped like two bicycle wheels, each ringed with reverse-mount LEDs; clever wiring lets a single ATtiny85 drive all 14 LEDs in phased pairs across just two GPIO pins, PWM-faking a spinning-wheel animation. Two capacitive-touch pads stand in for the handlebars and pedals — touching the "pedals" speeds the animation up, touching the "brakes" on the handlebars slows it down — so there are no physical buttons on the board at all. It runs on a single CR2032 coin cell.

The hardware (Eagle schematics, board files, and gerbers) and firmware (an Arduino sketch built on Paul Stoffregen's CapacitiveSensor library) are published on the maker's GitHub. No price or production quantity for the badge could be confirmed from available sources.

This entry duplicates another archive entry, `other-bike-badge`, filed under the "other" event since the original researcher didn't tie it to a specific year at the time; that entry carries the same design details and is a good candidate to merge with this one.
