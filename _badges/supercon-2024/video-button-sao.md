---
title: Video Button SAO
id: supercon-2024-video-button-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Ben Combee (unwiredben)
  url: https://hackaday.io/unwiredben
summary: A Simple Add-On built from an off-the-shelf WaveShare RP2040-LCD-0.99-B round display module and an Adafruit 6-pin ISP breadboard adapter, held together with hot glue, that plays 24fps MPEG-1 video on its tiny screen and exposes its accelerometer/gyro over the SAO I2C pins; submitted to the Supercon 8 (2024) SAO Contest.
functions: Plays back MPEG-1 encoded video clips (converted from source video with ffmpeg) at 128x128 resolution on the round LCD; exposes the display module's onboard IMU (accelerometer/gyroscope) to the host badge over the SAO I2C connection.
look:
  colors: []
  shape: circle
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: RP2040
  leds: null
  display: 0.99" round LCD (WaveShare RP2040-LCD-0.99-B, 128x128, driven at 128x115 with 180-degree rotation)
  connectivity:
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/unwiredben/button-video
  firmware_url: https://github.com/unwiredben/button-video
  eda_tool: null
links:
- label: hackaday.io/project/197669-video-button-sao
  url: https://hackaday.io/project/197669-video-button-sao
  kind: hackaday
- label: github.com/unwiredben/button-video
  url: https://github.com/unwiredben/button-video
  kind: repo
- label: slides.com/unwiredben/tinyplayer
  url: https://slides.com/unwiredben/tinyplayer
  kind: website
images:
- file: assets/images/badges/supercon-2024/video-button-sao/1c61defa01.jpg
  source: "https://hackaday.io/project/197669-video-button-sao"
  credit: "Ben Combee"
  caption: "Video Button SAO assembled from a WaveShare RP2040-LCD-0.99-B module and Adafruit ISP adapter"
- file: assets/images/badges/supercon-2024/video-button-sao/688ecdc3fe.jpg
  source: "https://hackaday.io/project/197669-video-button-sao"
  credit: "Ben Combee"
  caption: "Video Button SAO playing video on its round display"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/197669-video-button-sao
  title: Video Button SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/197669-video-button-sao
  title: Video Button SAO
  accessed: '2026-09-07'
  note: Confirmed maker, event (Supercon 8 / 2024 SAO Contest), display module, MPEG-1 playback, IMU over I2C, and open-source firmware link.
- kind: url
  url: https://github.com/unwiredben/button-video
  title: unwiredben/button-video
  accessed: '2026-09-07'
  note: Confirmed hardware (RP2040, WaveShare 0.99" round display, 128x115 effective resolution with rotation), MIT license, build process (ffmpeg to MPEG-1, pl_mpeg decoder, TFT_eSPI, arduino-pico/PlatformIO).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Slides.com deck (slides.com/unwiredben/tinyplayer) returned a 404 and could not be checked. Price, quantity made, and availability are not stated anywhere found; this appears to have been a one-off contest entry rather than a distributed item, so those fields are left empty rather than guessed. LED info left null since the display module itself has no separate addressable LEDs mentioned.
last_modified_date: '2026-09-07'
---

Ben Combee (unwiredben) built the Video Button SAO for the Supercon 8 (2024) SAO Contest by repurposing an off-the-shelf WaveShare RP2040-LCD-0.99-B round display module — a small board with its own onboard RP2040 and a 0.99" LCD — as a Simple Add-On. He wired it to an Adafruit 6-pin AVR ISP breadboard adapter to get SAO-header pinout and held the assembly together with hot glue rather than designing a custom PCB.

The firmware decodes MPEG-1 video files (produced from source clips with ffmpeg, embedded into the build as C headers) using the single-file `pl_mpeg` decoder and drives the display through a customized TFT_eSPI board definition, running on the arduino-pico core via PlatformIO. The RP2040 is overclocked to 275MHz to keep video playback smooth. Because the WaveShare module also carries an accelerometer/gyroscope, the project exposes that sensor to the host badge over the SAO's I2C pins in addition to playing video.

The hardware and firmware are published under the MIT license at github.com/unwiredben/button-video. No information was found on how many were made or whether it was distributed beyond the contest; it reads as a one-off entry rather than a badge sold or given away in quantity.
