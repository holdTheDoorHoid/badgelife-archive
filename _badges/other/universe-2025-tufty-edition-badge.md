---
title: Badger 2350 (GitHub Universe 2025 Badge)
id: other-universe-2025-tufty-edition-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2025
makers:
- name: Pimoroni
  url: https://badger.github.io
  role: hardware and firmware design (for GitHub)
summary: 'The official hackable conference badge for GitHub Universe 2025, a custom Pimoroni board (commercialized later as the "Tufty 2350") running MicroPython on an RP2350, with a color screen, WiFi, and a live GitHub-profile display app.'
functions: 'Runs MicroPython with eight preloaded apps: a badge app that pulls the wearer''s live GitHub stats (avatar, followers, contributions, repos) over WiFi, Flappy Mona and a brick-breaker game, a tamagotchi-style pet, a drawing/etch-a-sketch app, a photo gallery, an IR-based scavenger hunt, and a system debug app (network, storage, memory info). A web-based REPL tool (Web Serial API) lets attendees connect to and hack the badge live.'
look:
  colors: []
  shape: rectangle
  themes:
  - logo
  - hardware tool
tech:
  mcu: RP2350
  leds: null
  display: color LCD (24x24 pixel app icons)
  connectivity:
  - wifi
  - bluetooth
  - ir
  battery: battery-powered (rechargeable, USB-C)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - free_drop
  where: Given to GitHub Universe 2025 attendees only; as of the badge's debut there was "not yet a way to get hold of this hardware outside of GitHub Universe" due to supply constraints, though Pimoroni planned a later commercial release as the "Tufty 2350."
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://badger.github.io
  eda_tool: null
links:
- label: simonwillison.net/2025/Oct/28/github-universe-badge
  url: https://simonwillison.net/2025/Oct/28/github-universe-badge/
  kind: website
- label: badger.github.io
  url: https://badger.github.io
  kind: website
images:
  - file: assets/images/badges/other/universe-2025-tufty-edition-badge/7571194083.jpg
    source: "https://simonwillison.net/2025/Oct/28/github-universe-badge/"
    credit: "Simon Willison"
    caption: "Badge showing its color screen with six app icons"
  - file: assets/images/badges/other/universe-2025-tufty-edition-badge/f386eae860.jpg
    source: "https://simonwillison.net/2025/Oct/28/github-universe-badge/"
    credit: "Simon Willison"
    caption: "Badge app displaying the wearer's GitHub profile stats (avatar, followers, contributions, repos)"
contact: {}
notes:
- 'The event-year sweep found this via a blog post titled "Universe 2025 (Tufty Edition) Badge"; the maker/project itself calls the badge and its app catalog "Badger 2350," and describes the underlying hardware as a Pimoroni board slated for commercial release as the "Tufty 2350." Title updated to reflect the maker''s own naming, with the sweep''s title kept here for reference.'
status: released
sources:
- kind: url
  url: https://simonwillison.net/2025/Oct/28/github-universe-badge/
  title: Universe 2025 (Tufty Edition) Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:general-2025); event read as ''GitHub Universe 2025''.'
- kind: url
  url: https://badger.github.io
  title: 'Badger 2350: GitHub Universe 2025 Badge'
  accessed: '2026-09-08'
  note: 'Maker/project site; confirms the Badger 2350 name, app catalog, and GitHub-profile-pulling badge app.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'No matching event id exists in _data/events.yml for "GitHub Universe 2025" (it is a corporate developer conference, not a hacker con currently tracked there); event left as "other" per instructions, with the con and year (GitHub Universe 2025, held October 2025) noted here. Price and quantity made were not stated by either source. Hardware files (schematics/gerbers) were not found published; only the firmware/software side (MicroPython apps, badger.github.io) is public, so open_source is marked partial rather than yes.'
last_modified_date: '2026-09-08'
---

The Badger 2350 is the custom hackable badge Pimoroni built for GitHub Universe 2025, GitHub's annual developer conference. It runs MicroPython on an RP2350 microcontroller and pairs a color screen with WiFi, letting the stock "badge" app fetch and display the wearer's live GitHub profile: avatar, follower count, contributions, and repository count. Pimoroni has said the same board is headed for commercial release as the "Tufty 2350," making this badge a preview/limited run of that upcoming product.

Beyond the profile display, attendees got a small suite of preloaded apps: a Flappy Bird clone ("Flappy Mona"), a brick-breaker game, a tamagotchi-style virtual pet, a drawing/etch-a-sketch tool, a photo gallery, an infrared-based scavenger hunt, and a system debug screen exposing network, storage, and memory info. A browser-based REPL tool using the Web Serial API let people connect to and hack their badge directly from a Chrome/Edge tab.

Distribution was limited to Universe 2025 attendees; at launch there was no way to obtain the hardware outside the event due to supply constraints. The software and app catalog are documented publicly at badger.github.io, but no separate hardware design files (schematics or Gerbers) were located during this research pass.
