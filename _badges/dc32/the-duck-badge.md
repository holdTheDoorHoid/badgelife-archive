---
title: The Duck Badge
id: dc32-the-duck-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Red String Studio x The Crow & Pigeon
  url: https://instagram.com/redstring.studio
summary: A duck-shaped electronic badge with a "quack counter" 7-segment display and a speaker, sold as a novelty "adoption" at DEF CON 32.
functions: Press the button to wirelessly quack together with the entire flock! Comes with an easy puzzle or two and some neat duck facts to impress your friends.
look:
  colors:
  - black
  shape: duck
  themes:
  - duck
  - animal
  - bird
  - meme
tech:
  mcu: null
  leds: null
  display: 3-digit 7-segment ("quack counter")
  connectivity: []
  battery: batteries (included with adoption kit)
  sao_version: null
get_one:
  price: $80
  price_usd: 80.0
  quantity: ~300
  availability: sold_out
  availability_note: 'Maker''s site (hackthequack.com), checked 2026-09-06, shows only a later-year notice that the team could not attend that DEF CON and had "remaining ducks" for adoption; no live purchase link.'
  distribution:
  - purchase
  where: In person at DEF CON 32, direct from Red String Studio x The Crow & Pigeon; the $80 "adoption fee" included the badge, a sticker sheet, an adoption certificate, batteries, a lanyard, and instructions.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackthequack.com
  url: http://hackthequack.com/
  kind: website
- label: hackthequack.com (2024 archived adoption page)
  url: http://web.archive.org/web/20240811053926/http://hackthequack.com/
  kind: website
- label: Red String Studio (Instagram)
  url: https://instagram.com/redstring.studio
  kind: social
- label: The Crow & Pigeon (Instagram)
  url: https://instagram.com/thecrowandpigeon
  kind: social
images:
- file: assets/images/badges/dc32/the-duck-badge/dc09264722.png
  source: "http://hackthequack.com/"
  credit: "Red String Studio x The Crow & Pigeon"
  caption: "The Duck Badge PCB: duck-shaped board with coil antenna, quack counter display, speaker, and buttons"
- file: assets/images/badges/dc32/the-duck-badge/f64233f93a.jpg
  source: "http://hackthequack.com/"
  credit: "Red String Studio x The Crow & Pigeon"
  caption: "Annotated blueprint diagram of the Duck Badge showing quack counter, sound hole, quack button, and USB port"
contact:
  handles:
  - '@redstrngstudio'
  raw:
  - 'twitter handle:'
notes:
- The $100 price includes the optional sticker pack
status: released
sources:
- kind: sheet
  event: dc32
  row: 89
  updated: ''
- kind: url
  url: http://hackthequack.com/
  title: Duck Badge
  accessed: '2026-09-06'
  note: Current live page; confirms maker names and general concept, but is a later-year "we couldn't make it" notice rather than the original sale page.
- kind: url
  url: http://web.archive.org/web/20240811053926/http://hackthequack.com/
  title: Duck Badge 2024 (Wayback Machine capture, Aug 11 2024)
  accessed: '2026-09-06'
  note: 'Original DC32 adoption page: confirms $80 adoption fee, ~300 units, feature list (7-segment "quack counter," quack-together gameplay, puzzle/duck facts, on/off switch), and that the fee included badge, stickers, certificate, batteries, lanyard, and instructions.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    Confirmed via the Wayback Machine capture of the original 2024 sale page: price ($80),
    quantity (~300), and features match the community sheet. No maker's page states the
    MCU, LED count/type, or connectivity method for the "wireless" quacking (the board photo
    shows a coil-style antenna, suggesting RF or inductive signaling, but this is not
    confirmed by any source, so tech.connectivity is left empty rather than guessed).
    A linked "Duck Badge Care Instructions and Manual" PDF was referenced on the 2024
    page but is not preserved in the Wayback Machine, so it could not be checked. No
    GitHub repo, Hackaday.io project, or open-source design files were found for this
    badge. Availability is marked sold_out based on the current site's tone (it now
    reads as a post-event notice for a different year with only "remaining ducks"), but
    no explicit "sold out" statement was found, so confidence is medium rather than high.
last_modified_date: '2026-09-06'
---

The Duck Badge is a duck-shaped electronic badge sold by the collaboration of Red String Studio and The Crow & Pigeon at DEF CON 32 (2024) as a tongue-in-cheek "duck adoption." For an $80 "adoption fee," buyers received the badge itself, a sheet of duck-themed stickers, a mock adoption certificate, batteries, a lanyard, and instructions. Around 300 badges were made for the event.

The badge's black PCB is cut into a duck silhouette, with a coiled loop at the head standing in for the duck's "hair" (and doubling as an antenna), a built-in speaker at the "sound hole," and a 3-digit 7-segment display billed as a "quack counter." A button lets the wearer "quack" and, per the maker's description, wirelessly quack together with other Duck Badge wearers nearby; the exact wireless method (RF, IR, or something else) is not stated on the maker's site. The badge also included a small puzzle and some duck trivia for wearers to share.

No hardware files, firmware, or BOM were published for this badge, and no MCU, LED, or precise connectivity details could be confirmed from the maker's own materials. The original sale page is no longer live; the current site shows only a later notice that the makers could not attend that year's con and had leftover ducks up for adoption.
