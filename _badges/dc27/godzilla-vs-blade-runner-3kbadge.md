---
title: Godzilla vs. Blade Runner (3kbadge)
id: dc27-godzilla-vs-blade-runner-3kbadge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Alt_Bier
  role: original designer
- name: r3x3r
  role: 'team: Altbier and Chill (DC27 rework)'
- name: t3hub3rk1tten
  role: 'team: Altbier and Chill (DC27 rework)'
summary: A retro sci-fi themed electronic badge with blinking LEDs, originally made for 3000 Society's 10th anniversary conference and reworked for DEF CON 27.
functions: Blinking LED lighting effects; exact interactive functions beyond "blinkey lights" are not detailed by the source.
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - movie
tech:
  mcu: Trinket M0
  leds: null
  display: null
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: 'Sold at DEF CON 27 (2019); a portion of proceeds was donated to BSides DFW.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/gowenrw/3k_badge
  firmware_url: https://github.com/gowenrw/3k_badge
  eda_tool: KiCad
links:
- label: 3kbadge.altbier.us
  url: https://3kbadge.altbier.us/
  kind: website
- label: gowenrw/3k_badge
  url: https://github.com/gowenrw/3k_badge
  kind: repo
images:
- file: assets/images/badges/dc27/godzilla-vs-blade-runner-3kbadge/049f6d6a84.jpg
  source: "https://3kbadge.altbier.us/"
  credit: "Altbier and Chill"
  caption: "Godzilla vs. Blade Runner badge, DC27 reworked version"
- file: assets/images/badges/dc27/godzilla-vs-blade-runner-3kbadge/014036c934.jpg
  source: "https://3kbadge.altbier.us/"
  credit: "Alt_Bier"
  caption: "Original 3000 Society version of the badge"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry.
- 'Sheet listed the event as ''dc2021/3000 Society 2021''; the maker''s own page dates
  the original design to 3000 Society''s 10th anniversary conference (May 31-June 1,
  2019) and a reworked version to DEF CON 27 (also 2019). No 2021 event is mentioned
  anywhere in the sources, so this appears to be a sheet transcription error. Event
  set to dc27 since that is the version with the fuller writeup and the one whose
  repo survives; the 3000 Society showing is noted here since no distinct event id
  for it was found in events.yml.'
status: released
sources:
- kind: url
  url: https://3kbadge.altbier.us/
  title: Godzilla vs. Blade Runner (3kbadge)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sheet-research-spotted); event read as ''dc2021/3000 Society 2021''.'
- kind: url
  url: https://3kbadge.altbier.us/
  title: 3kbadge.altbier.us
  accessed: '2026-09-07'
  note: 'Primary source: maker/team names, original 3000 Society 2019 origin, DC27 2019 rework by "Altbier and Chill", BSides DFW donation, and the two badge photos.'
- kind: url
  url: https://github.com/gowenrw/3k_badge
  title: gowenrw/3k_badge
  accessed: '2026-09-07'
  note: 'Repo confirms Trinket M0 MCU, KiCad PCB design files, Python firmware, and MIT license.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Could not confirm LED count/type, display, price, quantity made, or current availability from any source. Exact interactive functions beyond "blinkey lights" are not spelled out on the maker's page. Event assignment (dc27 vs. an unlisted 3000 Society id) is a judgment call; see notes above.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/godzilla-vs-blade-runner-3kbadge/
---

The Godzilla vs. Blade Runner badge is a retro sci-fi themed electronic badge originally designed by Alt_Bier for 3000 Society's 10th anniversary conference, held May 31-June 1, 2019. It was later reworked for DEF CON 27 by a team calling itself "Altbier and Chill" (Alt_Bier along with r3x3r and t3hub3rk1tten), dedicated to the DFW-area hacker communities, with a portion of proceeds from the DC27 run going to BSides DFW.

The badge runs on an Adafruit Trinket M0 microcontroller and features blinking LED effects; the maker's page does not spell out LED count/type, display, price, or how many were made. Hardware (KiCad PCB files) and firmware (Python) for the badge are published on GitHub under an MIT license, making it open source and buildable by others.
