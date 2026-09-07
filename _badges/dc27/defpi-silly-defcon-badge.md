---
title: defpi — silly defcon badge
id: dc27-defpi-silly-defcon-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Hacksore
  url: https://github.com/Hacksore
summary: 'A homemade, tongue-in-cheek "badge" for DEF CON 27 built around a full Raspberry Pi rather than a small MCU.'
functions: 'Runs as a portable Wi-Fi access point with a touchscreen kiosk web app; scans the local network for connected clients and displays the results on-screen.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - security
tech:
  mcu: 'Raspberry Pi 3 A+'
  leds: null
  display: '3.5" ILI9486/VMP400 LCD'
  connectivity:
  - wifi
  battery: 'Anker PowerCore II Slim 10000 (USB power bank)'
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: not_released
  distribution: []
  where: 'Never distributed; a one-off personal build the maker carried at DEF CON 27.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Hacksore/defpi
  firmware_url: https://github.com/Hacksore/defpi
  eda_tool: null
links:
- label: github.com/Hacksore/defpi
  url: https://github.com/Hacksore/defpi
  kind: repo
images:
  - file: assets/images/badges/dc27/defpi-silly-defcon-badge/49a8ba1050.jpg
    source: "https://github.com/Hacksore/defpi"
    credit: "Hacksore"
    caption: "The defpi badge/handheld built around a Raspberry Pi 3 A+ and 3.5-inch display"
  - file: assets/images/badges/dc27/defpi-silly-defcon-badge/03853ab76c.jpg
    source: "https://github.com/Hacksore/defpi"
    credit: "Hacksore"
    caption: "defpi's kiosk-mode web interface showing network scan results"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Hacksore/defpi
  title: defpi — silly defcon badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/Hacksore/defpi
  title: 'GitHub - Hacksore/defpi: A silly badge for defcon 2019 built for a Raspberry PI'
  accessed: '2026-09-07'
  note: 'README confirms it is a DIY badge for DEF CON 2019 (DC27), built on a Raspberry Pi 3 A+ with a 3.5" ILI9486/VMP400 display and an Anker PowerCore II Slim 10000 power bank; runs Chromium in kiosk mode over a Node/Express + React stack, hostapd as an access point, and arp-scan for LAN client scanning. Source of the two hardware photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Single-source entry: the GitHub repo README is the only source found describing the build (a web search surfaced only the maker''s later, unrelated e-ink badge project and general DC27 badge coverage that does not mention defpi). No evidence it was sold, given away, or made in more than one unit — this reads as a personal one-off build, so availability is set to not_released/status released (the maker had and used it) rather than a produced/distributed item. No LED info, colors, or SAO header found; none is implied by the hardware described.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/defpi-silly-defcon-badge/
---

defpi is a homemade, mostly-joking "badge" that Hacksore built for DEF CON 27 (2019) out of a full Raspberry Pi 3 A+ rather than a small microcontroller — a deliberately oversized take on the badgelife tradition of wearable electronics. Instead of blinking LEDs, it drives a 3.5" ILI9486/VMP400 touchscreen in kiosk mode through Chromium, showing a React web app served by a local Node/Express backend, and is powered off an Anker PowerCore II Slim 10000 battery pack.

Functionally it doubles as a small network tool: `hostapd` turns the Pi into its own Wi-Fi access point, and `arp-scan` sweeps the local network for connected clients, with results shown live on the touchscreen interface. There is no indication it was sold, kitted, or distributed to anyone else — it appears to be a single, personal build the maker carried around the con, documented afterward on GitHub with the hardware/software bill of materials and two photos of the finished unit and its scanning screen.

The project is fully open in the sense that its glue code (the web app, server, and README describing the off-the-shelf hardware) is public on GitHub, though there are no PCB design files since the "hardware" is stock Raspberry Pi and display modules rather than a custom board.
