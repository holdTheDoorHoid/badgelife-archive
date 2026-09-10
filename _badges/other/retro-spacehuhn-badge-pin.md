---
title: Spacehuhn Blinky LED Badge
id: other-retro-spacehuhn-badge-pin
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2018
makers:
- name: davedarko
  url: https://github.com/davedarko
- name: Stefan Kremser (Spacehuhn)
  url: https://spacehuhn.com/
summary: A hand-painted blinky pin of the Spacehuhn logo (a chicken in a space helmet), with two fading RGB LEDs for eyes, made as a tribute to Spacehuhn's ESP8266 deauther work after a badge conversation at 34C3.
functions: Two RGB LEDs fade/blink automatically as animated eyes; no other interactivity.
look:
  colors:
  - white
  - multicolor
  shape: null
  themes:
  - animal
  - bird
  - space
  - pin
  - logo
tech:
  mcu: none
  leds:
    count: 2
    type: RGB
    note: fading/animated RGB LEDs used as the badge's eyes
  display: null
  connectivity: []
  battery: 2x CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing checked 2026-09-07: seller retired, item no longer purchasable.'
  distribution:
  - purchase
  where: Sold as a kit on Tindie (davedarko's store), and separately listed by Spacehuhn Technologies on Tindie.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SpaceHuhn%20Badge
  firmware_url: null
  eda_tool: Eagle
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/33886-spacehuhn-badge
  url: https://hackaday.io/project/33886-spacehuhn-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260515101515/https://hackaday.io/project/33886-spacehuhn-badge
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/SpaceHuhn%20Badge
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SpaceHuhn%20Badge
  kind: repo
- label: '@Spacehuhn blinky LED badge kit — Tindie (davedarko)'
  url: https://www.tindie.com/products/davedarko/spacehuhn-blinky-led-badge-kit/
  kind: store
  archived: https://web.archive.org/web/20260513145034/https://www.tindie.com/products/davedarko/spacehuhn-blinky-led-badge-kit/
- label: Spacehuhn Badge — Tindie (Spacehuhn Technologies)
  url: https://www.tindie.com/products/spacehuhn/spacehuhn-badge/
  kind: store
  archived: https://web.archive.org/web/20260503121823/https://www.tindie.com/products/spacehuhn/spacehuhn-badge/
images:
- file: assets/images/badges/other/retro-spacehuhn-badge-pin/0bde639695.jpg
  source: https://www.tindie.com/products/davedarko/spacehuhn-blinky-led-badge-kit/
  credit: davedarko (Tindie)
  caption: Assembled Spacehuhn blinky badge, hand-painted marker-colored PCB with RGB LED eyes
  archived: https://web.archive.org/web/20260513145034/https://www.tindie.com/products/davedarko/spacehuhn-blinky-led-badge-kit/
- file: assets/images/badges/other/retro-spacehuhn-badge-pin/9ba0a68f19.jpg
  source: https://www.tindie.com/products/davedarko/spacehuhn-blinky-led-badge-kit/
  credit: davedarko (Tindie)
  caption: Spacehuhn badge, second listing photo showing the kit
  archived: https://web.archive.org/web/20260513145034/https://www.tindie.com/products/davedarko/spacehuhn-blinky-led-badge-kit/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/33886-spacehuhn-badge
  title: Spacehuhn badge | Hackaday.io
  accessed: '2026-09-07'
  note: Origin story (34C3 conversation with Stefan Kremser, Jan 2018), 2/3/5mm LED and hand-painting experiments, ongoing-project status.
  archived: https://web.archive.org/web/20260515101515/https://hackaday.io/project/33886-spacehuhn-badge
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/SpaceHuhn%20Badge
  title: SpaceHuhn Badge folder in Simple-Add-ons-SAO repo
  accessed: '2026-09-07'
  note: Confirms hardware files exist (Eagle .sch/.brd) with rev2/rev3 subfolders; no firmware, since the board is passive (no MCU).
- kind: url
  url: https://www.tindie.com/products/davedarko/spacehuhn-blinky-led-badge-kit/
  title: '@Spacehuhn blinky LED badge kit from davedarko on Tindie'
  accessed: '2026-09-07'
  note: 'Listing details: 2 fading RGB LEDs, ~5x5cm PCB, SMD switch, solderable pin, battery holder, 2x CR2032 not included; hand-painted white silkscreen with markers; listing now retired/sold out. Source of both saved images.'
  archived: https://web.archive.org/web/20260513145034/https://www.tindie.com/products/davedarko/spacehuhn-blinky-led-badge-kit/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for no specific con — a tribute badge started after a badge-design chat at 34C3 (Dec 2017/Jan 2018), so event stays "other" (34C3 is not in events.yml and the maker explicitly says it was not made for that event). Price and quantity made were not stated on any source found. A second Tindie listing exists under "Spacehuhn Technologies" (spacehuhn/spacehuhn-badge) which may be a re-listing of the same item or a related product; not confirmed as distinct. Hardware files (Eagle schematic/board, rev2/rev3) are published in the linked repo; no firmware exists since the board has no MCU (tech.mcu: none, passive RGB blink circuit).'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/retro-spacehuhn-badge-pin.glb
  method: kicad
  source_file: badge_spacehuhn.brd
  generated: '2026-09-10'
  bytes: 34356
---

The Spacehuhn Blinky LED Badge is a small pin-style tribute badge honoring Stefan Kremser ("Spacehuhn"), author of the ESP8266 deauther project. Maker davedarko started the badge in January 2018 after the two discussed badge designs at 34C3 (the 34th Chaos Communication Congress); it was not made for any specific convention, but as a standalone project. The badge depicts Spacehuhn's chicken-in-a-space-helmet logo on a roughly 5cm x 5cm PCB, with two fading RGB LEDs standing in for the character's eyes.

Because affordable full-color PCB printing wasn't practical at the time, davedarko colored the badge's white silkscreen by hand using Edding 4200-series permanent markers, giving each unit a slightly individual, hand-painted look; the Hackaday.io project log documents experiments with 3mm, 5mm, and "straw hat" LED packages to get the eye glow right. The finished kit includes the PCB, two RGB LEDs, an SMD switch, a solderable pin back, and a battery holder for two CR2032 cells (batteries not included), and requires basic soldering to assemble.

The badge was sold as a kit on Tindie under davedarko's store; that listing has since been retired and is no longer purchasable, and price/quantity figures were not published anywhere found. The Eagle schematic and board files (with later rev2 and rev3 revisions) are published in davedarko's Simple-Add-ons-SAO GitHub repository, though no firmware is needed since the circuit is a passive blinker with no microcontroller.
