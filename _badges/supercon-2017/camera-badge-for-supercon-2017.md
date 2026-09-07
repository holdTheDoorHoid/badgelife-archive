---
title: Camera Badge for Supercon 2017
id: supercon-2017-camera-badge-for-supercon-2017
layout: badge
parent: Supercon 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2017
year: 2017
makers:
- name: Mike Harrison
  url: https://hackaday.io/mike-harrison
  role: designer
- name: Mike Szczys
  url: https://hackaday.io/mike-szczys
  role: team member
- name: Brian Benchoff
  url: https://hackaday.io/benchoff
  role: team member
summary: 'The official badge of the 2017 Hackaday Superconference: a hackable camera badge with a still/video camera module, color OLED display, and SD card slot, assembled by MacroFab with components donated by Microchip.'
functions: 'Captures still images and short video with the onboard camera; plays back encoded content from the microSD card; runs custom user firmware loaded via a bootloader; includes built-in puzzles and cryptographic challenges for attendees.'
look:
  colors: []
  shape: null
  themes:
  - camera
  - ctf
  - puzzle
tech:
  mcu: PIC32MX170F256D
  leds: null
  display: 128x128 color OLED
  connectivity: []
  battery: 2x AA
  sao_version: null
get_one:
  price: $99
  price_usd: 99
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  - free_drop
  where: Given to all 2017 Supercon attendees; extras were later sold on Tindie (hackadaystore) but that listing is now unavailable.
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/27427-camera-badge-for-supercon-2017
  url: https://hackaday.io/project/27427-camera-badge-for-supercon-2017
  kind: hackaday
- label: Tindie listing (hackadaystore) - 2017 Hackaday Superconference Badge
  url: https://www.tindie.com/products/hackadaystore/2017-hackaday-superconference-badge/
  kind: store
images:
- file: assets/images/badges/supercon-2017/camera-badge-for-supercon-2017/9e884df27e.jpg
  source: "https://hackaday.io/project/27427-camera-badge-for-supercon-2017"
  credit: "Mike Harrison"
  caption: "The Supercon 2017 camera badge"
- file: assets/images/badges/supercon-2017/camera-badge-for-supercon-2017/1915da1822.jpg
  source: "https://hackaday.io/project/27427-camera-badge-for-supercon-2017"
  credit: "Mike Harrison"
  caption: "Camera badge board detail"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/27427-camera-badge-for-supercon-2017
  title: Camera Badge for Supercon 2017
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''Supercon 2017''.'
- kind: url
  url: https://hackaday.io/project/27427-camera-badge-for-supercon-2017
  title: Camera Badge for Supercon 2017
  accessed: '2026-09-07'
  note: 'Hackaday.io project page: maker (Mike Harrison, team Mike Szczys/Benchoff), MacroFab assembly, Microchip component donation, PIC32MX170F256D MCU, OV9650 camera sensor, 128x128 OLED, microSD, accelerometer, 2xAA power, SD-card bootloader, firmware/schematics/DXF files in the project files section.'
- kind: url
  url: https://www.tindie.com/products/hackadaystore/2017-hackaday-superconference-badge/
  title: 2017 Hackaday Superconference Badge - hackadaystore - Tindie
  accessed: '2026-09-07'
  note: 'Tindie listing: $99 price, currently unavailable ("seller is taking a break"), package included one assembled badge plus a 2GB microSD card with firmware; lists SRAM, LED flash, six buttons, and prototyping headers not mentioned on the Hackaday.io page.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Verified against the Hackaday.io project page and the Tindie storefront directly. The Hackaday.io page itself only says "128x128 OLED display" without color/monochrome and mentions monochrome only as a video-capture mode, not the panel; the Tindie listing explicitly calls it a "128x128 color OLED display", and the badge photo saved from the project page shows a color (blue/purple) image on the screen, so color is corroborated rather than just asserted by one source. Confirmed on Hackaday.io: firmware (MPLABX projects, incl. a puzzle build and the bootloader) and hardware files (PDF schematic, Gerbers, DXF board outline) are both present in the project''s Files section, so make_your_own.open_source is set to yes; no direct per-file URL was found (Hackaday.io does not expose a simple link to that section) so hardware_url/firmware_url stay empty, and no license is stated anywhere on the page. "Everyone who goes to Supercon this year will get one of these badges" and "a limited number of the extra badges are available on Tindie" are both direct statements on the Hackaday.io page, confirming the free-to-attendees plus limited paid-extras distribution. 10+ hour battery life is from the maker''s own comment on the project page. tech.leds not itemized by sources beyond "illuminator LED" / "LED flash" for the camera, so left null. Quantity made not stated by sources.'
last_modified_date: '2026-09-07'
---

The Camera Badge was the official electronic badge of the 2017 Hackaday Superconference in Pasadena, designed by Mike Harrison (mikeselectricstuff) with Mike Szczys and Brian Benchoff, assembled by MacroFab with microcontrollers donated by Microchip. Built around a PIC32MX170F256D running at 48MHz, it pairs an OV9650 camera sensor with a 128x128 OLED display, a microSD card slot for storage and firmware updates, an onboard accelerometer, and an illuminator LED for low-light shots. It runs on two AA batteries for over ten hours of use and shipped with a bootloader so attendees could load their own firmware from the SD card.

Every 2017 Supercon attendee received one as their conference badge, and it was built to be more than a picture-taker: it included built-in puzzles and cryptographic challenges to work through during the event, encouraging hands-on hacking rather than passive wear. A limited run of extra assembled badges (bundled with a 2GB microSD card preloaded with firmware) was later sold through the Hackaday store on Tindie for $99; that listing is no longer active, with the seller "taking a break."

Full design materials, including MPLAB X firmware projects, bootloader source, PDF schematics, and a DXF board layout, were shared in the project's Hackaday.io files section, making the badge one of the more thoroughly documented Supercon badges of its era.
