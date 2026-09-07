---
title: Pickle Rick Badge SAO
id: dc27-pickle-rick-badge-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: s3gfault (TeamID64F)
summary: A Rick and Morty "Pickle Rick"-themed SAO with nine individually addressable LEDs, part of TeamID64F's line of pop-culture badge add-ons.
functions: 'Lights the nine onboard LEDs in patterns/colors under I2C control from the host badge.'
look:
  colors: [green]
  shape: null
  themes: [meme, pop culture, tv]
tech:
  mcu: none
  leds:
    count: 9
    type: discrete
    note: Driven via an MCP23008 I2C LED/GPIO expander rather than a microcontroller.
  display: none
  connectivity: [i2c]
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing shown as retired/no longer available for purchase, checked 2026-09-07.'
  distribution: [purchase]
  where: Sold on Tindie by TeamID64F (s3gfault); shipped from Switzerland, the US, and Brazil.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/s3gfault/team-id64f-pickle-rick-badge-sao
  url: https://www.tindie.com/products/s3gfault/team-id64f-pickle-rick-badge-sao/
  kind: store
images:
  - file: assets/images/badges/dc27/pickle-rick-badge-sao/48a1e91d0d.jpg
    source: "https://www.tindie.com/products/s3gfault/team-id64f-pickle-rick-badge-sao/"
    credit: "s3gfault (TeamID64F)"
    caption: "Pickle Rick Badge SAO, product photo"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
- 'TeamID64F sells a series of similarly-built SAOs (Punisher, Red Stapler, Windows Logo, DeadPool) around the same MCP23008/9-LED design; see research.notes.'
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/s3gfault/team-id64f-pickle-rick-badge-sao/
  title: Pickle Rick Badge SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27 (likely, unconfirmed)''.'
- kind: url
  url: https://www.tindie.com/products/s3gfault/team-id64f-pickle-rick-badge-sao/
  title: Team ID64F "Pickle Rick" Badge SAO from TeamID64F on Tindie
  accessed: '2026-09-07'
  note: 'WebFetch of the Tindie listing: confirms 9 LEDs via MCP23008 driver, I2C/3.3V, SAO v1.69bis, product first listed 2019-07-09, now retired with no listed price/quantity.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found is the maker''s own (now-retired) Tindie listing, which confirms this is a DEF CON-badge-compatible SAO first posted 2019-07-09 -- consistent with DC27 (2019), so the sheet''s tentative event guess is kept. No press coverage, repo, or design files were found. Price, original quantity, and open-source status are unknown. TeamID64F/s3gfault runs a small series of similarly-built pop-culture SAOs (Punisher, Red Stapler, Windows Logo, DeadPool) that may be worth their own entries -- see other_items_found.'
last_modified_date: '2026-09-07'
---

The Pickle Rick Badge SAO is a Rick and Morty-themed add-on made by TeamID64F (maker handle s3gfault) for DEF CON's unofficial SAO add-on ecosystem. It carries nine individually addressable LEDs driven through an MCP23008 I2C GPIO/LED expander rather than a dedicated microcontroller, running at 3.3V and following the SAO v1.69bis (6-pin) pinout so it plugs into any compatible badge header. The product photos show the board lit in blue, green, and red, suggesting the LEDs can be run in different color/pattern combinations under the host badge's control.

The Tindie listing dates to July 2019, placing the badge at DEF CON 27, and the product is now marked retired with no price or quantity information surviving on the page. No design files, firmware repository, or independent coverage of this specific SAO were found; everything here comes from the maker's own storefront listing.

TeamID64F sold several other similarly-built SAOs around the same era -- including Punisher, Red Stapler, Windows Logo, and DeadPool designs -- that share the same general construction and may warrant their own archive entries.
