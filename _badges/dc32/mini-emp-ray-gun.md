---
title: Mini EMP Ray-gun!!!
id: dc32-mini-emp-ray-gun
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: Embedded Systems Village
summary: A hand-held "ray gun" badge from Embedded Systems Village that pairs a high-voltage discharge tip with RGB LED animations and sound effects, built on a Raspberry Pi Pico (RP2040) running MicroPython.
functions: Two buttons trigger different modes; one cycles through LED animations (chase, rainbow, twinkle, wave) at low power, the other fires the high-voltage tip while playing WAV sound effects (arm, disarm, blaster, tesla, boom, pew) through an I2S audio path. Holding both buttons together toggles sound on/off.
look:
  colors: []
  shape: null
  themes:
  - sci-fi
  - hardware tool
tech:
  mcu: RP2040
  leds:
    count: null
    type: WS2812B
    note: Driven via MicroPython's neopixel module; animation modes include chase, rainbow, twinkle, and wave.
  display: none
  connectivity:
  - i2s
  battery: null
  sao_version: none
get_one:
  price: $150.00
  price_usd: 150.0
  quantity: ''
  availability: unknown
  distribution:
  - purchase
  where: Purchase at the Embedded Systems Village (ESV) at DEFCON
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: https://github.com/Embedded-Systems-Village/DEFCON32-Raygun
  eda_tool: null
links:
- label: github.com/Embedded-Systems-Village/DEFCON32-Raygun
  url: https://github.com/Embedded-Systems-Village/DEFCON32-Raygun
  kind: repo
- label: raw.githubusercontent.com/Embedded-Systems-Village/DEFCON32-Raygun/main/README.md
  url: https://raw.githubusercontent.com/Embedded-Systems-Village/DEFCON32-Raygun/main/README.md
  kind: website
- label: x.com/EmbeddedVillage/status/1819106299206160657
  url: https://x.com/EmbeddedVillage/status/1819106299206160657
  kind: social
- label: x.com/EmbeddedVillage/status/1819394650488119764
  url: https://x.com/EmbeddedVillage/status/1819394650488119764
  kind: social
images:
- file: assets/images/badges/dc32/mini-emp-ray-gun/a5e597454d.jpg
  source: "https://x.com/EmbeddedVillage/status/1819106299206160657"
  credit: "Embedded Systems Village"
  caption: "The ESV Mini EMP Ray-gun badge unveiled on X"
- file: assets/images/badges/dc32/mini-emp-ray-gun/68c04adfac.jpg
  source: "https://x.com/EmbeddedVillage/status/1819394650488119764"
  credit: "Embedded Systems Village"
  caption: "The Raygun badge being tested at the DEF CON 32 Olympics"
contact: {}
notes:
- There may be a way to purchase in advance... stay tuned!!
status: released
sources:
- kind: sheet
  event: dc32
  row: 56
  updated: '2024-08-01'
- kind: url
  url: https://raw.githubusercontent.com/Embedded-Systems-Village/DEFCON32-Raygun/main/README.md
  title: "DEFCON32-Raygun README"
  accessed: '2026-09-06'
  note: "Safety-warning README describing the badge as an experimental high-voltage device sold as-is, no warranty."
- kind: url
  url: https://github.com/Embedded-Systems-Village/DEFCON32-Raygun
  title: "Embedded-Systems-Village/DEFCON32-Raygun on GitHub"
  accessed: '2026-09-06'
  note: "Source repo: main.py firmware, micropython/ (RPI_PICO v1.23.0 uf2), sounds/ (wav files), utilities/."
- kind: url
  url: https://raw.githubusercontent.com/Embedded-Systems-Village/DEFCON32-Raygun/main/main.py
  title: "main.py"
  accessed: '2026-09-06'
  note: "Firmware confirms RP2040 (CSPico/Raspberry Pi Pico MicroPython driver base by Colin O'Flynn), neopixel LEDs, I2S WAV playback via wavplayer.py, two-button input on GPIO9/GPIO15, animation and sound-effect state machine."
- kind: url
  url: https://x.com/EmbeddedVillage/status/1819106299206160657
  title: "Embedded Systems Village unveiling post"
  accessed: '2026-09-06'
  note: "Announcement post; og:image gave a product photo, caption \"Unveiling the ESV #badgelife Ray Gun!\""
- kind: url
  url: https://x.com/EmbeddedVillage/status/1819394650488119764
  title: "Embedded Systems Village follow-up post"
  accessed: '2026-09-06'
  note: "Follow-up post; og:image gave a second photo, caption \"Our ESV Raygun Badge is already being tested out at the Olympics!\""
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: "Maker's GitHub firmware and README confirm the device and its RP2040/MicroPython base, LED animations, buttons, and WAV sound effects, but no maker page gives an LED count, battery spec, quantity made, or confirms whether it sold out. price_usd of $150 comes from the original sheet import only, not independently re-confirmed by a maker source. type set to badge (worn, self-powered device sold at a village) rather than sao/accessory since no SAO header is mentioned. X/Twitter posts could only be read via og:image/description meta tags (page itself returned HTTP 402 to automated fetch), so full post text is not available."
last_modified_date: '2026-09-06'
---

The Mini EMP Ray-gun is a badge-shaped ray gun made by Embedded Systems Village (ESV) for DEF CON 32, built around a Raspberry Pi Pico (RP2040) running MicroPython. Two buttons drive it: one cycles a set of NeoPixel LED animations (chase, rainbow, twinkle, wave) at a dimmed "low power" brightness, and the other fires a high-voltage discharge at the tip of the gun while playing sound effects — arming, blaster, tesla-coil, and boom sounds among them — over I2S audio. Holding both buttons together mutes or unmutes the sound.

ESV's own README frames it as a genuinely experimental, higher-voltage device: it warns against use near medical equipment, radios, and other electronics, cautions that touching the tip or the gap between the two PCBs can and will shock you, and says the badge is sold "as-is," with no warranty. It was sold at the Embedded Systems Village at DEF CON 32 for $150, per the original community badge-sheet listing. ESV posted photos of the badge on X around the con, including one showing it "tested out at the Olympics," but did not publish pricing, LED count, or sales-quantity details on their own channels that could be independently confirmed here.

The firmware and design are open on GitHub (Embedded-Systems-Village/DEFCON32-Raygun), including the MicroPython driver code, a bank of WAV sound files, and the Raspberry Pi Pico MicroPython build used to run it — enough for someone to reproduce the electronics side of the project, though no separate hardware (PCB/schematic) files were found in the repo.
