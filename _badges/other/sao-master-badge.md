---
title: SAO Master Badge
id: other-sao-master-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: babint
  url: https://hackaday.io/babint
summary: A simple coin-cell or LiPo powered "master" board that supplies power to a single Shitty Add-On (SAO), built by a Hackaday.io user as a first electronics project.
functions: Powers one SAO module (via a 4-pin/2x3 connector footprint that can be oriented to center different SAOs); a status LED indicates power.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: 0805 status LED, wired in parallel with the SAO connector.
  display: none
  connectivity: []
  battery: CR2032 (coin cell) or LiPo via JST connector; not both at once
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/159778-sao-master-badge
  url: https://hackaday.io/project/159778-sao-master-badge
  kind: hackaday
  archived: https://web.archive.org/web/20260225145003/https://hackaday.io/project/159778-sao-master-badge
images:
- file: assets/images/badges/other/sao-master-badge/f7db5d3b50.jpg
  source: https://hackaday.io/project/159778-sao-master-badge
  credit: babint
  caption: Bare PCB, front and back, silkscreened "Shitty Master Badge v0.0.2"
  archived: https://web.archive.org/web/20260225145003/https://hackaday.io/project/159778-sao-master-badge
- file: assets/images/badges/other/sao-master-badge/d558dee863.jpg
  source: https://hackaday.io/project/159778-sao-master-badge
  credit: babint
  caption: Bare PCB from an earlier revision, front and back, silkscreened "ShittyCoin v0.0.1"
  archived: https://web.archive.org/web/20260225145003/https://hackaday.io/project/159778-sao-master-badge
contact: {}
notes:
- 'Coin-cell powered ''Master'' badge to power SAOs; learning platform for #badgelife.'
- Not made for a specific convention; the maker built it as a personal electronics-learning exercise, first posted to Hackaday.io on 2018-07-17. No event/year field in the sheet maps to a real con, so event is left as "other".
status: released
sources:
- kind: url
  url: https://hackaday.io/project/159778-sao-master-badge
  title: SAO Master Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''badgelife general''.'
  archived: https://web.archive.org/web/20260225145003/https://hackaday.io/project/159778-sao-master-badge
- kind: url
  url: https://hackaday.io/project/159778-sao-master-badge
  title: SAO Master Badge (project log and components)
  accessed: '2026-09-07'
  note: 'Read the full project page: description, maker handle (babint), build log for versions 0 through 0.0.3, and the components list (SPTD SMD switch, CR2032 retainer, MIC5504-3.3YM5-TR LDO, 0805 LED). No price, quantity, storefront link, or published design files found on the page.'
  archived: https://web.archive.org/web/20260225145003/https://hackaday.io/project/159778-sao-master-badge
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-checked against the Hackaday.io project page and its build log/gallery. Corrected two errors from the prior pass: the lanyard hole was added in build-log version 0.0.2, not 0.0.1 as previously written, and the two saved photos are bare/unpopulated PCBs (one silkscreened "Shitty Master Badge v0.0.2", the other an earlier "ShittyCoin v0.0.1" revision), not assembled boards as the old captions claimed - both corrected in the body and image captions. Confirmed via a fetched quote that the coin cell and LiPo/JST power options cannot be used at once. Maker (Hackaday.io user "babint"), 2018-07-17 post date, "Fat Pika SAO"/DEF CON 26 SAO standard references, and all listed components (SPTD SMD switch, 20mm CR2032 retainer, MIC5504-3.3YM5-TR LDO, 0805 LED) all confirmed on the page. No pricing, quantity, availability, open-source files, or repo/Gerber link found on the page, matching the blank fields. Could not find the maker outside Hackaday.io.'
last_modified_date: '2026-09-07'
---

The SAO Master Badge is a small coin-cell or LiPo powered "master" board built by Hackaday.io user babint to power a single Shitty Add-On (SAO) module. It was not made for any particular convention; babint describes it explicitly as a personal exercise to learn circuit design, part sourcing, and PCB fabrication while getting acquainted with the #badgelife scene, referencing the DEF CON 26 SAO standard and crediting the "Fat Pika SAO" project as inspiration.

The board went through several iterations documented in a build log, starting from a basic coin-cell retainer with a 2x3 SAO connector (version 0), adding a status LED and a choice of connector orientations to center different SAO shapes (0.0.1), a JST connector for an alternative LiPo power source and a lanyard hole (0.0.2, coin cell and LiPo cannot be used at once), and finally a MIC5504-3.3YM5-TR LDO regulator to stabilize the output voltage at 3.3V (0.0.3). The bill of materials also lists an SPTD SMD switch and a 20mm CR2032 coin-cell retainer.

No pricing, unit count, or sale listing was found, and no schematic, Gerber, or firmware repository is linked from the project page, so its open-source status and availability are left unknown.
