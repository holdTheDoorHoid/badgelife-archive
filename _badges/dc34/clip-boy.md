---
title: Clip-Boy
id: dc34-clip-boy
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: Coruscant Productions, LLC
  url: https://tropicsquirrel.github.io/shop/
summary: A Fallout-parody wrist-mounted badge with an ESP32-S3, a touchscreen, and built-in Wi-Fi/Bluetooth recon tools, designed and built by a teenage maker (Bryce) as a follow-up to his DC33 Space Badge.
functions: Wrist-mounted, wasteland-inspired electronic badge with WiFi + Bluetooth research tools, 3D code scanner, 90+ collectibles, a theremin, on-badge puzzles and loads of awful jokes, puns, in-references and fan service. Also, a (very specific type of) radiation detector. Made by the same teen who did Space Badge for DC33. Proceeds support Bryce's college fund!
look:
  colors:
  - grey
  shape: null
  themes:
  - retro computer
  - sci-fi
  - puzzle
  - security
  - radio
  form_factor: wearable
tech:
  mcu: ESP32-S3
  leds:
    count: null
    type: RGB
    note: Addressable RGB lighting, customizable colors; feeds a built-in theremin light show.
  display: 2.8" LVGL touchscreen (ESP32-S3-Touch-LCD-2.8)
  connectivity:
  - wifi
  - bluetooth
  inputs:
  - touch
  battery: LiPo 2200 mAh
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: $120 (first run; sold out)
  price_usd: 120.0
  quantity: 152 units (first run)
  availability: sold_out
  availability_note: 'Checked 2026-09-06: maker''s shop page says the first run sold out (152 shipped); a second run is in a demand-gauging/pre-order phase with no price set yet, and the page states pre-orders close permanently with no restock.'
  distribution:
  - purchase
  - preorder
  where: Sold directly by the maker via clip.brycebadges.com (redirects to the Coruscant Productions shop page); optional add-ons included a $10 custom trim color and a $15 "Omni-Tag" physical scan tag.
make_your_own:
  open_source: true
  hardware_url: https://github.com/SafeHazard/Clip-Boy
  firmware_url: https://github.com/SafeHazard/Clip-Boy
  gerbers_url: https://github.com/SafeHazard/Clip-Boy
  bom_url: https://github.com/SafeHazard/Clip-Boy
  eda_tool: EasyEDA
  license: GPLv3 (MIT available for builds without the audio tools)
  fab_url: null
  notes: Repo includes BOM, EasyEDA PCB source, Gerbers, 3D-printable enclosure models, and firmware; a browser-based flasher lives at flash.brycebadges.com. Commits are under GitHub user tropicsquirrel (Bryce's father, who hosts the toolchain); the maker's page attributes the actual design/build work, with AI assistance, to Bryce.
links:
- label: clip.brycebadges.com
  url: https://clip.brycebadges.com
  kind: store
- label: flash.brycebadges.com
  url: https://flash.brycebadges.com/
  kind: repo
- label: www.youtube.com/watch?v=mVFxb8wNfNw
  url: https://www.youtube.com/watch?v=mVFxb8wNfNw
  kind: video
- label: github.com/SafeHazard/Clip-Boy
  url: https://github.com/SafeHazard/Clip-Boy
  kind: repo
- label: safehazard.github.io/Clip-Boy
  url: https://safehazard.github.io/Clip-Boy/
  kind: doc
- label: uberflux.com/product/NIKO-CLIPPY
  url: https://uberflux.com/product/NIKO-CLIPPY
  kind: store
- label: tropicsquirrel.github.io/shop
  url: https://tropicsquirrel.github.io/shop/
  kind: store
  archived: https://web.archive.org/web/20260829171455/https://tropicsquirrel.github.io/shop/
- label: brycebadges.com
  url: https://brycebadges.com
  kind: website
images:
- file: assets/images/badges/dc34/clip-boy/554231b975.jpg
  source: https://tropicsquirrel.github.io/shop/
  credit: Coruscant Productions, LLC
  caption: Clip-Boy Mk2 emerging from a vault door, hero shot
  archived: https://web.archive.org/web/20260829171455/https://tropicsquirrel.github.io/shop/
- file: assets/images/badges/dc34/clip-boy/c2142aa8bb.jpg
  source: https://uberflux.com/product/NIKO-CLIPPY
  credit: Coruscant Productions, LLC
  caption: Clip-Boy wrist-mounted badge product photo
- file: assets/images/badges/dc34/clip-boy/554231b975.jpg
  source: https://tropicsquirrel.github.io/shop/
  credit: Bryce / Coruscant Productions, LLC
  caption: Clip-Boy badge, Fallout-inspired hero image
  archived: https://web.archive.org/web/20260829171455/https://tropicsquirrel.github.io/shop/
contact:
  discord: n/a
  emails:
  - coruscantproductions@gmail.com
  raw:
  - defcon.social/@clipboy
notes:
- The badge's own promotional copy describes it as a "parody badge...Fallout-inspired, not affiliated with Bethesda or Valve."
status: released
sources:
- kind: sheet
  event: dc34
  row: 26
  updated: 6/26/2026 15:46:45
  listing: New
- kind: url
  url: https://tropicsquirrel.github.io/shop/?utm_source=badgelife
  title: Clip-Boy Mk2 shop page (Coruscant Productions)
  accessed: '2026-09-06'
  note: Maker's own storefront; confirms name (Clip-Boy Mk2), maker (Bryce, Coruscant Productions, LLC), first-run sellout at 152 units, second-run demand-gauging status, gunmetal-gray 3D-printed shell, custom trim colors (+$10), Omni-Tag add-on (+$15).
- kind: url
  url: https://flash.brycebadges.com/
  title: Clip-Boy web-based firmware flasher
  accessed: '2026-09-06'
  note: Confirms GPLv3 firmware license, link to GitHub source, ESP32-S3-Touch-LCD-2.8 board reference, and minisign-verified release checksums.
- kind: url
  url: https://github.com/SafeHazard/Clip-Boy
  title: SafeHazard/Clip-Boy on GitHub
  accessed: '2026-09-06'
  note: Confirms ESP32-S3 MCU, 2.8" LVGL touchscreen, VL53L5CX time-of-flight sensor, addressable RGB, SAO v1.69bis header, GPLv3/MIT dual licensing, EasyEDA PCB source, Gerbers, BOM, and enclosure files; Wi-Fi/BT recon tools derived from ESP32 Marauder, a drone Remote-ID (ASTM F3411) detector, and an ARG-style unlock finale using HMAC-derived codes.
- kind: url
  url: https://uberflux.com/product/NIKO-CLIPPY
  title: Clip-Boy
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://tropicsquirrel.github.io/shop/
  title: 'Clip-Boy: The Unofficial DEF CON 34 Electronic Badge — Pre-Order'
  accessed: '2026-09-07'
  note: 'Maker''s own storefront: identifies maker as Bryce (high school junior, San Antonio TX), unit counts, pricing, second-run pre-order details, and product photos.'
  archived: https://web.archive.org/web/20260829171455/https://tropicsquirrel.github.io/shop/
- kind: url
  url: https://safehazard.github.io/Clip-Boy
  title: Clip-Boy documentation
  accessed: '2026-09-07'
  note: Confirms hardware spec (display, sensor, LEDs, SAO connector), GPLv3 licensing, and second-run pre-order price.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: Core facts (maker, MCU, display, sensor, SAO version, license, pricing, quantity, availability) are confirmed by the maker's own shop page, GitHub repo, and flasher site. Could not confirm exact LED count or battery/power spec from available pages. Could not load the YouTube video's description (page content was just YouTube boilerplate navigation), so it was not used as a source. A second lineup/colorway image was seen referenced on the shop page (id="poLineup") but its image URL is set by JavaScript and could not be resolved to a direct file, so only one image was saved. Merged with duplicate entry 'Clip-Boy' (dc34-dc34-clip-boy).
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc34/clip-boy.glb
  method: gerber
  source_file: Clip-Boy/hardware/Gerber_Motherboard.zip
  generated: '2026-09-07'
  bytes: 94616
  size_mm:
  - 30.2
  - 60.5
redirect_from:
- /badges/dc34/dc34-clip-boy/
---

Clip-Boy Mk2 is a wrist-mounted, Fallout-parody electronic badge built around an ESP32-S3 with a 2.8" LVGL touchscreen, a VL53L5CX time-of-flight sensor, addressable RGB lighting, and a SAO v1.69bis expansion header. It ships in a "passive/listen-only" mode with an optional research build that unlocks Wi-Fi and Bluetooth reconnaissance tools derived from ESP32 Marauder, plus a drone Remote-ID (ASTM F3411) detector. On top of the recon tooling it packs a theremin, over 90 unlockable collectibles, on-badge puzzles, and an ARG-style finale that unlocks using HMAC-derived codes — layered over dense Fallout in-jokes and puns.

It's a follow-up to Space Badge, which the same maker built for DEF CON 33. According to the maker's shop page, Bryce — a high-school junior from San Antonio, TX — designed and built the PCB, enclosure, and firmware (with AI assistance), selling the badge through his family's Coruscant Productions, LLC to fund his college savings. GitHub commits for the project appear under the account of his father (tropicsquirrel), who hosts the build toolchain.

The first run of 152 units, priced at $120 with a gunmetal-gray 3D-printed shell (custom trim colors +$10, an "Omni-Tag" physical scan-tag add-on +$15), sold out; as of this check a second run was in a demand-gauging/pre-order phase with pricing not yet announced, and the maker's page states that once pre-orders close there will be no restock.

## Make your own

The full project — BOM, EasyEDA PCB source, Gerbers, 3D-printable enclosure, and firmware — is published on GitHub under `SafeHazard/Clip-Boy`, licensed GPLv3 (an MIT-licensed build without the audio tools is also offered). A browser-based Web Serial flasher at flash.brycebadges.com can install official releases directly from Chrome, Edge, or Opera, with release authenticity independently verifiable via minisign against checksums hosted on GitHub.

## Notes merged from the duplicate entry "Clip-Boy"

Clip-Boy is an unofficial, wrist-mounted electronic badge made for DEF CON 34 (Badge Life Village) by Bryce, a high-school junior from San Antonio, Texas, selling under the name niko / Coruscant Productions, LLC. Styled as a "digital wasteland survivor" prop in a Fallout-inspired parody (the maker is explicit that it is not affiliated with Bethesda or Valve), it runs on an ESP32-S3 with a 2.8-inch capacitive touchscreen LVGL interface, 8 customizable RGB LEDs, a VL53L5CX time-of-flight sensor, an SAO 1.69bis connector, stereo speakers, SD card storage, and a 2200 mAh battery.

Functionally, the badge bundles Wi-Fi and Bluetooth reconnaissance tools derived from ESP32 Marauder, a radiation-detector mode, a theremin, drone Remote-ID detection, 3D-code scanning, and over 90 unlockable in-device collectibles, capped off by an alternate-reality-game finale that unlocked phone codes after the event. It ships in a passive, listen-only mode by default, with an optional research firmware build available for authorized testing only.

The badge sold out its initial production (listed in a run of 36 on Uberflux, with the maker's own shop citing 152 units shipped total) at $125, and the maker later gauged interest in a second run with pre-orders at $135. Hardware and firmware are fully open source under GPLv3, with Gerbers, BOM, STEP enclosure files, and firmware published on GitHub (SafeHazard/Clip-Boy), and a browser-based Web Serial flasher hosted at flash.brycebadges.com for updating units in the field.

## Make your own

The GitHub repository (github.com/SafeHazard/Clip-Boy) publishes PCB Gerbers, a bill of materials, STEP files for the 3D-printed enclosure, and the full firmware source under GPLv3. Firmware can be applied to an assembled unit using the browser-based flasher at flash.brycebadges.com (Chrome/Edge/Opera on desktop, via Web Serial), which offers app-only, content/media, and full factory-reset flashing modes, plus optional minisign signature verification against the GitHub repo.
