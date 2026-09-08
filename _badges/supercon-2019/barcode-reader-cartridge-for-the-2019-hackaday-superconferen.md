---
title: Barcode Reader Cartridge for the 2019 Hackaday Superconference Badge
id: supercon-2019-barcode-reader-cartridge-for-the-2019-hackaday-superconferen
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2019
year: 2019
makers:
- name: Thomas Flummer
  url: https://github.com/flummer
summary: A cartridge for the 2019 Hackaday Superconference badge's cartridge slot that adds a GM65 barcode/QR scanner module, letting the badge read 1D and 2D codes off paper, badges, or phone screens.
functions: Reads 1D and 2D barcodes/QR codes (including off a phone or badge screen) via an onboard GM65 scanner module; carries an onboard SPI flash for self-contained cartridge configuration data.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
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
  open_source: 'yes'
  hardware_url: https://github.com/flummer/supercon2019-barcodecartridge
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/flummer/supercon2019-barcodecartridge
  url: https://github.com/flummer/supercon2019-barcodecartridge
  kind: repo
images:
- file: assets/images/badges/supercon-2019/barcode-reader-cartridge-for-the-2019-hackaday-superconferen/5c074b58ff.jpg
  source: "https://github.com/flummer/supercon2019-barcodecartridge"
  credit: "Thomas Flummer"
  caption: "Front and back render of the barcode reader cartridge PCB"
contact: {}
notes:
- A barcode-scanner cartridge for the 2019 Supercon badge's cartridge slot, by the same maker as the NFC cartridge. Found by the event-year sweep, task supercon-2019.
status: released
sources:
- kind: url
  url: https://github.com/flummer/supercon2019-barcodecartridge
  title: Barcode Reader Cartridge for the 2019 Hackaday Superconference Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2019); event read as ''supercon-2019''.'
- kind: url
  url: https://github.com/flummer/supercon2019-barcodecartridge
  title: flummer/supercon2019-barcodecartridge (GitHub repo)
  accessed: '2026-09-08'
  note: "Confirmed design intent (GM65 barcode module cartridge for the 2019 Supercon badge), KiCad source files, CC BY-SA 4.0 license, and the front/back render image."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own GitHub repo: it is a real, built cartridge (fits the unofficial Supercon badge cartridge template) carrying a GM65 barcode/QR module and a W25Q128 SPI flash chip, KiCad design files, released under CC BY-SA 4.0. No firmware repo, price, quantity made, or sale/distribution info was found, so those fields are left empty. Set type to accessory (cartridge, not a standalone badge or SAO) and tech.mcu to none since the board carries no microcontroller of its own, only the scanner module and flash. Confidence is medium: the repo confirms the hardware and its purpose but gives no evidence of it being sold, given away, or how many exist, so status is set to released (design published, buildable) rather than announced.'
last_modified_date: '2026-09-08'
---

Thomas Flummer, the maker behind the unofficial Hackaday Superconference 2019 badge ecosystem, designed this cartridge to plug into that badge's cartridge slot and add a GM65 barcode/QR scanner module. It can read both 1D and 2D codes, including codes shown on a phone or another badge's screen, and it carries an onboard W25Q128 SPI flash chip so a cartridge can hold its own configuration data.

The board is a companion piece to Flummer's NFC Cartridge for the same badge and follows the same unofficial cartridge template, connecting through a 2x20 pin angled male header. Design files (schematic, PCB, and project files) are KiCad format and are released under a CC BY-SA 4.0 license on GitHub; a later revision (v1.2) corrected pin-connection errors in the cartridge connector. No information was found about units built, price, or how (or whether) it was distributed at Supercon.

## Make your own

The KiCad hardware source is published at github.com/flummer/supercon2019-barcodecartridge under CC BY-SA 4.0, including the schematic, PCB layout, and a front/back render. No separate firmware repository was found.
