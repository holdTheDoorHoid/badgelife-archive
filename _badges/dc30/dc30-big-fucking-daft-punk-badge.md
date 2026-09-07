---
title: DC30 Big Fucking Daft Punk Badge
id: dc30-dc30-big-fucking-daft-punk-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc30
year: 2022
makers:
- name: hexum064 and Erin
  url: https://hackaday.io/hacker/172907-hexum064
summary: A large ESP32-based DEF CON 30 badge styled after Daft Punk's Random Access Memories helmet artwork that plays MP3s from an SD card to headphones, speakers or Bluetooth while over 500 WS2812B-2020 RGB LEDs in the mask show VU meters and equalizer bars.
functions: 'MP3 playback from SD card, Bluetooth or speaker audio output via two 3W MAX98357A amplifiers, LED VU meter and equalizer visualizations across the mask, song/volume selection buttons, output-mode and display-mode switching, a status screen, and a "Nyan Cat mode."'
look:
  colors: []
  shape: null
  themes:
  - music
  - sci-fi
  - pop culture
tech:
  mcu: ESP32
  leds:
    count: 500
    type: WS2812B-2020
    note: More than 500 5mA WS2812B-2020 RGB LEDs arranged across the mask/helmet panel.
  display: null
  connectivity:
  - bluetooth
  - audio
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Worn by the makers at DEF CON 30 (2022); described as a limited run, not sold through a storefront.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Hexum064/mp3-bt-sc-i2s-oled
  eda_tool: null
links:
- label: hackaday.io/project/184321-dc30-big-fucking-daft-punk-badge
  url: https://hackaday.io/project/184321-dc30-big-fucking-daft-punk-badge
  kind: hackaday
- label: github.com/Hexum064/mp3-bt-sc-i2s-oled
  url: https://github.com/Hexum064/mp3-bt-sc-i2s-oled
  kind: repo
- label: 'Tindie Blog: Badge Me if You Can – DEF CON 30'
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  kind: article
images:
- file: assets/images/badges/dc30/dc30-big-fucking-daft-punk-badge/ffc2b5bd72.jpg
  source: "https://hackaday.io/project/184321-dc30-big-fucking-daft-punk-badge"
  credit: "hexum064 and Erin"
  caption: "The finished Daft Punk-styled badge worn at DEF CON 30"
- file: assets/images/badges/dc30/dc30-big-fucking-daft-punk-badge/be9eb3b90d.jpg
  source: "https://hackaday.io/project/184321-dc30-big-fucking-daft-punk-badge"
  credit: "hexum064 and Erin"
  caption: "PCB and LED panel during assembly"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/184321-dc30-big-fucking-daft-punk-badge
  title: DC30 Big Fucking Daft Punk Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/Hexum064/mp3-bt-sc-i2s-oled
  title: Hexum064/mp3-bt-sc-i2s-oled
  accessed: '2026-09-07'
  note: Firmware repo linked from the Hackaday project; ESP-IDF based, confirms ESP32 platform, no license file found.
- kind: url
  url: https://blog.tindie.com/2022/08/badge-me-if-you-can-def-con-30/
  title: 'Tindie Blog: Badge Me if You Can – DEF CON 30'
  accessed: '2026-09-07'
  note: Press coverage confirming maker, three-PCB-stack build, two 3W speakers, 500+ LEDs, and that it was a limited run worn at the con.
- kind: url
  url: https://hackaday.io/project/184321/gallery
  title: 'Gallery | DC30 Big Fucking Daft Punk Badge | Hackaday.io'
  accessed: '2026-09-07'
  note: Used to locate photo URLs of the finished badge and assembly.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday project page and GitHub repo confirm the ESP32 platform, LED count/type, and audio path; the GitHub repo has no README content describing the badge itself (looks like a generic ESP-IDF template repo) so hardware_url, gerbers_url, bom_url and license could not be confirmed and are left empty. Price, quantity made, and exact availability (sold vs. given away vs. team-only) were not stated by any source found; Tindie's press coverage calls it a "limited run" worn by the makers, consistent with a self-made/team badge rather than a general sale, but this is not explicit. Display hardware (if any beyond the LED panel/status screen) was not specified.
last_modified_date: '2026-09-07'
---

Hexum064 and Erin built this DEF CON 30 badge as a wearable homage to Daft Punk's *Random Access Memories* album art, assembling it from three stacked PCBs into a helmet-like mask panel. An ESP32 drives the show: more than 500 WS2812B-2020 RGB LEDs cover the mask and animate as VU meters and equalizer bars in time with music, while a pair of 3W MAX98357A amplifiers push audio out through built-in speakers, a headphone jack, or Bluetooth. Songs are pulled from an SD card as MP3 files, with buttons for track and volume selection, switchable display and output modes, a status screen, and a bonus "Nyan Cat mode."

Coverage from Tindie's DEF CON 30 badge roundup describes it as a limited-run piece that "went fast" and was "a head-turner all weekend long," suggesting the makers wore and shared it among a small group rather than selling it broadly. The firmware lives in a public GitHub repository, though the repo's own documentation reads as a generic ESP-IDF starter template rather than badge-specific build notes, so it is only a partial look at how the project was put together.

## Make your own

Firmware source is public at github.com/Hexum064/mp3-bt-sc-i2s-oled (ESP-IDF project for ESP32 with MP3, Bluetooth, SD-card, and I2S audio support), but no hardware files, BOM, or license were found, so a full build is not currently reproducible from published materials alone.
