---
title: HITCON CMT 2023 NFC Badge
id: hitcon-2023-hitcon-cmt-2023-nfc-badge
layout: badge
parent: Hitcon Cmt 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitcon-2023
year: 2023
makers:
- name: HITCON Activity Team
summary: 'The official attendee badge for HITCON Community 2023 (Taipei), an NFC-based pass that doubled as a game token: badge scans at card readers around the venue activated mini-games and tallied a daily leaderboard.'
functions: 'NFC tap-to-activate mini-games at booths and venue-wide card-reader stations; daily score tracking with prizes for the top three scores each day, plus extra prizes for hitting participation thresholds. The Activity Team booth also let attendees inspect NFC card readers to learn how ID-card NFC operation works.'
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - nfc
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Included in the attendee welcome kit at HITCON Community (CMT) 2023, held August 18-19, 2023 at Academia Sinica, Taipei, Taiwan, alongside a limited-edition event T-shirt.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/badges/hitcon-cmt-2023-nfc-badge
  url: https://badge.gallery/badges/hitcon-cmt-2023-nfc-badge
  kind: website
- label: 'HITCON CMT 2023 - Events page (official)'
  url: https://hackdoor-leaderboard.hitcon.org/2023/CMT/en/events/
  kind: website
- label: 'HITCON CMT 2023 - main event site'
  url: https://hitcon.org/2023/CMT/en/
  kind: website
images: []
contact: {}
notes:
- NFC-based attendee badge used for card-reader mini-games and prize tracking at booths. Found by the event-year sweep, task con-hitcon.
- 'Sweep title matches the maker''s naming as reflected on badge.gallery; no maker-produced page with a different title was found.'
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/hitcon-cmt-2023-nfc-badge
  title: HITCON CMT 2023 NFC Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-hitcon); event read as ''HITCON CMT 2023''.'
- kind: url
  url: https://hackdoor-leaderboard.hitcon.org/2023/CMT/en/events/
  title: 'Events | HITCON CMT 2023'
  accessed: '2026-09-08'
  note: 'Official HITCON event page (via search-result snippet only; direct fetch blocked by Cloudflare challenge) confirming badge-activated mini-games, card readers around the venue and at the Activity Team booth, and NFC learning.'
- kind: url
  url: https://hitcon.org/2023/CMT/en/
  title: 'HITCON CMT 2023'
  accessed: '2026-09-08'
  note: 'Confirms event dates (Aug 18-19, 2023) and venue (Academia Sinica, Taipei).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: >-
    Confirmed as a real item: the official HITCON CMT 2023 events page (hackdoor-leaderboard.hitcon.org)
    independently describes badge-activated card-reader mini-games, matching badge.gallery's account, but
    the page itself sits behind a Cloudflare JS challenge that both WebFetch and curl could not pass, so
    it was read only via search-result snippets, not fetched directly. No maker photo of the badge was
    found anywhere searched (badge.gallery notes it is deliberately image-free pending licensed photos);
    no chip/NFC-tag model, LED, display, PCB, price, or quantity information was published by HITCON.
    Treated as a free giveaway included in the welcome kit rather than a sold item. If this is a plain
    NFC ID card rather than a custom PCB, it may be more "generic con merch" than a badgelife-style
    badge, but it has documented interactive functions (mini-games, leaderboard) so it was kept as
    type: badge rather than marked not_an_item.
last_modified_date: '2026-09-08'
---

The HITCON CMT 2023 NFC Badge was the attendee pass for HITCON Community 2023, held August 18-19, 2023 at Academia Sinica in Taipei. Rather than serving purely as identification, the badge doubled as a game token: card readers were placed at booths and scattered around the venue, and tapping the badge against them activated mini-games. The event tracked scores over each day of the con, with prizes going to the top three scorers daily and additional prizes for attendees who crossed participation thresholds.

The HITCON Activity Team also ran a booth where attendees could inspect NFC card readers directly, using the badge as a teaching tool for how NFC ID-card operation works under the hood. The badge was distributed for free as part of the standard welcome kit, alongside a limited-edition event T-shirt.

No public source discloses the badge's underlying hardware — chip family, NFC tag type, or whether it was a bespoke PCB versus an off-the-shelf NFC card — nor is there a surviving photo of the badge itself in the sources checked. The official HITCON event page corroborates the mini-game and card-reader mechanics but is not reachable by automated fetch (it sits behind a Cloudflare challenge), so this entry relies on that page's content as surfaced in search results plus a third-party badge catalog (badge.gallery) that appears to draw from the same source.
