---
title: APPSEC COMMUNITY BADGE
id: saintcon-2022-appsec-community-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Jup1t3r
summary: A SAINTCON 2022 community minibadge carrying the OWASP wasp mascot, given out at the AppSec Community booth.
functions: 'Passive: two LEDs (D1, D2) light up when the minibadge is chained onto a powered SAINTCON badge; no onboard logic.'
look:
  colors:
  - yellow
  - black
  - white
  shape: rectangle
  themes:
  - security
  - logo
  - mascot
tech:
  mcu: none
  leds:
    count: 2
    type: null
    note: 'Two LEDs (silkscreened D1, D2) plus one resistor (R1); "single-pad method" hand-soldering called out in the maker''s instructions.'
  display: null
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given out by interacting with the AppSec Community folks at their booth at SAINTCON 2022.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=APPSEC%20COMMUNITY%20BADGE&year=2022
  url: https://minibadge.wiki/?search=APPSEC%20COMMUNITY%20BADGE&year=2022
  kind: website
images:
  - file: assets/images/badges/saintcon-2022/appsec-community-badge/fe35a87ff7.jpg
    source: "https://minibadge.wiki/?search=APPSEC%20COMMUNITY%20BADGE&year=2022"
    credit: "Jup1t3r / MiniBadge Wiki"
    caption: "Front of the AppSec Community minibadge, yellow-and-black wasp artwork nodding to OWASP"
  - file: assets/images/badges/saintcon-2022/appsec-community-badge/fd518bb888.jpg
    source: "https://minibadge.wiki/?search=APPSEC%20COMMUNITY%20BADGE&year=2022"
    credit: "Jup1t3r / MiniBadge Wiki"
    caption: "Back of the AppSec Community minibadge showing the two LEDs (D1, D2) and resistor (R1)"
contact: {}
notes:
- 'category: Official; rarity: Common'
- 'MiniBadge Wiki lists "Beginner" soldering difficulty and quantityMade as 0 (not tracked by the submitter), so quantity is left blank here rather than reported as zero made.'
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=APPSEC%20COMMUNITY%20BADGE&year=2022
  title: APPSEC COMMUNITY BADGE
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: SAINTCON minibadges (via minibadge.wiki community database)); event read as ''SAINTCON 2022''.'
- kind: url
  url: https://minibadge.wiki/2022.json
  title: MiniBadge Wiki 2022 data feed (APPSEC COMMUNITY BADGE entry)
  accessed: '2026-09-07'
  note: 'Underlying JSON record behind the minibadge.wiki listing: description, soldering instructions, difficulty, category, rarity, and how-to-acquire text, plus front/back image URLs. The wiki''s search page itself renders client-side and returned no content on a plain fetch/curl.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Confirmed via the MiniBadge Wiki community database (community-submitted, not the maker''s own page/store, so confidence is medium rather than high). No separate maker page, repo, or store listing found for Jup1t3r or this badge; price, exact quantity made, and PCB manufacturer are not stated by the source. Board art and LED layout were verified directly from the front/back PCB images (2022.json also confirms the object is a real, produced SAINTCON minibadge, not a spec/tool page).'
last_modified_date: '2026-09-07'
---

The AppSec Community Badge is a SAINTCON 2022 minibadge made by Jup1t3r, one of many small collectible add-ons that chain onto a SAINTCON attendee's main conference badge. Its front carries the OWASP wasp mascot over a yellow-and-black hazard-stripe background with "AppSec Community" lettered beneath it, referencing the AppSec Community group that runs a booth at SAINTCON. The back is a bare functional side: two LEDs (D1 and D2) and a single resistor (R1), soldered by the "single-pad" hand-soldering method, with four 2-position header pads at the corners for physically and electrically chaining it to a powered badge.

It has no onboard microcontroller — it is a passive add-on whose LEDs light from power supplied through the chain rather than any onboard logic. MiniBadge Wiki, a community-run database of SAINTCON minibadges, categorizes it as "Official" and "Common" rarity, with "Beginner" soldering difficulty. It was distributed for free at SAINTCON 2022 by talking to the AppSec Community team at their booth; no price, exact production quantity, or separate maker storefront/repo was found.
