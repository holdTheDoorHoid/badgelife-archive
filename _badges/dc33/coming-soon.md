---
title: DC33 SAO
id: dc33-coming-soon
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc33
year: 2025
makers:
- name: Rare Circuits
summary: A companion SAO for the DC33 Aerospace Village ADS-B badge that adds air-band VHF and stereo FM radio reception plus its own fast OLED display.
functions: Receives and plays air-band VHF audio over an onboard 3.5mm jack, receives broadcast FM radio in stereo, receives an unspecified additional radio service, and drives a 60+ FPS 4-color grayscale image on an SSD1306 OLED.
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
  - hardware tool
tech:
  mcu: null
  leds: null
  display: SSD1306 OLED
  connectivity:
  - audio
  battery: powered by host badge
  sao_version: null
get_one:
  price: $80
  price_usd: 80.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  - village
  where: Sold by Aerospace Village alongside their $160 DC33 ADS-B badge at DEF CON 33; also listed on the Aerospace Village website as a standalone $80 add-on.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: Aerospace Village - DC33 Badge (includes DC33 SAO)
  url: https://www.aerospacevillage.org/dc33-badge
  kind: website
- label: "The Aerospace Village DC33 Badge (HamRadio.my writeup)"
  url: https://hamradio.my/aerospace-village-dc33-badge/
  kind: article
images:
- file: assets/images/badges/dc33/coming-soon/e5717a9a23.jpg
  source: "https://www.aerospacevillage.org/dc33-badge"
  credit: "Aerospace Village / Rare Circuits"
  caption: "Front of the DC33 SAO, showing the RARE CIRCUITS logo"
- file: assets/images/badges/dc33/coming-soon/fc0b46eedc.jpg
  source: "https://www.aerospacevillage.org/dc33-badge"
  credit: "Aerospace Village / Rare Circuits"
  caption: "Back of the DC33 SAO circuit board"
contact:
  emails:
  - hcadam@proton.me
notes: []
status: released
sources:
- kind: sheet
  event: dc33
  row: 26
  updated: 7/14/2025 15:05:45
- kind: url
  url: https://www.aerospacevillage.org/dc33-badge
  title: "DC33 Badge | Aerospace Village"
  accessed: '2026-09-06'
  note: "Confirms the item's actual title ('DC33 SAO'), $80 price, maker (Rare Circuits, in collaboration with Aerospace Village), feature list, and the two product photos used above."
- kind: url
  url: https://hamradio.my/aerospace-village-dc33-badge/
  title: "The Aerospace Village DC33 Badge: A Linux SDR That Tracks Aircraft in Real Time"
  accessed: '2026-09-06'
  note: "Independent writeup corroborating the $80 price and air-band/FM/OLED feature set."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: >-
    The sheet row carried only placeholder "Coming Soon" text and a maker name (Rare Circuits);
    the maker's own DC33 Badge page names the actual product "DC33 SAO" and this entry has been
    retitled accordingly (id/filename kept as dc33-coming-soon per the sheet import). This is the
    same $80 companion SAO already described in the body/notes of dc33-aerospace-village-adsb-badge
    (row 25, same event) -- duplicate_of that entry, which covers the Aerospace Village badge it
    plugs into. The Aerospace Village page redacted two feature details ("<redacted> radio comms"
    and the OLED driving technique) rather than omitting them by accident, so those are left
    unspecified rather than guessed. MCU, LED count/type, exact quantity made, and open-source
    status were not stated by either source and are left empty. Current sell-through/availability
    at time of check was not confirmed (no separate storefront listing found), so availability is
    left unknown rather than assumed sold out.
last_modified_date: '2026-09-06'
---

Rare Circuits designed the DC33 SAO as an $80 companion add-on for Aerospace Village's DC33 ADS-B badge, sold alongside it (and the village's other DEF CON 33 offerings) at DEF CON 33 in 2025. Rather than duplicating the badge's ADS-B reception, the SAO adds a separate set of radio features: it can receive and play air-band VHF audio (the frequencies used for air traffic control and pilot communications) through an onboard 3.5mm jack, tune in stereo broadcast FM radio, and pick up at least one other radio service that Aerospace Village's own product page declined to specify in detail ahead of the con. It also carries its own SSD1306 OLED, driven fast enough (60+ FPS) to show a 4-color grayscale image using a technique the maker likewise left undocumented on the announcement page.

Because it is designed to plug into the DC33 badge, it draws power from that host rather than carrying its own battery or MCU description from the sources checked. Aerospace Village's site is also the only place that explains it was a genuine collaboration between Rare Circuits and the village, distinct from the badge itself, which the village designed and produced on its own DC32-era hardware.
