---
title: Vectrex SAO
id: supercon-2022-vectrex-sao
layout: badge
parent: Supercon 2022
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2022
year: 2022
makers:
- name: Brett Walach (@Technobly)
  url: https://github.com/technobly
summary: A miniature playable Vectrex console in SAO form with a 7x10 Charlieplexed white LED display running a low-res Scramble variant, a one-button capacitive-touch controller on a hand-made coily cord, a PIC16F886 MCU, speaker, saved high score, and I2C/PWM hacking jumpers, made for Hackaday Supercon 2022.
functions: Plays a miniature low-res version of the arcade game Scramble on its LED display; capacitive-touch single-button controller connected via a hand-made coiled cord; built-in speaker (mutable); permanently saves high score; exposes I2C and PWM for hacking/expansion.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - console
  - arcade
tech:
  mcu: PIC16F886
  leds:
    count: 70
    type: charlieplexed
    note: 7x10 white LED matrix arranged in slight perspective to match Vectrex artwork
  display: LED matrix 7x10
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
  hardware_url: https://github.com/technobly/vectrex-sao
  firmware_url: https://github.com/technobly/vectrex-sao
  eda_tool: KiCad
  license: CC BY-SA 4.0
  notes: Repository includes KiCad schematics/PCB, Gerbers, and firmware source.
links:
- label: github.com/technobly/vectrex-sao
  url: https://github.com/technobly/vectrex-sao
  kind: repo
- label: hackaday.io/project/197854-vectrex-sao
  url: https://hackaday.io/project/197854-vectrex-sao
  kind: hackaday
- label: youtu.be/AfYQyKARwps
  url: https://youtu.be/AfYQyKARwps
  kind: video
images:
- file: assets/images/badges/supercon-2022/vectrex-sao/20d34785b4.jpg
  source: "https://github.com/technobly/vectrex-sao"
  credit: "Brett Walach (technobly)"
  caption: "Vectrex SAO board with 7x10 Charlieplexed LED display and coiled-cord controller"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/technobly/vectrex-sao
  title: 'technobly/vectrex-sao: Vectrex SAO for Hackaday Supercon.6 2022'
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/technobly/vectrex-sao
  title: technobly/vectrex-sao README
  accessed: '2026-09-07'
  note: 'Confirmed maker, event/year ("Made for Hackaday Supercon 2022"), MCU (PIC16F886), LED count/layout, features (Scramble game, capacitive touch, coily cord, speaker, saved high score, I2C/PWM), open-source status (KiCad + Gerbers + firmware, CC BY-SA 4.0), and image path.'
- kind: url
  url: https://hackaday.io/project/197854-vectrex-sao
  title: Vectrex SAO - Hackaday.io
  accessed: '2026-09-07'
  note: Corroborates description and features; project gallery has additional build photos (not independently verified for licensing so not saved).
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Price, quantity made, and current availability are not stated anywhere in the maker's repo, Hackaday.io project page, or video description; left empty rather than guessed. The Hackaday.io fetch also surfaced a line referencing "Supercon 8 SAO Contest (2024)" but the maker's own repo README explicitly says "Made for Hackaday Supercon 2022" and the repo title says "Supercon.6 2022" (Supercon.6 = 2022), so event/year is kept as 2022; noting the discrepancy here rather than acting on the unverified 2024 mention.
last_modified_date: '2026-09-07'
---

Brett Walach's Vectrex SAO shrinks the classic Vectrex arcade console down to badge-accessory scale for Hackaday Supercon 2022. A 7x10 Charlieplexed array of 70 white LEDs is arranged in a slight forced perspective to echo the original Vectrex's angled cabinet artwork, and it plays a low-resolution version of the arcade game Scramble. A single capacitive-touch button serves as the controller, wired to the SAO board through a hand-made coiled cord reminiscent of an old console controller cable.

The board runs on a PIC16F886 microcontroller, includes a small speaker (with mute), and permanently saves the player's high score across power cycles. It also breaks out I2C and PWM so hackers can extend or repurpose it. Hardware (KiCad schematics, PCB layout, and Gerbers) and firmware are published on GitHub under a CC BY-SA 4.0 license, making it fully open source, though the maker's pages do not state a price, production quantity, or whether it is still available.
