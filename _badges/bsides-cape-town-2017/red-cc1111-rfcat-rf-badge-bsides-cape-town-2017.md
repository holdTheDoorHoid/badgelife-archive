---
title: Red CC1111 RFCat RF badge (BSides Cape Town 2017)
id: bsides-cape-town-2017-red-cc1111-rfcat-rf-badge-bsides-cape-town-2017
layout: badge
parent: BSides Cape Town 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-cape-town-2017
year: 2017
makers:
- name: BSides Cape Town 2017 event team
summary: The RF half of BSides Cape Town 2017's two-badge system, a CC1111 RFCat-compatible radio board built for an 868MHz broadcast-chat challenge.
functions: Runs RFCat firmware on the CC1111 so attendees could send and receive on a broadcast-like RF chat network over 868MHz, with a hidden challenge server using a different modulation/syncword as the actual game; a Yardstick One was used by the challenge author to prototype the client/server before badges shipped.
look:
  colors:
  - red
  shape: rectangle
  themes:
  - radio
  - hardware tool
  - ctf
tech:
  mcu: CC1111
  leds: null
  display: none
  connectivity:
  - sub-ghz
  - usb
  battery: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to BSides Cape Town 2017 attendees as one of the two paired badges (with the black "flux capacitor" ESP badge); not sold.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/dogymike/cc11xx
  firmware_url: null
  eda_tool: null
links:
- label: badge.gallery/events/bsides-cape-town-2017
  url: https://badge.gallery/events/bsides-cape-town-2017
  kind: website
- label: 'SensePost: building the bsidescpt17 rfchallenge'
  url: https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
  kind: article
- label: 'BSides CPT 2017 - RFCat Challenge Server and Client Sources'
  url: https://gist.github.com/minkione/042c5792389803eec59064939f263198
  kind: repo
images:
- file: assets/images/badges/bsides-cape-town-2017/red-cc1111-rfcat-rf-badge-bsides-cape-town-2017/0695361ef8.jpg
  source: "https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/"
  credit: "SensePost / Leon Jacobs"
  caption: "Front of the red RF badge, showing the CC1111 chip, USB port, GoodFET and expansion headers, and antenna pads"
- file: assets/images/badges/bsides-cape-town-2017/red-cc1111-rfcat-rf-badge-bsides-cape-town-2017/35c4109c7f.jpg
  source: "https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/"
  credit: "SensePost / Leon Jacobs"
  caption: "Back of the red RF badge, with only test-point contacts exposed"
contact: {}
notes:
- Companion half of the 2017 two-part badge system, built around a CC1111 RFCat-compatible radio with USB port, button, and exposed RF contacts for an 868MHz broadcast-chat challenge. Found by the event-year sweep, task bsides-bsides-cape-town.
- The board's own silkscreen reads "Clone of Michael Ossmann's TC13 badge" and links to github.com/dogymike/cc11xx; it is a derivative of Great Scott Gadgets' ToorCon 14 RFCat badge (see the toorcon-2012-toorcon-14-rfcat-badge entry), rebuilt as the RF half of BSides Cape Town's badge for this challenge.
- Its companion, the black ESP8266 "flux capacitor" badge, is its own archive entry (bsides-cape-town-2017-black-flux-capacitor-esp-badge-bsides-cape-town-2017).
status: released
sources:
- kind: url
  url: https://badge.gallery/events/bsides-cape-town-2017
  title: Red CC1111 RFCat RF badge (BSides Cape Town 2017)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-cape-town); event read as ''BSides Cape Town 2017''.'
- kind: url
  url: https://sensepost.com/blog/2017/building-the-bsidescpt17-rfchallenge/
  title: 'building the bsidescpt17 rfchallenge - SensePost'
  accessed: '2026-09-10'
  note: 'Maker''s own writeup (author Leon Jacobs, SensePost) with photos of both badges; confirms the red badge''s CC1111 chip, USB port, button, exposed-contact back, that it was given to attendees, and the RF broadcast-chat challenge design.'
- kind: url
  url: https://gist.github.com/minkione/042c5792389803eec59064939f263198
  title: 'BSides CPT 2017 - RFCat Challenge Server and Client Sources'
  accessed: '2026-09-10'
  note: 'Challenge source code referenced from the SensePost post; confirms the challenge software exists publicly, though badge hardware design files were not found.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: Confirmed via the maker's (SensePost/Leon Jacobs) own blog post with photos of the badge front and back, plus badge.gallery. Price, quantity made, and any dedicated hardware repo for the BSides-specific board (vs. the general cc11xx clone repo it was built from) were not found. The badge's silkscreen credits @elasticninja, @shifttymike, @dalenunns, and @leonjza, but individual maker roles were not confirmed well enough to add as separate `makers` entries.
last_modified_date: '2026-09-10'
---

The red CC1111 badge was one half of BSides Cape Town 2017's badge, paired with a black ESP8266-based "flux capacitor" board that supplied Wi-Fi and power. Built around a CC1111 radio chip compatible with the RFCat firmware used by Great Scott Gadgets' Yardstick One and ToorCon 14 badge, the board carries a USB port, a single button, a GoodFET header, an expansion header, and antenna pads; its silkscreen names it directly as a clone of Michael Ossmann's TC13/ToorCon badge design, sourced from github.com/dogymike/cc11xx.

The badge anchored an 868MHz RF challenge built by SensePost's Leon Jacobs: attendees could run a broadcast-like chat client over the radio out of the box, with clues leading toward a separate, differently-modulated challenge server that ultimately unlocked a physical lockbox. Jacobs prototyped the challenge server and client using Yardstick One dongles before ever handling a finished badge, and published his account (with front and back photos of both badges) on the SensePost blog shortly after the event; the challenge's server/client source is also public via a community gist.

No price, production quantity, or standalone repo for the BSides-specific board revision were found; the badge was distributed free to attendees rather than sold.
