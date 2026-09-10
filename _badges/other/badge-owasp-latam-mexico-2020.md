---
title: badge-owasp-latam-mexico-2020
id: other-badge-owasp-latam-mexico-2020
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2020
makers:
- name: Electronic Cats
  url: https://github.com/ElectronicCats
summary: An ESP32-based conference badge Electronic Cats made for OWASP LATAM Mexico 2020 attendees, built around an onboard Capture The Flag challenge.
functions: Runs a Capture The Flag challenge that attendees access over Bluetooth; also has WS2812B mini addressable LEDs and an OLED display.
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
tech:
  mcu: ESP32
  leds:
    count: null
    type: WS2812B
    note: Described as "LED WS2812B Mini" in the repo README.
  display: 0.91" OLED 128x32 (I2C, SSD1306)
  connectivity:
  - wifi
  - ble
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of OWASP LATAM Mexico 2020.
make_your_own:
  open_source: true
  hardware_url: https://github.com/ElectronicCats/badge-owasp-latam-mexico-2020/tree/master/HW/Badge-OWASP-2020
  firmware_url: https://github.com/ElectronicCats/badge-owasp-latam-mexico-2020/tree/master/Firmware
  eda_tool: KiCad
  license: CERN Open Hardware Licence v1.2
links:
- label: github.com/ElectronicCats/badge-owasp-latam-mexico-2020
  url: https://github.com/ElectronicCats/badge-owasp-latam-mexico-2020
  kind: repo
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/ElectronicCats/badge-owasp-latam-mexico-2020
  title: badge-owasp-latam-mexico-2020
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''OWASP LATAM Mexico 2020''.'
- kind: url
  url: https://raw.githubusercontent.com/ElectronicCats/badge-owasp-latam-mexico-2020/master/README.md
  title: 'README: Badge OWASP LATAM México 2020'
  accessed: '2026-09-07'
  note: Confirms maker, event, MCU, LEDs, display options, CTF-over-Bluetooth concept, CERN OHL v1.2 licensing, and a "Dec 2019" credit line (design predates the 2020 event).
- kind: url
  url: https://api.github.com/repos/ElectronicCats/badge-owasp-latam-mexico-2020/contents/HW/Badge-OWASP-2020
  title: Repo contents, HW/Badge-OWASP-2020
  accessed: '2026-09-07'
  note: Confirms KiCad hardware files (schematic, PCB, libraries) are published in this folder; no photo of the assembled badge is present here. A vector art file (Badge_2020_OWASP.svg) exists separately at the repo root, not in this folder.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three cited sources (repo page, raw README, GitHub contents API) and confirmed every populated field and body sentence against them -- maker, ESP32 MCU, WS2812B mini LEDs, 0.91" 128x32 I2C/SSD1306 OLED (per the README''s own linked component options), wifi/ble/usb connectivity, Bluetooth-based CTF, CERN OHL v1.2 license, KiCad hardware files, and firmware (Firmware/test_LED_OLED/test_LED_OLED.ino) confirmed present, supporting open_source: yes. Corrected one inaccurate source note (the vector art SVG lives at the repo root, not inside the HW/Badge-OWASP-2020 folder as the note previously implied); no other changes needed. No matching "OWASP LATAM Mexico" event exists in _data/events.yml, so event is left as "other"; the con is OWASP LATAM Tour Mexico City, 2020. Price, quantity made, and LED count are still not stated anywhere in the repo, and no photo of the physical badge was found (repo has only KiCad source files and a vector artwork
    SVG, not photos), so images stays empty.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/badge-owasp-latam-mexico-2020.glb
  method: kicad
  source_file: HW/Badge-OWASP-2020/Badge-OWASP-2020.kicad_pcb
  generated: '2026-09-10'
  bytes: 203060
---

Electronic Cats built this ESP32-based badge for attendees of OWASP LATAM Mexico 2020, continuing their run of conference badges for the OWASP LATAM Tour. The badge pairs an ESP32 (with Wi-Fi and BLE) with a small OLED display, WS2812B mini addressable LEDs, and a USB-serial interface for programming.

The badge's centerpiece is a Capture The Flag challenge that attendees solve using a Bluetooth tool, turning the badge itself into the CTF target — fitting for a security-conference giveaway. Electronic Cats thanks PCBWay, LCSC, and Espressif in the README for supporting fabrication and components.

## Make your own

Hardware (KiCad schematic and PCB layout) and firmware are both published in the GitHub repository under the CERN Open Hardware Licence v1.2, so the design is fully open source. The hardware lives under `HW/Badge-OWASP-2020`, with firmware under `Firmware/`; a vector artwork file (`Badge_2020_OWASP.svg`) is also included for the badge's graphic design.
