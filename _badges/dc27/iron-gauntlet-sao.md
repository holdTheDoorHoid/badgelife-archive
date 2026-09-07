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
    note: 1204-package side-view LEDs (2 yellow, 1 red, 1 pink, 1 orange, 1 green, 1 blue) mounted behind hot-glue diffusers to represent the six Infinity Stones; the yellow stone uses two LEDs because a single one did not glow far enough. Passive SAO with no microcontroller of its own — it is driven by the host badge.
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
  gerbers_url: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
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
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-read both Hackaday.io project pages directly, including the SAO''s full component list and the Arc Badge page''s file list. Corrected the LED color note (the 7th LED is blue, per the project''s component list, not an unspecified "one more"), and corrected the body/Make-your-own text, which had wrongly said the corrected SAO Gerbers were never released — they were, in a second/final-run zip filed among the companion Arc Badge project''s downloads rather than on the SAO''s own page. No page states a build quantity for the SAO specifically (only the 220-unit badge run it shipped with) or a standalone price, since it was never sold separately. The SAO itself has no MCU — it is a passive LED add-on lit by the host Arc Badge. One design quirk confirmed on the maker''s page: an RGB LED originally planned for the purple stone was mis-wired (47-ohm resistor on the wrong leg) and swapped for a single-color pink LED as a fix. Both saved images were confirmed to appear on the SAO''s Hackaday.io page. All remaining non-empty fields and sentences checked out against the two cited maker pages.'
last_modified_date: '2026-09-07'
---

The Iron Gauntlet is a Simple Add-On built by TwinkleTwinkie exclusively for the DEF CON 27 Arc Badge, a two-person indie badge project with fellow maker Wire. Styled "gold on red with a splash of infinite cosmic power," it uses seven 1204-package side-view LEDs — one each for five of the Infinity Stones, two for the yellow stone, which needed the extra LED to glow far enough to read — each seated behind a hand-applied hot-glue diffuser to soften and spread the light. It carries no microcontroller of its own; power and control come from the host badge, which has two SAO headers in total.

The SAO was never sold on its own. It came bundled with the Arc Badge, an Arc Reactor-styled prop badge that ran on 2xAA batteries and defaulted to a blue Arc Reactor lighting pattern, sold through TwinkleTwinkie's Tindie store for $90 plus $10 USPS Priority shipping in a run of 200 units for sale plus 20 more set aside for donations and trades. The maker later released the badge's KiCad design files, parts list, and PIC16F15344 firmware, along with a downloadable KiCad footprint for the 1204 side-view LED package. The corrected Iron Gauntlet layout TwinkleTwinkie promised after the resistor-placement error was released too, as Gerbers for the SAO's second and final run — filed among the Arc Badge project's downloads rather than on the SAO's own page.

## Make your own

The Iron Gauntlet's own Hackaday.io page offers a standalone KiCad footprint for the 1204 side-view LED package. The corrected Gerbers for the SAO's final revision — built from 1204 side-view LEDs, appropriately-valued 0805 resistors, and a 2x3 male pin header — were released later and are filed among the companion Arc Badge project's downloads, which also carries the full KiCad source, a parts list, and the PIC16F15344 firmware for the badge that drives it.
