---
title: BSides Orlando 2023 Badge (Rise of the Robots)
id: bsides-orlando-2023-bsides-orlando-2023-badge-rise-of-the-robots
layout: badge
parent: 'BSides Orlando 2023: Rise of the Robots'
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-orlando-2023
year: 2023
makers:
- name: BSides Orlando
  url: https://github.com/bsidesorlando
  role: 'Badge team: @infosecanon, @notthatguy, @joehacksalot (credited on the PCB silkscreen)'
summary: The official conference badge for BSides Orlando 2023, themed "Rise of the Robots." It is a simple coin-cell-powered PCB badge with self-blinking LEDs and an SAO port, with no onboard microcontroller.
functions: 'Lights up on power-up: three "fast blink" LEDs and one "breathing" LED cycle automatically (no MCU driving them), plus a black 3mm infrared LED. An on/off slide switch controls power, and a 2x3 SAO header lets attendees plug in add-on boards.'
look:
  colors: []
  shape: null
  themes:
  - robot
  - security
tech:
  mcu: none
  leds:
    count: 5
    type: discrete
    note: 'Three self-flashing "Fast Blink 3mm LED" units, one "Breathing 3mm LED" unit, and one 3mm black infrared LED (opto); no microcontroller drives them.'
  display: none
  connectivity:
  - ir
  battery: CR2032 (Keystone 3002 coin-cell holder)
  sao_version: v2
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/bsidesorlando/2023-badge/tree/main/bsidesorl-v1
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/bsidesorlando/2023-badge
  url: https://github.com/bsidesorlando/2023-badge
  kind: repo
images: []
contact: {}
notes:
- 'Sweep found the repo but no README/maker credit visible on the repo page; maker attribution here comes from text embedded in the PCB silkscreen itself, read directly from the .kicad_pcb file (not from a rendered page). The sweep''s tentative "BadgePirates(?)" credit is not supported: BadgePirates'' own project catalog (docs.badgepirates.com/catalog) lists their 2023 badges (BSidesKC, BSidesSTL, CactusCon, DEF CON Biohack Village) and does not include a BSides Orlando badge.'
status: released
sources:
- kind: url
  url: https://github.com/bsidesorlando/2023-badge
  title: BSides Orlando 2023 Badge (Rise of the Robots)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-orlando); event read as ''bsides-orlando-2023''.'
- kind: url
  url: https://github.com/bsidesorlando/2023-badge/blob/main/bsidesorl-v1/bsidesorl-v1.kicad_pcb
  title: bsidesorl-v1.kicad_pcb (main badge board file)
  accessed: '2026-09-10'
  note: 'Read directly for hardware details: no MCU footprint, CR2032 holder, 3x self-blinking LED + 1x breathing LED + 1x IR LED, slide switch, 2x3 SAO header, and the "Badge Team: @infosecanon @notthatguy @joehacksalot" silkscreen credit.'
- kind: url
  url: https://bsidesorlando.org/conference-23-announcement/
  title: 2023 BSides Orlando Dates - Security BSides Orlando
  accessed: '2026-09-10'
  note: 'Confirms the "Rise of the Robots" 2023 conference theme and Oct 6-7, 2023 dates at Full Sail Live.'
- kind: url
  url: https://docs.badgepirates.com/catalog/
  title: Badge Catalog - BadgePirates Documents
  accessed: '2026-09-10'
  note: 'BadgePirates'' own badge catalog has no BSides Orlando 2023 entry, ruling out the sweep''s tentative BadgePirates attribution.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Confirmed as a real, released badge via its own KiCad hardware repo, whose PCB silkscreen credits a badge team (handles @infosecanon, @notthatguy, @joehacksalot) rather than an outside vendor. No README, storefront, press writeup, or photo of the assembled badge was found, so price, quantity, distribution method, exact board shape/color, and PCB image remain unconfirmed. The repo folder also contains several other SAO board files (dc239-sao, dc321-sao, dc321-2-sao, dc407-sao, iwc-iron-sao, bsidesorl-otgg-sao, bsidesorl-speaker-sao, bsidesorl-sponsor-sao, bsidesorl-staff-sao) that are separate items from this main badge; see reported "other items."'
last_modified_date: '2026-09-10'
---

The BSides Orlando 2023 badge was made for that year's conference, themed "Rise of the Robots," held October 6-7, 2023 at Full Sail Live. Its hardware design is published as a KiCad project on the BSides Orlando GitHub organization, in a folder alongside several related SAO boards. The badge itself carries no microcontroller: it is a coin-cell-powered board with a slide switch, three self-flashing LEDs, one "breathing" LED, and a single black 3mm infrared LED, all firing on their own without any firmware driving them. A 2x3 header gives it a standard SAO port so attendees could plug in add-on boards.

The community sheet that seeded this archive entry credited the badge to "BSides Orlando / BadgePirates(?)," but that attribution does not hold up: BadgePirates' own project catalog lists their other 2023 conference badges and has no entry for BSides Orlando. The actual credit, found directly in the PCB's silkscreen text, is a "Badge Team" of three handles — @infosecanon, @notthatguy, and @joehacksalot — working under the BSides Orlando organization.

No README, storefront listing, press coverage, or photo of an assembled unit turned up, so this entry cannot yet confirm the badge's price, production quantity, exact color or shape, or how it was distributed to attendees (registration freebie is likely for an official con badge but is not stated anywhere found).
