---
title: DEFCON-Badge-2024 (patridge)
id: dc32-defcon-badge-2024-patridge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
makers:
- name: patridge
  url: https://www.patridgedev.com/about-me/
summary: A personal, unofficial DEF CON 32 (2024) badge project written in C# for the Wilderness Labs Meadow "Project Lab" development board, cycling between DEF CON splash art and a few info pages on its color display.
functions: 'Cycles automatically between DEF CON 32 splash-screen artwork and app "pages" on the display: an EnvironmentPage showing live temperature, barometric pressure, humidity and ambient light readings, a GraphPage, and a stubbed-out WiFiTrackerPage (not implemented). Four buttons (up/down/left/right) page through content and adjust display brightness; the RGB LED lights green on startup; display brightness also auto-adjusts to ambient light via the onboard light sensor.'
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: Meadow F7v2 (STM32F7 core compute module)
  leds: null
  display: 3.2" 320x240 IPS TFT (ILI9341)
  connectivity:
  - wifi
  - ble
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Not distributed as hardware: it is firmware the maker wrote for their own Wilderness Labs Meadow Project Lab board (a commercial ~$250 .NET IoT dev board), not a custom PCB made for or given out at the con.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/patridge/DEFCON-Badge-2024
  eda_tool: null
links:
- label: github.com/patridge/DEFCON-Badge-2024
  url: https://github.com/patridge/DEFCON-Badge-2024
  kind: repo
- label: Wilderness Labs Project Lab board (product page)
  url: https://store.wildernesslabs.co/products/project-lab-board
  kind: doc
images: []
contact: {}
notes:
- 'Sheet listed this under a generic "Other" event; sources confirm it is a DEF CON 32 (2024) project, corrected to dc32.'
status: released
sources:
- kind: url
  url: https://github.com/patridge/DEFCON-Badge-2024
  title: DEFCON-Badge-2024 (patridge)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 2024''.'
- kind: url
  url: https://github.com/patridge/DEFCON-Badge-2024/blob/main/README.md
  title: 'README.md: "Proj Lab badge project for DEF CON 32 (2024)"'
  accessed: '2026-09-07'
  note: Confirms the event/year (DEF CON 32, 2024) and that it targets Wilderness Labs' Project Lab board.
- kind: url
  url: https://github.com/patridge/DEFCON-Badge-2024/blob/main/DefConBadge2024/MeadowApp.cs
  title: MeadowApp.cs (main app source)
  accessed: '2026-09-07'
  note: Source of functions (page cycling, buttons, RGB LED, brightness auto-adjust, splash images), MCU/hardware target (ProjectLab.Create(), F7CoreComputeV2), and license is C# / Meadow.
- kind: url
  url: https://github.com/patridge/DEFCON-Badge-2024/blob/main/DefConBadge2024/Pages/EnvironmentPage.cs
  title: EnvironmentPage.cs
  accessed: '2026-09-07'
  note: Confirms temperature/pressure/humidity/light sensor readout page.
- kind: url
  url: https://github.com/patridge/DEFCON-Badge-2024/blob/main/DefConBadge2024/Pages/WiFiTrackerPage.cs
  title: WiFiTrackerPage.cs
  accessed: '2026-09-07'
  note: Page exists but every method is an empty stub - feature not actually implemented.
- kind: url
  url: https://store.wildernesslabs.co/products/project-lab-board
  title: 'Project Lab v3 - .NET IoT prototyping platform - Wilderness Labs Store'
  accessed: '2026-09-07'
  note: Confirms Project Lab v3 hardware specs (Meadow F7v2/STM32F7, 3.2" 320x240 ILI9341 IPS TFT, BMI270 IMU, BME688 environmental sensor, BH1760 light sensor, $250 price) used as the badge's underlying hardware.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a maker''s personal software project for the commercial Wilderness Labs "Meadow Project Lab" dev board, not a custom PCB fabricated for or distributed at DEF CON - so quantity/price/availability/hardware_url are all not applicable/unknown. The three JPGs bundled in the repo (defcon32-1/2/3.jpg) are 320x240 splash-screen artwork sized to the display, not photos of the assembled device, so no images were saved per the guide''s "item itself, not a logo" rule. Same maker has a follow-up DEFCON-Badge-2025 repo (github.com/patridge/DEFCON-Badge-2025) for DEF CON 33, not covered by this entry. Battery/power and LED count/type were not stated by any source and are left empty.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/defcon-badge-2024-patridge/
---

A personal, open-source badge software project built by the GitHub user "patridge" for DEF CON 32 (2024). Rather than a custom PCB, it runs on Wilderness Labs' commercial "Meadow Project Lab" board, a $250 .NET IoT prototyping platform built around a Meadow F7v2 (STM32F7) compute module with a 3.2" 320x240 IPS color display, IMU, environmental sensor, and ambient light sensor. The firmware, written in C# against the Meadow SDK, cycles through DEF CON 32 splash artwork and a small set of app "pages": a live environment readout (temperature, pressure, humidity, light level), a graph page, and an unfinished WiFi tracker page whose methods are all empty stubs. The board's four directional buttons page through content and adjust brightness, the onboard RGB LED lights green at startup, and screen brightness auto-adjusts to the ambient light sensor.

Because this targets an existing commercial dev board rather than a badge PCB made for distribution, there was no production run, price, or availability at DEF CON - it appears to be the maker's own device rather than something handed out or sold. The maker followed up with a DEFCON-Badge-2025 repository built the same way for DEF CON 33 (2025), which is not covered by this entry.
