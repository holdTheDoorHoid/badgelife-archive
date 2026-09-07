---
title: SecKC Defcon 27 Badge (preorder)
id: dc27-seckc-defcon-27-badge-preorder
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: BadgePirates
summary: A preorder storefront listing for the SecKC DEF CON 27 badge, a 645-green-LED badge with a silhouette-shaped second board layered on top.
functions: Lights up 645 green LEDs in patterns; no interactive game or radio function reported.
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
  where: Preorder listing on the BadgePirates storefront ahead of DEF CON 27 (2019); about 90 of the eventual 150-unit run were presold.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: store.badgepirates.com/product/preorder-seckc-defcon-27-badge
  url: https://store.badgepirates.com/product/preorder-seckc-defcon-27-badge/
  kind: store
- label: 'Hackaday: "The Badgies: Clever, Crazy, and Creative Ideas In Electronic Design"'
  url: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  kind: article
  archived: https://web.archive.org/web/20260210064529/https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
- label: SecKC DC27 Badge (Tindie)
  url: https://www.tindie.com/products/BadgePirates/seckc-dc27-badge/
  kind: store
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'Duplicate: this is the same badge as dc27-seckc-badge-dc27 (SecKC Badge (DC27)), just captured from the storefront''s preorder listing page rather than press coverage. The store.badgepirates.com domain no longer resolves (checked 2026-09-07); details filled in from Tindie and Hackaday coverage of the same badge.'
status: sold_out
sources:
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
- kind: url
  url: https://hackaday.com/2019/08/21/the-badgies-clever-crazy-and-creative-ideas-in-electronic-design/
  title: 'The Badgies: Clever, Crazy, and Creative Ideas In Electronic Design'
  accessed: '2026-09-07'
  note: Source for LED count (645), quantity (150 built, ~90 presold), construction (ATmega328, Arduino IDE, EEPROM patterns, silhouette-shaped second board hiding the battery).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This entry duplicates dc27-seckc-badge-dc27, which was researched independently and carries higher confidence (Hackaday as primary source with photos). The original storefront page for this preorder listing (store.badgepirates.com) no longer resolves, so its exact wording/price could not be directly confirmed; the Tindie listing for what appears to be the same badge describes an IS31FL3741-driven controller, which conflicts with the Hackaday account of an ATmega328 with EEPROM patterns — noting the disagreement rather than resolving it, since it is possible BadgePirates iterated the controller design between preorder and final production, or Tindie is describing a related but distinct SKU (e.g. the "SecKC Defcon Party Badge - SAO" or "Party Star" also sold by BadgePirates for the same event). Price and exact quantity attributable to this specific preorder listing (vs. the final production run) were not found.'
last_modified_date: '2026-09-07'
---

This listing is the BadgePirates storefront's preorder page for the SecKC DEF CON 27 badge, the same badge documented in more depth (with photos) in the [SecKC Badge (DC27)](../seckc-badge-dc27) entry. The badge is built around 645 green LEDs on a hexagonal PCB, with a silhouette-shaped second board layered on top for a sense of depth, and was produced by SecKC's Badge Pirates crew for DEF CON 27 in 2019.

BadgePirates built 150 of these badges, with roughly 90 presold through listings like this one ahead of the event; by the time of this research the storefront domain (store.badgepirates.com) no longer resolves, and a related Tindie listing for the same badge shows it as retired/no longer available. A Tindie summary of the badge describes a mezzanine controller with two IS31FL3741 LED driver chips, which does not fully match the ATmega328/EEPROM-based description found in Hackaday's contemporary coverage — this may reflect a design revision, a related SKU from the same team (BadgePirates also sold a "SecKC Defcon Party Badge" SAO and "Party Star" for the same event), or simply imprecise secondhand description; it is noted here rather than resolved.

Because this entry and dc27-seckc-badge-dc27 describe the same physical badge, no new images were saved here — see the linked entry for photos.
