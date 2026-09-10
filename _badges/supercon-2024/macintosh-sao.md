---
title: Macintosh SAO
id: supercon-2024-macintosh-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Aaron (aeiche)
  url: https://hackaday.io/hacker/107039-aaron
summary: A Shitty Add-On shaped like the original Macintosh for its 40th anniversary, with a 64x48 OLED driven by a CH32V003 that plays MacPaint/MacWrite-style animations from I2C draw commands, built for the Supercon 8 (2024) SAO contest in a run of roughly 50 units.
functions: Draws a Mac-style desktop with an animated mouse cursor, and can play MacPaint- and MacWrite-like drawing/text animations. A host device sends command bytes over I2C that switch between a background layer and an animation layer to build up the screen.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - pop culture
tech:
  mcu: CH32V003 (J4M6, 8-pin SOIC)
  leds:
    count: 1
    type: side-shining
    note: Single side-shining LED behind the Apple logo, driven through a 1k resistor.
  display: 0.66" 64x48 OLED (SSD1306, I2C)
  connectivity:
  - i2c
  battery: null
  sao_version: null
tech_extra:
  other_parts: Fremont Micro FT24C64A 8KB EEPROM; Panasonic EVQP7J01P right-angle SMD button.
get_one:
  price: ''
  price_usd: null
  quantity: approximately 51 (about 40 white, 11 black)
  availability: unknown
  distribution:
  - contest
  where: Distributed to attendees of Hackaday Supercon 8 (2024) as part of the SAO contest; not sold on a storefront that we found.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/aaroneiche/macsao/tree/main/hardware
  firmware_url: https://github.com/aaroneiche/macsao/tree/main/firmware
  eda_tool: KiCad
links:
- label: hackaday.io/project/196403-macintosh-sao
  url: https://hackaday.io/project/196403-macintosh-sao
  kind: hackaday
  archived: https://web.archive.org/web/20260807051250/https://hackaday.io/project/196403-macintosh-sao
- label: github.com/aaroneiche/macsao
  url: https://github.com/aaroneiche/macsao
  kind: repo
- label: aeiche.com/macsao
  url: https://aeiche.com/macsao
  kind: website
  archived: https://web.archive.org/web/20260115085549/https://aeiche.com/macsao/
images:
- file: assets/images/badges/supercon-2024/macintosh-sao/f228c4dc45.jpg
  source: https://hackaday.io/project/196403-macintosh-sao
  credit: Aaron (aeiche)
  caption: The Macintosh SAO, an add-on shaped like the original 1984 Macintosh
  archived: https://web.archive.org/web/20260807051250/https://hackaday.io/project/196403-macintosh-sao
- file: assets/images/badges/supercon-2024/macintosh-sao/9358433240.jpg
  source: https://hackaday.io/project/196403-macintosh-sao
  credit: Aaron (aeiche)
  caption: Close-up of the Macintosh SAO PCB showing the OLED screen and Apple logo LED
  archived: https://web.archive.org/web/20260807051250/https://hackaday.io/project/196403-macintosh-sao
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/196403-macintosh-sao
  title: Macintosh SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260807051250/https://hackaday.io/project/196403-macintosh-sao
- kind: url
  url: https://hackaday.io/project/196403-macintosh-sao
  title: Macintosh SAO
  accessed: '2026-09-07'
  note: 'Maker''s own project log: confirms maker (Aaron/aeiche), Supercon 8 (2024) SAO contest, CH32V003 MCU, 64x48 SSD1306 OLED, EEPROM and LED/button parts, quantity built (~51 units, ~40 white/11 black), and I2C draw-command animation scheme.'
  archived: https://web.archive.org/web/20260807051250/https://hackaday.io/project/196403-macintosh-sao
- kind: url
  url: https://github.com/aaroneiche/macsao
  title: aaroneiche/macsao
  accessed: '2026-09-07'
  note: README confirms it was built heading into Hackaday Supercon 2024 as a 40th-anniversary Macintosh tribute, and that the maker considers the code open to use ("in the spirit of open source"); repo contains firmware/ and hardware/ (KiCad) directories with no separate LICENSE file.
- kind: url
  url: https://aeiche.com/macsao
  title: The Mac SAO
  accessed: '2026-09-07'
  note: Page could not be extracted beyond its title; no additional information obtained.
  archived: https://web.archive.org/web/20260115085549/https://aeiche.com/macsao/
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Verification pass (2026-09-07): re-fetched hackaday.io/project/196403-macintosh-sao and github.com/aaroneiche/macsao and confirmed every non-empty field and body sentence against them, including details not spot-checked before: the 0.66" display size, the mouse-cursor/background-layer/animation-layer I2C scheme, the MacPaint/MacWrite drawing and typing logs, and the 1k LED resistor. The maker''s Hackaday project log also states the white/black split is a PCB solder-mask option (not an OLED-glass variant) and that the units are powered from the SAO header, but neither look.colors nor a tech.power/battery field was added since filling previously-empty fields is outside this verification pass''s scope. Could not confirm price (likely free/contest-distributed, not sold), exact SAO header pin count/version, or an explicit open-source license (the repo says the code is "open to use" but carries no LICENSE file, matching what the entry already says). aeiche.com/macsao still would not
    render beyond its page title. Both saved images were re-checked and clearly show the physical Macintosh SAO (front shells and populated PCB with maker signature), matching their captions.'
last_modified_date: '2026-09-07'
---

The Macintosh SAO is a Shitty Add-On built by Aaron (hackaday.io handle aeiche) for the Supercon 8 SAO contest in October 2024, marking the 40th anniversary of the original 1984 Macintosh. A CH32V003 microcontroller drives a 0.66" 64x48 SSD1306 OLED to recreate a tiny Mac "desktop," complete with an animated mouse cursor and MacPaint- and MacWrite-style drawing and text effects. A host badge (or other controller) talks to the SAO over I2C, sending command bytes that switch between a background layer and an animation layer to build up what's on screen. The board also carries an 8KB EEPROM, a right-angle SMD button, and a single side-shining LED lighting the Apple logo.

Aaron built around 51 of them for Supercon attendees — roughly 40 in white and 11 in black — and open-sourced the firmware and KiCad hardware files on GitHub in the same spirit as the rest of the SAO badgelife scene, though without a formal license attached.

## Make your own

The hardware (KiCad project) and firmware live in separate folders of the [macsao GitHub repo](https://github.com/aaroneiche/macsao). The README states the maker considers everything there open to use; there's no build guide beyond the source itself, so replicating it means reading the firmware to see the I2C command protocol and using the KiCad files to fab the board.
