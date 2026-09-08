---
title: RVAsec 2020 Badge
id: rvasec-2020-rvasec-2020-badge
layout: badge
parent: RVAsec 2020
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: rvasec-2020
year: 2020
makers:
- name: HackRVA
  url: https://www.hackrva.org/badge/
summary: A PIC24-based electronic badge built by HackRVA for RVAsec 2020, with an LCD, RGB LED, IR send/receive, and a small custom C interpreter attendees could program over USB.
functions: Runs user-written C programs uploaded over USB serial through a badge-hosted interpreter; supports IR send/receive between badges, button/D-pad navigation, RGB "flare" LED effects, and timer-based PWM audio playback.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: PIC24
  leds: null
  display: LCD (framebuffer)
  connectivity:
  - usb
  - ir
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Distributed to RVAsec attendees by HackRVA (Richmond, VA hacker community), who has made a badge for RVAsec nearly every year.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/HackRVA/badge2020
  eda_tool: null
links:
- label: github.com/HackRVA/badge2020
  url: https://github.com/HackRVA/badge2020
  kind: repo
- label: HackRVA badge page
  url: https://www.hackrva.org/badge/
  kind: website
- label: HackRVA wiki - RVAsec Badge Builds
  url: https://wiki.hackrva.org/index.php/RVAsec_Badge_Builds
  kind: doc
images:
  - file: assets/images/badges/rvasec-2020/rvasec-2020-badge/b81a6bd490.jpg
    source: "https://www.hackrva.org/badge/"
    credit: "HackRVA"
    caption: "The 2020 RVAsec badge, HackRVA's first badge year"
  - file: assets/images/badges/rvasec-2020/rvasec-2020-badge/1e186dfe56.jpg
    source: "https://www.hackrva.org/badge/"
    credit: "HackRVA"
    caption: "RVAsec badge PCBs during assembly"
contact: {}
notes:
- Badge firmware built for RVAsec 2020, though the in-person conference/soldering parties did not happen due to COVID distancing. Found by the event-year sweep, task con-rvasec.
- The sweep's sources list titled the repo "RVAsec 2020 Badge"; GitHub's own repo description reads "HackRVA 2020 RVASEC badge firmware," and the README file itself is named badge2019interp ("Software for the HackRVA 2020 badge"), suggesting the 2020 board reused the 2019 firmware base. Kept the sheet's title since it matches the event and is how the archive's own naming convention already reads other years in this series.
status: listed
sources:
- kind: url
  url: https://github.com/HackRVA/badge2020
  title: RVAsec 2020 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-rvasec); event read as ''RVAsec 2020''.'
- kind: url
  url: https://github.com/HackRVA/badge2020
  title: HackRVA/badge2020 GitHub repo (README)
  accessed: '2026-09-08'
  note: Confirms maker (HackRVA), event/year, PIC24 MCU, LCD/framebuffer, USB bootloader, IR, RGB LED, custom C interpreter for user apps; open-source firmware.
- kind: url
  url: https://www.hackrva.org/badge/
  title: Badge - hack.RVA
  accessed: '2026-09-08'
  note: HackRVA's own badge page confirms "our first badges, back in 2020, were much simpler" with a period photo of badges under assembly; source of the two saved images.
- kind: url
  url: https://wiki.hackrva.org/index.php/RVAsec_Badge_Builds
  title: RVAsec Badge Builds - HackRVA wiki
  accessed: '2026-09-08'
  note: Confirms "RVASec 2020 did not happen [in person], but we had some of the badge started," consistent with the notes field; no hardware distribution details given.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: The maker's own firmware repo and badge page confirm this badge is real and was built for RVAsec 2020 by HackRVA, and that at least some boards were assembled (soldering-party photos). However, because the in-person 2020 conference did not happen, no source states final production quantity, price, or how many badges actually reached attendees versus staying half-built; hardware design files (schematic/PCB) were not found, only firmware. LED count/type and battery/power are not stated anywhere found. Left those fields empty rather than guessed.
last_modified_date: '2026-09-08'
---

HackRVA, the Richmond, Virginia hacker community that has built a badge for RVAsec nearly every year, built the 2020 edition around a PIC24 microcontroller with an LCD framebuffer display, RGB LED, IR transceiver, and a USB bootloader. Its signature feature carries over from earlier RVAsec badges in the same firmware lineage: a small, deliberately limited C interpreter running on the badge itself, so attendees could write short programs on a laptop and beam or upload them onto the badge over USB serial to run.

The 2020 RVAsec conference did not happen in person because of COVID-19 distancing measures, and HackRVA's own wiki notes that the badge build was already underway when that happened ("we had some of the badge started. But we could not do soldering parties while socially distanced"). Photos on HackRVA's badge page from the same period show boards silkscreened "rvasec" partway through hand assembly, so at least some units were built, but no source found states how many were completed, sold, or given away, or what a finished unit cost.

## Make your own

Firmware source, a Makefile-based build, and USB bootloader tools (`tools/bootloadit`, `tools/sendbadge.py`) are published at github.com/HackRVA/badge2020. No PCB schematic, Gerbers, or bill of materials were found in that repository or elsewhere, so hardware files are not confirmed available; open-source status is recorded as partial (firmware only) on that basis.
