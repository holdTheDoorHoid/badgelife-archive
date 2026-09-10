---
title: NerdFlareBadge25
id: other-nerdflarebadge25
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: NerdFlare
  url: https://github.com/NerdFlare
summary: A member badge from NerdFlare, an electronics-art club at Cal Poly San Luis Obispo, built for the 2024-25 academic year to bring "badgelife" PCB-art culture to campus.
functions: Runs several non-blocking LED light modes (sunrise/sunset fade, three marquee chase patterns, random blink) selected with a button; over BLE it advertises its name and scans for other NerdFlare25 badges nearby, switching to a "random blink" mode that scales with how many other badges are detected.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - learn to solder
  - wearable
  form_factor: pcb badge
tech:
  mcu: Raspberry Pi Pico 2 W
  leds:
    count: 10
    type: discrete
    note: 7 red + 3 yellow discrete SMD LEDs (Würth WL-SMSW), each driven via PWM.
  display: none
  connectivity:
  - ble
  inputs:
  - buttons
  battery: 2x AA
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - membership
  where: Distributed to NerdFlare club members/participants at Cal Poly SLO (e.g. an IEEE x NerdFlare soldering competition); not sold to the public as far as sources indicate.
make_your_own:
  open_source: true
  hardware_url: https://github.com/NerdFlare/NerdFlareBadge25/tree/main/pcb
  firmware_url: https://github.com/NerdFlare/NerdFlareBadge25/tree/main/src
  eda_tool: KiCad
  gerbers_url: null
  bom_url: https://github.com/NerdFlare/NerdFlareBadge25/blob/main/pcb/NerdFlare25-BOM.csv
  license: null
  fab_url: null
  notes: Firmware is MicroPython (uses aioble for BLE); KiCad PCB source and a BOM (~$10.80/unit at qty 50) are in the repo, but no README or license file is present.
links:
- label: github.com/NerdFlare/NerdFlareBadge25
  url: https://github.com/NerdFlare/NerdFlareBadge25
  kind: repo
- label: NerdFlare (Cal Poly) on GitHub
  url: https://github.com/NerdFlare
  kind: website
images: []
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: released
sources:
- kind: url
  url: https://github.com/NerdFlare/NerdFlareBadge25
  title: NerdFlareBadge25
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/NerdFlare/NerdFlareBadge25/main/src/main.py
  title: 'NerdFlareBadge25: src/main.py'
  accessed: '2026-09-07'
  note: Firmware version (1.2.1), LED mode list, BLE advertise/scan behavior, button-driven mode switching.
- kind: url
  url: https://raw.githubusercontent.com/NerdFlare/NerdFlareBadge25/main/src/nerdflare25.py
  title: 'NerdFlareBadge25: src/nerdflare25.py'
  accessed: '2026-09-07'
  note: Pin-level hardware driver confirming 10 discrete PWM-driven LEDs and a pull-up button on GP8.
- kind: url
  url: https://raw.githubusercontent.com/NerdFlare/NerdFlareBadge25/main/pcb/NerdFlare25-BOM.csv
  title: 'NerdFlareBadge25: pcb/NerdFlare25-BOM.csv'
  accessed: '2026-09-07'
  note: Bill of materials confirming Raspberry Pi Pico 2 W, 2xAA battery holder, LED colors/counts, switches, per-unit cost.
- kind: url
  url: https://github.com/NerdFlare
  title: Cal Poly NerdFlare (GitHub organization)
  accessed: '2026-09-07'
  note: Identifies NerdFlare as "Cal Poly NerdFlare", a US-based organization.
- kind: url
  url: https://hackaday.com/2025/09/30/2025-hackaday-speakers-round-one-and-spoilers/
  title: 2025 Hackaday Speakers, Round One! And Spoilers
  accessed: '2026-09-07'
  note: 'Lists a talk by Zachary Peterson (the repo''s committing author), "NerdFlare: Bringing #badgelife to Academia," describing NerdFlare as a Cal Poly PCB-art/badge initiative that grew into a campus-wide creative movement.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'NerdFlare is a Cal Poly San Luis Obispo student club/initiative (per its GitHub org name "Cal Poly NerdFlare" and a 2025 Hackaday Supercon talk by Zachary Peterson, "NerdFlare: Bringing #badgelife to Academia"), not a hacker-convention badge, so no matching id exists in events.yml; leaving event as ''other''. The repo name and firmware banner both read "NerdFlare25" for "24-25 AY" (academic year), read here as year 2025. No README, license, or price/quantity/distribution details were published in the repo; get_one.where is inferred from IEEE Cal Poly''s mention of an "IEEE x NerdFlare Soldering Competition" and could not be confirmed as the only distribution channel. No photos of an assembled badge were found (repo only contains a KiCad PCB, BOM, MicroPython source, and one Cal Poly shield SVG logo), so images could not be saved.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/nerdflarebadge25.glb
  method: kicad
  source_file: pcb/NerdFlare25.kicad_pcb
  generated: '2026-09-10'
  bytes: 133316
---

NerdFlareBadge25 is a member/participant badge from NerdFlare, a PCB-art and electronics club at Cal Poly San Luis Obispo, made for the 2024-25 academic year. It is built around a Raspberry Pi Pico 2 W running MicroPython, with ten discrete LEDs (seven red, three yellow) driven by PWM for several light patterns, a single push button to cycle modes, and a two-AA battery holder for standalone power. NerdFlare describes itself as bringing "badgelife" PCB-art culture into a university setting, and the badge appears to have circulated through club activities such as an IEEE-co-hosted soldering competition, though no README or public sale listing spells out exact distribution numbers or price.

Over Bluetooth Low Energy, each badge advertises its own presence and scans for other NerdFlare25 badges nearby; when it detects others, it switches into a "random blink" pattern whose speed and LED count scale with how many other badges are in range, turning a room of badge-wearers into a loosely synchronized light show. Other selectable modes include a sunrise/sunset fade and three marquee chase patterns, cycled with the button. Firmware and KiCad hardware source are both published on GitHub under the Cal Poly NerdFlare organization, along with a bill of materials pricing the board at roughly $10.80 per unit at a quantity of 50.

## Make your own

Hardware (`pcb/`, KiCad project + BOM) and firmware (`src/`, MicroPython) are both in the [GitHub repo](https://github.com/NerdFlare/NerdFlareBadge25). No license file is present, so terms of reuse are unstated.
