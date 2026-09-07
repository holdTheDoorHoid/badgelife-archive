---
title: DEFCON-Badge-2025 — Wilderness Labs Meadow Project Lab badge
id: dc33-defcon-badge-2025-wilderness-labs-meadow-project-lab-badge
layout: badge
parent: DC33
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc33
year: 2025
makers:
- name: Adam Patridge (patridge)
  url: https://github.com/patridge
summary: A personal, home-brew DEF CON 33 badge built by developer Adam Patridge (patridge) as custom C#/.NET firmware for Wilderness Labs' commercial "Project Lab" Meadow development board, rather than a from-scratch PCB.
functions: 'Cycles through DEF CON 33 splash artwork and a set of pages: an environment page showing live temperature, humidity, barometric pressure, and ambient light readings from the Project Lab''s onboard sensors, a sine-wave graph demo page, and a WiFi-tracker page that exists in the code but is an empty, unimplemented stub. The onboard RGB LED is set green at boot, and display brightness auto-adjusts to ambient light.'
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - measurement
tech:
  mcu: Meadow F7CoreComputeV2 (STM32F7-based)
  leds:
    count: 1
    type: RGB
    note: onboard status LED, set solid green at boot; not otherwise animated in the firmware
  display: 3.2" ILI9341 TFT LCD, 320x240
  connectivity:
  - i2c
  inputs:
  - buttons
  - accelerometer
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
  hardware_url: null
  firmware_url: https://github.com/patridge/DEFCON-Badge-2025
  eda_tool: null
  license: Apache-2.0
  notes: 'Firmware/software is open source (C#/.NET, Meadow platform); the underlying hardware is Wilderness Labs'' own commercial "Project Lab v3" dev board (https://store.wildernesslabs.co/products/project-lab-board), not a custom PCB designed for this project.'
links:
- label: github.com/patridge/DEFCON-Badge-2025
  url: https://github.com/patridge/DEFCON-Badge-2025
  kind: repo
- label: Wilderness Labs Project Lab v3 (store)
  url: https://store.wildernesslabs.co/products/project-lab-board
  kind: store
images:
- file: assets/images/badges/dc33/defcon-badge-2025-wilderness-labs-meadow-project-lab-badge/6e33347f61.jpg
  source: "https://store.wildernesslabs.co/products/project-lab-board"
  credit: "Wilderness Labs"
  caption: "Wilderness Labs Project Lab v3 board, the hardware patridge's DEF CON 33 badge firmware runs on"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/patridge/DEFCON-Badge-2025
  title: DEFCON-Badge-2025 — Wilderness Labs Meadow Project Lab badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 33/2025''.'
- kind: url
  url: https://raw.githubusercontent.com/patridge/DEFCON-Badge-2025/main/README.md
  title: 'DEFCON-Badge-2025 README'
  accessed: '2026-09-07'
  note: 'One-line README confirming maker, event, and that it is a Meadow Project Lab based badge.'
- kind: url
  url: https://raw.githubusercontent.com/patridge/DEFCON-Badge-2025/main/DefConBadge2025/MeadowApp.cs
  title: 'MeadowApp.cs source'
  accessed: '2026-09-07'
  note: 'Confirmed F7CoreComputeV2 MCU, ProjectLab.Create() hardware abstraction, RGB LED behavior, page-cycling logic, ambient-light-based display brightness.'
- kind: url
  url: https://raw.githubusercontent.com/patridge/DEFCON-Badge-2025/main/DefConBadge2025/Pages/EnvironmentPage.cs
  title: 'EnvironmentPage.cs source'
  accessed: '2026-09-07'
  note: 'Confirmed temperature, barometric pressure, humidity, and light sensor readouts.'
- kind: url
  url: https://raw.githubusercontent.com/patridge/DEFCON-Badge-2025/main/DefConBadge2025/Pages/WiFiTrackerPage.cs
  title: 'WiFiTrackerPage.cs source'
  accessed: '2026-09-07'
  note: 'Confirmed this page is an empty stub with no implemented logic.'
- kind: url
  url: https://raw.githubusercontent.com/patridge/DEFCON-Badge-2025/main/LICENSE
  title: 'LICENSE'
  accessed: '2026-09-07'
  note: 'Confirmed Apache-2.0 license.'
- kind: url
  url: https://github.com/WildernessLabs/Meadow.ProjectLab
  title: 'WildernessLabs/Meadow.ProjectLab'
  accessed: '2026-09-07'
  note: 'Confirmed Project Lab board specs: F7FeatherV2/Meadow MCU family, ILI9341 320x240 display, BMI270/BH1750/BME688 sensors over I2C, 4 buttons.'
- kind: url
  url: https://store.wildernesslabs.co/products/project-lab-board
  title: 'Project Lab v3 — Wilderness Labs Store'
  accessed: '2026-09-07'
  note: 'Product photo used for images; confirmed Project Lab v3 retail price ($250) for the base dev board (not the badge itself, which was not sold).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'This is a home-brew personal badge: a software/firmware project (C#/.NET, Apache-2.0) written to run on Wilderness Labs'' existing commercial "Project Lab v3" development board, not a custom PCB made for DEF CON 33. No photos of the maker''s actual assembled unit were found, so the saved image is the manufacturer''s stock photo of the underlying board. No pricing, quantity, or distribution applies since it was not sold or given away as a badge — availability left unknown. Battery/power details and full connectivity (the board is known in general to include other options) were not confirmed in the sources checked, so left empty per the never-guess rule. The WiFiTrackerPage class exists but has no implementation, suggesting a planned but unfinished feature.'
last_modified_date: '2026-09-07'
---

This is a home-brew DEF CON 33 (2025) badge built by developer Adam Patridge, who goes by "patridge" on GitHub. Rather than designing a custom PCB, Patridge wrote custom C#/.NET firmware (using Wilderness Labs' Meadow platform) that runs on Wilderness Labs' own commercial "Project Lab v3" development board — a $250 prototyping board built around a Meadow F7 core compute module, with a 3.2" 320x240 TFT display, onboard environmental and motion sensors, four buttons, and an RGB status LED.

The firmware cycles through DEF CON 33 splash artwork alongside a small set of "pages": one showing live temperature, humidity, barometric pressure, and ambient-light readings pulled from the board's onboard sensors, and a scrolling sine-wave graph demo. A third page, intended to be a WiFi tracker, exists in the source as an empty class with no implemented behavior — apparently a planned feature that wasn't finished before the con. The onboard RGB LED is set to solid green at startup, and the display's backlight brightness adjusts automatically based on the ambient light sensor.

The project's source code and artwork are published on GitHub under the Apache-2.0 license, but there is no custom hardware design here — anyone wanting to build the same badge would need their own Project Lab board and would flash this firmware onto it. It does not appear to have been sold, kitted, or distributed to other attendees; it reads as a one-off personal project Patridge built to wear and use at the con.
