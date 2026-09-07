---
title: Punisher Badge SAO
id: dc27-punisher-badge-sao
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: s3gfault (TeamID64F)
summary: A Punisher-skull-themed SAO made by TeamID64F for DEF CON 27, sold alongside a DeadPool-themed SAO from the same maker.
functions: Lights blue on the body and green for the eyes on power-up via a preloaded ATtiny85 light sequence; can also be driven directly from a host badge's MCP23017 LED driver if the badge supports it.
look:
  colors: []
  shape: skull
  themes:
  - skull
  - movie
  - pop culture
tech:
  mcu: ATtiny85
  leds:
    count: 16
    type: discrete
    note: 10x blue and 6x green 1206 LEDs, driven by the ATtiny85's preloaded sequence or via an onboard MCP23017 I/O expander if the host badge supports it.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: $10
  price_usd: 10
  quantity: ''
  availability: sold_out
  availability_note: Listing shows "Sold out since Jan 16, 2022"; the live product URL now 302-redirects to the store's front page (checked 2026-09-07), confirmed via an Internet Archive snapshot of the listing since the live page is blocked by Cloudflare.
  distribution:
  - purchase
  where: Sold via TeamID64F's Tindie store (s3gfault) for $10; listing is no longer active/purchasable.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/s3gfault/team-id64f-punisher-badge-sao
  url: https://www.tindie.com/products/s3gfault/team-id64f-punisher-badge-sao/
  kind: store
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/s3gfault/team-id64f-punisher-badge-sao/
  title: Punisher Badge SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27 (likely, unconfirmed)''. Live page is Cloudflare-blocked and now 302-redirects to the store front page; content verified instead via the Internet Archive snapshot below.'
- kind: url
  url: https://www.tindie.com/stores/s3gfault/
  title: 'Browse products by TeamID64F on Tindie'
  accessed: '2026-09-07'
  note: 'Live store page is Cloudflare-blocked; verified instead via the Internet Archive snapshot below, which shows only three current listings for this maker (Punisher SAO, DeadPool SAO, and a "SAO Package") — it does NOT show a Red Stapler or Windows Logo SAO, so those two could not be confirmed and were removed from the body text.'
- kind: url
  url: http://web.archive.org/web/20221224183500/https://www.tindie.com/products/s3gfault/team-id64f-punisher-badge-sao/
  title: 'Team ID64F "Punisher" Badge SAO from TeamID64F on Tindie (archived Dec 2022)'
  accessed: '2026-09-07'
  note: 'Archived copy of the live listing, read directly (not a search snippet). Confirms: made for DefCon27; $10.00 price; "Sold out since Jan 16, 2022"; ATtiny85 microcontroller plus an MCP23017 LED driver; 10x blue + 6x green 1206 LEDs, lighting blue on the body and green for the eyes; SAO v1.69bis connector, 3.3V, compatible with "last year''s badge."'
- kind: url
  url: http://web.archive.org/web/20221126082446/https://www.tindie.com/stores/s3gfault/
  title: TeamID64F Tindie store (archived Nov 2022)
  accessed: '2026-09-07'
  note: 'Archived copy of the store front page, read directly. Lists only the Punisher SAO, a DeadPool SAO, and a "SAO Package" bundle at that time — no Red Stapler, Windows Logo, or Pickle Rick items are shown.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): the live Tindie listing and store page remain Cloudflare-blocked (WebFetch 403, curl returns a JS challenge; the direct product URL also 302-redirects to the store front page, consistent with the listing no longer being live). Internet Archive snapshots of both pages (Dec 2022 and Nov 2022) were read directly and confirm every fact now recorded: DEF CON 27, ATtiny85 + MCP23017 LED driver, 10 blue + 6 green 1206 LEDs, blue body/green eyes light pattern, SAO v1.69bis connector, $10 price, and "Sold out since Jan 16, 2022." The prior draft''s claim (sourced from search-engine snippets) that TeamID64F also made a Red Stapler, Windows Logo, and Pickle Rick SAO alongside this one could NOT be corroborated: the archived store page from the same era lists only this SAO, a DeadPool SAO, and a bundle "SAO Package." That sentence and those product names have been removed from the body. The DeadPool SAO mention is retained since it does appear in the archived store snapshot. LED count/type, price, and SAO version, previously left blank, are now filled in with confidence since they come from the maker''s own listing text.'
last_modified_date: '2026-09-07'
---

The Punisher Badge SAO is a Punisher-skull-themed add-on made by TeamID64F (Tindie seller s3gfault) for DEF CON 27 in 2019, sold alongside a DeadPool-themed SAO from the same maker. It carries an ATtiny85 plus an MCP23017 LED driver feeding 10 blue and 6 green 1206 LEDs, and lights up on power-up with a preloaded animation — blue for the body, green for the eyes. If the host badge supports the MCP23017 driver, the LEDs can also be programmed directly rather than relying on the preloaded sequence. It uses a SAO v1.69bis connector at 3.3V.

The SAO sold for $10 through TeamID64F's Tindie storefront; the listing shows it as sold out since January 16, 2022, and the listing itself is no longer reachable directly (it now redirects to the store's front page). No hardware or firmware files, or production-quantity figures, were recoverable from available sources. The live Tindie pages sit behind Cloudflare bot-detection, so this entry's facts come from Internet Archive snapshots of the product listing and storefront rather than the live pages.
