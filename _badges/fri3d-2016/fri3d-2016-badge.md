---
title: Fri3d Camp 2016 Badge
id: fri3d-2016-fri3d-2016-badge
layout: badge
parent: Fri3d Camp 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: fri3d-2016
year: 2016
makers:
- name: Christophe VG / Fri3d Camp
  url: https://github.com/christophevg/Fri3dBadge2016
summary: An Arduino-compatible badge for Fri3d Camp 2016, built around an Arduino Pro Micro-style ATmega32U4 board with an IR transmitter/receiver and an RGB LED for a simple wireless badge network.
functions: Fri3d Camp 2016 app for IR-based interaction between badges, an included TV-B-Gone implementation, and RGB LED feedback; doubles as a general-purpose Arduino Micro dev board after the event.
look:
  colors: []
  shape: null
  themes:
  - learn to solder
  - hardware tool
tech:
  mcu: ATmega32U4
  leds: 
    count: 1
    type: RGB
    note: single RGB LED for status/feedback
  display: none
  connectivity:
  - ir
  - usb
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: distributed to attendees of Fri3d Camp 2016 (~300 people)
make_your_own:
  open_source: yes
  hardware_url: https://github.com/christophevg/Fri3dBadge2016/tree/master/design/eagle
  firmware_url: https://github.com/christophevg/Fri3dBadge2016/tree/master/src
  eda_tool: Eagle
links:
- label: christophe.vg/makes/Fri3d-Badge
  url: https://christophe.vg/makes/Fri3d-Badge
  kind: website
- label: github.com/christophevg/Fri3dBadge2016
  url: https://github.com/christophevg/Fri3dBadge2016
  kind: repo
images:
  - file: assets/images/badges/fri3d-2016/fri3d-2016-badge/8beffea458.jpg
    source: "https://github.com/christophevg/Fri3dBadge2016"
    credit: "Christophe VG"
    caption: "Fri3d Camp 2016 badge, v2 board render"
  - file: assets/images/badges/fri3d-2016/fri3d-2016-badge/ad98e3f26a.jpg
    source: "https://github.com/christophevg/Fri3dBadge2016"
    credit: "Christophe VG"
    caption: "Fri3d Camp 2016 badge, v1 board render"
contact: {}
notes:
- The discovery sweep's title was "Fri3d 2016 Badge"; the maker's repo and site call it the "Fri3d Camp Badge" / "Fri3d Camp 2016 Badge", used here.
- Price and quantity produced are not stated in the sources checked; badge was made for Fri3d Camp 2016 attendees (event is generally sized around a few hundred people, but no exact figure is confirmed in sources read).
status: released
sources:
- kind: url
  url: https://christophe.vg/makes/Fri3d-Badge
  title: Fri3d 2016 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:fri3d); event read as ''fri3d-2016''. Page returned a Cloudflare challenge on re-check and could not be read directly.'
- kind: url
  url: https://github.com/christophevg/Fri3dBadge2016
  title: "christophevg/Fri3dBadge2016 (GitHub, archived)"
  accessed: '2026-09-08'
  note: Confirmed maker, event/year, MCU (ATmega32U4/Arduino Pro Micro style), IR transmitter/receiver, RGB LED, USB programming, and open hardware (Eagle) + firmware files. Repo is archived (read-only) as of 2023-10-28.
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-08'
  notes: Fact-check pass (2026-09-08) re-fetched the GitHub repo, its design/eagle and src subfolders, the design/media image folder, and the repo README, confirming maker, event/year, MCU (Arduino Micro/ATmega32U4), IR tx/rx, RGB LED, USB, the open Eagle hardware files and firmware/bootloader files, and the "Fri3d Camp 2016 app" for IR badge-to-badge interaction plus the TV-B-Gone tribute described in the body and functions field. The design/media folder was confirmed to contain fri3d-badge-v1.png and fri3d-badge-v2.png, matching the two saved images' captions. The maker's own christophe.vg page still returns a Cloudflare JS challenge to both WebFetch and curl and could not be read directly, but a search-engine snippet of https://christophe.vg/ independently corroborates the maker, "300 participants," and the infrared feature, consistent with what's already in the entry. Price, exact quantity, and distribution method remain unstated in any source read and are correctly left empty. No photos of an assembled badge were found, only the two board renders used.
last_modified_date: '2026-09-08'
---

The Fri3d Camp 2016 badge was designed by Christophe VG together with the Fri3d Camp organization for the 2016 edition of the Belgian hacker/maker camp. It is built as a near-clone of the Arduino Pro Micro (3.3V/8MHz, ATmega32U4), programmable over micro-USB straight from the Arduino IDE, with an infrared transmitter and receiver added to let badges talk to each other wirelessly, plus a single RGB LED for status feedback.

Software included a dedicated Fri3d Camp 2016 app using the IR link, a TV-B-Gone implementation (a nod to Mitch Altman's project, one of the badge's stated inspirations), and a helper library for the onboard extras. The hardware and firmware are fully open: the GitHub repository contains Eagle schematics, board files, and Gerbers-adjacent design files, along with a "design journal" chronicling the creator's first SMD-based board project. The repository has since been archived (read-only) by GitHub as of October 2023, but remains available for reference.

## Make your own

Eagle CAD schematic and board files, plus source firmware for the Arduino IDE, are in the [Fri3dBadge2016 repository](https://github.com/christophevg/Fri3dBadge2016), under `design/eagle` and `src` respectively. The badge is designed to be built and programmed like a standard Arduino Micro, with the IR and RGB LED functionality added via the project's own library.
