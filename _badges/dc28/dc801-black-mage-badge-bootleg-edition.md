---
title: DC801 Black Mage Badge - "Bootleg Edition"
id: dc28-dc801-black-mage-badge-bootleg-edition
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
makers:
- name: redactd
  url: https://www.tindie.com/stores/redactd/
summary: A community-built reproduction of the DC801 Black Mage Badge, the open-source badge platform DC801 first released for DEF CON 28, done as a limited "after dark" run with a black FR4 core and clear solder mask over the standard design.
functions: Runs the open-source Black Mage Badge platform and its built-in game (a touchscreen adventure/puzzle title), with Bluetooth (including mesh) connectivity and SAO passthrough for other badges to plug into.
look:
  colors:
  - black
  - copper
  shape: null
  themes: []
  form_factor: pcb badge
tech:
  mcu: nRF52840
  leds:
    count: 19
    type: null
    note: 19 blue LEDs; button backlighting handled by a separate Microchip ATtiny1617 driving 27 buttons
  display: 2.4" 240x320 TFT LCD (touchscreen)
  connectivity:
  - ble
  - usb
  battery: null
  power: USB-C
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: $250
  price_usd: 250
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shows sold out; last unit sold August 2, 2026 per listing history (checked 2026-09-07)
  distribution:
  - purchase
  where: Sold directly by redactd through their Tindie store.
make_your_own:
  open_source: true
  hardware_url: https://github.com/DC801/BM-Badge
  firmware_url: https://github.com/DC801/BM-Badge
  eda_tool: KiCad
  license: AGPL-3.0
links:
- label: www.tindie.com/products/redactd/dc801-black-mage-badge-bootleg-edition
  url: https://www.tindie.com/products/redactd/dc801-black-mage-badge-bootleg-edition/
  kind: store
- label: DC801/BM-Badge on GitHub
  url: https://github.com/DC801/BM-Badge
  kind: repo
images:
- file: assets/images/badges/dc28/dc801-black-mage-badge-bootleg-edition/a920c62e5a.jpg
  source: https://www.tindie.com/products/redactd/dc801-black-mage-badge-bootleg-edition/
  credit: redactd
  caption: DC801 Black Mage Badge - Bootleg Edition, black FR4/clear solder mask build
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://www.tindie.com/products/redactd/dc801-black-mage-badge-bootleg-edition/
  title: DC801 Black Mage Badge - "Bootleg Edition"
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc28 (a reproduction, not tied to one specific con year)''.'
- kind: url
  url: https://www.tindie.com/products/redactd/dc801-black-mage-badge-bootleg-edition/
  title: DC801 Black Mage Badge - "Bootleg Edition" (product listing)
  accessed: '2026-09-07'
  note: Full listing text — maker, specs (nRF52840, 27 buttons via ATtiny1617, 19 blue LEDs, 2.4" 240x320 touchscreen TFT, USB-C UF2, SD card, SAO 1.69bis + Saintcon minibadge + DC801 ART front board headers), price $250, out of stock since 2022-08-02.
- kind: url
  url: https://github.com/DC801/BM-Badge
  title: 'DC801/BM-Badge: The DC801 Badge Platform for DC28+'
  accessed: '2026-09-07'
  note: Confirms this is a reproduction of DC801's official DC28 badge platform; open source, AGPL-3.0, hardware in KiCad.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This is an unofficial third-party reproduction ("bootleg") of the official DC801 Black Mage Badge, which DC801 designed and released for DEF CON 28; the underlying hardware/firmware repo is DC801's own, not redactd's. It is unclear whether redactd published separate design files for their bootleg variant specifically, or exactly how many units they made — the Tindie listing does not say. Product photos on the listing are dated mid-2022, well after DC28 (2020), consistent with this being a later independent run rather than an original-batch badge.
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc28/dc801-black-mage-badge-bootleg-edition.glb
  method: kicad
  source_file: Hardware/BackBoard/purplewizard.kicad_pcb
  generated: '2026-09-07'
  bytes: 840184
---

The DC801 Black Mage Badge began as DC801's official electronic badge platform for DEF CON 28: an open-source, KiCad-designed board built around a Nordic nRF52840, with a 2.4" touchscreen TFT, 27 tactile buttons, Bluetooth (including mesh), and a built-in adventure game. Because the hardware and firmware were released publicly under AGPL-3.0, other makers were free to build their own copies, and this listing is one of them.

redactd, selling through Tindie, produced a limited "after dark" run of the badge using a black FR4 core with clear solder mask, which leaves the copper traces and pads visible through the board rather than hiding them under conventional silkscreen — giving the badge a different look from the original run while keeping the same electronics: the nRF52840 MCU, 19 blue LEDs, ATtiny1617-driven button matrix, USB-C with drag-and-drop UF2 firmware updates, an SD card slot, and header support for SAO 1.69bis, Saintcon minibadges, and DC801's own ART front-board add-ons.

The listing priced the badge at $250 and shows it sold out as of August 2022; the listing does not state how many units redactd made.
