---
title: WHY2025 Badge
id: why-2025-why2025-badge
layout: badge
parent: Why 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: why-2025
year: 2025
makers:
- name: Team:Badge (WHY2025), repo at gitlab.com/why2025/team-badge
summary: The official electronic badge for WHY2025, built around two ESP32 modules plus a LoRa radio, with a 3.95" LCD and a built-in mechanical-dome keyboard.
functions: Runs the BadgeVMS operating system and third-party apps distributed through BadgeHub (badge.why2025.org); supports Meshtastic over its 868MHz LoRa radio; a Doom port was demonstrated running on the badge's screen.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - radio
tech:
  mcu: ESP32 (dual)
  leds: null
  display: 3.95" LCD (W395HDC001-A)
  connectivity:
  - wifi
  - lora
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: over 3500 made
  availability: unknown
  distribution: []
  where: Distributed to WHY2025 attendees; some units handed out unassembled and built by attendees at the on-site BadgeTent.
make_your_own:
  open_source: partial
  hardware_url: https://gitlab.com/why2025/team-badge
  firmware_url: https://gitlab.com/why2025/team-badge
  eda_tool: null
links:
- label: wiki.why2025.org/Badge
  url: https://wiki.why2025.org/Badge
  kind: website
- label: gitlab.com/why2025/team-badge
  url: https://gitlab.com/why2025/team-badge
  kind: repo
images:
  - file: assets/images/badges/why-2025/why2025-badge/242051d346.jpg
    source: "https://wiki.why2025.org/Badge"
    credit: "WHY2025 Team:Badge"
    caption: "Assembled WHY2025 badge with keyboard, 3.95in LCD, and LoRa antenna"
  - file: assets/images/badges/why-2025/why2025-badge/343bcbeff9.jpg
    source: "https://wiki.why2025.org/Badge"
    credit: "WHY2025 Team:Badge"
    caption: "WHY2025 badge running Doom on its 3.95in LCD"
contact: {}
notes:
- Dual ESP32 + LoRa (868MHz) badge, 3.95in LCD (W395HDC001-A), solder.party keyboard dome layer, M.2 accessory connector, SAO adapter support, runs BadgeVMS firmware; app hub at badge.why2025.org (BadgeHub).
status: released
sources:
- kind: url
  url: https://wiki.why2025.org/Badge
  title: WHY2025 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: eu-camps: European hacker camps/cons via badge.team (SHA2017, Hackerhotel, Disobey, CampZone, Fri3d Camp, MCH2022, WHY2025), EMF Camp TiLDA lineage, CCC card10, and BornHack); event read as ''WHY2025''.'
- kind: url
  url: https://wiki.why2025.org/Badge
  title: WHY2025 Badge - wiki.why2025.org
  accessed: '2026-09-07'
  note: 'Confirmed dual-ESP32 + LoRa architecture, 3.95in LCD (W395HDC001-A), dome-switch keyboard, dual USB-C, over 3500 units produced, some distributed unassembled and built at BadgeTent, BadgeVMS firmware, GitLab hardware repo, Meshtastic and Doom demonstrated.'
- kind: url
  url: https://gitlab.com/why2025/team-badge
  title: Team:Badge · GitLab
  accessed: '2026-09-07'
  note: 'GitLab group page confirmed to exist for the badge team; page content beyond the title was not retrievable via fetch, so hardware/firmware file details and license could not be verified directly.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core specs (dual ESP32, LoRa, 3.95in LCD, keyboard, BadgeVMS, BadgeHub) confirmed from the maker wiki. Could not verify: price, exact LED count/type, battery type/capacity, SAO header version, or license terms on the GitLab repo (the repo page loaded but its file contents were not retrievable through the fetch tool). Availability status left unknown since no storefront/sale terms were found — badge appears to have been distributed to attendees rather than sold, but no price data was found. Web search was unavailable (session search budget exhausted) so only the wiki and a GitLab landing check were consulted.'
last_modified_date: '2026-09-07'
---

The WHY2025 Badge is the official electronic badge given out at WHY2025, the Dutch outdoor hacker camp held in 2025. Built by the volunteer Team:Badge, it centers on two ESP32 modules paired with an 868MHz LoRa radio, a 3.95" LCD (part number W395HDC001-A), and a built-in mechanical-feel keyboard made from a dome-switch layer over a silicone layer. The badge has dual USB-C ports (one for flashing, one for charging) and an M.2 accessory connector alongside SAO-header support for plugging in add-ons.

Over 3,500 units were produced; some attendees received their badges unassembled and put them together themselves at the camp's on-site BadgeTent, following instructions on the project wiki covering spacer sizes and front-panel assembly. The badge runs a custom operating system called BadgeVMS and can load third-party apps distributed through BadgeHub (badge.why2025.org). Demonstrated software includes a Meshtastic client over the onboard LoRa radio and, notably, a working Doom port shown running on the badge's screen. Hardware and firmware live in a GitLab repository maintained by Team:Badge, and the community has since published 3D-printable case designs on Printables and Thingiverse.
