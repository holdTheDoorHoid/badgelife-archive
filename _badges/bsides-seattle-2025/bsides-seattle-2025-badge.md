---
title: BSides Seattle 2025 badge
id: bsides-seattle-2025-bsides-seattle-2025-badge
layout: badge
parent: BSides Seattle 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-seattle-2025
year: 2025
makers:
- name: Electronic Cats
  url: https://electroniccats.com/
summary: The official electronic badge for BSides Seattle 2025, built around WiFi and BLE offensive tools plus a two-player Red-vs-Blue OWASP card game.
functions: 'WiFi: deauth, broadcast packets, rogue-AP cloning, AP combine attack, multi-AP creation, and captive portals (Google credential phish or WiFi password phish). BLE: AirTag/Tile tracker scanning and BLE device spam. Zigbee: IEEE 802.15.4 sniffer over a serial connection. A pairing-based two-player game where a Red team picks an OWASP-profile attack and a Blue team must pick the right mitigation; winning with all 10 OWASP profiles unlocks Jedi- or Sith-themed logo screens.'
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - pop culture
tech:
  mcu: ESP32-S3
  leds: null
  display: null
  connectivity:
  - wifi
  - ble
  - zigbee
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
  open_source: yes
  hardware_url: https://github.com/ElectronicCats/bsides-seattle-2025/tree/main/hardware
  firmware_url: https://github.com/ElectronicCats/bsides-seattle-2025/tree/main/firmware
  eda_tool: KiCad
links:
- label: github.com/ElectronicCats/bsides-seattle-2025
  url: https://github.com/ElectronicCats/bsides-seattle-2025
  kind: repo
images: []
contact: {}
notes:
- Official 2025 conference badge designed by Electronic Cats with WiFi deauth/rogue-AP, BLE tracker-scan/spam, and Zigbee sniffing features plus a Red-vs-Blue OWASP card game; hardware released under CERN OHL v1.2. Found by the event-year sweep, task bsides-las-vegas.
- The maker's repo does not state price, quantity, or availability; those fields are left unknown. No photo of the assembled badge was found (repo images are in-game logo/profile-map screenshots, not the physical board), so no images were saved.
status: listed
sources:
- kind: url
  url: https://github.com/ElectronicCats/bsides-seattle-2025
  title: BSides Seattle 2025 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-las-vegas); event read as ''BSides Seattle 2025''.'
- kind: url
  url: https://raw.githubusercontent.com/ElectronicCats/bsides-seattle-2025/main/README.md
  title: 'ElectronicCats/bsides-seattle-2025: README'
  accessed: '2026-09-10'
  note: Confirms maker, feature list (WiFi/BLE/Zigbee/game), and CERN OHL v1.2 hardware license.
- kind: url
  url: https://github.com/ElectronicCats/bsides-seattle-2025/tree/main/firmware
  title: firmware directory (sdkconfig.defaults.esp32s3)
  accessed: '2026-09-10'
  note: ESP-IDF sdkconfig defaults include an esp32s3-specific file, indicating the badge targets ESP32-S3.
- kind: url
  url: https://github.com/ElectronicCats/bsides-seattle-2025/tree/main/hardware
  title: hardware directory (KiCad project)
  accessed: '2026-09-10'
  note: Hardware is a KiCad project (.kicad_pcb/.kicad_sch), confirming open hardware and EDA tool.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Maker's own GitHub repo confirms the badge is real and describes its features in detail, so confidence is medium rather than low. Could not find price, quantity, availability, LED count/type, display, battery, SAO support, board color/shape, or any photo of the assembled physical badge from the maker or press; those fields are left empty/unknown. No storefront or press coverage was found beyond the repo itself.
last_modified_date: '2026-09-10'
---

The BSides Seattle 2025 badge is Electronic Cats' official electronic badge for the 2025 edition of BSides Seattle, built on an ESP32-S3 and released as open hardware (KiCad design files) under the CERN Open Hardware Licence v1.2, with open firmware under an ESP-IDF project.

Functionally it leans into offensive wireless tooling as its main hook: a WiFi menu with deauth, broadcast-packet flooding, rogue-AP cloning, a combined clone-plus-broadcast attack, multi-AP creation from scanned networks, and captive portals that request Google credentials or a WiFi password from a target; a BLE menu that scans for AirTag and Tile trackers and can spam BLE advertising packets toward Apple devices; and a Zigbee/IEEE 802.15.4 sniffer that streams captures over a serial connection to a computer.

Alongside the radio tools, the badge ships a two-player pairing game: a Red team player picks one of ten OWASP-based vulnerability profiles and an attack, and a Blue team player must choose the correct mitigation to win the round. Winning with all ten profiles unlocks cosmetic Jedi- and Sith-themed logo screens, with four rank tiers on each side (Padawan through Grand Master; Lord through Dark Lord).

No price, production quantity, availability, or storefront listing was found for this badge, and no photo of the assembled physical board turned up outside the repository's in-firmware game screenshots — only the GitHub source confirms the project's existence and design.
