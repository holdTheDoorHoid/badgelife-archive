---
title: Agency Wand
id: dc34-agency-wand
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc34
year: 2026
makers:
- name: 000000widow (Brooke's Bytes)
summary: 'A wand-shaped electronic badge with five reverse-mounted addressable LEDs that shine through the front of the PCB, made in partnership with TrueControl.'
functions: 'Two buttons control it: a handle button cycles through roughly five or six animated lighting programs, and a rear button enters a setup/configuration mode. A rear red LED does ambient-light detection, and two red handle LEDs give feedback while in setup mode.'
look:
  colors: []
  shape: wand
  themes:
  - wearable
tech:
  mcu: ATtiny1616
  leds:
    count: 8
    type: reverse-mount
    note: '5 front-facing reverse-mounted addressable LEDs for animated effects, 1 rear red LED for ambient-light detection, and 2 red handle LEDs for setup-mode feedback.'
  display: none
  connectivity:
  - uart
  battery: CR2032
  sao_version: none
get_one:
  price: '$60'
  price_usd: 60
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold on Uberflux (uberflux.com); the maker's listing shows 19 sold and none remaining as of 2026-09-07.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'The maker links a TrueControl git repository (git.trueserve.org/trueControl/hsc25-dc34-wand) for "full documentation and technical resources," but the page returned 403 Forbidden when checked, so open-source status and file links could not be confirmed.'
links:
- label: uberflux.com/product/WIDOW-agency_wand
  url: https://uberflux.com/product/WIDOW-agency_wand
  kind: store
- label: TrueControl documentation repo (hsc25-dc34-wand)
  url: https://git.trueserve.org/trueControl/hsc25-dc34-wand
  kind: repo
images:
  - file: assets/images/badges/dc34/agency-wand/326aa186b0.jpg
    source: "https://uberflux.com/product/WIDOW-agency_wand"
    credit: "Brooke's Bytes (000000widow)"
    caption: "The Agency Wand badge, front view"
  - file: assets/images/badges/dc34/agency-wand/cd9d4b4743.jpg
    source: "https://uberflux.com/product/WIDOW-agency_wand"
    credit: "Brooke's Bytes (000000widow)"
    caption: "The Agency Wand badge, alternate view"
contact: {}
notes:
- 'Uberflux. $60, status: sold out.'
- 'The maker''s own description says the wand concept started in 2025 and first came together for HackSpaceCon 2025 (no matching event id exists in events.yml for HackSpaceCon), with this specific listing being the new iteration the maker planned to drop at DEF CON 34, "in correlation with this year''s theme" — hence event set to dc34.'
status: released
sources:
- kind: url
  url: https://uberflux.com/product/WIDOW-agency_wand
  title: Agency Wand
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: uberflux-shops); event read as ''unknown''.'
- kind: url
  url: https://uberflux.com/product/WIDOW-agency_wand
  title: Agency Wand
  accessed: '2026-09-07'
  note: 'Full product description, hardware spec list, price ($60, 19 sold, price_cents 6000), and product photos.'
- kind: url
  url: https://git.trueserve.org/trueControl/hsc25-dc34-wand
  title: 'TrueControl hsc25-dc34-wand repository'
  accessed: '2026-09-07'
  note: 'Linked by the maker as the documentation/technical-resources repo; returned HTTP 403 Forbidden when fetched, so contents could not be confirmed.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Confirmed maker, hardware spec, price, and sold-out status directly from the maker''s own storefront listing. Could not confirm open-source status, gerbers, or firmware links because the linked TrueControl repo returned 403 Forbidden. Quantity made is unknown beyond "19 sold, 0 remaining" (listing may have been limited to that run). Event corrected from "other" to dc34 based on the maker''s stated intent to release this named iteration at DEF CON 34; the item may also be associated with HackSpaceCon 2025 as an earlier related project, but no HackSpaceCon event id exists in this archive.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/agency-wand/
---

The Agency Wand is a wand-shaped electronic badge made by 000000widow of Brooke's Bytes, in partnership with TrueControl. The idea began in 2025, first taking shape as a badge for HackSpaceCon 2025; the maker describes the version sold here as a new iteration, named "Agency Wand" to match that year's DEF CON theme, planned for release at DEF CON 34.

The wand is built around an ATtiny1616 microcontroller and runs on a CR2032 coin cell. Five reverse-mounted addressable LEDs shine through the front of the PCB to produce animated lighting effects, alongside a rear red LED used for ambient-light detection and two red handle LEDs that give feedback while the badge is in its setup mode. Two physical buttons operate it: a handle button steps through roughly five or six lighting programs, and a rear button enters setup and configuration. Exposed UART pins allow firmware updates.

It sold for $60 through the maker's Uberflux storefront and is now sold out, with the listing showing 19 units sold. The maker links a TrueControl git repository for documentation and technical resources, but that page could not be reached (403 Forbidden) to confirm whether hardware or firmware files are actually published there.
