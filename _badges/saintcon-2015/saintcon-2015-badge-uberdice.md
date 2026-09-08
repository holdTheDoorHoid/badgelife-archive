---
title: SAINTCON 2015 Badge
id: saintcon-2015-saintcon-2015-badge-uberdice
layout: badge
parent: SAINTCON 2015
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: saintcon-2015
year: 2015
makers:
- name: Luke Jenkins
  url: https://hackaday.io/wifiluke
summary: The official Wi-Fi-connected attendee badge for SAINTCON 2015, built around an Atmel XMega and an ESP module, with a color LCD, buttons, and a buzzer.
functions: Displays attendee info and switchable modes (including a "Name mode"), talks to an onboard ESP Wi-Fi module for conference challenges/location features, and can be reprogrammed and reflashed by attendees.
look:
  colors:
  - green
  shape: rectangle
  themes:
  - security
  - wearable
tech:
  mcu: ATXMega256A3BU
  leds: null
  display: ILI9341 color LCD
  connectivity:
  - wifi
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to SAINTCON 2015 attendees as the conference's official badge.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/atticus88/SAINTCON-2015-Badge
  firmware_url: https://github.com/atticus88/SAINTCON-2015-Badge
  eda_tool: null
links:
- label: hackaday.io/project/7089-saintcon-2015-badge
  url: https://hackaday.io/project/7089-saintcon-2015-badge
  kind: hackaday
- label: github.com/atticus88/SAINTCON-2015-Badge
  url: https://github.com/atticus88/SAINTCON-2015-Badge
  kind: repo
- label: hackaday.io/project/7089/gallery
  url: https://hackaday.io/project/7089/gallery
  kind: hackaday
- label: badge.gallery — SAINTCON series
  url: https://badge.gallery/series/saintcon
  kind: article
images:
- file: assets/images/badges/saintcon-2015/saintcon-2015-badge-uberdice/3ffd927c7f.jpg
  source: "https://hackaday.io/project/7089-saintcon-2015-badge"
  credit: "Luke Jenkins"
  caption: "Close-up of the SAINTCON 2015 badge PCB showing buttons, buzzer, and header pins"
contact: {}
notes:
- Official SAINTCON 2015 conference badge, created by Luke Jenkins with hardware/firmware published on GitHub (atticus88/SAINTCON-2015-Badge). Found by the event-year sweep, task saintcon-2015.
- 'The sweep''s title and "9 LEDs per side / accelerometer / programmable die" description came from a *different*, unrelated Hackaday.io project called "uberdice" (hackaday.io/project/1599-uberdice, by a user named Peter) that appeared as a "related project" recommendation card on the SAINTCON 2015 Badge''s own Hackaday page. The two projects share no connection beyond that sidebar placement; the SAINTCON 2015 badge itself is not a dice. Title corrected from "SAINTCON 2015 Badge (UberDice)" to "SAINTCON 2015 Badge".'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/7089-saintcon-2015-badge
  title: SAINTCON 2015 Badge (UberDice)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:saintcon-2015); event read as ''saintcon-2015''.'
- kind: url
  url: https://hackaday.io/project/7089-saintcon-2015-badge
  title: SAINTCON 2015 Badge
  accessed: '2026-09-08'
  note: Maker (Luke Jenkins), project title, and og:image photo of the badge PCB. Also carries the unrelated "uberdice" related-project card that misled the original sweep.
- kind: url
  url: https://github.com/atticus88/SAINTCON-2015-Badge
  title: atticus88/SAINTCON-2015-Badge on GitHub
  accessed: '2026-09-08'
  note: Confirms open hardware/firmware; MCU (ATXMega256A3BU), ILI9341 display, ESP Wi-Fi module, NodeMCU/Lua firmware for the Wi-Fi module, PDI/AVRISP programming.
- kind: url
  url: https://badge.gallery/series/saintcon
  title: SAINTCON · Hacker Con Badges - badge.gallery
  accessed: '2026-09-08'
  note: Describes the 2015 badge as a Wi-Fi-enabled, LCD-and-button attendee badge used with Cisco CMX location data for conference challenges, carried by roughly 550 participants.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Corrected a mix-up: the entry''s title and notes described an unrelated Hackaday project ("uberdice" by Peter, project 1599) rather than the actual SAINTCON 2015 badge (project 7089, by Luke Jenkins). No price, exact quantity, or LED/battery details were found for the real badge; badge.gallery states roughly 550 were distributed to attendees but that number is not confirmed on the maker''s own pages, so quantity/availability were left unfilled rather than guessed. Bluetooth is mentioned in the GitHub README only as an example OTA-update method (linking to an unrelated library), not confirmed as a feature of the shipped badge, so it was not added to connectivity.'
last_modified_date: '2026-09-08'
---

The SAINTCON 2015 badge was the official attendee badge for that year's SAINTCON security conference in Utah, designed by Luke Jenkins with hardware and firmware published as open source on GitHub. It is built around an Atmel ATXMega256A3BU microcontroller driving a color ILI9341 LCD, with physical buttons, a buzzer, and an onboard ESP Wi-Fi module (flashed with NodeMCU/Lua firmware) that let the badge participate in conference-wide, Wi-Fi-location-linked challenges — badge.gallery describes roughly 550 attendees carrying these LCD-and-button badges as part of a Cisco CMX-based experiment.

An early sweep of the web mislabeled this entry "SAINTCON 2015 Badge (UberDice)" and described it as a USB-connected programmable die with 9 LEDs per side and an accelerometer. That description belongs to a completely unrelated Hackaday.io project titled "uberdice" (by a user named Peter, hackaday.io/project/1599-uberdice), which happened to appear as a "related project" card on the SAINTCON badge's own Hackaday.io page. The two have no connection; this entry has been corrected to describe the actual SAINTCON 2015 badge.

## Make your own

Hardware and firmware are on GitHub at atticus88/SAINTCON-2015-Badge. The repo includes the XMega application source (built with avr-gcc), two bootloader options (a standard one and xboot for over-the-air updates), a badge-test branch for verifying hardware, and a `saintcon2015-badge-lua` directory with NodeMCU Lua firmware for the badge's ESP Wi-Fi module. Programming uses PDI/AVRISP mkII; a presentation and slide deck explaining the project are linked from the README.
