---
title: Kernelcon 2019 K Badge
id: kernelcon-2019-kernelcon-2019-k-badge
layout: badge
parent: Kernelcon 2019
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: kernelcon-2019
year: 2019
makers:
- name: ZonkSec (Tyler Rosonke)
- name: diggeroflogs
- name: scotchsec
summary: An ATtiny85-powered, K-shaped electronic badge for Kernelcon 2019 with five APA102 RGB LEDs and a built-in binary-blink CTF.
functions: 'A mode button cycles through seven LED behaviors: independent color fading, freeze states, synchronized fading, binary output, a fast-changing "rave" mode, and looping color-progression animations. The binary-output mode encodes data for an on-badge CTF with four challenges (extracting binary from the LED pattern, an SSRF exploit, a restricted "DNA service" endpoint, and capturing auth headers from an intercepted request), backed by Docker-hosted challenge infrastructure. Separate variants existed for hackers, crew/organizers, and speakers.'
look:
  colors: []
  shape: k
  themes:
  - ctf
  - security
  - learn to solder
tech:
  mcu: ATtiny85
  leds:
    count: 5
    type: APA102
    note: five addressable RGB LEDs
  display: none
  connectivity: []
  battery: 3x CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to attendees, crew, and speakers at Kernelcon 2019 (Omaha, Nebraska).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/ZonkSec/kernelcon-2019-badge
  eda_tool: null
links:
- label: badge.gallery/badges/kernelcon-2019-k-badge
  url: https://badge.gallery/badges/kernelcon-2019-k-badge
  kind: website
- label: github.com/ZonkSec/kernelcon-2019-badge
  url: https://github.com/ZonkSec/kernelcon-2019-badge
  kind: repo
- label: zonksec.com/blog/kernelcon-electronic-badges-and-pogopin-hackery
  url: https://zonksec.com/blog/kernelcon-electronic-badges-and-pogopin-hackery/
  kind: website
images:
  - file: assets/images/badges/kernelcon-2019/kernelcon-2019-k-badge/a1ff8e7dcd.png
    source: "https://github.com/ZonkSec/kernelcon-2019-badge"
    credit: "ZonkSec"
    caption: "Front of the Kernelcon 2019 K badge"
  - file: assets/images/badges/kernelcon-2019/kernelcon-2019-k-badge/39a5e394bb.png
    source: "https://github.com/ZonkSec/kernelcon-2019-badge"
    credit: "ZonkSec"
    caption: "Back of the Kernelcon 2019 K badge"
contact: {}
notes:
- ATtiny85-powered, K-shaped badge with five APA102 RGB LEDs and a binary-blink CTF, distributed at Kernelcon 2019. Found by the event-year sweep, task con-kernelcon.
- 'Title unchanged: the maker''s own repo and blog post both call this the Kernelcon 2019 badge / "K badge" shape, matching the sheet''s wording.'
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/kernelcon-2019-k-badge
  title: Kernelcon 2019 K Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kernelcon); event read as ''Kernelcon 2019''.'
- kind: url
  url: https://zonksec.com/blog/kernelcon-electronic-badges-and-pogopin-hackery/
  title: 'Kernelcon Electronic Badges and Pogopin Hackery - ZonkSec blog'
  accessed: '2026-09-08'
  note: Maker's own write-up confirming event/year, makers, ATtiny85 MCU, 5x APA102 LEDs, CR2032 power, and the binary-blink CTF concept.
- kind: url
  url: https://github.com/ZonkSec/kernelcon-2019-badge
  title: ZonkSec/kernelcon-2019-badge (GitHub repo)
  accessed: '2026-09-08'
  note: Maker's repo confirming hardware specs, the seven LED modes, four CTF challenges with Docker infrastructure, and source of the front/back photos saved to this entry.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts (maker, event/year, MCU, LED count/type, power, CTF concept) confirmed directly on the maker's own blog and GitHub repo. Price and quantity made are not stated anywhere found. PCB/solder-mask color, exact silkscreen theme colors, and license for the repo are not specified in the sources, so left empty. No public storefront found; badge was distributed free at the event, so availability left as unknown/free_drop rather than guessed as sold via purchase.
last_modified_date: '2026-09-08'
---

ZonkSec (led by Tyler Rosonke, with diggeroflogs and scotchsec) built the K-shaped electronic badge handed out at Kernelcon 2019 in Omaha, Nebraska. Each badge runs on an ATtiny85 and drives five APA102 addressable RGB LEDs, powered by three CR2032 coin cells with a physical power switch and a mode button.

A single button cycles through seven LED behaviors — independent per-LED color fading, freeze states, synchronized fading, a binary-output mode, a fast "rave" mode, and looping color-progression animations. The binary-output mode is the entry point to an on-badge CTF: attendees decode binary data from the blink pattern to work through four challenges, including an SSRF exploit, a restricted "DNA service" endpoint, and capturing authentication headers from an intercepted request, all backed by Docker-hosted challenge infrastructure. Kernelcon issued separate badge variants for hackers, crew/organizers, and speakers.

## Make your own

The firmware and CTF challenge code are published on GitHub at ZonkSec/kernelcon-2019-badge, including the Docker setup for the challenge backend and the front/back reference photos of the physical badge. No hardware design files (schematic/PCB/Gerbers) or an explicit license were found in the repository at the time of this research.
