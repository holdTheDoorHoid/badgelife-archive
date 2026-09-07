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
- label: "The Aerospace Village DC33 Badge (HamRadio.my writeup)"
  url: https://hamradio.my/aerospace-village-dc33-badge/
  kind: article
images:
- file: assets/images/badges/dc33/aerospace-village-adsb-badge/00b32465cd.jpg
  source: "https://www.aerospacevillage.org/dc33-badge"
  credit: "Aerospace Village"
  caption: "Front of the badge, showing the display and antenna"
- file: assets/images/badges/dc33/aerospace-village-adsb-badge/7b00734163.jpg
  source: "https://www.aerospacevillage.org/dc33-badge"
  credit: "Aerospace Village"
  caption: "Back of the badge, showing the battery compartment and connectors"
contact:
  emails:
  - hcadam@proton.me
notes: []
status: released
sources:
- kind: sheet
  event: dc33
  row: 25
  updated: 7/14/2025 15:02:56
- kind: url
  url: https://www.aerospacevillage.org/dc33-badge
  title: "DC33 Badge | Aerospace Village"
  accessed: '2026-09-06'
  note: "Maker, price tiers, distribution, SAO collaboration, and badge photos."
- kind: url
  url: https://github.com/AerospaceVillage/avBadge_2024
  title: "GitHub - AerospaceVillage/avBadge_2024"
  accessed: '2026-09-06'
  note: "Confirms hardware spec (dual-core, 128MB DDR3, 8GB eMMC), software releases, SAO connector (I2C/UART/CAN)."
- kind: url
  url: https://hamradio.my/aerospace-village-dc33-badge/
  title: "The Aerospace Village DC33 Badge: A Linux SDR That Tracks Aircraft in Real Time"
  accessed: '2026-09-06'
  note: "Describes the DC33 badge as DC32 hardware with new software, and the Rare Circuits SAO's air-band/FM/OLED features."
- kind: url
  url: https://www.tindie.com/products/aero_village/2024-aerospace-village-badge/
  title: "2024 Aerospace Village Badge"
  accessed: '2026-09-06'
  note: "Confirms the badge is now listed as retired/out of stock; open-source claim and SAO connector spec."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    The community sheet listed the maker as "Rare Circuits", but sources agree the badge itself
    was designed and produced by Aerospace Village; Rare Circuits designed a separate $80 companion
    SAO for DC33 (air-band/FM radio receiver with a 4-color grayscale OLED). Both makers are recorded
    above. This is the same badge hardware as dc32-aerospace-village-unnamed-badge-sao (same $160
    price, reused DC32 hardware with new DC33 firmware) -- see duplicate_of in the research report.
    Exact LED count/type, quantity produced, and full hardware open-source files (Gerbers/BOM/EDA
    tool) were not confirmed from the sources checked and are left empty.
last_modified_date: '2026-09-06'
---

The DC33 Aerospace Village badge is a wearable Linux computer built around an Allwinner T113 dual-core SoC, with 128MB of DDR3 RAM and 8GB of eMMC storage, that natively receives ADS-B aircraft transponder signals at 1090 MHz through an onboard PCB antenna (with a connector for an external one) and plots nearby aircraft on its SSD1306 OLED screen. Beyond ADS-B tracking it functions as a general-purpose Linux single-board computer accessible over SSH or a plugged-in keyboard, with built-in Wi-Fi, GPS, a USB-C dual-role port with Power Delivery charging, a microSD slot, and a replaceable 18650 battery. It carries an SAO connector that exposes I2C, UART, and CAN bus.

This is the same hardware Aerospace Village first sold for DC32 in 2024, brought back for DC33 in 2025 with updated software (releases v1.1 and v2.0 on the group's GitHub). Alongside the badge, Rare Circuits designed a dedicated $80 companion SAO for DC33 that adds air-band VHF and stereo FM radio reception (through a 3.5mm jack) and its own high-speed 4-color grayscale OLED display; a $20 "Winnebago" SAO and a $40 antenna kit were also sold, along with a $350 bundle. Aerospace Village sold the badge directly at DEF CON in limited batches announced over social media; it is now listed as retired and out of stock on the group's Tindie storefront.

## Make your own

Aerospace Village publishes badge software (not confirmed to include full hardware design files) at [github.com/AerospaceVillage/avBadge_2024](https://github.com/AerospaceVillage/avBadge_2024), including v1.1 and v2.0 releases and setup documentation.
