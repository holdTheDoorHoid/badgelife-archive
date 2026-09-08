---
title: BruCON 0x10 Badge (2024)
id: brucon-2024-brucon-0x10-badge-2024
layout: badge
parent: BruCON 0x10
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: brucon-2024
year: 2024
makers:
- name: Joris Witteman (curious.supplies)
  role: hardware/software
- name: Tom Clement (curious.supplies)
  role: software
- name: Nikolett S. (ankhaneko.art)
  role: PCB art
- name: Norbert (Allnet China)
  role: production/sourcing
summary: The official electronic badge for BruCON 0x10 (2024), an ESP32-based, MicroPython-driven badge with a screen, six buttons, and an app/game store.
functions: Runs a launcher OS with installable apps and games (a beer-brewing themed BruCON Game, a tilt-based Ko-Lab Game, three CTF challenges, and community-built apps such as a custom DOOM engine and a snake game). Two badges can link over an audio-jack cable for badge-to-badge play, and the badge exposes a USB serial console at 115200 baud for flashing and debugging.
look:
  colors: []
  shape: null
  themes:
  - security
  - ctf
  - console
tech:
  mcu: ESP32
  leds: null
  display: LED screen
  connectivity:
  - usb
  - uart
  - audio
  battery: 18650 Li-ion, USB-C charging
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: Distributed to BruCON 0x10 (2024) attendees; not sold as a separate product.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/ko-lab/brucon-0x10-apps
  eda_tool: null
links:
- label: github.com/Brucon0X10/Badge
  url: https://github.com/Brucon0X10/Badge
  kind: repo
- label: github.com/ko-lab/brucon-0x10-apps
  url: https://github.com/ko-lab/brucon-0x10-apps
  kind: repo
- label: teodor-trotea.com/projects/brucon-doom
  url: https://teodor-trotea.com/projects/brucon-doom
  kind: website
images:
- file: assets/images/badges/brucon-2024/brucon-0x10-badge-2024/80d003b5dd.jpg
  source: "https://github.com/Brucon0X10/Badge"
  credit: "Brucon0X10/Badge repo"
  caption: "The BruCON 0x10 badge PCB with screen and button controls"
contact: {}
notes:
- Official BruCON 0x10 (2024) badge with embedded screen, 6-button controls, USB-C/18650 battery power, and a launcher OS with apps and games. Found by the event-year sweep, task con-brucon.
- The archive sweep's title matched the maker's own naming ("Brucon 0x10 Badge Documentation" on GitHub); no change made.
status: released
sources:
- kind: url
  url: https://github.com/Brucon0X10/Badge
  title: BruCON 0x10 Badge (2024)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-brucon); event read as ''BruCON 2024''.'
- kind: url
  url: https://github.com/Brucon0X10/Badge/blob/main/Readme.md
  title: Brucon 0x10 Badge Documentation (Readme)
  accessed: '2026-09-08'
  note: Maker credits (hardware/software/PCB art/production), battery, buttons, connectivity, audio-jack link-play, and serial baud rate.
- kind: url
  url: https://github.com/ko-lab/brucon-0x10-apps
  title: ko-lab/brucon-0x10-apps
  accessed: '2026-09-08'
  note: Confirms MicroPython/ESP32 hardware target, app store install flow, and bootloader button combo; source of app repo (games/CTF apps).
- kind: url
  url: https://teodor-trotea.com/projects/brucon-doom
  title: DOOM on Brucon Badge - Teodor Trotea
  accessed: '2026-09-08'
  note: Community-built custom DOOM engine for the badge; confirms event/year and describes it as limited RAM/display hardware.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: The maker's own repo and README confirm the badge's existence, makers, and core features (buttons, battery, audio-jack link, serial baud). No page states the exact MCU part number, display size/type, LED presence, price, or production quantity — the ko-lab apps repo describes the firmware as MicroPython on ESP32 but does not name the specific module (e.g. ESP32-S3 vs plain ESP32), so tech.mcu is left as the general family. No official design files (KiCad/gerbers/BOM) were found; only the firmware/apps repo is open.
last_modified_date: '2026-09-08'
---

The BruCON 0x10 badge was the official electronic badge given to attendees of BruCON 0x10, the 2024 edition of the Belgian security and hacker conference. It was built by Joris Witteman and Tom Clement of curious.supplies (hardware and software), with PCB artwork by Nikolett S. (ankhaneko.art) and production/sourcing handled by Norbert of Allnet China. The badge runs on an ESP32-family microcontroller with MicroPython firmware, has a small screen, six front buttons (four directional plus A/B), and is powered by an 18650 lithium-ion cell with USB-C charging.

Out of the box the badge ships with a launcher and an app store: a beer-brewing themed "BruCON Game," a tilt-based "Ko-Lab Game" from Ko-Lab makerspace, three built-in CTF challenges, and nickname customization. A 3.5mm audio jack lets two badges link together for badge-to-badge play, and the badge exposes a 115200-baud USB serial console for flashing new apps. The community extended the platform after the con — Ko-Lab published an apps repository with additional games (including an in-progress snake game) and a Python flashing tool, and developer Teodor Trotea built a from-scratch raycasting DOOM engine scaled to the badge's constrained RAM and display.

No source found states the exact MCU part number, display type/size, LED count, unit price, or production quantity, so those fields are left empty rather than guessed. No hardware design files (schematics, KiCad project, gerbers, or BOM) were found publicly; only the firmware/apps side of the project is open source.
