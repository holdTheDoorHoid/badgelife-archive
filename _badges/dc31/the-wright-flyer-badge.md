---
title: The Wright Flyer Badge
id: dc31-the-wright-flyer-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: Aerospace Village
  url: https://www.aerospacevillage.org/
summary: A limited-edition, donation-priced badge from the Aerospace Village celebrating the group's 5th DEF CON anniversary and the 120th anniversary of the Wright Brothers' first flight.
functions: Boots as its own Wi-Fi access point and hosts hidden challenges and "Easter eggs" themed around normal and emergency flight procedures.
look:
  colors: []
  shape: null
  themes:
  - aviation
  - history
  - village badge
tech:
  mcu: ESP32-S2
  leds: null
  display: null
  connectivity:
  - wifi
  battery: null
  sao_version: null
  sao_ports: 2
get_one:
  price: "$250"
  price_usd: 250
  quantity: '50'
  availability: sold_out
  availability_note: 'Sold out on Tindie as of 2026-09-10; the listing shows "This seller is taking a break."'
  distribution:
  - purchase
  where: Sold directly by the Aerospace Village via Tindie.
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
  notes: The Aerospace Village said source code would be released after DEF CON 31; no public repo was found for this specific badge.
links:
- label: www.aerospacevillage.org/dc31-badge
  url: https://www.aerospacevillage.org/dc31-badge
  kind: website
- label: Tindie listing
  url: https://www.tindie.com/products/aero_village/aerospace-village-5th-anniversary-badge-for-dc-31/
  kind: store
- label: Hackster.io coverage
  url: https://www.hackster.io/news/aerospace-village-celebrates-120-years-of-flight-with-this-limited-edition-commemorative-badge-9b48c147144c
  kind: article
images:
  - file: assets/images/badges/dc31/the-wright-flyer-badge/60750594e5.jpg
    source: "https://www.aerospacevillage.org/dc31-badge"
    credit: "Aerospace Village"
    caption: "The Wright Flyer Badge, featuring counter-rotating propellers"
  - file: assets/images/badges/dc31/the-wright-flyer-badge/d002fdc4a7.jpg
    source: "https://www.tindie.com/products/aero_village/aerospace-village-5th-anniversary-badge-for-dc-31/"
    credit: "Aerospace Village"
    caption: "Back of The Wright Flyer Badge"
contact: {}
notes:
- Aerospace Village's $250 limited-edition (50 made) DC31 badge, distinct from their lower-tier 'Wright Stuff' donation badge already in the archive. Found by the event-year sweep, task dc31-indie; confirmed on the maker's own page, Tindie listing, and Hackster.io coverage.
status: released
sources:
- kind: url
  url: https://www.aerospacevillage.org/dc31-badge
  title: The Wright Flyer Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc31-indie); event read as ''dc31''.'
- kind: url
  url: https://www.tindie.com/products/aero_village/aerospace-village-5th-anniversary-badge-for-dc-31/
  title: Aerospace Village 5th Anniversary Badge for DC 31
  accessed: '2026-09-10'
  note: Confirmed price ($250), quantity (50), sold-out status, and back-of-badge photo.
- kind: url
  url: https://www.hackster.io/news/aerospace-village-celebrates-120-years-of-flight-with-this-limited-edition-commemorative-badge-9b48c147144c
  title: 'Aerospace Village Celebrates 120 Years of Flight with This Limited Edition Commemorative Badge'
  accessed: '2026-09-10'
  note: Third-party press coverage corroborating the maker's page (fetch returned 403, listed via search snippet only).
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'LED count, display, and battery are not mentioned in any source found and are left empty. No public hardware/firmware repo was located despite the maker''s stated intent to release source after DEF CON 31 -- possibly released later under a different name or not published. Hackster.io article could not be directly fetched (403); its content was read via search snippet only.'
last_modified_date: '2026-09-10'
---

The Wright Flyer Badge is a limited-edition electronic badge released by the Aerospace Village for DEF CON 31 (2023), marking both the group's 5th anniversary at DEF CON and the 120th anniversary of the Wright Brothers' first powered flight. The design is inspired by the iconic photograph of that first flight on December 17, 1903, and includes two counter-rotating propellers echoing the Wrights' original aircraft design.

Built around an ESP32-S2, the badge functions as its own Wi-Fi access point and hosts embedded challenges and "Easter eggs" themed around normal and emergency flight procedures, tying its gameplay to real aviation safety concepts. It carries two SAO headers for stacking add-ons from other makers. Only 50 units were made, sold directly through the Aerospace Village's Tindie storefront for $250 each as a way to fund the village's ongoing work; the listing is now sold out.

This badge is distinct from the Aerospace Village's other, lower-tier DC31 badge, "The Wright Stuff," which is a separate entry in this archive. The Aerospace Village stated that source code for the badge would be released after DEF CON 31, but no public repository specific to this badge was located during this research pass.
