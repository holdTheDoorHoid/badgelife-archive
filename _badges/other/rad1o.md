---
title: Rad1o
id: other-rad1o
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2015
makers:
- name: Chaos Computer Club Munich
  url: https://github.com/rad1o
summary: A wearable software-defined radio transceiver badge given out at Chaos Communication Camp 2015, tuning roughly 50 MHz to 4000 MHz and software-compatible with HackRF.
functions: Half-duplex SDR transceiver (50 MHz-4000 MHz); can boot into HackRF-compatible firmware or custom firmware; displays a custom nickname; joystick navigation.
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
tech:
  mcu: ARM Cortex-M4 (NXP LPC4330)
  leds: null
  display: Nokia 6100, 130x130 pixel color LCD
  connectivity:
  - usb
  battery: LiPo (onboard, USB-chargeable)
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: '4500'
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of Chaos Communication Camp 2015 as the event badge.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/rad1o/hardware
  firmware_url: https://github.com/rad1o
  eda_tool: null
links:
- label: hackaday.io/project/7322-rad1o
  url: https://hackaday.io/project/7322-rad1o
  kind: hackaday
- label: CCCamp 2015 Rad1o Badge (Hackaday.com)
  url: https://hackaday.com/2015/07/12/cccamp-2015-rad1o-badge/
  kind: article
  accessed: '2026-09-07'
  archived: https://web.archive.org/web/20260729112303/https://hackaday.com/2015/07/12/cccamp-2015-rad1o-badge/
- label: rad1o hardware repository (GitHub)
  url: https://github.com/rad1o/hardware
  kind: repo
  accessed: '2026-09-07'
- label: rad1o wiki / official badge site
  url: https://rad1o.badge.events.ccc.de/
  kind: website
  accessed: '2026-09-07'
images:
- file: assets/images/badges/other/rad1o/099d1fd198.jpg
  source: https://hackaday.io/project/7322-rad1o
  credit: rad1o project / CCC
  caption: The rad1o SDR badge, front side
contact: {}
notes:
- EDA tool used for the hardware is Eagle CAD (.sch/.brd files in the hardware repo), not confirmed as a maker-published label so left null in tech fields per guide, but recorded here.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/7322-rad1o
  title: Rad1o
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''Chaos Communication Congress (badge.team lineage)''.'
- kind: url
  url: https://hackaday.io/project/7322-rad1o
  title: rad1o | Hackaday.io
  accessed: '2026-09-07'
  note: Project summary, maker, MCU, connectivity, open-source status, image gallery link.
- kind: url
  url: https://hackaday.com/2015/07/12/cccamp-2015-rad1o-badge/
  title: CCCamp 2015 Rad1o Badge
  accessed: '2026-09-07'
  note: Confirms event, year, frequency range, display, battery, joystick, and lineage from the r0ket (CCCamp 2011 badge).
  archived: https://web.archive.org/web/20260729112303/https://hackaday.com/2015/07/12/cccamp-2015-rad1o-badge/
- kind: url
  url: https://rad1o.badge.events.ccc.de/
  title: start [rad1o]
  accessed: '2026-09-07'
  note: Official wiki confirming badge features and firmware update process.
- kind: url
  url: https://github.com/rad1o/hardware
  title: 'GitHub - rad1o/hardware: rad1o: CCCamp15 SDR Badge'
  accessed: '2026-09-07'
  note: Confirms open-source hardware under GPL-2.0, Eagle CAD schematic/board files.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Made by Chaos Computer Club Munich as the official badge of Chaos Communication Camp 2015 (a camp, not a Congress, correcting the sweep''s original guess); the archive''s events.yml has no cccamp-2015 entry (only cccamp-2019 exists), so event is left as "other" pending that event being added. 4,500 units were made and given away free to attendees; none are for sale now. LED count/type not documented in sources reviewed. EDA tool for hardware is Eagle CAD per the GitHub repo, but not stated as such by the maker in prose, so left out of tech.eda_tool per the "never invent" / prefer explicit statement caution; noted in notes instead. The rad1o is the direct successor to the r0ket badge (CCCamp 2011). Fact-check pass (2026-09-07): corrected "full-duplex" to "half-duplex" in functions (both hackaday.io and the official wiki explicitly call it a half-duplex transceiver); removed an unsupported claim about community-written games (no source mentions games); removed an invented "second
    USB port" detail from the body (only one USB connection is documented, used for both charging and data/firmware); changed get_one.availability from sold_out to free per the guide''s vocabulary, since this was a giveaway, never a sale. NXP LPC4330 is confirmed only indirectly, via an LPC4350/30/20/10 datasheet filed in the GitHub hardware repo''s datasheets folder; no source states "LPC4330" in prose. All other fields and sentences were confirmed against the cited maker/press sources and left as-is.'
last_modified_date: '2026-09-07'
---

The rad1o is a wearable software-defined radio transceiver built by members of Chaos Computer Club Munich as the official conference badge of Chaos Communication Camp 2015. Around 4,500 units were manufactured and given free to camp attendees. Built around an NXP LPC4330 (ARM Cortex-M4) microcontroller paired with a wideband RF transceiver, it tunes roughly 50 MHz to 4000 MHz and is software-compatible with the open-source HackRF platform, letting owners boot it either into HackRF-compatible firmware or into custom rad1o firmware that exercises the badge's own peripherals.

Physically it carries a small color Nokia 6100 LCD (130x130 pixels) and a joystick for navigation, features it inherited from CCC's earlier r0ket badge (Chaos Communication Camp 2011). It runs on an onboard rechargeable LiPo battery charged over USB, and connects to a computer over USB for firmware updates and for use with SDR software such as GNU Radio.

## Make your own

The hardware (schematics and board files, in Eagle CAD format) and firmware are published under GPL-2.0 in the `rad1o` GitHub organization, starting with the [hardware repo](https://github.com/rad1o/hardware). The project's own wiki at rad1o.badge.events.ccc.de documents firmware flashing and development setup for anyone building or modifying one.
