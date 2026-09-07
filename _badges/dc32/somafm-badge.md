---
title: SomaFM Badge
id: dc32-somafm-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: dc32
year: 2024
makers:
- name: Tom Nardi
  url: https://hackaday.io/MS3FGX
summary: A custom electronic badge Tom Nardi built as a gift for SomaFM's DJs, with a backlit fiberglass SomaFM logo and a small display cycling through channel artwork.
functions: Cycles through SomaFM channel artwork on its display via two tactile buttons; backlit logo cutout; two SAO ports for plugging in other add-ons.
look:
  colors:
  - black
  shape: logo
  themes:
  - music
  - radio
  - logo
tech:
  mcu: RP2040
  leds:
    count: 6
    type: reverse-mount
    note: Right-angle SMD LEDs backlighting an exposed-fiberglass SomaFM logo cutout through a clear hot-glue diffuser, covered with black duct tape to cut down reflected light.
  display: 1.3" ST7789 LCD
  connectivity: []
  battery: 2x AA (3V)
  sao_version: v1
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: KiCad
links:
- label: hackaday.io/project/196876-somafm-badge
  url: https://hackaday.io/project/196876-somafm-badge
  kind: hackaday
- label: Tom Nardi's original SAO concept post (Mastodon)
  url: https://hackaday.social/@tomnardi/111707447123330809
  kind: social
- label: SomaFM
  url: https://somafm.com/
  kind: website
images:
- file: assets/images/badges/dc32/somafm-badge/fc7f407a07.jpg
  source: "https://hackaday.io/project/196876-somafm-badge"
  credit: "Tom Nardi"
  caption: "Finished SomaFM Badge with backlit fiberglass logo and display"
- file: assets/images/badges/dc32/somafm-badge/7cbff37103.jpg
  source: "https://hackaday.io/project/196876-somafm-badge"
  credit: "Tom Nardi"
  caption: "SomaFM Badge showing channel artwork on the ST7789 display"
contact: {}
notes:
- Right-angle SMD LEDs backlight exposed fiberglass logo; SAO form factor.
- Not sold; made as a personal gift/tribute, six units built and shipped directly to SomaFM's studio in San Francisco for their DJs to wear at DEF CON 32.
- All SomaFM logos/artwork used with permission from SomaFM.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/196876-somafm-badge
  title: SomaFM Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/196876-somafm-badge
  title: SomaFM Badge (full project log)
  accessed: '2026-09-07'
  note: Primary source for maker (Tom Nardi), event/year (DEF CON 32, 2024), build story, MCU/display/LED/battery details, quantity (six), and photos.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: All core facts confirmed on the maker's own Hackaday.io project page, including full build log. No hardware/firmware repo was found linked from the project (only a display-modification reference and an Adafruit library issue), so make_your_own fields are left null/KiCad-only. This was never a public sale; it was a one-off gift project, so get_one fields are intentionally left empty and price/quantity-for-sale do not apply beyond the six units made.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/somafm-badge/
---

Tom Nardi built the SomaFM Badge as a tribute to the internet radio station SomaFM, whose General Manager Rusty Hodge he connected with after posting an early concept for a backlit-logo SAO on Mastodon in January 2024. The badge went through two PCB revisions: a first version with an inverted MCU footprint and swapped display pins that nonetheless proved the lighting concept, and a final version with six right-angle SMD LEDs shining through a clear hot-glue diffuser behind an exposed-fiberglass SomaFM logo cutout, finished with black duct tape to tame reflected light. A 1.3" ST7789 LCD cycles through SomaFM's channel artwork, driven by a Waveshare RP2040 Zero running CircuitPython; two SAO ports let the badge host other add-ons, and it runs off a pair of AA batteries.

Six completed badges shipped to SomaFM's San Francisco studio on August 1, 2024, in time for DEF CON 32, where they were worn by SomaFM's DJs. It was never sold or distributed beyond that gift, and all SomaFM branding was used with the station's permission.
