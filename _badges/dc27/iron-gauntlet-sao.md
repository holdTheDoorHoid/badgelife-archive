---
title: Iron Gauntlet
id: dc27-iron-gauntlet-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: TwinkleTwinkie
  url: https://hackaday.io/twinkletwinkie
summary: A badge-exclusive SAO that shipped with the DEF CON 27 Arc Badge, using seven side-view LEDs (two for the yellow stone) behind a hot-glue diffuser to represent the six Infinity Stones.
functions: ''
look:
  colors:
  - gold
  - red
  shape: null
  themes:
  - movie
  - pop culture
tech:
  mcu: none
  leds:
    count: 7
    type: reverse-mount
    note: 1204-package side-view LEDs (2 yellow, 1 red, 1 pink, 1 orange, 1 green, plus one more) mounted behind hot-glue diffusers to represent the six Infinity Stones; the yellow stone uses two LEDs because a single one did not glow far enough. Passive SAO with no microcontroller of its own — it is driven by the host badge.
  display: null
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution:
  - purchase
  where: Included only with the Arc Badge (TwinkleTwinkie and Wire's DEF CON 27 indie badge), sold on Tindie for $90 plus $10 shipping; not sold separately.
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/165320-arc-badge-dc27-indie-badge
  url: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260523064150/https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
- label: hackaday.io/project/165322-iron-gauntlet-dc27-sao
  url: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  kind: hackaday
- label: Tindie - TwinkleTwinkie store
  url: https://www.tindie.com/stores/twinkletwinkie/
  kind: store
  archived: https://web.archive.org/web/20260503111119/https://www.tindie.com/stores/twinkletwinkie/
images:
- file: assets/images/badges/dc27/iron-gauntlet-sao/0506da0c77.jpg
  source: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  credit: TwinkleTwinkie
  caption: The Iron Gauntlet SAO
- file: assets/images/badges/dc27/iron-gauntlet-sao/725f969f69.jpg
  source: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  credit: TwinkleTwinkie
  caption: Iron Gauntlet SAO detail, showing the side-view LEDs behind hot-glue diffusers
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
  title: Arc Badge - DC27 Indie Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260523064150/https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
- kind: url
  url: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  title: Iron Gauntlet - DC27 SAO
  accessed: '2026-09-07'
  note: Maker's own project page for the SAO — LED layout, hot-glue diffuser technique, the yellow-stone dual-LED workaround, and a KiCad footprint download for the 1204 side-view LED package.
- kind: url
  url: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
  title: Arc Badge - DC27 Indie Badge
  accessed: '2026-09-07'
  note: Confirms the SAO shipped exclusively with the Arc Badge (200 units for sale plus 20 for donation/trade at $90 + $10 shipping on Tindie), and that the badge/SAO combo's Gerbers, KiCad source, and PIC16F15344 firmware were released.
  archived: https://web.archive.org/web/20260523064150/https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io pages confirm design and distribution, but no page states a build quantity for the SAO specifically (only the 220-unit badge run it shipped with) or a standalone price, since it was never sold separately. The SAO itself has no MCU — it is a passive LED add-on lit by the host Arc Badge. One design quirk noted by the maker: an RGB LED originally planned for the purple stone was mis-wired (47-ohm resistor on the wrong leg) and swapped for a single-color pink LED as a fix.'
last_modified_date: '2026-09-07'
---

The Iron Gauntlet is a Simple Add-On built by TwinkleTwinkie exclusively for the DEF CON 27 Arc Badge, a two-person indie badge project with fellow maker Wire. Styled "gold on red with a splash of infinite cosmic power," it uses seven 1204-package side-view LEDs — one each for five of the Infinity Stones, two for the yellow stone, which needed the extra LED to glow far enough to read — each seated behind a hand-applied hot-glue diffuser to soften and spread the light. It carries no microcontroller of its own; power and control come from the host badge's two SAO headers.

The SAO was never sold on its own. It came bundled with the Arc Badge, an Arc Reactor-styled prop badge that ran on 2xAA batteries and defaulted to a blue Arc Reactor lighting pattern, sold through TwinkleTwinkie's Tindie store for $90 plus $10 USPS Priority shipping in a run of 200 units for sale plus 20 more set aside for donations and trades. The maker later released the badge and SAO's KiCad design files, Gerbers, and PIC16F15344 firmware for the badge, along with a downloadable KiCad footprint for the 1204 side-view LED package, though the release did not include a corrected SAO layout that TwinkleTwinkie mentioned planning after a resistor-placement error had defeated the intended RGB LED for the purple stone.

## Make your own

The Iron Gauntlet's project page on Hackaday.io provides Gerber files and a bill of materials (1204 side-view LEDs, 0805 resistors, and a 2x3 male pin header for the SAO connector), plus a standalone KiCad footprint download for the 1204 LED package. The companion Arc Badge project page hosts the full KiCad source and PIC16F15344 firmware for the badge that drives it.
