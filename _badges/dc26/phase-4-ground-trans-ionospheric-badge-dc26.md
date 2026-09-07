---
title: Phase 4 Ground Trans-Ionospheric Badge (DC26)
id: dc26-phase-4-ground-trans-ionospheric-badge-dc26
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: Open Research Institute
  url: https://openresearch.institute/
- name: Phase 4 Ground
  url: https://github.com/phase4ground
summary: A hackable, wearable amateur-radio peripheral badge from Open Research Institute's Phase 4 Ground project, demonstrated at DEF CON 26. It pairs a Nordic nRF52 Bluetooth Low Energy MCU with a small color display and is fully open source, down to firmware and hardware design files.
functions: Bluetooth Low Energy connectivity to phone apps (nRF UART / nRF Connect), including a monitor mode with hidden easter eggs; user-customizable/reflashable firmware; drives a small color LCD.
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
tech:
  mcu: nRF52
  leds: null
  display: 1.45" color TFT LCD (128x128, Crystalfontz CFAF128128B-0145T)
  connectivity:
  - ble
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Given out / sold to attendees at DEF CON 26 (2018); a "for sale" poster was published by Open Research Institute.
make_your_own:
  open_source: true
  hardware_url: https://github.com/phase4ground/trans-ionospheric/tree/master/hardware
  firmware_url: https://github.com/phase4ground/trans-ionospheric/tree/master/firmware
  eda_tool: Altium
links:
- label: openresearch.institute/badge
  url: http://openresearch.institute/badge/
  kind: website
  archived: https://web.archive.org/web/20260410153707/https://www.openresearch.institute/badge/
- label: trans-ionospheric (GitHub repo)
  url: https://github.com/phase4ground/trans-ionospheric
  kind: repo
- label: 'Hackaday #badgelife DEFCON26 documentary segment'
  url: https://youtu.be/G2fHKRONc6U?t=12m22s
  kind: video
images:
- file: assets/images/badges/dc26/phase-4-ground-trans-ionospheric-badge-dc26/fe7d5d3b0d.jpg
  source: http://openresearch.institute/badge/
  credit: Open Research Institute
  caption: The Trans-Ionospheric badge at DEF CON 26
  archived: https://web.archive.org/web/20260410153707/https://www.openresearch.institute/badge/
- file: assets/images/badges/dc26/phase-4-ground-trans-ionospheric-badge-dc26/daa41d611c.jpg
  source: http://openresearch.institute/badge/
  credit: Open Research Institute
  caption: Trans-Ionospheric sale poster showing the badge
  archived: https://web.archive.org/web/20260410153707/https://www.openresearch.institute/badge/
contact: {}
notes:
- HAM radio peripheral badge
status: released
sources:
- kind: url
  url: http://openresearch.institute/badge/
  title: Phase 4 Ground Trans-Ionospheric Badge (DC26)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 26''.'
  archived: https://web.archive.org/web/20260410153707/https://www.openresearch.institute/badge/
- kind: url
  url: https://github.com/phase4ground/trans-ionospheric
  title: phase4ground/trans-ionospheric on GitHub
  accessed: '2026-09-07'
  note: Confirmed open hardware (Altium schematics/PCB) and open firmware (Apache 2.0); repo layout for firmware and hardware folders.
- kind: url
  url: https://raw.githubusercontent.com/phase4ground/trans-ionospheric/master/firmware/README.md
  title: trans-ionospheric firmware README
  accessed: '2026-09-07'
  note: MCU confirmed as Nordic nRF52 (Nordic SDK v12.3, openocd nrf52.cfg target); firmware based on the JoCo Cruise 2018 badge, itself based on AND!XOR's DEF CON 25 Bender Badge; Apache 2.0 license.
- kind: url
  url: https://api.github.com/repos/phase4ground/trans-ionospheric/contents/hardware/Datasheets
  title: trans-ionospheric hardware/Datasheets folder listing
  accessed: '2026-09-07'
  note: Display identified via bundled datasheet as a Crystalfontz CFAF128128B-0145T, a 1.45" 128x128 color TFT.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price, quantity made, and LED count/type were not stated on the maker page, GitHub repo, or firmware README; left empty rather than guessed. The maker's own page and GitHub repo agree on all other details, so no source conflicts.
last_modified_date: '2026-09-07'
---

The Trans-Ionospheric badge is a wearable amateur-radio peripheral built by [Open Research Institute](https://openresearch.institute/) for its Phase 4 Ground project, and was demonstrated at DEF CON 26 in Las Vegas in 2018. It runs on a Nordic nRF52 Bluetooth Low Energy microcontroller and drives a small 1.45" color TFT display, and it connects to a phone over BLE using the nRF UART or nRF Connect apps, including a monitor mode with hidden easter eggs.

The badge's firmware is fully open and reflashable by owners with an SWD programmer, and traces its lineage back through the unofficial JoCo Cruise 2018 "pirate monkey" badge to the AND!XOR team's DEF CON 25 Bender Badge. Open Research Institute published the complete firmware (Apache License 2.0) and hardware design (Altium schematics and PCB files) on GitHub, along with per-folder READMEs covering build and flashing steps, and encouraged attendees to file ideas or pull requests against the repository.

## Make your own

The [hardware](https://github.com/phase4ground/trans-ionospheric/tree/master/hardware) folder holds the Altium schematics (processor, power, LEDs) and PCB project files. The [firmware](https://github.com/phase4ground/trans-ionospheric/tree/master/firmware) folder holds the source and build scripts: install the Nordic nRF5 SDK v12.3 and a GNU ARM Embedded toolchain, set the `SDK_ROOT` environment variable, then run `make` in `firmware/src` followed by `./update.sh`. Flashing uses either `./provision.sh` or `make flash_softdevice && make flash` over an SWD interface (e.g. a Segger J-Link or ST-Link).
