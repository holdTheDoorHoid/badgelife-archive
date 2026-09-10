---
title: BSidesPR 2019 Badge (DIY ATtiny13A kit)
id: bsidespr-2019-bsidespr-2019-badge-luffy-badge-diy-attiny13a-kit
layout: badge
parent: BSides Puerto Rico 2019
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: bsidespr-2019
year: 2019
makers:
- name: soynerdito
  url: https://github.com/soynerdito
summary: A DIY through-hole soldering kit badge made for BSides Puerto Rico 2019, built around an ATtiny13A with two LEDs and a police-lights/fade light show.
functions: Runs sample ATtiny13A firmware that blinks two LEDs in "police lights" and "fade" patterns; toggled on/off with a slide switch.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - kit
  - security
tech:
  mcu: ATtiny13A
  leds:
    count: 2
    type: discrete
    note: one red, one blue LED, each behind a 680 ohm resistor
  display: none
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as a soldering/assembly kit to BSides Puerto Rico 2019 attendees; not sold as a product.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/soynerdito/BSidesPR_2019_Badge
  firmware_url: https://github.com/soynerdito/BSidesPR_2019_Badge
  eda_tool: KiCad
  license: Apache-2.0
  notes: Repo includes KiCad schematic/PCB/Gerbers, custom KiCad footprint libraries, and Arduino-IDE sample firmware. Build docs at https://bsidesprbadge2019.readthedocs.io/.
links:
- label: github.com/soynerdito/BSidesPR_2019_Badge
  url: https://github.com/soynerdito/BSidesPR_2019_Badge
  kind: repo
- label: badge.gallery/events/bsidespr-2019
  url: https://badge.gallery/events/bsidespr-2019
  kind: website
- label: BSides PR 2019 Badge Documentation (ReadTheDocs)
  url: https://bsidesprbadge2019.readthedocs.io/
  kind: doc
images:
  - file: assets/images/badges/bsidespr-2019/bsidespr-2019-badge-luffy-badge-diy-attiny13a-kit/d700f9fe08.jpg
    source: "https://github.com/soynerdito/BSidesPR_2019_Badge"
    credit: "soynerdito"
    caption: "Assembled front of the BSides Puerto Rico 2019 DIY ATtiny13A badge kit"
  - file: assets/images/badges/bsidespr-2019/bsidespr-2019-badge-luffy-badge-diy-attiny13a-kit/01362e5253.jpg
    source: "https://github.com/soynerdito/BSidesPR_2019_Badge"
    credit: "soynerdito"
    caption: "3D render of the BSides Puerto Rico 2019 DIY badge PCB"
contact: {}
notes:
- "The discovery sweep's title called this the 'Luffy Badge'; no source found (GitHub repo, badge.gallery, or the ReadTheDocs build guide) uses that name anywhere. Title corrected to drop it; original sweep wording preserved here for reference."
status: released
sources:
- kind: url
  url: https://github.com/soynerdito/BSidesPR_2019_Badge
  title: BSidesPR 2019 Badge (Luffy Badge / DIY ATtiny13A kit)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsidespr); event read as ''BSides Puerto Rico 2019''.'
- kind: url
  url: https://github.com/soynerdito/BSidesPR_2019_Badge
  title: soynerdito/BSidesPR_2019_Badge
  accessed: '2026-09-10'
  note: 'README and repo contents: DIY through-hole badge kit, KiCad design files, Arduino sample firmware, Apache-2.0 license; maker states it "is not a product for sale in any way, it''s for sharing and learning."'
- kind: url
  url: https://badge.gallery/events/bsidespr-2019
  title: BSides Puerto Rico 2019 - badge.gallery
  accessed: '2026-09-10'
  note: 'Confirms ATtiny13A, two red/blue LEDs, two 680 ohm resistors, slide switch, CR2032 battery, and "police lights and fade" sample firmware.'
- kind: url
  url: https://bsidesprbadge2019.readthedocs.io/
  title: BSides PR 2019 Badge Documentation
  accessed: '2026-09-10'
  note: 'Overview text and assembly steps; confirms DIY kit distribution and bill of materials; no mention of a "Luffy" name.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Core facts (maker, chip, LEDs, power, open-source status) are confirmed directly from the maker''s own repo, docs site, and badge.gallery, which all agree. Price and quantity made are not stated anywhere found, so left empty. No "Luffy" reference exists in any source; treated as a sweep error rather than an alternate name.'
last_modified_date: '2026-09-10'
---

The BSides Puerto Rico 2019 badge is a do-it-yourself, through-hole soldering kit that maker soynerdito designed for that year's conference, continuing a tradition of building a different badge for BSidesPR each year. Rather than being handed out fully assembled, it was distributed as a kit of DIP (through-hole) parts for attendees to solder themselves, aimed at people with little to no soldering experience.

Electrically it's simple by design: an ATtiny13A microcontroller drives two LEDs (one red, one blue) through 680 ohm current-limiting resistors, powered by a CR2032 coin cell and switched on with a slide switch. The included Arduino-IDE sample firmware runs a "police lights" pattern and a fade effect. All hardware (KiCad schematic, PCB layout, Gerbers, and custom footprint libraries) and firmware are published under an Apache-2.0 license on GitHub, with a step-by-step assembly guide hosted on ReadTheDocs. The maker states explicitly that the badge "is not a product for sale in any way, it's for sharing and learning," consistent with no price or quantity being listed anywhere.

## Make your own

All files needed to build one are in the GitHub repo: KiCad schematic and PCB source, Gerbers for fabrication, and Arduino sample code for the ATtiny13A. The ReadTheDocs site (bsidesprbadge2019.readthedocs.io) walks through the bill of materials and assembly order — resistors first, then LEDs, switch, and battery holder.
