---
title: GrrCON 2024 BadgeBuddy
id: grrcon-2024-grrcon-2024-badgebuddy
layout: badge
parent: GrrCON 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: grrcon-2024
year: 2024
makers:
- name: CynicalSignals (ickfosec)
  url: https://www.cynicalsignals.com/
summary: An unofficial ESP8266-powered proximity badge built for about 30 friends attending GrrCON 2024, whose 8x8 LED matrix animation grows as other BadgeBuddies come into WiFi range.
functions: Scans WiFi for nearby BadgeBuddy SSIDs; below a proximity threshold it shows a bouncing-pixel Breakout/DVD-screensaver-style animation, and above the threshold it switches to a denser Matrix-style animation, acting as a conversation starter and informal group-coordination tool.
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - hardware tool
  - wearable
tech:
  mcu: ESP8266
  leds:
    count: 64
    type: RGB
    note: Socketed 8x8 LED matrix so the color of the matrix can be swapped.
  display: LED matrix 8x8
  connectivity:
  - wifi
  battery: 3x AA (~32 hour battery life)
  sao_version: none
get_one:
  price: "$9.44 per badge at minimum 20-unit production"
  price_usd: 9.44
  quantity: '~30'
  availability: not_released
  availability_note: Not commercially sold; built and given to friends attending GrrCON 2024. Checked 2026-09-08.
  distribution:
  - free_drop
  where: Given directly by the maker to about 30 friends attending GrrCON 2024; not sold or distributed at the con generally.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ickfosec/esp
  firmware_url: https://github.com/ickfosec/esp
  eda_tool: null
links:
- label: www.cynicalsignals.com/building-an-unofficial-badge-for-grrcon-2024
  url: https://www.cynicalsignals.com/building-an-unofficial-badge-for-grrcon-2024/
  kind: website
- label: ickfosec/esp on GitHub
  url: https://github.com/ickfosec/esp
  kind: repo
images:
- file: assets/images/badges/grrcon-2024/grrcon-2024-badgebuddy/034593ad50.jpg
  source: "https://www.cynicalsignals.com/building-an-unofficial-badge-for-grrcon-2024/"
  credit: "CynicalSignals (ickfosec)"
  caption: "Assembled BadgeBuddy units for GrrCON 2024"
- file: assets/images/badges/grrcon-2024/grrcon-2024-badgebuddy/ed03b29ece.jpg
  source: "https://www.cynicalsignals.com/building-an-unofficial-badge-for-grrcon-2024/"
  credit: "CynicalSignals (ickfosec)"
  caption: "Closeup of the BadgeBuddy PCB and 8x8 LED matrix"
contact: {}
notes:
- The community sweep's one-line summary ("Unofficial ESP8266 + 8x8 LED matrix proximity badge built for about 30 attendees at GrrCON 2024; code on GitHub as ickfosec/esp") is confirmed by the maker's own blog post.
status: released
sources:
- kind: url
  url: https://www.cynicalsignals.com/building-an-unofficial-badge-for-grrcon-2024/
  title: GrrCON 2024 BadgeBuddy
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-derbycon); event read as ''GrrCON 2024''.'
- kind: url
  url: https://www.cynicalsignals.com/building-an-unofficial-badge-for-grrcon-2024/
  title: Building an Unofficial Badge for GrrCon 2024
  accessed: '2026-09-08'
  note: Maker's own writeup; source for functions, hardware specs, price, quantity, distribution, and images.
- kind: url
  url: https://github.com/ickfosec/esp
  title: ickfosec/esp
  accessed: '2026-09-08'
  note: Confirms repo holds code and SVG wiring diagrams for BadgeBuddy (and a companion project, "Backpack of Shame"); no explicit license found.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own blog post confirms the item and all core facts (hardware, functions, price, quantity, distribution). Could not confirm a license on the GitHub repo, so make_your_own.license is left empty. Gerbers/BOM not found, only firmware code and wiring diagrams, so make_your_own.eda_tool and gerbers_url/bom_url are left empty.
last_modified_date: '2026-09-08'
---

CynicalSignals (handle ickfosec) built the BadgeBuddy as an unofficial add-on badge for GrrCON 2024 in Grand Rapids, MI, making about 30 of them to hand out to friends attending the conference rather than selling or distributing them broadly. Each badge is an ESP8266 board driving a socketed 8x8 RGB LED matrix, powered by a 3xAA pack rated for roughly 32 hours of use.

The badge works as a WiFi-based proximity toy: it scans for the SSIDs of nearby BadgeBuddies, and the matrix normally shows a bouncing-pixel animation reminiscent of Breakout or a DVD screensaver. When enough other badges are detected nearby, it switches to a denser, Matrix-style animation, making it a conversation starter and an informal way for wearers to find each other in a crowd. At a stated production cost of about $9.44 per unit (at a minimum run of 20), the project was clearly built as a low-cost hobby batch rather than a commercial product.

## Make your own

Code and SVG wiring diagrams are published on GitHub at ickfosec/esp, alongside a companion project called "Backpack of Shame." No license, Gerbers, or BOM were found in the repo at the time of this research, so build files beyond the code and wiring diagrams are not confirmed to exist publicly.
