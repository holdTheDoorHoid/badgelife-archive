---
title: 37c3 NFC Badge
id: 37c3-2023-37c3-nfc-badge
layout: badge
parent: 37C3
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: 37c3-2023
year: 2023
makers:
- name: Thomas Flummer
  url: https://github.com/flummer
summary: An independent, open-source NFC badge made for 37C3 (2023), built around an NXP NTAG I2C Plus chip with a StemmaQT/Qwiic I2C connector.
functions: Carries an NDEF link record readable by any NFC phone (e.g. via NXP's TagWriter app); the onboard memory can be rewritten, and RF/I2C write access can be individually locked via on-chip registers.
look:
  colors: []
  shape: null
  themes:
  - nfc
  - security
tech:
  mcu: none
  leds: null
  display: none
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
  open_source: yes
  hardware_url: https://github.com/flummer/37c3
  firmware_url: null
  eda_tool: KiCad
notes:
- Independent open-source NFC hardware badge for 37C3, using an NXP NTAG I2C Plus chip and a StemmaQT/Qwiic connector, inspired by the BornHack 2023 badge design. Found by the event-year sweep, task general-2023.
- 'Research 2026-09-08: confirmed via the maker''s GitHub repo README. Title, maker, chip, connector, and open-source status all confirmed there. Price, quantity, and availability are not stated anywhere on the repo and were left unfilled rather than guessed.'
status: listed
sources:
- kind: url
  url: https://github.com/flummer/37c3
  title: 37c3 NFC Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2023); event read as ''37C3 2023''.'
- kind: url
  url: https://github.com/flummer/37c3
  title: 37c3 NFC Badge (README)
  accessed: '2026-09-08'
  note: Confirmed maker, chip (NXP NT3H2111W0FHKH NTAG I2C Plus 1K), StemmaQT/Qwiic I2C connector, KiCad v7 design tool, CC BY-SA 4.0 license, and that it is inspired by/copied from the BornHack 2023 badge electronics.
images:
- file: assets/images/badges/37c3-2023/37c3-nfc-badge/361a443b42.jpg
  source: "https://github.com/flummer/37c3"
  credit: "Thomas Flummer"
  caption: "37c3 NFC badge, front and back, standing"
contact: {}
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Maker's own GitHub repo confirms the badge, chip, connector, license, and design tool. No price, quantity made, or distribution details are published anywhere in the repo, so those fields are left empty. No independent press coverage (Hackaday, Tindie, etc.) was found; confidence is medium rather than high because everything traces to the one repo.
last_modified_date: '2026-09-08'
---

The 37c3 NFC Badge is a small, independent hardware badge that Thomas Flummer designed for the Chaos Communication Congress 37C3 in 2023. It is built around an NXP NTAG I2C Plus (NT3H2111W0FHKH) chip, giving it a passive NFC interface alongside a StemmaQT/Qwiic-compatible I2C connector for wired communication with other boards. The badge ships preloaded with an NDEF link record pointing back to its own GitHub repository, and its 1K of onboard memory can be rewritten with apps such as NXP's TagWriter, with optional register-level write protection on the RF and I2C interfaces independently.

By the maker's own account, the badge's electronics are almost entirely carried over from the BornHack 2023 badge (also an NXP NTAG I2C Plus design), scaled down slightly to 1K of memory instead of BornHack's 2K. The hardware is fully open source, designed in KiCad v7, and released under a CC BY-SA 4.0 license.

No price, production quantity, or distribution details are published in the repository, so availability could not be confirmed beyond the design files themselves being public.
