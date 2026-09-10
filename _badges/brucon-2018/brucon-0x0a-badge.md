---
title: BruCON 0x0A Badge
id: brucon-2018-brucon-0x0a-badge
layout: badge
parent: BruCON 0x0A
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: brucon-2018
year: 2018
makers:
- name: Jean-George (Jegeva)
  url: https://github.com/Jegeva
summary: The official electronic badge for BruCON 0x0A (2018), an ESP32-based badge with a Nokia 6100 LCD, Wi-Fi schedule sync, and a built-in alcohol sensor.
functions: Displays the conference schedule (refreshed on reboot) and a venue map, and reminds attendees about upcoming talks and workshops via a menu on its LCD. Also includes an alcohol-sensor mode and battery-voltage monitoring.
look:
  colors: []
  shape: null
  themes:
  - security
  - drink
tech:
  mcu: ESP32
  leds: null
  display: Nokia 6100 LCD
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to BruCON 0x0A (2018) conference attendees.
make_your_own:
  open_source: true
  hardware_url: https://github.com/Jegeva/BruCONbadge2018/tree/master/pcb
  firmware_url: https://github.com/Jegeva/BruCONbadge2018
  eda_tool: KiCad
links:
- label: badge.gallery/badges/brucon-2018-badge
  url: https://badge.gallery/badges/brucon-2018-badge
  kind: website
- label: github.com/Jegeva/BruCONbadge2018
  url: https://github.com/Jegeva/BruCONbadge2018/
  kind: repo
- label: archive.brucon.org/2019/2018/10/09/brucon-0x0a-is-over-and-it-was-awesome
  url: https://archive.brucon.org/2019/2018/10/09/brucon-0x0a-is-over-and-it-was-awesome/
  kind: website
images: []
contact: {}
notes:
- Official 10th-edition BruCON electronic badge with schedule/venue-map/reminder functions and a built-in alcohol sensor, ESP-IDF/KiCad based. Found by the event-year sweep, task con-brucon.
- The discovery sweep's page title read simply "BruCON 0x0A badge"; the maker's own README titles the repo "BruCon badge 2018" with no other stated product name, so the existing title was kept.
status: released
sources:
- kind: url
  url: https://badge.gallery/badges/brucon-2018-badge
  title: BruCON 0x0A Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-brucon); event read as ''BruCON 2018''.'
- kind: url
  url: https://github.com/Jegeva/BruCONbadge2018/
  title: Jegeva/BruCONbadge2018
  accessed: '2026-09-08'
  note: Maker's own repo; confirms ESP-IDF/ESP32 firmware, KiCad PCB, and open-source hardware+firmware release, including a tagged "BruCON0xA" release matching what shipped.
- kind: url
  url: https://archive.brucon.org/2019/2018/10/09/brucon-0x0a-is-over-and-it-was-awesome/
  title: BruCon 0x0A is over.... and it was awesome!
  accessed: '2026-09-08'
  note: BruCON's own recap post naming Jean-George (@NoNonyme) as designer/firmware author, describing the schedule/venue-map functions, alcohol sensor, and last-minute volunteer assembly of batteries and screens the night before the con.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Confirmed via the maker's own GitHub repo and BruCON's own recap post, so this is a real, released badge, not just a sweep snippet. Display and MCU details came from a fetched summary of the badge.gallery page and repo folder names, not a direct read of source files, so tech.display and tech.mcu are held at medium confidence. No LED info, no price/quantity, no battery chemistry, and no images were found in the repo or on badge.gallery within the research budget; badge.gallery appears to be a JS-rendered page with no static image tags to pull from.
last_modified_date: '2026-09-10'
model:
  file: assets/models/brucon-2018/brucon-0x0a-badge.glb
  method: kicad
  source_file: pcb/BruCON_0x0a.kicad_pcb
  generated: '2026-09-10'
  bytes: 1208448
---

The BruCON 0x0A badge was the official electronic badge given to attendees of BruCON's 10th edition in 2018, in Ghent, Belgium. It was designed by Jean-George, known as Jegeva (also posting as @NoNonyme), who both laid out the ESP32-based PCB in KiCad and wrote the ESP-IDF firmware. On its Nokia 6100 LCD the badge showed the conference schedule (refreshing on reboot), a venue map, and reminders about upcoming talks and workshops, and it also doubled as a novelty alcohol-sensor gadget with battery-voltage monitoring, syncing schedule data over Wi-Fi with a PHP/MySQL backend.

Production came down to the wire: BruCON's own recap post describes volunteers helping attach batteries and screens to the badges through the night before the con while Jean-George finished the firmware, so what shipped kept its "bugs and all," per the maker's own tagged GitHub release. Both the hardware (KiCad schematics and PCB files) and firmware, along with the server-side enrollment scripts, were published afterward on GitHub, making it a fully open-source badge. No pricing applies since it was distributed free to attendees; no total production quantity was found in the available sources.

## Make your own

Hardware and firmware are both open source. Grab the KiCad project from the `pcb` folder of the [GitHub repo](https://github.com/Jegeva/BruCONbadge2018/) to build the board, and set up the ESP-IDF toolchain to build the firmware — the repo's `BruCON0xA` tagged release matches what was actually on the 2018 badges.
