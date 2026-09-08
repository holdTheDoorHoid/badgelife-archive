---
title: Skully
id: dc30-skully-sao
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Nerfhammer
  url: https://www.tindie.com/stores/nerfhammer/
summary: A skull-shaped wearable badge with amber LEDs that simulate a flame flickering up from behind the skull, worn on a lapel pin rather than a lanyard.
functions: An onboard accelerometer keeps the simulated flame oriented toward the bottom of the badge no matter how it is worn or tilted. The flame pattern fades out over about a minute when the badge sits still, dropping it into a low-power sleep mode, then wakes and relights automatically when it senses motion again.
look:
  colors:
  - black
  - gold
  shape: skull
  themes:
  - skull
  - horror
tech:
  mcu: ATMega168
  leds: null
  display: none
  connectivity: []
  battery: CR2032
  sao_version: null
get_one:
  price: $30
  price_usd: 30
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold by Nerfhammer through their Tindie store; also handed out/sold in person at DEF CON events.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  kind: store
- label: tindie.com/products/nerfhammer/skully
  url: https://www.tindie.com/products/nerfhammer/skully/
  kind: store
images:
  - file: assets/images/badges/dc30/skully-sao/be63e5a2c6.jpg
    source: "https://www.tindie.com/products/nerfhammer/skully/"
    credit: "Nerfhammer"
    caption: "Skully SAO, skull-shaped badge with amber backlit flame LEDs"
contact: {}
notes:
- Silk-screened SAO with an accelerometer that makes the LEDs flicker out like a candle, sold by Nerfhammer at DEF CON 30. Found by the event-year sweep, task dc30-saos.
- 'Sweep called it "Skully SAO"; Nerfhammer''s own Tindie listing just calls it "Skully" — title corrected to match.'
status: released
sources:
- kind: url
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  title: Skully SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc30-saos); event read as ''dc30''.'
- kind: url
  url: https://www.tindie.com/products/nerfhammer/skully/
  title: Skully by nerfhammer on Tindie
  accessed: '2026-09-08'
  note: Maker's own product listing; source for description, price, MCU, accelerometer, battery, physical dimensions, and pin-back mounting.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'The Tindie blog post lists Skully among the popular items Nerfhammer sold at DEF CON 30 (2022), which is why this entry sits under dc30. However Nerfhammer''s own Tindie listing for Skully carries product photos dated September 2019 (just after DEF CON 27) and customer reviews spanning 2020-2022, so it reads as a standing item sold across several years/cons rather than something made specifically for DC30 — I did not find a source stating an exact debut year, so I left event as dc30 (the year this archive''s source names) rather than guessing an earlier one. No SAO connector version, LED count/type, or open-source design files are given anywhere I found; it may not use a standard SAO header at all since it runs on its own CR2032 and has a bar pin for lapel wear rather than badge-mount pins. Listing is currently marked as the seller on a break (returning ~2026-09-15) with no live stock count, so availability is left unknown rather than sold_out.'
last_modified_date: '2026-09-08'
---

Skully is a skull-shaped wearable made by Nerfhammer, sold through their Tindie store and also carried to DEF CON in person — the Tindie blog's 2022 recap of vendor tables at DEF CON 30 names it among Nerfhammer's popular items that year. The badge is roughly 2.3 by 2.3 inches, built around an ATMega168 with an LIS3DH accelerometer, and wears on a lapel via a bar pin rather than a lanyard clip.

Its signature feature is a set of amber LEDs behind the skull that simulate a flickering flame, an effect the maker says shows up best in low light. The accelerometer keeps the simulated flame oriented downward regardless of how the badge is tilted or worn, and the flame gradually fades over about a minute of stillness before the board sleeps, waking and relighting itself as soon as it detects motion again. It runs on a single CR2032 coin cell and ships fully assembled.

As of research, the Tindie listing shows the seller on a break until mid-September 2026 with no open stock, so current availability could not be confirmed one way or the other.
