---
title: H2HC 2023 Game Boy Badge
id: h2hc-2023-h2hc-2023-game-boy-badge
layout: badge
parent: H2HC 2023
grand_parent: Badge Archive
nav_exclude: true
type: other
event: h2hc-2023
year: 2023
makers:
- name: brian
  url: https://security-bits.de
summary: A custom Game Boy game flashed onto ~120 real cartridges and given to attendees of H2HC 2023 in place of a PCB electronic badge.
functions: 'A short adventure game set at an imaginary version of the H2HC venue and hotel in Sao Paulo, with dialogue, NPCs, multiple rooms/scenes, and a bowling-alley minigame with randomized results.'
look:
  colors: []
  shape: null
  themes:
  - console
  - retro computer
  - video game
tech:
  mcu: none
  leds: null
  display: none
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: '~120'
  availability: free
  distribution:
  - free_drop
  where: Given to attendees at H2HC 2023 as a flashed physical Game Boy cartridge.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/series/h2hc
  url: https://badge.gallery/series/h2hc
  kind: website
- label: 'Security-Bits.de: Gameboy? Gameboy!'
  url: https://security-bits.de/posts/2023-12-10-gameboy/
  kind: article
- label: Play the game online
  url: https://security-bits.de/h2hc23
  kind: website
- label: GB Studio (game engine used)
  url: https://www.gbstudio.dev/
  kind: doc
- label: FlashGBX (cartridge flashing tool used)
  url: https://github.com/lesserkuma/FlashGBX
  kind: repo
images: []
contact: {}
notes:
- Custom Game Boy-shaped conference badge/game artifact for H2HC 2023. Found by the event-year sweep, task con-ekoparty.
- 'The sweep''s title called this a "Game Boy Badge" implying a Game Boy-shaped PCB; sources show it is instead a real Game Boy game cartridge (software project, GB Studio) physically flashed and distributed as the conference''s badge/keepsake for that year. Title kept as-is since it matches how the item is known, but it is not an electronics board.'
status: released
sources:
- kind: url
  url: https://badge.gallery/series/h2hc
  title: H2HC 2023 Game Boy Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''H2HC 2023''.'
- kind: url
  url: https://security-bits.de/posts/2023-12-10-gameboy/
  title: 'Gameboy? Gameboy! (Security-Bits.de)'
  accessed: '2026-09-08'
  note: 'Maker''s own writeup: confirms it is a custom Game Boy game made with GB Studio, made for H2HC (Sao Paulo, Brazil), ~120 cartridges physically flashed with a GBxCart RW and FlashGBX, given to attendees as their conference badge for 2023. Author signs as "brian" (also credited for the H2HC 2015 and 2018 badge entries).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Confirmed via the maker''s own blog post (security-bits.de), which is the sole independent source found; no press coverage, storefront, or maker social post turned up in search. No photo of the physical cartridge was found on the writeup (only screenshots of the dev tools and in-game screens), so no images were saved. Price/cost of production, exact quantity beyond "120", and hardware/firmware repo (if any beyond the linked third-party tools) are not stated by the source. No indication of a save battery or other cartridge hardware detail, so tech fields beyond mcu/display are left null.'
last_modified_date: '2026-09-08'
---

For H2HC 2023 in Sao Paulo, Brazil, security researcher "brian" (security-bits.de), who had previously made the H2HC 2015 and 2018 badges, built the conference's badge as a real, playable Game Boy game rather than a PCB. Using GB Studio for the game logic, Tiled for maps, and Aseprite for pixel art, he created a short adventure depicting a visit to an imaginary version of the H2HC venue and hotel, complete with dialogue, multiple rooms, NPCs, and a bowling-alley minigame with randomized outcomes.

About 120 physical Game Boy cartridges were flashed using a GBxCart RW adapter and the FlashGBX tool (three flashing instances run in parallel from one laptop) and handed out to attendees as their conference badge/keepsake. The game is also playable in a browser at security-bits.de/h2hc23. No PCB, MCU, or display of its own is involved — the cartridge relies entirely on a standard Game Boy to run.
