---
title: Power Slug SAO
id: supercon-2024-power-slug-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Ticktok
  url: https://hackaday.io/Ticktok
summary: A Satisfactory-themed SAO with a 3D-printed hollow translucent PETG power slug over a through-hole RGB LED, driven by an ATtiny1614 that picks blue, yellow, or magenta at startup and pulses it, with I2C control at address 0x55; made for the Supercon 8 (2024) SAO contest.
functions: 'Randomly picks blue, yellow, or magenta on power-up and pulses that color like the power slug item from the video game Satisfactory. Supports multiple modes over I2C (address 0x55): the default power-slug pulse, a blink mode, a custom fade, and a GPIO-trigger mode, with brightness, PWM timing, and fade duration adjustable via registers. Designed to integrate with the Supercon 2024 badge''s button and touch-wheel controls.'
look:
  colors:
  - clear
  shape: null
  themes:
  - pop culture
tech:
  mcu: ATtiny1614
  leds:
    count: 1
    type: RGB
    note: 5mm through-hole RGB LED (common anode), housed inside a hollow translucent PETG 3D-printed "power slug" shell
  display: null
  connectivity:
  - i2c
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Made for the Supercon 8 (2024) SAO contest; not documented as sold separately.
make_your_own:
  open_source: 'yes'
  hardware_url: https://codeberg.org/ticktok/Satisfactory_Slug_SAO
  firmware_url: https://codeberg.org/ticktok/Satisfactory_Slug_SAO
  eda_tool: KiCad
links:
- label: hackaday.io/project/198996-power-slug-sao
  url: https://hackaday.io/project/198996-power-slug-sao
  kind: hackaday
- label: codeberg.org/ticktok/Satisfactory_Slug_SAO
  url: https://codeberg.org/ticktok/Satisfactory_Slug_SAO
  kind: repo
images:
- file: assets/images/badges/supercon-2024/power-slug-sao/0057c64657.jpg
  source: "https://hackaday.io/project/198996-power-slug-sao"
  credit: "Ticktok"
  caption: "The Power Slug SAO with translucent 3D-printed slug housing over an RGB LED"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198996-power-slug-sao
  title: Power Slug SAO
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/198996-power-slug-sao
  title: Power Slug SAO
  accessed: '2026-09-07'
  note: Confirmed maker, event/year, MCU, LED, I2C address and modes, and open-source status; source image used for the entry photo.
- kind: url
  url: https://codeberg.org/ticktok/Satisfactory_Slug_SAO
  title: Satisfactory_Slug_SAO repository
  accessed: '2026-09-07'
  note: Confirmed hardware/firmware files present (KiCad project, schematics, Blender/STL 3D models, Arduino firmware, LICENSE file) and design details about a resistor rework and PCB panelization issue.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday.io project page and Codeberg repo both confirm the core facts (maker, event, MCU, LED, I2C protocol, open-source files). Price, quantity made, and retail availability are not stated anywhere found; the maker describes it as an ongoing project with manufacturing issues (resistor rework needed, PCB panelization problems), so it is treated as released/distributed at the contest rather than sold. No additional maker photos beyond the one saved were confirmed reachable without further searching.
last_modified_date: '2026-09-07'
---

The Power Slug SAO is a Simple Add-On built by the Hackaday.io maker Ticktok for the Supercon 8 (2024) SAO contest. It reimagines the "power slug" item from the video game Satisfactory as a small glowing add-on: a hollow, translucent PETG shell 3D-printed to look like the slug sits over a 5mm RGB LED, so the whole piece lights up rather than showing a bare LED. On power-up it randomly selects blue, yellow, or magenta — the slug's three in-game power tiers — and pulses that color.

Under the hood, an ATtiny1614 drives the LED and exposes an I2C interface at address 0x55, letting a host badge (such as Supercon 2024's own badge) switch between the default power-slug pulse, a blink mode, a custom fade, and a GPIO-trigger mode, with brightness, PWM timing, and fade duration adjustable through registers. The maker built it to respond to the host badge's button and touch-wheel controls.

Hardware and firmware are fully open source on Codeberg, including the KiCad project, schematics, Blender/STL models for the 3D-printed slug shell, and Arduino firmware. The maker notes the boards shipped with a current-limiting resistor mistake that needed a "deadbug style" through-hole rework, and that panelization issues meant boards had to be separated by hand — details that place it as a hobbyist contest entry rather than a polished commercial product. No price, production quantity, or separate sale of the SAO was found in the sources reviewed.
