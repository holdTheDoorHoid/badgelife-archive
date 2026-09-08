---
title: SAOGNR - An SAO for Morse Code
id: supercon-2024-saognr-a-ham-radio-sao-supercon-add-on
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Al Williams (wd5gnr)
  url: https://hackaday.io/project/198144-saognr-an-sao-for-morse-code
summary: An RP2040-based SAO that sends canned messages in Morse code over a built-in speaker and intelligent LEDs, and can act as an I2C peripheral so a host badge can command it to send Morse.
functions: Sends short Morse code messages via speaker and addressable LEDs; can be commanded over I2C by a host badge's own microcontroller to send Morse snippets.
look:
  colors: []
  shape: null
  themes:
  - radio
tech:
  mcu: RP2040
  leds: null
  display: none
  connectivity:
  - i2c
  - audio
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '20 built for Supercon 2024'
  availability: sold_out
  distribution:
  - swap
  where: Al Williams brought 20 units to Supercon 2024 and traded most of them away, leaving with only 3.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/wd5gnr/saognr
  firmware_url: https://github.com/wd5gnr/saognr
  eda_tool: null
links:
- label: hackaday.io/project/198144-saognr-an-sao-for-morse-code
  url: https://hackaday.io/project/198144-saognr-an-sao-for-morse-code
  kind: hackaday
- label: github.com/wd5gnr/saognr
  url: https://github.com/wd5gnr/saognr
  kind: repo
images:
  - file: assets/images/badges/supercon-2024/saognr-a-ham-radio-sao-supercon-add-on/c8fcac51c5.jpg
    source: "https://hackaday.io/project/198144-saognr-an-sao-for-morse-code"
    credit: "Al Williams (wd5gnr)"
    caption: "SAOGNR Morse code SAO board"
contact: {}
notes:
- A Morse-code themed SAO Al Williams (WD5GNR) designed as his own example entry for the Supercon 2024 "use I2C" SAO challenge; he brought 20 to Supercon 2024 and left with 3 after trading. The discovery sweep's title read "A Ham Radio SAO" (from the sheet); the maker's own title on Hackaday.io and GitHub is "SAOGNR - An SAO for Morse Code" / "SAO (Supercon Add On) I2C peripheral for sending Morse code", which this entry now uses.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198144-saognr-an-sao-for-morse-code
  title: SAOGNR - An SAO for Morse Code
  accessed: '2026-09-08'
  note: 'Maker''s Hackaday.io project page: confirms creator, event (Supercon 2024), RP2040 MCU, I2C/speaker functions, quantity (20 built, 3 kept), and open-source status.'
- kind: url
  url: https://github.com/wd5gnr/saognr
  title: wd5gnr/saognr - SAO (Supercon Add On) I2C peripheral for sending Morse code
  accessed: '2026-09-08'
  note: 'Maker''s GitHub repo README: confirms it was built for the Supercon 2024 "use I2C" SAO challenge, power options (SAO connector or USB-C), and links Gerbers/schematic/BOM.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: LED type/count not stated on either source beyond "intelligent LEDs" (addressable), so tech.leds is left null. No price is mentioned anywhere; it was distributed by trading at the event, not sold. EDA tool not specified in the repo listing.
last_modified_date: '2026-09-08'
---

SAOGNR is a Simple Add-On (SAO) built by Al Williams (WD5GNR) as his own entry for the Supercon 2024 SAO challenge, which that year asked designers to make use of I2C. The board sends short, canned messages in Morse code through a built-in speaker and a set of addressable LEDs, and doubles as an I2C peripheral so a host badge's own microcontroller can command it to key out Morse snippets on demand. It runs on an RP2040 and can draw power either from the host badge's SAO connector or from its own USB-C port; Williams notes that running the speaker alongside the main Supercon badge's own RP2040 can noticeably reduce its volume.

Williams brought 20 assembled units to Supercon 2024 and traded away all but three over the course of the event, so it was never sold — it circulated as a badge-swap item among attendees. The hardware and firmware are fully open source, published on GitHub with a schematic, bill of materials, and Gerber files alongside an early user's guide.

## Make your own

The full design is published at github.com/wd5gnr/saognr, including a PDF schematic, an Excel bill of materials, and Gerber files for fabrication, plus firmware for the RP2040.
