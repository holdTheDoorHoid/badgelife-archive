---
title: PiBadge Mini (DCZia)
id: dc28-badge-dczia
layout: badge
parent: DC28
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc28
year: 2020
series: DCZia
makers:
- name: DCZia
  url: https://github.com/dczia
summary: A build-it-yourself desk badge from DCZia for the "virtual" DEF CON 28, made from a Raspberry Pi Zero W and a small LCD instead of a custom PCB, auto-playing open-source and in-house videos.
functions: Auto-plays a loop of open-source and DCZia-made videos on boot; doubles as a desk toy/screensaver. Includes a separate barcode-and-Polybius-cipher puzzle (a scannable image plus an encrypted archive) that solvers had to crack to get a password.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - puzzle
  - ctf
tech:
  mcu: Raspberry Pi Zero W
  leds: null
  display: Waveshare 1.44" LCD HAT (128x128)
  connectivity:
  - wifi
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Not sold as an assembled unit: DCZia published a parts list (Raspberry Pi Zero W, Waveshare 1.44" LCD HAT, SD card) with Amazon links and a custom Raspbian image; people sourced the parts themselves and assembled it at home.'
make_your_own:
  open_source: true
  hardware_url: https://github.com/dczia/Defcon28-Badge
  firmware_url: https://github.com/dczia/Defcon28-Badge
  eda_tool: null
links:
- label: github.com/dczia/Defcon28-Badge
  url: https://github.com/dczia/Defcon28-Badge
  kind: repo
  archived: https://web.archive.org/web/20260523084132/https://github.com/dczia/Defcon28-Badge
- label: DCZia DEFCON 28 Badge Challenge write-up (devBioS)
  url: https://github.com/devBioS/DC28_DCZIA_BadgeChallengeSolver/blob/master/write-up.md
  kind: article
- label: DCZia
  url: https://dczia.net/
  kind: website
  archived: https://web.archive.org/web/20260514004509/https://dczia.net/
images: []
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/dczia/Defcon28-Badge
  title: Defcon28-Badge (DCZia)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 28''.'
  archived: https://web.archive.org/web/20260523084132/https://github.com/dczia/Defcon28-Badge
- kind: url
  url: https://raw.githubusercontent.com/dczia/Defcon28-Badge/master/README.md
  title: 'DEFCON28-Badge README: DCZia 2020 Defcon 28 Badge - PiBadge Mini'
  accessed: '2026-09-07'
  note: Maker's own description, hardware list (Pi Zero W + Waveshare 1.44" LCD HAT), build guide, and note that this was a stand-in project because their original plan for the (virtual) 2020 con fell through.
- kind: url
  url: https://github.com/devBioS/DC28_DCZIA_BadgeChallengeSolver/blob/master/write-up.md
  title: DC28 DCZIA Build-Your-Own-Badge Challenge write-up
  accessed: '2026-09-07'
  note: 'Third-party solver write-up describing the accompanying puzzle: a barcode image decoded via a Polybius cipher keyed "DCZIA" to yield the password for an encrypted loot archive.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No photos of an assembled unit were found (GitHub repo, dczia.net, and web search only surface generic OpenGraph link-preview cards, not device photos), so images stays empty. No price, quantity-made, or a clear stock/availability status is published anywhere found; it was a self-sourced parts kit rather than something DCZia sold or gave away as a finished item, so get_one.price/quantity are left blank and availability is "unknown". LEDs are not mentioned in any source. The GitHub topics/description tag this "#badgelife" and label it a "badge", though there is no custom PCB — it is Pi Zero W + off-the-shelf LCD HAT + 3D-printed case files, closer to a DIY kit than a traditional badge.
last_modified_date: '2026-09-07'
---

DCZia's plan for DEF CON 28 (2020) fell through when the con went virtual, so rather than skip the year they published an open, build-it-at-home alternative: the PiBadge Mini, a Raspberry Pi Zero W fitted with a Waveshare 1.44" LCD HAT (128x128 pixels). DCZia wrote a custom Raspbian image that auto-plays a loop of open-source and in-house-made videos on boot, effectively turning the small screen into a looping desk toy or screensaver. The GitHub repository lists the parts (Pi Zero W, LCD HAT, an 8 GB+ SD card) with sourcing links, ships a build script for people who wanted to roll their own image instead of flashing the official one, and includes 3D-printable case files — one remixed by a contributor named Syntax to add an optional lid, and a separate Zia-shaped desk stand contributed by babdor. The repo also documents fallback options: any Pi with an fbcp-ili9341-compatible screen, or simply piping HDMI out to a TV for a larger "PiBadge XL" version using a Hyperpixel 4" display.

Alongside the badge, DCZia ran a standalone puzzle for the year: a distributed image containing a non-standard barcode labeled "DC ZIA 28," whose bar widths encoded a message when normalized and run through a Polybius-square cipher keyed with "DCZIA." Solving it yielded the password to an encrypted 7z archive of extra loot. A third-party write-up documents the full solve path.

## Make your own

Source is on GitHub at dczia/Defcon28-Badge. To build one: gather a Raspberry Pi Zero W, a Waveshare 1.44" LCD HAT, and a Class 10/U1 SD card; either flash DCZia's prebuilt Raspbian image, or flash stock Raspberry Pi OS Lite and run the repo's `dczia_setup.sh` to build the environment yourself (the script also supports the Adafruit PiTFT 3.5" and the Hyperpixel 4" "PiBadge XL" variant). 3D-printable case and stand files are included under `/case`.
