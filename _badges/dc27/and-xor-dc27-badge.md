---
title: AND!XOR DC27 Badge
id: dc27-and-xor-dc27-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: AND!XOR
  url: https://andnxor.com/
summary: A hackable, SAO-equipped DEF CON 27 badge from AND!XOR shaped like a gas-masked, hoodie-wearing mascot, with a 102-pixel RGB LED matrix diffused through 3D light pipes instead of a screen.
functions: Bluetooth-based "botnet" badge-to-badge game, a text-based alternate-reality/hacking challenge, and a built-in hardware-hacking multi-tool (serial, I2C, SPI, and JTAG via OpenOCD) exposed through the onboard FTDI FT2232H debugger.
look:
  colors:
  - black
  - white
  - gold
  shape: other
  themes:
  - robot
  - hardware tool
  - security
  - puzzle
  - ctf
tech:
  mcu: NRF52840 (Rigado BMD-340 module)
  leds:
    count: 102
    type: RGB
    note: IS31FL3741 LED driver, light-piped into a goggle-shaped matrix rather than a bare grid
  display: none
  connectivity:
  - bluetooth
  - uart
  - i2c
  battery: 2x AA
  sao_version: v1.69bis
tech_extra:
  capacitive_touch: Azoteq IQS333, two scroll wheels plus a center pad
  usb_uart_bridge: FTDI FT2232H (dual UART, also drives SPI/I2C/JTAG-via-OpenOCD)
  power_reg: LM1117 LDO (USB-C) and Skyworks AAT1217-3.3 boost converter (from AA batteries)
get_one:
  price: free
  price_usd: 0
  quantity: ~600
  availability: sold_out
  availability_note: Checked 2026-09-07 via press coverage; ~75% distributed free at DEF CON 27 / BSides Las Vegas, remaining ~25% sold to Kickstarter-style backers and already sold out at the time.
  distribution:
  - free_drop
  - purchase
  where: Given out at DEF CON 27 and B-Sides Las Vegas, with a portion pre-sold to backers; sponsored by Urbane Security, Macrofab, Mouser Electronics, and Rigado.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: Hackaday.io project logs document the hardware and firmware design, but no consolidated hardware/firmware repo link was found in the sources checked.
links:
- label: hackaday.io/project/164346-andxor-dc27-badge
  url: https://hackaday.io/project/164346-andxor-dc27-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260517132807/https://hackaday.io/project/164346-andxor-dc27-badge
- label: 'Hackaday: Hands-On, AND!XOR DEF CON 27 Badge Ditches Bender, Adopts Light Pipes'
  url: https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
  kind: article
  archived: https://web.archive.org/web/20260831031531/https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
  archived: https://web.archive.org/web/20260513003300/https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
images:
- file: assets/images/badges/dc27/and-xor-dc27-badge/ee96bc1b67.jpg
  source: https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
  credit: AND!XOR / Hackaday
  caption: Front view of the AND!XOR DC27 badge showing the RGB LED goggles matrix and light pipes
  archived: https://web.archive.org/web/20260831031531/https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
- file: assets/images/badges/dc27/and-xor-dc27-badge/4c1c67fb88.jpg
  source: https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
  credit: AND!XOR / Hackaday
  caption: Rear view of the AND!XOR DC27 badge
  archived: https://web.archive.org/web/20260831031531/https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/164346-andxor-dc27-badge
  title: AND!XOR DC27 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''DEF CON 27''.'
  archived: https://web.archive.org/web/20260517132807/https://hackaday.io/project/164346-andxor-dc27-badge
- kind: url
  url: https://hackaday.io/project/164346-andxor-dc27-badge
  title: AND!XOR DC27 Badge (Hackaday.io project page)
  accessed: '2026-09-07'
  note: Confirmed maker, event/year, MCU, LED driver, touch IC, USB bridge, SAO version, and open project-log presence.
  archived: https://web.archive.org/web/20260517132807/https://hackaday.io/project/164346-andxor-dc27-badge
- kind: url
  url: https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
  title: 'Hands-On: AND!XOR DEF CON 27 Badge Ditches Bender, Adopts Light Pipes'
  accessed: '2026-09-07'
  note: Source for LED count/light pipes, power (2x AA + boost converter), design/color scheme, SAO add-ons, distribution split (free vs. sold), and badge photos.
  archived: https://web.archive.org/web/20260831031531/https://hackaday.com/2019/07/29/hands-on-andxor-def-con-27-badge-ditches-bender-adopts-light-pipes/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Maker team members named in some sources as Zapp, Andrew, and Hyr0n, but the entry keeps "AND!XOR" as the credited maker per the sheet's convention (team-level credit used consistently across their other DC entries, e.g. dc30/dc31/dc32/dc33). No consolidated GitHub/hardware repo link was located in the sources checked, so make_your_own.hardware_url/firmware_url are left empty despite the project logs discussing design details (open_source set to "partial" on that basis). Exact price for the backer-sold ~25% was not stated in sources found.
last_modified_date: '2026-09-07'
---

The AND!XOR DC27 badge is a hackable electronic conference badge made by the AND!XOR team for DEF CON 27 (August 2019) in Las Vegas. It replaces a traditional screen with a 102-pixel RGB LED matrix, built around an IS31FL3741 driver and diffused through flexible 3D light pipes into a gas-masked, hoodie-wearing mascot design finished in a black, white, and gold color scheme. Around 600 badges were produced with sponsorship from Urbane Security, Macrofab, Mouser Electronics, and Rigado; roughly three-quarters were given away free at DEF CON 27 and B-Sides Las Vegas, with the remainder pre-sold to backers.

Under the hood it runs an NRF52840 core (via a Rigado BMD-340 module) and uses an Azoteq IQS333 capacitive touch controller for two scroll wheels and a center pad. An onboard FTDI FT2232H exposes dual UART plus SPI, I2C, and JTAG (via OpenOCD), turning the badge into a general-purpose hardware-hacking tool alongside its own games: a Bluetooth "botnet" that let badges interact with each other, and a text-based alternate-reality hacking challenge. It carries a standard SAO v1.69bis header, and the badge supported several companion add-ons sold separately, including a Bender SAO with a hidden serial output, an Audio Reactive SAO, and a Doom SAO with its own screen and serial sniffer. Power comes from two AA batteries through a boost converter, with USB-C handling charging/data via a separate linear regulator.

## Make your own

No consolidated hardware or firmware repository link was found in the sources checked; the Hackaday.io project page documents the build through a series of project logs rather than a single repo, so files were not confirmed as fully published.
