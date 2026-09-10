---
title: LOCKPICKING BADGE
id: saintcon-2022-lockpicking-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Redactd
summary: A SAINTCON 2022 official minibadge for the Lock Picking Village, handed out (or earned by picking a lock) at the Lock Picking Community area.
functions: Simple LED minibadge; no interactive functions beyond lighting up once assembled.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - village badge
tech:
  mcu: none
  leds:
    count: null
    type: discrete
    note: Soldered by the builder using the single-pad hand-soldering method; exact LED count/type not stated by the source.
  display: none
  connectivity: []
  battery: battery held in place by spring contacts (four springs inserted into positions to complete the circuit); battery type not stated by the source
  sao_version: none
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  availability_note: 'Checked minibadge.wiki 2026-09-07; listed as quantityMade: 0 (not recorded by the source), category Official, rarity Common.'
  distribution:
  - free_drop
  - village
  where: Handed out at the SAINTCON Lock Picking Village; per the maker, "They MAY make you pick a lock to earn one, or they may just be handing them out."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=LOCKPICKING%20BADGE&year=2022
  url: https://minibadge.wiki/?search=LOCKPICKING%20BADGE&year=2022
  kind: website
images:
- file: assets/images/badges/saintcon-2022/lockpicking-badge/f30bf005b1.jpg
  source: https://minibadge.wiki/?search=LOCKPICKING%20BADGE&year=2022
  credit: Redactd / SAINTCON Lock Picking Village
  caption: Front of the Lock Picking minibadge PCB artwork, showing the 'by redactd' credit and unpopulated footprints for the LED, resistor, and spring components
- file: assets/images/badges/saintcon-2022/lockpicking-badge/876ba22736.jpg
  source: https://minibadge.wiki/?search=LOCKPICKING%20BADGE&year=2022
  credit: Redactd / SAINTCON Lock Picking Village
  caption: Back of the Lock Picking minibadge PCB artwork, showing the 'LOCKPICK' graphic and the four spring-contact footprints
contact: {}
notes:
- 'category: Official; rarity: Common'
- quantityMade recorded as 0 on minibadge.wiki, which the site appears to use to mean "not recorded" rather than none made, since the badge was clearly distributed.
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=LOCKPICKING%20BADGE&year=2022
  title: LOCKPICKING BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2022''.'
- kind: url
  url: https://minibadge.wiki/2022.json
  title: Minibadge Wiki - 2022 data (LOCKPICKING BADGE entry)
  accessed: '2026-09-07'
  note: 'Underlying JSON record for this listing: description, soldering instructions, maker, category, rarity, and front/back image paths. The wiki page itself is JS-rendered and does not show data via a plain fetch, so the data file behind it was read directly.'
  archived: https://web.archive.org/web/20260611101915/http://minibadge.wiki/2022.json
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Only source found is the minibadge.wiki community database; no maker-run page, repo, or storefront located for this specific badge. LED count/type, exact colors/shape, and any design files are not stated anywhere found. No web search results turned up beyond the wiki (a WebSearch budget limit was hit before broader searches on "Redactd" could be run). Verification pass (2026-09-07): re-fetched minibadge.wiki/2022.json directly and confirmed maker, category, rarity, quantityMade, description, and acquisition text word-for-word. Corrected one overclaim: the source never says the battery is a coin cell, only that four springs complete the circuit to an unspecified battery, so tech.battery and the body were reworded to drop "coin cell". Also corrected both image captions: the two images are unpopulated PCB artwork/silkscreen renders (footprint outlines for LEDs/resistor/springs and a "by redactd" / "LOCKPICK" graphic), not photos of an assembled badge, so "assembled with LEDs" was
    removed. Confirmed via sha1(url) that the front/back file assignment matches the source''s own front.png/back.png filenames. Everything else in the entry is supported by the source as re-read.'
last_modified_date: '2026-09-07'
---

The Lock Picking Badge is a SAINTCON 2022 official minibadge made for the con's Lock Picking Village, credited to maker Redactd. It's a simple hand-solder kit: a few LEDs and a resistor go on using the single-pad method, and the badge is powered by a battery held in place with four springs that complete the circuit rather than a soldered battery holder (the source doesn't specify the battery type). There's no microcontroller or SAO header — it's a passive, always-on LED badge once assembled.

Distribution was informal, in keeping with SAINTCON's village-badge culture: attendees got one either by visiting the Lock Picking Community and asking, or in some years by picking a lock to earn it. The badge carries the village's message that "everything is vulnerable if you know how it works," tying the giveaway to the village's teaching mission around lockpicking as a way of thinking about security.

No maker-run project page, repository, or storefront was found for this specific badge; the only record located is its listing on the minibadge.wiki community database, which supplied the description, soldering instructions, and photos used here.
