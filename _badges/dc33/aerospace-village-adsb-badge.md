---
title: Aerospace Village ADSB Badge
id: dc33-aerospace-village-adsb-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Aerospace Village
  url: https://www.aerospacevillage.org/dc33-badge
  role: badge design and production
- name: Rare Circuits
  role: designed the DC33 companion SAO sold alongside the badge
summary: A wearable Linux single-board computer that natively receives and displays nearby aircraft via ADS-B at 1090 MHz, reusing the DC32 hardware with new DC33 software.
functions: ADS-B aircraft reception and mapping, Linux 6.6 SBC (SSH/keyboard access, custom scripting), video playback, and game emulation.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - hardware tool
tech:
  mcu: Allwinner T113 (dual-core Cortex-A7)
  leds: null
  display: SSD1306 OLED
  connectivity:
  - wifi
  - gps
  - usb
  - uart
  - i2c
  battery: Replaceable 18650, USB-C PD fast charging
  sao_version: null
get_one:
  price: $160
  price_usd: 160.0
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - village
  where: Sold directly by Aerospace Village at DEF CON 33; a $80 companion SAO (Rare Circuits), a $20 "Winnebago" SAO, and a $40 antenna kit were also offered, plus a $350 supporter bundle. As of research date the badge is listed as retired/out of stock on the Aerospace Village Tindie store.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/AerospaceVillage/avBadge_2024
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: The GitHub repo (avBadge_2024) hosts software releases (v1.1, v2.0) and documentation; it is not clear from what was checked whether full hardware design files (schematics/Gerbers) are published there.
links:
- label: github.com/AerospaceVillage/avBadge_2024
  url: https://github.com/AerospaceVillage/avBadge_2024
  kind: repo
- label: Aerospace Village - DC33 Badge
  url: https://www.aerospacevillage.org/dc33-badge
  kind: website
- label: 2024 Aerospace Village Badge (Tindie, retired)
  url: https://www.tindie.com/products/aero_village/2024-aerospace-village-badge/
  kind: store
- label: The Aerospace Village DC33 Badge (HamRadio.my writeup)
  url: https://hamradio.my/aerospace-village-dc33-badge/
  kind: article
images:
- file: assets/images/badges/dc33/aerospace-village-adsb-badge/00b32465cd.jpg
  source: https://www.aerospacevillage.org/dc33-badge
  credit: Aerospace Village
  caption: Front of the badge, showing the display and antenna
- file: assets/images/badges/dc33/aerospace-village-adsb-badge/7b00734163.jpg
  source: https://www.aerospacevillage.org/dc33-badge
  credit: Aerospace Village
  caption: Back of the badge, showing the battery compartment and connectors
- file: assets/images/badges/dc33/aerospace-village-adsb-badge/ebc1b86606.jpg
  source: https://www.aerospacevillage.org/dc33-badge
  credit: Aerospace Village
  caption: Front view of the DC33 badge
- file: assets/images/badges/dc33/aerospace-village-adsb-badge/21308784a5.jpg
  source: https://www.aerospacevillage.org/dc33-badge
  credit: Rare Circuits / Aerospace Village
  caption: DC33 SAO with OLED display and antenna jacks
- file: assets/images/badges/dc33/aerospace-village-adsb-badge/e5717a9a23.jpg
  source: https://www.aerospacevillage.org/dc33-badge
  credit: Aerospace Village / Rare Circuits
  caption: Front of the DC33 SAO, showing the RARE CIRCUITS logo
- file: assets/images/badges/dc33/aerospace-village-adsb-badge/fc0b46eedc.jpg
  source: https://www.aerospacevillage.org/dc33-badge
  credit: Aerospace Village / Rare Circuits
  caption: Back of the DC33 SAO circuit board
contact:
  emails:
  - hcadam@proton.me
notes:
- Sheet row only listed "Aerospace Village" as an expected maker for DC33, with no other detail; this entry was filled in from the maker's own DC33 badge page and press coverage.
status: released
sources:
- kind: sheet
  event: dc33
  row: 25
  updated: 7/14/2025 15:02:56
- kind: url
  url: https://www.aerospacevillage.org/dc33-badge
  title: DC33 Badge | Aerospace Village
  accessed: '2026-09-06'
  note: Maker, price tiers, distribution, SAO collaboration, and badge photos.
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2024
  title: GitHub - AerospaceVillage/avBadge_2024
  accessed: '2026-09-06'
  note: Confirms hardware spec (dual-core, 128MB DDR3, 8GB eMMC), software releases, SAO connector (I2C/UART/CAN).
- kind: url
  url: https://hamradio.my/aerospace-village-dc33-badge/
  title: 'The Aerospace Village DC33 Badge: A Linux SDR That Tracks Aircraft in Real Time'
  accessed: '2026-09-06'
  note: Describes the DC33 badge as DC32 hardware with new software, and the Rare Circuits SAO's air-band/FM/OLED features.
- kind: url
  url: https://www.tindie.com/products/aero_village/2024-aerospace-village-badge/
  title: 2024 Aerospace Village Badge
  accessed: '2026-09-06'
  note: Confirms the badge is now listed as retired/out of stock; open-source claim and SAO connector spec.
- kind: sheet
  event: dc33
  row: 5
  tab: 2025 (expected makers)
  updated: ''
- kind: sheet
  event: dc33
  row: 26
  updated: 7/14/2025 15:05:45
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: The community sheet listed the maker as "Rare Circuits", but sources agree the badge itself was designed and produced by Aerospace Village; Rare Circuits designed a separate $80 companion SAO for DC33 (air-band/FM radio receiver with a 4-color grayscale OLED). Both makers are recorded above. This is the same badge hardware as dc32-aerospace-village-unnamed-badge-sao (same $160 price, reused DC32 hardware with new DC33 firmware) -- see duplicate_of in the research report. Exact LED count/type, quantity produced, and full hardware open-source files (Gerbers/BOM/EDA tool) were not confirmed from the sources checked and are left empty. Merged with duplicate entry 'Aerospace Village DC33 Badge' (dc33-aerospace-village-listed-for-def-con-33-no-details). Merged with duplicate entry 'DC33 SAO' (dc33-coming-soon).
last_modified_date: '2026-09-06'
redirect_from:
- /badges/dc33/aerospace-village-listed-for-def-con-33-no-details/
- /badges/dc33/coming-soon/
related:
- dc32-aerospace-village-unnamed-badge-sao
---

The DC33 Aerospace Village badge is a wearable Linux computer built around an Allwinner T113 dual-core SoC, with 128MB of DDR3 RAM and 8GB of eMMC storage, that natively receives ADS-B aircraft transponder signals at 1090 MHz through an onboard PCB antenna (with a connector for an external one) and plots nearby aircraft on its SSD1306 OLED screen. Beyond ADS-B tracking it functions as a general-purpose Linux single-board computer accessible over SSH or a plugged-in keyboard, with built-in Wi-Fi, GPS, a USB-C dual-role port with Power Delivery charging, a microSD slot, and a replaceable 18650 battery. It carries an SAO connector that exposes I2C, UART, and CAN bus.

This is the same hardware Aerospace Village first sold for DC32 in 2024, brought back for DC33 in 2025 with updated software (releases v1.1 and v2.0 on the group's GitHub). Alongside the badge, Rare Circuits designed a dedicated $80 companion SAO for DC33 that adds air-band VHF and stereo FM radio reception (through a 3.5mm jack) and its own high-speed 4-color grayscale OLED display; a $20 "Winnebago" SAO and a $40 antenna kit were also sold, along with a $350 bundle. Aerospace Village sold the badge directly at DEF CON in limited batches announced over social media; it is now listed as retired and out of stock on the group's Tindie storefront.

## Make your own

Aerospace Village publishes badge software (not confirmed to include full hardware design files) at [github.com/AerospaceVillage/avBadge_2024](https://github.com/AerospaceVillage/avBadge_2024), including v1.1 and v2.0 releases and setup documentation.

## Notes merged from the duplicate entry "Aerospace Village DC33 Badge"

Aerospace Village listed only its own name as an expected DC33 maker on the community sheet, with no other details. Its actual DC33 offering, found via the village's own site and press coverage, was the same ADS-B badge line it first sold for DC32 in 2024: a wearable Linux single-board computer that natively receives 1090 MHz ADS-B aircraft transponder signals through an onboard PCB antenna and plots them on a moving map, alongside general Linux SBC functions (SSH/keyboard access, video playback, game emulation). It carries built-in Wi-Fi and GPS, a USB-C dual-role port with Power Delivery charging, a microSD slot, a replaceable 18650 battery, and an SAO connector exposing I2C, UART, and CAN bus.

For DC33 the hardware was reused from DC32 with updated software. Aerospace Village sold the $160 badge directly at DEF CON, alongside an $80 companion SAO designed by Rare Circuits (air-band VHF and stereo FM radio reception with its own OLED display), a $20 "Winnebago" SAO, a $40 antenna kit, and a $350 supporter bundle.

This entry duplicates `dc33-aerospace-village-adsb-badge`, a separate community-sheet row for the same badge that credits "Rare Circuits" as maker; that entry has more complete technical detail from further research.

## Notes merged from the duplicate entry "DC33 SAO"

Rare Circuits designed the DC33 SAO as an $80 companion add-on for Aerospace Village's DC33 ADS-B badge, sold alongside it (and the village's other DEF CON 33 offerings) at DEF CON 33 in 2025. Rather than duplicating the badge's ADS-B reception, the SAO adds a separate set of radio features: it can receive and play air-band VHF audio (the frequencies used for air traffic control and pilot communications) through an onboard 3.5mm jack, tune in stereo broadcast FM radio, and pick up at least one other radio service that Aerospace Village's own product page declined to specify in detail ahead of the con. It also carries its own SSD1306 OLED, driven fast enough (60+ FPS) to show a 4-color grayscale image using a technique the maker likewise left undocumented on the announcement page.

Because it is designed to plug into the DC33 badge, it draws power from that host rather than carrying its own battery or MCU description from the sources checked. Aerospace Village's site is also the only place that explains it was a genuine collaboration between Rare Circuits and the village, distinct from the badge itself, which the village designed and produced on its own DC32-era hardware.
