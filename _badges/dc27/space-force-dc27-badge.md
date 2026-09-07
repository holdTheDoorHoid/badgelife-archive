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
- name: 'true'
  url: https://hackaday.io/true
summary: An independent ESP32-based electronic badge made for DEF CON 27, styled around the "Space Force" theme, with an OLED display, accelerometer, and IR transceiver.
functions: Shows status/graphics on its OLED, senses motion/orientation via an onboard accelerometer, and can send and receive signals over IR (transmitter/receiver) in addition to a strobing LED mode.
look:
  colors: []
  shape: null
  themes:
  - space
tech:
  mcu: ESP32
  leds: null
  display: OLED
  connectivity:
  - ir
  - usb
  battery: rechargeable, with protection circuitry
  sao_version: null
get_one:
  price: ~$100
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
  archived: https://web.archive.org/web/20251108164206/https://hackaday.io/project/166454-space-force-dc27-badge
images:
- file: assets/images/badges/dc27/space-force-dc27-badge/e21518dabf.jpg
  source: https://hackaday.io/project/166454-space-force-dc27-badge
  credit: true (hackaday.io)
  caption: Space Force DC27 badge, front view
  archived: https://web.archive.org/web/20251108164206/https://hackaday.io/project/166454-space-force-dc27-badge
- file: assets/images/badges/dc27/space-force-dc27-badge/1e39be976e.jpg
  source: https://hackaday.io/project/166454-space-force-dc27-badge
  credit: true (hackaday.io)
  caption: Space Force DC27 badge, detail view
  archived: https://web.archive.org/web/20251108164206/https://hackaday.io/project/166454-space-force-dc27-badge
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/166454-space-force-dc27-badge
  title: Space Force DC27 Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''DEF CON 27''.'
  archived: https://web.archive.org/web/20251108164206/https://hackaday.io/project/166454-space-force-dc27-badge
- kind: url
  url: https://hackaday.io/project/166454-space-force-dc27-badge
  title: Space Force! DC27 Badge (Hackaday.io project page)
  accessed: '2026-09-07'
  note: Primary source for description, features (ESP32, OLED, accelerometer, IR, LEDs, USB, battery), price (~$100), sale at DEF CON 27, firmware download links, and project photos.
  archived: https://web.archive.org/web/20251108164206/https://hackaday.io/project/166454-space-force-dc27-badge
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: Fact-check pass (2026-09-07) against the same Hackaday.io project page found and corrected two issues from the prior draft. (1) tech.display was overstated as '0.96" OLED'; the page confirms an OLED display but never gives a size, so it was changed to just "OLED". (2) look.themes included "sci-fi", which is not supported by the page; removed, leaving only "space". (3) The body's claim that the badge rode "the topical joke of the newly-announced U.S. Space Force" was contradicted by the maker's own project log, which explains the name as an inside joke from the "Whiskey Pirates" DEF CON group at DEF CON 26, where someone yelled "SPACE FORCE" during late-night chatter; the body was corrected to reflect that origin. Everything else in the entry (MCU, IR/USB connectivity, battery/protection circuitry, ~$100 price, sale to DEF CON 27 attendees, partial open-source status, hand-assembly rate and component counts) was checked against the same page and is supported. Maker uses the Hackaday.io username "true"; no real name disclosed on the project page. Only firmware archives (source + binaries/updater) are linked, no PCB hardware files or gerbers were found, so make_your_own.open_source is "partial" rather than "yes". Exact total production quantity is not stated (left blank). LED count/type not specified. No separate storefront, GitHub repo, or press coverage was found beyond the Hackaday.io project page itself; confidence remains medium because only a single source (one page) was available.
last_modified_date: '2026-09-07'
---

The Space Force DC27 Badge is an independent, unofficial electronic badge built by a Hackaday.io user going by "true" for DEF CON 27 in 2019. The name comes from an inside joke: at DEF CON 26, in the "Whiskey Pirates" group's room, someone yelled "SPACE FORCE" during late-night, punch-drunk conversation, and the phrase stuck. It runs on an ESP32 and packs an OLED display, an accelerometer, IR transmit/receive, and LEDs with a strobe mode, powered by a rechargeable battery with its own protection circuitry, plus USB connectivity and EN/IO0 buttons and a power switch for control.

The maker sold the badge directly to DEF CON attendees for around $100 during the con, assembling units by hand at a self-reported rate of about 7-8 per hour during peak production, with roughly 40 units of at least one component hand-soldered. Exact total production numbers were not stated. The maker considered carrying any leftover stock to Supercon later that year. Firmware source and a binary/updater package are available for download from the project page, but no PCB design files or a public repository were found, so it is only partially open source.
