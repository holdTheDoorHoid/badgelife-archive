---
title: Ultra Tiny Smart SAO
id: supercon-2024-ultra-tiny-smart-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Alex
  url: https://hackaday.io/tinyledmatrix
summary: 'A deliberately miniaturized "smart" SAO, built to be smaller than the SAO header it plugs into, entered in Supercon 8''s SAO Contest.'
functions: 'Blinks a tiny RGB LED and talks I2C to the host badge; no other stated functions.'
look:
  colors: []
  shape: null
  themes:
  - minimalist
tech:
  mcu: ATtiny20-UU (BGA)
  leds:
    count: 1
    type: discrete
    note: tiny discrete RGB LED, not a standard single-package LED
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: 'Entered in the Supercon 8 SAO Contest; no storefront found.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/197899-ultra-tiny-smart-sao
  url: https://hackaday.io/project/197899-ultra-tiny-smart-sao
  kind: hackaday
- label: Alex (tinyledmatrix) on Hackaday.io
  url: https://hackaday.io/tinyledmatrix
  kind: social
images:
- file: assets/images/badges/supercon-2024/ultra-tiny-smart-sao/1777bd7677.jpg
  source: "https://hackaday.io/project/197899-ultra-tiny-smart-sao"
  credit: "Alex (tinyledmatrix)"
  caption: "Ultra Tiny Smart SAO PCB"
- file: assets/images/badges/supercon-2024/ultra-tiny-smart-sao/0ab194c929.jpg
  source: "https://hackaday.io/project/197899-ultra-tiny-smart-sao"
  credit: "Alex (tinyledmatrix)"
  caption: "Early concept rendering of the SAO seated on a SAO header"
contact: {}
notes: []
status: announced
sources:
- kind: url
  url: https://hackaday.io/project/197899-ultra-tiny-smart-sao
  title: Ultra Tiny Smart SAO
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: supercon-addons); event read as ''Supercon 8 Add-On Contest — honorable mention; fits within the space of four header pins''.'
- kind: url
  url: https://hackaday.io/project/197899-ultra-tiny-smart-sao
  title: Ultra Tiny Smart SAO (project page, fetched for research)
  accessed: '2026-09-07'
  note: 'Confirmed maker (Alex / tinyledmatrix), event (Supercon 8 SAO Contest, 2024), MCU (ATtiny20-UU BGA), single discrete RGB LED, I2C, castellated corner mounting, 01005 passives; PCBs arrived Sept 25 2024 with assembly in progress. No repo, BOM, or design files linked. No storefront or price found.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a Supercon 8 (2024) SAO Contest entry, not a 2025 item; event corrected to supercon-2024 and file moved into that event folder. Verified against the Hackaday.io project page (maker, contest, MCU, LED, I2C, castellated mounting, 01005 passives, build status) and the maker''s tinyledmatrix profile (name/handle match). One image caption was corrected: the second saved image is labeled "Early Concept rendering" on the image itself, not a photo of an assembled unit, so its caption was fixed to say so. Could not confirm final assembly/working status (no log shows it completed), price, quantity made, or whether design files were ever published. No storefront found.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2025/ultra-tiny-smart-sao/
---

The Ultra Tiny Smart SAO is a self-imposed design challenge by a maker going by Alex (Hackaday.io handle tinyledmatrix), entered into Supercon 8's SAO Contest in 2024. The goal was to build a "smart" add-on — meaning it does at least some I2C communication with the host badge — while making the whole board smaller than the SAO header it plugs into. To hit that footprint, the design uses an ATtiny20 in a BGA package, 01005-size passives (one size down from the already-tiny 0402), and a single discrete RGB LED rather than a standard packaged LED, with castellated holes at all four corners so the tiny PCB can seat directly onto the header pins.

As of the most recent project log (September 25, 2024), the bare PCBs had arrived and needed to be cut and sanded free of the manufacturer's panel frame before assembly could begin; a later comment on the project page (mid-October 2024) mentions still waiting on parts. No log confirms the board was ever fully assembled or shown working. No BOM, schematic, or firmware repository is linked from the project page, and no storefront or pricing information was found, so it reads as a contest entry and design exercise rather than a badge that was ever sold or distributed in quantity.

