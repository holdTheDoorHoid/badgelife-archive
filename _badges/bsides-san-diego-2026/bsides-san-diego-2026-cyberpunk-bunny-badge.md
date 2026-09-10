---
title: BSides San Diego 2026 Cyberpunk Bunny Badge
id: bsides-san-diego-2026-bsides-san-diego-2026-cyberpunk-bunny-badge
layout: badge
parent: BSides San Diego 2026
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-san-diego-2026
year: 2026
makers:
- name: Electronic Cats
  url: https://electroniccats.com
summary: A standalone cryptography-challenge badge for BSides San Diego 2026, cyberpunk-bunny themed, with a two-tier cipher CTF and BLE co-op play between badges.
functions: Shake-activated "Magic 8 Ball" fortune mode; a gated CTF with three classical-cipher challenges (basic tier) and four modern-cryptography challenges (advanced tier, covering encoding, bitwise ops, a stream cipher, and AES-128/ChaCha20 per the bsidessd.org description); a BLE co-op mode where two badges within ~10cm negotiate roles and unlock together; a hidden "Forbidden Shake" easter egg that broadcasts an event to every badge in BLE range.
look:
  colors: []
  shape: rabbit
  themes:
  - animal
  - cyberpunk
  - security
  - ctf
  - puzzle
tech:
  mcu: ESP32-C6
  leds:
    count: 2
    type: WS2812B
    note: 'Status colors: solid blue at boot, solid red idle, blinking red on BLE handshake, rainbow cycling when all advanced challenges are complete, solid red (instant) when Forbidden Shake triggers.'
  display: 0.96" OLED (SH1106G, 128x64, I2C)
  connectivity:
  - ble
  inputs:
  - joystick
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
  hardware_url: https://github.com/ElectronicCats/badge-bsides-sandiego-2026/tree/main/hardware
  firmware_url: https://github.com/ElectronicCats/badge-bsides-sandiego-2026/tree/main/Firmware
  eda_tool: KiCad
  license: MIT
links:
- label: github.com/ElectronicCats/badge-bsides-sandiego-2026
  url: https://github.com/ElectronicCats/badge-bsides-sandiego-2026
  kind: repo
- label: www.bsidessd.org/activities/badge-challenge
  url: https://www.bsidessd.org/activities/badge-challenge
  kind: website
- label: badge.gallery/events/bsides-san-diego-2026
  url: https://badge.gallery/events/bsides-san-diego-2026
  kind: website
images: []
contact: {}
notes:
- Official BSides San Diego 2026 conference badge, a Cyberpunk Bunny-shaped ESP32-C6 device with OLED display, joystick, addressable LEDs, BLE co-op cryptography CTF and a hidden 'Forbidden Shake' easter-egg mode. Found by the event-year sweep, task bsides-bsides-san-diego.
- 'Title confirmed as-is; the sweep''s wording matched the maker''s own README title ("Badge BSides San Diego 2026") and the con site''s "Cyberpunk Bunny" framing, so no correction was needed.'
status: listed
sources:
- kind: url
  url: https://github.com/ElectronicCats/badge-bsides-sandiego-2026
  title: BSides San Diego 2026 Cyberpunk Bunny Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-san-diego); event read as ''BSides San Diego 2026''.'
- kind: url
  url: https://github.com/ElectronicCats/badge-bsides-sandiego-2026
  title: 'Electronic Cats: Badge BSides San Diego 2026 (README)'
  accessed: '2026-09-10'
  note: Confirmed maker, event, MCU (ESP32-C6), display (SH1106G OLED 128x64 I2C), 2x WS2812B LEDs, joystick+boot button input, accelerometer, BLE, LED status-color meanings, KiCad hardware files under hardware/, MIT license, and the challenge/co-op/Forbidden-Shake mechanics.
- kind: url
  url: https://www.bsidessd.org/activities/badge-challenge
  title: BSides San Diego — Badge Challenge
  accessed: '2026-09-10'
  note: Confirmed "Cyberpunk Bunny" naming/shape, D-pad/joystick and accelerometer, BLE co-op, shake-activated "Hacker Oracle" 8-ball mode, and named the advanced-tier ciphers (Base32, XOR, AES-128, ChaCha20). No pricing, quantity, or availability given.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: The maker's repo and the con's own activity page both confirm the badge is real and describe it consistently; confidence is medium rather than high because neither source states price, quantity produced, availability, or battery/power details, and no photo of the physical badge could be located (only the Electronic Cats logo appears in the repo, and the con's badge-challenge page is a JS-rendered Google Sites page that did not yield an identifiable product photo within the research budget). look.shape was inferred as "rabbit" from the "Cyberpunk Bunny" name plus the con page's description, not from a photo, so should be reweighted if a photo later shows otherwise.
last_modified_date: '2026-09-10'
---

Electronic Cats built the BSides San Diego 2026 conference badge as a standalone cryptography-challenge device shaped like a "Cyberpunk Bunny." It runs on an ESP32-C6 with a small SH1106G OLED display, a 4-axis joystick and boot button for navigation, an onboard accelerometer for shake detection, and two WS2812B addressable LEDs that report status (blue at boot, red when idle, rainbow once the advanced challenges are cleared).

The badge's core activity is a two-tier CTF: three classical-cipher puzzles (substitution, rotation, transposition) unlock a basic flag, and four modern-cryptography puzzles — described on the con's site as covering Base32 encoding, XOR, AES-128, and ChaCha20 — unlock an advanced flag. Two badges brought within about 10cm of each other negotiate roles over Bluetooth Low Energy and can unlock a cooperative flag together; there's also a manual fallback for solo players. A shake gesture triggers a "Magic 8 Ball" fortune mode (called the "Hacker Oracle" on the con page), and a hidden "Forbidden Shake" sequence — reachable only after meeting certain prerequisites — broadcasts a visible event to every other badge in BLE range.

Electronic Cats published the full design under the MIT license: KiCad PCB/schematic files live in the repo's `hardware/` folder, and Arduino-based firmware (with esptool instructions for reading a badge's flash and cloning it onto a fresh board, aside from the eFuse-burned MAC/BLE identity) lives under `Firmware/`. Neither the repository nor the con's activity page states a price, production quantity, or public availability, so those fields are left blank.
