---
title: SAO Many SAOs Badge
id: dc33-sao-for-above
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Coruscant Ventures
  url: https://coruscantventures.com/defcon-badges
summary: A DEF CON 33 "SAO carrier" badge with 25 slots for standalone add-on (SAO) modules, with white edge LEDs that need the maker's own SmartAO to animate.
functions: Hosts up to 25 SAO modules at once, each with fused/surge-protected power; edge LEDs are driven by whichever SAO is plugged into the top-left slot.
look:
  colors: []
  shape: null
  themes:
  - sao
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: 2x 18650 (USB or barrel-jack charging)
  sao_version: v2
get_one:
  price: '100'
  price_usd: 100.0
  quantity: ''
  availability: available
  availability_note: Listed "IN STOCK" on the maker storefront as of 2026-09-06; PayPal checkout on the page is broken, maker asks buyers to contact them directly via Discord/Reddit/contact form.
  distribution:
  - purchase
  where: Sold directly from the maker's Coruscant Ventures storefront (coruscantventures.com), by contacting the maker to arrange payment outside the broken checkout.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  firmware_url: null
  gerbers_url: null
  eda_tool: null
  notes: GitHub repo has schematics (as SVG sheets), a BOM, and assembly photos; maker notes Gerbers "may be released after DEF CON."
links:
- label: coruscantventures.com/defcon-badges/p/sao-many-saos
  url: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  kind: website
  archived: https://web.archive.org/web/20260506040947/https://coruscantventures.com/defcon-badges/p/sao-many-saos
- label: GitHub - vortexcodes/DC33-SaO-MANY-SAOs
  url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  kind: repo
images:
- file: assets/images/badges/dc33/sao-for-above/aa920f25c4.jpg
  source: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  credit: Coruscant Ventures
  caption: SAO Many SAOs badge product photo
  archived: https://web.archive.org/web/20260506040947/https://coruscantventures.com/defcon-badges/p/sao-many-saos
contact: {}
notes:
- SmartAO SAO required to make the LEDs around the edge light up.
- Sheet listed the title as "SAO for above"; retitled to match the maker's product name, "SAO Many SAOs Badge," per the linked storefront page.
status: released
sources:
- kind: sheet
  event: dc33
  row: 51
  updated: 7/28/2025
- kind: url
  url: https://coruscantventures.com/defcon-badges/p/sao-many-saos
  title: SAO Many SAOs Badge DEFCON 33 — Coruscant Ventures
  accessed: '2026-09-06'
  note: Maker's storefront listing; confirmed name, price ($100, not the $35 on the sheet), in-stock status, SmartAO dependency, and GitHub link.
  archived: https://web.archive.org/web/20260506040947/https://coruscantventures.com/defcon-badges/p/sao-many-saos
- kind: url
  url: https://github.com/vortexcodes/DC33-SaO-MANY-SAOs
  title: GitHub - vortexcodes/DC33-SaO-MANY-SAOs
  accessed: '2026-09-06'
  note: Maker's repo; confirmed 25-slot SAO carrier design, dual 18650 battery power, fused/surge-protected slots, edge LEDs driven by the top-left slot, and that Gerbers were withheld until after the con.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: This entry duplicates an existing entry for the same product, dc33-sao-many-saos (and possibly dc33-sao-and-many-sao-badge). The community sheet's title "SAO for above" does not match any product name on the maker's site or repo; the linked URL (coruscantventures.com/defcon-badges/p/sao-many-saos) is unambiguously the "SAO Many SAOs Badge," so the title was corrected to match. Price on the sheet ($35) does not match the current storefront listing ($100); kept the storefront figure since it is the maker's own current price and noted the discrepancy here. MCU/chip was not named in either the storefront copy or the visible README text. Quantity made was not stated anywhere found.
last_modified_date: '2026-09-06'
---

Coruscant Ventures' "SAO Many SAOs Badge" is a DEF CON 33 badge built to be a carrier for other people's SAOs rather than a single fixed add-on: it exposes 25 SAO slots, each fused and surge-protected, powered by a pair of 18650 cells charged over USB or a barrel jack. White LEDs run around the badge's edge, but they only animate when the top-left SAO slot holds the maker's companion SmartAO SAO (sold separately), which drives the display.

The community badge sheet listed this row under the title "SAO for above," but that name does not appear on the maker's storefront, GitHub repo, or anywhere else found; the sheet's own link points straight to the "SAO Many SAOs Badge" product page, so the entry has been retitled to match. As of this check the badge is listed in stock for $100 (the sheet's $35 price could not be confirmed and appears to be stale or a transcription error), though the storefront's PayPal checkout is broken and the maker asks buyers to arrange payment directly via Discord or Reddit. Design files — schematics as SVG sheets and a bill of materials — are published on GitHub, with the maker noting Gerbers might follow after the con.

This is very likely the same badge already catalogued under `dc33-sao-many-saos` (and possibly overlapping with `dc33-sao-and-many-sao-badge`); the three sheet rows appear to describe the same Coruscant Ventures product.
