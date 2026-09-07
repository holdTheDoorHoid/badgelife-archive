---
title: Arctic Wolf MicroBadge Extender Display
id: saintcon-2025-arctic-wolf-microbadge-extender-display
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: Cyberm3n
summary: 'A display board that holds and shows off six SAINTCON-style microbadges at once, sized to house the whole Arctic Wolf microbadge set.'
functions: 'Purely a display/holder: female headers on the front accept up to six microbadges (2x3 grid) built to the shared minibadge pin spec, so collected pieces can be shown together rather than loose.'
look:
  colors: []
  shape: rectangle
  themes:
  - security
  - minimalist
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  - swap
  where: 'Handed out / traded for at the Arctic Wolf sponsor booth at SAINTCON 2025; also obtainable by finding and trading with an Arctic Wolf employee.'
make_your_own:
  open_source: partial
  hardware_url: https://github.com/cyberm3n-org/SC_2025/arctic_wolf
  firmware_url: null
  eda_tool: null
links:
- label: minibadge.wiki/?search=Arctic%20Wolf%20MicroBadge%20Extender%20Display&year=2025
  url: https://minibadge.wiki/?search=Arctic%20Wolf%20MicroBadge%20Extender%20Display&year=2025
  kind: website
- label: 'cyberm3n-org/SC_2025 (arctic_wolf) on GitHub'
  url: https://github.com/cyberm3n-org/SC_2025/arctic_wolf
  kind: repo
images:
  - file: assets/images/badges/saintcon-2025/arctic-wolf-microbadge-extender-display/1777d17a65.png
    source: "https://minibadge.wiki/?search=Arctic%20Wolf%20MicroBadge%20Extender%20Display&year=2025"
    credit: "Cyberm3n"
    caption: "Front of the extender board, showing 2x3 microbadge socket array"
  - file: assets/images/badges/saintcon-2025/arctic-wolf-microbadge-extender-display/bf6695c495.png
    source: "https://minibadge.wiki/?search=Arctic%20Wolf%20MicroBadge%20Extender%20Display&year=2025"
    credit: "Cyberm3n"
    caption: "Back of the extender board"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 2).
status: released
sources:
- kind: url
  url: https://minibadge.wiki/?search=Arctic%20Wolf%20MicroBadge%20Extender%20Display&year=2025
  title: Arctic Wolf MicroBadge Extender Display
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run2-spotted); event read as ''saintcon-2025''.'
- kind: url
  url: https://minibadge.wiki/2025.json
  title: 'MiniBadge Wiki 2025 data feed (JSON entry for Arctic Wolf MicroBadge Extender Display)'
  accessed: '2026-09-07'
  note: 'Primary source: maker-submitted description, soldering instructions, how-to-acquire text, category (Sponsor), rarity (Uncommon), board house (JLCPCB), and image filenames.'
- kind: url
  url: https://github.com/cyberm3n-org/SC_2025/arctic_wolf
  title: cyberm3n-org/SC_2025 arctic_wolf directory
  accessed: '2026-09-07'
  note: 'Confirmed the repo exists (linked from the soldering instructions); did not open individual files to check for KiCad/Gerber sources, so open_source is marked partial rather than yes.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker-submitted listing on minibadge.wiki (a community-run SAINTCON minibadge wiki, not the maker''s own site) is the only real source found; treated as maker-authored since it is filled in directly by the badge''s creator (author: Cyberm3n) via the site''s submission form. No independent press coverage or storefront found. This is one of a small Arctic Wolf-sponsored family for SAINTCON 2025 (a main "Arctic Wolf Base" triple-board badge, this six-slot extender/display board, and four collectible team/theme microbadges: Red Team, Blue Team, Purple Team, and Black Badge) documented in the same data feed but out of scope for this entry. Quantity made, MCU/LED/display specs were not stated anywhere found — it appears to be a passive PCB with no electronics of its own, just header sockets, but this was not explicitly confirmed by the maker so tech fields are left null rather than guessed.'
last_modified_date: '2026-09-07'
---

The Arctic Wolf MicroBadge Extender Display is a sponsor-badge accessory that Cyberm3n built for SAINTCON 2025, sized to hold and show off up to six SAINTCON-style microbadges at once in a 2x3 grid of female header sockets. It was designed specifically to display the four-piece Arctic Wolf microbadge set (Red Team, Blue Team, Purple Team, and Black Badge) together, but it accepts any microbadge built to the shared pin specification published by another SAINTCON badge designer known as pip801, so attendees could mix in other makers' pieces too.

Assembly is simple: pull the pins from a female header so they line up with the badge, solder the headers to the front of the board, solder pins to the back for mounting, then plug microbadges into the sockets. Boards were fabricated through JLCPCB. It was given away free at SAINTCON 2025 — attendees could get one by visiting the Arctic Wolf sponsor booth or by finding and trading with an Arctic Wolf employee. Detailed soldering instructions and hardware files for the whole Arctic Wolf badge family live in Cyberm3n's `SC_2025` GitHub repo, under the `arctic_wolf` directory; the individual files were not inspected for this entry, so `make_your_own.open_source` is marked partial rather than confirmed fully open.

No maker-stated quantity, MCU, or LED/display specs were found. The board appears to be a passive holder with no active electronics, but that was not explicitly confirmed, so those tech fields are left empty rather than guessed.
