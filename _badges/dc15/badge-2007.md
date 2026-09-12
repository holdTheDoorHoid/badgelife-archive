---
title: DEF CON 15 Badge (2007)
id: dc15-badge-2007
layout: badge
parent: DC15
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc15
year: 2007
makers:
- name: Joe Grand (Grand Idea Studio)
summary: The official electronic badge for DEF CON 15, a battery-powered PCB badge with a 95-LED matrix that scrolls a user-customizable text message and hides a persistence-of-vision secret message.
functions: Idle/sleep on power-up until an icon is touched. Scrolling-text mode shows a default message; a second mode lets the wearer enter a custom message (up to 16 characters) using two capacitive-touch icons to cycle and select letters. A speed-select mode sets scroll velocity (1-5). A final mode shows a hidden message via persistence-of-vision when the badge is waved through the air.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: Freescale MC9S08QG8
  leds:
    count: 95
    type: discrete
    note: Red, 0603 surface-mount, arranged in a 5-column by 19-row matrix (Avago HSMH-C192).
  display: LED matrix 5x19
  connectivity: []
  battery: 2x CR2032 3V coin cell
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: 6,800
  availability: free
  distribution:
  - free_drop
  where: Given to attendees of DEF CON 15 (Riviera Hotel and Casino, Las Vegas, August 3-5, 2007); roughly 6,800 badges were worn at the event per the designer's own account.
make_your_own:
  open_source: true
  hardware_url: https://media.defcon.org/DEF%20CON%2015/DEF%20CON%2015%20badge/
  firmware_url: https://media.defcon.org/DEF%20CON%2015/DEF%20CON%2015%20badge/Firmware/
  eda_tool: null
links:
- label: media.defcon.org/DEF%20CON%2015/DEF%20CON%2015%20badge
  url: https://media.defcon.org/DEF%20CON%2015/DEF%20CON%2015%20badge/
  kind: website
- label: Ode to the DEFCON 15 Badge (Joe Grand, PDF)
  url: https://media.defcon.org/DEF%20CON%2015/DEF%20CON%2015%20badge/DEF%20CON%2015%20-%20grand-ode_to_defcon_badge.pdf
  kind: doc
- label: DEF CON 15 badge Bill of Materials (PDF)
  url: https://media.defcon.org/DEF%20CON%2015/DEF%20CON%2015%20badge/DEF%20CON%2015%20-%20grand-bom.pdf
  kind: doc
- label: 'DEF CON 15 archive: Making of the DEF CON 15 Badge (talk)'
  url: https://www.defcon.org/html/links/dc-archives/dc-15-archive.html
  kind: article
  archived: https://web.archive.org/web/20260729075542/https://defcon.org/html/links/dc-archives/dc-15-archive.html
- label: grandideastudio.com/portfolio/other/defcon-15-badge
  url: https://grandideastudio.com/portfolio/other/defcon-15-badge/
  kind: website
images:
- file: assets/images/badges/dc15/badge-2007/2e4e3bbf57.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-15-badge/
  credit: Grand Idea Studio
  caption: DEF CON 15 badge, front
- file: assets/images/badges/dc15/badge-2007/6a6eb0d6e1.jpg
  source: https://grandideastudio.com/portfolio/other/defcon-15-badge/
  credit: Grand Idea Studio
  caption: DEF CON 15 badge variants
contact: {}
notes:
- Official DC15 electronic badge; media.defcon.org archive folder used as item page since no dedicated announcement page was verified this session. Maker per established/public badge history, not independently re-verified in this session.
- DEF CON 15 predates the earliest event covered in this archive's events.yml (DC24 onward), so no matching event id exists yet; event left as 'other'. If a dc15 event entry is added, this belongs there (DEF CON 15, Riviera Hotel and Casino, Las Vegas, August 3-5, 2007).
- Official 2007 badge built around a Freescale MC9S08QG8 MCU driving a 5x19 LED matrix for scrolling text, issued in six variants (Human, Goon, Press, Speaker, Vendor, Uber) distinguished by cutout text and soldermask color, ~6,800 units made; schematic/BOM/source published by Grand Idea Studio. Found by the event-year sweep, task dc15-all.
- This is the same badge already covered in more detail at dc15-badge-2007 ("DEF CON 15 Badge (2007)"); that entry sources media.defcon.org directly and has fuller tech/get_one fields (battery, distribution details). Flagged as a likely duplicate rather than merged or deleted, per research rules.
status: released
sources:
- kind: url
  url: https://media.defcon.org/DEF%20CON%2015/DEF%20CON%2015%20badge/
  title: DEF CON 15 Badge (2007)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: official-badges); event read as ''DEF CON 15''.'
- kind: url
  url: https://media.defcon.org/DEF%20CON%2015/DEF%20CON%2015%20badge/DEF%20CON%2015%20-%20grand-ode_to_defcon_badge.pdf
  title: Ode to the DEFCON 15 Badge
  accessed: '2026-09-07'
  note: 'Joe Grand''s own writeup: MCU (Freescale MC9S08QG8), 95-LED 5x19 matrix, two CR2032 batteries, touch-icon UI, scrolling custom-text and persistence-of-vision modes, ~6,800 badges worn, open source code/schematics on the DEFCON CD, unpopulated footprints for an MMA7260QT accelerometer and MC13191FC 802.15.4/ZigBee transceiver.'
- kind: url
  url: https://media.defcon.org/DEF%20CON%2015/DEF%20CON%2015%20badge/DEF%20CON%2015%20-%20grand-bom.pdf
  title: DEFCON 15 Circuit Board Badge Bill-of-Materials
  accessed: '2026-09-07'
  note: Confirms 95x red 0603 LEDs (Avago HSMH-C192), MC9S08QG8CFFE microcontroller, QT100 QTouch capacitive sensor, two CR2032 coin cells, and do-not-populate footprints for the accelerometer/RF transceiver.
- kind: url
  url: https://www.defcon.org/html/links/dc-archives/dc-15-archive.html
  title: DEF CON 15 archive page
  accessed: '2026-09-07'
  note: Confirms Joe Grand's talk 'Making of the DEF CON 15 Badge' at DC15 (Riviera Hotel and Casino, August 3-5, 2007) with the ode PDF as a presentation extra.
  archived: https://web.archive.org/web/20260729075542/https://defcon.org/html/links/dc-archives/dc-15-archive.html
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-15-badge/
  title: DEF CON 15 Official Electronic Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc15-all); event read as ''dc15''.'
- kind: url
  url: https://grandideastudio.com/portfolio/other/defcon-15-badge/
  title: DEF CON 15 Official Electronic Badge — Grand Idea Studio portfolio page
  accessed: '2026-09-08'
  note: Confirmed maker, MCU, LED matrix, variants, quantity (~6,800), and located schematic/BOM/assembly/firmware/source links plus badge photos.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched all three cited sources (ode PDF, BOM PDF, DC archive page) and confirmed every non-empty field and every factual sentence in the body against them - MCU (MC9S08QG8 / MC9S08QG8CFFE), 95x red 0603 LEDs (Avago HSMH-C192) in a 5x19 matrix, 2x CR2032, QT100 capacitive-touch UI with 16-character custom message and POV mode, unpopulated MMA7260QT accelerometer and MC13191FC transceiver footprints, ~6,800 badges worn, DC15 dates/venue, and the "Making of the DEF CON 15 Badge" talk. One correction made: make_your_own.open_source was "partial" but the ode PDF states plainly that "Complete source code and schematics are on the DEFCON CD and also available at" Grand Idea Studio''s site - both hardware and firmware were released, so per the guide this is "yes", not "partial"; corrected. No images were present to check. Could not find price/quantity-made figures beyond the ~6,800-worn estimate (likely attendance-driven, not a separate production figure)
    or a photo of the assembled badge (media.defcon.org hosts only PDFs here; Grand Idea Studio''s current site no longer has a dedicated DC badges page); look.shape and look.colors correctly left empty for that reason. Merged with duplicate entry ''DEF CON 15 Official Electronic Badge'' (dc15-official-electronic-badge).'
last_modified_date: '2026-09-08'
redirect_from:
- /badges/other/badge-2007/
- /badges/dc15/official-electronic-badge/
---

The DEF CON 15 badge was designed by Joe Grand (aka Kingpin) of Grand Idea Studio for the August 2007 conference at the Riviera Hotel and Casino in Las Vegas. It is a battery-powered PCB badge built around a Freescale MC9S08QG8 microcontroller, driving a matrix of 95 discrete red LEDs (5 columns by 19 rows) to display scrolling text. On power-up the badge stays asleep until the wearer touches one of two capacitive-touch icons, which step through modes: a default scrolling message, a custom-message editor (up to 16 characters, entered letter-by-letter through the two touch icons), a scroll-speed selector, and a persistence-of-vision mode that reveals a hidden message when the badge is waved through the air. It runs on two CR2032 coin-cell batteries.

Grand designed the board with unpopulated footprints for an MMA7260QT triple-axis accelerometer and an MC13191FC 2.4GHz 802.15.4/ZigBee transceiver, intended for attendees to populate and hack themselves; the firmware source and full schematics were released on the DEF CON CD and made available on Grand Idea Studio's site, and DEF CON ran a hardware-hacking table with tools and components for badge modification. Per Grand's own account, roughly 6,800 of the badges were worn at the event, and the top hacked badges were recognized at the closing award ceremony. Design documentation - schematic, PCB layout, bill of materials, and assembly drawing - remains archived on DEF CON's media server.

## Notes merged from the duplicate entry "DEF CON 15 Official Electronic Badge"

The DEF CON 15 official electronic badge, designed by Joe Grand of Grand Idea Studio, was the conference's badge for the 2007 event. It is a battery-powered PCB built around a Freescale MC9S08QG8 8-bit microcontroller driving a 95-LED array arranged in a 5x19 matrix, primarily used to scroll a short text message that attendees could customize.

Two capacitive touch sensors on the board let the wearer cycle through five operating states: the default scrolling display, a message-entry mode for typing a custom string, a scroll-speed selector, a persistence-of-vision mode that reveals a hidden image or message when the badge is waved through the air, and a sleep mode. The board also included unpopulated footprints for an optional accelerometer and RF transceiver, though these were not part of the stock badge.

Roughly 6,800 badges were made across six variants — Human, Goon, Press, Speaker, Vendor, and Uber — distinguished by cutout text and soldermask color, and handed out to the corresponding attendee categories. Grand Idea Studio published the full schematic, bill of materials, assembly drawing, test procedure, and CodeWarrior firmware source for the badge on their site.

## Make your own

Grand Idea Studio's portfolio page hosts the schematic (PDF), BOM (PDF), assembly drawing (PDF), test procedure (PDF), and the original CodeWarrior firmware project (ZIP) for anyone who wants to reproduce the badge's hardware and firmware.
