---
title: Blue Team Community Badge
id: saintcon-2023-blue-team-community-badge
layout: badge
parent: Saintcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2023
year: 2023
makers:
- name: SHIFTY
summary: 'A SAINTCON 2023 community minibadge for the "Eiffel 65" Blue Team community, illustrating three hooded blue-hoodie figures over the text "EIFFEL 65 BLUE-TEAM".'
functions: 'No interactive functions; single-LED indicator badge. Collected at the Blue Team community booth, part of the minibadge trading/collecting game.'
look:
  colors:
  - blue
  - white
  - black
  shape: square
  themes:
  - security
  - text
  - minimalist
tech:
  mcu: null
  leds:
    count: 1
    type: reverse-mount
    note: Single LED (D1) with a single resistor (R1), soldered single-pad style; designators visible on the badge's own back photo, soldering method per the official 2023 Minibadge Guide.
  display: none
  connectivity: []
  battery: null
  sao_version: null
sao_ports: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Given out at the Blue Team ("Eiffel 65") community booth at SAINTCON 2023; the community page said details on how to collect it were still being worked out as of the con.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  kind: website
- label: SAINTCON 2023 Blue Team Community page
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/com-blueteam-community/
  kind: website
- label: MiniBadge Wiki (2023 catalog entry)
  url: https://minibadge.wiki/
  kind: website
images:
- file: assets/images/badges/saintcon-2023/blue-team-community-badge/b496ff95fd.png
  source: "https://minibadge.wiki/"
  credit: "SHIFTY"
  caption: "Front of the Blue Team Community minibadge"
- file: assets/images/badges/saintcon-2023/blue-team-community-badge/bedafc4786.png
  source: "https://minibadge.wiki/"
  credit: "SHIFTY"
  caption: "Back of the Blue Team Community minibadge"
contact: {}
notes:
- 2023 community minibadge for the Eiffel 65 Blue Team defensive-security community. Found by the event-year sweep, task saintcon-2023.
- 'The sweep''s title matches the maker''s own title exactly ("BLUE TEAM COMMUNITY BADGE"), confirmed via the MiniBadge Wiki 2023 data export.'
status: listed
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/wp-content/uploads/2023/10/2023_Minibadge_Guide_10.31.2023.pdf
  title: Blue Team Community Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2023); event read as ''saintcon-2023''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2023/saintcon.org/com-blueteam-community/
  title: 'COM - Blueteam Community - SAINTCON'
  accessed: '2026-09-10'
  note: 'Community page: confirms the community is nicknamed "Eiffel 65", focused on defensive security, and that the minibadge was distributed at the community booth; no design/price/quantity details given here.'
- kind: url
  url: https://minibadge.wiki/
  title: MiniBadge Wiki (2023.json data export)
  accessed: '2026-09-10'
  note: 'Maker-submitted catalog entry by SHIFTY for "BLUE TEAM COMMUNITY BADGE": description, soldering instructions (LED, resistor, pin headers, single-pad method, beginner difficulty), category Community, rarity Common, quantityMade listed as 0 (not recorded), and front/back photos, which were saved to images. The saved back photo itself shows exactly one LED and one resistor, silkscreened D1/R1.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Verification pass (2026-09-10): confirmed title, description, LED/resistor/header parts list and single-pad soldering method against both the maker-submitted MiniBadge Wiki 2023 data (minibadge.wiki/2023.json) and the official SAINTCON 2023 Minibadge Guide PDF, which independently agree. The saved front/back photos were checked byte-for-byte against the images hosted on minibadge.wiki and match; the back photo directly shows one LED (D1) and one resistor (R1), confirming tech.leds.count/note. Corrected one theme tag: "hardware tool" was dropped as unsupported and inconsistent with functions (no interactive/tool function) and replaced with "text" (large logotype is a dominant, verifiable design element). No price or quantity-made figure was published anywhere found; the wiki entry lists quantityMade as 0, which reads as "not recorded" rather than a real count, so get_one.quantity was left blank rather than guessed. No dedicated storefront, repo, or hardware files were found for this badge, so make_your_own and price/availability fields stay empty. A related but distinct v2 of this badge exists for SAINTCON 2024 (saintcon-2024-blue-team-community-minibadge-v2, made by a different author per the wiki data); this entry is specifically the 2023 original by SHIFTY.'
last_modified_date: '2026-09-10'
---

The Blue Team Community Badge is a SAINTCON 2023 minibadge made for the con's Blue Team community, nicknamed "Eiffel 65" after the band (a nod to the community's blue branding). The community itself is dedicated to defensive security — building and maintaining security tools, forensics, and related "blue team" disciplines — and the badge was given out at the community's booth at the conference as part of SAINTCON's long-running minibadge trading culture.

Electrically the badge is simple: a single reverse-mount LED (D1) and its current-limiting resistor (R1), both hand-solderable via the single-pad technique, plus pin headers to plug into a host badge. It carries no display, MCU, or wireless connectivity. The board art shows three hooded figures in blue hoodies above the text "EIFFEL 65 BLUE-TEAM", printed on blue solder mask with white silkscreen; the back carries the SAINTCON 2023 and SHIFTY maker credit along with the component silkscreen.

No price, print run, or storefront information was published for this badge — SAINTCON minibadges are typically free drops obtained by visiting the sponsoring community's table rather than sold. A separate, updated "v2" of this Blue Team community badge was made for SAINTCON 2024.
