---
title: Learn to Solder Badge
id: dc31-learn-to-solder-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Hak4Kidz Lab
  url: https://www.hak4kidz.com
summary: An unassembled soldering-practice kit shaped like Tinker, Hak4Kidz's gender-neutral robot mascot, with a DEF CON badge SAO connector.
functions: A guided soldering exercise -- populate LEDs, resistors, potentiometers, a switch and a battery holder, then use three potentiometers to adjust the color of Tinker's two RGB LED eyes.
look:
  colors: [black]
  shape: robot
  themes: [robot, mascot, learn to solder, kit]
tech:
  mcu: none
  leds:
    count: 2
    type: RGB
    note: Eye color is adjustable via three onboard potentiometers rather than a microcontroller.
  display: none
  connectivity: []
  battery: CR2032
  sao_version: v1
get_one:
  price: $20.00
  price_usd: 20.0
  quantity: '50 available'
  availability: available
  availability_note: 'Listed as purchasable on the Hak4Kidz Lab Tindie store, checked 2026-09-07.'
  distribution: [purchase, kit]
  where: Sold by Hak4Kidz Lab on Tindie; proceeds support the Hak4Kidz youth cybersecurity education mission.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: Hak4Kidz Learn to Solder Badge and SAO (Tindie)
  url: https://www.tindie.com/products/h4klab/hak4kidz-learn-to-solder-badge-and-sao/
  kind: store
- label: www.hak4kidz.com
  url: https://www.hak4kidz.com
  kind: website
images: []
contact: {}
notes:
- 'This entry duplicates dc31-learn-to-solder-badge-2, a separate sheet row (row 51) for what appears to be the same $20 Hak4Kidz badge sold at DC31; see research.notes.'
status: released
sources:
- kind: sheet
  event: dc31
  row: 35
  updated: '2023-07-21'
- kind: url
  url: https://www.tindie.com/products/h4klab/hak4kidz-learn-to-solder-badge-and-sao/
  title: Hak4Kidz Learn to Solder Badge and SAO (Tindie)
  accessed: '2026-09-07'
  note: Product description, price, quantity/kit contents, SAO connector, LED and potentiometer details, maker; used to identify this row as a likely duplicate of dc31-learn-to-solder-badge-2.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    This sheet row (row 35, "Learn to Solder Badge", $20, no maker/links) matches
    dc31-learn-to-solder-badge-2 (row 51, "Learn to solder badge", also $20, maker
    Hak4Kidz Lab, same Tindie listing) closely enough -- identical title concept,
    identical price, same event -- that it is treated here as the same physical
    product entered twice from two different sheet rows, rather than a second
    distinct badge. Filled in the maker, description, and technical/commercial
    details from the fuller sibling entry's research rather than duplicating a
    fresh web search. No separate hardware/Gerber files were found published for
    it, and no MCU is used (the board is a passive analog circuit using
    potentiometers to mix LED color).
last_modified_date: '2026-09-07'
---

This appears to be the same badge as `dc31-learn-to-solder-badge-2`, entered from a different row of the DC31 community sheet. Both rows describe a $20 "Learn to Solder" badge for DEF CON 31 (2023), and research on the sibling entry identified it as the Hak4Kidz Learn to Solder Badge and SAO: a beginner soldering kit sold by Hak4Kidz Lab, the hardware arm of Hak4Kidz, a nonprofit running youth cybersecurity and hacking education events.

The kit centers on "Tinker," Hak4Kidz's gender-neutral robot mascot, and is built as an unofficial badgelife SAO: builders solder on two RGB LEDs for Tinker's eyes, three potentiometers, resistors, a switch, a CR2032 battery holder, and a SAO connector so the finished piece can plug into a host conference badge. Eye color is mixed by hand via the three potentiometers rather than by a microcontroller. All proceeds support the Hak4Kidz mission of introducing kids to hacking and security concepts.

Because this row carries no maker name or links of its own on the sheet, and the sibling row (row 51) supplies a fuller record of the same $20 item, this entry is treated as a likely duplicate rather than researched independently from scratch.
