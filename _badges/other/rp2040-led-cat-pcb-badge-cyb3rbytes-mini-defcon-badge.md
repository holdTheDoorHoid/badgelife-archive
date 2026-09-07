---
title: RP2040-LED-Cat-PCB-badge — Cyb3rBytes mini-DefCon badge
id: other-rp2040-led-cat-pcb-badge-cyb3rbytes-mini-defcon-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 0
makers:
- name: Cyb3rBytes404
summary: 'A Felix-the-cat-shaped RP2040 learning badge built for the Cyb3rBytes404 cyber coding camp, taught with MicroPython LED-animation challenges.'
functions: 'Runs MicroPython scripts that drive 30 WS2812 LEDs through effects such as "Shake Shake" (read from the onboard accelerometer), Twinkle Stars, Bouncing LEDs, Matrix, Meteor, Fireworks Cannon, Hyper Jump, and a Knight-Rider-style scan; a `challenges/` folder walks students from lighting a single LED up through a full rainbow-cycle animation.'
look:
  colors:
  - white
  - black
  shape: cat
  themes:
  - cat
  - learn to solder
  - security
tech:
  mcu: RP2040
  leds:
    count: 30
    type: WS2812B
    note: Also called WS2812 / NeoPixel in the maker's docs; driven from a GPIO pin via MicroPython's neopixel.py.
  display: none
  connectivity:
  - usb
  - i2c
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Distributed to participants of the Cyb3rBytes404 cyber coding camp; not sold on a public storefront that could be found.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/Cyb3rBytes404/RP2040-LED-Cat-PCB-badge
  eda_tool: null
links:
- label: github.com/Cyb3rBytes404/RP2040-LED-Cat-PCB-badge
  url: https://github.com/Cyb3rBytes404/RP2040-LED-Cat-PCB-badge
  kind: repo
images:
  - file: assets/images/badges/other/rp2040-led-cat-pcb-badge-cyb3rbytes-mini-defcon-badge/3d8265fa08.png
    source: "https://github.com/Cyb3rBytes404/RP2040-LED-Cat-PCB-badge"
    credit: "Cyb3rBytes404"
    caption: "Board layout render showing the cat-head PCB outline, 30 WS2812 LEDs, RP2040 module, and LIS3DH accelerometer"
  - file: assets/images/badges/other/rp2040-led-cat-pcb-badge-cyb3rbytes-mini-defcon-badge/83cb8fbdbd.png
    source: "https://github.com/Cyb3rBytes404/RP2040-LED-Cat-PCB-badge"
    credit: "Cyb3rBytes404"
    caption: "Felix-the-cat-shaped PCB with copper traces forming the eyes"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Cyb3rBytes404/RP2040-LED-Cat-PCB-badge
  title: RP2040-LED-Cat-PCB-badge — Cyb3rBytes mini-DefCon badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/Cyb3rBytes404/RP2040-LED-Cat-PCB-badge
  title: "Cyb3rBytes404/RP2040-LED-Cat-PCB-badge — README"
  accessed: '2026-09-07'
  note: "Confirms it is teaching hardware for the Cyb3rBytes404 cyber coding camp (not a specific DEF CON event badge), lists RP2040 + MPU-6050/LIS3DH + 30x WS2812 LEDs, MicroPython firmware, and 'Designed & assembled in ... San Diego, California' silkscreen text."
- kind: url
  url: https://raw.githubusercontent.com/Cyb3rBytes404/RP2040-LED-Cat-PCB-badge/main/assets/logo3.png
  title: "Board layout image (assets/logo3.png)"
  accessed: '2026-09-07'
  note: "Shows the actual PCB silkscreen: 30 labeled LEDs, an RP2040 module, a LIS3DH breakout header, and 'Designed & assembled in ... San Diego, California'."
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    The repo's own tagline calls it "The Ultimate Mini-DefCon style badge for
    Future Tech Heroes" but the README and repo content make clear it is
    educational hardware for the Cyb3rBytes404 cyber coding camp (aimed at kids
    learning MicroPython/electronics), not a badge made for or distributed at
    an actual DEF CON event — "mini-DefCon" reads as a stylistic description,
    not an event tie. No matching event id exists in events.yml for this
    camp, so event is left as "other". The README names an MPU-6050
    accelerometer while the board silkscreen (assets/logo3.png) labels the
    same header "LIS3DH" — sources disagree on the exact accelerometer part.
    No pricing, unit quantity, sale channel, or specific year could be found;
    the repo has no commit history or release dates visible via the GitHub
    API fetch used here. Only firmware (MicroPython scripts) is published;
    no hardware design files (schematic, PCB layout, gerbers) were found in
    the repository, so make_your_own.open_source is "partial" rather than
    "yes".
last_modified_date: '2026-09-07'
---

The RP2040-LED-Cat-PCB-badge is a Felix-the-cat-shaped learning board made for the Cyb3rBytes404 cyber coding camp, a program that teaches kids MicroPython and basic electronics through an "ethical hacker" framing. Despite its GitHub tagline calling it a "Mini-DefCon style badge," nothing in the repository ties it to an actual DEF CON event — it reads as a stylistic nod rather than an event badge, and the board is instead camp-issued hardware with a "this board belongs to: [blank] — a future computer engineer" fill-in field silkscreened on the back.

The board carries an RP2040 microcontroller, an onboard accelerometer (called MPU-6050 in the README text but labeled LIS3DH on the actual silkscreen), and 30 WS2812 RGB LEDs arranged across the cat-head-shaped PCB, with USB-C for power and programming. Its repository ships only the MicroPython firmware side: a `neopixel.py` driver and a set of numbered effect scripts (Shake Shake, Twinkle Stars, Bouncing LEDs, Matrix, Meteor, Fireworks Cannon, Hyper Jump, and a moving-LED scan effect), plus a `challenges/` folder that walks a student from lighting one LED to a full rainbow cycle. No schematic, PCB layout, or gerber files are included, so the hardware design itself is not published — only the software that runs on it. The board's own artwork includes a second Felix-the-cat motif where copper traces form the character's eyes as a decorative element on the PCB.

No information was found on unit price, how many were made, or whether the badge was ever offered outside the camp itself; it appears to have been given to camp participants rather than sold.
