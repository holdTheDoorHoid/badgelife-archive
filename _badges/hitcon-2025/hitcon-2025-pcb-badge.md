---
title: HITCON 2025 PCB Badge
id: hitcon-2025-hitcon-2025-pcb-badge
layout: badge
parent: HITCON 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hitcon-2025
year: 2025
makers:
- name: HITCON
summary: The official attendee PCB badge for HITCON 2025 (Taipei, August 15-16, 2025), built around an STM32F103CBT6 with a 128-LED matrix and an onboard motion sensor. Its signature feature is "Hacker Pet," a virtual-pet/pedometer mode, alongside built-in games and IR-based badge-to-badge play.
functions: Name editing, score display, brightness/display-mode settings, built-in games (Hacker Pet, Tetris, Dino, Snake), Red-vs-Blue tower-capture play between badges, Re:CTF badge-ID binding, cross-board IR communication, and BadUSB behavior.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - ctf
  - pop culture
tech:
  mcu: STM32F103CBT6
  leds:
    count: 128
    type: null
    note: 128-LED matrix display, row/column driven via DMA with PWM brightness control.
  display: LED matrix 128
  connectivity:
  - ir
  - uart
  battery: AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to HITCON 2025 attendees as part of the conference welcome kit; not sold separately.
make_your_own:
  open_source: true
  hardware_url: https://github.com/john0312/hitcon-pcb-badge
  firmware_url: https://github.com/john0312/hitcon-pcb-badge
  eda_tool: KiCad
  license: BSD-3-Clause
  notes: Repo also includes the base-station/backend and web components used for the conference leaderboard.
links:
- label: badge.gallery/years/2025
  url: https://badge.gallery/years/2025
  kind: website
- label: github.com/john0312/hitcon-pcb-badge
  url: https://github.com/john0312/hitcon-pcb-badge
  kind: repo
- label: pcb.hitcon.org/2025 (official user guide)
  url: https://pcb.hitcon.org/2025/
  kind: doc
- label: badge.gallery - Hacker Pet badge mode
  url: https://badge.gallery/addons/hitcon-2025-pcb-badge/hacker-pet-badge-mode
  kind: article
images: []
contact: {}
notes:
- HITCON 2025's PCB badge, described as a 'hacker-pet' with tower-defense-style play, per the badge.gallery compendium. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task general-2025.
- STM32F103CBT6 hacker-pet PCB badge with 128-LED matrix, LSM6DS3 motion sensor, pedometer scoring and Red-vs-Blue tower-capture play. Found by the event-year sweep, task con-hitcon.
- This is the same physical badge as entry hitcon-2025-hitcon-2025-pcb-badge (also in this archive); "Hacker Pet" is one game mode of the single HITCON 2025 PCB Badge, not a distinct hardware item. Kept the sweep's title as-is since it names a real, documented mode.
status: listed
sources:
- kind: url
  url: https://badge.gallery/years/2025
  title: HITCON 2025 PCB Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2025); event read as ''HITCON 2025''.'
- kind: url
  url: https://github.com/john0312/hitcon-pcb-badge
  title: HITCON 2025 PCB Badge (Hacker Pet)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-hitcon); event read as ''HITCON 2025''.'
- kind: url
  url: https://github.com/john0312/hitcon-pcb-badge
  title: john0312/hitcon-pcb-badge (repo)
  accessed: '2026-09-08'
  note: Confirms open-source firmware/PCB (BSD-3-Clause), STM32 MCU, LED matrix, IR cross-board comms, hardware revisions V1.1 (2024 CMT) through V2.2 (2025 attendee).
- kind: url
  url: https://badge.gallery/addons/hitcon-2025-pcb-badge/hacker-pet-badge-mode
  title: Hacker Pet badge mode - Hacker Con Badges
  accessed: '2026-09-08'
  note: Confirms maker (Justin/aoaaceai per HITCON 2025 dev talk), STM32F103CBT6, LSM6DS3 motion sensor, IR receiver, 128 LED positions, 8 tactile buttons, AAA battery + USB-C, full game/feature list, and that it shipped in the attendee welcome kit.
research:
  status: stub
  confidence: low
  last_checked: '2026-09-07'
  notes: Imported from the community badge sheet; not yet researched. Merged with duplicate entry 'HITCON 2025 PCB Badge (Hacker Pet)' (hitcon-2025-hitcon-2025-pcb-badge-hacker-pet).
last_modified_date: '2026-09-08'
redirect_from:
- /badges/hitcon-2025/hitcon-2025-pcb-badge-hacker-pet/
---


## Notes merged from the duplicate entry "HITCON 2025 PCB Badge (Hacker Pet)"

The HITCON 2025 PCB Badge is the attendee badge for HITCON 2025, held August 15-16, 2025 in Taipei. It is built around an STM32F103CBT6 microcontroller with a 128-position LED matrix, an LSM6DS3 motion sensor, an IR receiver/transmitter for badge-to-badge interaction, eight tactile buttons, a USB-C connector, and AAA battery power. The badge was developed by Justin (aoaaceai) as part of the HITCON activity team, following on from a 2024 CMT prototype revision (V1.1) through several 2025 prototypes (V2.0, V2.1) to the final attendee hardware (V2.2).

Its headline feature is "Hacker Pet," a virtual-pet mode that uses the onboard motion sensor as a pedometer to track the wearer's steps and feed a pet-care/scoring loop. The badge also runs several built-in games (Tetris, Dino, Snake), supports a Red-vs-Blue tower-capture game played over IR between badges, ties into the conference's Re:CTF challenge via badge-ID binding, and exhibits BadUSB behavior when connected to a computer. It was distributed free as part of the attendee welcome kit rather than sold.

## Make your own

The hardware (KiCad) and firmware are fully open-sourced under a BSD-3-Clause license at github.com/john0312/hitcon-pcb-badge, which also includes the backend/base-station and web components used to run the conference's badge leaderboard. The firmware is built in STM32CubeIDE; the repo documents separate build/run configurations for each hardware revision (V1.1 through V2.2), selectable to match the revision printed on the back of a given badge.
