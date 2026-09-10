---
title: RVAsec 2012 Badge
id: rvasec-2012-rvasec-2012-badge
layout: badge
parent: RVAsec 2012
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2012
year: 2012
makers:
- name: HackRVA
  url: https://github.com/HackRVA
summary: 'The first RVAsec electronic conference badge: an MSP430-based badge with a Nokia 5110 LCD and four-button text entry, built by the HackRVA hackerspace.'
functions: Initializes the Nokia LCD, draws RVAsec and HackRVA graphics, and handles four-button text input recognizing strings like "hackrva," "anonymous," and "rvasec." Includes a Konami-code easter egg that displays "99 LIVES!"
look:
  colors: []
  shape: null
  themes:
  - security
  - text
tech:
  mcu: MSP430G2X[0/3]2
  leds: null
  display: 0.96" Nokia 5110 LCD (PCD8544 controller)
  connectivity: []
  inputs:
  - buttons
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/HackRVA/rvasec-badge-2012/tree/master/eagle
  firmware_url: https://github.com/HackRVA/rvasec-badge-2012/tree/master/src
  eda_tool: Eagle
  notes: Repo also includes production Gerbers, component documentation, and LCD/RJ45 graphics assets under doc/ and graphics/.
links:
- label: badge.gallery/badges/rvasec-2012-badge
  url: https://badge.gallery/badges/rvasec-2012-badge
  kind: website
- label: HackRVA/rvasec-badge-2012 (GitHub)
  url: https://github.com/HackRVA/rvasec-badge-2012
  kind: repo
images: []
contact: {}
notes:
- First RVAsec electronic conference badge, listed on badge.gallery's RVAsec credits page. Found by the event-year sweep, task con-rvasec.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/rvasec-2012-badge
  title: RVAsec 2012 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2012''.'
- kind: url
  url: https://github.com/HackRVA/rvasec-badge-2012
  title: HackRVA/rvasec-badge-2012
  accessed: '2026-09-08'
  note: 'Maker''s own repo: confirms MSP430 MCU, Nokia 5110/PCD8544 LCD, four-button interface, Eagle design files and firmware source; firmware credited to Luke Libraro in source headers.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Confirmed by both badge.gallery and the maker's own HackRVA GitHub repo. No price or quantity-made figures found anywhere; availability could not be determined (this was conference-issued hardware from 2012, not a current storefront item). No rights-cleared photo of the physical badge could be found - badge.gallery notes the same gap, and the repo's graphics/ folder holds only LCD bitmap art (e.g. babs.bmp/.gif/.psd) and RJ45/LCD documentation, not photos of the assembled board, so no images were saved. Set status to "released" (not the sheet's "listed") since this was HackRVA's badge distributed at the actual 2012 conference, per the maker's own repo description as documentation "for the RvaSec security conference for 2012."
last_modified_date: '2026-09-10'
model:
  file: assets/models/rvasec-2012/rvasec-2012-badge.glb
  method: kicad
  source_file: badge-v2.brd
  generated: '2026-09-10'
  bytes: 159456
---

The RVAsec 2012 badge was the first electronic conference badge for RVAsec, the Richmond, Virginia security conference, built by the local hackerspace HackRVA for the inaugural 2012 event. It centers on a Texas Instruments MSP430G2X[0/3]2 microcontroller driving a Nokia 5110 LCD (PCD8544 controller), with four buttons for navigation and text entry. On boot it draws RVAsec and HackRVA graphics and lets attendees type text, recognizing a handful of hidden strings ("hackrva," "anonymous," "rvasec") and a Konami-code easter egg that pops up "99 LIVES!" The board also carries two RJ45 connectors, per the maker's documentation.

HackRVA published the full design under an open hardware/firmware model: Eagle schematic and board files, production Gerbers, component documentation, and the badge's graphics assets sit alongside the firmware source in the group's `rvasec-badge-2012` GitHub repository. Source-code headers credit HackRVA member Luke Libraro as the firmware author.

No price, production quantity, or post-conference availability could be confirmed; this appears to have been badge hardware handed out at the 2012 conference rather than something sold afterward. No rights-cleared photograph of the assembled badge turned up either in the repo or on badge.gallery, which notes the same gap in its own listing.

## Make your own

The HackRVA repo (linked above) has everything needed to reproduce the board: Eagle schematic/board files and Gerbers under `eagle/`, the MSP430 firmware under `src/`, and the Nokia-LCD graphics and RJ45 pin documentation under `graphics/` and `doc/`.
