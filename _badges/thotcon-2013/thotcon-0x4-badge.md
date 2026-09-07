---
title: ThotCon 0x4 Badge
id: thotcon-2013-thotcon-0x4-badge
layout: badge
parent: Thotcon 2013
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: thotcon-2013
year: 2013
makers:
- name: rudy
  url: https://hackaday.io/rudy
series: null
summary: An AVR-based, Arduino-compatible conference badge for THOTCON 0x4 with an LED raster-scan display and an 802.15.4 radio.
functions: 'Drives an LED raster-scan array for visual output; carries an 802.15.4 frame radio (the chip supports ZigBee-style stacks). Attendees later repurposed the badge firmware to turn it into an 802.15.4 sniffer.'
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
  - hardware tool
tech:
  mcu: ATmega128RFA1
  leds:
    count: null
    type: LED raster scan array
    note: 'Uses an LED array driven in a raster-scan pattern rather than individually addressable LEDs; exact LED count not stated in sources.'
  display: LED raster scan array
  connectivity:
  - sub-ghz
  - zigbee
  inputs: []
  power: null
  battery: null
  sao_version: none
  sao_ports: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  availability_note: ''
  distribution:
  - village
  where: 'Distributed at THOTCON 0x4 (2013) in Chicago as a limited-production-run conference badge; the project team called itself Workshop88 (a Chicago-area hackerspace).'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Workshop88/thotcon0x4
  firmware_url: https://github.com/Workshop88/thotcon0x4
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: null
  fab_url: null
  notes: 'The GitHub repo (Workshop88/thotcon0x4) holds firmware sketches, bootloader hex files, PCB layout files, and design-research notes (radio chipset/protocol comparisons), but no clearly labeled schematic/Gerber export or license file was found.'
links:
- label: hackaday.io/project/981-thotcon-0x4-badge
  url: https://hackaday.io/project/981-thotcon-0x4-badge
  kind: hackaday
- label: Workshop88/thotcon0x4 (GitHub)
  url: https://github.com/Workshop88/thotcon0x4
  kind: repo
images:
- file: assets/images/badges/thotcon-2013/thotcon-0x4-badge/bb818613b7.jpg
  source: "https://hackaday.io/project/981-thotcon-0x4-badge"
  credit: "rudy"
  caption: "THOTCON 0x4 badge, AVR-based with LED raster scan array"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/981-thotcon-0x4-badge
  title: ThotCon 0x4 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''ThotCon 0x4''.'
- kind: url
  url: https://hackaday.io/project/981-thotcon-0x4-badge
  title: THOTCON 0x4 Badge - Hackaday.io
  accessed: '2026-09-07'
  note: 'Confirmed maker (rudy), description ("AVR based, arduino compatible badge containing an LED raster scan array and a 802.15.4 frame radio"), that it was hacked into an 802.15.4 sniffer, and og:image photo of the badge.'
- kind: url
  url: https://github.com/Workshop88/thotcon0x4
  title: Workshop88/thotcon0x4
  accessed: '2026-09-07'
  note: 'Repo contents confirm ATmega128RFA1-based firmware (ATmegaBOOT_168_atmega128rfa1.hex), PCB layout folder, and radio/protocol research notes (DesignNotes.md/html); no explicit license or Gerber export found.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s Hackaday project page and GitHub repo (both from the maker, "rudy"/Workshop88) confirm the core facts, but neither states exact LED count, battery/power source, price, or quantity made, so those fields are left empty. The repo''s README just says "Thotcon 0x4 Badges" with no further write-up. A separate, unrelated project exists for a later THOTCON 0x8 (2017) badge by a different maker (Gigawatts) — see other_items_found, not this entry.'
last_modified_date: '2026-09-07'
---

The THOTCON 0x4 badge was a limited-production conference badge handed out at THOTCON 0x4, the 2013 edition of the Chicago hacker conference, built by a team going by "rudy" on Hackaday.io and associated with Workshop88, a Chicago-area hackerspace. It runs on an AVR-based, Arduino-compatible microcontroller (an ATmega128RFA1, based on the bootloader files in the project's repo) and drives an LED array in a raster-scan pattern for its visual display, rather than individually addressable LEDs.

The badge's other headline feature is its onboard 802.15.4 radio, the same frame-layer radio used by ZigBee and similar low-power wireless protocols. According to the project's Hackaday.io page, at least one attendee reverse-engineered or reprogrammed the badge to work as an 802.15.4 sniffer, turning the conference badge into an ad hoc RF-analysis tool.

## Make your own

Firmware and supporting files are published in the `Workshop88/thotcon0x4` GitHub repository, including several badge firmware variants (animation demos, beacon/check-in modes, a signal meter, a battery test), AVR bootloader hex files for the ATmega128RFA1/Zigduino, a PCB layout folder, and a set of design-research notes comparing radio chipsets and low-power networking protocols (802.15.4, ZigBee, 6LowPan, SimpliciTI, and others) that the team considered while designing the badge. No explicit open-source license or a single consolidated schematic/Gerber export was found in the repo, so build-from-scratch steps beyond loading the published firmware onto compatible hardware are not fully documented in what's public.
