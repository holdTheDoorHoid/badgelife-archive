---
title: DEF CON 23 Hardware Hacking Village Learn-to-Solder Kit
id: other-hardware-hacking-village-learn-to-solder-kit
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: other
year: 2015
makers:
- name: Smitty
  role: concept, crypto, and 2014 firmware
- name: Krux
  role: hardware
- name: Cmdc0de
  role: 2015 firmware
summary: An Arduino-compatible, self-solder ID badge sold by DEF CON's Hardware Hacking Village at DEF CON 23 (2015), acting as a "DarkNet ID Badge" that exchanged identifiers with other badges over IR as part of the con's DarkNet challenge.
functions: Exchanges a unique identifier with other assembled DarkNet badges via IR when pointed at each other, as part of DEF CON's DarkNet puzzle challenge; drives a small OLED display; can also act as a USB keyboard.
look:
  colors: []
  shape: rectangle
  themes:
  - learn to solder
  - kit
  - village badge
tech:
  mcu: ATmega (Arduino-compatible)
  leds: null
  display: SSD1306-based OLED (daughterboard)
  connectivity:
  - ir
  - usb
  battery: null
  sao_version: null
get_one:
  price: $25
  price_usd: 25
  quantity: '350+ (over 300 chips programmed for the run; ~200 additional sold Saturday after Friday sellout)'
  availability: sold_out
  distribution:
  - kit
  - village
  where: Sold as a solder-it-yourself kit at the DEF CON 23 (2015) Hardware Hacking Village.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/thedarknet/hhvkit
  firmware_url: https://github.com/thedarknet/hhvkit
  eda_tool: null
  bom_url: https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=6bc2d848d8
  notes: Repo contains Arduino-based firmware (targets Arduino v1.6.4), modified Adafruit GFX/SSD1306 display libraries, a modified SoftwareSerial for IR, a modified vusb-for-arduino USB-keyboard library, and the batch-programming scripts (buildDB.pl, burn-bootloader.sh, burn-eeprom.sh, burn-flash.sh, run.pl) used to program the ~350-chip run. Assembly instructions were originally hosted at dcdark.net/2015/hhv-badge/ and dcdark.net/2015/hhv-display/, both now 404.
links:
- label: github.com/thedarknet/hhvkit
  url: https://github.com/thedarknet/hhvkit
  kind: repo
- label: Hackaday - All The Unofficial Electronic Badges Of DEF CON (2015)
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  kind: article
images:
  - file: assets/images/badges/other/hardware-hacking-village-learn-to-solder-kit/9f071b48c8.jpg
    source: "https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/"
    credit: "Hackaday"
    caption: "DEF CON DarkNet Hardware Hacking Village badge, assembled"
  - file: assets/images/badges/other/hardware-hacking-village-learn-to-solder-kit/f281f39c87.jpg
    source: "https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/"
    credit: "Hackaday"
    caption: "DEF CON DarkNet Hardware Hacking Village badge kit parts/board"
contact: {}
notes:
- Described as 'DefCon Hardware Hacking Village Learn To Solder Kit'; the maker's own repo README dates this specific kit to DEF CON 23 (2015), continuing a badge the same designers (Smitty, Krux) made the prior year (2014) - "this year's design is very similar to last year's" per Hackaday. No matching event id for DEF CON's Hardware Hacking Village exists in events.yml as a sub-event, so event is left as 'other' with the con/year (DEF CON 23, 2015) noted here; the closest whole-con id is 'dc23'.
- A commenter on the Hackaday article calls out a separate "display daughter board" for the badge, consistent with the OLED display being an add-on board rather than on the main PCB.
status: released
sources:
- kind: url
  url: https://github.com/thedarknet/hhvkit
  title: Hardware Hacking Village Learn-to-Solder Kit
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''DEF CON Hardware Hacking Village, year unconfirmed (ongoing/recurring kit)''.'
- kind: url
  url: https://github.com/thedarknet/hhvkit
  title: "thedarknet/hhvkit README"
  accessed: '2026-09-07'
  note: "Maker's own README: names the DEF CON 23 (2015) event, the three makers and their roles, the ATmega/Arduino platform, IR modulation, OLED display, USB-keyboard capability, BOM link (Mouser), and now-dead dcdark.net assembly-instruction links."
- kind: url
  url: https://hackaday.com/2015/08/10/all-the-unofficial-electronic-badges-of-def-con/
  title: "All The Unofficial Electronic Badges Of DEF CON (Hackaday, 2015)"
  accessed: '2026-09-07'
  note: "Confirms $25 kit price, sold out Friday with ~200 more sold Saturday, Arduino-based, IR badge-to-badge identifier exchange for the DarkNet challenge, designers Smitty and Krux; supplied the two photos used here (captioned 'DEF CON DarkNet Badge')."
- kind: url
  url: https://forum.defcon.org/node/221577
  title: "DEF CON Forums - Darknet Badge Kits thread"
  accessed: '2026-09-07'
  note: "Attempted fetch failed (connection reset); not used as a source."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Core facts (event/year, makers, platform, function, price, open-source status) confirmed directly from the maker''s own GitHub README plus a contemporaneous Hackaday article. LED count/type and exact battery/power arrangement are not stated in any source found and are left empty. The original dcdark.net assembly-instruction pages (linked from the README) now return 404, so build-a-badge instructions beyond the GitHub firmware/BOM could not be verified live. No matching sub-event id for "DEF CON Hardware Hacking Village" exists in events.yml (only whole-con ids like dc23 exist), so event was left as ''other'' rather than guessed onto dc23, which represents the whole convention, not the village. Quantity is stated only loosely across sources (over 300 chips programmed per the firmware README''s build tooling; ~350+ sold per the Hackaday sellout numbers) so get_one.quantity is reported as a range/description rather than a single figure.'
last_modified_date: '2026-09-07'
---

The DEF CON 23 Hardware Hacking Village Learn-to-Solder Kit was a self-assembly "DarkNet ID Badge" sold at DEF CON 23 in Las Vegas in August 2015. Built around an Arduino-compatible ATmega microcontroller with a small SSD1306-based OLED display daughterboard, the badge used an infrared LED to exchange a unique identifier with any other assembled badge it was pointed at, feeding into DEF CON's ongoing "DarkNet" puzzle challenge that ran across multiple years. It also doubled as a USB keyboard via a modified vusb-for-arduino library. The kit sold for $25 at the Hardware Hacking Village and was popular enough to sell out on the first day, with roughly 200 more made available the next morning.

The badge continued a design lineage from the previous year's DarkNet badge (2014), created by Smitty (concept, crypto, and the original firmware) and Krux (hardware), with Cmdc0de contributing the 2015 firmware update. Its makers open-sourced the Arduino firmware, custom IR-serial and display libraries, and the batch-programming scripts used to flash EEPROM identifiers and firmware onto the several hundred chips built for the con, along with a link to a Mouser-hosted bill of materials. The original web-hosted assembly instructions (at dcdark.net) are no longer live, but the GitHub repository still documents how to build and flash the firmware.

## Make your own

Firmware, the BOM link, and the batch-programming tooling are published at [github.com/thedarknet/hhvkit](https://github.com/thedarknet/hhvkit). The firmware builds under Arduino v1.6.4; the repo also includes `burn-bootloader.sh`, `burn-eeprom.sh`, and `burn-flash.sh` scripts (written for a USBtinyISP) that were used to program the run of badges, plus a `buildDB.pl` script to generate the GUID/key pairs a badge needs in EEPROM to function as a DarkNet ID. Hardware/PCB files referenced by the README were not independently verified as still present in the repo at time of writing.
