---
title: DC801 Tariff Badge
id: dc33-dc801-tariff-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: DC801
summary: A hand-branded wooden badge with a single glowing red LED, made by DC801 as a satirical response to 2025 tariff anxieties.
functions: Joy, smell of burnt wood, a return to basics. One red LED glows (blinking not guaranteed).
look:
  colors:
  - wood
  - red
  shape: null
  themes:
  - meme
  - pop culture
  - minimalist
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: A single red LED that glows; described by the maker as not guaranteed to blink.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: $50
  price_usd: 50.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold via a PayPal listing; pickup at 801 Labs the Thursday before DEF CON 33 (7/31/2025) or at the DC801 party (8/9/2025), or shipped.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: dc801.party
  url: https://dc801.party
  kind: website
- label: DC801 Tariff Badge (PayPal listing)
  url: https://www.paypal.com/ncp/payment/BC5AKHTEJEN7Q
  kind: store
images:
- file: assets/images/badges/dc33/dc801-tariff-badge/80973c0f37.jpg
  source: "https://www.paypal.com/ncp/payment/BC5AKHTEJEN7Q"
  credit: "DC801"
  caption: "Hand-branded wooden DC801 Tariff Badge with a red LED"
contact:
  emails:
  - kimber@801labs.org
notes:
- Any profits from this badge will power 801 Labs hackerspace for the 2026 fiscal year.
- 'Maker''s own listing description: "When tariffs loomed and the economy trembled, we responded the only way that made sense: with a badge. A tiny monument to policy panic, late-stage capitalism, and the art of turning bad news into wearable irony. No PCB, just blinking lights and quiet defiance."'
status: listed
sources:
- kind: sheet
  event: dc33
  row: 31
  updated: 7/20/2025 20:58:36
- kind: url
  url: "https://www.paypal.com/ncp/payment/BC5AKHTEJEN7Q"
  title: DC801 Tariff Badge - PayPal listing
  accessed: '2026-09-06'
  note: Maker's own product description, price ($50), pickup/shipping logistics, and the only known photo of the badge; retrieved via the page's embedded metadata since the checkout UI itself is JS-rendered.
- kind: url
  url: "http://web.archive.org/web/20250809032609/https://dc801.party/"
  title: "SIGNAL_801 | Underground Frequency (DC801 party site, Aug 2025 snapshot)"
  accessed: '2026-09-06'
  note: Wayback Machine snapshot of dc801.party from Aug 9 2025 (during DEF CON 33); its bundled JS contains the "Support us with a DC801 tariff badge" call-to-action linking to the PayPal listing.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    Core facts (what it is, price, maker, distribution) come straight from the maker's own PayPal
    listing description, which is high-confidence for content but the listing itself is a
    third-party checkout page rather than a dedicated project/press page, hence "medium" rather
    than "high". dc801.party is a JS-rendered SPA that render tools could not read directly, so
    the current live site was accessed only via its 2025 archived JS bundle. No maker's own photo
    gallery, GitHub repo, Hackaday.io project, or press coverage was found for this specific badge
    (DC801's GitHub org has repos for several other-year DC801 badges, e.g. BM-Badge, DC25/26/27
    PartyBadge, but none for the 2025 Tariff Badge). Quantity made and whether it sold out are not
    stated anywhere found. No MCU is implied by the "No PCB, just blinking lights" description, so
    tech.mcu is set to "none" and leds.type to "discrete" as the most defensible reading rather than
    a guess at a specific driver circuit.
last_modified_date: '2026-09-06'
---

The DC801 Tariff Badge was a one-off, satirical badge sold by the Salt Lake City hackerspace 801 Labs (as "DC801") around DEF CON 33 in August 2025. Rather than a PCB, it is a hand-branded ("artisanal, one-of-a-kind") piece of wood decorated with imagery of DC801's past badges, fitted with a single red LED that the maker describes as glowing "mimicking the love we have in our hearts for our dearest Helga" — with blinking "not guaranteed." The badge was priced at $50 and sold directly through a PayPal listing rather than a storefront, with proceeds going toward funding 801 Labs for the following fiscal year.

It was made as commentary on the 2025 U.S. tariff turmoil, framed by the maker as "a tiny monument to policy panic, late-stage capitalism, and the art of turning bad news into wearable irony." Buyers could pick it up in person at 801 Labs the Thursday before DEF CON (July 31, 2025), at the annual DC801 party during the con (August 9, 2025), or have it shipped before or after the event.

No design files, GitHub repo, or dedicated project page were found for this badge specifically — DC801's GitHub organization hosts repos for several other years' party badges and minibadges, but none for the 2025 Tariff Badge, consistent with it being a simple wood-and-LED craft piece rather than an electronics project with a public build.
