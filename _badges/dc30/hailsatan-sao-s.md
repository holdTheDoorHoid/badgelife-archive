---
title: HailSatan SAO(s)
id: dc30-hailsatan-sao-s
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc30
year: 2022
makers:
- name: Sqearlsalazar
  url: https://www.tindie.com/stores/sqearlsalazar/
summary: A combo listing pairing sqearlsalazar's two occult-themed DEF CON SAOs, the Baphomet SAO and the Devil's Trap SAO, marketed under the "#hailsatan" hashtag.
functions: Each half lights red LEDs when powered by a host badge's SAO header; the pair carries clues to online challenges (video/audio, stego, crypto, file analysis, brute force, pcap analysis, general brain teasers), though the listing does not say solving them requires info from both SAOs together.
look:
  colors:
  - red
  - black
  shape: null
  themes:
  - horror
  - occult
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: null
get_one:
  price: $30
  price_usd: 30.0
  quantity: ''
  availability: available
  availability_note: The combo listing (satanic-saos-baphomet-devils-trap) loaded live on 2026-09-07 with price and customer reviews shown; the "hailsatan-saos" URL itself 302-redirects to the seller's store front rather than 404ing, so it may be a retired slug for the same or a related listing rather than a dead product.
  distribution:
  - purchase
  where: Sold as a pair on Tindie by sqearlsalazar, bundling the separately-sold Baphomet SAO and Devil's Trap SAO.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.tindie.com/products/sqearlsalazar/hailsatan-saos
  url: https://www.tindie.com/products/sqearlsalazar/hailsatan-saos/
  kind: store
- label: Satanic SAOs - Baphomet & Devil's Trap (Tindie, archived)
  url: https://www.tindie.com/products/sqearlsalazar/satanic-saos-baphomet-devils-trap/
  kind: store
  archived: https://web.archive.org/web/20221226050428/https://www.tindie.com/products/sqearlsalazar/satanic-saos-baphomet-devils-trap/
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- This listing is a bundle of two SAOs that already have their own archive entries -  dc30-baphomet-sao and dc30-devil-trap - sold together as a pair under the "#hailsatan" branding.
status: listed
sources:
- kind: url
  url: https://www.tindie.com/products/sqearlsalazar/hailsatan-saos/
  title: HailSatan SAO(s)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''unknown (pre-dates dc30, referenced as a companion piece)''. Verified 2026-09-07: this exact URL is not reachable as a distinct product page - it 302-redirects to the seller''s Tindie store front (https://www.tindie.com/stores/sqearlsalazar/), and a plain fetch of it returns a Cloudflare bot-check (403) rather than the product. No Wayback snapshot of the bare URL exists either.'
- kind: url
  url: https://www.tindie.com/products/sqearlsalazar/satanic-saos-baphomet-devils-trap/
  title: Satanic SAOs - Baphomet & Devil's Trap from sqearlsalazar on Tindie
  accessed: '2026-09-07'
  note: 'Verified 2026-09-07 by direct fetch: live page confirms $30 price, includes 1x Baphomet SAO + 1x Devil''s Trap SAO (plus optional dog-tag SAO holders for $10 more), and the exact quote "The #hailsatan SAOs will answer all of your thoughts and prayers." The description lists challenge types (video/audio, stego, crypto, file analysis, brute force, pcap analysis, general brain teasers) but does NOT state that solving them requires info from both SAOs together - that claim in an earlier draft of this entry was unsupported and has been removed. This is a same-maker, same-hashtag combo listing at a different URL than "hailsatan-saos"; treated as the likely same/successor product rather than confirmed identical.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: |
    Fact-check pass (2026-09-07): re-verified every field against its cited source. The "hailsatan-saos" Tindie URL is
    still not fetchable as its own product page - a plain WebFetch gets a Cloudflare 403, and a curl with a browser
    user-agent shows it 302-redirects to the seller's store front (tindie.com/stores/sqearlsalazar/) rather than a
    404, so the slug is retired/merged rather than confirmed broken. No Wayback snapshot of the bare URL exists.

    Direct fetch of the related combo listing, "Satanic SAOs - Baphomet & Devil's Trap" ($30), confirmed: price,
    that it bundles 1x Baphomet SAO + 1x Devil's Trap SAO (plus optional dog-tag holders), the exact "#hailsatan...
    answer all of your thoughts and prayers" quote, and the list of challenge types (video/audio, stego, crypto, file
    analysis, brute force, pcap analysis, general brain teasers). It did NOT confirm the earlier draft's claim that
    solving the challenge requires info from both SAOs together - that sentence was not supported by the source text
    and has been removed from the summary, functions, and body. `tech.sao_version` was also blanked: the two
    components carry different SAO versions (v1.69bis for Baphomet, v1 for Devil's Trap per their own entries), so a
    single "v1" for the bundle was an unsupported guess. `get_one.availability` was updated from "unknown" to
    "available" since the combo listing loaded live on 2026-09-07 with price and reviews shown.

    Colors/themes (red, black; horror, occult) are carried over from the two individual entries (dc30-baphomet-sao,
    dc30-devil-trap) rather than confirmed on this combo page directly, which does not describe PCB color. Treating
    this as the same or a successor combo product to "hailsatan-saos," and a likely duplicate/bundle of the two
    existing entries, rather than inventing separate specs for it. Quantity, exact release date, and whether the
    "hailsatan-saos" slug and this combo listing were ever literally the same product could not be confirmed - kept
    at low confidence.
last_modified_date: '2026-09-07'
related:
- dc30-baphomet-sao
- dc30-devil-trap
---

"HailSatan SAO(s)" appears to be sqearlsalazar's Tindie listing bundling two of the maker's occult-themed DEF CON 30 add-ons together: the Baphomet SAO (sold standalone as the "Baphomet Defcon SAO," described in its own listing as the "Satanic Goat SAO") and the Devil's Trap SAO. Both are passive, LED-only PCBs powered from a host badge's SAO header, with no onboard microcontroller. The maker's copy for the "#hailsatan" line promises the pieces will "answer all of your thoughts and prayers" and ties them to an online challenge - video/audio, stego, crypto, file analysis, brute force, pcap analysis, and general brain teasers - though the listing itself does not say the challenge requires information from both SAOs together.

The exact "hailsatan-saos" product page could not be reached directly: it 302-redirects to the seller's Tindie store front rather than showing a product, and no Wayback Machine snapshot of the bare URL exists. This entry is instead based on a directly-fetched, same-maker combo listing, "Satanic SAOs - Baphomet & Devil's Trap," which bundles the same two SAOs for $30 and carries matching "#hailsatan" copy. Because the individual pieces already have their own archive entries (dc30-baphomet-sao and dc30-devil-trap) with fuller specs, this entry is likely a duplicate covering the same hardware sold as a set, and should probably be merged or cross-referenced rather than treated as a third distinct item.
