---
title: SECYC Marvin Badge
id: dc32-secyc-marvin-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Social Engineering Community Youth Challenge
  url: https://www.se.community/youth-challenge/
summary: A learn-to-solder badge shaped like Marvin the Paranoid Android from "The Hitchhiker's Guide to the Galaxy," given free to kids competing in the 2024 SEC Youth Challenge at DEF CON 32.
functions: Arrives with components missing; youth challengers solder Marvin's parts on themselves as part of the competition to "repair" him and make him functional again.
look:
  colors: []
  shape: robot
  themes:
  - robot
  - sci-fi
  - learn to solder
  - kit
tech:
  mcu: null
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: Free
  price_usd: 0.0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  - contest
  where: Given free to registered youth participants in the 2024 SEC Youth Challenge (DEF CON 32) as part of one of the competition's challenges; supplies were limited, so the organizers recommended pre-registering to guarantee a spot. Any surplus left over at the con was to be sold for $100 to help fund the challenge.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: www.se.community/youth-challenge
  url: https://www.se.community/youth-challenge/
  kind: website
- label: twitter.com/sec_defcon
  url: https://twitter.com/sec_defcon
  kind: social
images:
- file: assets/images/badges/dc32/secyc-marvin-badge/9790e4590d.jpg
  source: "https://www.se.community/youth-challenge/"
  credit: "Social Engineering Community"
  caption: "The Marvin badge, a learn-to-solder kit shaped like Marvin the Paranoid Android from The Hitchhiker's Guide to the Galaxy"
contact: {}
notes:
- It will be free to all youth challenge participants. If we have extra later in the con, we will sell them for $100 to help support the challenge, but it will be a limited qty. We recommend youth challenger pre-register to guarantee their spot. https://www.se.community/youth-challenge/
status: released
sources:
- kind: sheet
  event: dc32
  row: 101
  updated: '2024-07-24'
- kind: url
  url: https://www.se.community/youth-challenge/
  title: Youth Challenge | Social Engineering Community
  accessed: '2026-09-06'
  note: Current page confirms the 2024 SEC Youth Challenge program and that it later moved to DC NextGen, but no longer carries the 2024 Marvin badge copy or photo.
- kind: url
  url: http://web.archive.org/web/20240814210231/https://www.se.community/youth-challenge/
  title: "Youth Challenge (archived, Aug 2024) | Social Engineering Community"
  accessed: '2026-09-06'
  note: "Wayback capture from the DEF CON 32 run year: describes Marvin as the youth-challenge badge, that it ships with missing components challengers must solder on to make it functional, that it was free with limited supply, and any surplus would be sold at $100. Source of the badge photo."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: 'The live se.community youth-challenge page has since been overwritten with a "program discontinued" notice, so all badge-specific detail comes from an August 2024 Wayback Machine capture of that same page (the only source found describing Marvin). No mentions of chip, LEDs, battery, or design files were found anywhere -- Marvin appears to be a passive/solder-practice board rather than an electronic badge with onboard intelligence, but that was not stated outright, so tech.mcu etc. are left empty rather than guessed. Could not reach x.com/sec_defcon (redirect not fetchable by available tools) to check for additional photos or details. No Hackaday.io project, repo, or storefront listing was found.'
last_modified_date: '2026-09-06'
---

The SECYC Marvin Badge was the 2024 giveaway badge for the Social Engineering Community's Youth Challenge (SECYC) at DEF CON 32, a competition that taught kids cryptography, social engineering, and network security skills through a Hitchhiker's Guide to the Galaxy-themed storyline about stopping the universe from imploding. Marvin -- named for the perpetually depressed robot of the books -- was framed as broken and in need of repair: participants who registered for the challenge received the badge for free and had to solder its missing components onto the board themselves to bring it "back to life" as part of the competition.

Supplies were limited and pre-registration was recommended to guarantee a badge. Any badges left over after the youth competitors were served were to be sold at the con for $100, with proceeds going back into funding the challenge. No schematic, firmware, or component list was found in any source, so it isn't confirmed whether Marvin carries any onboard electronics (LEDs, a microcontroller) beyond whatever discrete parts youth challengers solder on, or whether it is purely a solder-practice board; this entry leaves those tech fields empty rather than guess.
