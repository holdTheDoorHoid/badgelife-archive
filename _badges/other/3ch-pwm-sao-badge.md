---
title: 3ch_pwm_sao_badge
id: other-3ch-pwm-sao-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 0
makers:
- name: 9a
  url: https://github.com/9a
summary: A SAO-compatible 3-channel PWM driver board built around an ATtiny402, made to power 3D-printed "LED noodle" mini neon signs.
functions: Drives up to three channels of LEDs (or LED noodle/flexible strip lighting) independently via PWM from the onboard ATtiny402.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: ATtiny402
  leds: null
  display: null
  connectivity: []
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
  open_source: true
  hardware_url: https://github.com/9a/3ch_pwm_sao_badge/tree/main/sao_kicad_files
  firmware_url: https://github.com/9a/3ch_pwm_sao_badge/blob/main/sao_3ch_pwm.ino
  eda_tool: KiCad
links:
- label: github.com/9a/3ch_pwm_sao_badge
  url: https://github.com/9a/3ch_pwm_sao_badge
  kind: repo
images:
- file: assets/images/badges/other/3ch-pwm-sao-badge/b4cf05d135.jpg
  source: https://github.com/9a/3ch_pwm_sao_badge
  credit: 9a
  caption: Top side of the 3ch PWM SAO badge
- file: assets/images/badges/other/3ch-pwm-sao-badge/86f22a30a5.jpg
  source: https://github.com/9a/3ch_pwm_sao_badge
  credit: 9a
  caption: Bottom side of the 3ch PWM SAO badge
contact: {}
notes:
- 3ch PWM LED SAO on ATtiny402
status: released
sources:
- kind: url
  url: https://github.com/9a/3ch_pwm_sao_badge
  title: 3ch_pwm_sao_badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/9a/3ch_pwm_sao_badge
  title: 9a/3ch_pwm_sao_badge - GitHub
  accessed: '2026-09-07'
  note: 'README and repo contents confirm: ATtiny402-based 3-channel PWM SAO for driving 3D-printed LED noodle badges (linked Printables designs: LED Noodle Ghost and Animated Cat mini neon signs); KiCad 7.0 hardware files, Arduino .ino firmware, BOM, schematic PDF and Gerbers included in the repo (no explicit license file); no price, quantity, con/event, or year stated anywhere in the repo.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: This reads as a personal open-hardware SAO project shared on GitHub, not tied to any specific convention or year -- the repo, README, and maker's GitHub profile give no event, date, price, or distribution details. Left event as "other" and year as 0 since no con could be identified. No license file is present in the repo, so make_your_own.license is left empty rather than guessed. LED count/type and PCB color are not stated in the repo or images closely enough to state with confidence, so left empty.
last_modified_date: '2026-09-07'
model:
  file: assets/models/other/3ch-pwm-sao-badge.glb
  method: kicad
  source_file: sao_kicad_files/sao_pcb.kicad_pcb
  generated: '2026-09-07'
  bytes: 107652
---

The 3ch PWM SAO badge is a small SAO (Shitty Add-On) board by GitHub user 9a, built around an ATtiny402 microcontroller. It provides three independent PWM-controlled channels, intended to drive LEDs or flexible "LED noodle" strips -- the kind used in 3D-printed mini neon sign projects such as the Printables "LED Noodle Ghost" and "LED Noodle Animated Cat" designs the maker links to in the README.

Unlike most entries in this archive, the project isn't tied to a specific convention badge; it's shared purely as an open-hardware add-on for hobbyists building their own light-up projects, with no stated price, production run, or event of origin.

## Make your own

The repository includes KiCad 7.0 schematic and PCB files, PCB Gerbers, a bill of materials (BOM), and an Arduino sketch (`sao_3ch_pwm.ino`) for the firmware. The README notes that when programming via the Arduino IDE, `millis()` should be disabled in the Tools menu. No license is stated for the shared files.
