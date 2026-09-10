---
title: HOPE XV Electronic Badge
id: hope-2024-hope-xv-electronic-badge
layout: badge
parent: HOPE XV
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hope-2024
year: 2024
makers:
- name: HOPE Badge Team (HBT) with Novel Circuits
summary: The official electronic badge given to in-person attendees of HOPE XV, with a purchasable "pro" version with extra components.
functions: Cycles LED light patterns (button 1), dims/brightens the LEDs (buttons 2-3), and sends an IR "blast" to other badges in range that makes their lights flash and their vibration motor buzz (button 4). Runs stock firmware or can be reflashed with MicroPython or ESPHome.
look:
  colors:
  - purple
  - black
  - green
  - pink
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ESP32-C3
  leds:
    count: 16
    type: WS2812B
    note: Described on the wiki as "16 WS2812 or similar"
  display: none
  connectivity:
  - wifi
  - ir
  - nfc
  - usb
  battery: LiPo, charged via MCP73871 controller
  sao_version: null
get_one:
  price: Attendee badge included with registration; pro version $100 (extra components) or $150 (extra components and accessories)
  price_usd: 150
  quantity: ''
  availability: sold_out
  availability_note: As of 2026-09-08, 2600.com was offering leftover HOPE XV badge kits for free with a t-shirt purchase while supplies lasted; unclear if any remain.
  distribution:
  - free_drop
  - purchase
  where: Given to in-person HOPE XV attendees at registration; "pro" versions sold at the on-site Badge Clinic; leftover kits later bundled free with t-shirt orders from the 2600 store.
make_your_own:
  open_source: true
  hardware_url: https://gitlab.com/tidklaas/hip-badge
  firmware_url: https://gitlab.com/tidklaas/hip-badge
  eda_tool: KiCad
notes:
- HOPE wiki flags that the linked GitLab repo (branch REL_0.8.14) "does not specifically mention HOPE" by name, so the maintainer-to-badge link is inferred rather than stated outright; the wiki also links a vibration-motor branch and notes badges can be reflashed via ESPHomeBadge (https://github.com/fortuna/ESPHomeBadge).
- Official electronic badge given to in-person attendees of the 2024 HOPE conference, built around an ESP32-C3 with 16 WS2812 LEDs and IR badge-to-badge interaction, open-hardware KiCAD design on GitLab. Found by the event-year sweep, task general-2023.
- The sweep titled this entry "HOPE XV Electronic Badge (HOPE_16)" ("HOPE_16" is the wiki page's internal MediaWiki title slug, not a separate model name); retitled to match the maker's plain name.
links:
- label: wiki.hope.net/index.php/HOPE_XV_Electronic_Badge
  url: https://wiki.hope.net/index.php/HOPE_XV_Electronic_Badge
  kind: website
- label: wiki.hope.net/images/6/6b/HOPE_XV_Electronic_Badge_User_Manual.pdf
  url: https://wiki.hope.net/images/6/6b/HOPE_XV_Electronic_Badge_User_Manual.pdf
  kind: website
- label: www.2600.com/content/hope-xv-update-t-shirts-and-badge-kits
  url: https://www.2600.com/content/hope-xv-update-t-shirts-and-badge-kits
  kind: website
- label: gitlab.com/tidklaas/hip-badge
  url: https://gitlab.com/tidklaas/hip-badge
  kind: repo
- label: wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  url: https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  kind: website
- label: github.com/fortuna/ESPHomeBadge
  url: https://github.com/fortuna/ESPHomeBadge
  kind: repo
images:
- file: assets/images/badges/hope-2024/hope-xv-electronic-badge/5ba4008e20.jpg
  source: https://wiki.hope.net/index.php/HOPE_XV_Electronic_Badge
  credit: HOPE Badge Team
  caption: HOPE XV Electronic Badge PCB, front
- file: assets/images/badges/hope-2024/hope-xv-electronic-badge/924e926a31.jpg
  source: https://wiki.hope.net/index.php/HOPE_XV_Electronic_Badge
  credit: HOPE Badge Team
  caption: HOPE XV Electronic Badge PCB, back
- file: assets/images/badges/hope-2024/hope-xv-electronic-badge/843b0c3413.jpg
  source: https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  credit: HOPE wiki
  caption: Front of the HOPE XV electronic badge
- file: assets/images/badges/hope-2024/hope-xv-electronic-badge/924e926a31.jpg
  source: https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  credit: HOPE wiki
  caption: Back of the HOPE XV electronic badge
contact: {}
status: released
sources:
- kind: url
  url: https://wiki.hope.net/index.php/HOPE_XV_Electronic_Badge
  title: HOPE XV Electronic Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:hope); event read as ''hope-2024''.'
- kind: url
  url: https://www.2600.com/content/hope-xv-update-t-shirts-and-badge-kits
  title: 'HOPE XV Update: T-Shirts and Badge Kits'
  accessed: '2026-09-08'
  note: Confirms leftover badge kits were later given away free with t-shirt purchases from the 2600 store; badges ship without battery or buzzer.
- kind: url
  url: https://gitlab.com/tidklaas/hip-badge
  title: hip-badge (GitLab repository)
  accessed: '2026-09-08'
  note: Open hardware/firmware repo linked from the wiki as the badge's KiCad + firmware source; the wiki itself notes the link is not explicitly confirmed as the HOPE badge.
- kind: url
  url: https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  title: HOPE XV Electronic Badge (HOPE_16)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2023); event read as ''HOPE 2024''.'
- kind: url
  url: https://wiki.hope.net/index.php?title=HOPE_XV_Electronic_Badge
  title: HOPE XV Electronic Badge
  accessed: '2026-09-08'
  note: Confirmed badge, maker, chip, LEDs, IR feature, NFC/air-quality sensor pro-version add-ons, and Badge Clinic pricing.
- kind: url
  url: https://github.com/fortuna/ESPHomeBadge
  title: fortuna/ESPHomeBadge on GitHub
  accessed: '2026-09-08'
  note: Confirms this targets the HOPE XV badge specifically; documents ESPHome-based alternate firmware with buttons, LED strip, vibration motor, NFC, air-quality sensor, and IR control.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (MCU, LEDs, distribution, pricing, open-source repo) confirmed on the official HOPE wiki page and corroborated by a 2600.com store post about leftover kits. Total quantity made is not stated anywhere found. The wiki page itself flags the linked GitLab repo as not explicitly HOPE-branded, so hardware_url/firmware_url are given with that caveat. A near-duplicate entry already exists in the archive: hope-2024-hope-xv-electronic-badge-hope-16 (same badge, credited to "tidklaas (Open Hardware repo maintainer) / HOPE badge team") — flagged as duplicate_of, not merged per task rules. Merged with duplicate entry ''HOPE XV Electronic Badge'' (hope-2024-hope-xv-electronic-badge-hope-16).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/hope-2024/hope-xv-electronic-badge-hope-16/
model:
  file: assets/models/hope-2024/hope-xv-electronic-badge.glb
  method: kicad
  source_file: hardware/hipstenc.kicad_pcb
  generated: '2026-09-10'
  bytes: 1785364
---

The HOPE XV Electronic Badge was the official badge handed to in-person attendees of HOPE XV (2024) at registration, with a "pro" version carrying extra populated components sold on-site at the Badge Clinic for $100–$150. Attendee boards are purple; pro boards are black, with pink, green, or black cases. It is built around an ESP32-C3 microcontroller with 16 WS2812-style addressable LEDs, LiPo charging via an MCP73871 controller, an IR emitter for badge-to-badge interaction, NFC, an ATECC608B crypto element, and SAO/JTAG/FFC expansion connectors, though a number of the fancier parts (microphone, gas sensor, vibration motor) are only populated on the pro boards.

Stock firmware lets wearers cycle LED patterns and adjust brightness with the front buttons, and a fourth button fires an IR "blast" that makes nearby badges flash their LEDs and buzz their vibration motor. The badge can also be reflashed with MicroPython or with the community ESPHomeBadge project. HOPE's wiki links the hardware and firmware to a GitLab repository (tidklaas/hip-badge) as fully open hardware designed in KiCad, though the wiki itself notes uncertainty about whether that specific repo is officially the HOPE badge's source. After the con, 2600 offered leftover badge kits for free with t-shirt purchases from its online store while supplies lasted, noting the giveaway units ship without a battery or buzzer but can run on USB-C power in the meantime.

## Notes merged from the duplicate entry "HOPE XV Electronic Badge"

The HOPE XV Electronic Badge was the official electronic badge given to in-person attendees of HOPE XV (2024), built by the HOPE Badge Team with Novel Circuits around an ESP32-C3 microcontroller and 16 WS2812B-class addressable LEDs. Four buttons let the wearer cycle light patterns and adjust brightness, and an IR emitter/receiver lets nearby badges "blast" each other, triggering flashing lights and a vibration-motor buzz on the receiving badge.

Beyond the standard badge included with registration, a "pro" version with additional components (NFC tags, an air-quality sensor, and other accessories) was sold on-site at the Badge Clinic for $100 or $150 depending on configuration. The hardware and firmware are open source, published as KiCad design files and firmware on GitLab, and the community-built ESPHomeBadge project lets owners reflash the badge with ESPHome for easier customization, including support for WiFi, a badge-info display page, and Home Assistant integration.

The underlying hardware design traces back to a GitLab repository ("hip-badge") originally associated with a separate, earlier event in Berlin ("Hacking in Parallel," December 2022); the HOPE wiki notes the repo doesn't explicitly reference HOPE by name, so the badge team appears to have adapted an existing open-hardware design rather than starting from scratch.
