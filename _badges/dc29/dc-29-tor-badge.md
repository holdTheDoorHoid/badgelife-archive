---
title: Tor Polygraph (Lie Detector) Badge
id: dc29-dc-29-tor-badge
layout: badge
parent: DC29
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc29
year: 2021
makers:
- name: Gigs (@gigstaggart)
  role: PCB and hardware design
- name: SeeEss (@see_ess)
  role: software development and marketing
summary: A DEF CON 29 badge built as a miniature lie detector, combining an optical heart-rate monitor and a galvanic skin response sensor with dual OLED graphs. It also doubled as the entry point to a multi-layer crypto/puzzle challenge, with proceeds going to the Tor Project.
functions: Graphs live heart rate (via a reverse-mounted green LED sensor) and galvanic skin response on two OLED displays; also hosts a hidden multi-stage puzzle (Konami-code menu, morse code on the lanyard, Vigenère cipher, Game Genie codes, What3Words, a custom "onion layer" cipher) documented in a public walkthrough.
look:
  colors: []
  shape: null
  themes:
  - privacy
  - security
  - puzzle
  - ctf
tech:
  mcu: SAMD21 (Seeeduino XIAO)
  leds:
    count: 5
    type: reverse-mount
    note: Four onboard XIAO LEDs plus one reverse-mounted green LED used as the heart-rate sensor.
  display: 2x 1.3" I2C OLED
  connectivity: []
  battery: 2x AA (boosted to 3.3V), USB-C
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold at the Hacker Warehouse vendor booth at DEF CON 29; all profits donated to the Tor Project.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/seeess/Defcon-Tor-29-Badge
  firmware_url: https://github.com/seeess/Defcon-Tor-29-Badge
  eda_tool: null
links:
- label: gigsatdc.com/dc29/torbadge_walkthrough.php
  url: https://gigsatdc.com/dc29/torbadge_walkthrough.php
  kind: website
- label: Defcon-Tor-29-Badge (GitHub, seeess)
  url: https://github.com/seeess/Defcon-Tor-29-Badge
  kind: repo
- label: Gigs Badge and PCB Design portfolio
  url: https://gigsbadge.com/
  kind: website
images:
- file: assets/images/badges/dc29/dc-29-tor-badge/9ae84b93d8.jpg
  source: "https://gigsbadge.com/"
  credit: "Gigs"
  caption: "Tor Polygraph Badge (DEF CON 29)"
contact: {}
notes:
- Sweep sourced this from Gigs's own DC29 challenge-walkthrough page and titled the entry "DC 29 Tor Badge"; the maker's own name for the badge is "Tor Polygraph (Lie Detector) Badge".
- This is the same badge as the existing entry dc29-tor-lie-detector-badge-dc29-version (Seeess, gigs); left as a separate file per task instructions, flagged as duplicate.
- Price and production quantity were not stated on the sources checked (maker portfolio, GitHub README, walkthrough page).
status: released
sources:
- kind: url
  url: https://gigsatdc.com/dc29/torbadge_walkthrough.php
  title: DC 29 Tor Badge Challenge Walkthrough
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass; confirms the puzzle/challenge side of the badge and that Gigs made the challenge.
- kind: url
  url: https://gigsbadge.com/
  title: Gigs Badge and PCB Design
  accessed: '2026-09-10'
  note: Maker's own summary of the Tor Polygraph Badge, attribution (Gigs = PCB/hardware, SeeEss = software/marketing), and the item photo.
- kind: url
  url: https://github.com/seeess/Defcon-Tor-29-Badge
  title: Defcon-Tor-29-Badge README
  accessed: '2026-09-10'
  note: Hardware/firmware repo; confirms MCU (SAMD21/Seeeduino XIAO), dual 1.3" OLEDs, GSR and heart-rate sensors, SAO 1.69bis header, AA/USB-C power, and that it sold at the Hacker Warehouse booth.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: Maker's own portfolio page and the open-source GitHub repo both confirm the core facts. Price and production quantity were not found on any source checked. This entry duplicates dc29-tor-lie-detector-badge-dc29-version, which covers the same physical badge under a different sheet title/attribution order.
last_modified_date: '2026-09-10'
---

The Tor Polygraph (Lie Detector) Badge was sold at the Hacker Warehouse vendor booth at DEF CON 29 (2021), with all profits donated to the Tor Project. It works as a miniature lie detector: an optical heart-rate sensor (a reverse-mounted green LED read through a fingertip) and a galvanic skin response sensor feed two 1.3" I2C OLED displays that graph the wearer's readings live. Hardware and PCB design were handled by Gigs (@gigstaggart); SeeEss (@see_ess) wrote most of the software and led marketing. It runs on a SAMD21-based Seeeduino XIAO, is powered by two AA batteries boosted to 3.3V (with a USB-C option), and carries a single SAO 1.69bis header.

Beyond the sensor gimmick, the badge doubled as the entry point to a seven-layer crypto/puzzle challenge that Gigs designed and later documented in a public walkthrough: a Konami-code-triggered help menu, morse code printed along the lanyard, Game Genie codes, a Vigenère cipher, What3Words geolocation encoding, and a custom "onion layer" cipher, ending at a web-based challenge page. Firmware and schematics are open-sourced in SeeEss's GitHub repository.

This entry was created from the challenge-walkthrough page alone and is the same physical badge already catalogued as `dc29-tor-lie-detector-badge-dc29-version`; see that entry's notes for any differences in how the two records describe it.
