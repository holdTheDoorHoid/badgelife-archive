---
title: The Last HOPE Attendee Meta-Data (AMD) Badge
id: hope-2008-the-last-hope-attendee-meta-data-amd-badge
layout: badge
parent: Hope 2008
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: hope-2008
year: 2008
makers:
- name: HOPE conference organizers (hope.net)
summary: 'An RFID-tagged conference badge for The Last HOPE (2008) that let attendees register interest tags for location-based, on-site social networking.'
functions: 'Attendees could add "interest" tags to their badge profile; the RFID system used this metadata plus location within the venue to help connect people with shared interests in person.'
look:
  colors: []
  shape: null
  themes:
  - radio
  - security
tech:
  mcu: null
  leds: null
  display: null
  connectivity:
  - rfid
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: 'Given to attendees at The Last HOPE (2008); an RFID-free badge was available on request for attendees who did not want to be tracked.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2008/07/18/the-trackable-last-hope-conference-badge
  url: https://hackaday.com/2008/07/18/the-trackable-last-hope-conference-badge/
  kind: article
- label: www.thelasthope.org/amd.php
  url: http://www.thelasthope.org/amd.php
  kind: website
images:
  - file: assets/images/badges/hope-2008/the-last-hope-attendee-meta-data-amd-badge/09ba307e98.jpg
    source: "https://hackaday.com/2008/07/18/the-trackable-last-hope-conference-badge/"
    credit: "Hackaday"
    caption: "The Last HOPE AMD RFID badge, as pictured in Hackaday's 2008 coverage"
contact: {}
notes:
- RFID-tagged badge enabling attendees to register interest tags and get location-based networking/tracking at the conference; individual designer not credited in the article, only the project name (AMD) and hope.net contact.
- Hackaday's 2008 writeup describes a "tombstonian" (rectangular, tombstone-like) badge shape but does not give exact chip model, LED count, or production numbers. The official project page (thelasthope.org/amd.php) could not be reached: modern TLS on that host presents a hope.net wildcard certificate that does not match the www.thelasthope.org hostname, and no Wayback Machine snapshot of /amd.php exists (Internet Archive itself returned a "temporarily offline" error during this check).
status: listed
sources:
- kind: url
  url: https://hackaday.com/2008/07/18/the-trackable-last-hope-conference-badge/
  title: The Last HOPE Attendee Meta-Data (AMD) Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: bsides-regional (US regional hacker cons: BSides variants, ShmooCon, Thotcon, CypherCon, DerbyCon, CarolinaCon, GrrCON, ToorCon, HOPE, CactusCon, WWHF, Circle City Con, Layer8, Blue Team Con, ShellCon, NorthSec, Hackfest)); event read as ''The Last HOPE (New York, 2008)''.'
- kind: url
  url: https://hackaday.com/2008/07/18/the-trackable-last-hope-conference-badge/
  title: 'The trackable Last HOPE conference badge'
  accessed: '2026-09-07'
  note: 'Confirmed event/year, RFID interest-tag/location-based networking concept, opt-out (chip-free badge on request), and pulled the badge photo (hope-badge-rfid.jpg) from the article.'
research:
  status: researched
  confidence: low
  last_checked: '2026-09-07'
  notes: 'Confirmed via Hackaday only; the maker''s own project page (thelasthope.org/amd.php) was unreachable (certificate mismatch, and no Wayback snapshot exists). Could not confirm chip/MCU, LEDs, exact quantity made, or a named individual designer. Left tech.* fields empty rather than guess.'
last_modified_date: '2026-09-07'
---

The Last HOPE Attendee Meta-Data (AMD) badge was an RFID-tagged conference badge distributed to attendees of The Last HOPE, held in New York City in July 2008. It was built around an "Attendee Meta-Data" concept: badge-holders could register personal interest tags, and the conference's RFID infrastructure used those tags together with an attendee's location in the venue to surface potential connections with other attendees who shared the same interests — an attempt to bring social-networking-style matching into in-person conference socializing.

Because the badge doubled as a location-tracking device, HOPE organizers built in an opt-out: attendees uncomfortable with being tracked could request a badge without the RFID chip. Hackaday's contemporary coverage credits the project to the HOPE organization generally (via the hope.net contact address) rather than crediting an individual designer, and does not give a chip model, LED details, or production numbers, so those fields are left empty here.
