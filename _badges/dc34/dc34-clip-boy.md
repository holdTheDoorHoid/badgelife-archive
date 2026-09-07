---
title: Clip-Boy
id: dc34-dc34-clip-boy
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: niko / Coruscant Productions, LLC
  url: https://brycebadges.com
summary: Wrist-mounted unofficial DEF CON 34 badge built on an ESP32-S3 with a 2.8-inch capacitive touchscreen, running Wi-Fi and Bluetooth analysis tools derived from ESP32 Marauder, with 8 customizable LEDs, a time-of-flight sensor, stereo speakers, SD card, a 2200 mAh battery and an SAO 1.69bis connector.
functions: Wi-Fi and Bluetooth reconnaissance tools derived from ESP32 Marauder, a radiation-detector mode, a theremin, drone Remote-ID detection, a screensaver idle clock, 3D-code (QR/marker) scanning, 90+ unlockable in-device collectibles, and an ARG (alternate reality game) finale that unlocked phone codes. Ships in a passive, listen-only mode; an optional research firmware build with additional capabilities is available for authorized testing only.
look:
  colors: []
  shape: null
  themes:
  - post-apocalyptic
  - wearable
  - radio
  - security
tech:
  mcu: ESP32-S3
  leds:
    count: 8
    type: RGB
    note: 8 customizable addressable LEDs
  display: 2.8" 320x240 capacitive touchscreen (LVGL UI)
  connectivity:
  - wifi
  - bluetooth
  battery: LiPo 2200 mAh
  sao_version: v1.69bis
  inputs:
  - touch
  - capacitive
get_one:
  price: $125 (first run); $135 (second-run pre-order)
  price_usd: 125
  quantity: '188'
  availability: sold_out
  distribution:
  - purchase
  - preorder
  where: Sold directly by the maker via brycebadges.com (redirects to tropicsquirrel.github.io/shop) and listed on Uberflux; first run of 36 units on Uberflux sold out, a separate run of 152 units also shipped, and a second production run was later gauged for interest with pre-orders at $135 (deadline noted as September 13).
make_your_own:
  open_source: true
  hardware_url: https://github.com/SafeHazard/Clip-Boy
  firmware_url: https://github.com/SafeHazard/Clip-Boy
  eda_tool: null
  license: GPLv3
  notes: PCB Gerbers, bill of materials, STEP enclosure files, and firmware source are published in the GitHub repo. A browser-based Web Serial firmware flasher is hosted at flash.brycebadges.com, with optional firmware verification via minisign signatures against the GitHub repo.
links:
- label: uberflux.com/product/NIKO-CLIPPY
  url: https://uberflux.com/product/NIKO-CLIPPY
  kind: store
- label: github.com/SafeHazard/Clip-Boy
  url: https://github.com/SafeHazard/Clip-Boy
  kind: repo
- label: tropicsquirrel.github.io/shop
  url: https://tropicsquirrel.github.io/shop/
  kind: store
- label: brycebadges.com
  url: https://brycebadges.com
  kind: website
- label: flash.brycebadges.com
  url: https://flash.brycebadges.com/
  kind: website
- label: safehazard.github.io/Clip-Boy
  url: https://safehazard.github.io/Clip-Boy
  kind: website
images:
- file: assets/images/badges/dc34/dc34-clip-boy/c2142aa8bb.jpg
  source: https://uberflux.com/product/NIKO-CLIPPY
  credit: Coruscant Productions, LLC
  caption: Clip-Boy wrist-mounted badge product photo
- file: assets/images/badges/dc34/dc34-clip-boy/554231b975.jpg
  source: https://tropicsquirrel.github.io/shop/
  credit: Bryce / Coruscant Productions, LLC
  caption: Clip-Boy badge, Fallout-inspired hero image
contact: {}
notes:
- The badge's own promotional copy describes it as a "parody badge...Fallout-inspired, not affiliated with Bethesda or Valve."
status: released
sources:
- kind: url
  url: https://uberflux.com/product/NIKO-CLIPPY
  title: Clip-Boy
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/SafeHazard/Clip-Boy
  title: GitHub - SafeHazard/Clip-Boy
  accessed: '2026-09-07'
  note: 'Repo readme: hardware/firmware description, chip, license, and open-source file listing.'
- kind: url
  url: https://tropicsquirrel.github.io/shop/
  title: 'Clip-Boy: The Unofficial DEF CON 34 Electronic Badge — Pre-Order'
  accessed: '2026-09-07'
  note: 'Maker''s own storefront: identifies maker as Bryce (high school junior, San Antonio TX), unit counts, pricing, second-run pre-order details, and product photos.'
- kind: url
  url: https://safehazard.github.io/Clip-Boy
  title: Clip-Boy documentation
  accessed: '2026-09-07'
  note: Confirms hardware spec (display, sensor, LEDs, SAO connector), GPLv3 licensing, and second-run pre-order price.
- kind: url
  url: https://flash.brycebadges.com/
  title: Clip-Boy Flasher
  accessed: '2026-09-07'
  note: Confirms seller of record (Coruscant Productions LLC), firmware flashing modes, and parody/non-affiliation disclaimer.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker is publicly credited on the GitHub repo and the tropicsquirrel.github.io storefront as Bryce, a high-school student in San Antonio, TX, doing business as niko / Coruscant Productions, LLC (kept the sheet''s maker name as given, since sources do not contradict it — ''niko'' appears to be the storefront/legal handle). Unit counts differ slightly by source: Uberflux listed a run of 36 (sold out), while the maker''s own shop states 152 units shipped in the first run overall, with a second run later gauged for interest at $135/unit (pre-order deadline September 13, year not stated on that page but consistent with 2026). Could not confirm exact quantity across all sales channels combined, so get_one.quantity reflects the shop''s own total. Speaker/audio hardware and time-of-flight sensor model (VL53L5CX) confirmed by the repo; exact LED color/PCB colorway not confirmed by any source, so look.colors is left empty.'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/dc34-clip-boy.glb
  method: gerber
  source_file: Clip-Boy/hardware/Gerber_Motherboard.zip
  generated: '2026-09-07'
  bytes: 94616
  size_mm:
  - 30.2
  - 60.5
---

Clip-Boy is an unofficial, wrist-mounted electronic badge made for DEF CON 34 (Badge Life Village) by Bryce, a high-school junior from San Antonio, Texas, selling under the name niko / Coruscant Productions, LLC. Styled as a "digital wasteland survivor" prop in a Fallout-inspired parody (the maker is explicit that it is not affiliated with Bethesda or Valve), it runs on an ESP32-S3 with a 2.8-inch capacitive touchscreen LVGL interface, 8 customizable RGB LEDs, a VL53L5CX time-of-flight sensor, an SAO 1.69bis connector, stereo speakers, SD card storage, and a 2200 mAh battery.

Functionally, the badge bundles Wi-Fi and Bluetooth reconnaissance tools derived from ESP32 Marauder, a radiation-detector mode, a theremin, drone Remote-ID detection, 3D-code scanning, and over 90 unlockable in-device collectibles, capped off by an alternate-reality-game finale that unlocked phone codes after the event. It ships in a passive, listen-only mode by default, with an optional research firmware build available for authorized testing only.

The badge sold out its initial production (listed in a run of 36 on Uberflux, with the maker's own shop citing 152 units shipped total) at $125, and the maker later gauged interest in a second run with pre-orders at $135. Hardware and firmware are fully open source under GPLv3, with Gerbers, BOM, STEP enclosure files, and firmware published on GitHub (SafeHazard/Clip-Boy), and a browser-based Web Serial flasher hosted at flash.brycebadges.com for updating units in the field.

## Make your own

The GitHub repository (github.com/SafeHazard/Clip-Boy) publishes PCB Gerbers, a bill of materials, STEP files for the 3D-printed enclosure, and the full firmware source under GPLv3. Firmware can be applied to an assembled unit using the browser-based flasher at flash.brycebadges.com (Chrome/Edge/Opera on desktop, via Web Serial), which offers app-only, content/media, and full factory-reset flashing modes, plus optional minisign signature verification against the GitHub repo.
