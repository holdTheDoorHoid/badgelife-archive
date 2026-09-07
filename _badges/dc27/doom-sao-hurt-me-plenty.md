---
title: DC27 DOOM SAO - Hurt Me Plenty
id: dc27-doom-sao-hurt-me-plenty
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc27
year: 2019
makers:
- name: AND!XOR
  url: https://andnxor.com/
- name: LonghornEngineer (Parker Dillmann / Cr4bf04m)
  url: https://github.com/LonghornEngineer
  role: hardware/firmware design
summary: A SAO v1.69bis hardware-hacking add-on for the DC27 AND!XOR badge that shows DOOM Guy on a color LCD and doubles as a passive I2C/UART bus sniffer for the badge it's plugged into.
functions: Displays an animated DOOM Guy face whose "health" and anger state react to I2C traffic on the badge's SAO bus; sniffs and logs I2C and UART traffic passing between the badge and its add-ons; can run standalone in an "auto mode" when not attached to a host badge; settings persist in EEPROM.
look:
  colors: []
  shape: rectangle
  themes:
  - video game
  - horror
  - hardware tool
  - security
tech:
  mcu: ATSAMD21G18A
  leds: null
  display: 1.3" IPS LCD (ST7789, 240x240)
  connectivity:
  - i2c
  - uart
  - usb
  battery: powered by host badge
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Sold through the AND!XOR shop (shop.andnxor.com); remaining stock was also taken to the Hacker Warehouse vendor booth at DEF CON 27.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/LonghornEngineer/DOOM_SAO
  firmware_url: https://github.com/LonghornEngineer/DOOM_SAO
  eda_tool: null
  license: Apache License 2.0 (embargoed until 2019-08-11)
links:
- label: hackaday.io/project/164346-andxor-dc27-badge/log/165849-dc27-doom-sao-hurt-me-plenty
  url: https://hackaday.io/project/164346-andxor-dc27-badge/log/165849-dc27-doom-sao-hurt-me-plenty
  kind: hackaday
- label: LonghornEngineer/DOOM_SAO (GitHub)
  url: https://github.com/LonghornEngineer/DOOM_SAO
  kind: repo
images:
- file: assets/images/badges/dc27/doom-sao-hurt-me-plenty/f24f10311b.jpg
  source: "https://hackaday.io/project/164346-andxor-dc27-badge/log/165849-dc27-doom-sao-hurt-me-plenty"
  credit: "AND!XOR / LonghornEngineer"
  caption: "DOOM SAO Hurt Me Plenty board detail"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://hackaday.io/project/164346-andxor-dc27-badge/log/165849-dc27-doom-sao-hurt-me-plenty
  title: DC27 DOOM SAO - Hurt Me Plenty
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''dc27''.'
- kind: url
  url: https://github.com/LonghornEngineer/DOOM_SAO
  title: LonghornEngineer/DOOM_SAO
  accessed: '2026-09-07'
  note: Hardware/firmware repo; confirms chip (ATSAMD21G18A), display (ST7789 1.3" 240x240), I2C address 0x50, license.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: >-
    Price and quantity made were not stated on either the Hackaday.io log or the GitHub repo, so those fields are left empty. The board has no addressable/discrete LEDs of its own (all visual output is via the LCD), so tech.leds is left null rather than guessed. Fact-check found one of the two saved images (5d7167109e.jpg) was not a photo of this SAO at all -- it was an unrelated AND!XOR badge packaging/warning-label graphic -- so it was deleted and removed from the entry; only the genuine board photo (f24f10311b.jpg, showing the ATSAMD21 MCU, USB-C connector, and "DOOM"/"Longhorn 2018" silkscreen) remains. The "where sold" text was also corrected -- the Hackaday.io log says remaining stock went to the Hacker Warehouse vendor booth at DEF CON 27, not AND!XOR's own vendor table. All other fields (maker, MCU, display, connectivity, SAO version, I2C address, functions/auto-mode/health/anger/EEPROM/I2C+UART sniffing, license, open-source status) were directly confirmed against the Hackaday.io log and the GitHub repo README.
last_modified_date: '2026-09-07'
---

The DOOM SAO "Hurt Me Plenty" is a Shitty Add-On built by Parker Dillmann (LonghornEngineer, working under the handle Cr4bf04m) for AND!XOR's DEF CON 27 badge in 2019. Rather than being a purely decorative add-on, it's a hardware-hacking tool disguised as a game reference: a 1.3" color LCD renders an animated DOOM Guy face whose expression and "health" respond to real I2C traffic passing across the SAO bus, while the board simultaneously acts as a passive sniffer for the I2C and UART lines connecting the host badge to its other add-ons.

Under the hood it runs an Arduino-compatible Microchip ATSAMD21G18A, talks over the SAO v1.69bis (6-pin) standard, and exposes a USB-C connector for a serial terminal used to configure it and view sniffed traffic. Settings and captured state are held in EEPROM, and the board can also run standalone in an "auto mode" when it isn't attached to a badge. It was sold through AND!XOR's own shop, with remaining stock taken to the Hacker Warehouse vendor booth at DEF CON 27.

Hardware and firmware are both open source on GitHub under the Apache License 2.0 (released after a short embargo following DEF CON 27), making it a documented, buildable reference design for anyone who wants a bus-sniffing SAO of their own.
