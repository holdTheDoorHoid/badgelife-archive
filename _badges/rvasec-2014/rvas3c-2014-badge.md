---
title: RVAs3c 2014 Badge
id: rvasec-2014-rvas3c-2014-badge
layout: badge
parent: RVAsec 2014
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2014
year: 2014
makers:
- name: HackRVA
summary: An electronic badge designed and hand-manufactured by the Richmond, VA hackerspace HackRVA for RVAsec 2014, with IR badge-to-badge communication and a Nokia 5110 LCD.
functions: IR transmit/receive for badge-to-badge interaction, capacitive-touch UI, LCD-based games and menus, LED effects, and audio via an onboard speaker.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
  - wearable
tech:
  mcu: PIC32MX250F128D
  leds:
    count: 8
    type: discrete
    note: 8 yellow LEDs, per the maker's GitHub README.
  display: Nokia 5110 LCD
  connectivity:
  - ir
  - usb
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: '300'
  availability: unknown
  distribution:
  - free_drop
  where: Given to RVAsec 2014 attendees; HackRVA members etched, populated, and hand-soldered all 300 boards.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HackRVA/rvasec-badge-2014
  eda_tool: null
links:
- label: badge.gallery/badges/rvasec-2014-rvas3c-badge
  url: https://badge.gallery/badges/rvasec-2014-rvas3c-badge
  kind: website
- label: HackRVA/rvasec-badge-2014 (GitHub)
  url: https://github.com/HackRVA/rvasec-badge-2014
  kind: repo
- label: "RVAsec Badge Build 2014 (HackRVA wiki)"
  url: https://wiki.hackrva.org/index.php/RVAsec_Badge_Build_2014
  kind: doc
- label: "RVAsec Badge Build 2014 WrapUp (HackRVA blog)"
  url: https://www.hackrva.org/2014/06/rvasec-badge-build-2014-wrapup/
  kind: article
images:
  - file: assets/images/badges/rvasec-2014/rvas3c-2014-badge/ec44d9bfdb.jpg
    source: "https://github.com/HackRVA/rvasec-badge-2014"
    credit: "HackRVA"
    caption: "Completed RVAsec 2014 badges at the conference"
contact: {}
notes:
- HackRVA-built badge for RVAsec 2014, branded "RVAs3c"; firmware/programmer repo exists under the HackRVA GitHub org. (seen only in a search snippet; unconfirmed) Found by the event-year sweep, task con-rvasec.
- "Confirmed via badge.gallery, the HackRVA GitHub repo, HackRVA's wiki build log, and HackRVA's blog wrap-up. Sources agree it is a real, distributed badge, not a rumor."
- "LED count discrepancy: badge.gallery's summary says 24 LEDs, but the maker's own GitHub README says 8 yellow LEDs. Went with the maker's own repo."
- "Chip part number transcribed from GitHub README as 'PIC32MX250128D'; recorded here as PIC32MX250F128D (the likely full Microchip part number, matching the MX2xx/128D family), but this exact spelling was not independently confirmed on a datasheet page."
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/rvasec-2014-rvas3c-badge
  title: RVAs3c 2014 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2014''.'
- kind: url
  url: https://github.com/HackRVA/rvasec-badge-2014
  title: "HackRVA/rvasec-badge-2014"
  accessed: '2026-09-10'
  note: "Maker's own repo; confirms chip, LCD, IR, touch sliders, LEDs, speaker, USB, and final_badges_at_conf.jpg photo."
- kind: url
  url: https://wiki.hackrva.org/index.php/RVAsec_Badge_Build_2014
  title: "RVAsec Badge Build 2014 - HackRVA wiki"
  accessed: '2026-09-10'
  note: "Build-process account: badges etched, pick-and-placed, and soldered by HackRVA members from bare copper."
- kind: url
  url: https://www.hackrva.org/2014/06/rvasec-badge-build-2014-wrapup/
  title: "RVAsec Badge Build 2014 WrapUp - hack.RVA"
  accessed: '2026-09-10'
  note: "States 300 badges were made over several months; source of the two blog photo URLs (both since 404)."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-10'
  notes: "Confirmed as a real, distributed badge. Price was not stated anywhere found (likely given free with conference registration, consistent with distribution: free_drop). No separate hardware/PCB repo or Gerbers were found beyond the firmware/programmer repo linked above, so open_source is 'partial'. The two photo URLs embedded in HackRVA's 2014 blog post are now dead (404); recovered one photo instead from the GitHub repo's own README image."
last_modified_date: '2026-09-10'
---

The RVAs3c badge was HackRVA's second electronic badge for RVAsec, built for the 2014 Richmond, VA security conference. Roughly 300 units were etched, populated, and hand-soldered by HackRVA members from bare copper boards over several months, then given out to conference attendees. The badge is built around a PIC32MX250F128D microcontroller driving a Nokia 5110 LCD, with two capacitive-touch sliders, a button, eight yellow LEDs, a speaker, infrared transmit/receive hardware for badge-to-badge interaction, and a micro-USB connector.

HackRVA's stated goal was to make the badge worthwhile after the conference ended: attendees kept the hardware, and the firmware/programmer source was released publicly on GitHub so people could keep hacking on it. No separate hardware design files (schematics, Gerbers, BOM) were found alongside the firmware repo, so the project is only partially open source.

## Make your own

Firmware and programmer source, plus component datasheets, are published at HackRVA's GitHub repo (linked above). No hardware design files were located during this research pass.
