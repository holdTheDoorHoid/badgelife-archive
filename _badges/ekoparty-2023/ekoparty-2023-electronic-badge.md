---
title: Ekoparty 2023 Electronic Badge
id: ekoparty-2023-ekoparty-2023-electronic-badge
layout: badge
parent: Ekoparty 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: ekoparty-2023
year: 2023
makers:
- name: Electronic Cats
  url: https://electroniccats.com/
summary: The official electronic badge for Ekoparty 2023, designed and open-sourced by Electronic Cats, built around a WCH CH32V208 RISC-V/BLE chip with an OLED display and addressable LEDs.
functions: Runs custom firmware examples that drive the onboard WS2812B LEDs, the OLED display, and Bluetooth Low Energy. The badge also has a removable, community-designable acrylic/PCB "mask" accessory that changes its look; the CH32V208 additionally exposes I2C, UART, SPI, and CAN on GPIO for hardware hacking.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - kit
tech:
  mcu: CH32V208CBU6 (WCH, RISC-V)
  leds:
    count: null
    type: WS2812B
    note: Addressable LEDs; exact count not stated in the source.
  display: OLED (SSD1306 driver, per firmware source)
  connectivity:
  - ble
  - i2c
  - uart
  battery: 3x AA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 500 (per third-party listing; not confirmed by the maker)
  availability: unknown
  distribution: []
  where: Distributed at Ekoparty 2023 (Buenos Aires); exact method (free with registration, village, etc.) not stated by the maker.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/ElectronicCats/badge-ekoparty2023/tree/main/hardware
  firmware_url: https://github.com/ElectronicCats/badge-ekoparty2023/tree/main/firmware
  eda_tool: KiCad
links:
- label: github.com/ElectronicCats/badge-ekoparty2023
  url: https://github.com/ElectronicCats/badge-ekoparty2023
  kind: repo
- label: Charla Badge con Electronic Cats - Ekoparty 2023 (YouTube)
  url: https://www.youtube.com/watch?v=oSCkR2gFtc8
  kind: video
- label: Ekoparty badge series overview (badge.gallery, third-party)
  url: https://badge.gallery/series/ekoparty
  kind: article
images: []
contact: {}
notes:
- Ekoparty's first limited electronic conference badge, open-hardware design by Electronic Cats. Found by the event-year sweep, task con-ekoparty.
- The maker's own README calls it "EKO Badge 2023" / "EKOBadge"; kept the archive's existing title, which matches the naming style used for the site's other Ekoparty badge entries.
status: released
sources:
- kind: url
  url: https://github.com/ElectronicCats/badge-ekoparty2023
  title: Ekoparty 2023 Electronic Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''Ekoparty 2023''.'
- kind: url
  url: https://github.com/ElectronicCats/badge-ekoparty2023
  title: ElectronicCats/badge-ekoparty2023 README
  accessed: '2026-09-08'
  note: 'Maker''s own README (Spanish): confirms CH32V208CBU6 RISC-V chip, BLE/I2C/UART/SPI/CAN, OLED, the removable "mask" accessory, CERN OHL v1.2 hardware license, and "Sept 2023" date. README only says generic "Baterias AA" (no count) and does not name GPL for firmware; those two points are confirmed separately (repo license API, BOM) below.'
- kind: url
  url: https://github.com/ElectronicCats/badge-ekoparty2023/blob/main/hardware/ekoparty2023.csv
  title: badge-ekoparty2023 hardware BOM (ekoparty2023.csv)
  accessed: '2026-09-08'
  note: BOM line "J1, Battery, Ekoparty:BAT_12BH331P-GR" identifies the battery holder as Eagle Plastic Devices/EPD part 12BH331P-GR, which Mouser/Jotrin/JAK Electronics listings describe as a 3xAA PC-pin holder - corrects the entry from an unsupported "2x AA" to "3x AA". Repo folder listing (via gh api tree) also corroborates WS2812B and SSD1306 driver folders under firmware/ and a WS2812B footprint under hardware/Library, supporting the leds.type and display fields.
- kind: url
  url: https://api.github.com/repos/ElectronicCats/badge-ekoparty2023
  title: GitHub repo API record for badge-ekoparty2023
  accessed: '2026-09-08'
  note: Confirms repo-level license is GPL-3.0 (supports make_your_own.open_source firmware licensing, which the README text itself does not state).
- kind: url
  url: https://badge.gallery/series/ekoparty
  title: Ekoparty · Hacker Con Badges (badge.gallery)
  accessed: '2026-09-08'
  note: Third-party aggregator; states the 2023 badge was "capped at 500 units" and describes it as the first limited Ekoparty electronic badge. No photo of the 2023 unit shown on that page; not corroborated by the maker, so quantity is flagged as unconfirmed.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): corrected tech.battery and the body text from an unsupported "2x AA" to "3x AA" - the maker''s README only says generic "Baterias AA" with no count, but the maker''s own hardware BOM (hardware/ekoparty2023.csv) specifies battery holder part 12BH331P-GR, which independent distributor listings (Mouser, Jotrin, JAK Electronics) identify as a 3xAA PC-pin holder. Re-verified chip, BLE/I2C/UART/SPI/CAN, OLED/SSD1306, WS2812B LEDs (firmware folder names and a hardware/Library WS2812B footprint corroborate this), CERN OHL v1.2 hardware license (README) and GPL-3.0 firmware license (repo license API record), the "mask" accessory, KiCad tooling, and the YouTube talk title/link - all check out against the maker''s own repo. The badge.gallery "500 units" figure remains a third-party, unconfirmed claim (that page also calls it a "paid support option," which is new but does not contradict the entry''s blank price/availability fields, so left as-is). Could not find
    price, exact LED count, distribution method, or any photo of the assembled badge - the repo has no image files and no other coverage turned up in searches. With the battery correction made, everything remaining in the entry is now supported by a source that was actually read.'
last_modified_date: '2026-09-10'
model:
  file: assets/models/ekoparty-2023/ekoparty-2023-electronic-badge.glb
  method: kicad
  source_file: hardware/ekoparty2023.kicad_pcb
  generated: '2026-09-10'
  bytes: 383964
---

The Ekoparty 2023 Electronic Badge was Electronic Cats' first official electronic badge for Ekoparty, the large annual hacking conference in Buenos Aires, Argentina. It is built around a WCH CH32V208CBU6, a RISC-V microcontroller with built-in Bluetooth Low Energy, and pairs it with an OLED display and WS2812B addressable LEDs. The badge runs on three AA batteries and exposes I2C, UART, SPI, and CAN on its GPIO pins for anyone who wants to go beyond the stock firmware.

A distinctive feature is the badge's removable "mask" accessory: Electronic Cats released the mechanical design (with PCB thickness and mounting details) so attendees could design and fabricate their own custom mask to change the badge's look, using tools like KiCad, Inkscape, and svg2shenzhen/svg2mod to convert artwork into a mountable board. The hardware and firmware are both open source - hardware under the CERN Open Hardware Licence v1.2, firmware under GPL-3.0 - with example firmware provided for driving the LEDs, BLE, and OLED.

Beyond the maker's own repository, corroborating detail is thin: no assembled-badge photos, pricing, or an official distribution/quantity count from Electronic Cats or Ekoparty turned up in research. A third-party badge-tracking site puts the run at 500 units, but that figure is unconfirmed by the maker and is noted here only as a secondary claim.

## Make your own

The full KiCad hardware project and example firmware are published at [github.com/ElectronicCats/badge-ekoparty2023](https://github.com/ElectronicCats/badge-ekoparty2023): the `hardware/` folder holds the KiCad PCB/schematic/BOM for the badge itself (plus a separate `TopEkoparty` PCB project and a panel folder), and `firmware/` and `firmware_test/` hold example code showing how to control the LEDs, BLE, and OLED. The README also documents the CH32V208's datasheet, WCH's official SDK (openwch/ch32v20x), and the MounRiver IDE used to build for it, along with the recommended tools (KiCad, Inkscape, svg2shenzhen or svg2mod) for anyone designing a custom mask.
