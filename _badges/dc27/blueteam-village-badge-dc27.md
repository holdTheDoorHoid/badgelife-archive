---
title: Blueteam Village Badge (DC27)
id: dc27-blueteam-village-badge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Jeff Yestrumskas
  url: https://jeffyestrumskas.com/projects/defcon-27-blue-team-village-badge/
summary: 'The official DEF CON 27 Blue Team Village badge: a wearable, self-contained WiFi honeypot built around a Raspberry Pi Zero W.'
functions: 'Runs Raspbian Linux with the honeypots Cowrie (SSH) and HoneyDB (multiple services) to attract and log attacker connections, uploading captured data; by default joins a shared "badgenet" WiFi network for official BTV announcements and badge-to-badge pairing/communication; interface is a shell-script-driven menu on the screen; supports user-written shell-script addons for custom features (honeypot monitoring, LED control, networking) and can be extended via an i2c SAO header.'
look:
  colors: [black]
  shape: hexagon
  themes: [security, retro computer, sci-fi]
tech:
  mcu: none
  leds:
    count: 8
    type: discrete
    note: 'SMD front-facing LEDs driven by a 74HC595 shift register'
  display: 2.2" TFT (320x240)
  connectivity: [wifi, i2c]
  inputs:
  - buttons (4-way d-pad, "A"/"B", plus 3 control buttons)
  battery: LiPo 4400 mAh with charging circuit and TPS61090 boost converter
  sao_version: null
  sao_ports: 1
get_one:
  price: ''
  price_usd: null
  quantity: '250'
  availability: unknown
  distribution: [village]
  where: 'Given to Blue Team Village attendees at DEF CON 27 (2019); exact distribution/price terms not documented on the maker''s pages.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/fyrm/btvbadge
  eda_tool: null
  license: 'GPLv3 (some parts CC BY-SA 3.0), per the GitHub repo'
  notes: 'The GitHub repo (github.com/fyrm/btvbadge) holds the addon shell scripts, documentation, and a flashable disk image (btvbadge-20191023.img.bz2); it does not appear to include PCB/schematic/Gerber files.'
links:
- label: fyrmassociates.com/blog/2019/06/08/defcon-27-blue-team-village-badge
  url: https://fyrmassociates.com/blog/2019/06/08/defcon-27-blue-team-village-badge/
  kind: website
- label: DEF CON 27 Blue Team Village Badge Wrap Up
  url: https://fyrmassociates.com/blog/2019/10/10/defcon-27-blue-team-village-badge-wrapup/
  kind: website
- label: 'GitHub: fyrm/btvbadge'
  url: https://github.com/fyrm/btvbadge
  kind: repo
- label: Jeff Yestrumskas project page
  url: https://jeffyestrumskas.com/projects/defcon-27-blue-team-village-badge/
  kind: website
- label: 'Hackaday: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
images:
- file: assets/images/badges/dc27/blueteam-village-badge-dc27/5887a8f997.jpg
  source: "https://fyrmassociates.com/blog/2019/06/08/defcon-27-blue-team-village-badge/"
  credit: "Jeff Yestrumskas / FYRM Associates"
  caption: "Final version of the DEF CON 27 Blue Team Village badge, front side"
- file: assets/images/badges/dc27/blueteam-village-badge-dc27/f46c2a5241.jpg
  source: "https://fyrmassociates.com/blog/2019/10/10/defcon-27-blue-team-village-badge-wrapup/"
  credit: "Jeff Yestrumskas / FYRM Associates"
  caption: "Back of the DEF CON 27 Blue Team Village badge"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://fyrmassociates.com/blog/2019/06/08/defcon-27-blue-team-village-badge/
  title: Blueteam Village Badge (DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://fyrmassociates.com/blog/2019/10/10/defcon-27-blue-team-village-badge-wrapup/
  title: DEF CON 27 Blue Team Village Badge Wrap Up
  accessed: '2026-09-07'
  note: 'Production details: 25 min assembly per badge, luggage logistics, ~75 badges'' data pulled; confirms GPLv3/CC BY-SA 3.0 licensing and github.com/fyrm/btvbadge repo.'
- kind: url
  url: https://github.com/fyrm/btvbadge
  title: 'GitHub - fyrm/btvbadge: DEF CON 27 Blue Team Village badge'
  accessed: '2026-09-07'
  note: 'Confirms i2c SAO header, license (GPLv3 + CC BY-SA 3.0), and that the repo holds addon scripts/disk image rather than hardware design files.'
- kind: url
  url: https://jeffyestrumskas.com/projects/defcon-27-blue-team-village-badge/
  title: 'DEF CON 27 Blue Team Village Electronic Conference Badge – Jeff Yestrumskas'
  accessed: '2026-09-07'
  note: 'Maker''s own project page; confirms badge granted access to the village but gives no price/distribution mechanics.'
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: 'Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27 | Hackaday'
  accessed: '2026-09-07'
  note: 'Confirms quantity produced (250) and creator.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Price and exact distribution terms (sold vs. included with village badge/ticket) were not stated on any source found; "village" distribution and empty price are inferred from the maker''s statement that the badge "granted badgeholders access to an event." No PCB/schematic/Gerber files were found published, only firmware/addon scripts and a disk image, so make_your_own.open_source is set to partial rather than yes.'
last_modified_date: '2026-09-07'
---

The DEF CON 27 Blue Team Village badge, designed by Jeff Yestrumskas of FYRM Associates, is a wearable, self-contained WiFi honeypot rather than a typical blinky badge. Built around a Raspberry Pi Zero W with a 2.2" color TFT screen, eight shift-register-driven LEDs, a nine-button control pad, and a 4400 mAh battery good for over 26 hours, each of the 250 badges ran Raspbian Linux with the Cowrie SSH honeypot and HoneyDB running in the background, quietly collecting and uploading data on anyone who tried to attack it. Badges joined a shared "badgenet" WiFi network by default, which carried official Blue Team Village announcements and let badges pair and communicate with each other. The hexagonal PCB's silkscreen art was inspired by Arthur C. Clarke's "Childhood's End," coordinating with DEF CON 27's retrofuturism theme.

Assembling and packaging the run of badges reportedly took about 25 minutes each, with batteries installed separately on-site in Las Vegas; the finished badges were carried to the conference across five people's carry-on luggage. A shell-script menu system, plus documented support for building custom shell-script "addons," made the badge hackable well beyond its stock honeypot function, and it exposed an i2c-based SAO header for hardware add-ons too.

## Make your own

The badge's addon scripts, setup documentation, and a flashable Raspberry Pi disk image (`btvbadge-20191023.img.bz2`) are published at [github.com/fyrm/btvbadge](https://github.com/fyrm/btvbadge) under GPLv3 (with some parts under CC BY-SA 3.0). No PCB schematics, layout, or Gerber files were found published, so the hardware itself is not reproducible from what's public — only the software/firmware side is open.
