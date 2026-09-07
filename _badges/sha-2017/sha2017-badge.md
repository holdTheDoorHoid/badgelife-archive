---
title: SHA2017 Badge
id: sha-2017-sha2017-badge
layout: badge
parent: Sha 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: sha-2017
year: 2017
makers:
- name: Badge.Team, led by Niek Blankers and Sebastian Oort (Markus Bechtold, Bas van Sisseren, Jeroen Domburg/Sprite_tm, Renze Nicolai, et al.)
  url: https://badge.team/
summary: A reprogrammable ESP32 conference badge with an e-paper display, built by Badge.Team for the SHA2017 "Still Hacking Anyway" camp in the Netherlands.
functions: Runs MicroPython apps distributed through Badge.Team's "Hatchery" app repository; connects to the camp Wi-Fi; supports NFC-style capacitive touch input; drives an e-ink display and optional add-on LEDs and a vibration motor for notifications/games.
look:
  colors:
  - red
  shape: rectangle
  themes:
  - hardware tool
  - learn to solder
  - kit
tech:
  mcu: ESP32 (Wroom module)
  leds:
    count: 6
    type: SK6812
    note: RGBW LEDs; unpopulated pads on the front of the board that attendees solder on themselves (adding parts to the front required a second pass through pick-and-place, so they shipped as a DIY add-on).
  display: 2.9" e-paper (DKE Group DEPG0290B1, pinout-compatible with the GDEH029A1)
  connectivity:
  - wifi
  inputs:
  - touch
  - capacitive
  battery: LiPo 1000mAh, 1S 3.7V, JST-PH3 connector, charged via onboard TP4056; also includes a vibration motor as a DIY add-on
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to SHA2017 attendees; the project describes itself as funded by sponsorship/crowdfunding on top of ticket sales rather than sold separately, per the event wiki.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/SHA2017-badge/PCB
  firmware_url: https://github.com/SHA2017-badge
  eda_tool: Eagle
  notes: 'PCB repo (Eagle 6.6 board files, rev1_0_1 is the final production revision) is MIT licensed. Firmware and other project repos are under the SHA2017-badge and badge.team GitHub organizations. App repository ("Hatchery"): https://badge.sha2017.org'
links:
- label: badge.team/docs/badges/sha2017
  url: https://badge.team/docs/badges/sha2017/
  kind: website
- label: SHA2017-badge PCB (Eagle, MIT)
  url: https://github.com/SHA2017-badge/PCB
  kind: repo
- label: SHA2017-badge GitHub organization
  url: https://github.com/SHA2017-badge
  kind: repo
- label: SHA2017 badge wiki page
  url: https://wiki.sha2017.org/w/Projects:Badge
  kind: doc
- label: Hardware documentation (components, LUT, power)
  url: https://badge.team/docs/badges/sha2017/hardware/
  kind: doc
- label: Getting started / assembly guide
  url: https://badge.team/docs/badges/sha2017/getting_started/
  kind: doc
images:
- file: assets/images/badges/sha-2017/sha2017-badge/eaef39e9a7.png
  source: "https://badge.team/docs/badges/sha2017/getting_started/"
  credit: "Badge.Team"
  caption: "Assembly guide close-ups of the badge PCB: SK6812 LED strip, vibration motor, and LiPo battery mount"
contact: {}
notes:
- E-paper hackable conference badge; foundational badge.team firmware platform badge.
- Kit as handed out included the badge board, battery, an adhesive hook-and-loop pad, 6x SK6812 RGBW LEDs, a vibration motor, and a lanyard; LEDs and motor were DIY solder-on add-ons and the badge works fine without them.
- Touch input uses an MPR121 capacitive touch/GPIO expander (not physical buttons for the touch pads); IRQ tied to ESP32 GPIO25.
- USB-serial bridge is a Silicon Labs CP2102 (needs a driver on macOS).
status: released
sources:
- kind: url
  url: https://badge.team/docs/badges/sha2017/
  title: SHA2017 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''SHA2017''.'
- kind: url
  url: https://badge.team/docs/badges/sha2017/hardware/
  title: SHA2017 Badge Hardware
  accessed: '2026-09-07'
  note: Component list (ESP32 Wroom, DEPG0290B1 e-paper, MPR121 touch controller, SK6812 LED pads, TP4056 charger, AP2114H LDO, LiPo 1000mAh battery, CP2102 USB-serial), expansion connector pinout.
- kind: url
  url: https://badge.team/docs/badges/sha2017/getting_started/
  title: SHA2017 Badge Getting Started
  accessed: '2026-09-07'
  note: Kit contents flyer (badge, battery, hook-and-loop pad, 6x SK6812 RGBW LEDs, vibration motor, lanyard), power-on instructions, Hatchery/wiki/GitHub links.
- kind: url
  url: https://en.wikipedia.org/wiki/Electronic_badge
  title: Electronic badge (Wikipedia)
  accessed: '2026-09-07'
  note: Confirms e-ink screen + ESP32 for the SHA2017 ("Still Hacking Anyway") badge.
- kind: url
  url: https://github.com/SHA2017-badge/PCB
  title: SHA2017-badge/PCB
  accessed: '2026-09-07'
  note: Hardware repo is Eagle 6.6 board files, MIT licensed; rev1_0_1 is the final badge revision.
- kind: url
  url: https://github.com/SHA2017-badge
  title: SHA2017-badge GitHub organization
  accessed: '2026-09-07'
  note: Organization lists firmware, PCB, scarves, MicroPython port, and Hatchery repos.
- kind: url
  url: https://wiki.sha2017.org/w/Projects:Badge
  title: SHA2017 wiki - Projects:Badge
  accessed: '2026-09-07'
  note: Notes the badge required sponsorship/crowdfunding beyond ticket sales; no explicit price or quantity given.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s own documentation (badge.team docs + SHA2017-badge GitHub org) confirmed hardware, firmware, and kit contents in detail. Not found anywhere: unit price, total quantity produced, and an explicit statement that every attendee received one for free vs. it being ticket-bundled. The exact firmware repo name (vs. the MicroPython port) was not pinned down precisely. A second flyer image (text-only, kit contents list) was fetched but not added to `images` since it does not show the badge itself.'
last_modified_date: '2026-09-07'
---

The SHA2017 badge was Badge.Team's flagship device for the "Still Hacking Anyway" hacker camp held in the Netherlands in August 2017, and the project that established the badge.team ESP32 firmware platform later reused for MCH2022 and other events. Built around an ESP32 Wroom module and a 2.9" DKE Group DEPG0290B1 e-paper display, it ran MicroPython apps that attendees could write and share through Badge.Team's "Hatchery" app repository, connecting over the camp Wi-Fi. Input came via an MPR121 capacitive touch controller doubling as a GPIO expander rather than mechanical buttons.

Attendees received a kit rather than a finished gadget: the board, a 1000 mAh LiPo battery, an adhesive hook-and-loop pad, six SK6812 RGBW LEDs, a vibration motor, and a lanyard, with the LEDs and motor left for hackers to solder on themselves at camp (adding parts to the front of the board would have required a second pass through the pick-and-place machine). The badge worked out of the box without those add-ons. Power came from a TP4056 charger and AP2114H LDO regulator, with a USB-serial bridge (Silicon Labs CP2102) for reflashing and hacking.

Hardware (Eagle board files, MIT licensed) and firmware are both open source under the SHA2017-badge GitHub organization. The event's wiki notes that the badge's components and manufacturing were funded through sponsorship and crowdfunding on top of ticket sales, rather than sold as a separate product; exact unit price and total quantity produced were not found in the sources checked.

## Make your own

Board files live in the [SHA2017-badge/PCB](https://github.com/SHA2017-badge/PCB) repository (Eagle 6.6, revision `rev1_0_1` is the final production board, MIT licensed). Firmware and MicroPython app sources are in the wider [SHA2017-badge GitHub organization](https://github.com/SHA2017-badge). The original DEPG0290B1 display is hard to source today; badge.team's hardware docs describe switching to a pinout-compatible GDEH029A1 panel via an NVS flag (`eink.dev.type`) in the on-device MicroPython shell.
