---
title: Viking Ship Badge (DC26)
id: dc26-viking-ship-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Thomas Flummer
  url: https://thomasflummer.com/
summary: An independent, Viking longship-shaped electronic badge made for DEF CON 26, with PCB artwork inspired by Nordic night-sky constellations instead of the usual skull motifs.
functions: Blinking LED indicators and an experimental puzzle element built into the badge.
look:
  colors: []
  shape: null
  themes:
  - pirate
  - space
  - puzzle
tech:
  mcu: EFM32HG322 (Happy Gecko)
  leds: null
  display: null
  connectivity:
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: 'Firmware uses the Geckoboot bootloader (open source, on GitHub at github.com/flummer/geckoboot), originally written by esmil for the 2017 Bornhack badge, allowing USB firmware updates with no external programmer. No hardware design files (schematic/PCB/Gerbers) for the Viking badge itself were found.'
links:
- label: thomasflummer.com/2018/making-an-indie-badge-for-defcon-26
  url: https://thomasflummer.com/2018/making-an-indie-badge-for-defcon-26/
  kind: website
- label: flummer/geckoboot (bootloader used by the badge)
  url: https://github.com/flummer/geckoboot
  kind: repo
images:
- file: assets/images/badges/dc26/viking-ship-badge-dc26/a074217558.jpg
  source: "https://thomasflummer.com/2018/making-an-indie-badge-for-defcon-26/"
  credit: "Thomas Flummer"
  caption: "The Viking ship badge made for DEF CON 26"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://thomasflummer.com/2018/making-an-indie-badge-for-defcon-26/
  title: Viking Ship Badge (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
- kind: url
  url: https://thomasflummer.com/2018/making-an-indie-badge-for-defcon-26/
  title: Making an indie badge for DEFCON 26
  accessed: '2026-09-07'
  note: 'Primary source: maker''s own project writeup describing the badge, its EFM32HG322 (Happy Gecko) MCU, Geckoboot bootloader, and Nordic-constellation PCB art; image URL for the badge photo.'
- kind: url
  url: https://github.com/flummer/geckoboot
  title: flummer/geckoboot
  accessed: '2026-09-07'
  note: 'Confirms the Geckoboot bootloader used by the badge is open source; credits esmil (original author) and KNielsen.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own project page confirms this is a Viking-longship-shaped independent badge made by Thomas Flummer for DEF CON 26 (2018), running on an EFM32HG322 "Happy Gecko" MCU with the open-source Geckoboot bootloader (originally written by esmil for the 2017 Bornhack badge). The page does not state price, quantity made, distribution method, LED count/type, battery, or whether hardware design files were published; a search of Flummer''s GitHub repositories (github.com/flummer) turned up no repo specifically for this badge''s hardware. Could not run a second web search to corroborate further (session web-search budget was exhausted) or find press coverage beyond the maker''s own page.'
last_modified_date: '2026-09-07'
---

Thomas Flummer, a hardware developer from Denmark, made this badge as an independent entry for DEF CON 26 in 2018. Rather than the skull imagery common on badges at the event, he designed the PCB artwork around a Viking longship and constellations from the northern night sky. The badge is built around the Silicon Labs EFM32HG322 "Happy Gecko" microcontroller, chosen for its built-in USB support without needing an external crystal and its integrated voltage regulator, and it includes blinking LEDs and an experimental puzzle element.

The badge's firmware runs on the Geckoboot bootloader, an open-source USB bootloader originally written by esmil for the Bornhack 2017 badge, with additional firmware credited to esmil and KNielsen. This let the badge's firmware be updated over USB without an external programmer. Geckoboot itself is published on GitHub, but no dedicated repository with the Viking badge's own schematic, PCB, or Gerber files was found, so its hardware is not confirmed as fully open source.

Details such as price, production quantity, and how the badge was distributed at DEF CON 26 were not stated in the available source and remain unknown.
</content>
