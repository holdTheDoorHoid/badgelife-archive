---
title: Cyber Saiyan WHY2025 Badge (Dragon Sphere)
id: why-2025-cyber-saiyan-why2025-badge-dragon-sphere
layout: badge
parent: Why 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: why-2025
year: 2025
makers:
- name: Cyber Saiyan community
  url: https://www.cybersaiyan.it/why2025/
summary: An independent community badge Cyber Saiyan brought to WHY2025, styled after Dragon Ball's dragon spheres, with a color TFT screen, BLE badge-radar, and Wi-Fi schedule sync.
functions: Shows the event logo and schedule, a BLE radar screen that detects nearby badges, a badge list, Wi-Fi tools, and a Snake game; also runs several LED animation modes.
look:
  colors: []
  shape: null
  themes:
  - anime
  - sci-fi
  - security
tech:
  mcu: ESP32-C3
  leds:
    count: 7
    type: WS2812B
    note: Individually addressable front RGB LEDs
  display: 2.8in TFT LCD (240x320, ST7789 controller)
  connectivity:
  - wifi
  - ble
  battery: LiPo with onboard charging circuit and power switch
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '200'
  availability: free
  distribution:
  - free_drop
  where: Given out at the Cyber Saiyan Village at WHY2025 (August 2025).
make_your_own:
  open_source: yes
  hardware_url: https://github.com/CyberSaiyanIT/why2025-badge/tree/main
  firmware_url: https://github.com/CyberSaiyanIT/why2025-badge/tree/main
  eda_tool: null
links:
- label: github.com/CyberSaiyanIT/why2025-badge
  url: https://github.com/CyberSaiyanIT/why2025-badge
  kind: repo
images:
- file: assets/images/badges/why-2025/cyber-saiyan-why2025-badge-dragon-sphere/cb1481b17a.png
  source: "https://github.com/CyberSaiyanIT/why2025-badge/tree/main"
  credit: "Cyber Saiyan community"
  caption: "WHY2025 badge, front view"
- file: assets/images/badges/why-2025/cyber-saiyan-why2025-badge-dragon-sphere/4a7de8361d.png
  source: "https://github.com/CyberSaiyanIT/why2025-badge/tree/main"
  credit: "Cyber Saiyan community"
  caption: "WHY2025 badge, rear view"
contact: {}
notes:
- Independent community badge brought to WHY2025 by the Cyber Saiyan group, dragon-sphere themed and built on an ESP32-C3 with a 2.8in TFT, BLE badge-radar, and Wi-Fi; an evolution of their earlier RomHack Camp 2022 badge, later re-adapted for EMF Camp 2026. Found by the event-year sweep, task dutch-camps.
- The sweep's title matched the maker's own naming on the repo README; no change needed.
status: released
sources:
- kind: url
  url: https://github.com/CyberSaiyanIT/why2025-badge
  title: Cyber Saiyan WHY2025 Badge (Dragon Sphere)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dutch-camps); event read as ''why-2025''.'
- kind: url
  url: https://github.com/CyberSaiyanIT/why2025-badge/tree/main
  title: why2025-badge README (main branch)
  accessed: '2026-09-08'
  note: Confirms maker, event, hardware specs, software features, quantity (200), free distribution at the Cyber Saiyan Village, and open-source status.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Repo default branch now shows a later EMF Camp 2026 revision of the same board (readme updated in place); the "main" branch still holds the original WHY2025-specific README used for this entry, confirming it was made for WHY2025 (Aug 2025), 200 made, free giveaway at the Cyber Saiyan Village. Price was not stated anywhere. No mention found of it being an evolution of a RomHack Camp 2022 badge on the maker''s own pages (that claim came from the sweep''s notes and could not be independently confirmed, so it is kept only as sweep provenance, not asserted as fact in the body).'
last_modified_date: '2026-09-08'
---

The Cyber Saiyan community, an Italian hacker collective, brought this independent badge to WHY2025 in August 2025 as a giveaway at their Cyber Saiyan Village. It is styled after the dragon spheres from Dragon Ball, built around an ESP32-C3 with a 2.8" color TFT (ST7789 controller) and seven addressable WS2812B RGB LEDs on the front, plus Wi-Fi and Bluetooth 5 LE.

On screen it offers an event logo/splash, a schedule viewer that can sync over Wi-Fi, a BLE-based "radar" that detects other nearby badges, a badge list, and a Snake game, alongside several LED animation modes. Two dial-wheel switches handle navigation. It runs on a LiPo battery with an onboard charging circuit and power switch, and exposes 16 programmable GPIOs with expansion connectors for hacking.

Cyber Saiyan made 200 of the badges and gave them away free at their village rather than selling them. The hardware and firmware are fully open source on GitHub under an MIT-compatible license. The same design was later revised and reused for EMF Camp 2026, which is now the repository's default branch; the original WHY2025 README lives on the repo's `main` branch.
