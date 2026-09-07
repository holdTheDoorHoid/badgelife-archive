---
title: sloth badge
id: other-sloth-badge-pin
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2017
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A wearable sloth-shaped blinky pin (not an SAO) built around an ATtiny13A driving 12 charlieplexed LEDs, entered in Hackaday.io's Coin Cell Challenge in November 2017.
functions: Button-driven menu of LED animations, replicating the menu tricks of Pimoroni's Bearables badges; optimized for very low power draw (~0.1uA in power-down mode).
look:
  colors: []
  shape: null
  themes:
  - animal
  - pin
  - wearable
tech:
  mcu: ATtiny13A
  leds:
    count: 12
    type: charlieplexed
    note: ''
  display: null
  connectivity: []
  battery: coin cell
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Sloth%20Badge/REV1
  firmware_url: ''
  eda_tool: Eagle
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/28330-sloth-badge
  url: https://hackaday.io/project/28330-sloth-badge
  kind: hackaday
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/Sloth%20Badge
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Sloth%20Badge
  kind: repo
images:
  - file: assets/images/badges/other/sloth-badge-pin/89540fe526.png
    source: "https://hackaday.io/project/28330-sloth-badge"
    credit: "davedarko"
    caption: "The sloth badge pin, front view"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/28330-sloth-badge
  title: Sloth Badge - Hackaday.io project by davedarko
  accessed: '2026-09-07'
  note: Primary source; confirms maker, Nov 2017 date, Coin Cell Challenge entry, ATtiny13A, 12 charlieplexed LEDs, power figures, and mentions REV1 design/firmware files.
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Sloth%20Badge/REV1
  title: Simple-Add-ons-SAO/Sloth Badge/REV1 at main
  accessed: '2026-09-07'
  note: Confirms schematic/board files (sloth_final.sch, sloth_final.brd) and a PDF are published; no firmware source file or license file visible in this directory listing.
- kind: url
  url: https://raw.githubusercontent.com/davedarko/Simple-Add-ons-SAO/main/README.md
  title: davedarko/Simple-Add-ons-SAO README
  accessed: '2026-09-07'
  note: 'Fact-check pass: the repo README''s own design table lists the Sloth Badge as an Eagle-format design, not KiCad as the previous pass had recorded. Corrected eda_tool to Eagle on this basis (maker''s own repo outranks the file-extension guess).'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): corrected two errors from the prior research pass. (1) eda_tool was recorded as KiCad, but the maker''s own Simple-Add-ons-SAO README design table lists the Sloth Badge as Eagle format; corrected to Eagle. (2) The second saved image (53806e794d.jpg, captioned "Sloth badge project photo") was a rectangular PCB render with a button, DIP-8 socket and 6-pin ISP header that does not match the sloth-shaped board and does not appear among any image URLs on the cited Hackaday project page (checked every cdn.hackaday.io image referenced there); it was not verifiably from this project, so the image and its file were removed. Also blanked firmware_url, which had been set to the same REV1 folder URL as hardware_url even though that folder contains no firmware source file. Everything else checked out: maker, Nov 2017 date, Coin Cell Challenge entry, ATtiny13A, 12 charlieplexed LEDs, coin-cell battery, the button-menu/animations description and Bearables comparison, the 0.1uA/1.1mA power figures, and the remaining image (89540fe526.png) all confirmed against the Hackaday project page and GitHub repo. This was a Hackaday.io "Coin Cell Challenge" contest entry, not a badgelife con badge, so it has no matching id in events.yml and event is left as "other". No evidence found of it being sold, given away, or produced in quantity beyond the maker''s own prototype(s); price, quantity, and distribution remain unconfirmed and blank.'
last_modified_date: '2026-09-07'
---

The sloth badge is a wearable, sloth-shaped blinky pin built by Hackaday.io user davedarko and posted in November 2017 as an entry to Hackaday's Coin Cell Challenge, a low-power design contest rather than a physical convention. It runs on an ATtiny13A driving 12 LEDs in a charlieplexed arrangement, with a button-driven menu of animations modeled directly on the menu system used by Pimoroni's Bearables line of badges. The project write-up frames it partly as a technical exercise in power efficiency: the maker reports getting power-down consumption down to roughly 0.1 microamp, a large improvement over the 1.1 milliamp draw he measured on an original Bearables board, achieved by working around some quirks in the ATtiny13A's sleep behavior.

Design files for a REV1 board are published in davedarko's Simple-Add-ons-SAO GitHub repository, including an Eagle schematic and board layout plus a PDF render, though no firmware source file or license was found alongside them at the time of this research, so the project is only partially open source by the archive's standard. There is no indication in the available sources that the badge was ever sold or distributed at scale — it reads as a one-off or small-batch personal project — so pricing, quantity, and distribution details are left blank rather than guessed.
