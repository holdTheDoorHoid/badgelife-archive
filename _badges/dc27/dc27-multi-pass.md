---
title: DC27 MULTI PASS
id: dc27-dc27-multi-pass
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Bliss Jourdan (BoZe / CromulonB)
  url: https://hackaday.io/CromulonB
summary: An indie DEF CON 27 badge themed after the MULTI PASS from The Fifth Element, built around an ESP32 WROOM with a 2.9-inch e-paper display, MPR121 capacitive touch, 13 animated LEDs driven by an ATmega48, micro SD, 1000mAh LiPo and two SAO v1.69bis headers, running the badge.team MicroPython firmware so it can load hatchery apps written for the SHA and HackerHotel badges.
functions: Capacitive-touch directional pad plus select/start/A/B buttons for navigating MicroPython apps; WiFi for OTA firmware updates and downloading apps from the badge.team hatchery; zero-power e-paper persistence between screen updates; 13 animated reverse-mount LEDs with capacitive touch pads implemented as copper mesh rather than solid pour.
look:
  colors:
  - black
  shape: card
  themes:
  - sci-fi
  - movie
  - retro computer
  - security
tech:
  mcu: ESP32 WROOM
  leds:
    count: 13
    type: reverse-mount
    note: driven by a separate ATmega48 LED controller
  display: 2.9" e-paper (296x128)
  connectivity:
  - wifi
  inputs:
  - capacitive
  - touch
  battery: LiPo 1000 mAh
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: 170 (goal was 200; crowdfunding backers claimed about 130)
  availability: sold_out
  availability_note: Reported sold out around DEF CON 27 (2019); checked 2026-09-07, no live storefront found.
  distribution:
  - crowdfunding
  where: Funded and sold via a Kickstarter campaign ("MULTI PASS / DEF CON 27 Indie Badge"), fulfilled to backers at DEF CON 27.
make_your_own:
  open_source: true
  hardware_url: https://github.com/CromulonB/DC27-MULTI-PASS
  firmware_url: https://github.com/CromulonB/DC27-MULTI-PASS
  eda_tool: null
links:
- label: hackaday.io/project/164625-dc27-multi-pass
  url: https://hackaday.io/project/164625-dc27-multi-pass
  kind: hackaday
  archived: https://web.archive.org/web/20260416234959/https://hackaday.io/project/164625-dc27-multi-pass
- label: github.com/CromulonB/DC27-MULTI-PASS
  url: https://github.com/CromulonB/DC27-MULTI-PASS
  kind: repo
- label: Kickstarter — MULTI PASS / DEF CON 27 Indie Badge
  url: https://www.kickstarter.com/projects/cromulonb/multi-pass-def-con-27-indie-badge
  kind: store
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- label: 'Hackster.io: The MULTI PASS DEF CON 27 Badge Is Perfect for Trips to Fhloston Paradise'
  url: https://www.hackster.io/news/the-multi-pass-def-con-27-badge-is-perfect-for-trips-to-fhloston-paradise-314e5aa41a2c
  kind: article
images:
- file: assets/images/badges/dc27/dc27-multi-pass/3d8d7a9e0d.jpg
  source: https://hackaday.io/project/164625-dc27-multi-pass
  credit: Bliss Jourdan (CromulonB)
  caption: The DC27 MULTI PASS badge, styled after the Fifth Element prop
  archived: https://web.archive.org/web/20260416234959/https://hackaday.io/project/164625-dc27-multi-pass
- file: assets/images/badges/dc27/dc27-multi-pass/26e1309149.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday
  caption: Front view of the DC27 MULTI PASS badge with e-paper display
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/164625-dc27-multi-pass
  title: DC27 MULTI PASS
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260416234959/https://hackaday.io/project/164625-dc27-multi-pass
- kind: url
  url: https://github.com/CromulonB/DC27-MULTI-PASS
  title: 'GitHub - CromulonB/DC27-MULTI-PASS: DC27 MULTI PASS Badge'
  accessed: '2026-09-07'
  note: Confirms hardware/software directories are published; ESP32 platform, badge.team firmware.
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27
  accessed: '2026-09-07'
  note: Quantity made (170 of a 200 goal), reverse-mount LEDs with copper-mesh capacitive touch pads, front/rear photos.
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
- kind: url
  url: https://www.kickstarter.com/projects/cromulonb/multi-pass-def-con-27-indie-badge
  title: MULTI PASS / DEF CON 27 Indie Badge by Bliss Jourdan — Kickstarter
  accessed: '2026-09-07'
  note: Identifies the maker's real name (Bliss Jourdan) and that the badge was funded and distributed via Kickstarter; page itself returned 403 to direct fetch, name/context taken from search result summaries.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Core specs (ESP32 WROOM, MPR121 touch, 2.9in e-paper, ATmega48 LED driver, 1000mAh LiPo, badge.team firmware) confirmed by the maker's own Hackaday.io and GitHub pages. Price per unit was not found on any source checked (Kickstarter page returned 403 to automated fetch; only search-result summaries were available, which did not state a pledge price). Quantity and "sold out" status come from a third-party Hackaday.com article, not the maker directly, though it lines up with the crowdfunding framing. Maker's given name (Bliss Jourdan) and handle (BoZe / CromulonB) both appear in search results; kept the sheet-provided "BoZe" alongside the fuller name.
last_modified_date: '2026-09-07'
---

The DC27 MULTI PASS is an indie badge that Bliss Jourdan (known online as BoZe, or by their GitHub/Hackaday handle CromulonB) built for DEF CON 27 in 2019, recreating the "Multipass" ID card prop from *The Fifth Element*. It centers on an ESP32 WROOM module paired with a 2.9-inch e-paper display, so the screen holds its image with zero power draw between updates. Thirteen reverse-mount LEDs, driven by a separate ATmega48 controller, animate around the card, and capacitive touch (via an MPR121 controller) is implemented with a copper-mesh pattern on the top copper layer standing in for buttons, giving the badge a directional pad plus select/start/A/B controls without any physical switches.

The badge runs the badge.team MicroPython firmware, the same platform used by the SHA2017 and HackerHotel badges, so it can load community apps from the badge.team hatchery and receive over-the-air updates via WiFi. A micro SD slot, CP2102 USB-UART, TP4056 charge controller, and a 1000mAh LiPo (rated for roughly a full day of use) round out the hardware, and two SAO v1.69bis headers let it host other badges' add-ons.

The project was funded through a Kickstarter campaign ("MULTI PASS / DEF CON 27 Indie Badge"); Jourdan set out to produce 200 units and ended up completing 170 in time for the con, about a quarter more than the campaign's backer count. Hardware and firmware are published on GitHub under Hardware and Software directories, and the Hackaday.io project log documents the build process in detail. No individual per-unit price was found in the sources checked.
