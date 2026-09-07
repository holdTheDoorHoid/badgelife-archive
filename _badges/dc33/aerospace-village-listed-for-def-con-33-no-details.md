---
title: Aerospace Village DC33 Badge
id: dc33-aerospace-village-listed-for-def-con-33-no-details
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
summary: A wearable Linux single-board computer that natively receives and displays nearby aircraft via ADS-B at 1090 MHz, reusing the DC32 hardware with new DC33 software.
functions: ADS-B aircraft reception and moving-map display, Linux single-board computer (SSH/keyboard accessible), video playback, and game emulation.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - hardware tool
tech:
  mcu: null
  leds: null
  display: null
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
  availability: unknown
  distribution:
  - purchase
  - village
  where: Sold directly by Aerospace Village at DEF CON 33; an $80 companion SAO by Rare Circuits, a $20 "Winnebago" SAO, and a $40 antenna kit were also offered, plus a $350 supporter bundle.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/AerospaceVillage/avBadge_2024
  eda_tool: null
links:
- label: Aerospace Village - DC33 Badge
  url: https://www.aerospacevillage.org/dc33-badge
  kind: website
- label: github.com/AerospaceVillage/avBadge_2024
  url: https://github.com/AerospaceVillage/avBadge_2024
  kind: repo
- label: "The Aerospace Village DC33 Badge (HamRadio.my writeup)"
  url: https://hamradio.my/aerospace-village-dc33-badge/
  kind: article
images:
- file: assets/images/badges/dc33/aerospace-village-listed-for-def-con-33-no-details/ebc1b86606.jpg
  source: "https://www.aerospacevillage.org/dc33-badge"
  credit: "Aerospace Village"
  caption: "Front view of the DC33 badge"
- file: assets/images/badges/dc33/aerospace-village-listed-for-def-con-33-no-details/21308784a5.jpg
  source: "https://www.aerospacevillage.org/dc33-badge"
  credit: "Rare Circuits / Aerospace Village"
  caption: "DC33 SAO with OLED display and antenna jacks"
contact: {}
notes:
- Sheet row only listed "Aerospace Village" as an expected maker for DC33, with no other detail; this entry was filled in from the maker's own DC33 badge page and press coverage.
status: released
sources:
- kind: sheet
  event: dc33
  row: 5
  tab: 2025 (expected makers)
  updated: ''
- kind: url
  url: https://www.aerospacevillage.org/dc33-badge
  title: "DC33 Badge | Aerospace Village"
  accessed: '2026-09-06'
  note: Primary source for badge description, price tiers, SAO/accessory lineup, and photos.
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2024
  title: "GitHub - AerospaceVillage/avBadge_2024"
  accessed: '2026-09-06'
  note: Confirms hardware/software repo and that DC33 reused DC32 hardware with new firmware.
- kind: url
  url: https://hamradio.my/aerospace-village-dc33-badge/
  title: "The Aerospace Village DC33 Badge: A Linux SDR That Tracks Aircraft in Real Time"
  accessed: '2026-09-06'
  note: Describes the DC33 badge as DC32 hardware with new software, and the Rare Circuits SAO's features.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    This sheet row only named "Aerospace Village" as an expected DC33 maker with no other detail.
    Research found the item: the same DC33 ADS-B badge covered by dc33-aerospace-village-adsb-badge
    (that entry lists maker "Rare Circuits" and price $160 from a separate sheet row). This entry is
    a duplicate of that one -- see duplicate_of in the research report. Exact MCU model, LED
    count/type, display size, quantity produced, and full hardware open-source files were not
    confirmed from the sources checked and are left empty here (the sibling entry has since filled
    in some of these from further research).
last_modified_date: '2026-09-06'
---

Aerospace Village listed only its own name as an expected DC33 maker on the community sheet, with no other details. Its actual DC33 offering, found via the village's own site and press coverage, was the same ADS-B badge line it first sold for DC32 in 2024: a wearable Linux single-board computer that natively receives 1090 MHz ADS-B aircraft transponder signals through an onboard PCB antenna and plots them on a moving map, alongside general Linux SBC functions (SSH/keyboard access, video playback, game emulation). It carries built-in Wi-Fi and GPS, a USB-C dual-role port with Power Delivery charging, a microSD slot, a replaceable 18650 battery, and an SAO connector exposing I2C, UART, and CAN bus.

For DC33 the hardware was reused from DC32 with updated software. Aerospace Village sold the $160 badge directly at DEF CON, alongside an $80 companion SAO designed by Rare Circuits (air-band VHF and stereo FM radio reception with its own OLED display), a $20 "Winnebago" SAO, a $40 antenna kit, and a $350 supporter bundle.

This entry duplicates `dc33-aerospace-village-adsb-badge`, a separate community-sheet row for the same badge that credits "Rare Circuits" as maker; that entry has more complete technical detail from further research.
