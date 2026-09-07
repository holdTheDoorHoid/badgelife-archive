---
title: Telephreak 12 Badge (Geiger counter for WiFi deauth frames)
id: dc27-telephreak-12-badge-geiger-counter-for-wifi-deauth-frames
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Nick Price (dominotree)
  url: https://spun.io/
summary: A directional "Geiger counter" for WiFi deauthentication frames, chirping when it detects deauth packets instead of radiation.
functions: Listens for 802.11 deauthentication frames over WiFi and chirps/alerts when one is detected, acting like a directional Geiger counter pointed at the source of the deauth attack.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - measurement
  - hardware tool
tech:
  mcu: ESP32
  leds: null
  display: null
  connectivity:
  - wifi
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: spun.io/2019/07/26/a-geiger-counter-for-wifi-deauthentication-frames-the-telephreak-12-badge
  url: https://spun.io/2019/07/26/a-geiger-counter-for-wifi-deauthentication-frames-the-telephreak-12-badge/
  kind: website
- label: 'Hackaday: Great Badge Concept - A "Geiger Counter" For WiFi Deauthentication Frames'
  url: https://hackaday.com/2020/06/20/great-badge-concept-a-geiger-counter-for-wifi-deauthentication-frames/
  kind: article
images:
- file: assets/images/badges/dc27/telephreak-12-badge-geiger-counter-for-wifi-deauth-frames/1098b82283.jpg
  source: "https://spun.io/2019/07/26/a-geiger-counter-for-wifi-deauthentication-frames-the-telephreak-12-badge/"
  credit: "Nick Price (dominotree)"
  caption: "Prototype Telephreak 12 badge PCB"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: unknown
sources:
- kind: url
  url: https://spun.io/2019/07/26/a-geiger-counter-for-wifi-deauthentication-frames-the-telephreak-12-badge/
  title: "A Geiger Counter for WiFi Deauthentication Frames: the Telephreak 12 Badge"
  accessed: '2026-09-07'
  note: "Maker's own project blog (Nick Price / dominotree); describes the concept, an ESP32-based board replicating Adafruit's HUZZAH32 design, and a copper pipe end-cap antenna modification for directionality. Written while the badge was still in final prototyping ahead of DEF CON 27, ~$40 estimated cost."
- kind: url
  url: https://hackaday.com/2020/06/20/great-badge-concept-a-geiger-counter-for-wifi-deauthentication-frames/
  title: 'Great Badge Concept: A "Geiger Counter" For WiFi Deauthentication Frames'
  accessed: '2026-09-07'
  note: "Hackaday's write-up of the same project, revisited roughly a year later; states the badge was not completed in time for the intended DEF CON event, leaving its final production/distribution status unclear."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >
    Made by Nick Price (handle dominotree) for the Telephreak party at DEF CON 27 (2019), as
    a follow-up to his Telephreak 11 badge (2018, ATmega328-based). Concept: a directional
    detector that chirps when it senses WiFi deauthentication frames, like a Geiger counter
    for deauth attacks. Built around a custom ESP32 board that replicates Adafruit's HUZZAH32
    Feather design, described by the maker as a hackable, Arduino/Feather-compatible platform.
    Directionality came from wrapping the PCB's omnidirectional antenna in a copper pipe end
    cap rather than the originally-planned (impractical) PCB Yagi antenna. No LED, display, or
    battery details were given in either source. No source repository (hardware or firmware)
    was found despite the "hackable platform" framing, so make_your_own fields are left empty.
    Quantity produced, final price, and whether it was actually distributed/sold at DEF CON 27
    are unknown: the spun.io post (July 2019) describes the badge still being finished, and
    Hackaday's later piece (June 2020) states it was not completed in time for its intended
    DEF CON event, so status is left as "unknown" rather than "released". No Tindie/storefront,
    Hackaday.io project page, or GitHub/GitLab repo for this specific badge (as distinct from
    the Telephreak 11 badge repo) was located.
last_modified_date: '2026-09-07'
---

The Telephreak 12 badge was Nick Price's (dominotree) 2019 follow-up to his Telephreak 11 badge, made for the Telephreak party at DEF CON 27. Instead of a conventional badge, he built a directional detector for WiFi deauthentication frames: point it at a source of deauth packets and it chirps, the same way a Geiger counter clicks faster near a source of radiation. The idea reportedly came to him while watching a TV miniseries about the Chernobyl disaster.

Under the hood the badge is a custom ESP32 board designed to replicate Adafruit's HUZZAH32 Feather, which the maker pitched as a hackable platform buildable with the Arduino IDE. To get directionality out of the board's PCB antenna without resorting to an oversized, expensive four-layer PCB Yagi antenna, he instead soldered a copper pipe end cap (sourced from a hardware store's plumbing aisle) around the antenna's ground plane.

As of the maker's July 2019 write-up the badge was still being finished, with an estimated build cost around $40 and final software and distribution details undecided. A Hackaday piece revisiting the project in mid-2020 notes it was not completed in time for its intended DEF CON outing, so it is unclear whether it was ever finished, produced in quantity, or actually handed out — no storefront, repository, or production photos for the finished badge were found.
