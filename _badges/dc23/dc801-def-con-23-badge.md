---
title: DC801 2015 DEF CON VIP Party Badge
id: dc23-dc801-def-con-23-badge
layout: badge
parent: DC23
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc23
year: 2015
makers:
- name: DC801
  url: https://dc801.org/
- name: theTransistor
  url: http://thetransistor.com/
summary: A handheld game-console-style party badge built by DC801 and theTransistor for their DEF CON 23 (2015) VIP party, with a color touchscreen, dual joysticks, and RGB LED lighting in a laser-cut acrylic case.
functions: Runs custom software demoed on its LCD (a "801 LABS" splash/boot screen is shown in one photo); the repo includes a Software directory of example code for the platform. Has a charge/voltage readout capability and microSD storage.
look:
  colors:
  - black
  - white
  - red
  - green
  shape: rectangle
  themes:
  - retro computer
  - console
  - hardware tool
tech:
  mcu: Parallax P8X32A Propeller + ATmega328P
  leds:
    count: 10
    type: WS2812B
    note: RGB pixel LEDs around the case edges
  display: 3.6" LCD, 400x240, 18-bit color (R61509V driver, originally speced as ILI9327)
  connectivity:
  - wifi
  - uart
  battery: 2000 mAh LiPo with charging circuit
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Given to VIPs/attendees at the DC801 DEF CON 23 party in 2015; not sold.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/hamster/DefCon23
  firmware_url: https://github.com/hamster/DefCon23
  bom_url: https://github.com/hamster/DefCon23/tree/master/Hardware
  eda_tool: EAGLE
links:
- label: github.com/hamster/DefCon23
  url: https://github.com/hamster/DefCon23
  kind: repo
- label: github.com/thetransistor/DefCon23 (upstream)
  url: https://github.com/thetransistor/DefCon23
  kind: repo
- label: dc801.org
  url: https://dc801.org/
  kind: website
images:
- file: assets/images/badges/dc23/dc801-def-con-23-badge/31b1fefd17.jpg
  source: https://github.com/hamster/DefCon23
  credit: DC801 / theTransistor
  caption: The 2015 DC801 DEF CON VIP party badge
- file: assets/images/badges/dc23/dc801-def-con-23-badge/3f72fd0c60.jpg
  source: https://github.com/hamster/DefCon23
  credit: DC801 / theTransistor
  caption: The assembled badge in its acrylic case with dual joysticks
contact:
  irc: '#thetransistor on freenode'
  email: d3c4f [at] thetransistor [dot] com
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/hamster/DefCon23
  title: DC801 DEF CON 23 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc23''.'
- kind: url
  url: https://github.com/hamster/DefCon23#readme
  title: 'hamster/DefCon23 README: DC801 2015 Defcon VIP Party Badge'
  accessed: '2026-09-07'
  note: Primary source for makers, full hardware feature list (MCUs, display, LEDs, battery, joysticks/encoder/buttons, microSD, case), credits, and contact info. This is a fork of thetransistor/DefCon23; the README also notes @hamster added a Software directory of demo code.
- kind: url
  url: https://github.com/thetransistor/DefCon23
  title: thetransistor/DefCon23 (upstream repo)
  accessed: '2026-09-07'
  note: Confirmed this is the original (upstream) project repo that the linked entry forks from; same README content.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Event corrected from "other" to dc23 (DEF CON 23, 2015) based on the repo README title and year. Price/quantity not stated anywhere; it was a party giveaway, not sold, so get_one.price is left empty. No SAO header mentioned in the source; sao_version left null rather than guessing "none" since the badge predates common SAO convention and the README does not address it explicitly. Fact-check pass (2026-09-07): re-fetched both repo READMEs and the Hardware directory listing. All front-matter fields and body sentences confirmed against the cited sources, with two corrections: the "Make your own" section had wrongly stated no BOM was found — the repo Hardware directory actually contains "BOM - LED Board.xlsx" and "BOM - Mainboard.xlsx", so a make_your_own.bom_url was added and the sentence fixed; and the caption on the second image ("Badge PCB/enclosure design render") was wrong — the photo is an actual assembled unit with green joysticks, not a render, so the caption was corrected.
    No Gerbers or fab-house link found, confirmed. dc801.org currently shows an "under construction" placeholder page (checked 2026-09-07); it is kept only as a website link, not cited as a factual source, so this does not affect confidence.'
last_modified_date: '2026-09-11'
redirect_from:
- /badges/other/dc801-def-con-23-badge/
model:
  file: assets/models/dc23/dc801-def-con-23-badge.glb
  method: kicad
  source_file: Mainboard v4.brd
  generated: '2026-09-11'
  bytes: 370524
---

The DC801 2015 DEF CON VIP Party Badge is a handheld, game-console-shaped party badge built by the Salt Lake City hacker groups DC801 and theTransistor for their annual DEF CON party, held during DEF CON 23 in 2015. It packs a Parallax P8X32A Propeller microcontroller alongside an ATmega328P for analog/extra I/O, an ESP8266 (ESP-12E) Wi-Fi module, a socket for an XBee serial radio, and FTDI with switchable output. The centerpiece is a 3.6" 400x240 18-bit color LCD, flanked by two analog joysticks, a rotary encoder, and two pushbuttons, with 10 WS2812B RGB LEDs lighting the edges of a laser-cut HDPE/acrylic case. It runs on a 2000 mAh LiPo battery with onboard charging and voltage/charge readout, and includes a microSD slot for storage.

The badge was designed by D3c4f with electronics engineering by Compukidmike, case manufacturing by Isaac at Rusted Friend, and assembly/QA/software work from a larger DC801/theTransistor crew. It was handed out to VIPs and attendees at the group's DEF CON party rather than sold. The linked GitHub repository (a fork by user "hamster" of the original thetransistor/DefCon23 project) publishes the Eagle hardware design files and adds a Software directory demonstrating example firmware for the platform; the license is MIT.

## Make your own

Hardware design files (Eagle format), bills of materials for both the mainboard and LED board, and starter firmware/example software are published at both github.com/hamster/DefCon23 and the upstream github.com/thetransistor/DefCon23, under the MIT license. No Gerbers or fab-house share link were found in the repo.
