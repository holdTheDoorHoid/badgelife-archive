---
title: Numberwang Badge
id: cccamp-2019-numberwang-badge-2
layout: badge
parent: CCCamp19
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cccamp-2019
year: 2019
makers:
- name: timonsku
  url: https://hackaday.io/timonsku
summary: A badge made for the Numberwang village at Chaos Communication Camp 2019 that does blinking LEDs and sound so wearers can pretend to play Numberwang, built on an ATSAMD21G18 with the Adafruit Itsy Bitsy M0 pinout, a LiPo charger, and custom CircuitPython firmware.
functions: 'Blinking LEDs and I2S audio so the wearer can "pretend to play Numberwang" (a reference to the fictional game from the British comedy sketch series of the same name).'
look:
  colors: []
  shape: null
  themes:
  - meme
  - tv
  - village badge
tech:
  mcu: ATSAMD21G18
  leds: null
  display: null
  connectivity:
  - audio
  battery: LiPo with integrated charger (JST-PH 2.0 SMT, reversed polarity)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed to attendees of the Numberwang village at CCCamp19; the maker notes surviving units were given out directly rather than sold.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/timonsku/Numberwang-Badge
  firmware_url: https://github.com/timonsku/Numberwang-Badge
  eda_tool: null
links:
- label: hackaday.io/project/167356-numberwang-badge
  url: https://hackaday.io/project/167356-numberwang-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260907111101/https://hackaday.io/project/167356-numberwang-badge
- label: github.com/timonsku/Numberwang-Badge
  url: https://github.com/timonsku/Numberwang-Badge
  kind: repo
  archived: https://web.archive.org/web/20260907111136/https://github.com/timonsku/Numberwang-Badge
- label: twitter.com/i/status/1162331672601403394
  url: https://twitter.com/i/status/1162331672601403394
  kind: social
images:
- file: assets/images/badges/cccamp-2019/numberwang-badge-2/00ca752b29.jpg
  source: "https://hackaday.io/project/167356-numberwang-badge"
  credit: "timonsku"
  caption: "The Numberwang Badge PCB"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/167356-numberwang-badge
  title: Numberwang Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
  archived: https://web.archive.org/web/20260907111101/https://hackaday.io/project/167356-numberwang-badge
- kind: url
  url: https://hackaday.io/project/167356-numberwang-badge
  title: Numberwang Badge - Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed event/village, function (blinkies and sound to "pretend to play Numberwang"), and that it was given to Numberwang village attendees at CCCamp19; supplied the badge photo used above.
- kind: url
  url: https://github.com/timonsku/Numberwang-Badge
  title: timonsku/Numberwang-Badge
  accessed: '2026-09-07'
  note: Confirmed MCU (ATSAMD21G18, Itsy Bitsy M0 pinout), LiPo charger with JST-PH 2.0 SMT connector, I2S audio amp, CircuitPython/UF2 firmware with Arduino support via Adafruit SAMD package, and a known hardware bodge required for audio (a signal was left unconnected to the I2S amp).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: The maker's own Hackaday.io and GitHub pages confirm hardware and purpose, but neither states LED count/type, price, or quantity made, so those fields remain empty. The repo notes a known hardware bug (one signal not routed to the I2S amp) requiring a bodge wire for audio to work; documentation is described by the maker as minimal. No storefront was found, consistent with village giveaway distribution rather than sale.
last_modified_date: '2026-09-07'
---

The Numberwang Badge was made by timonsku for the Numberwang village at Chaos Communication Camp 2019 (CCCamp19), a village themed around the fictional game "Numberwang" from the British comedy sketch series of the same name. The badge is built around an ATSAMD21G18 microcontroller wired to the Adafruit Itsy Bitsy M0 pinout, runs on a LiPo battery with an onboard charger, and combines blinking LEDs with an I2S audio amplifier so wearers can pretend to play along with the game.

Firmware is a customized build of CircuitPython for the Itsy Bitsy M0, distributed as a UF2 file, with the board also usable under Arduino via Adafruit's SAMD board package. The maker's GitHub repo notes one hardware bug in the initial run: a signal meant to feed the I2S amplifier was left unconnected, requiring a bodge wire (documented with a reference image in the repo) to get audio working. Hardware and firmware files are published on GitHub, though the maker describes the documentation as minimal.

## Make your own

Design files and firmware are at https://github.com/timonsku/Numberwang-Badge. Note the documented audio bodge fix is required on boards built from the original files for the I2S amp to function.
