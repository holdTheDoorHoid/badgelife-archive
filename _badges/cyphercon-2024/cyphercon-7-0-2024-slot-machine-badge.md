---
title: CypherCon 7.0 (2024) Slot Machine Badge
id: cyphercon-2024-cyphercon-7-0-2024-slot-machine-badge
layout: badge
parent: CypherCon 7.0
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2024
year: 2024
makers:
- name: TYMKRS
summary: 'The official CypherCon 7.0 (2024) badge: a slot-machine themed electronic badge built around the con''s "Casino Heist" theme.'
functions: 'A spinning slot-machine playfield with 24 icons in order of value: Lemon, Clover, Diamond, Hack (a CypherCon-specific icon standing in for the usual BAR symbol), Horseshoe, Cherries, CypherCon Gear, and Seven. Badges also identify themselves over a serial link and support a badge-to-badge point-trading feature (reverse-engineered separately by a third party; see notes).'
look:
  colors: []
  shape: null
  themes:
  - casino
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: cyphercon.com/cyphercon-7-0
  url: https://cyphercon.com/cyphercon-7-0/
  kind: website
- label: hackthebadge.com/cyphercon-7-0-2024
  url: https://hackthebadge.com/cyphercon-7-0-2024/
  kind: website
- label: www.reddit.com/r/Tymkrs/comments/1byh4kw/cyphercon_badge_2024_70
  url: https://www.reddit.com/r/Tymkrs/comments/1byh4kw/cyphercon_badge_2024_70/
  kind: social
- label: ANDnXOR/cyphercon2024_badge_serial (GitHub)
  url: https://github.com/ANDnXOR/cyphercon2024_badge_serial
  kind: repo
images: []
contact: {}
notes:
- Official electronic conference badge for CypherCon 7.0 (Casino Heist theme), a slot-machine-themed badge with an icon-trading feature over an audio-cable link, documented on hackthebadge.com. Found by the event-year sweep, task general-2023.
- 'Duplicate: this entry describes the same badge as cyphercon-2024-the-slot-machine-badge-cyphercon-7-0-2024, which has already been researched independently and reaches the same conclusions; reported as duplicate_of rather than merged here.'
- Official CypherCon 2024 conference badge with a casino theme, featuring 24 spinning slot-machine icon reels including a con-specific 'Hack' symbol. Found by the event-year sweep, task cyphercon.
- Sweep's wording "The Slot Machine Badge (CypherCon 7.0, 2024)" matches the maker's own hackthebadge.com post title; kept as-is.
status: released
sources:
- kind: url
  url: https://cyphercon.com/cyphercon-7-0/
  title: CypherCon 7.0 (2024) Slot Machine Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2023); event read as ''CypherCon 2024''.'
- kind: url
  url: https://hackthebadge.com/cyphercon-7-0-2024/
  title: CypherCon 7.0 (2024) - hackthebadge.com
  accessed: '2026-09-08'
  note: 'TYMKRS'' own blog post announcing the badge: confirms maker, event, "Casino" theme, and the 24-icon slot-machine playfield (Lemon, Clover, Diamond, Hack, Horseshoe, Cherries, CypherCon Gear, Seven). Also notes the first hardware revision failed due to missing parts and the shipped badge was a reworked second version. No chip/LED/display/price/quantity details or badge photos present on the page.'
- kind: url
  url: https://cyphercon.com/cyphercon-7-0/
  title: CypherCon 7.0 - CypherCon
  accessed: '2026-09-08'
  note: 'Official CypherCon history page confirms "Badge: Slot Machine Badge by the TYMKRS" for CypherCon 7.0, April 4-5, 2024, Baird Center, Milwaukee, theme "Casino Heist", ~1780 attendees.'
- kind: url
  url: https://github.com/ANDnXOR/cyphercon2024_badge_serial
  title: 'ANDnXOR/cyphercon2024_badge_serial: Reverse engineering the badge serial protocol'
  accessed: '2026-09-08'
  note: 'Third-party repo reverse-engineering the badge''s serial protocol: badges report an ID/type/item number and support a point-trading feature between badges, with ID ranges mapped to point values (general 10, VIP 20, speaker 100, vendor 1,000, founder 10,000, lifetime member 100,000). Confirms the trading/scoring functionality mentioned in the original sweep notes, though no MCU or physical-link (e.g. audio-cable) detail is stated explicitly in the repo.'
- kind: url
  url: https://www.reddit.com/r/Tymkrs/comments/1byh4kw/cyphercon_badge_2024_70/
  title: 'CypherCon Badge 2024 (7.0) : r/Tymkrs'
  accessed: '2026-09-08'
  note: TYMKRS' own announcement post; confirms maker, event, casino theme, and the 24-icon slot-machine playfield (Lemon, Clover, Diamond, Hack, Horseshoe, Cherries, CypherCon Gear, Seven). Full page could not be fetched directly (Reddit blocks automated fetches); details taken from a search-result snippet of this same maker post.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed as a real, distributed badge via the maker's own hackthebadge.com post and CypherCon's official history page. The Reddit announcement thread (the primary maker post) could not be fetched directly during this pass (Reddit blocks automated fetches); its content is known only via search-result snippets, which match hackthebadge.com. The sweep's original note that trading happens "over an audio-cable link" could not be independently confirmed or sourced to a reachable page; a separate reverse-engineering repo (ANDnXOR) confirms a serial-based ID/point-trading system but does not specify the physical link type, so tech.connectivity is left empty rather than guessed. No page found gives chip, LED, display, battery, price, or quantity, so those fields remain empty. No confirmed photo of the badge itself was found on any reachable page. This entry duplicates cyphercon-2024-the-slot-machine-badge-cyphercon-7-0-2024, which covers the same badge and sources; flagged as duplicate_of.
    Merged with duplicate entry 'The Slot Machine Badge (CypherCon 7.0, 2024)' (cyphercon-2024-the-slot-machine-badge-cyphercon-7-0-2024).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/cyphercon-2024/the-slot-machine-badge-cyphercon-7-0-2024/
---

The Slot Machine Badge was TYMKRS' badge for CypherCon 7.0, held April 4-5, 2024 at the Baird Center in Milwaukee, Wisconsin, under the con's "Casino Heist" theme. It carries a spinning slot-machine playfield of 24 icons arranged in order of value: Lemon, Clover, Diamond, a CypherCon-specific "Hack" icon standing in for the usual BAR symbol, Horseshoe, Cherries, CypherCon Gear, and Seven.

TYMKRS' own announcement noted that their first build of the badge didn't work because parts went missing, and the badge that shipped was a reworked second version. A separate reverse-engineering project (ANDnXOR's `cyphercon2024_badge_serial`) documents a badge-to-badge trading feature: each badge reports an ID, type, and item number over a serial link, and different attendee categories (general, VIP, speaker, vendor, founder, lifetime member) carry different point values that can be traded between badges.

Beyond the slot-reel description and the trading mechanic, no further technical details (microcontroller, LEDs, display, power, price, or quantity produced) were found on any page reachable during this research pass, and no confirmed photo of the badge could be retrieved.

## Notes merged from the duplicate entry "The Slot Machine Badge (CypherCon 7.0, 2024)"

The Slot Machine Badge was TYMKRS' badge for CypherCon 7.0, held April 4-5, 2024 at the Baird Center in Milwaukee, Wisconsin, under the con's "Casino Heist" theme. It carries a spinning slot-machine playfield of 24 icons arranged in order of value: Lemon, Clover, Diamond, a CypherCon-specific "Hack" icon standing in for the usual BAR symbol, Horseshoe, Cherries, CypherCon Gear, and Seven.

TYMKRS' own announcement noted that their first build of the badge didn't work because parts went missing, and the badge that shipped was a reworked second version. Beyond that account and the slot-reel description, no further technical details (microcontroller, LEDs, display, power, price, or quantity produced) were found on any page reachable during this research pass, and no confirmed photo of the badge could be retrieved.
