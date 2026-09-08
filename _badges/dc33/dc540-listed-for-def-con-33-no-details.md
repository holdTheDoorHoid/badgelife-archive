---
title: DC540 METRO Analog Badge
id: dc33-dc540-listed-for-def-con-33-no-details
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: DC540
  url: https://dc540.org
summary: A free, screenless "analog" badge for DEF CON 33 styled as an homage to the Washington DC Metro map, with an RFID sticker on the back for a badge-scanning decode game.
functions: Each badge carries an RFID tag with a unique piece of data that attendees decrypt (with help from the DCNextGen community's M138-lite cipher project). Attendees scan other people's METRO badges and visit each badge's URL; every visit is logged, so a badge's page shows a running list of inbound and outbound visits.
look:
  colors:
  - multicolor
  shape: rectangle
  themes:
  - puzzle
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - rfid
  battery: none
  sao_version: none
get_one:
  price: free
  price_usd: 0
  quantity: a few hundred
  availability: free
  distribution:
  - free_drop
  where: Given away free at DEF CON 33 by DC540; the maker said they'd have "a few hundred on hand."
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'No PCB/hardware files (this is a paper/card badge, not electronics). DC540 published the "strips" cipher key file used for the RFID decode game: https://dc540.org/xxx/wp-content/uploads/2025/07/strips.txt'
links:
- kind: website
  label: DC540 METRO Analog Badge (DC33-2025) — project page
  url: https://dc540.org/xxx/dc540-badges-for-def-con/metro-analog-badge-dc33-2025/
  archived: https://web.archive.org/web/20260413082911/https://dc540.org/xxx/dc540-badges-for-def-con/metro-analog-badge-dc33-2025/
- kind: article
  label: DC540 has a badge for DEFCON this year (blog post)
  url: https://dc540.org/xxx/2025/07/dc540-has-a-badge-for-defcon-this-year/
- kind: social
  label: DC540 on Mastodon (defcon.social)
  url: https://defcon.social/@dc540
  archived: https://web.archive.org/web/20260606172302/https://defcon.social/@dc540
images:
- file: assets/images/badges/dc33/dc540-listed-for-def-con-33-no-details/edbc8432eb.jpg
  source: https://dc540.org/xxx/dc540-badges-for-def-con/metro-analog-badge-dc33-2025/
  credit: DC540
  caption: The DC540 METRO Analog Badge for DEF CON 33, a paper/card badge styled after the DC Metro system map
  archived: https://web.archive.org/web/20260413082911/https://dc540.org/xxx/dc540-badges-for-def-con/metro-analog-badge-dc33-2025/
contact: {}
notes:
- Sheet listed only "DC540" for DC33 with no other details; the badge itself was identified through DC540's own blog and Mastodon posts.
- DC540 is a Northern Virginia ("Nova regional, near Dulles") DEF CON group, not the Montreal group of a similar name.
- DC540 has made a different themed badge nearly every DEF CON: DC29 Tree of Life, DC30 Tarot, DC32 Chakra, and this DC33 Metro badge. These are not sold under one continuing "series" name, just a yearly one-off theme, so `series` is left blank.
status: released
sources:
- kind: sheet
  event: dc33
  row: 35
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://dc540.org/xxx/2025/07/dc540-has-a-badge-for-defcon-this-year/
  title: DC540 has a badge for DEFCON this year. – DC540
  accessed: '2026-09-06'
  note: Announcement post; confirms the badge exists, is deliberately simple (no blink, no screen), and links to the project page.
- kind: url
  url: https://dc540.org/xxx/dc540-badges-for-def-con/metro-analog-badge-dc33-2025/
  title: DC540 METRO Analog Badge (DC33-2025)
  accessed: '2026-09-06'
  note: 'Primary source: badge concept (DC Metro homage), RFID/decode game mechanics, free distribution, quantity (a few hundred), and the cipher strips file link.'
  archived: https://web.archive.org/web/20260413082911/https://dc540.org/xxx/dc540-badges-for-def-con/metro-analog-badge-dc33-2025/
- kind: url
  url: https://defcon.social/@dc540
  title: DC540 (@dc540@defcon.social)
  accessed: '2026-09-06'
  note: Confirmed DC540's identity/location (Northern Virginia group) and surfaced the DC33 badge announcement post via its status history.
  archived: https://web.archive.org/web/20260606172302/https://defcon.social/@dc540
- kind: url
  url: https://github.com/DC540-Nova
  title: DC540-Nova · GitHub
  accessed: '2026-09-06'
  note: Org repos show DC540's past badge projects (DC29 Tree of Life, DC30/Tarot, DC32 Chakra) but no DC33 repo — consistent with DC33 being a non-electronic badge.
  archived: https://web.archive.org/web/20260908003415/https://github.com/DC540-Nova
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: The maker's own project page and blog post confirmed the badge and its mechanics directly, so confidence is high. No maker photo of the badge's reverse (RFID sticker) side was found, and no image showing the "M138-lite cipher" itself. Exact LED/color breakdown of the Metro-map graphic wasn't independently confirmed beyond the one photo saved.
last_modified_date: '2026-09-06'
---

DC540, the Northern Virginia DEF CON group, made a deliberately low-tech badge for DEF CON 33 after deciding tariffs, time constraints, and the effort that went into the prior year's Chakra badge (a full RP2040-based electronic badge with a screen) made another elaborate build impractical. The result is the METRO Analog Badge: a paper/card badge styled as an homage to the Washington DC Metro system map, a nod to family history — the maker's grandfather and great-grandfather worked for DC Transit, WMATA's predecessor (DC540 notes it has no official connection to WMATA or Metro).

To keep a "tech" element in the spirit of the con, each badge carries an RFID sticker on the back encoding a unique piece of data that the holder has to decrypt, with a assist available from the DCNextGen community's M138-lite cipher project; DC540 published the cipher's "strips" key file publicly. A second layer of the game has attendees scan each other's badges and visit the URL encoded on them, building a logged, mutual record of who has scanned whom.

The badge was free, with DC540 planning to bring a few hundred to give away at the con, and the maker was candid that the social game had not been tested ahead of time ("None of this has been tested in the wild. It'll be an adventure.").
