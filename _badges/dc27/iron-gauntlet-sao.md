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
functions: Lights up the six Infinity Stones using seven side-view LEDs (yellow used two LEDs to match the others' glow distance); no interactivity beyond illumination.
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
  display: none
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
  availability_note: Bundled exclusively with the Arc Badge, which its Tindie listing marks as its final, now sold-out run (checked 2026-09-07).
make_your_own:
  open_source: partial
  hardware_url: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  firmware_url: null
  gerbers_url: https://hackaday.io/project/165320-arc-badge-dc27-indie-badge
  eda_tool: KiCad
  notes: The project page offers a KiCad footprint library for the 1204 side-view LEDs (1204_SVLED.zip); full gerbers/schematics were not found published.
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
- label: hackaday.io/hacker/308303-twinkletwinkie
  url: https://hackaday.io/hacker/308303-twinkletwinkie
  kind: hackaday
- label: Arc Badge - DC27 Indie Badge (Tindie)
  url: https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
  kind: store
  archived: https://web.archive.org/web/20260510025611/https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
images:
- file: assets/images/badges/dc27/iron-gauntlet-sao/0506da0c77.jpg
  source: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  credit: TwinkleTwinkie
  caption: The Iron Gauntlet SAO
- file: assets/images/badges/dc27/iron-gauntlet-sao/725f969f69.jpg
  source: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  credit: TwinkleTwinkie
  caption: Iron Gauntlet SAO detail, showing the side-view LEDs behind hot-glue diffusers
- file: assets/images/badges/dc27/iron-gauntlet-sao/0506da0c77.jpg
  source: https://hackaday.io/project/165322-iron-gauntlet-dc27-sao
  credit: TwinkleTwinkie
  caption: The Iron Gauntlet SAO, a DEF CON 27 accessory shaped like Marvel's Infinity Gauntlet
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
- kind: url
  url: https://hackaday.io/project/165322/files
  title: Files | Iron Gauntlet - DC27 SAO
  accessed: '2026-09-07'
  note: Only a KiCad footprint library for the 1204 side-view LEDs is published; no gerbers/schematics/license found.
- kind: url
  url: https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
  title: Arc Badge - DC27 Indie Badge (Tindie)
  accessed: '2026-09-07'
  note: Confirms the SAO was bundled exclusively with the Arc Badge (not sold separately), and that the Arc Badge's final run is sold out.
  archived: https://web.archive.org/web/20260510025611/https://www.tindie.com/products/twinkletwinkie/arc-badge-dc27-indie-badge/
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-read both Hackaday.io project pages directly, including the SAO''s full component list and the Arc Badge page''s file list. Corrected the LED color note (the 7th LED is blue, per the project''s component list, not an unspecified "one more"), and corrected the body/Make-your-own text, which had wrongly said the corrected SAO Gerbers were never released — they were, in a second/final-run zip filed among the companion Arc Badge project''s downloads rather than on the SAO''s own page. No page states a build quantity for the SAO specifically (only the 220-unit badge run it shipped with) or a standalone price, since it was never sold separately. The SAO itself has no MCU — it is a passive LED add-on lit by the host Arc Badge. One design quirk confirmed on the maker''s page: an RGB LED originally planned for the purple stone was mis-wired (47-ohm resistor on the wrong leg) and swapped for a single-color pink LED as a fix. Both saved images were confirmed
    to appear on the SAO''s Hackaday.io page. All remaining non-empty fields and sentences checked out against the two cited maker pages. Merged with duplicate entry ''Iron Gauntlet'' (dc27-dc27-iron-gauntlet-sao).'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc27/iron-gauntlet-sao.glb
  method: gerber
  source_file: Iron_Gauntlet_JLC-20191202-1359.zip
  generated: '2026-09-07'
  bytes: 252028
  size_mm:
  - 55.0
  - 69.0
redirect_from:
- /badges/dc27/dc27-iron-gauntlet-sao/
---

The Iron Gauntlet is a Simple Add-On built by TwinkleTwinkie exclusively for the DEF CON 27 Arc Badge, a two-person indie badge project with fellow maker Wire. Styled "gold on red with a splash of infinite cosmic power," it uses seven 1204-package side-view LEDs — one each for five of the Infinity Stones, two for the yellow stone, which needed the extra LED to glow far enough to read — each seated behind a hand-applied hot-glue diffuser to soften and spread the light. It carries no microcontroller of its own; power and control come from the host badge, which has two SAO headers in total.

The SAO was never sold on its own. It came bundled with the Arc Badge, an Arc Reactor-styled prop badge that ran on 2xAA batteries and defaulted to a blue Arc Reactor lighting pattern, sold through TwinkleTwinkie's Tindie store for $90 plus $10 USPS Priority shipping in a run of 200 units for sale plus 20 more set aside for donations and trades. The maker later released the badge's KiCad design files, parts list, and PIC16F15344 firmware, along with a downloadable KiCad footprint for the 1204 side-view LED package. The corrected Iron Gauntlet layout TwinkleTwinkie promised after the resistor-placement error was released too, as Gerbers for the SAO's second and final run — filed among the Arc Badge project's downloads rather than on the SAO's own page.

## Make your own

The Iron Gauntlet's own Hackaday.io page offers a standalone KiCad footprint for the 1204 side-view LED package. The corrected Gerbers for the SAO's final revision — built from 1204 side-view LEDs, appropriately-valued 0805 resistors, and a 2x3 male pin header — were released later and are filed among the companion Arc Badge project's downloads, which also carries the full KiCad source, a parts list, and the PIC16F15344 firmware for the badge that drives it.

## Notes merged from the duplicate entry "Iron Gauntlet"

The Iron Gauntlet is a DEF CON 27 (2019) SAO by TwinkleTwinkie, shaped after Marvel's Infinity Gauntlet. It uses seven side-view LEDs in the 1204 package to stand in for the six Infinity Stones — yellow needed two LEDs to match the glow distance of the others — with the light diffused through a layer of hot glue rather than a milled or printed lens. The maker had originally planned an RGB LED to render purple, but a resistor placed on the wrong side of the LED kept that color from working, so a single pink LED was swapped in as a fix; the project notes a future revision was meant to correct it.

The SAO was never sold on its own. It shipped exclusively bundled with TwinkleTwinkie's Arc Badge, the maker's DC27 indie badge, sold through Tindie together with a lanyard and batteries. The Tindie listing describes that run as final, and as of this check the listing shows it sold out. A KiCad footprint library for the 1204 side-view LEDs is published on the project's Hackaday.io page, but no full gerber set, schematic, or firmware was found.
