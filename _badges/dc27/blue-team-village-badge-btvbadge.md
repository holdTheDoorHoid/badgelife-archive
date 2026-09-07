---
title: Blue Team Village Badge (btvbadge)
id: dc27-blue-team-village-badge-btvbadge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: fyrm
  url: https://github.com/fyrm
summary: A Raspberry Pi-based programmable badge distributed at DEF CON 27's Blue Team Village, running Raspbian in text mode with a 320x240 display and a WiFi "badgenet" for inter-badge communication.
functions: Boots into a Raspbian text-mode console with a D-pad (mapped to arrow keys) and A/B buttons (tab/enter) for navigation. Auto-joins a "badgenet" WiFi network for inter-badge messaging and official announcements. Supports a shell-script addon system (drop-in scripts under /badge/addons/) for extra modes, including a suggested honeypot-monitoring addon with LED feedback.
look:
  colors: []
  shape: null
  themes:
  - village badge
  - security
tech:
  mcu: Raspberry Pi (Raspbian)
  leds: null
  display: 320x240 color LCD, 40x17 text mode
  connectivity:
  - wifi
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Distributed to attendees of Blue Team Village at DEF CON 27 (2019).
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/fyrm/btvbadge
  eda_tool: null
  license: GPL-3.0 (some components CC BY-SA 3.0)
  notes: The GitHub repo publishes the badge's OS setup, addon scripts, and a disk image (btvbadge-20191023.img.bz2, referenced as hosted on fyrmassociates.com); no PCB/hardware design files are included since the badge is built around a stock Raspberry Pi.
links:
- label: github.com/fyrm/btvbadge
  url: https://github.com/fyrm/btvbadge
  kind: repo
images: []
contact: {}
notes:
- Found via GitHub search; description/year not confirmed due to GitHub API rate-limit before repo could be inspected further.
status: released
sources:
- kind: url
  url: https://github.com/fyrm/btvbadge
  title: Blue Team Village Badge (btvbadge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: villages-early: DEF CON village and DC-group badges, DEF CON 24-29 (2016-2021)); event read as ''Blue Team Village, DEF CON (year unconfirmed - BTV launched ~DEF CON 26/2018)''.'
- kind: url
  url: https://github.com/fyrm/btvbadge
  title: 'GitHub - fyrm/btvbadge: DEF CON 27 Blue Team Village badge'
  accessed: '2026-09-07'
  note: 'README and repo social-preview metadata confirm this is the DEF CON 27 (2019) Blue Team Village badge (not DC26/2018); it is Raspberry Pi/Raspbian-based, with a 320x240 display, badgenet WiFi, D-pad/A/B input, a shell-script addon system, and GPLv3/CC BY-SA 3.0 licensing. No PCB design files or photos of the physical badge are present in the repo.'
- kind: url
  url: https://fyrmassociates.com/tools/
  title: FYRM Associates - Tools
  accessed: '2026-09-07'
  note: Checked for a listing or photo of the btvbadge; the page covers FYRM's other security tools and does not mention the badge or link an image/disk-download page for it.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Event corrected from dc26 (2018) to dc27 (2019): the repo''s own README and GitHub social-preview image both title it "DEF CON 27 Blue Team Village Badge." No photo of the physical badge, no price/quantity, and no PCB/BOM files were found in the repo or on the maker''s site, so those fields are left empty. tech.mcu is a Raspberry Pi board (running Raspbian), not a typical badge MCU, and tech.leds/battery/sao_version could not be confirmed from available sources.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc26/blue-team-village-badge-btvbadge/
---

The Blue Team Village badge (btvbadge) was the programmable badge given to attendees of DEF CON 27's Blue Team Village in 2019, built by the security research group fyrm. Rather than a custom PCB, it runs Raspbian on a Raspberry Pi in text-console mode, driving a 320x240 color display with room for 40x17 characters, navigated with a D-pad and A/B buttons mirroring arrow keys, tab, and enter.

On boot the badge automatically joins a shared "badgenet" WiFi network, which was used for inter-badge communication among attendees and for official village announcements. Its functionality was meant to be extended: addons are plain shell scripts dropped into `/badge/addons/`, named `addon_name.sh`, which then appear in the badge's on-screen addon menu. The README suggests possibilities such as a honeypot-monitoring addon with LED feedback and custom display modes, and notes i2c support for SAO ("Shitty Add-On") hardware expansion, though no SAO header specification or hardware files are published.

The project's GitHub repository publishes the OS configuration and addon scripts, along with a disk image (`btvbadge-20191023.img.bz2`) referenced as hosted on fyrmassociates.com, under GPLv3 with some components under CC BY-SA 3.0. No photos of the assembled badge, pricing, or production-quantity information were found in the available sources.
