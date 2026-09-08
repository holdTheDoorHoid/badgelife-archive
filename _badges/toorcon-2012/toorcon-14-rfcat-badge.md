---
title: ToorCon 14 Badge
id: toorcon-2012-toorcon-14-rfcat-badge
layout: badge
parent: ToorCon 14
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: toorcon-2012
year: 2012
makers:
- name: Great Scott Gadgets
  url: https://greatscottgadgets.com/tc14badge/
summary: A USB-controlled sub-1 GHz wireless transceiver badge built around the same CC1111 radio circuit as the IM-Me, shipped with atlas's RfCat firmware and a CC Bootloader so attendees could drive it from an interactive Python shell.
functions: Sub-1 GHz RF transmit/receive from a computer over USB, an interactive RfCat Python shell, and a specan (spectrum analysis) function; firmware is field-upgradeable without extra programming hardware via the CC Bootloader.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - hardware tool
tech:
  mcu: CC1111
  leds:
    count: 1
    type: discrete
    note: LED1 lights during bootloader mode.
  display: none
  connectivity:
  - sub-ghz
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Distributed to ToorCon 14 (San Diego, Oct 19-21, 2012) attendees; exact distribution terms not stated on the maker's page.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/mossmann/cc11xx/tree/master/tc14badge
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/badges/toorcon-14-rfcat-badge
  url: https://badge.gallery/badges/toorcon-14-rfcat-badge
  kind: website
- label: Great Scott Gadgets - ToorCon 14 Badge
  url: https://greatscottgadgets.com/tc14badge/
  kind: website
- label: cc11xx/tc14badge on GitHub
  url: https://github.com/mossmann/cc11xx/tree/master/tc14badge
  kind: repo
images:
- file: assets/images/badges/toorcon-2012/toorcon-14-rfcat-badge/f10844d30d.jpg
  source: "https://greatscottgadgets.com/tc14badge/"
  credit: "Great Scott Gadgets"
  caption: "The ToorCon 14 RfCat badge"
contact: {}
notes:
- Official ToorCon 14 (2012) badge, a USB-controlled sub-1 GHz RF transceiver running atlas's RfCat firmware with a CC Bootloader. Found by the event-year sweep, task con-toorcon.
- The maker's own page titles it simply "ToorCon 14 Badge"; the sweep's title "ToorCon 14 RfCat Badge" (also used by badge.gallery) is kept as the entry title since it is the more commonly used and disambiguating name.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/toorcon-14-rfcat-badge
  title: ToorCon 14 RfCat Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-toorcon); event read as ''ToorCon 2012''.'
- kind: url
  url: https://greatscottgadgets.com/tc14badge/
  title: ToorCon 14 Badge - Great Scott Gadgets
  accessed: '2026-09-08'
  note: Maker's own project page; confirmed chip (CC1111), features, LED behavior, GitHub hardware repo, and badge photo.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own page confirms the item, chip, firmware, and open hardware repo. Price, quantity made, and how it was distributed to attendees (free vs. purchase) are not stated anywhere found; get_one fields left mostly empty. No firmware repo link found (RfCat firmware is a separate atlas project, not linked from the badge page). Display/LED count beyond the single bootloader-mode LED not documented.
last_modified_date: '2026-09-08'
---

The ToorCon 14 Badge, made by Great Scott Gadgets for ToorCon 14 in San Diego (October 19-21, 2012), is a USB-controlled sub-1 GHz wireless transceiver rather than a typical blinky conference badge. It reuses the CC1111 radio circuit from the IM-Me devices that Great Scott Gadgets had previously repurposed for RF security research, giving attendees a pocket-sized RF tool they could plug into a computer and drive from an interactive Python shell.

The badge shipped with atlas's RfCat firmware, which exposes both transmit/receive control and a spectrum-analysis (specan) function, plus a CC Bootloader that lets the firmware be reflashed over USB without any separate programming hardware. A GoodFET-compatible connector and spring-pin test points are also present for lower-level access. A single LED (LED1) lights up to indicate bootloader mode.

Great Scott Gadgets describes the badge as entirely open source hardware and software, with contributions credited to atlas, Fergus Noble, and Adam Laurie. The hardware design files are published in the `cc11xx` GitHub repository under the `tc14badge` directory.

## Make your own

Hardware schematics and board layout are available in the [cc11xx GitHub repository](https://github.com/mossmann/cc11xx/tree/master/tc14badge). The badge runs atlas's RfCat firmware (distributed separately from the hardware repo) and can be reflashed over USB using the CC Bootloader and its `bootload.py` utility, without needing external programming hardware.
