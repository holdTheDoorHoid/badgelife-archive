---
title: Tie-Dye BitHead SAO
id: dc32-tie-dye-bithead-sao
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: HackerBoxes
  url: https://hackerboxes.com/
summary: A skull-shaped SAO with a full-color tie-dye silkscreen and two LED "eyes," sold as one of six solder-practice SAO kits and assembled as part of HackerBox #0104 "Engage."
functions: No microcontroller; the two LEDs simply light up as the skull's eyes when the SAO is powered through its header.
look:
  colors:
  - black
  - multicolor
  shape: skull
  themes:
  - skull
  - kit
  - learn to solder
tech:
  mcu: none
  leds:
    count: 2
    type: discrete
    note: Two 5mm frosted LEDs (one appears red/pink, one blue) form the skull's eyes; the guide warns not to substitute 3mm clear LEDs.
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v2
get_one:
  price: $9.99
  price_usd: 9.99
  quantity: ''
  availability: sold_out
  availability_note: Listed as sold out on hackerboxes.com/products/simple-add-on-kits as of 2026-09-07.
  distribution:
  - purchase
  - kit
  where: Sold individually as a "Simple Add-On (SAO)" kit on the HackerBoxes Shopify store, and included as one of the build projects in HackerBox #0104 "Engage" (a $59 monthly subscription box shipped around the 2024 summer solstice, timed for DEF CON 32 / Hacker Summer Camp).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.instructables.com/HackerBox-0104-Engage/#step7
  url: https://www.instructables.com/HackerBox-0104-Engage/#step7
  kind: website
- label: HackerBoxes – Simple Add-On (SAO) kits
  url: https://hackerboxes.com/products/simple-add-on-kits
  kind: store
- label: HackerBoxes – HackerBox #0104 Engage
  url: https://hackerboxes.com/products/hackerbox-0104-engage
  kind: store
images:
  - file: assets/images/badges/dc32/tie-dye-bithead-sao/7516f9e20d.jpg
    source: "https://www.instructables.com/HackerBox-0104-Engage/#step7"
    credit: "HackerBoxes"
    caption: "Assembly diagram showing the Tie-Dye BitHead SAO (skull shape, tie-dye silkscreen, two LED eyes) alongside the other HackerBox 0104 SAOs"
  - file: assets/images/badges/dc32/tie-dye-bithead-sao/a18249d754.png
    source: "https://hackerboxes.com/products/simple-add-on-kits"
    credit: "HackerBoxes"
    caption: "Tie-Dye BitHead (top left) shown with the other five SAO kits in the HackerBoxes Simple Add-On lineup"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
status: released
sources:
- kind: url
  url: https://www.instructables.com/HackerBox-0104-Engage/#step7
  title: Tie-Dye BitHead SAO
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc32''.'
- kind: url
  url: https://hackerboxes.com/products/simple-add-on-kits
  title: Simple Add-On (SAO) – HackerBoxes
  accessed: '2026-09-07'
  note: Confirms price ($9.99), sold-out status, and that it is one of six solder-practice SAO kits (assembly covered in HackerBox 0104).
- kind: url
  url: https://hackerboxes.com/products/hackerbox-0104-engage
  title: HackerBox #0104 - Engage – HackerBoxes
  accessed: '2026-09-07'
  note: Confirms HackerBox #0104 price ($59) and that the Tie-Dye BitHead SAO is one of the box's build projects.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: HackerBox #0104 "Engage" shipped around the summer solstice in 2024, explicitly timed for "Hacker Summer Camp" (DEF CON 32/BSides Las Vegas), so event dc32/year 2024 is a good fit even though the SAO itself was not sold at DEF CON directly. No microcontroller is mentioned anywhere; it is a passive board with two LEDs. Exact LED colors (which eye is red vs. blue) are read from the assembly photo, not stated in text, so treated as visual observation rather than a maker claim.
last_modified_date: '2026-09-07'
---

The Tie-Dye BitHead is a skull-shaped Simple Add-On (SAO) from HackerBoxes, one of six solder-practice SAO kits ("Tie-Dye BitHead," "Artemis Mission," "Trippie the Space Sloth," "Mushroom Mushroom," "Phreakin' Clowns," and "Guy Fawkes Mask") sold individually for $9.99 through the HackerBoxes Shopify store. It has no microcontroller — it is a simple passive board with a full-color, UV-cured tie-dye silkscreen and two 5mm frosted LEDs standing in for the skull's eyes, powered through its SAO header from a host badge.

Assembly of the SAO is walked through as a build step in HackerBox #0104 "Engage," a $59 monthly subscription box from HackerBoxes that shipped around the summer solstice of 2024, explicitly timed for "Hacker Summer Camp" — DEF CON 32 and BSides Las Vegas. The same box also included an Alien Robot Badge kit (already a separate archive entry), a Galactic Power Badge kit, and HighRollerCon Duck SAOs distributed at DEF CON 32's High Roller event, none of which are covered by this entry.

As of research, the Tie-Dye BitHead is listed sold out on the HackerBoxes storefront. No hardware or firmware files are published for it, consistent with it being a simple solder-practice kit rather than an open-source project.
