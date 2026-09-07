---
title: FREE-WILi DC32 Badge Firmware
id: dc32-free-wili-dc32-badge-firmware
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: other
event: dc32
year: 2024
makers:
- name: FREE-WILi project team
  url: https://freewili.com/
summary: Free alternative firmware for the DEF CON 32 (RP2350) badge that turns it into a hardware-hacking multi-tool, released by the FREE-WILi team to showcase their own device's capabilities.
functions: Adds a graphical menu for GPIO pin control, I2C communication, and infrared transmit/receive on the stock DC32 badge; also supports testing and debugging SAOs, similar in spirit to a Bus Pirate.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: RP2350
  leds: null
  display: graphical menu (uses the stock DC32 badge's screen)
  connectivity:
  - i2c
  - ir
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Released as a free firmware download for owners of the official DEF CON 32 badge (approximately 30,000 of which were issued).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/freewili/freewili-firmware
  eda_tool: null
links:
- label: hackaday.com/2024/11/21/free-wili-turns-dc32-badge-into-hardware-dev-tool
  url: https://hackaday.com/2024/11/21/free-wili-turns-dc32-badge-into-hardware-dev-tool/
  kind: article
- label: freewili/freewili-firmware (GitHub)
  url: https://github.com/freewili/freewili-firmware
  kind: repo
- label: FREE-WILi project site
  url: https://freewili.com/
  kind: website
images: []
contact: {}
notes:
- Not a standalone physical badge or SAO; it is replacement firmware for the official, separately-issued DEF CON 32 badge.
status: not_an_item
sources:
- kind: url
  url: https://hackaday.com/2024/11/21/free-wili-turns-dc32-badge-into-hardware-dev-tool/
  title: FREE-WILi DC32 Badge Firmware
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''DEF CON 32''.'
- kind: url
  url: https://hackaday.com/2024/11/21/free-wili-turns-dc32-badge-into-hardware-dev-tool/
  title: 'FREE-WILi Turns DC32 Badge Into Hardware Dev Tool'
  accessed: '2026-09-07'
  note: Confirmed it is firmware (not a physical item) for the stock RP2350 DC32 badge; MCU, features (GPIO/I2C/IR/SAO debugging), ~30,000 DC32 badges in circulation, GitHub repo has binaries only (no published source at time of writing).
- kind: url
  url: https://github.com/freewili/freewili-firmware
  title: 'GitHub - freewili/freewili-firmware: Firmware files for Free-WILi'
  accessed: '2026-09-07'
  note: Firmware repository referenced as the source of the DC32 badge build; contents not verified to include full source for the DC32-specific build.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: This is alternative firmware for the officially-issued DEF CON 32 badge, not a distinct physical badge or SAO, so it does not fit the archive's item model. Left as an entry documenting the software release. Hackaday reported the GitHub repo at the time contained only binaries, no source; the freewili-firmware repo exists but its DC32-specific source completeness was not independently verified.
last_modified_date: '2026-09-07'
---

FREE-WILi is a commercial open-electronics multitool built around the RP2350 microcontroller. In November 2024, the FREE-WILi team released a free alternative firmware image for the official DEF CON 32 attendee badge (which itself uses an RP2350), giving badge owners a graphical menu-driven interface for controlling GPIO pins, talking over I2C, and sending or receiving infrared signals. The firmware also supports testing and debugging Simple Add-Ons (SAOs) plugged into the badge, effectively turning the stock badge into a low-cost hardware-hacking tool in the spirit of a Bus Pirate.

With roughly 30,000 DC32 badges issued, this gave a large existing installer base new functionality for free, while doubling as a demonstration and on-ramp for FREE-WILi's own paid hardware line. At the time of the Hackaday writeup, the firmware's GitHub repository shipped only pre-built binaries rather than full source, though a broader `freewili/freewili-firmware` repository exists for the underlying platform.

This is documented here as a notable badge-software release rather than as a standalone badge or SAO, since it modifies an already-catalogued official con badge rather than being its own hardware item.
