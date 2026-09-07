---
title: DIY Badge
id: dc30-diy-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc30
year: 2022
makers:
- name: The Diana Initiative
  url: https://www.dianainitiative.org/
summary: A build-it-yourself electronic badge kit sold in the Diana Initiative's Maker Village during DEF CON 30 week, built around a Raspberry Pi Pico.
functions: 'A soldering project: attendees assemble an RP2040 board, a 0.96" OLED, and buttons (including one labeled "PEWPEW") onto a badge-shaped PCB, suggesting a small on-screen game once built.'
look:
  colors:
  - green
  - white
  shape: null
  themes:
  - learn to solder
  - kit
tech:
  mcu: RP2040
  leds: null
  display: 0.96" OLED
  connectivity: []
  battery: 3x AAA
  sao_version: null
get_one:
  price: $50
  price_usd: 50.0
  quantity: ''
  availability: sold_out
  availability_note: Eventbrite listing (accessed 2026-09-06) shows the event, held August 10-11, 2022, has ended; a note on the sheet said only 72 tickets were left as of 19 Jul 2022.
  distribution:
  - purchase
  - kit
  where: Sold as an Eventbrite ticket ("Diana Initiative DIY Electronic Badge Kit") redeemable in the Maker Village at The Westin Las Vegas during DEF CON 30 week.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.eventbrite.com/e/diana-initiative-diy-electronic-badge-kit-tickets-382680175707
  url: https://www.eventbrite.com/e/diana-initiative-diy-electronic-badge-kit-tickets-382680175707
  kind: store
images:
- file: assets/images/badges/dc30/diy-badge/70bcd7cec6.jpg
  source: "https://www.eventbrite.com/e/diana-initiative-diy-electronic-badge-kit-tickets-382680175707"
  credit: "Diana Initiative"
  caption: "Unassembled DIY badge kit: RP2040 (Raspberry Pi Pico), 0.96\" OLED, buttons labeled LEFT/RIGHT/PEWPEW, and AAA battery holder"
contact: {}
notes:
- Only 72 left as of 2022 CDT on 19Jul2022
status: listed
sources:
- kind: sheet
  event: dc30
  row: 27
  updated: '2022-07-19'
- kind: url
  url: https://www.eventbrite.com/e/diana-initiative-diy-electronic-badge-kit-tickets-382680175707
  title: Diana Initiative DIY Electronic Badge Kit
  accessed: '2026-09-06'
  note: Confirms price ($50), organizer (The Diana Initiative), venue/dates (Westin Las Vegas, Aug 10-11 2022), one-line description ("Assemble your own electronic badge in the maker village!"), and listing photo of the kit contents.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: >-
    No maker page, repo, or press coverage beyond the Eventbrite listing was found; the
    Diana Initiative's current website has no archived mention of the 2022 Maker Village
    or this kit. tech.mcu, tech.display, and tech.battery were read directly off the
    listing's own product photo (a Raspberry Pi Pico box, a badge-shaped PCB silkscreened
    "PROTOTYPE" with an OLED footprint and buttons marked LEFT/RIGHT/PEWPEW, and a 3xAAA
    holder), not from written specs, since none were published. No hardware/firmware
    files, LED info, or exact quantity were found. Title kept as given on the sheet
    (matches the event's own listing title); "kit" fits the type vocabulary better than
    "badge" since it was sold and assembled as a DIY build.
last_modified_date: '2026-09-06'
---

The Diana Initiative ran a Maker Village during DEF CON 30 week in August 2022 at the Westin Las Vegas, and sold a $50 ticket for a DIY electronic badge kit that attendees could solder together on site. Eventbrite's own description was just "Assemble your own electronic badge in the maker village!" with no maker credited beyond the Diana Initiative itself, and a community-sheet note recorded only 72 tickets left about three weeks before the event.

The listing's product photo is the only technical source found: it shows a Raspberry Pi Pico (RP2040) still boxed, a 0.96" OLED module, a handful of buttons and passives, a 3xAAA battery holder, and a badge-shaped PCB silkscreened "PROTOTYPE" with two joystick-style button clusters and pads labeled LEFT, RIGHT, and PEWPEW — suggesting the finished badge ran a simple game on the small screen. No schematic, firmware, or write-up of the finished build was located, so functions, LEDs, and design files are left blank rather than guessed.
