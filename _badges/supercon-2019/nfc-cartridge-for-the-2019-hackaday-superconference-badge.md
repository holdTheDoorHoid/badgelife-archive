---
title: NFC Cartridge for the 2019 Hackaday Superconference Badge
id: supercon-2019-nfc-cartridge-for-the-2019-hackaday-superconference-badge
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
summary: An NFC-tag cartridge for the 2019 Hackaday Superconference badge, built on the unofficial cartridge template so it plugs into the badge's cartridge connector.
functions: Provides an NFC tag (readable over RF without being plugged in) and, when plugged into the badge, shares that same tag memory with the badge over I2C; an onboard SPI flash lets it carry its own badge firmware/configuration.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds: null
  display: null
  connectivity:
  - nfc
  - i2c
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/flummer/supercon2019-nfccartridge
  firmware_url: null
  eda_tool: KiCad
  license: CC BY-SA 4.0
  notes: Built on the unofficial Superconference 2019 badge cartridge template (https://github.com/flummer/supercon2019-cartridgetemplate).
links:
- label: github.com/flummer/supercon2019-nfccartridge
  url: https://github.com/flummer/supercon2019-nfccartridge
  kind: repo
images:
- file: assets/images/badges/supercon-2019/nfc-cartridge-for-the-2019-hackaday-superconference-badge/bb935a7096.jpg
  source: https://github.com/flummer/supercon2019-nfccartridge
  credit: Thomas Flummer
  caption: Front and back render of the NFC cartridge PCB
contact: {}
notes:
- An NFC-reader cartridge built on the unofficial Superconference 2019 badge cartridge template. Found by the event-year sweep, task supercon-2019.
- Sweep title matched the repo's own title exactly; no change needed.
status: released
sources:
- kind: url
  url: https://github.com/flummer/supercon2019-nfccartridge
  title: NFC Cartridge for the 2019 Hackaday Superconference Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2019); event read as ''supercon-2019''.'
- kind: url
  url: https://github.com/flummer/supercon2019-nfccartridge
  title: flummer/supercon2019-nfccartridge README
  accessed: '2026-09-08'
  note: Confirmed chip (ST25DV NFC + W25Q128 SPI flash), function, license (CC BY-SA 4.0), KiCad design files, and v1.2 pinout fix; source of the cartridge render image.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker's own GitHub repo confirms the design and license, but no storefront, price, or quantity-made information was found anywhere, so get_one fields are left empty. No separate maker bio/profile page was checked beyond the repo itself.
last_modified_date: '2026-09-10'
model:
  file: assets/models/supercon-2019/nfc-cartridge-for-the-2019-hackaday-superconference-badge.glb
  method: kicad
  source_file: NFCCartridge.kicad_pcb
  generated: '2026-09-10'
  bytes: 159480
---

This cartridge plugs into the unofficial cartridge connector on the 2019 Hackaday Superconference badge and adds an NFC tag built around an ST25DV chip. The tag can be read or written over RF even when the cartridge isn't plugged in, and the same ST25DV also exposes an I2C interface wired to the badge's connector, so the badge and an external NFC reader can share the same memory. A W25Q128 SPI flash chip on board lets the cartridge carry its own firmware and configuration data, making it self-contained rather than dependent on the badge's onboard storage.

The design is by Thomas Flummer, who also built the unofficial cartridge template it's based on, alongside a companion barcode-reader cartridge for the same badge. Version 1.2 of the board fixed a pinout error in the original release where two columns of the cartridge connector were swapped; boards built to the original layout can still be used by carefully rearranging pins on the header by hand. The project is open source under CC BY-SA 4.0, with KiCad schematic and PCB files published in the repository.

## Make your own

The GitHub repository (linked above) includes the KiCad schematic and PCB layout, the component footprints used, and rendered images of the board. No separate BOM or Gerber file bundle was found in the repo; anyone building one would need to export Gerbers themselves from the KiCad project.
