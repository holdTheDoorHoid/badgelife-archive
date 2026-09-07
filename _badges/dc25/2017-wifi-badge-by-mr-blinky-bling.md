---
title: 2017 WiFi Badge by Mr. Blinky Bling
id: dc25-2017-wifi-badge-by-mr-blinky-bling
layout: badge
parent: DC25
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc25
year: 2017
makers:
- name: Ben Hibben (Blenster)
  url: https://hackaday.io/blenster
- name: The Hat
summary: An unofficial DEF CON 25 badge that scans nearby WiFi and lights up LEDs by channel, built around an ESP8266 WiFi module and an ATtiny88 for LED/touch control.
functions: Scans for WiFi access points and displays SSID/channel data on a small OLED screen; channel-specific LED indicators light up as networks are found; supports programmable LED animations and capacitive touch buttons; Arduino-compatible for hacking on.
look:
  colors:
  - red
  shape: null
  themes:
  - wifi
  - radio
  - hardware tool
tech:
  mcu: ATtiny88
  leds: null
  display: 128x32 OLED
  connectivity:
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - crowdfunding
  where: 'Hand-assembled "Founder''s Edition" batch (red PCB, brighter white LEDs) sold/distributed around DEF CON 25; broader distribution was to follow via a Kickstarter campaign and later Tindie listings for add-on boards.'
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.io/project/25722-2017-wifi-badge-by-mr-blinky-bling
  url: https://hackaday.io/project/25722-2017-wifi-badge-by-mr-blinky-bling
  kind: hackaday
images:
- file: assets/images/badges/dc25/2017-wifi-badge-by-mr-blinky-bling/9fefb5f21d.png
  source: "https://hackaday.io/project/25722-2017-wifi-badge-by-mr-blinky-bling"
  credit: "Ben Hibben (Blenster)"
  caption: "The 2017 WiFi Badge, main project photo"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/25722-2017-wifi-badge-by-mr-blinky-bling
  title: 2017 WiFi Badge by Mr. Blinky Bling
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/25722-2017-wifi-badge-by-mr-blinky-bling
  title: 2017 WiFi Badge by Mr Blinky Bling (Hackaday.io project page)
  accessed: '2026-09-07'
  note: 'Primary source for maker names, chips, display, and Founder''s Edition/Kickstarter details.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core facts (maker, MCU/WiFi chip, display, DEF CON 25 / 2017 context) confirmed on the Hackaday.io project page itself. Could not confirm price, quantity made, LED count/type, battery, SAO header, or whether hardware/firmware files were ever published — the project page references design files and photos but no direct GitHub/gerber link was visible in the fetched content, and the Kickstarter/Tindie listings mentioned on the page could not be located or verified in this pass. A second image (cdn.hackaday.io/files/257221100490048/1.jpg) timed out on download and was not saved.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/2017-wifi-badge-by-mr-blinky-bling/
---

The 2017 WiFi Badge is an unofficial DEF CON 25 badge built by Ben Hibben (aka Blenster) and a collaborator known as The Hat. It pairs an ESP8266 WiFi module, used to scan for nearby access points, with an ATtiny88 microcontroller that drives the badge's LEDs and capacitive touch buttons, plus a 128x32 OLED display for showing scan results by channel. The project page describes it as Arduino-compatible, with a library meant to make it easy for other hackers to build on.

A hand-assembled "Founder's Edition" run used a red PCB with brighter white LEDs. The makers planned wider distribution through a Kickstarter campaign, with add-on boards and an ESP8266 programmer to follow on Tindie after the con, though this research pass could not confirm whether those follow-on listings ever went live or how many units were ultimately made.
