---
title: DC SDR badge
id: dc31-dc-sdr-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc31
year: 2023
makers:
- name: Alexandre Rouma
  url: https://github.com/AlexandreRouma
summary: 'A self-contained SDR (software-defined radio) receiver built as a DEF CON badge add-on, with an RTL-SDR-style R820T tuner, RP2040 microcontroller, and audio output, designed by SDR++ author Alexandre Rouma for DEF CON 31.'
functions: 'Standalone SDR receiver: tunes and demodulates radio signals using an R820T tuner front-end, decodes/processes on an onboard RP2040, and outputs audio via a 3.5mm jack (through a TLV320DAC3203 codec) or shows status on a small OLED display.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
tech:
  mcu: RP2040
  leds:
    count: 8
    type: WS2812B
    note: ''
  display: OLED
  connectivity:
  - usb
  - audio
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
  open_source: partial
  hardware_url: https://github.com/AlexandreRouma/dc_sdr
  firmware_url: https://github.com/AlexandreRouma/dc_sdr
  eda_tool: KiCad
links:
- label: github.com/AlexandreRouma/dc_sdr
  url: https://github.com/AlexandreRouma/dc_sdr
  kind: repo
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: unknown
sources:
- kind: url
  url: https://github.com/AlexandreRouma/dc_sdr
  title: DC SDR badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/AlexandreRouma/dc_sdr
  title: 'AlexandreRouma/dc_sdr: My SDR badge insert for defcon'
  accessed: '2026-09-07'
  note: 'GitHub repo description ("My SDR badge insert for defcon"), file listing (KiCad source, gerbers, firmware.uf2, license marked NOT for commercial purposes), and README warning that firmware is unfinished and hardware not fully tested.'
- kind: url
  url: https://api.github.com/repos/AlexandreRouma/dc_sdr
  title: dc_sdr repository metadata
  accessed: '2026-09-07'
  note: Repo description and creation/push dates confirming this was made for DEF CON (commits July-August 2023, i.e. DEF CON 31).
- kind: url
  url: https://raw.githubusercontent.com/AlexandreRouma/dc_sdr/master/dc_sdr.csv
  title: dc_sdr bill of materials (dc_sdr.csv)
  accessed: '2026-09-07'
  note: 'BOM confirming RP2040 MCU, R820T RF tuner, BGA2817 LNA, TLV320DAC3203 audio codec, W25Q16 flash, USB-C and 3.5mm audio jacks, and 8x WS2812B LEDs.'
- kind: url
  url: https://github.com/AlexandreRouma
  title: AlexandreRouma (GitHub profile)
  accessed: '2026-09-07'
  note: 'Maker identity check: Alexandre Rouma, PhD student at NC State, founder of Dragon Labs, better known as the author of the SDR++ software; no separate Hackaday.io project page found for this badge.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    This is a personal, DIY project repo rather than a sold product: no store listing,
    price, production quantity, or public release/distribution info was found, so
    those fields are left empty. The README itself says the firmware is unfinished
    and the hardware not fully tested, and the repo has no tagged releases, so it's
    unclear whether any units were ever built beyond the designer's own. The repo
    was created in July 2023 with the last commit in August 2023, and its GitHub
    description reads "My SDR badge insert for defcon" - taken together with those
    dates this points to DEF CON 31 (2023), so event was corrected from 'other' to
    'dc31'. Display tech is inferred from folder names in the repo (oled, lcd0_model,
    lcd1_model - suggesting multiple display options were evaluated) and a display
    footprint labeled "ADA4520" in the BOM, which was not independently confirmed as
    an exact panel model. No sao_version/header count is stated, so it is left null;
    despite the repo calling itself a "badge insert" it is being catalogued as an SAO
    since no host badge of its own is described. No photos of the assembled item were
    found - the repo contains only KiCad source, gerbers, a STEP/FreeCAD 3D model, and
    firmware, no product photography.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/dc-sdr-badge/
---

Alexandre Rouma - the developer better known for the SDR++ software-defined radio application - built this as a personal add-on for DEF CON 31 (2023): a self-contained SDR receiver on a small PCB rather than a passive SAO. The board pairs an RP2040 microcontroller with an R820T tuner and BGA2817 low-noise amplifier (the same class of RF front end used in RTL-SDR dongles), a TLV320DAC3203 audio codec feeding a 3.5mm headphone jack, USB-C for power and firmware updates, onboard SPI flash, and eight WS2812B RGB LEDs. The repository's file layout (separate oled, lcd0_model, and lcd1_model directories) suggests more than one small display was tried during development.

The GitHub repo publishes the full KiCad design (schematic, PCB, BOM, gerbers), a 3D mechanical model, and a compiled firmware.uf2, but its own README warns that the firmware is unfinished and the hardware not fully tested, and the license explicitly restricts the files to non-commercial use. No storefront, announcement post, price, or production-quantity information was found, so it reads as a one-off (or very small run) personal build rather than a badge sold or distributed at the con.

## Make your own

The repository (github.com/AlexandreRouma/dc_sdr) contains everything needed to reproduce the board: KiCad schematic and PCB files, a component BOM (dc_sdr.csv), a gerbers.zip for fabrication, a FreeCAD full-assembly model, and a firmware.uf2 for the RP2040. The maker cautions that both the firmware and hardware were incomplete/untested as of the last commit, so anyone building it should treat it as an in-progress design.
