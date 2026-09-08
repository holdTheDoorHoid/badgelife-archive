---
title: ToorCamp 2024 Deer Badge
id: toorcamp-2024-toorcamp-2024-deer-badge
layout: badge
parent: ToorCamp 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: toorcamp-2024
year: 2024
makers:
- name: lithiumbot
summary: An ATtiny85-based electronic-dice badge shaped like a glowing cyberdeer skull, built for ToorCamp 2024's forested "cyberdeer" theme.
functions: Functions as an electronic die - pressing a tactile switch rolls a random result shown by seven 3mm LEDs wired in pairs (via PWM) to light up the deer skull's "eyes" in dice patterns.
look:
  colors: []
  shape: skull
  themes:
  - animal
  - skull
  - horror
tech:
  mcu: ATtiny85
  leds:
    count: 7
    type: discrete
    note: Seven 3mm LEDs wired mostly in pairs to fit the ATtiny85's limited outputs, forming dice-style pip patterns.
  display: none
  connectivity: []
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - kit
  where: 'Parts kits were handed out at ToorCamp 2024''s Hardware Hacking Stage during scheduled build times; OlyMEGA camp volunteers helped attendees solder and assemble it themselves.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/lithiumbot/deerbadge2024
  firmware_url: https://github.com/lithiumbot/deerbadge2024
  eda_tool: null
links:
- label: github.com/lithiumbot/deerbadge2024
  url: https://github.com/lithiumbot/deerbadge2024
  kind: repo
images:
  - file: assets/images/badges/toorcamp-2024/toorcamp-2024-deer-badge/3d49bcee40.jpg
    source: "https://github.com/lithiumbot/deerbadge2024"
    credit: "lithiumbot"
    caption: "Assembled Deer Badge with glowing dice-pattern LED eyes"
  - file: assets/images/badges/toorcamp-2024/toorcamp-2024-deer-badge/0db19fda4b.jpg
    source: "https://github.com/lithiumbot/deerbadge2024"
    credit: "lithiumbot"
    caption: "Deer Badge PCB prototype"
contact: {}
notes:
- Unofficial ATtiny85-based electronic-dice badge with a glowing cyberdeer-skull design made for ToorCamp 2024's camp/horror theme. Found by the event-year sweep, task con-toorcon.
status: released
sources:
- kind: url
  url: https://github.com/lithiumbot/deerbadge2024
  title: ToorCamp 2024 Deer Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-toorcon); event read as ''ToorCamp 2024''.'
- kind: url
  url: https://github.com/lithiumbot/deerbadge2024
  title: "lithiumbot/deerbadge2024 README"
  accessed: '2026-09-08'
  note: "Confirmed maker, event, ATtiny85/LED/switch build, PWM eye animation, free build-your-own distribution at the Hardware Hacking Stage, and open firmware/schematics."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: "The repo README confirms the badge exists and gives build details, but doesn't state a print run size or price (parts were given away free at a build station, so no price applies). No standalone schematic/PCB CAD source file was found in the repo (only rendered schematic and layout images plus the Arduino .ino firmware), so make_your_own.open_source is set to partial and eda_tool left null. No SAO header is mentioned or shown; treated as a standalone badge, sao_version: none."
last_modified_date: '2026-09-08'
---

The Deer Badge is an unofficial, community-built electronic-dice badge made by lithiumbot for ToorCamp 2024, whose "cyberdeer" theme fit the con's forested Doe Bay campsite. The artwork - a deer skull floating over the bay - is styled after a horror-movie poster, playing on the idea of camping somewhere a slasher film might be set.

Under the skull, the badge is a simple ATtiny85 project: pressing a tactile switch triggers a PWM-driven light sequence across seven 3mm LEDs, most wired in pairs to make the most of the chip's limited output pins, so the deer's "eyes" flash dice-style pip patterns like an electronic die roll.

Rather than being sold or handed out pre-built, the badge was distributed as a build-it-yourself kit: attendees picked up parts at ToorCamp 2024's Hardware Hacking Stage during scheduled build times, where OlyMEGA camp volunteers ran soldering stations to help people assemble their own.

## Make your own

The GitHub repo (github.com/lithiumbot/deerbadge2024) publishes the Arduino firmware (`toorcamp2024_GlowEyesBadgePWM.ino`, plus a `toorcamp2024_sleepy_dicebadge` variant) along with schematic and PCB-layout images and a parts list: a 10k and a 100 ohm resistor, an ATtiny85 in an 8-pin DIP socket, seven 3mm LEDs, and a 4-leg tactile switch (with a spare, unused switch footprint). No separate CAD source file (KiCad/Eagle/etc.) is included in the repo, only rendered schematic and layout images, so hardware files are only partially open.
