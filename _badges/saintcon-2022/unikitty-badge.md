---
title: UniKitty
id: saintcon-2022-unikitty-badge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: Z3Thunder
summary: A personal minibadge shaped like a cat riding a lightning bolt, with a unicorn horn, made by Z3Thunder for their daughter.
functions: Lights up two LEDs (front horn/body highlight and the lightning bolt); otherwise a static novelty minibadge.
look:
  colors:
  - purple
  - gold
  shape: cat
  themes:
  - cat
  - mascot
  - fantasy
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two through-hole LEDs (D1, D2) with single-pad hand-soldering pads; hot glue recommended over the LEDs for diffusion.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - swap
  where: Traded in person with the maker (Z3Thunder) at SAINTCON 2022; the build guide says simply "ask her for one."
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  kind: website
images:
  - file: assets/images/badges/saintcon-2022/unikitty-badge/unikitty-front.png
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "Z3Thunder / SAINTCON"
    caption: "UniKitty minibadge PCB art: a horned cat riding a lightning bolt, purple board with gold silkscreen"
  - file: assets/images/badges/saintcon-2022/unikitty-badge/unikitty-back.png
    source: "https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf"
    credit: "Z3Thunder / SAINTCON"
    caption: "UniKitty minibadge back side, showing the 'Z3Thunder' and 'Meow' silkscreen and header pads"
contact: {}
notes:
- Personal UniKitty-themed minibadge by Z3Thunder. Found by the event-year sweep, task saintcon-2022.
- The 2022 SAINTCON MiniBadge Assembly Guide (page 74-75) lists the title simply as "UniKitty" (no "Badge" suffix); the sweep's title "UniKitty Badge" is kept as the entry filename/id but the maker's own wording is used for the `title` field.
- Listed with difficulty "beginner" and rarity "rare" in the guide.
status: listed
sources:
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: UniKitty Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2022); event read as ''saintcon-2022''.'
- kind: url
  url: https://saintcon.zip/SAINTCON_2015-2022/archive.saintcon.org/2022/saintcon.org/wp-content/uploads/2022/10/MiniBadges-of-2022-v2.pdf
  title: 'SAINTCON MiniBadge Assembly Guide 2022 — UniKitty (pages 74-75)'
  accessed: '2026-09-10'
  note: 'Confirmed the badge is real and pulled title, maker, description, difficulty/rarity, LED count, and assembly notes directly from the PDF build guide text and embedded PCB artwork images.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: >
    Confirmed via the official 2022 SAINTCON MiniBadge Assembly Guide PDF (pages 74-75), which is
    the maker-adjacent primary source for SAINTCON minibadges (published by SAINTCON, describing
    each submitted design). Could not find any independent page, storefront, repo, or social
    profile for Z3Thunder or this specific badge outside the guide, so confidence is medium rather
    than high. Distribution ("just ask her for one, she'd especially love to trade") implies a
    real, informal, in-person trade at the con with no fixed quantity or price; get_one.quantity
    and hardware/firmware sources are left empty since no source states them. No SAO header is
    used; it connects via a 4x 2-position header set (minibadge-style), not a 6-pin SAO connector,
    so tech.sao_version is set to none.
last_modified_date: '2026-09-10'
---

UniKitty is a SAINTCON 2022 minibadge designed by Z3Thunder as a personal icon for their
daughter, described in the official build guide as "lover of Unicorns and Kitty whisperer." The
board depicts a horned cat riding a lightning bolt, rendered in gold silkscreen over a purple
PCB, with the maker's handle and "Meow" lettered on the back.

It is a simple beginner-level minibadge: two through-hole LEDs (D1 and D2) soldered with the
single-pad hand-soldering method, plus four 2-position headers. The guide suggests hot-gluing
over the LEDs and the unmasked back area for a better lighting/diffusion effect. SAINTCON's guide
marks it "RARE" for trading rarity.

Distribution was informal and in-person: the build guide simply instructs attendees to ask
Z3Thunder for one, noting she especially enjoys trading. No price, print run, or online
storefront is documented, and no hardware or firmware files are published.
