---
title: Learn to solder badge
id: dc31-learn-to-solder-badge-2
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
  availability_note: 'Listed as purchasable on the Hak4Kidz Lab Tindie store, checked 2026-09-06.'
  distribution: [purchase, kit]
  where: Sold by Hak4Kidz Lab on Tindie; proceeds support the Hak4Kidz youth cybersecurity education mission.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: t.co/SUchUZ8Z7M
  url: https://t.co/SUchUZ8Z7M
  kind: website
- label: www.hak4kidz.com
  url: https://www.hak4kidz.com
  kind: website
- label: Hak4Kidz Learn to Solder Badge and SAO (Tindie)
  url: https://www.tindie.com/products/h4klab/hak4kidz-learn-to-solder-badge-and-sao/
  kind: store
images:
  - file: assets/images/badges/dc31/learn-to-solder-badge-2/1462b72936.png
    source: "https://www.tindie.com/products/h4klab/hak4kidz-learn-to-solder-badge-and-sao/"
    credit: "Hak4Kidz Lab"
    caption: "Hak4Kidz Learn to Solder Badge and SAO with Tinker robot BOM/assembly graphic"
contact: {}
notes:
- All proceeds go to the Hak4Kids mission. Please go check them out at https://www.hak4kidz.com.
- 'This entry duplicates dc31-learn-to-solder-badge, a separate sheet row for the same $20 Hak4Kidz badge sold at DC31; see research.notes.'
status: released
sources:
- kind: sheet
  event: dc31
  row: 51
  updated: '2023-07-21'
- kind: url
  url: https://www.tindie.com/products/h4klab/hak4kidz-learn-to-solder-badge-and-sao/
  title: Hak4Kidz Learn to Solder Badge and SAO (Tindie)
  accessed: '2026-09-06'
  note: Product description, price, quantity/kit contents, SAO connector, LED and potentiometer details, maker location.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    The t.co short link redirects to the Hak4Kidz Lab Tindie listing for this exact
    kit, which matches the sheet's $20 price and 50-unit quantity. This entry is a
    likely duplicate of dc31-learn-to-solder-badge (same event, same $20 price, same
    "learn to solder" concept, separate sheet row 35 with no maker/links filled in) --
    both appear to describe the same Hak4Kidz product from two different sheet rows.
    Could not confirm an MCU (the board appears to be a passive analog circuit using
    potentiometers to mix LED color rather than a microcontroller), and no separate
    hardware/Gerber files were found published for it.
last_modified_date: '2026-09-06'
---

The Learn to Solder Badge and SAO is a beginner soldering kit sold by Hak4Kidz Lab, the hardware arm of Hak4Kidz, a nonprofit that runs youth cybersecurity and hacking education events. Sold for $20 around DEF CON 31 (2023), the kit centers on "Tinker," Hak4Kidz's gender-neutral robot mascot, and is built as an unofficial badgelife SAO: builders solder on two RGB LEDs for Tinker's eyes, three potentiometers, resistors, a switch, a CR2032 battery holder, and a SAO connector so the finished piece can plug into a host conference badge. A QR code on the board links to assembly instructions, and a Hak4Kidz-branded lanyard is included. All proceeds support the Hak4Kidz mission of introducing kids to hacking and security concepts.

This entry appears to duplicate `dc31-learn-to-solder-badge`, a separate row from the same community sheet for DC31 that lists the identical $20 price with no maker or links filled in. Both most likely describe this same Hak4Kidz product, just entered twice from two different sheet rows.
