---
title: Front Row Badge (DC16 Badge Hacking Contest entry)
id: dc16-front-row-badge-dc16-badge-hacking-contest-entry
layout: badge
parent: DC16
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc16
year: 2008
makers:
- name: BonzoESC, Sterling, Critta, Jymbolia
summary: A firmware hack for the stock DEF CON 16 electronic badge that used its IR transmitter to emulate Apple Front Row and HP Pavilion DV-series laptop remote controls. It took 2nd place in the DEFCON 16 Badge Hacking Contest.
functions: Emulates Apple Front Row and HP Pavilion DV-series laptop IR remote controls via the DC16 badge's onboard IR transmitter; also brute-forces the 8-bit keyspace used to pair a real Front Row remote to a Mac.
look:
  colors: []
  shape: null
  themes: []
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - ir
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: null
  firmware_url: https://github.com/bkerley/dc16_badge/
  eda_tool: null
links:
- label: github.com/bkerley/dc16_badge
  url: https://github.com/bkerley/dc16_badge/
  kind: repo
- label: 'DEFCON 16 - Contest Results'
  url: https://defcon.net/html/defcon-16/dc-16-contest-results.html
  kind: article
  archived: null
- label: 'DC16 Badge Hack: Mac Front Row and HP Laptop 0wning (YouTube)'
  url: https://www.youtube.com/watch?v=waA2tHzhQOs
  kind: video
  archived: null
- label: 'Front Row Badge (YouTube)'
  url: https://www.youtube.com/watch?v=gPQHFCoAvgE
  kind: video
  archived: null
images: []
contact: {}
notes:
- Spotted by a research agent while working on another entry; not yet researched.
- 'Not a distinct maker-built badge/SAO: it is a firmware modification of the official Joe Grand / Grand Idea Studio DEF CON 16 electronic badge (see entry dc16-badge-2008), demonstrated as a contest hack rather than distributed as its own hardware. No standalone board, price, or quantity exists to document.'
status: not_an_item
sources:
- kind: url
  url: https://github.com/bkerley/dc16_badge/
  title: Front Row Badge (DC16 Badge Hacking Contest entry)
  accessed: '2026-09-10'
  note: Reported as an 'other item found' during the stub research pass.
- kind: url
  url: https://defcon.net/html/defcon-16/dc-16-contest-results.html
  title: 'DEFCON 16 Badge Hacking Contest Results'
  accessed: '2026-09-10'
  note: 'Confirms 2nd-place contest entry, makers, and description: IR emulation of Apple Front Row and HP Pavilion DV remote controls, plus brute-forcing the 8-bit pairing keyspace.'
- kind: url
  url: https://www.youtube.com/watch?v=waA2tHzhQOs
  title: 'DC16 Badge Hack: Mac Front Row and HP Laptop 0wning'
  accessed: '2026-09-10'
  note: 'Confirms this is the 2nd place DC16 Badge Hacking Contest entry by BonzoESC, Sterling, Critta, and Jymbolia.'
- kind: url
  url: https://www.youtube.com/watch?v=gPQHFCoAvgE
  title: 'Front Row Badge'
  accessed: '2026-09-10'
  note: Demo video linking to the same GitHub source repo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: 'Confirmed via the official DEFCON 16 contest-results page and two YouTube demo videos: this was the 2nd-place entry in the DEFCON 16 Badge Hacking Contest, a firmware hack of the stock DC16 badge (not a separate hardware product), using the badge''s IR transmitter to emulate Apple Front Row / HP Pavilion DV remote controls and brute-force the Front Row pairing keyspace. GitHub repo (bkerley/dc16_badge) has no README and no images of the badge itself; source is HCS08-family assembly/C project files matching the stock DC16 badge''s Freescale MCU, but the maker never states the chip name so tech.mcu is left null. Marked not_an_item per research-guide rules: it is a contest hack/tool applied to the official DC16 badge (see dc16-badge-2008), not a distinct maker-produced badge, SAO, or accessory with its own hardware, price, or availability.'
last_modified_date: '2026-09-10'
---

"Front Row Badge" is the name given to a firmware hack entered into the DEFCON 16 (2008) Badge Hacking Contest by a team going by BonzoESC, Sterling, Critta, and Jymbolia. Rather than being its own physical badge or SAO, it is a piece of custom firmware loaded onto the stock DEF CON 16 electronic badge (designed by Joe Grand / Grand Idea Studio; see the separate entry for that badge). The hack repurposed the badge's built-in IR transmitter to emulate Apple's Front Row remote control and HP Pavilion DV-series laptop remotes, and also brute-forced the 8-bit keyspace used to pair a genuine Front Row remote to a Mac — letting the badge hijack nearby laptops' media-center software and Front Row-equipped Macs from across a room.

The entry placed 2nd in that year's contest, behind the "Human Password Generator" and ahead of a motion-triggered music/snooze-alert hack. The team published their source on GitHub (bkerley/dc16_badge), which contains HCS08-toolchain project files (CodeWarrior/P&E BDM configs) but no README describing hardware specifics, so details like the exact MCU part number, LED behavior, or display are not stated by the makers and are left blank here. Two contemporary YouTube videos demonstrate the hack in action and corroborate the contest writeup.

Because this was a one-off software modification of an already-existing, separately catalogued badge rather than a distinct hardware product with its own price, quantity, or distribution, it is marked `not_an_item` in this archive rather than filled out as a standalone badge/SAO/accessory entry.
