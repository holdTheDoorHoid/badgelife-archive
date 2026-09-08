---
title: Kernelcon 2023 1337 kHz Radio Badge
id: kernelcon-2023-kernelcon-2023-1337-khz-radio-badge
layout: badge
parent: Kernelcon 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: kernelcon-2023
year: 2023
makers:
- name: Kevin Neubauer (bl4cksmith)
  url: https://infosec.exchange/@bl4cksmith
- name: Tyler Rosonke (zonksec)
  url: https://twitter.com/zonksec
summary: An all-analog AM radio badge for Kernelcon 2023, built around the 10-cent TA7642 radio IC with no microcontroller at all.
functions: Tunes and listens to AM radio (including several transmitters set up around the con) via a single inductor/capacitor tuner, a small transistor amplifier, and a headphone jack; includes a labeled prototyping area for badge-hacking-village activities.
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
tech:
  mcu: none
  leds: null
  display: none
  connectivity:
  - audio
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
- label: badge.gallery/badges/kernelcon-2023-1337-khz-radio-badge
  url: https://badge.gallery/badges/kernelcon-2023-1337-khz-radio-badge
  kind: website
- label: 2023.badge.kernelcon.org
  url: https://2023.badge.kernelcon.org/
  kind: website
- label: 2023.badge.kernelcon.org/about.html
  url: https://2023.badge.kernelcon.org/about.html
  kind: website
- label: Kevin Neubauer (bl4cksmith) on infosec.exchange
  url: https://infosec.exchange/@bl4cksmith
  kind: social
- label: Tyler Rosonke (zonksec) on Twitter
  url: https://twitter.com/zonksec
  kind: social
images:
- file: assets/images/badges/kernelcon-2023/kernelcon-2023-1337-khz-radio-badge/b1b6e19b25.png
  source: "https://2023.badge.kernelcon.org/"
  credit: "Kernelcon 2023 (Kevin Neubauer / Tyler Rosonke)"
  caption: "The Kernelcon 2023 1337 kHz AM radio badge"
contact: {}
notes:
- Analog TA7642-based AM radio conference badge for Kernelcon 2023. Found by the event-year sweep, task con-kernelcon.
- The sweep's title matched the maker's own naming exactly ("1337 khz badge"); no correction needed.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/kernelcon-2023-1337-khz-radio-badge
  title: Kernelcon 2023 1337 kHz Radio Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kernelcon); event read as ''Kernelcon 2023''.'
- kind: url
  url: https://2023.badge.kernelcon.org/
  title: 1337 khz | kernelcon 2023 badge
  accessed: '2026-09-08'
  note: Maker's own badge site; confirms it is an AM radio badge with an interactive BOM and badge-hacking-village activities, and links the Radio.png badge photo.
- kind: url
  url: https://2023.badge.kernelcon.org/about.html
  title: About | 1337 khz kernelcon 2023 badge
  accessed: '2026-09-08'
  note: 'Maker''s own About page: confirms designers Kevin Neubauer and Tyler Rosonke, assembly by Cyber City Circuits (Augusta, GA), TA7642 IC, 1.5V design (too low to drive most LEDs), transistor amp for headphones, mono audio to both channels, and the RF gain knob hack for the TA7642''s weak AGC.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own site (2023.badge.kernelcon.org) confirms designers, chip, and design intent directly. Could not find price, quantity produced, availability/distribution details, or any published hardware/firmware repo (there is no firmware since the badge has no MCU; an interactive BOM exists on the site's ibom.html page but no linked schematic/Gerber repo was found). LED and connectivity beyond audio left empty since the badge has no MCU or lighting circuit worth noting beyond the note that 1.5V is too low for most LEDs.
last_modified_date: '2026-09-08'
---

The Kernelcon 2023 badge broke from the microcontroller-and-blinky norm entirely: it is a fully analog AM radio, built around the TA7642, a roughly 10-cent radio-on-a-chip. Designed and prototyped by Kevin Neubauer (bl4cksmith) and Tyler Rosonke (zonksec) and assembled by Cyber City Circuits in Augusta, Georgia, the badge runs on just 1.5V — a voltage low enough that, as the makers note on their site, most LEDs simply won't light up on it. Several AM transmitters were set up around the Kernelcon venue for attendees to tune in with the badge's single inductor/capacitor tuner.

Beyond the radio itself, the badge includes a small transistor amplifier driving a headphone jack (mono audio sent to both channels) and a notable RF Gain knob. The makers explain this knob exists specifically to work around the TA7642's weak automatic gain control: without it, in Omaha the tuner would simply pick up the strong local AM station (1110 KFAB) across the entire dial, drowning out the con's own transmitters. Turning down the RF tuner's power improves selectivity enough to actually separate stations. The badge also carries a labeled, unpopulated prototyping area intended for badge-hacking-village activities, continuing the design's playful embrace of the era's component shortages by avoiding microcontrollers and flash chips altogether.

No pricing, production quantity, or public hardware/firmware repository was found; the maker's site hosts an interactive bill of materials for the badge but no linked schematic or Gerber files were located.
