---
title: HackConRD 2024 Badge
id: other-hhw-hackconrd2024
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2024
makers:
- name: jrgdiaz
  url: https://github.com/jrgdiaz
summary: The official first-ever conference badge for HackConRD (Dominican Republic), an ATtiny85-based badge with addressable RGB LEDs and a buzzer, worn on a lanyard with embedded challenges.
functions: Runs event-specific firmware with hidden challenges and secrets; drives 9 onboard addressable RGB LEDs (expandable with external aRGB strips) with custom animation patterns; plays melodies through an onboard buzzer. Fully reprogrammable, including the bootloader, over a USB-TTL serial interface.
look:
  colors: []
  shape: null
  themes:
  - ctf
  - hardware tool
  - learn to solder
tech:
  mcu: ATtiny85
  leds:
    count: 9
    type: RGB
    note: Addressable (aRGB) LEDs driven from physical PIN 2; three pins broken out next to D9 allow chaining external aRGB LEDs.
  display: none
  connectivity:
  - uart
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to attendees of HackConRD 2024, a hacking conference in the Dominican Republic.
make_your_own:
  open_source: true
  hardware_url: https://github.com/jrgdiaz/HHW_HackConRD2024
  firmware_url: https://github.com/jrgdiaz/HHW_HackConRD2024
  eda_tool: KiCad
links:
- label: github.com/jrgdiaz/HHW_HackConRD2024
  url: https://github.com/jrgdiaz/HHW_HackConRD2024
  kind: repo
images:
- file: assets/images/badges/other/hhw-hackconrd2024/2ad46bf5a1.png
  source: https://github.com/jrgdiaz/HHW_HackConRD2024
  credit: jrgdiaz
  caption: 3D rendering of the HackConRD 2024 badge PCB
- file: assets/images/badges/other/hhw-hackconrd2024/077ef317e9.jpg
  source: https://github.com/jrgdiaz/HHW_HackConRD2024
  credit: jrgdiaz
  caption: Physical HackConRD 2024 badge connected via USB-TTL serial interface
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/jrgdiaz/HHW_HackConRD2024
  title: HHW_HackConRD2024
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''HackConRD 2024 (Dominican Republic)''.'
- kind: url
  url: https://github.com/jrgdiaz/HHW_HackConRD2024
  title: HHW_HackConRD2024 README
  accessed: '2026-09-07'
  note: 'Full README (bilingual ES/EN): chip specs, LED/buzzer pin usage, bootloader instructions, KiCad manufacturing files, image URLs.'
- kind: url
  url: https://verpent.co/posts/hackconrd2024
  title: HackConRD 2024 Badge Features - Verpent
  accessed: '2026-09-07'
  note: Third-party summary of the same GitHub README; confirmed chip/LED/buzzer details, no pricing or quantity found.
  archived: https://web.archive.org/web/20260209091126/https://verpent.co/posts/hackconrd2024
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: HackConRD is a hacking conference held in the Dominican Republic; no matching event id exists in _data/events.yml (searched for "hackconrd" and "dominican" with no hits), so event is left as "other" per instructions. This is described in the README as the first-ever official HackConRD badge, marking the start of Badgelife in that community. No pricing, production quantity, or storefront was found anywhere; it appears to have been given to conference attendees rather than sold, so get_one.price/quantity/availability are left empty/unknown. No PCB solder-mask color or shape could be confirmed from the 3D-render image alone with confidence, so look.colors/shape are left empty.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/hhw-hackconrd2024.glb
  method: kicad
  source_file: HackConRD_Badge_Fab-main_unz/HackConRD_Badge_Fab-main/HackconRD_Badge.kicad_pcb
  generated: '2026-09-10'
  bytes: 119772
---

The HackConRD 2024 Badge is the first official conference badge for HackConRD, a hacking conference in the Dominican Republic, designed by GitHub user jrgdiaz. It marks, in the maker's own words, "the beginning of Badgelife" in that community's hacker scene. The badge is built around an ATtiny85 microcontroller (8 KB flash, 512 bytes SRAM, 6 I/O pins, 1.8–5.5V, 8 MHz) and features 9 onboard addressable RGB LEDs driven from a single pin, with three additional pins broken out next to D9 so attendees can chain on external aRGB strips and write their own animation patterns. A buzzer on a separate pin can play melodies.

At the conference the badge shipped with event-specific firmware containing hidden challenges and secrets, worn on a lanyard, but it is fully reprogrammable — including the bootloader (Optiboot, pre-installed) — over an exposed USB-TTL serial interface, using the Arduino IDE with the ATTinyCore board package. No price, production quantity, or public sale was found; it reads as a badge given to conference attendees rather than sold through a storefront.

## Make your own

The maker published the complete KiCad design (`HackConRD_Badge_Fab-main.zip`) along with a BOM/assembly CSV in the GitHub repository, plus step-by-step instructions for burning the Optiboot bootloader onto a fresh ATtiny85 with an Arduino Nano and for uploading new sketches over the badge's serial header.
