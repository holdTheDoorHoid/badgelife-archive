---
title: Open Sauce 2026 VU Meter Badge
id: open-sauce-2026-open-sauce-vu-meter-badge
layout: badge
parent: Open Sauce 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: open-sauce-2026
year: 2026
makers:
- name: miekush
  url: https://github.com/miekush
summary: A sound-reactive novelty badge kit for Open Sauce 2026, hand-built around a bare PIC16F17576 in a DIP-40 package, a CR2032 cell, and an electret microphone, worn on a lanyard as a low-tech VU meter.
functions: Listens through an onboard electret microphone and drives a bar of LEDs as a real-time volume/VU meter, plus three extra "nose" LEDs, in deliberate contrast to "fancy IoT" sound-reactive gadgets.
look:
  colors:
  - yellow
  shape: robot
  themes:
  - music
  - hardware tool
  - robot
tech:
  mcu: PIC16F17576
  leds:
    count: 10
    type: discrete
    note: 'Through-hole LEDs: 7 form the main VU meter bar (green/yellow/red, each
      via a 220 ohm resistor off a GPIO pin) plus 3 separate "nose" LEDs, per the
      maker''s schematic.'
  display: none
  connectivity:
  - uart
  battery: CR2032
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: ''
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/miekush/open-sauce-vu-meter-badge
  eda_tool: KiCad
links:
- label: www.hackster.io/miekush/open-sauce-vu-meter-badge-afa1ef
  url: https://www.hackster.io/miekush/open-sauce-vu-meter-badge-afa1ef
  kind: article
- label: github.com/miekush/open-sauce-vu-meter-badge
  url: https://github.com/miekush/open-sauce-vu-meter-badge
  kind: repo
images:
- file: assets/images/badges/open-sauce-2026/open-sauce-vu-meter-badge/c100ef6b7f.jpg
  source: "https://github.com/miekush/open-sauce-vu-meter-badge"
  credit: "miekush"
  caption: "Unassembled kit parts for the Open Sauce 2026 VU Meter Badge: the yellow robot-shaped PCB, PIC16F17576 DIP-40 chip, CR2032 cell, through-hole LEDs, and a lanyard"
contact: {}
notes:
- 'Fact-check pass (2026-09-10): confirmed via the maker''s own GitHub README (title
  "Open Sauce 2026 VU Meter Badge", PIC-in-DIP-package-plus-electret-microphone
  description) and by rendering the cited schematic PDF, which is a genuine KiCad
  (v10.0.0) export titled "OPEN SAUCE 2026 VU METER BADGE" by Mike Kushnerik, file
  open_sauce_badge_v1.kicad_sch, dated 2026-07-07. The schematic shows a CR2032
  battery, an electret mic (POM-3535P-3-R), 7 VU-meter LEDs plus 3 "nose" LEDs, a
  UART breakout header, an ICSP header, and no SAO connector. The maker''s own kit
  photo (used as the entry image) shows loose, unsoldered parts -- PCB, DIP-40 chip,
  battery, LEDs, headers, a DIP socket -- plus a lanyard, confirming kit distribution
  and that the board is not an SAO. The `type` was accordingly corrected from
  "sao" to "badge" (no source ever called it an add-on/SAO; that was an
  unsupported inference in the prior pass), and the image caption was corrected
  from "Assembled" to reflect the unassembled kit shown. tech.leds, tech.display,
  tech.connectivity, tech.battery, tech.sao_version, and get_one.distribution
  were filled in from the schematic/photo, which were already-cited sources. The
  Hackster.io project page remains blocked by Cloudflare on every fetch attempt
  (WebFetch and curl both returned 403), so price, quantity, and availability
  still cannot be confirmed and are left empty.'
status: listed
sources:
- kind: url
  url: https://www.hackster.io/miekush/open-sauce-vu-meter-badge-afa1ef
  title: Open Sauce VU Meter Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-open-sauce);
    event read as ''Open Sauce''. Still Cloudflare-blocked as of 2026-09-10 (403
    on WebFetch and curl).'
- kind: url
  url: https://github.com/miekush/open-sauce-vu-meter-badge
  title: miekush/open-sauce-vu-meter-badge
  accessed: '2026-09-10'
  note: Maker's own repo; README (fetched raw) confirms the exact title "Open Sauce
    2026 VU Meter Badge", the PIC-in-DIP-package-plus-electret-microphone concept,
    and provided the badge/kit photo used in this entry. Contains MPLAB/PIC firmware
    sources only, no hardware/KiCad project files.
- kind: url
  url: https://hacksterio.s3.amazonaws.com/uploads/attachments/1977051/open_sauce_mic_badge_2026_7zQCyz3g7n.pdf
  title: 'Open Sauce 2026 VU Meter Badge schematic PDF (Hackster attachment)'
  accessed: '2026-09-10'
  note: Downloaded and rendered directly. Genuine KiCad E.D.A. 10.0.0 schematic
    export (file open_sauce_badge_v1.kicad_sch), titled "OPEN SAUCE 2026 VU METER
    BADGE", by Mike Kushnerik, dated 2026-07-07. Confirms PIC16F17576, CR2032
    battery, electret mic part POM-3535P-3-R, 7 VU LEDs + 3 "nose" LEDs each via
    220 ohm resistors, a UART header, an ICSP header, a mode switch, and a gain
    trimmer; shows no SAO connector.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Core specs (maker, event/year, MCU, mic, battery, LED layout, kit format,
    KiCad tooling) are now confirmed directly from the maker''s own repo, his own
    schematic file, and his own kit photo. Kept at "researched" rather than
    "verified" because the maker''s main Hackster.io writeup -- likely the source
    for price, quantity, and availability -- remains unreachable behind a
    persistent Cloudflare block, so those fields stay empty rather than confirmed.
    No storefront or press coverage found beyond an Instagram repost noted in an
    earlier pass (not independently re-verified here).'
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/open-sauce-vu-meter-badge/
---

The Open Sauce 2026 VU Meter Badge is an unofficial kit made by Mike Kushnerik (miekush) for Open Sauce 2026. Builders solder up a bare Microchip PIC16F17576, in a through-hole DIP-40 package, alongside a CR2032 coin cell and an electret microphone to turn ambient sound into a real-time volume/VU display on a bar of LEDs, styled as a deliberately low-tech answer to "fancy IoT" sound-reactive gear. The yellow PCB is cut into a robot-like face, complete with a pair of googly eyes and three extra "nose" LEDs, and hangs from a lanyard.

The maker's GitHub repository holds MPLAB/PIC firmware sources (MCC-generated config, CMake build scaffolding, PIC16F17576 build output) along with the kit photo used here. A KiCad-drawn schematic for the board (titled "Open Sauce 2026 VU Meter Badge," dated July 2026) is available as a PDF export linked from the project's Hackster.io page, and confirms the CR2032 power, the microphone wiring, the 220 ohm LED bar, a UART breakout, and an ICSP programming header -- but no full KiCad project, Gerbers, or BOM were found published anywhere, and no SAO connector appears on the board. The Hackster.io page itself stayed behind a Cloudflare block through this research pass, so price, quantity made, and current availability are unconfirmed and left blank.

## Make your own

The firmware (MPLAB X / MCC project for the PIC16F17576) is published at [github.com/miekush/open-sauce-vu-meter-badge](https://github.com/miekush/open-sauce-vu-meter-badge). No hardware source files (KiCad project, Gerbers, BOM) have been found published, only a rendered schematic PDF, so this is a firmware-only open release for now.
