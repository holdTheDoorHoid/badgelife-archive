---
title: Hackaday Supercon 2022 Badge (computing history handheld)
id: supercon-2022-hackaday-supercon-2022-badge-computing-history-handheld
layout: badge
parent: Supercon 2022
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2022
year: 2022
makers:
- name: Voja Antonic
  role: hardware/firmware designer
- name: Hackaday badge team
summary: A handheld badge that simulates a hypothetical 4-bit CPU, letting attendees hand-enter and run programs bit by bit and watch memory light up on an 8x16 LED array, echoing early microcomputers like the Altair 8800 and IMSAI 8080.
functions: Bit-by-bit program entry and execution on a simulated 4-bit CPU (31 opcodes, 4,096 x 12-bit instruction memory, 256 x 4-bit data memory, 5-deep stack); adjustable clock speed from 0.5 Hz up to about 250 KHz (0.1 MIPS); up to 15 programs stored in onboard flash; code can also be loaded/saved over UART via a USB-to-serial adapter; a 12-pin expansion connector let attendees build add-ons, including a punch-card reader hack built during the con.
look:
  colors: []
  shape: rectangle
  themes:
  - retro computer
  - learn to solder
  - puzzle
tech:
  mcu: PIC24FJ256GA704
  leds:
    count: 128
    type: discrete
    note: 8x16 LED array used as a window into the simulated CPU's memory/registers, not decorative lighting.
  display: LED matrix 8x16
  connectivity:
  - uart
  inputs:
  - buttons
  battery: null
  sao_version: v1
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of the 2022 Hackaday Superconference (November 4-6, 2022).
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: Hackaday's badge-reveal post said design files, Gerbers, an emulator, and firmware were planned for public release; no confirmed repo/Gerber link was found this session.
links:
- label: hackaday.com/2022/10/12/the-2022-supercon-badge-is-a-handheld-trip-through-computing-history
  url: https://hackaday.com/2022/10/12/the-2022-supercon-badge-is-a-handheld-trip-through-computing-history/
  kind: article
  archived: https://web.archive.org/web/20260730121929/https://hackaday.com/2022/10/12/the-2022-supercon-badge-is-a-handheld-trip-through-computing-history/
- label: hackaday.com/2022/11/17/supercon-badge-reads-a-punch-card
  url: https://hackaday.com/2022/11/17/supercon-badge-reads-a-punch-card/
  kind: article
  archived: https://web.archive.org/web/20260306180035/https://hackaday.com/2022/11/17/supercon-badge-reads-a-punch-card/
images:
- file: assets/images/badges/supercon-2022/hackaday-supercon-2022-badge-computing-history-handheld/543e11afc4.jpg
  source: https://hackaday.com/2022/11/17/supercon-badge-reads-a-punch-card/
  credit: Hackaday
  caption: The 2022 Supercon badge with an attendee-built punch-card reader attachment
  archived: https://web.archive.org/web/20260306180035/https://hackaday.com/2022/11/17/supercon-badge-reads-a-punch-card/
- file: assets/images/badges/supercon-2022/hackaday-supercon-2022-badge-computing-history-handheld/c24f94501a.jpg
  source: https://hackaday.com/2022/10/12/the-2022-supercon-badge-is-a-handheld-trip-through-computing-history/
  credit: Elliot Williams / Hackaday
  caption: The 2022 Supercon badge, an 8x16 LED array simulating a 4-bit CPU
  archived: https://web.archive.org/web/20260730121929/https://hackaday.com/2022/10/12/the-2022-supercon-badge-is-a-handheld-trip-through-computing-history/
contact: {}
notes:
- See also hackaday.com/2022/11/17/supercon-badge-reads-a-punch-card/, which covers an attendee-built optical punch-card reader add-on (Ben Hencke and Zach Fredin) that plugged into the badge's expansion connector and read encoded programs via charlieplexed LEDs used as photodiodes.
status: released
sources:
- kind: url
  url: https://hackaday.com/2022/10/12/the-2022-supercon-badge-is-a-handheld-trip-through-computing-history/
  title: Hackaday Supercon 2022 Badge (computing history handheld)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''Hackaday Supercon 2022''.'
  archived: https://web.archive.org/web/20260730121929/https://hackaday.com/2022/10/12/the-2022-supercon-badge-is-a-handheld-trip-through-computing-history/
- kind: url
  url: https://hackaday.com/2022/10/12/the-2022-supercon-badge-is-a-handheld-trip-through-computing-history/
  title: The 2022 Supercon Badge Is A Handheld Trip Through Computing History
  accessed: '2026-09-07'
  note: Confirmed designer (Voja Antonic), MCU (PIC24FJ256GA704), CPU simulation details, LED matrix, clock speed range, flash program storage, and planned open-source release.
  archived: https://web.archive.org/web/20260730121929/https://hackaday.com/2022/10/12/the-2022-supercon-badge-is-a-handheld-trip-through-computing-history/
- kind: url
  url: https://hackaday.com/2022/11/17/supercon-badge-reads-a-punch-card/
  title: Supercon Badge Reads A Punch Card
  accessed: '2026-09-07'
  note: Confirmed the badge's 12-pin expansion connector and an attendee hack (punch-card reader) built at the con; provided a photo of the badge.
  archived: https://web.archive.org/web/20260306180035/https://hackaday.com/2022/11/17/supercon-badge-reads-a-punch-card/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (designer, MCU, CPU simulation, LED display, expansion connector) confirmed on Hackaday''s own coverage. Could not confirm: price/cost to Hackaday, quantity made, whether Gerbers/firmware were actually published (only that release was planned), and no repo or hackaday.io project link was found this session. Web search budget was exhausted before a repo/hackaday.io search could be run.'
last_modified_date: '2026-09-07'
---

The 2022 Hackaday Superconference badge, designed by Voja Antonic, is a handheld computer built around a hypothetical 4-bit CPU rather than a real historical chip. A PIC24FJ256GA704 microcontroller runs the simulation: 4,096 words of 12-bit instruction memory, 256 nibbles of data memory, a 5-deep stack, and 31 opcodes. Attendees enter programs by hand, bit by bit, using the badge's tactile buttons, and watch the CPU's memory and registers light up across an 8x16 LED array — a nod to front-panel machines like the Altair 8800 and IMSAI 8080. The simulated clock can be slowed to 0.5 Hz to watch execution step by step, or sped up to roughly 250 KHz (about 0.1 MIPS). Up to 15 programs can be saved to onboard flash, and code can also be loaded or dumped over UART through a USB-to-serial adapter.

A 12-pin expansion connector on the badge invited hardware add-ons, and one of the more notable hacks to come out of Supercon that year used it: Ben Hencke and Zach Fredin built an optical punch-card reader that fed encoded 12-bit opcodes into the badge over serial, repurposing ordinary LEDs as photodiodes (via charlieplexing) to sense marks on printed cards.

Hackaday's badge reveal post said Gerbers, an emulator, and firmware would be released publicly, but this session could not locate a confirmed repository or hackaday.io project page carrying those files.
