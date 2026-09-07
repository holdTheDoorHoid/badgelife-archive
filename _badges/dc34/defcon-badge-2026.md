---
title: defcon_badge_2026
id: dc34-defcon-badge-2026
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: '0x1ea7bee5'
  url: https://github.com/0x1ea7bee5
summary: A self-designed, unofficial DEF CON 34 (2026) hardware badge built around an ESP32-C5, still in active development as of mid-2026 with no public release yet.
functions: 'Wi-Fi packet scanning and experiments in Wi-Fi-based direction finding/tracking (channel-data matrix construction and eigenvector decomposition, i.e. a MUSIC-style angle-of-arrival approach), plus a joystick input and a small stepper-motor-driven mechanism (A4988 driver, limit switch).'
look:
  colors: []
  shape: null
  themes:
  - security
  - radio
tech:
  mcu: ESP32-C5
  leds: null
  display: null
  connectivity:
  - wifi
  battery: null
  sao_version: null
make_your_own:
  open_source: partial
  hardware_url: https://github.com/0x1ea7bee5/defcon_badge_2026/tree/main/defcon_badge_main
  firmware_url: https://github.com/0x1ea7bee5/defcon_badge_2026/tree/main/software/wifi_tracking
  eda_tool: KiCad
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
links:
- label: github.com/0x1ea7bee5/defcon_badge_2026
  url: https://github.com/0x1ea7bee5/defcon_badge_2026
  kind: repo
images: []
contact: {}
notes: []
status: announced
sources:
- kind: url
  url: https://github.com/0x1ea7bee5/defcon_badge_2026
  title: defcon_badge_2026
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 2026''.'
- kind: url
  url: https://api.github.com/repos/0x1ea7bee5/defcon_badge_2026/contents/
  title: 'defcon_badge_2026 repo file listing (GitHub API)'
  accessed: '2026-09-07'
  note: 'README.md is empty (0 bytes); repo instead contains a KiCad hardware project (defcon_badge_main), an STL file, a gerbers folder, and a software folder. Confirms KiCad as the EDA tool and that hardware+some firmware are public (no license file found, so open_source is marked partial).'
- kind: url
  url: https://github.com/0x1ea7bee5/defcon_badge_2026/tree/main/defcon_badge_main
  title: 'defcon_badge_main KiCad project (file listing)'
  accessed: '2026-09-07'
  note: 'Schematic sheet names confirm an ESP32 section, a display footprint library, a joystick, a limit switch, LED and motor-driver schematics (A4988 stepper driver datasheet is in the repo root), and 5V/8V power regulation sheets. No description text was found, only file/sheet names, so tech.leds and tech.display are left empty rather than guessed.'
- kind: url
  url: https://api.github.com/repos/0x1ea7bee5/defcon_badge_2026/commits?per_page=30
  title: 'defcon_badge_2026 commit history (GitHub API)'
  accessed: '2026-09-07'
  note: 'Commit messages ("initial project" 2026-02-21 through "python_tools/" 2026-07-02) show KiCad schematic/layout work Feb-Apr 2026, then Wi-Fi tracking software work Jun-Jul 2026, including a commit titled "vibecoded V matrix creation and eigenvector decomposition" -- basis for the MUSIC-style direction-finding description. No commits or tags indicate a finished build, release, or that units exist beyond the designer''s own.'
- kind: url
  url: https://raw.githubusercontent.com/0x1ea7bee5/defcon_badge_2026/main/software/wifi_tracking/README.md
  title: 'software/wifi_tracking README'
  accessed: '2026-09-07'
  note: 'This is the stock Espressif ESP-IDF wifi_scan example README (lists ESP32-C5 as a supported target), not maker-authored documentation -- confirms the ESP32-C5 chip choice but gives no project-specific description.'
- kind: url
  url: https://api.github.com/users/0x1ea7bee5/repos
  title: '0x1ea7bee5 GitHub repositories'
  accessed: '2026-09-07'
  note: 'Maker has no storefront, Hackaday.io project, or other public listing for this badge; their other repos are unrelated personal hobby projects. No press coverage or forum posts about this badge were found in web searches.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Corrected event from "other" to dc34 (DEF CON 34, 2026) per the maker''s own repo name and the entry''s prior source note. This is a personal, unofficial hardware project (not an official DEF CON badge, a store product, or a documented completed build) with no README, no announcement post, no images, and no evidence of release, sale, or quantity produced -- everything here comes from reading the repo''s file/folder/sheet names and commit log directly, since no maker-authored description exists. tech.leds, tech.display, tech.battery, look.colors and look.shape are left empty because no source states them; a "led.kicad_sch" schematic sheet exists in the repo but does not by itself establish LED count or type. get_one fields are left empty/unknown since this does not appear to be for sale. No other badges or SAOs were noticed during this research.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/defcon-badge-2026/
---

This is a self-designed, unofficial hardware badge built by a hobbyist (GitHub handle `0x1ea7bee5`) for DEF CON 34 (2026), rather than an officially sanctioned conference badge. The hardware, laid out in KiCad, centers on an ESP32-C5 module and also includes a small stepper-motor subsystem (an A4988 driver plus a limit switch), a joystick input, and dedicated schematic sheets for LEDs and a display, alongside 5V and 8V power regulation. Gerber files and an STL (likely an enclosure or physical part) are included in the repository alongside the KiCad source.

On the software side, the maker has been building Wi-Fi packet-scanning tools on top of the ESP32-C5's radio, including code described in a commit as constructing a channel-data matrix and performing eigenvector decomposition -- a signal-processing approach (in the style of the MUSIC algorithm) typically used for estimating the direction of a Wi-Fi signal's source, suggesting the badge is meant to do some form of Wi-Fi-based tracking or direction finding rather than just scanning for access points.

As of the most recent commits (July 2026), the project shows active hardware layout and software work but no README, announcement, storefront listing, or photos of a built unit, so it is unclear whether the badge has been fabricated, whether more than one unit exists, or whether it will be distributed at DEF CON at all. It reads as an in-progress personal build documented in the open rather than a released or for-sale product.

## Make your own

The KiCad hardware source (schematics, PCB layout, and a gerbers folder) is in `defcon_badge_main/` in the repository, and the ESP32-C5 Wi-Fi scanning firmware is in `software/wifi_tracking/` (built on the Espressif ESP-IDF `wifi_scan` example). No BOM, assembly instructions, or license file were found in the repo.
