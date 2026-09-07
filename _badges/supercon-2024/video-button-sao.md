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
summary: A Simple Add-On built from an off-the-shelf WaveShare RP2040-LCD-0.99-B round display module and an Adafruit 6-pin ISP breadboard adapter, held together with hot glue, that plays back MPEG-1 video at about 24fps on its tiny round screen; submitted to the Supercon 8 (2024) SAO Contest.
functions: Plays back MPEG-1 encoded video clips (converted from source video with ffmpeg) at 128x128 resolution on the round LCD. The display module also has an onboard accelerometer/gyroscope IMU that the maker intended to expose to the host badge over the SAO's I2C pins, but found could not actually be read that way (see notes).
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
  caption: "Video Button SAO assembled from a WaveShare RP2040-LCD-0.99-B module and Adafruit ISP adapter, playing video on its round display"
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
  note: Confirmed hardware (RP2040, WaveShare 0.99" round display, 128x115 effective resolution with rotation), MIT license, build process (ffmpeg to MPEG-1, pl_mpeg decoder, TFT_eSPI, arduino-pico/PlatformIO). README does not mention the IMU/accelerometer being read or exposed anywhere in the firmware.
- kind: url
  url: https://hackaday.io/project/197669-video-button-sao/details
  title: Video Button SAO (project details / log)
  accessed: '2026-09-07'
  note: "Fact-check pass. Confirms Supercon 8 SAO Contest context. Its \"Connectivity Problems\" section states the IMU and SAO I2C connector share the RP2040's I2C1 peripheral and can't be used simultaneously, so IMU-over-SAO was attempted but not functional. Confirms the final build ran at 125MHz/~24fps/2.95V/40mA after an earlier 270-275MHz overclock proved too power-hungry for the badge."
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: Fact-check pass corrected two overstated claims from the prior research pass. (1) The entry had stated the SAO "exposes" the WaveShare module's accelerometer/gyroscope IMU to the host badge over I2C as a working feature; the hackaday.io project log's "Connectivity Problems" section (details subpage) says the maker found the IMU and the SAO connector share the RP2040's I2C1 peripheral and "can't really use the IMU while processing requests from the badge" — so this was an attempted, non-functional feature, not a delivered one. Corrected summary, functions, and body accordingly. (2) The body had stated flatly that the RP2040 "is overclocked to 275MHz to keep video playback smooth"; the hackaday.io log and GitHub README together show the final SAO build actually ran at the standard 125MHz (~24fps, 2.95V/40mA) because the 270-275MHz overclock drew too much current for the badge's power pins — corrected to describe both stages. (3) The second saved image (688ecdc3fe.jpg) was a hand-drawn I2C pinout sketch mislabeled as "playing video on its round display"; it did not show the item and was removed, and the caption on the remaining photo was corrected to describe what it actually shows. All other non-empty fields (maker, event, MCU, display module/resolution, connectivity, MIT license and repo links, shape, status) were confirmed directly against the hackaday.io project page and the unwiredben/button-video GitHub repo/README. Slides.com deck (slides.com/unwiredben/tinyplayer) still returns a 404 and could not be checked. Price, quantity made, and availability remain unstated anywhere found; left empty rather than guessed.
last_modified_date: '2026-09-07'
---

Ben Combee (unwiredben) built the Video Button SAO for the Supercon 8 (2024) SAO Contest by repurposing an off-the-shelf WaveShare RP2040-LCD-0.99-B round display module — a small board with its own onboard RP2040 and a 0.99" LCD — as a Simple Add-On. He wired it to an Adafruit 6-pin AVR ISP breadboard adapter to get SAO-header pinout and held the assembly together with hot glue rather than designing a custom PCB.

The firmware decodes MPEG-1 video files (produced from source clips with ffmpeg, embedded into the build as C headers) using the single-file `pl_mpeg` decoder and drives the display through a customized TFT_eSPI board definition, running on the arduino-pico core via PlatformIO. Combee first got smooth playback by overclocking the RP2040 to around 270-275MHz, but that drew too much current to run safely off a badge's SAO power pins; switching to the smaller 128x128 frame size let him drop back to the RP2040's standard 125MHz clock, which still played video at an acceptable ~24fps within the badge's power budget. He also looked into exposing the WaveShare module's onboard accelerometer/gyroscope IMU to the host badge over the SAO's I2C pins, but found the IMU and the SAO connector shared the same RP2040 I2C peripheral and couldn't be used at the same time, so that feature was never made to work.

The hardware and firmware are published under the MIT license at github.com/unwiredben/button-video. No information was found on how many were made or whether it was distributed beyond the contest; it reads as a one-off entry rather than a badge sold or given away in quantity.
