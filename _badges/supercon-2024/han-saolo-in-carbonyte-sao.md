---
title: Han SAOlo in carbonyte
id: supercon-2024-han-saolo-in-carbonyte-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A Han Solo frozen in carbonite SAO by davedarko that uses exposed HASL copper for the silver slab look and silkscreen for a 3D "dimetric" effect, with an ATtiny412 driving five side-glow LEDs through a defreeze-scene blink animation; made for the Supercon 8 (2024) SAO contest and handed out there.
functions: Plays a scheduled RGB blink animation on five side-glow LEDs, timed to roughly follow the carbonite defreezing scene from Return of the Jedi. The black solder mask is see-through where there is no copper behind it, so Han's face appears to glow during the animation.
look:
  colors:
  - black
  - silver
  - copper
  shape: null
  themes:
  - sci-fi
  - movie
  - pop culture
tech:
  mcu: ATtiny412
  leds:
    count: 5
    type: SK6805-EC3210R
    note: side-glow/reverse-mount LEDs
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: '30'
  availability: free
  distribution:
  - free_drop
  - contest
  where: Handed out by the maker at Supercon 8 (2024); JLCPCB sponsored assembly of 30 units.
make_your_own:
  open_source: true
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SoloCarbonite
  firmware_url: null
  eda_tool: null
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/197803-han-saolo
  url: https://hackaday.io/project/197803-han-saolo
  kind: hackaday
  archived: https://web.archive.org/web/20260311225117/https://hackaday.io/project/197803-han-saolo
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/SoloCarbonite
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SoloCarbonite
  kind: repo
images:
- file: assets/images/badges/supercon-2024/han-saolo-in-carbonyte-sao/40249f99d2.jpg
  source: https://hackaday.io/project/197803-han-saolo
  credit: davedarko
  caption: Han SAOlo in Carbonite SAO, populated board
  archived: https://web.archive.org/web/20260311225117/https://hackaday.io/project/197803-han-saolo
- file: assets/images/badges/supercon-2024/han-saolo-in-carbonyte-sao/7ac6225c6a.jpg
  source: https://hackaday.io/project/197803-han-saolo
  credit: davedarko
  caption: Han SAOlo project cover image
  archived: https://web.archive.org/web/20260311225117/https://hackaday.io/project/197803-han-saolo
contact: {}
notes:
- The maker's own Hackaday.io components list gives ATtiny412 as the final MCU; a short project readme in the GitHub repo (2411_Hans_SAOLO.md) mentions an ATtiny13 from an earlier idea stage. The Hackaday.io page (with a bill of materials and build logs describing JLCPCB assembly) is treated as authoritative for the shipped version.
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/197803-han-saolo
  title: Han SAOlo by davedarko - Hackaday.io
  accessed: '2026-09-07'
  note: Primary source; description, build logs, components (1x ATtiny412, 5x SK6805-EC3210R), Supercon 8 SAO contest submission, JLCPCB-sponsored assembly of 30 units, connector details (JST-SH and 2x3 header), and photos.
  archived: https://web.archive.org/web/20260311225117/https://hackaday.io/project/197803-han-saolo
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/SoloCarbonite/2411_Hans_SAOLO.md
  title: Hans SAOLO project note (davedarko/Simple-Add-ons-SAO repo)
  accessed: '2026-09-07'
  note: Maker's short design note; mentions ATtiny13 as the chip used for scheduled blinking (differs from the Hackaday.io BOM, see research.notes).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event, design concept, LED count/type, distribution) confirmed by the maker''s own Hackaday.io project page and build logs. MCU has a minor source conflict: Hackaday.io BOM says ATtiny412, the GitHub repo''s short readme says ATtiny13 (likely an earlier design note left unupdated). No price/storefront listing found beyond free giveaway at Supercon; no separate firmware repo link found. look.shape left empty — sources describe a "dimetric" carbonite-slab silhouette but no single shape-vocabulary term fits well.'
last_modified_date: '2026-09-07'
---

Han SAOlo in Carbonite is a Simple Add-On (SAO) by davedarko (also known for other Simple-Add-ons-SAO releases), designed for the Supercon 8 (2024) SAO Contest. Inspired by another SAO that used exposed, tinned copper for a shiny metallic look, davedarko applied the same trick to recreate Han Solo's carbonite slab from Star Wars: exposed HASL copper stands in for the "silver" carbonite surface, while silkscreen linework and 45-degree "dimetric" angles give the flat PCB a sense of 3D depth.

The board is driven by an ATtiny412 and lights five SK6805-EC3210R side-glow LEDs in a scheduled blink sequence patterned after the carbonite defreezing scene in Return of the Jedi. A build quirk turned into a feature: the black solder mask is transparent wherever there's no copper underneath it, so Han's face glows during the animation. The board connects over both a JST-SH cable and a 2x3 pin header (I2C-capable), and carries a few in-joke silkscreen details, including a nod to an "AT-ATiny" pun from a social media comment.

JLCPCB sponsored assembly of 30 fully populated units, which the maker programmed and hand-glued before handing them out for free at Supercon. It was reportedly the most popular add-on davedarko distributed that year, prompting him to plan a future standalone version with a battery holder and pin/brooch mount for wearing without a host badge. Design files are published in davedarko's Simple-Add-ons-SAO GitHub repository.
