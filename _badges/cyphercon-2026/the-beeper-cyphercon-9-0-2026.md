---
title: The Beeper (CypherCon 9.0, 2026)
id: cyphercon-2026-the-beeper-cyphercon-9-0-2026
layout: badge
parent: CypherCon 9.0
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cyphercon-2026
year: 2026
makers:
- name: TYMKRS
  url: https://hackthebadge.com/
summary: The official CypherCon 9.0 (2026) badge, built around pager ("beeper") technology as a nod to the "extremely insecure network" of old paging systems.
functions: Participates in an on-site pager-style paging network at CypherCon, described by the makers as "an extremely insecure network"; exact on-badge functions not stated by the maker.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - security
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
- label: hackthebadge.com/cyphercon-9-0-2026
  url: https://hackthebadge.com/cyphercon-9-0-2026/
  kind: website
- label: r/Tymkrs discussion thread
  url: https://www.reddit.com/r/Tymkrs/comments/1s806y5/cyphercon_badge_2026_90/
  kind: social
- label: SomewhatParticular/cyphercon2026 (community pager-traffic sniffer, not maker firmware)
  url: https://github.com/SomewhatParticular/cyphercon2026
  kind: repo
  archived: https://web.archive.org/web/20260405034138/https://github.com/SomewhatParticular/cyphercon2026
images: []
contact: {}
notes:
- Official CypherCon 2026 conference badge, a vintage-pager-themed device built around a deliberately insecure paging network, tied to an 'internet nostalgia' theme. Found by the event-year sweep, task cyphercon.
status: released
sources:
- kind: url
  url: https://hackthebadge.com/cyphercon-9-0-2026/
  title: The Beeper (CypherCon 9.0, 2026)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:cyphercon); event read as ''cyphercon-2026''.'
- kind: url
  url: https://hackthebadge.com/cyphercon-9-0-2026/
  title: CypherCon 9.0 (2026) - The Beeper
  accessed: '2026-09-08'
  note: TYMKRS's own post confirming name and the pager/insecure-network theme. The page's only date is a WordPress "Posted in" stamp of April 5, 2026, which is the blog-post date, not a stated event date; do not treat it as when the con occurred (see correction below).
- kind: url
  url: https://github.com/SomewhatParticular/cyphercon2026
  title: SomewhatParticular/cyphercon2026
  accessed: '2026-09-08'
  note: Third-party (not TYMKRS) repo describing a sniffer for "CypherCon 9 pager traffic", confirming the badge communicates over a pager-style protocol; not the maker's own firmware, so not used as an open-source/firmware link.
  archived: https://web.archive.org/web/20260405034138/https://github.com/SomewhatParticular/cyphercon2026
- kind: url
  url: https://infosec-conferences.com/event/20260401-cyphercon-9-2026/
  title: CypherCon 9 2026, Milwaukee, United States | Cyber Event
  accessed: '2026-09-08'
  note: Third-party event listing giving the actual CypherCon 9.0 dates as April 1-2, 2026, at the Baird Center, Milwaukee — corrects the entry's earlier mistaken use of the hackthebadge.com blog-post date (April 5, 2026) as the event date. Corroborated by matching listings on kure-cal.com and epochal-intelligence.com.
  archived: https://web.archive.org/web/20260516083226/https://infosec-conferences.com/event/20260401-cyphercon-9-2026/
research:
  status: researched
  confidence: low
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): the prior draft stated the con was "held April 5, 2026", citing TYMKRS''s hackthebadge.com post — but that page never states an event date; April 5, 2026 is only the WordPress post-date stamp. Third-party event listings (infosec-conferences.com, kure-cal.com, epochal-intelligence.com) independently agree CypherCon 9.0 was actually held April 1-2, 2026 in Milwaukee. Corrected the body text and this note accordingly; the "released" status conclusion is unaffected since either date has already passed relative to today (2026-09-08). TYMKRS''s own hackthebadge.com post is otherwise very short and confirms only the name and the pager/"insecure network" theme; it does not state MCU, LEDs, display, price, quantity, or availability, and includes no photo of the badge itself. The linked r/Tymkrs writeup (usual source for TYMKRS badge build details in past years) could not be fetched — reddit.com blocked both the fetch tool and curl, again on this recheck. A
    third-party GitHub repo (SomewhatParticular/cyphercon2026) built a sniffer for the badge''s pager traffic, which corroborates the pager theme but is not the maker''s own hardware/firmware source and gives no chip/display/LED specifics, so tech fields and make_your_own remain unfilled. (Note: that repo also contains a "base-badge" folder described as "a dump of the badge''s base code" that appears to reference an RP2040, an ST7565 LCD, and an SX1262 LoRa radio — but since it is an unverified third-party dump rather than a maker statement, and filling tech fields was outside this fact-check''s scope, it is flagged here for a future research pass rather than used to fill fields.) status remains "released" (not "verified") because the reddit thread and tech details remain unconfirmed.'
last_modified_date: '2026-09-08'
---

The Beeper is TYMKRS's badge for CypherCon 9.0, held April 1-2, 2026 in Milwaukee. The con's theme was "Remember when the internet was fun?", and having already covered early-web nostalgia (webrings, old webpages) with a previous e-ink badge, TYMKRS turned this year to pagers, framed as "an extremely insecure network" from the same era.

Beyond the name, maker, and theme, TYMKRS's own writeup on hackthebadge.com is sparse: it does not describe the badge's MCU, display, LEDs, or how it was distributed, and includes no photo. A community member's GitHub repo (SomewhatParticular/cyphercon2026) built a sniffer for "CypherCon 9 pager traffic" by adapting code from the CypherCon 6 e-paper badge, which confirms the badge exchanges pager-style radio traffic on-site but is not TYMKRS's own hardware or firmware release. TYMKRS's usual practice is to post fuller build details to r/Tymkrs; that thread exists (linked from the maker's page) but could not be retrieved in this pass since reddit.com blocked both the fetch tool and a direct curl request.
