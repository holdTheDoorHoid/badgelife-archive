---
title: Sputnik (OpenBeacon)
id: cccamp-2007-sputnik-openbeacon
layout: badge
parent: Chaos Communication Camp 2007
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: cccamp-2007
year: 2007
makers:
- name: Milosch Meriac / OpenBeacon project (Bitmanufaktur)
  url: http://www.openbeacon.org
summary: An active 2.4GHz RFID tag handed out at Chaos Communication Camp 2007 for real-time attendee tracking, built on the open-source OpenBeacon platform.
functions: 'Broadcasts a 2.4GHz beacon signal to fixed and mesh OpenBeacon reader stations for camp-wide proximity tracking. A hardware push button doubles as a "mood measurement" input: pressing it one to four times in a row records an enjoyment level, which was mapped into a live display of joy across the camp grounds. Tags brought back from the prior year (23C3) could be reflashed with new firmware at the project table.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - hardware tool
  - security
tech:
  mcu: PIC16F684
  leds: null
  display: none
  connectivity:
  - rfid
  battery: CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 500 new v0.2 tags at the camp
  availability: free
  distribution:
  - free_drop
  where: Handed out / sold at the Sputnik project table in the Art & Beauty shelter at CCCamp 2007; prior-year (23C3) tags could be brought back and reflashed there as well.
make_your_own:
  open_source: true
  hardware_url: http://www.openbeacon.org
  firmware_url: http://www.openbeacon.org
  eda_tool: null
  license: GNU General Public License (firmware)
  notes: Both the OpenBeacon reader (USB stick, 32-bit ARM) and the Sputnik tag firmware were released under the GPL; hardware/firmware are on the OpenBeacon project site rather than a single repo link.
links:
- label: events.ccc.de/camp/2007/Sputnik
  url: https://events.ccc.de/camp/2007/Sputnik/
  kind: website
  archived: https://web.archive.org/web/20260912180012/https://events.ccc.de/camp/2007/Sputnik/
- label: OpenBeacon project site
  url: http://www.openbeacon.org
  kind: website
  archived: https://web.archive.org/web/20260908080806/https://www.openbeacon.org/
- label: 'CCC Sputnik lecture: "Inside Sputnik & OpenBeacon - Smart Dust for the Masses"'
  url: https://fahrplan.events.ccc.de/camp/2007/Fahrplan/events/1955.en.html
  kind: video
  archived: https://web.archive.org/web/20260213095858/https://fahrplan.events.ccc.de/camp/2007/Fahrplan/events/1955.en.html
- label: CCC Sputnik @ CCCamp 2007 - lecture slides
  url: https://fahrplan.events.ccc.de/camp/2007/Fahrplan/attachments/1337-Sputnik%20Slides
  kind: doc
  archived: https://web.archive.org/web/20260912180146/https://fahrplan.events.ccc.de/camp/2007/Fahrplan/attachments/1337-Sputnik%20Slides
images:
- file: assets/images/badges/cccamp-2007/sputnik-openbeacon/926571eeee.jpg
  source: https://events.ccc.de/camp/2007/Sputnik/
  credit: CCC / OpenBeacon project
  caption: Sputnik tag v0.2 held in a hand
  archived: https://web.archive.org/web/20260912180012/https://events.ccc.de/camp/2007/Sputnik/
- file: assets/images/badges/cccamp-2007/sputnik-openbeacon/300bdc13f4.jpg
  source: https://events.ccc.de/camp/2007/Sputnik/
  credit: CCC / OpenBeacon project
  caption: OpenBeacon USB reader node with Sputnik tags
  archived: https://web.archive.org/web/20260912180012/https://events.ccc.de/camp/2007/Sputnik/
contact: {}
notes:
- Active 2.4GHz RFID badge distributed to CCCamp 2007 attendees, built on the OpenBeacon platform for real-time camp tracking and post-camp hardware hacking. Found by the event-year sweep, task cccamp.
- The sweep's notes line called it a generic "active RFID badge"; the CCC event page and OpenBeacon project material both use the name "Sputnik" for the tag and describe it as part of the CCC Sputnik / OpenBeacon project. Kept the sweep's title, which already matches the maker's naming.
status: released
sources:
- kind: url
  url: https://events.ccc.de/camp/2007/Sputnik/
  title: Sputnik (OpenBeacon)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:cccamp); event read as ''cccamp-2007''.'
  archived: https://web.archive.org/web/20260912180012/https://events.ccc.de/camp/2007/Sputnik/
- kind: url
  url: https://fahrplan.events.ccc.de/camp/2007/Fahrplan/events/1955.en.html
  title: Inside Sputnik & OpenBeacon - Smart Dust for the Masses
  accessed: '2026-09-08'
  note: 'Confirmed tag hardware: PIC16F684 MCU, NRF24L01 2.4GHz RF chip, CR2032 battery, LED and touch-sensor pads, quartz timing for meshing; no price was published for attendees.'
  archived: https://web.archive.org/web/20260213095858/https://fahrplan.events.ccc.de/camp/2007/Fahrplan/events/1955.en.html
- kind: url
  url: https://hackaday.com/2007/10/01/
  title: 'OpenBeacon: Active RFID Tag'
  accessed: '2026-09-08'
  note: Independent confirmation that OpenBeacon tags (the CCC Sputnik tag family) use a PIC16F684 and 2.4GHz transceiver.
  archived: https://web.archive.org/web/20260912180258/https://hackaday.com/2007/10/01/
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: No price was ever published; it appears the tags were distributed as part of camp participation rather than sold at a stated price, so get_one.price is left blank and availability set to free. LED count/type and exact "gold-plated pads" cosmetic detail were mentioned but no further LED spec was given, so tech.leds is left null. Sources agree on the core facts (maker, event, hardware, open-source firmware).
last_modified_date: '2026-09-08'
---

Sputnik was an active 2.4GHz RFID tag handed out to attendees of Chaos Communication Camp 2007, continuing a project the CCC had run the previous year at 23C3. Built on Milosch Meriac's open-source OpenBeacon platform (a PIC16F684 microcontroller paired with a Nordic nRF24L01 2.4GHz radio, running off a single CR2032 cell), the v0.2 tag added gold-plated contact pads, a hardware push button in place of the earlier touch sensor, and an optional buzzer interface, all packaged in a small round plastic case. Roughly 500 new tags were made available at the camp, and attendees who still had their tag from the prior year could bring it back and reflash it with updated firmware at the project's table in the Art & Beauty shelter.

Functionally, Sputnik tags beaconed to a network of fixed and wireless mesh OpenBeacon reader stations scattered across the campground (including in trees) to demonstrate both the utility and the privacy risks of large-scale RFID tracking and data mining. The push button doubled as a lighthearted "camp mood" sensor: pressing it one to four times in a row logged a self-reported enjoyment level, which organizers turned into a live map of "joy bubbles" across the site. The project was also the subject of a camp lecture, "Inside Sputnik & OpenBeacon - Smart Dust for the Masses."

Both the OpenBeacon reader firmware and the Sputnik tag firmware were released under the GNU General Public License, and the hardware designs live on the OpenBeacon project site rather than in a single dedicated repository.
