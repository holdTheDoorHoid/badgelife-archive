---
title: Disobey 2026 Badge
id: disobey-2026-disobey-2025-2026-badge
layout: badge
parent: Disobey 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: disobey-2026
year: 2026
makers:
- name: Disobey Badge Team
  url: https://github.com/disobeyfi
summary: An ESP32-S3 conference badge with a 1.9-inch TFT display, RGB LEDs and joystick controls, originally built for Disobey 2025 but delayed until Disobey 2026.
functions: Runs MicroPython social/competition games over OTA-updatable firmware, with a web-based flasher and inter-badge communication for event challenges.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - puzzle
  - ctf
tech:
  mcu: ESP32-S3 WROOM-2
  leds:
    count: null
    type: SK6812MINI
    note: RGB
  display: 1.9" TFT (ER-TFT019-1)
  connectivity:
  - wifi
  - ble
  battery: 3x AA or USB-C
  sao_version: null
  inputs:
  - joystick
  - buttons
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Handed out to attendees at Disobey 2026 (Kaapelitehdas, Helsinki, February 13-14, 2026).
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/disobeyfi/disobey-badge-2025-game-firmware
  firmware_url: https://github.com/disobeyfi/disobey-badge-2025-game-firmware
  eda_tool: null
links:
- label: badge.gallery/events/disobey-2026
  url: https://badge.gallery/events/disobey-2026
  kind: website
- label: badge.gallery/badges/disobey-2026-badge
  url: https://badge.gallery/badges/disobey-2026-badge
  kind: website
- label: disobeyfi/disobey-badge-2025-game-firmware (GitHub)
  url: https://github.com/disobeyfi/disobey-badge-2025-game-firmware
  kind: repo
- label: Disobey Badges web flasher
  url: https://badge.disobey.fi/web-flash/
  kind: website
- label: disobey2026badge Rust hardware support crate (docs.rs)
  url: https://docs.rs/crate/disobey2026badge/latest
  kind: repo
images: []
contact: {}
notes:
- 'Sweep-imported wording was "Disobey 2025/2026 Badge"; the maker''s own badge.gallery page and GitHub repo call it the Disobey 2026 badge (or "Disobey Badge 2025" in the firmware repo readme, reflecting its original target year), so the title here was updated to match the event it was actually distributed at.'
- 'No reusable images found: badge.gallery explicitly states no image is published because the official photos lack a clear reusable license, and no other source offered a usable image.'
- 'PCB design credited to "tracy"; game content credited to Piia Alavesa, per badge.gallery.'
status: released
sources:
- kind: url
  url: https://badge.gallery/events/disobey-2026
  title: Disobey 2025/2026 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-disobey); event read as ''Disobey 2026''.'
- kind: url
  url: https://badge.gallery/badges/disobey-2026-badge
  title: Disobey 2026 Badge · Hacker Con Badges
  accessed: '2026-09-08'
  note: Confirmed maker names (Disobey Badge Team, PCB by tracy, games by Piia Alavesa), venue/dates, and that no reusable image is published.
- kind: url
  url: https://github.com/disobeyfi/disobey-badge-2025-game-firmware
  title: disobeyfi/disobey-badge-2025-game-firmware
  accessed: '2026-09-08'
  note: Confirmed open-source firmware and hardware docs (HARDWARE.md), MicroPython game stack, OTA update support.
- kind: url
  url: https://badge.disobey.fi/web-flash/
  title: Web Flash | Disobey Badges
  accessed: '2026-09-08'
  note: Confirmed browser-based ESP Web Tools flasher for the badge.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Core facts (chip, display, LEDs, open-source firmware/hardware, delayed-from-2025 story) confirmed across badge.gallery and the maker's GitHub repo. Price, quantity made, LED count, and reusable images were not found anywhere checked; get_one.price/quantity and look.colors/shape/form_factor left empty. A separate Rust embedded tutorial (shadikka/disobey-badge-2026-tutorial) and a Rust hardware support crate (disobey2026badge, by Taneli Kaivola) exist for the same badge but are third-party tooling, not separate badges.
last_modified_date: '2026-09-08'
---

The Disobey 2026 badge is an ESP32-S3-based conference badge with a 1.9-inch TFT display, SK6812MINI RGB LEDs, and joystick/button controls, handed out at Disobey 2026 (Kaapelitehdas, Helsinki, February 13-14, 2026). It was originally built and slated for Disobey 2025, but production was delayed and the badges did not arrive until the following year's event. PCB design is credited to "tracy," with game content from Piia Alavesa.

The badge runs MicroPython-based social and competition games with support for over-the-air firmware updates and a browser-based flasher (ESP Web Tools) so attendees can reflash without installing drivers or software. Both hardware documentation and firmware are published on GitHub, and independent community tooling has grown up around it, including a Rust hardware-support crate and an embedded-Rust tutorial built specifically for this badge.

No price, production quantity, or reusable photos of the badge were found in the sources checked; the maker's own badge.gallery page notes that its images are not paired with an explicit reusable license.

## Make your own

Hardware and firmware are published together at [disobeyfi/disobey-badge-2025-game-firmware](https://github.com/disobeyfi/disobey-badge-2025-game-firmware), including a HARDWARE.md with schematics/3D models and MicroPython firmware built on `micropython-micro-gui`. The badge can be reflashed over USB via the browser-based [web flasher](https://badge.disobey.fi/web-flash/), or updated over the air once running Disobey firmware.
