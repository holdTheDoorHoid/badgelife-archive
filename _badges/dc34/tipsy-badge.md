---
title: Tipsy Badge
id: dc34-tipsy-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: seeess + gigs
  url: https://github.com/seeess
summary: 'A bottle-shaped electronic badge that uses galvanic vestibular stimulation: conductive pads held behind the wearer''s ears by a headband carry a few milliamps that shift the sense of balance left or right, or make the wearer wobble. This appears to be the same Tipsy Badge sold at the Hacker Warehouse booth for DEF CON 33 (2025), re-listed on the community sheet for DEF CON 34.'
functions: 'Steering mode pushes the wearer''s balance left or right; wobble mode rocks it back and forth quickly; a Stroop-effect color game zaps you on right or wrong answers; bling mode shows pictures, with custom 128x160 .tga images loadable over USB mass storage. Zapping only happens while the in-line ZAP button is held; ~5 mA hardware current limit with 2, 3 and 4 mA software targets.'
look:
  colors:
  - black
  - yellow
  shape: bottle
  themes:
  - drink
  - text
  form_factor: pcb badge
tech:
  mcu: RP2040
  leds:
    count: 12
    type: charlieplexed
    note: 12 orange charlieplexed LEDs per the firmware source, rear-mounted; plus red and green status LEDs. (Confirmed on the DC33 build of this badge; not reverified separately for a DC34 release.)
  display: '1.77" 160x128 RGB565 color TFT'
  connectivity:
  - usb
  inputs:
  - buttons
  power: 2x AAA or USB-C (zap modes are meant to run on batteries only)
  battery: 2x AAA
  sao_version: v1.69bis
  sao_ports: 1
get_one:
  price: This will be sold at hacker warehouse's booth
  price_usd: 100.0
  quantity: ''
  availability: unknown
  availability_note: 'hackerwarehouse.com/product/tipsy-badge/ (checked 2026-09-06) shows the badge marked down from $100 to $75 and Out of stock, but that listing is not dated to a specific DEF CON year.'
  distribution:
  - purchase
  where: Sold at the Hacker Warehouse booth in the vendor area; also listed on hackerwarehouse.com.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/seeess/Defcon-Tipsy-33-Badge/tree/main/tipsy
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: CC BY-NC 4.0
  fab_url: null
  notes: The repo (named for DEF CON 33) has the Arduino sketch, a prebuilt UF2, sample .tga pictures, headband STLs and flashing instructions. No schematic, PCB files, Gerbers or BOM are published.
links:
- label: hackerwarehouse.com/product/tipsy-badge
  url: https://hackerwarehouse.com/product/tipsy-badge/
  kind: store
- label: github.com/seeess/Defcon-Tipsy-33-Badge
  url: https://github.com/seeess/Defcon-Tipsy-33-Badge
  kind: repo
- label: www.youtube.com/watch?v=PIN-Ia04JUs
  url: https://www.youtube.com/watch?v=PIN-Ia04JUs
  kind: video
- label: Tipsy Electronic Badge thread on the DEF CON forums
  url: https://forum.defcon.org/node/253193
  kind: social
images: []
contact:
  discord: seeess
  emails:
  - seeess@torproject.org
  handles:
  - '@see_ess'
  raw:
  - twitter
notes:
- 'This entry duplicates dc33-tipsy-badge. Every public source found (the GitHub repo name "Defcon-Tipsy-33-Badge", the maker''s 8 Aug 2025 sale-announcement tweet tagged #defcon33, the DEF CON forum post, and Hacker Warehouse product photos dated to September 2025) ties this badge to DEF CON 33 (2025), not DEF CON 34. The community sheet appears to have re-listed the same row under the DC34 tab; no independent DC34-specific listing, sale post, or new repo was found.'
status: listed
sources:
- kind: sheet
  event: dc34
  row: 20
  updated: 6/16/2026 17:31:31
  listing: New
- kind: url
  url: https://hackerwarehouse.com/product/tipsy-badge/
  title: Tipsy Badge - Hacker Warehouse
  accessed: '2026-09-06'
  note: 'Product listing: RP2040-based, color TFT, 1x SAO 1.69bis port, 2MB flash with USB mass storage, open source; $100 marked down to $75, Out of stock; product photos dated wp-content/uploads/2025/09. Read via WebFetch (direct curl was blocked by Cloudflare).'
- kind: url
  url: https://github.com/seeess/Defcon-Tipsy-33-Badge
  title: 'GitHub - seeess/Defcon-Tipsy-33-Badge: Defcon Tipsy Badge / Volt 4.5 ma'
  accessed: '2026-09-06'
  note: Repo name and README describe this as the DEF CON 33 badge; supports MCU, display, memory, connectivity, modes, and license (CC BY-NC 4.0). Same repo already cited on the dc33-tipsy-badge entry.
- kind: url
  url: https://x.com/see_ess/status/1953718808105169371
  title: seeess on X, 8 Aug 2025, tagged #defcon33
  accessed: '2026-09-06'
  note: Sale announcement explicitly tagged #defcon33, supporting that this is the DC33 badge rather than a separate DC34 release.
- kind: url
  url: https://forum.defcon.org/node/253193
  title: Tipsy Electronic Badge - DEF CON Forums
  accessed: '2026-09-06'
  note: Maker's post (user seeess), same content already used for the dc33 entry; $100 price, Hacker Warehouse booth, open source, half of profits to Tor.
research:
  status: researched
  confidence: low
  last_checked: '2026-09-06'
  notes: 'Could not confirm this is a distinct DEF CON 34 item, only a re-listing of the DEF CON 33 Tipsy Badge (see dc33-tipsy-badge, status: verified). No DC34-dated source (sale post, storefront date, new repo, or press) was found in searches; the repo name, the maker''s #defcon33-tagged sale tweet, and the September 2025 photo timestamps on the Hacker Warehouse listing all point to DC33. Left get_one fields largely matching the original sheet wording rather than asserting a DC34-specific price/availability. Did not fetch new images for this entry: the same product/README photos are already archived under dc33-tipsy-badge, and Hacker Warehouse blocked direct fetching via curl (Cloudflare) with no distinct DC34 photo found to justify separate saves. Recommend the archive maintainer verify with the maker whether the badge returned for DC34 or merge/redirect this entry into dc33-tipsy-badge.'
last_modified_date: '2026-09-06'
---

This entry on the community sheet lists a "Tipsy Badge" by seeess (with gigs) for DEF CON 34, but every source found for it points back to the DEF CON 33 badge already documented at `dc33-tipsy-badge`: the maker's GitHub repo is named `Defcon-Tipsy-33-Badge`, the sale-announcement post on X is tagged `#defcon33`, the DEF CON forum thread and Hacker Warehouse product photos (timestamped September 2025) all date to the DC33 timeframe. No DC34-specific listing, new repo, or fresh sale post was found.

The badge itself is a bottle-shaped board built around an RP2040 with a 1.77" color TFT, a 1.69bis SAO header, USB-C, and two AAA cells. It uses galvanic vestibular stimulation: a headband holds conductive pads behind the wearer's ears, and while the ZAP!! button is held, a small current (hardware-limited to about 5 mA) steers the wearer's balance left or right, or rocks them back and forth in wobble mode. A bling mode displays custom images loaded over USB mass storage, and a Stroop-effect color game zaps the wearer on right or wrong answers. It was sold at the Hacker Warehouse vendor booth for $100, with half the profits going to the Tor Project.

Given the overlap, this is most likely the same physical badge re-appearing on the DC34 sheet rather than a new DC34 release — see `dc33-tipsy-badge` for the fully verified writeup, including firmware-level LED counts, safety-interlock behavior, and archived photos.
