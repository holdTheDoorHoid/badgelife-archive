---
title: Gunslinger-B-Gone and Sheriff SAO
id: dc33-gunslinger-b-gone-and-sheriff-sao
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: BigTaro's Badges
  url: https://bigtaro.net
summary: A wild-west-themed badge pair - a "Gunslinger-B-Gone" TV-B-Gone remote shaped like a revolver, and a companion Sheriff SAO that reacts to being "shot" with IR, sold by BigTaro's Badges for DEF CON 33 (2025).
functions: A wild west themed badge, works as a TV-B-Gone, "Laser Tag" with the Sheriff SAO, CTF, Drinking Game, and lots of bling.  Also interacts with BigTaro's other badges this year.
look:
  colors: []
  shape: null
  themes:
  - western
  - pop culture
  - security
tech:
  mcu: RP2040
  leds: null
  display: null
  connectivity:
  - ir
  battery: 18650 (Gunslinger-B-Gone); CR2032/LIR2032 (Sheriff SAO standalone kit)
  sao_version: v1
get_one:
  price: $140.00
  price_usd: 140.0
  quantity: ''
  availability: limited
  distribution:
  - purchase
  - free_drop
  where: Sold in person at the Hacker Warehouse booth in the DEF CON 33 (2025) vendor hall; leftover stock later listed on the maker's Tindie store; drop announcements posted on the maker's Bluesky and a Signal group.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: https://bigtaro.net/wwhfbadge25/GunslingerFirmware.1.1.uf2
  eda_tool: null
links:
- label: bigtaro.net
  url: https://bigtaro.net
  kind: website
- label: Gunslinger-B-Gone & Sheriff SAO badge page
  url: https://bigtaro.net/wwhfbadge25
  kind: website
  archived: https://web.archive.org/web/20260508142717/https://bigtaro.net/wwhfbadge25/
- label: Sheriff SAO standalone build guide
  url: https://bigtaro.net/wwhfbadge25/sheriffguide.html
  kind: doc
  archived: https://web.archive.org/web/20251208141217/https://bigtaro.net/wwhfbadge25/sheriffguide.html
- label: BigTaro on Tindie
  url: https://www.tindie.com/stores/bigtaro/
  kind: store
  archived: https://web.archive.org/web/20260503101828/https://www.tindie.com/stores/bigtaro/
- label: BigTaro on Bluesky
  url: https://bsky.app/profile/bigtaro.bsky.social
  kind: social
images:
- file: assets/images/badges/dc33/gunslinger-b-gone-and-sheriff-sao/de8ef8f815.jpg
  source: https://bigtaro.net/wwhfbadge25
  credit: BigTaro's Badges
  caption: Gunslinger-B-Gone badge, front
  archived: https://web.archive.org/web/20260508142717/https://bigtaro.net/wwhfbadge25/
- file: assets/images/badges/dc33/gunslinger-b-gone-and-sheriff-sao/962938f417.jpg
  source: https://bigtaro.net/wwhfbadge25/sheriffguide.html
  credit: BigTaro's Badges
  caption: Sheriff SAO worn standalone with battery kit
  archived: https://web.archive.org/web/20251208141217/https://bigtaro.net/wwhfbadge25/sheriffguide.html
contact:
  emails:
  - psymastr@hotmail.com
notes: []
status: released
sources:
- kind: sheet
  event: dc33
  row: 21
  updated: 7/10/2025 11:25:27
- kind: url
  url: https://bigtaro.net
  title: BigTaro's Badges (bigtaro.net)
  accessed: '2026-09-06'
  note: Maker's site terminal listing confirms this badge's official name, a plain-language feature summary, and links to the dedicated badge page.
- kind: url
  url: https://bigtaro.net/wwhfbadge25
  title: Gunslinger-B-Gone Badge & Sheriff SAO
  accessed: '2026-09-06'
  note: Primary source for functions, controls, firmware update process (UF2 drag-and-drop), known issues (linear charger caution), distribution (Hacker Warehouse vendor hall at DEF CON 33, Tindie leftovers, Bluesky/Signal drop announcements), and front/back badge photos.
  archived: https://web.archive.org/web/20260508142717/https://bigtaro.net/wwhfbadge25/
- kind: url
  url: https://bigtaro.net/wwhfbadge25/sheriffguide.html
  title: Gunslinger-B-Gone Sheriff SAO Standalone Build Guide
  accessed: '2026-09-06'
  note: Confirms the Sheriff SAO's MCU is an RP2040 ("stick a pad to the back of the rp2040 chip on the board"), the CR2032/LIR2032 standalone battery kit, the SAO connector attachment, and provided a photo of the worn Sheriff SAO.
  archived: https://web.archive.org/web/20251208141217/https://bigtaro.net/wwhfbadge25/sheriffguide.html
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: Maker's own badge page and build guide confirm functions, controls, and RP2040 MCU (explicitly named only for the Sheriff SAO; the Gunslinger-B-Gone's UF2-based firmware update strongly suggests the same MCU family but this was not stated outright, so tech.mcu is recorded for the pair with that caveat). LED count/type, display, and exact quantity made were not stated on any source found. Tindie store page (https://www.tindie.com/stores/bigtaro/) is behind a Cloudflare bot check and could not be fetched to confirm current stock/price for a standalone online listing; the $140 price is carried over from the community sheet and not independently confirmed by the maker's own page (which gives no price, only that units were sold at the DEF CON 33 Hacker Warehouse booth and any extras go to Tindie afterward).
last_modified_date: '2026-09-06'
---

The Gunslinger-B-Gone is a revolver-shaped TV-B-Gone badge from BigTaro's Badges for DEF CON 33 (2025), paired with a companion Sheriff SAO. Point the Gunslinger at a television and pull the trigger to power it off; the badge also plays "laser tag" against the Sheriff SAO, which lights up and reacts over IR when "shot." Beyond the core gimmick, the pair includes a CTF with hidden challenges that unlock extra features, a built-in drinking game, and numerous LED bling modes, and the badges are designed to interact with BigTaro's other 2025 badge line.

Both badges are user-programmable after the con. The Sheriff SAO's PCB is built around an RP2040 and can be worn standalone (it ships with a CR2032/LIR2032 battery, a magnetic battery holder, and a sticky pad for a simple solder-it-yourself build) or plugged into the Gunslinger-B-Gone's SAO port. The Gunslinger-B-Gone runs on an 18650 cell or USB power, updates its firmware via drag-and-drop UF2 files, and the maker notes it uses a linear charger, so it should only be charged while powered off to avoid stressing the battery under load.

Units were sold in person at the Hacker Warehouse booth in the DEF CON 33 vendor hall; any leftover stock was later offered through the maker's Tindie store, with drop announcements posted to BigTaro's Bluesky account and a Signal group. The community sheet lists a $140 price, which was not independently confirmed on the maker's own pages.
