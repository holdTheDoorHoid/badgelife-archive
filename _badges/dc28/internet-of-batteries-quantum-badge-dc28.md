---
title: Internet of Batteries QUANTUM Badge (DC28)
id: dc28-internet-of-batteries-quantum-badge-dc28
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
makers:
- name: 'Internet of Batteries (Whiskey Pirates crew: Aask, Lightning, true, RaigaHomsar42)'
  url: https://dc28.whiskeypirates.com/
summary: A DEF CON 28 badge/SAO hybrid that back-powers add-on badges and tracks their power draw over a WiFi mesh network, rather than displaying its own light show.
functions: Provides ~700mA at 3.3V to power other badges and SAOs through its four SAO-style headers; runs "Itero," a WiFi mesh network that lets up to 25 IoB units send broadcast or private text messages to each other; hosts a captive-portal web UI ("Captive Arcade") showing live power-consumption stats per port; can run standalone off its own battery.
look:
  colors:
  - green
  - gold
  - copper
  shape: rectangle
  themes:
  - hardware tool
  - measurement
  - radio
  - village badge
tech:
  mcu: ESP32-WROOM-32 + Cypress PSoC5 (CY8C52xx)
  leds: RGB LEDs on a daughter "LED board"; status indicated via onboard SMD LEDs
  display: none
  connectivity:
  - wifi
  battery: 3.7V 900mAh LiPo, USB (micro-USB) recharge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: about 50
  availability: sold_out
  availability_note: Sold via shop.truecontrol.org during/after DC28 (Aug 2020); site now shows no listing for it as of 2026-09-07 check.
  distribution:
  - purchase
  where: Sold by the Whiskey Pirates / trueControl crew through shop.truecontrol.org around DEF CON 28 (Aug 2020), with leftover stock earmarked for giveaways.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Aask42/IoB_DC28
  firmware_url: https://github.com/Aask42/IoB_DC28
  eda_tool: null
links:
- label: hackaday.io/project/172036-internet-of-batteries-iob-dc28
  url: https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
  kind: hackaday
  archived: https://web.archive.org/web/20251211141115/https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
- label: hackaday.com/2020/08/09/hands-on-internet-of-batteries-quantum-badge-brings-badgelife-add-ons-the-power-and-internet-they-crave
  url: https://hackaday.com/2020/08/09/hands-on-internet-of-batteries-quantum-badge-brings-badgelife-add-ons-the-power-and-internet-they-crave/
  kind: article
  archived: https://web.archive.org/web/20260419111826/https://hackaday.com/2020/08/09/hands-on-internet-of-batteries-quantum-badge-brings-badgelife-add-ons-the-power-and-internet-they-crave/
- label: github.com/Aask42/IoB_DC28
  url: https://github.com/Aask42/IoB_DC28
  kind: repo
  archived: https://web.archive.org/web/20251211045344/https://github.com/Aask42/IoB_DC28
- label: dc28.whiskeypirates.com
  url: https://dc28.whiskeypirates.com/
  kind: website
  archived: https://web.archive.org/web/20260519153316/https://dc28.whiskeypirates.com/
images:
- file: assets/images/badges/dc28/internet-of-batteries-quantum-badge-dc28/cfa9ed69c2.jpg
  source: https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
  credit: Internet of Batteries / Whiskey Pirates team
  caption: DEF CELL QUANTUM board powered on, green status LED lit
  archived: https://web.archive.org/web/20251211141115/https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
- file: assets/images/badges/dc28/internet-of-batteries-quantum-badge-dc28/22d68b91db.jpg
  source: https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
  credit: Internet of Batteries / Whiskey Pirates team
  caption: IoB2020 REV7 board showing the ESP32-WROOM-32 module and PSoC5 controller
  archived: https://web.archive.org/web/20251211141115/https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
contact: {}
notes:
- ESP32 + PSoC5 power/mesh-networking badge with 4 SAO ports, designed to power other badges' add-ons; gold-plated copper PCB front over red solder mask.
- Firmware in the repo is tagged as a "buggy" v0.2.1 (DEFCELL_QUANTUM) release per the maker; project log describes it as still "Hello World" stage at review time.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
  title: Internet of Batteries (IoB-DC28) | Hackaday.io
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc28-dc29); event read as ''DEF CON 28 Safe Mode (unofficial)''.'
  archived: https://web.archive.org/web/20251211141115/https://hackaday.io/project/172036-internet-of-batteries-iob-dc28
- kind: url
  url: https://hackaday.com/2020/08/09/hands-on-internet-of-batteries-quantum-badge-brings-badgelife-add-ons-the-power-and-internet-they-crave/
  title: 'Hands-On: Internet Of Batteries Quantum Badge Brings Badgelife Add-Ons The Power And Internet They Crave'
  accessed: '2026-09-07'
  note: Confirmed maker (Whiskey Pirates/trueControl), ~50 units made, MCU (PSoC5 + ESP32), 9 RGB LEDs in 2x15 matrix on daughter board, LiPo battery, capacitive touch pads, colors/finish.
  archived: https://web.archive.org/web/20260419111826/https://hackaday.com/2020/08/09/hands-on-internet-of-batteries-quantum-badge-brings-badgelife-add-ons-the-power-and-internet-they-crave/
- kind: url
  url: https://github.com/Aask42/IoB_DC28
  title: 'GitHub - Aask42/IoB_DC28: Safe Mode w/ Networking'
  accessed: '2026-09-07'
  note: Repo holds both hardware and ESP32/PSoC5 firmware; PlatformIO-based build; no explicit license found.
  archived: https://web.archive.org/web/20251211045344/https://github.com/Aask42/IoB_DC28
- kind: url
  url: https://dc28.whiskeypirates.com/
  title: DC28 Pirate Projects - the whiskey pirates
  accessed: '2026-09-07'
  note: Attempted fetch returned 403 (blocked); listed as the crew's DC28 project hub in search results, cited here as the makers' own site.
  archived: https://web.archive.org/web/20260519153316/https://dc28.whiskeypirates.com/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Sources disagree slightly on LED detail: Hackaday.com describes "nine RGB LEDs in a 2x15 matrix" plus four upside-down white status LEDs used as diffusers, while the Hackaday.io project log and repo mention RGB LEDs more generally without a fixed count; recorded the descriptive note rather than a single unverified count. Exact retail price and open-source license were not stated anywhere found; hardware_url/firmware_url point to the same combined repo since hardware and firmware are not split into separate URLs there. shop.truecontrol.org and dc28.whiskeypirates.com both returned 403 to automated fetch, so current-listing status is inferred from press coverage rather than a live storefront check.'
last_modified_date: '2026-09-07'
---

The Internet of Batteries (IoB) QUANTUM, badge-coded "DEF CELL QUANTUM," is an unofficial DEF CON 28 (2020) add-on built by the Internet of Batteries team within the Whiskey Pirates/trueControl crew (Aask, Lightning, true, and RaigaHomsar42). Rather than being a badge people wear to show off its own light show, it is a power hub: it back-powers other attendees' badges and SAOs through four SAO-style headers, delivering roughly 700 mA at 3.3 V from its own 900 mAh LiPo cell, and tracks how much power each connected device is drawing.

Its two-chip design pairs an ESP32-WROOM-32 for WiFi with a Cypress PSoC5 (CY8C52xx) for board logic and the RGB LED daughterboard. The ESP32 runs "Itero," a WiFi mesh network letting up to 25 IoB units exchange broadcast or private messages, and serves a captive-portal web page ("Captive Arcade") showing live power-consumption stats. The board itself is finished in gold-plated copper over a red solder mask, with capacitive touch pads under the "DEF" and "CELL" silkscreen and a row of chevron-shaped touch controls.

About 50 units were built and sold through the crew's own shop (shop.truecontrol.org) around DEF CON 28, with leftover stock set aside for giveaways. Hardware and firmware are shared together in a single GitHub repo (Aask42/IoB_DC28), built with PlatformIO; the maker's own project log describes the firmware as an early, "buggy" v0.2.1 release at the time of DC28, with mesh networking and the captive portal still being finished.
