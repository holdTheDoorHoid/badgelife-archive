---
title: Cereal Booper
id: dc30-cereal-booper
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: DEFCON Furs
  url: https://dcfurs.com/
summary: DEFCON Furs' own electronic PCB badge for DEF CON 30, built around an RP2040 running MicroPython, with touch points and a shitty add-on (SAO) port.
functions: Touch-point interaction driven by MicroPython on the RP2040; drives an onboard LED matrix through an IS31FL3737 driver chip; carries a #badgelife SAO port so other add-ons can plug into it.
look:
  colors: []
  shape: null
  themes:
  - movie
tech:
  mcu: RP2040
  leds:
    count: null
    type: discrete
    note: Driven by an IS31FL3737 LED matrix driver chip (per the released schematic); exact LED count not stated.
  display: none
  connectivity: []
  inputs:
  - touch
  battery: null
  sao_version: null
  sao_ports: 1
get_one:
  price: $125/$150
  price_usd: 125.0
  quantity: ''
  availability: sold_out
  availability_note: The Gumroad bundle listing was marked sold out, with remaining stock reserved for in-person pickup at DEF CON 30 (checked 2026-09-06).
  distribution:
  - purchase
  - free_drop
  where: 'Sold as a $150 donation bundle at donate.defconfurs.org (Gumroad): one blank/unpopulated PCB badge (with 2022 DEFCON Furs Suite access) picked up in person at DEF CON 30, plus one fully-assembled badge shipped afterward in October 2022.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/defconfurs/dcfurs-badge-dc30
  firmware_url: https://github.com/defconfurs/dcfurs-badge-dc30/tree/main/builds
  gerbers_url: null
  bom_url: https://docs.google.com/spreadsheets/d/1ubZ6uMp17yrBXjzQ3mNF3NKE6toNoUMcJH_Sa5_5ocY/edit?usp=sharing
  eda_tool: null
  license: null
  fab_url: null
  notes: 'Schematic is a PDF (DCF30BadgeSchematic.pdf), not source CAD files; firmware is published as compiled .uf2 builds (OSD.ino.uf2 test firmware and DCFurs30_Rev1.uf2 initial release) plus an Arduino library for the LED driver. No explicit license found in the repo.'
links:
- label: donate.defconfurs.org/l/2022-badge-bundle
  url: https://donate.defconfurs.org/l/2022-badge-bundle
  kind: website
- label: defconfurs/dcfurs-badge-dc30 (GitHub)
  url: https://github.com/defconfurs/dcfurs-badge-dc30
  kind: repo
- label: DC30 Badge Bill of Materials (Google Sheets)
  url: https://docs.google.com/spreadsheets/d/1ubZ6uMp17yrBXjzQ3mNF3NKE6toNoUMcJH_Sa5_5ocY/edit?usp=sharing
  kind: doc
images: []
contact: {}
notes:
- Two different options explained on their site
status: released
sources:
- kind: sheet
  event: dc30
  row: 12
  updated: '2022-07-25'
- kind: url
  url: https://donate.defconfurs.org/l/2022-badge-bundle
  title: 'DEFCON Furs 2022 Badge: Cereal Booper - Badge Bundle (Gumroad)'
  accessed: '2026-09-06'
  note: Maker's own listing; confirms name, RP2040/MicroPython/touch/SAO description, bundle contents, $150 price, sold-out status, and shipping timeline.
- kind: url
  url: https://github.com/defconfurs/dcfurs-badge-dc30
  title: defconfurs/dcfurs-badge-dc30 (GitHub)
  accessed: '2026-09-06'
  note: DEFCON Furs' own 2022 badge repo; schematic PDF, BOM link, and firmware .uf2 builds; identifies the IS31FL3737 LED driver.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: 'Core facts (RP2040 MCU, MicroPython, touch points, SAO port, price, sold-out status) come from the maker''s own Gumroad listing. The GitHub repo (defconfurs/dcfurs-badge-dc30) is the same org''s 2022 badge project and matches on year, LED driver, and UF2 (RP2040 bootloader) firmware format, but its README/commit history never uses the "Cereal Booper" name itself, so the repo-to-name match is inferred rather than stated outright. LED count, exact colors/shape, and a confirmed SAO header version were not stated anywhere found. No photo of the assembled badge itself was found within the search budget; the only image on the Gumroad listing is a promotional teaser graphic with the badge shape deliberately blurred out, so no image was saved (a logo/mascot illustration, not the item). The $125 half of the sheet''s "$125/$150" price note was not independently confirmed; only the $150 bundle price was verified on Gumroad.'
last_modified_date: '2026-09-06'
---

DEFCON Furs, the furry-community suite/village group at DEF CON, designed the Cereal Booper as their own contribution to the badgelife scene for DEF CON 30 (2022), themed around that year's suite theme of "Hackers" and named after the film's "Cereal Killer" character. It's a proper electronic PCB badge: an RP2040 microcontroller running MicroPython scripting, touch points for interaction, and an IS31FL3737 chip driving its LEDs, plus a #badgelife-standard SAO add-on port so it can host other people's add-ons.

DEFCON Furs sold it through a $150 Gumroad "donation" bundle that combined a blank/unpopulated PCB (which doubled as the ticket into their DEF CON 30 suite events and open bar) with a fully-assembled badge shipped out after the con in October 2022. The bundle sold out, with the maker noting any remaining blanks would only be available in person at DEF CON. Owning the badge did not substitute for an actual DEF CON badge.

True to badgelife tradition, DEFCON Furs published the badge's schematic, bill of materials, and compiled firmware (an LED test build and the initial release firmware) on GitHub after the con, though as PDF/BOM-sheet/binary artifacts rather than full CAD source files.
