---
title: AND!XOR DC26 Badge
id: dc26-andxor-dc26-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: AND!XOR
  url: https://twitter.com/ANDnXOR
summary: 'AND!XOR''s DEF CON 26 indie badge, subtitled "The Wild West of IoT": an ESP32-WROVER badge with a 220x176 color LCD, IS31FL3736-driven LEDs, a UART console, games, puzzles, the LULZCODE scripting interpreter, badge-to-badge wireless features and a Shitty Add-On connector, crowdfunded on Kickstarter in 2018.'
functions: 'A menu-driven UI (seen on-badge as "Bling", "Botnet", "Games", "Settings", "Wifi On") with embedded games and puzzles, hardware hacking challenges reachable over a UART console, badge-to-badge wireless ("Botnet") features, and the custom LULZCODE scripting language (an extension of LOLCODE) for writing badge scripts.'
look:
  colors:
  - red
  - white
  - gold
  shape: skull
  themes:
  - skull
  - robot
  - cyberpunk
  - security
  - puzzle
tech:
  mcu: ESP32-WROVER
  leds: null
  display: 220x176 color LCD
  connectivity:
  - wifi
  - uart
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - crowdfunding
  where: 'Crowdfunded via Kickstarter (campaign page could not be reached for pricing/quantity details; site returned a bot-check page during research).'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/28389-andxor-dc26-badge
  url: https://hackaday.io/project/28389-andxor-dc26-badge
  kind: hackaday
- label: www.kickstarter.com/projects/hyr0n/andxor-defcon-26-indie-badge
  url: https://www.kickstarter.com/projects/hyr0n/andxor-defcon-26-indie-badge
  kind: store
- label: geocities.ws/andnxor/lulzcode
  url: http://geocities.ws/andnxor/lulzcode/
  kind: website
- label: twitter.com/ANDnXOR
  url: https://twitter.com/ANDnXOR
  kind: social
images:
- file: assets/images/badges/dc26/andxor-dc26-badge/1c485120ab.jpg
  source: "https://hackaday.io/project/28389-andxor-dc26-badge"
  credit: "AND!XOR"
  caption: "AND!XOR DC26 badge, front view, powered on and showing its menu"
- file: assets/images/badges/dc26/andxor-dc26-badge/8b45492ff2.png
  source: "https://hackaday.io/project/28389-andxor-dc26-badge"
  credit: "AND!XOR"
  caption: "AND!XOR DC26 badge PCB artwork: a robotic skull wearing a cowboy hat"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/28389-andxor-dc26-badge
  title: AND!XOR DC26 Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/28389-andxor-dc26-badge
  title: AND!XOR DC26 Badge (Hackaday.io project page)
  accessed: '2026-09-07'
  note: Confirmed maker (AND!XOR, team of five including Zapp, Andrew, Hyr0n, bitstr3m), event (DEF CON 26, Aug 9-12 2018, Caesars Palace), MCU (ESP32-WROVER), display (220x176 color LCD, upgraded from a 128x128 prototype), IS31FL3736 LED driver, Greenpak debouncing, CP2102N USB-UART bridge, LULZCODE scripting, Shitty Add-On support, and open-source-after-the-con plan for hardware/firmware. Also source of the two saved photos (front view with menu, and PCB skull/cowboy artwork).
- kind: url
  url: https://www.kickstarter.com/projects/hyr0n/andxor-defcon-26-indie-badge
  title: AND!XOR DEFCON 26 Indie Badge (Kickstarter)
  accessed: '2026-09-07'
  note: 'Page could not be retrieved: Kickstarter served a Cloudflare bot-check challenge to both the fetch tool and a plain curl request, so pledge tiers, price, and quantity funded could not be confirmed.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, event/year, MCU, display, LED driver, connectivity, functions, open-source plan) confirmed from the Hackaday.io project page. Price, quantity produced, and exact availability could not be confirmed because Kickstarter blocked both WebFetch and curl with a Cloudflare challenge; the LULZCODE geocities mirror also returned 403. tech.leds.count/type, tech.battery, and make_your_own URLs remain unconfirmed and left empty. A GitHub repo for the hardware/firmware was mentioned as planned post-con but no confirmed URL was found in the sources actually read.'
last_modified_date: '2026-09-07'
---

AND!XOR's badge for DEF CON 26 (Caesars Palace, Las Vegas, August 9-12, 2018) continued the group's tradition of elaborate, game-laden independent badges, this one subtitled "The Wild West of IoT." The PCB is cut into a skull-in-a-cowboy-hat silhouette, printed in red and white with gold accents, and centers a 220x176 color LCD (an upgrade from an earlier 128x128 prototype) that drives a menu system offering "Bling," "Botnet," "Games," "Settings," and Wi-Fi toggling. An ESP32-WROVER module provides the brains and Wi-Fi connectivity, an IS31FL3736 driver runs the badge's LED lighting, a Greenpak chip handles button debouncing, and a CP2102N bridges USB to the on-board UART console used for hardware-hacking challenges.

Beyond the on-screen menu, the badge supported badge-to-badge "Botnet" wireless interaction, embedded games and puzzles, a Shitty Add-On connector for attaching SAOs, and AND!XOR's own LULZCODE, a scripting language extending LOLCODE that let owners write and run their own badge scripts. The team — credited on the project page as Zapp, Andrew, Hyr0n, and bitstr3m — crowdfunded production through a Kickstarter campaign; that page could not be read during this research pass (Kickstarter returned a Cloudflare bot-check to both an automated fetch and a plain curl request), so pledge pricing and the number of units funded remain unconfirmed here. The Hackaday.io project page stated the team's intent to open-source the hardware and firmware after the conference, but no confirmed repository URL was located among the sources actually reached.
