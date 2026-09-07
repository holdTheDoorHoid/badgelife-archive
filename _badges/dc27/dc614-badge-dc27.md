---
title: DC614 Badge (DC27)
id: dc27-dc614-badge-dc27
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: DC614
  url: https://github.com/dc614
summary: 'A DEF CON 27 unofficial badge built around an Orange Pi Zero single-board computer, cut into an Ohio-outline PCB shield with onboard wireless pentesting radios and an amplified speaker.'
functions: 'Boots a custom Linux image from a microSD card; carries a Ralink RT5370 Wi-Fi adapter and an nRF24LU1p (CrazyRadio-compatible) 2.4GHz USB radio for wireless research use, plus an LM386-driven speaker for audio output.'
look:
  colors: []
  shape: 'state outline (Ohio)'
  themes:
  - hardware tool
  - security
  - radio
tech:
  mcu: 'Orange Pi Zero (512MB, Allwinner H2+)'
  leds: {count: 1, type: RGB, note: 'Everlight Elec 67-23/R6GHBHC-B01/2T SMD indicator LED'}
  display: null
  connectivity:
  - wifi
  - usb
  battery: 'dual 9V batteries via buckle connectors'
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/dc614/DC-27-Badge
  firmware_url: https://github.com/dc614/DC-27-Badge
  eda_tool: null
links:
- label: github.com/dc614/DC-27-Badge
  url: https://github.com/dc614/DC-27-Badge
  kind: repo
- label: DC614 GitHub org
  url: https://github.com/dc614
  kind: repo
- label: 'Hackaday: Pictorial Guide to the Unofficial Electronic Badges of DEF CON 27'
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
images:
  - file: assets/images/badges/dc27/dc614-badge-dc27/94335c0192.jpg
    source: "https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/dc614-badge-dc27/"
    credit: "DC614 / Hackaday"
    caption: "DC614 badge for DEF CON 27, front view, showing Ohio-shaped PCB with Orange Pi Zero and wireless modules"
  - file: assets/images/badges/dc27/dc614-badge-dc27/58a20c3fed.jpg
    source: "https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/dc614-badge-dc27-rear/"
    credit: "DC614 / Hackaday"
    caption: "DC614 badge for DEF CON 27, rear view, showing USB-A ports and battery buckle connectors"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/insecurityofthings/jackit
  title: DC614 Badge (DC27)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: dc26-dc27-sao-wave); event read as ''DEF CON 27''. This URL turned out to be unrelated (a MouseJack exploit tool, not a badge) — kept per record-keeping rules but not used as a source of facts.'
- kind: url
  url: https://github.com/dc614/DC-27-Badge
  title: 'GitHub - dc614/DC-27-Badge: The DC614 badge for DEF CON 27'
  accessed: '2026-09-07'
  note: 'Primary source: README with full BOM, components, assembly notes, and software build/flash instructions.'
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/dc614-badge-dc27/
  title: 'Pictorial Guide To The Unofficial Electronic Badges Of DEF CON 27 | Hackaday'
  accessed: '2026-09-07'
  note: 'Confirmed event/maker attribution and supplied front photo.'
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/dc614-badge-dc27-rear/
  title: 'DC614-badge-DC27-rear | Hackaday'
  accessed: '2026-09-07'
  note: 'Supplied rear photo.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'The original discovery-sweep link (insecurityofthings/jackit) is an unrelated MouseJack exploit tool; the real project lives at github.com/dc614/DC-27-Badge. Price, quantity made, and availability/distribution are not stated anywhere in the repo or coverage found, so those fields are left empty. No license file was found in the repo, so open_source is marked partial (hardware and firmware/build scripts are public, but no explicit license is stated).'
last_modified_date: '2026-09-07'
---

The DC614 badge was built by the DC614 hacker group (DC614 is the Columbus, Ohio DEF CON group, named for the local area code) for DEF CON 27 in 2019. Rather than a typical microcontroller badge, it uses a full Orange Pi Zero single-board computer as its brain, running a custom Linux image built from a `reconstruct.sh` script and flashed to a microSD card. The PCB itself is cut into the outline of the state of Ohio, a nod to the group's home turf.

Functionally the badge doubles as a compact wireless-research platform: it carries a Ralink RT5370 Wi-Fi adapter and an nRF24LU1p 2.4GHz USB radio (CrazyRadio-compatible, usable with tools like the unrelated MouseJack/JackIt project) soldered onto USB-A ports on the back, alongside an LM386-amplified speaker and a single RGB status LED. Power comes from two 9V batteries connected through printed buckle connectors, with 3D-printed holders recommended for the dual-battery pack.

The hardware design and build/flash scripts are published on GitHub (dc614/DC-27-Badge), making it reproducible, though no formal open-source license is stated in the repository. Sources found during this research did not state a price, production quantity, or how the badge was distributed at the con.
