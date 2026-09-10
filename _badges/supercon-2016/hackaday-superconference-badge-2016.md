---
title: Hackaday Superconference Badge 2016
id: supercon-2016-hackaday-superconference-badge-2016
layout: badge
parent: Hackaday Supercon 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2016
year: 2016
makers:
- name: Voja Antonic
  url: https://hackaday.io/vojaantonic
  role: designer
- name: Dusan Petrovic
  role: designer
summary: 'The official badge for Hackaday Superconference II (Pasadena, Nov 2016): an 8x16 surface-mount LED matrix badge with buttons, an accelerometer, and IR badge-to-badge communication.'
functions: Scrolling-message kiosk mode, an IR-based crypto/puzzle challenge between badges, badge-to-badge IR communication, and a hackable C firmware framework via a drag-and-drop USB bootloader.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - puzzle
  - ctf
tech:
  mcu: PIC18F25K50
  leds:
    count: 128
    type: discrete
    note: 8x16 matrix of surface-mount LEDs, driven with a 74HC138 3-to-8 decoder, behind an acrylic diffuser bezel
  display: LED matrix 8x16
  connectivity:
  - ir
  battery: 2x AA
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to attendees of Hackaday Superconference II, Pasadena, November 5-6, 2016; not sold.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Hack-a-Day/2016-Hackaday-SuperConference-Badge-Hacking
  firmware_url: https://github.com/perkyguy/XPRESS-Bootloader/tree/HaDSuperConference2016
  eda_tool: null
links:
- label: hackaday.com/2016/09/28/new-supercon-badge-is-40-lighter-and-a-work-of-art
  url: https://hackaday.com/2016/09/28/new-supercon-badge-is-40-lighter-and-a-work-of-art/
  kind: article
  archived: https://web.archive.org/web/20260509232350/https://hackaday.com/2016/09/28/new-supercon-badge-is-40-lighter-and-a-work-of-art/
- label: 'Hackaday.io: Supercon II Badge'
  url: https://hackaday.io/project/16401
  kind: hackaday
- label: 'GitHub: 2016 Hackaday SuperConference Badge Hacking'
  url: https://github.com/Hack-a-Day/2016-Hackaday-SuperConference-Badge-Hacking
  kind: repo
  archived: https://web.archive.org/web/20251022125835/https://github.com/Hack-a-Day/2016-Hackaday-SuperConference-Badge-Hacking
- label: 'GitHub: XPRESS-Bootloader (HaDSuperConference2016 branch)'
  url: https://github.com/perkyguy/XPRESS-Bootloader/tree/HaDSuperConference2016
  kind: repo
images:
- file: assets/images/badges/supercon-2016/hackaday-superconference-badge-2016/d699c1d1b4.jpg
  source: https://hackaday.com/2016/09/28/new-supercon-badge-is-40-lighter-and-a-work-of-art/
  credit: Hackaday
  caption: Front of the 2016 Hackaday Superconference badge, showing the 8x16 LED matrix
  archived: https://web.archive.org/web/20260509232350/https://hackaday.com/2016/09/28/new-supercon-badge-is-40-lighter-and-a-work-of-art/
- file: assets/images/badges/supercon-2016/hackaday-superconference-badge-2016/f818d7b807.jpg
  source: https://hackaday.com/2016/09/28/new-supercon-badge-is-40-lighter-and-a-work-of-art/
  credit: Hackaday
  caption: Back of the 2016 Hackaday Superconference badge, showing the battery holders
  archived: https://web.archive.org/web/20260509232350/https://hackaday.com/2016/09/28/new-supercon-badge-is-40-lighter-and-a-work-of-art/
contact: {}
notes:
- The Hackaday.io project page for this badge is titled "Supercon II Badge" (Hackaday Superconference II, Nov 2016), so both names refer to the same event and item.
- 'Sources disagree on battery type: the Hackaday.com article says two AAA batteries, while the Hackaday.io project page says two AA batteries in custom-mounted holders; recorded as AA per the project page, the more detailed source, but this is unresolved.'
- The GitHub hardware repo (2016-Hackaday-SuperConference-Badge-Hacking) contains firmware/framework source, a schematic image, and a license file, but no Gerbers or BOM in the repo itself; a separate BOM was said to be shared via Google Sheets, not independently verified this session, so open_source is recorded as partial rather than yes.
status: released
sources:
- kind: url
  url: https://hackaday.com/2016/09/28/new-supercon-badge-is-40-lighter-and-a-work-of-art/
  title: Hackaday Superconference Badge 2016
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''Hackaday Superconference 2016''.'
  archived: https://web.archive.org/web/20260509232350/https://hackaday.com/2016/09/28/new-supercon-badge-is-40-lighter-and-a-work-of-art/
- kind: url
  url: https://hackaday.io/project/16401
  title: Supercon II Badge
  accessed: '2026-09-07'
  note: Confirmed maker team (Voja Antonic, Dusan Petrovic), chip (PIC18F25K50), LED count, accelerometer, IR link, battery type, and open-source hardware/firmware/BOM links.
- kind: url
  url: https://github.com/Hack-a-Day/2016-Hackaday-SuperConference-Badge-Hacking
  title: 2016-Hackaday-SuperConference-Badge-Hacking
  accessed: '2026-09-07'
  note: 'Confirmed repo contents: firmware/hacking framework, schematic image, license file; no Gerbers or BOM in-repo.'
  archived: https://web.archive.org/web/20251022125835/https://github.com/Hack-a-Day/2016-Hackaday-SuperConference-Badge-Hacking
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price and quantity made were not stated by any source and are left empty. Battery type (AA vs AAA) disagrees between the two primary sources; see notes above. No Gerbers/BOM were found hosted directly in the linked repos.
last_modified_date: '2026-09-07'
---

The 2016 Hackaday Superconference badge — officially "Supercon II Badge" on its Hackaday.io project page — was designed by Voja Antonic (creator of the Galaksija computer) with Dusan Petrovic, and given to attendees of Hackaday Superconference II in Pasadena, California on November 5-6, 2016. It was built around a PIC18F25K50 microcontroller and centers on an 8x16 matrix of 128 discrete surface-mount LEDs behind an acrylic diffuser, driven through a 74HC138 decoder. Four user buttons (plus reset and a wake-from-sleep button), a three-axis accelerometer, and a 940 nm IR transmitter/receiver pair round out the hardware, all powered by two AA batteries in edge-mounted holders. At 52 grams it was billed as roughly 40% lighter than the previous year's Hackaday badge.

Beyond showing scrolling text and simple animations, the badge doubled as a puzzle platform: it could exchange messages with other badges over IR, and Hackaday built a hidden IR-based crypto challenge into the con for attendees to find and solve. A Microchip-built USB bootloader let the badge appear as a mass-storage drive, so attendees could reflash it by dragging a new .hex file onto it without needing separate programming hardware.

## Make your own

Hackaday published a hacking framework for the badge on GitHub (`Hack-a-Day/2016-Hackaday-SuperConference-Badge-Hacking`), including a C-language SDK with kernel functions for the display, buttons, delays, and accelerometer, a compiled example .hex, and a schematic image, along with a fork of the XPRESS bootloader used to flash it. The repo does not include Gerbers or a bill of materials directly; a BOM was said to be shared separately via Google Sheets at the time, but that has not been independently verified.
