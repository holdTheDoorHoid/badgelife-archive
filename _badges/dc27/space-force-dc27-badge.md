---
title: Space Force DC27 Badge
id: dc27-space-force-dc27-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: "true"
  url: https://hackaday.io/true
summary: An independent ESP32-based electronic badge made for DEF CON 27, styled around the "Space Force" theme, with an OLED display, accelerometer, and IR transceiver.
functions: Shows status/graphics on its OLED, senses motion/orientation via an onboard accelerometer, and can send and receive signals over IR (transmitter/receiver) in addition to a strobing LED mode.
look:
  colors: []
  shape: null
  themes:
  - space
  - sci-fi
tech:
  mcu: ESP32
  leds: null
  display: 0.96" OLED
  connectivity:
  - ir
  - usb
  battery: rechargeable, with protection circuitry
  sao_version: null
get_one:
  price: "~$100"
  price_usd: 100
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: Sold directly by the maker to DEF CON 27 attendees in 2019; maker mentioned possibly bringing remaining stock to Supercon 2019.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://hackaday.io/project/166454-space-force-dc27-badge
  eda_tool: null
links:
- label: hackaday.io/project/166454-space-force-dc27-badge
  url: https://hackaday.io/project/166454-space-force-dc27-badge
  kind: hackaday
images:
- file: assets/images/badges/dc27/space-force-dc27-badge/e21518dabf.jpg
  source: "https://hackaday.io/project/166454-space-force-dc27-badge"
  credit: "true (hackaday.io)"
  caption: "Space Force DC27 badge, front view"
- file: assets/images/badges/dc27/space-force-dc27-badge/1e39be976e.jpg
  source: "https://hackaday.io/project/166454-space-force-dc27-badge"
  credit: "true (hackaday.io)"
  caption: "Space Force DC27 badge, detail view"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/166454-space-force-dc27-badge
  title: Space Force DC27 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''DEF CON 27''.'
- kind: url
  url: https://hackaday.io/project/166454-space-force-dc27-badge
  title: Space Force! DC27 Badge (Hackaday.io project page)
  accessed: '2026-09-07'
  note: Primary source for description, features (ESP32, OLED, accelerometer, IR, LEDs, USB, battery), price (~$100), sale at DEF CON 27, firmware download links, and project photos.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Maker uses the Hackaday.io username "true"; no real name disclosed on the project page.
    Only firmware archives (source + binaries/updater) are linked on the page, no PCB
    hardware files or gerbers were found, so make_your_own.open_source is "partial" rather
    than "yes". Exact quantity produced is unclear; the maker described assembling badges
    at roughly 7-8 per hour at peak and hand-soldering around 40 units of some component,
    but no total production count is stated. LED count/type not specified beyond "LEDs
    (including strobe capability)". No separate storefront, GitHub repo, or press coverage
    was found beyond the Hackaday.io project page itself; a broader web search was not
    possible this run (search budget exhausted), so confidence is medium rather than high.
last_modified_date: '2026-09-07'
---

The Space Force DC27 Badge is an independent, unofficial electronic badge built by a Hackaday.io user going by "true" for DEF CON 27 in 2019, riding the topical joke of the newly-announced U.S. Space Force. It runs on an ESP32 and packs an OLED display, an accelerometer, IR transmit/receive, and LEDs with a strobe mode, powered by a rechargeable battery with its own protection circuitry, plus USB connectivity and EN/IO0 buttons and a power switch for control.

The maker sold the badge directly to DEF CON attendees for around $100 during the con, assembling units by hand at a self-reported rate of about 7-8 per hour during peak production, with roughly 40 units of at least one component hand-soldered. Exact total production numbers were not stated. The maker considered carrying any leftover stock to Supercon later that year. Firmware source and a binary/updater package are available for download from the project page, but no PCB design files or a public repository were found, so it is only partially open source.
