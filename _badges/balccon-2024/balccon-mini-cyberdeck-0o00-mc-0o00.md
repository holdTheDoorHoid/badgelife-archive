---
title: BalCCon Mini Cyberdeck 0o00 (MC-0o00)
id: balccon-2024-balccon-mini-cyberdeck-0o00-mc-0o00
layout: badge
parent: BalCCon2k24 - Invisible Path
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: balccon-2024
year: 2024
makers:
- name: CH405 Labs
  url: https://ch405labs.net/
summary: A CH32V003-based "mini cyberdeck" badge for BalCCon2k24, with an LCD, six buttons and a buzzer, designed to pair with the previous year's BCD-0o27 badge.
functions: 'Runs small onboard apps: Melody Maker (music composition), Space Invaders (MIT-licensed game), CB Pong (playable alone or networked against a connected BCD-0o27), and a hardware self-test utility.'
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: CH32V003F6P6
  leds: null
  display: ST7735 LCD
  connectivity: []
  battery: null
  sao_version: null
  inputs:
  - buttons
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://gitlab.com/ch405labs/badgelife/mcd-0o00/mcd-0o00-hardware-design
  firmware_url: null
  eda_tool: null
links:
- label: ch405-labs.com/mc-0o00
  url: https://ch405-labs.com/mc-0o00/
  kind: website
- label: badge.gallery/badges/balccon-2024-mc-0o00
  url: https://badge.gallery/badges/balccon-2024-mc-0o00
  kind: website
- label: ch405labs.net/mc-0o00
  url: https://ch405labs.net/mc-0o00/
  kind: website
- label: MCD 0o00 Hardware Design (GitLab)
  url: https://gitlab.com/ch405labs/badgelife/mcd-0o00/mcd-0o00-hardware-design
  kind: repo
- label: CB Pong addon page (badge.gallery)
  url: https://badge.gallery/addons/balccon-2024-mc-0o00/cb-pong
  kind: website
images: []
contact: {}
notes:
- CH32V003 RISC-V mini cyberdeck badge with LCD, six buttons, buzzer and GPIO/power interface designed to companion the BCD-0o27, released as the BalCCon2k24 badge with MIT-licensed firmware (Space Invaders, CB Pong, Melody Maker). Found by the event-year sweep, task con-balccon.
- The maker's own page titles it simply "Mini Cyberdeck 0o00 (MC-0o00)" without the "BalCCon" prefix the sweep used; kept the sweep's fuller title since it matches how the community sheet and badge.gallery both refer to it.
status: listed
sources:
- kind: url
  url: https://ch405-labs.com/mc-0o00/
  title: BalCCon Mini Cyberdeck 0o00 (MC-0o00)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-balccon); event read as ''BalCCon 2024''.'
- kind: url
  url: https://badge.gallery/badges/balccon-2024-mc-0o00
  title: BalCCon Mini Cyberdeck 0o00 - badge.gallery
  accessed: '2026-09-08'
  note: Confirmed maker, event, MCU (CH32V003F6P6), ST7735 LCD, six buttons, buzzer, companion firmware apps (Melody Maker, Space Invaders MIT-licensed, CB Pong).
- kind: url
  url: https://ch405labs.net/mc-0o00/
  title: Mini Cyberdeck 0o00 - ch405labs.net
  accessed: '2026-09-08'
  note: 'This is the maker''s real, currently live project page (search-index snippet corroborates the badge.gallery description: "badge for the BalCCon 2k24 conference... CH32V003 processor... ST7735 lcd display, a piezoelectric buzzer and 6 buttons"). Could not be fetched directly this session (both WebFetch and curl timed out against ch405labs.net), so only the indexed snippet was read, not the full live page. The entry''s existing link ch405-labs.com/mc-0o00/ (note the hyphen) loads as empty/unreachable and appears to be a dead or unrelated domain, not the maker''s actual site.'
- kind: url
  url: https://gitlab.com/ch405labs/badgelife/mcd-0o00/mcd-0o00-hardware-design
  title: MCD 0o00 Hardware Design - GitLab
  accessed: '2026-09-08'
  note: Confirms a hardware-design repo exists for the badge (created Dec 2024, has a README); could not confirm license or EDA tool from the page excerpt available, so make_your_own.eda_tool and license were left blank.
- kind: url
  url: https://badge.gallery/addons/balccon-2024-mc-0o00/cb-pong
  title: CB Pong · Hacker Con Badges
  accessed: '2026-09-08'
  note: Documents the CB Pong firmware app as playable standalone or networked against a connected BCD-0o27; no price, availability, or image info on this page.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (maker, event, MCU, display, buttons, buzzer, companion firmware) are corroborated by badge.gallery and a search-engine snippet of the maker''s own live page, but the maker''s own page (ch405labs.net/mc-0o00/) could not be fetched directly this session — both WebFetch and curl timed out against that host, so confidence is medium rather than high. Not found anywhere: price, quantity made, availability/sold-out status, LED info, colors/shape/theme (no images seen), and a confirmed firmware license/repo URL beyond Space Invaders being called MIT-licensed. No images could be saved — the badge.gallery page states it has no rights-cleared images, and the maker''s own site could not be reached to check for photos. The existing ch405-labs.com/mc-0o00/ link (hyphenated domain) returned empty content both via WebFetch and curl; the maker''s actual site is ch405labs.net (no hyphen) — left the old link in place per instructions but flagged this in case it is dead or squatted.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/balccon-2024/balccon-mini-cyberdeck-0o00-mc-0o00.glb
  method: kicad
  source_file: MCD-0o00.kicad_pcb
  generated: '2026-09-10'
  bytes: 584452
---

The Mini Cyberdeck 0o00 (MC-0o00) is CH405 Labs' badge for BalCCon2k24 (Novi Sad, Serbia, 2024), built around a WCH CH32V003F6P6 RISC-V microcontroller. It carries an ST7735 LCD, six buttons, a piezoelectric buzzer, and a GPIO/power interface (2.7V-5.5V) that lets it connect to and interoperate with the previous year's badge, the BalCCon Cyberdeck 0o27 (BCD-0o27), rather than replace it.

Onboard firmware includes a handful of small apps documented on CH405 Labs' site and on badge.gallery: Melody Maker (a music-composition tool), Space Invaders (a game released under the MIT license with published source), and CB Pong, which can be played solo or networked against a connected BCD-0o27. A hardware self-test utility is also documented, though CH405 Labs notes the simple badge cannot fully diagnose itself and needs user confirmation during the test.

A hardware-design repository for the board exists on GitLab, but this pass could not confirm its license or which EDA tool was used, and could not reach the maker's own project page directly (network timeouts), relying instead on a corroborating badge.gallery writeup and a search-index snippet of the maker's page. Price, quantity produced, and current availability are not documented anywhere found.
