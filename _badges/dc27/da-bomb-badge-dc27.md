---
title: da Bomb! Badge (DC27)
id: dc27-da-bomb-badge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Team Ides
  url: https://ides.team/dabomb/
  role: John Adams (lead), with Bill Paul
summary: 'A bomb-shaped, hackable independent badge for DEF CON 27, built around an nRF52840 (BMD340) module with a color LCD, an RGB LED matrix, and stereo audio, and funded via Kickstarter as a follow-up to Team Ides'' DC25 "Ides of Defcon" badge.'
functions: 'Runs multiple onboard games and interactive modes, supports a Konami-code-style button sequence across seven buttons, plays stereo audio, and is intended as a hackable/programmable learning platform.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - learn to solder
tech:
  mcu: nRF52840 (BMD340 module)
  leds:
    count: null
    type: RGB
    note: 'Driven by an IS3736 32x8 LED matrix driver chip; exact onboard LED count not confirmed by sources.'
  display: LCD (color TFT-style touchscreen per press coverage; exact size not confirmed)
  connectivity:
  - ble
  inputs:
  - buttons
  battery: Rechargeable LiPo with fuel gauge circuit
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '500 (planned production run per Kickstarter/Hackaday.io updates)'
  availability: unknown
  availability_note: 'Checked 2026-09-07: original storefront (troupeit.com/badge/) and Kickstarter listing status not independently verified; project dates to 2019.'
  distribution:
  - crowdfunding
  - purchase
  where: 'Funded via Kickstarter ("it''s da Bomb! An Indie DEF CON badge for DC27 by John Adams"); also sold via troupeit.com/badge/ per the maker''s project log.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/netik/dc27_badge/tree/master/hardware/dc27_badge_kicad
  firmware_url: https://github.com/netik/dc27_badge/tree/master/software/firmware/badge
  eda_tool: KiCad
  license: Apache-2.0
  fab_url: null
  bom_url: null
  gerbers_url: null
  notes: 'Repository (netik/dc27_badge) also includes Kickstarter materials and artwork folders; roughly 133 parts on a 4-layer PCB per the Hackaday.io project log.'
links:
- label: ides.team/dabomb
  url: https://ides.team/dabomb/
  kind: website
- label: netik/dc27_badge (GitHub)
  url: https://github.com/netik/dc27_badge
  kind: repo
- label: 'Team Ides: DC27 / da Bomb! (Hackaday.io)'
  url: https://hackaday.io/project/161163-team-ides-dc27-da-bomb
  kind: hackaday
- label: "it's da Bomb! (Kickstarter)"
  url: https://www.kickstarter.com/projects/1887776662/its-da-bomb-an-indie-def-con-badge-for-dc27
  kind: store
- label: Da Bomb Is a Hackable Badge for DEF CON 27 (Hackster.io)
  url: https://www.hackster.io/news/da-bomb-is-a-hackable-badge-for-def-con-27-74c9f7020eb8
  kind: article
- label: Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27 (Hackaday)
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
images:
- file: assets/images/badges/dc27/da-bomb-badge-dc27/27a0a511a1.png
  source: "https://ides.team/dabomb/"
  credit: "Team Ides / John Adams"
  caption: "da Bomb badge face artwork"
- file: assets/images/badges/dc27/da-bomb-badge-dc27/256919ca3a.jpg
  source: "https://ides.team/dabomb/"
  credit: "Team Ides / John Adams"
  caption: "da Bomb badge kit box"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://ides.team/dabomb/
  title: Da Bomb Badge (DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''.'
- kind: url
  url: https://ides.team/dabomb/
  title: da Bomb! project page (ides.team)
  accessed: '2026-09-07'
  note: 'Confirmed maker (Team Ides / John Adams), event/year, and found GitHub repo links and image URLs.'
- kind: url
  url: https://github.com/netik/dc27_badge
  title: 'GitHub - netik/dc27_badge: Defcon 27 "DaBomb!" badge.'
  accessed: '2026-09-07'
  note: 'Confirmed open source (Apache-2.0), repo layout with hardware/software/artwork folders.'
- kind: url
  url: https://hackaday.io/project/161163-team-ides-dc27-da-bomb
  title: 'Team Ides: DC27 / da Bomb! (Hackaday.io)'
  accessed: '2026-09-07'
  note: 'Primary technical source: MCU (nRF52840/BMD340), IS3736 LED matrix driver, CS4344 stereo DAC, seven buttons/Konami code, planned 500-unit run, ~133 parts on a 4-layer PCB, collaborator Bill Paul, storefront troupeit.com/badge/.'
- kind: url
  url: https://www.hackster.io/news/da-bomb-is-a-hackable-badge-for-def-con-27-74c9f7020eb8
  title: Da Bomb Is a Hackable Badge for DEF CON 27
  accessed: '2026-09-07'
  note: 'Press summary corroborating BMD340 MCU, 320x240 TFT touchscreen, 32 RGB LEDs, BLE 5.0, and 2000mAh LiPo battery (higher-confidence than the Hackaday.io prototype log for final specs, though not independently confirmed by a maker source in this pass).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Two sources give somewhat different final specs: Hackaday.io''s project log (a build-in-progress post) says an IS3736 32x8 LED matrix driver and does not give a firm LED count, while Hackster.io''s press summary states 32 RGB LEDs, a 320x240 TFT touchscreen, BLE 5.0, and a 2000mAh LiPo; both are plausible for the finished badge but neither is confirmed by a maker post covering the final, shipped hardware, so LED count/type, exact display spec, and battery capacity are given cautiously. Kickstarter page returned HTTP 403 and could not be read directly, so price and backer/funding numbers are empty. Shape and PCB/solder-mask colors are not confirmed by any source read (Hackaday.io''s early log describes only a placeholder square test board), so look.shape and look.colors are left empty rather than guessed from the "bomb" name or box art.'
last_modified_date: '2026-09-07'
---

The da Bomb! badge was Team Ides' follow-up to their DC25 "Ides of Defcon" badge, built by John Adams (with collaborator Bill Paul) for DEF CON 27 in 2019 and funded through a Kickstarter campaign ("it's da Bomb! An Indie DEF CON badge for DC27"). It is a hackable, independent conference badge centered on a Nordic nRF52840 (BMD340 module), pairing a color LCD with an RGB LED matrix (driven by an IS3736 matrix driver chip), stereo audio through a Cirrus Logic CS4344 DAC, Bluetooth Low Energy, and seven buttons supporting a Konami-code-style input sequence. The badge runs multiple onboard games and was designed as an approachable platform for badge hackers to program and modify, with a rechargeable LiPo battery and fuel-gauge circuit.

The hardware and firmware are open source, published in the `netik/dc27_badge` GitHub repository (Apache-2.0 licensed) alongside Kickstarter and artwork materials; the PCB was designed in KiCad as a 4-layer board with roughly 133 parts. Team Ides' project log targeted a production run of about 500 badges, sold through the Kickstarter campaign and via troupeit.com. Some final-hardware details (exact LED count, display size, and battery capacity) are reported differently between the maker's own build-in-progress project log and later press coverage, so those figures are noted with medium confidence pending a maker source describing the final, shipped badge.

## Make your own

Hardware (KiCad project) and firmware source are both published in the `netik/dc27_badge` repository: hardware under `hardware/dc27_badge_kicad`, firmware under `software/firmware/badge`. The repo is licensed Apache-2.0 and also includes the original Kickstarter copy and artwork assets.
