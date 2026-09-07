---
title: BornHack 2024 Badge
id: bornhack-2024-bornhack-2024-badge
layout: badge
parent: Bornhack 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2024
year: 2024
makers:
- name: Thomas Flummer
summary: 'A slim rectangular ESP32-C3 badge for BornHack 2024 with a row of addressable LEDs for persistence-of-vision effects and an NFC chip used for an onsite game.'
functions: 'Persistence-of-vision LED effects and light shows; NFC tag (readable and, via the NT3H2x11, writable) used for an onsite game; expandable over SAO and QWiC connectors and GPIO pads.'
look:
  colors: []
  shape: rectangle
  themes:
  - radio
  - hardware tool
tech:
  mcu: ESP32-C3
  leds:
    count: 16
    type: WS2812B
    note: Row of addressable LEDs used for persistence-of-vision (POV) effects.
  display: none
  connectivity:
  - nfc
  battery: LiPo
  sao_version: v1
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to BornHack 2024 ticket holders as the event badge.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/bornhack/badge2024
  firmware_url: https://github.com/bornhack/badge2024
  eda_tool: KiCad
  license: CC-BY-SA-4.0
links:
- label: hackaday.com/2025/08/01/two-for-the-price-of-one-bornhack-2024-and-2025-badges
  url: https://hackaday.com/2025/08/01/two-for-the-price-of-one-bornhack-2024-and-2025-badges/
  kind: article
  archived: https://web.archive.org/web/20260717220115/https://hackaday.com/2025/08/01/two-for-the-price-of-one-bornhack-2024-and-2025-badges/
- label: github.com/bornhack/badge2024
  url: https://github.com/bornhack/badge2024
  kind: repo
- label: github.com/Pwnies/bornhack-badge-esp32-c3-rust
  url: https://github.com/Pwnies/bornhack-badge-esp32-c3-rust
  kind: repo
images:
  - file: assets/images/badges/bornhack-2024/bornhack-2024-badge/b119efb2cd.jpg
    source: "https://hackaday.com/2025/08/01/two-for-the-price-of-one-bornhack-2024-and-2025-badges/"
    credit: "Hackaday"
    caption: "Both sides of the BornHack 2024 badge PCB"
contact: {}
notes:
- ESP32-C3 Mini, NT3H2x11 NFC chip, LIS2DH accelerometer, SAO and QWiC connectors, POV LED display
status: released
sources:
- kind: url
  url: https://hackaday.com/2025/08/01/two-for-the-price-of-one-bornhack-2024-and-2025-badges/
  title: BornHack 2024 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''BornHack 2024''.'
  archived: https://web.archive.org/web/20260717220115/https://hackaday.com/2025/08/01/two-for-the-price-of-one-bornhack-2024-and-2025-badges/
- kind: url
  url: https://hackaday.com/2025/08/01/two-for-the-price-of-one-bornhack-2024-and-2025-badges/
  title: 'Two-For-The-Price-Of-One: BornHack 2024 And 2025 Badges'
  accessed: '2026-09-07'
  note: Confirmed maker (Thomas Flummer), board dimensions, ESP32-C3 Mini, LED PoV row, NT3H2x11 NFC chip, SAO/QWiC connectors, LiPo power circuit; source of the saved photo.
- kind: url
  url: https://github.com/bornhack/badge2024
  title: bornhack/badge2024
  accessed: '2026-09-07'
  note: Official hardware/firmware repo. Confirmed 16x WS2812 LEDs, LIS2DH accelerometer, NTAG NFC, KiCad design files, CC-BY-SA-4.0 license, and a 3D-printed case on a branch.
- kind: url
  url: https://github.com/Pwnies/bornhack-badge-esp32-c3-rust
  title: Pwnies/bornhack-badge-esp32-c3-rust
  accessed: '2026-09-07'
  note: Community Rust firmware examples for the badge's ESP32-C3, found via GitHub search; noted as an additional link, not used for factual claims.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'No price or production-quantity figures found; it was distributed as the standard event badge to BornHack 2024 ticket holders rather than sold, so get_one.price is left empty. Display field left as none since the LEDs form a linear PoV strip rather than a matrix/screen; not stated as a dedicated display component. SAO header count not explicitly stated in sources checked; recorded as 1 based on "SAO and QWiC connectors" phrasing (singular SAO, singular QWiC) — flagged as inferred rather than directly confirmed.'
last_modified_date: '2026-09-07'
---

The BornHack 2024 badge was designed by Thomas Flummer as the standard event badge for BornHack 2024, the Danish outdoor hacker camp. It is a slim rectangular PCB, roughly 140 by 45 mm, built around an ESP32-C3 Mini module with a row of 16 WS2812B addressable LEDs used to create persistence-of-vision light effects. An NT3H2x11 NFC chip doubles as a passive tag and an addressable component, which the organizers used for an onsite game, and an LIS2DH accelerometer supports motion-based effects. The badge is expandable through a SAO connector, a QWiC connector, and general GPIO pads, and it runs from a LiPo battery with charging and power circuitry on the rear of the board.

Hardware and firmware are fully open source, published by the BornHack team on GitHub under the CC-BY-SA-4.0 license, with KiCad schematic and PCB files and a 3D-printed case design available on a separate branch. A community-contributed Rust firmware for the badge's ESP32-C3 also exists as a separate project.

## Make your own

The official hardware (KiCad) and firmware are at https://github.com/bornhack/badge2024, released under CC-BY-SA-4.0. A community Rust firmware alternative is at https://github.com/Pwnies/bornhack-badge-esp32-c3-rust.
