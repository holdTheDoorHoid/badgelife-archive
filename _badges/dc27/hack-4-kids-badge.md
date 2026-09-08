---
title: Hak4Kidz DEF CON 27 Badge
id: dc27-hack-4-kids-badge
layout: badge
parent: DC27
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc27
year: 2019
makers:
- name: Hak4Kidz
  url: https://www.hak4kidz.com/
summary: A puzzle badge from the youth ethical-hacking nonprofit Hak4Kidz, built around a color TFT screen styled as a cryptex that hides a challenge behind capacitive touch pads.
functions: A cryptex-unlocking puzzle challenge navigated with 6 capacitive touch pads around the screen; programmable over USB via a micro SD card slot for flashing the ESP32.
look:
  colors: []
  shape: null
  themes:
  - puzzle
  - learn to solder
  - security
  - mascot
tech:
  mcu: ESP32
  leds: null
  display: 2.4" 240x320 color TFT LCD
  connectivity:
  - wifi
  - bluetooth
  - usb
  battery: USB or 3x AA (included)
  sao_version: null
get_one:
  price: $100
  price_usd: 100
  quantity: '200'
  availability: sold_out
  distribution:
  - crowdfunding
  - purchase
  where: Kickstarter campaign (ended July 1, 2019); pickup at DEF CON 27 in Las Vegas or shipped
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  kind: article
- label: hackster.io - Hak4Kidz Is Making a DEF CON 27 Indie Badge Just for Kids
  url: https://www.hackster.io/news/hak4kidz-is-making-a-def-con-27-indie-badge-just-for-kids-a2a0b7a3dd19
  kind: article
- label: Kickstarter - Hak4Kidz DEF CON 27 Indie Badge
  url: https://www.kickstarter.com/projects/h4k/hak4kidz-def-con-27-indie-badge
  kind: store
- label: Hak4Kidz
  url: https://www.hak4kidz.com/
  kind: website
images:
- file: assets/images/badges/dc27/hack-4-kids-badge/e0cacaf1c4.jpg
  source: "https://www.hackster.io/news/hak4kidz-is-making-a-def-con-27-indie-badge-just-for-kids-a2a0b7a3dd19"
  credit: "Hak4Kidz / Hackster.io (Cameron Coward)"
  caption: "Hak4Kidz DEF CON 27 badge, featuring the Tinker mascot and cryptex design around the color TFT screen"
contact: {}
notes:
- Charity-themed badge from the GrrCON organizers shown at DEF CON 27. Found by the event-year sweep, task dc27-badges.
- The sweep's sheet attributed this to "GrrCON organizers" and titled it "Hack 4 Kids Badge." Sources instead identify the maker as Hak4Kidz (a youth ethical-hacking nonprofit); Hackaday notes the design was "originally designed for GrrCON" before being sold as a DEF CON 27 indie badge via Kickstarter, so the GrrCON connection has some basis but the maker of record for this specific DC27 release is Hak4Kidz. Title corrected to match how the maker and press refer to it.
status: released
sources:
- kind: url
  url: https://hackaday.com/2019/09/19/pictorial-guide-to-the-unofficial-electronic-badges-of-def-con-27/
  title: Hack 4 Kids Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:dc27-badges); event read as ''dc27''.'
- kind: url
  url: https://www.hackster.io/news/hak4kidz-is-making-a-def-con-27-indie-badge-just-for-kids-a2a0b7a3dd19
  title: Hak4Kidz Is Making a DEF CON 27 Indie Badge Just for Kids
  accessed: '2026-09-08'
  note: Full spec details (ESP32, 2.4" TFT, capacitive touch, SAO ports, battery, price, distribution) and story of the badge; fetched via Wayback Machine snapshot since the live page returns 403 to automated fetches.
- kind: url
  url: https://www.kickstarter.com/projects/h4k/hak4kidz-def-con-27-indie-badge
  title: Hak4Kidz DEF CON 27 Indie Badge
  accessed: '2026-09-08'
  note: Confirms maker (Hak4Kidz) and campaign existence; page itself was behind a Cloudflare challenge so could not be read directly.
- kind: url
  url: https://www.hak4kidz.com/
  title: Hak4Kidz | Home
  accessed: '2026-09-08'
  note: Confirms Hak4Kidz as an active youth ethical-hacking conference/nonprofit.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: Core specs and story come from a Hackster.io article (maker-adjacent press, read via a Wayback Machine snapshot since the live page 403s automated fetches) corroborated by the Hackaday DC27 badge roundup; the maker's own Kickstarter and site pages were reachable only enough to confirm identity, not to pull additional detail, since Kickstarter serves a Cloudflare challenge to automated fetches. LED count/type not stated in any source found. sao_version and sao_ports not stated (source says "two SAO locations" but not which pinout). hardware/firmware open-source status not found.
last_modified_date: '2026-09-08'
---

The Hak4Kidz DEF CON 27 badge is a puzzle badge from Hak4Kidz, a nonprofit that runs youth-focused ethical-hacking events, built around the group's mascot Tinker standing behind a cryptex-styled centerpiece. A 2.4" 240x320 color TFT LCD sits in the middle of the cryptex, surrounded by 6 capacitive touch pads that players use to work through an unlock puzzle hidden in the badge's firmware. Hackaday's contemporaneous roundup notes the design was originally created for GrrCON before this DEF CON 27 run.

Under the hood it runs an ESP32, giving it Wi-Fi and Bluetooth, with a micro SD card slot for flashing code and two SAO add-on locations for expansion. It can run on USB power or three included AA batteries. About 200 were produced; roughly half were sold through a Kickstarter campaign that ran through July 1, 2019, at $100 each, with backers able to pick the badge up in person at DEF CON 27 in Las Vegas or have it shipped.
