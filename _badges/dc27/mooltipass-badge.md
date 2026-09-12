---
title: DC27 MULTI PASS
id: dc27-mooltipass-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: CromulonB (Bliss Jourdan)
  url: https://hackaday.io/boze
summary: An ESP32-based indie DEF CON 27 badge shaped like the MULTI PASS ID card from the film The Fifth Element, running the badge.team MicroPython firmware platform.
functions: Runs badge.team firmware with MicroPython apps from the "hatchery" app library; capacitive touch controls; e-paper display shows customizable info; OTA app/software updates over WiFi; two SAO ports and GPIO headers for add-ons.
look:
  colors:
  - gold
  - black
  shape: card
  themes:
  - sci-fi
  - movie
  - badge.team
  - retro computer
  form_factor: pcb badge
tech:
  mcu: ESP32 WROOM (16MB, dual-core 240MHz, WiFi/Bluetooth)
  leds:
    count: 13
    type: RGB
    note: driven by a separate ATmega48
  display: 2.9" e-paper (296x128), partial update, zero-power persistence
  connectivity:
  - wifi
  - bluetooth
  inputs:
  - touch
  - capacitive
  battery: LiPo 1000 mAh, USB (CP2102) recharge, quoted 24+ hours runtime
  sao_version: v1.69bis
  sao_ports: 2
get_one:
  price: ''
  price_usd: null
  quantity: 200 planned, 170 produced in time for DEF CON 27
  availability: sold_out
  availability_note: Checked 2026-09-07; funded via a 2019 Kickstarter campaign, no active storefront found.
  distribution:
  - crowdfunding
  where: Funded and distributed as backer rewards through a Kickstarter campaign ("MULTI PASS / DEF CON 27 Indie Badge" by Bliss Jourdan); not sold through an ongoing storefront.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/CromulonB/DC27-MULTI-PASS
  firmware_url: https://github.com/CromulonB/DC27-MULTI-PASS
  eda_tool: null
  notes: GitHub repo has "Hardware" and "Software" folders; firmware is the badge.team platform. Gerbers, BOM, and license terms were not confirmed from the pages checked.
links:
- label: hac.io/o/164625
  url: http://hac.io/o/164625
  kind: website
- label: DC27 MULTI PASS (hackaday.io)
  url: https://hackaday.io/project/164625-dc27-multi-pass
  kind: hackaday
  archived: https://web.archive.org/web/20260416234959/https://hackaday.io/project/164625-dc27-multi-pass
- label: DC27-MULTI-PASS (GitHub)
  url: https://github.com/CromulonB/DC27-MULTI-PASS
  kind: repo
- label: MULTI PASS / DEF CON 27 Indie Badge (Kickstarter)
  url: https://www.kickstarter.com/projects/cromulonb/multi-pass-def-con-27-indie-badge
  kind: store
- label: The MULTI PASS DEF CON 27 Badge Is Perfect for Trips to Fhloston Paradise (Hackster.io)
  url: https://www.hackster.io/news/the-multi-pass-def-con-27-badge-is-perfect-for-trips-to-fhloston-paradise-314e5aa41a2c
  kind: article
- label: The Multi Pass Def Con Indie Badge Has A European Flavour (Hackaday)
  url: https://hackaday.com/2019/06/02/the-multi-pass-def-con-indie-badge-has-a-european-flavour/
  kind: article
  archived: https://web.archive.org/web/20260410162223/https://hackaday.com/2019/06/02/the-multi-pass-def-con-indie-badge-has-a-european-flavour/
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
images:
- file: assets/images/badges/dc27/mooltipass-badge/3d8d7a9e0d.jpg
  source: https://hackaday.io/project/164625-dc27-multi-pass
  credit: CromulonB (Bliss Jourdan)
  caption: The DC27 MULTI PASS badge
  archived: https://web.archive.org/web/20260416234959/https://hackaday.io/project/164625-dc27-multi-pass
- file: assets/images/badges/dc27/mooltipass-badge/4582df6084.jpg
  source: https://hackaday.io/project/164625-dc27-multi-pass
  credit: CromulonB (Bliss Jourdan)
  caption: Render of the badge in final colors
  archived: https://web.archive.org/web/20260416234959/https://hackaday.io/project/164625-dc27-multi-pass
- file: assets/images/badges/dc27/mooltipass-badge/3d8d7a9e0d.jpg
  source: https://hackaday.io/project/164625-dc27-multi-pass
  credit: Bliss Jourdan (CromulonB)
  caption: The DC27 MULTI PASS badge, styled after the Fifth Element prop
  archived: https://web.archive.org/web/20260416234959/https://hackaday.io/project/164625-dc27-multi-pass
- file: assets/images/badges/dc27/mooltipass-badge/26e1309149.jpg
  source: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  credit: Hackaday
  caption: Front view of the DC27 MULTI PASS badge with e-paper display
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
contact: {}
notes:
- Entry title was recorded as "Mooltipass" by the discovery sweep; the maker's own name for the badge is "MULTI PASS" (the Fifth Element prop), not to be confused with the unrelated Mooltipass password-manager hardware. Kept the id/slug as-is per instructions; corrected the display title.
status: released
sources:
- kind: url
  url: http://hac.io/o/164625
  title: DC27 Mooltipass Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://hackaday.io/project/164625-dc27-multi-pass
  title: DC27 MULTI PASS | Hackaday.io
  accessed: '2026-09-07'
  note: Primary project page - maker, hardware specs (ESP32, e-paper display, touch, LEDs, SAO headers), availability note about limited production, mention of design files releasing after DEF CON.
  archived: https://web.archive.org/web/20260416234959/https://hackaday.io/project/164625-dc27-multi-pass
- kind: url
  url: https://github.com/CromulonB/DC27-MULTI-PASS
  title: 'GitHub - CromulonB/DC27-MULTI-PASS: DC27 MULTI PASS Badge'
  accessed: '2026-09-07'
  note: Confirms Hardware/Software repo structure and that firmware is the badge.team platform.
- kind: url
  url: https://www.hackster.io/news/the-multi-pass-def-con-27-badge-is-perfect-for-trips-to-fhloston-paradise-314e5aa41a2c
  title: The MULTI PASS DEF CON 27 Badge Is Perfect for Trips to Fhloston Paradise - Hackster.io
  accessed: '2026-09-07'
  note: Confirms badge.team ESP32 firmware platform, e-ink display, touch buttons, theme faithfulness to the movie prop.
- kind: url
  url: https://hackaday.com/2019/06/02/the-multi-pass-def-con-indie-badge-has-a-european-flavour/
  title: The Multi Pass Def Con Indie Badge Has A European Flavour | Hackaday
  accessed: '2026-09-07'
  note: Confirms creator CromulonB (Bliss Jourdan), Kickstarter funding, production target of 200 with 170 delivered by DEF CON 27.
  archived: https://web.archive.org/web/20260410162223/https://hackaday.com/2019/06/02/the-multi-pass-def-con-indie-badge-has-a-european-flavour/
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
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker's own hackaday.io project page and GitHub repo confirmed the core hardware facts; price per unit/backer tier and whether gerbers/license were actually published could not be confirmed (Kickstarter page returned 403 to automated fetch). Quantity and distribution (Kickstarter, 170 of 200 planned) confirmed by two independent sources (Hackaday, Hackaday.io comments). Merged with duplicate entry 'DC27 MULTI PASS' (dc27-dc27-multi-pass).
last_modified_date: '2026-09-11'
model:
  file: assets/models/dc27/mooltipass-badge.glb
  method: kicad
  source_file: element.brd
  generated: '2026-09-11'
  bytes: 718948
redirect_from:
- /badges/dc27/dc27-multi-pass/
---

The DC27 MULTI PASS is an indie electronic badge built for DEF CON 27 (2019) by Bliss Jourdan, who goes by CromulonB. It reimagines the "Multi Pass" ID card prop from the film *The Fifth Element* as a wearable gadget: a gold, card-shaped PCB with a 2.9" e-paper display, capacitive touch buttons standing in for the prop's control surface, and 13 RGB LEDs driven by a secondary ATmega48. Under the hood it runs on a 16MB ESP32 WROOM module and boots the badge.team firmware platform (the same MicroPython-based system used on the SHA2017 and Hacker Hotel badges), so it can load community-written Python apps from the "hatchery" library and receive OTA updates over WiFi.

The badge was funded through a Kickstarter campaign under the title "MULTI PASS / DEF CON 27 Indie Badge." CromulonB set out to build 200 units and managed to finish 170 in time for the con, roughly 25% over the number promised to backers. It shipped as a backer reward rather than through an ongoing storefront, and the maker said at the time they didn't want to "flood the market" with extras, so it was never broadly available at retail. Hardware and firmware files were split into "Hardware" and "Software" folders in a public GitHub repository, with the maker stating schematics and code would be released after the con; the repo confirms that structure, though gerbers, a bill of materials, and license terms were not independently verified from the pages checked.

## Notes merged from the duplicate entry "DC27 MULTI PASS"

The DC27 MULTI PASS is an indie badge that Bliss Jourdan (known online as BoZe, or by their GitHub/Hackaday handle CromulonB) built for DEF CON 27 in 2019, recreating the "Multipass" ID card prop from *The Fifth Element*. It centers on an ESP32 WROOM module paired with a 2.9-inch e-paper display, so the screen holds its image with zero power draw between updates. Thirteen reverse-mount LEDs, driven by a separate ATmega48 controller, animate around the card, and capacitive touch (via an MPR121 controller) is implemented with a copper-mesh pattern on the top copper layer standing in for buttons, giving the badge a directional pad plus select/start/A/B controls without any physical switches.

The badge runs the badge.team MicroPython firmware, the same platform used by the SHA2017 and HackerHotel badges, so it can load community apps from the badge.team hatchery and receive over-the-air updates via WiFi. A micro SD slot, CP2102 USB-UART, TP4056 charge controller, and a 1000mAh LiPo (rated for roughly a full day of use) round out the hardware, and two SAO v1.69bis headers let it host other badges' add-ons.

The project was funded through a Kickstarter campaign ("MULTI PASS / DEF CON 27 Indie Badge"); Jourdan set out to produce 200 units and ended up completing 170 in time for the con, about a quarter more than the campaign's backer count. Hardware and firmware are published on GitHub under Hardware and Software directories, and the Hackaday.io project log documents the build process in detail. No individual per-unit price was found in the sources checked.
