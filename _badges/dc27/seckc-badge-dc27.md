---
title: SecKC Badge (DC27)
id: dc27-seckc-badge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: SecKC / Badge Pirates (@badgepirates)
summary: A DEF CON 27 badge that gets its "bling" from 645 green LEDs and a silhouette-shaped second board layered on top, rather than from multi-colored LEDs.
functions: Lights up 645 green LEDs in patterns stored in EEPROM; no interactive game or radio function reported.
look:
  colors:
  - green
  shape: null
  themes:
  - security
tech:
  mcu: ATmega328
  leds:
    count: 645
    type: discrete
    note: Green LEDs only; driven by an ATmega328 programmed via the Arduino IDE, with animation patterns stored in EEPROM.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '150'
  availability: sold_out
  distribution:
  - purchase
  - preorder
  where: Sold to the SecKC / Badge Pirates community around DEF CON 27 (2019); about 90 were presold ahead of the 150 built.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/wp-content/uploads/2019/08/SecKC-DC27-badge-wide.jpg
  url: https://hackaday.com/wp-content/uploads/2019/08/SecKC-DC27-badge-wide.jpg
  kind: article
- label: 'Hackaday: "The Badgies: Clever, Crazy, and Creative Ideas In Electronic Design"'
  url: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  kind: article
  archived: https://web.archive.org/web/20260210064529/https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
- label: store.badgepirates.com/product/preorder-seckc-defcon-27-badge
  url: https://store.badgepirates.com/product/preorder-seckc-defcon-27-badge/
  kind: store
- label: SecKC DC27 Badge (Tindie)
  url: https://www.tindie.com/products/BadgePirates/seckc-dc27-badge/
  kind: store
images:
- file: assets/images/badges/dc27/seckc-badge-dc27/ab6f5932fa.jpg
  source: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  credit: Hackaday / Badge Pirates
  caption: SecKC DC27 badge, front, showing the green LED lit silhouette-shaped top board
  archived: https://web.archive.org/web/20260210064529/https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
- file: assets/images/badges/dc27/seckc-badge-dc27/e62bfa2b1f.jpg
  source: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  credit: Hackaday / Badge Pirates
  caption: SecKC DC27 badge with the top silhouette board removed, showing the larger LED array beneath
  archived: https://web.archive.org/web/20260210064529/https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
contact: {}
notes:
- image URL only; 150-unit run, 645 LEDs
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'Duplicate: this is the same badge as dc27-seckc-badge-dc27 (SecKC Badge (DC27)), just captured from the storefront''s preorder listing page rather than press coverage. The store.badgepirates.com domain no longer resolves (checked 2026-09-07); details filled in from Tindie and Hackaday coverage of the same badge.'
status: released
sources:
- kind: url
  url: https://hackaday.com/wp-content/uploads/2019/08/SecKC-DC27-badge-wide.jpg
  title: SecKC Badge (DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  title: 'The Badgies: Clever, Crazy, and Creative Ideas In Electronic Design'
  accessed: '2026-09-07'
  note: Source for maker (SecKC / Badge Pirates), LED count (645), quantity (150 built, ~90 presold), construction (ATmega328, Arduino IDE, EEPROM patterns, silhouette-shaped second board hiding the battery), and yield/rework issues.
  archived: https://web.archive.org/web/20260210064529/https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
- kind: url
  url: https://store.badgepirates.com/product/preorder-seckc-defcon-27-badge/
  title: SecKC Defcon 27 Badge (preorder)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''dc27''. Domain no longer resolves as of 2026-09-07, so page content could not be re-verified directly.'
- kind: url
  url: https://www.tindie.com/products/BadgePirates/seckc-dc27-badge/
  title: SecKC DC27 Badge
  accessed: '2026-09-07'
  note: Confirms maker (BadgePirates, Lee's Summit, MO), event/year (DEF CON 27, 2019), 645 LEDs driven by two IS31FL3741 drivers on the hexagonal LED board, modular mezzanine controller design, product now retired/unavailable, open source firmware referenced (BadgePiratesLLC/SecKCDC27 GitHub).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price, exact distribution channel details, and any open-source hardware/firmware files were not found in the Hackaday coverage or elsewhere; left empty rather than guessed. The badge's exact shape/silhouette design is not described beyond "silhouette-shaped." Merged with duplicate entry 'SecKC Defcon 27 Badge (preorder)' (dc27-seckc-defcon-27-badge-preorder).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc27/seckc-defcon-27-badge-preorder/
---

The SecKC Badge was built by the SecKC (Security KC) group's Badge Pirates crew for DEF CON 27 in 2019. Rather than chasing multi-colored LED effects, the team leaned into a single color: 645 green LEDs packed into the badge, driven by an ATmega328 programmed through the Arduino IDE with animation patterns stored in EEPROM.

The badge's visual trick is mechanical rather than electronic: a second, silhouette-shaped board sits on top of the main board, mounted on three connectors. That layering creates a sense of depth in the lighting and doubles as a hiding place for the battery between the two boards.

The group produced 150 badges, having presold roughly 90 of them ahead of the event. Hand-assembly at that density came with a cost — every badge needed rework on at least one LED (placed backwards or otherwise faulty), and about half needed more extensive attention than that.

## Notes merged from the duplicate entry "SecKC Defcon 27 Badge (preorder)"

This listing is the BadgePirates storefront's preorder page for the SecKC DEF CON 27 badge, the same badge documented in more depth (with photos) in the [SecKC Badge (DC27)](../seckc-badge-dc27) entry. The badge is built around 645 green LEDs, with a silhouette-shaped second board layered on top for a sense of depth, and was produced by SecKC's Badge Pirates crew for DEF CON 27 in 2019.

BadgePirates built 150 of these badges, with roughly 90 presold through listings like this one ahead of the event; by the time of this research the storefront domain (store.badgepirates.com) no longer resolves, and a related Tindie listing for the same badge shows it as retired/no longer available. A Tindie summary of the badge describes a mezzanine controller with two IS31FL3741 LED driver chips, which does not fully match the ATmega328/EEPROM-based description found in Hackaday's contemporary coverage — this may reflect a design revision, a related SKU from the same team (BadgePirates also sold a "SecKC Defcon Party Badge" SAO and "Party Star" for the same event), or simply imprecise secondhand description; it is noted here rather than resolved.

Because this entry and dc27-seckc-badge-dc27 describe the same physical badge, no new images were saved here — see the linked entry for photos.
