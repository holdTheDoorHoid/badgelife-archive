---
title: BSides Canberra 2020/2021 badge (SAMD21/ESP32 e-paper badge)
id: bsides-canberra-2021-bsides-canberra-2020-2021-badge-samd21-esp32-e-paper-badge
layout: badge
parent: BSides Canberra 2021
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-canberra-2021
year: 2021
makers:
- name: Penten
  url: https://www.penten.com/
  role: badge design and sponsorship
- name: BSidesCbr
  role: community volunteers, firmware collaboration
summary: A dual-MCU electronic badge for BSides Canberra 2021, combining an ATSAMD21G18A and an ESP32-PICO-D4 with an e-paper display, RGB LEDs, and capacitive touch buttons, designed for hacking.
functions: Capacitive-touch button input, RGB and status LED lighting, an e-ink display driven by the ESP32, a microSD slot, and expansion headers for an IR transceiver, audio codec, IMU, flash, and RAM add-ons sold onsite as an expansion pack.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: ATSAMD21G18A + ESP32-PICO-D4
  leds:
    count: 11
    type: RGB
    note: 8 RGB LEDs plus 3 user LEDs, driven by the SAMD21
  display: e-paper
  connectivity:
  - ir
  battery: LiPo, 2x AAA pack, or USB 2.0
  sao_version: v1
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Given to attendees of the BSides Canberra 2020/2021 conference (9-10 April 2021, Canberra, Australia); an expansion pack with extra components (IR transceiver, audio codec, IMU, flash, RAM) was sold onsite separately.
make_your_own:
  open_source: true
  hardware_url: null
  firmware_url: https://gitlab.com/bsidescbr-2021-badge/2021-badge
  eda_tool: null
  notes: Firmware/build system is on GitLab with submodules and git-lfs assets (Docker or Ubuntu/Debian build environment, ./build.sh to build and flash). Schematics were said to be posted on the conference's own badge page (bsidesau.com.au/badge2021.html), which is no longer live.
links:
- label: gitlab.com/bsidescbr-2021-badge/2021-badge
  url: https://gitlab.com/bsidescbr-2021-badge/2021-badge
  kind: repo
- label: github.com/BSidesCbr/2021Badge
  url: https://github.com/BSidesCbr/2021Badge
  kind: repo
  archived: https://web.archive.org/web/20251102070010/https://github.com/BSidesCbr/2021Badge
- label: 'BSides Canberra: badge reveal post (Facebook)'
  url: https://www.facebook.com/BSidesCanberra/posts/checking-out-the-bsidescbr2021-electronic-badge-designed-sponsored-by-penten-no-/3686957694721112/
  kind: social
images:
- file: assets/images/badges/bsides-canberra-2021/bsides-canberra-2020-2021-badge-samd21-esp32-e-paper-badge/ed0efcb693.jpg
  source: https://www.facebook.com/BSidesCanberra/posts/checking-out-the-bsidescbr2021-electronic-badge-designed-sponsored-by-penten-no-/3686957694721112/
  credit: BSides Canberra / Penten
  caption: The BSides Canberra 2021 electronic badge
contact: {}
notes:
- Hybrid electronic badge combining a SAMD21 and ESP32 with an e-paper display, LEDs and capacitive touch, with full hardware/firmware source on GitLab. Found by the event-year sweep, task bsides-canberra.
- Sweep imported title matches the maker's repo title ('BSides Canberra 2021 Badge' / '2020-2021 badge' used interchangeably in the README); kept as-is.
status: released
sources:
- kind: url
  url: https://gitlab.com/bsidescbr-2021-badge/2021-badge
  title: BSides Canberra 2020/2021 badge (SAMD21/ESP32 e-paper badge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-canberra); event read as ''BSides Canberra 2021''.'
- kind: url
  url: https://gitlab.com/bsidescbr-2021-badge/2021-badge/-/raw/develop/README.md
  title: BSides Canberra 2021 Badge README
  accessed: '2026-09-10'
  note: Confirms maker (Penten, with BSidesCbr community volunteers), event dates (9-10 April 2021), hardware (ATSAMD21G18A + ESP32-PICO-D4, 8 capacitive touch buttons, 3 user LEDs, 8 RGB LEDs, SAO header, eInk display, 5 user buttons, microSD, expansion pack components), power options, MIT license.
- kind: url
  url: https://www.facebook.com/BSidesCanberra/posts/checking-out-the-bsidescbr2021-electronic-badge-designed-sponsored-by-penten-no-/3686957694721112/
  title: 'BSides Canberra Facebook post: badge reveal'
  accessed: '2026-09-10'
  note: Confirms the badge was designed and sponsored by Penten, and provided the only photo of the badge found.
- kind: url
  url: https://github.com/BSidesCbr/2021Badge
  title: BSidesCbr/2021Badge on GitHub
  accessed: '2026-09-10'
  note: Mirror/companion repo of the same badge project; no additional details beyond the GitLab README.
  archived: https://web.archive.org/web/20251102070010/https://github.com/BSidesCbr/2021Badge
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Maker's own README (GitLab) confirms MCU, LED, display, touch, power, and license details, and a Facebook post from the event organizers supplied the one photo found. Price, quantity produced, and distribution/availability were not stated anywhere found; the conference's own badge detail page (bsidesau.com.au/badge2021.html), which reportedly had schematics, now 404s and was not recoverable. Assumed given to attendees rather than sold, consistent with typical con-badge distribution, but this is not explicitly confirmed by a source, so get_one.availability is left unknown and get_one.distribution empty rather than guessed.
last_modified_date: '2026-09-10'
---

The BSides Canberra 2020/2021 badge was designed and sponsored by the Canberra-based security firm Penten, developed in collaboration with BSidesCbr community volunteers, and distributed at the BSides Canberra V conference held 9-10 April 2021. It is a dual-microcontroller design built around an Atmel/Microchip ATSAMD21G18A and an ESP32-PICO-D4, giving it two "hacking surfaces": the SAMD21 side drives 8 capacitive touch buttons, 3 user LEDs, 8 RGB LEDs, an infra-red transceiver (expansion), and a Shitty Add-On header, while the ESP32 side drives an e-paper (eInk) display, 5 physical buttons, a microSD card slot, and expansion pads for an audio codec, an inertial measurement unit, extra flash, and extra RAM. Power can come from a LiPo cell, a 2xAAA pack, or USB. Attendees could buy an expansion pack onsite to populate some of the unpopulated component footprints.

Firmware and the full build toolchain (Docker or native Ubuntu/Debian, using a `build.sh` wrapper and CMake) are published under the MIT license on GitLab, with a companion mirror on GitHub. The conference's own page with schematics and compiled firmware (bsidesau.com.au/badge2021.html) is no longer reachable, so pricing, production quantity, and exact distribution mechanics were not confirmed by any source found in this pass.
