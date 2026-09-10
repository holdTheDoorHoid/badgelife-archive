---
title: ScryptKeeper
id: other-scryptkeeper
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2021
makers:
- name: HTHackers
  url: https://hthackers.com
summary: A CircuitPython-powered HID badge made for the 2021 Hackers Teaching Hackers conference in Columbus, Ohio. It starts locked behind a set of on-board challenges shown on its "brain" LEDs, and once unlocked doubles as a full keyboard/mouse emulator.
functions: Ships locked with four challenge gates (binary, cryptography, Morse code, UART protocol discovery, plus a steganography step) that must be solved over a 9600-baud serial connection to unlock full functionality. Unlocked, it offers a CircuitPython Python REPL over USB-C, "Bling Mode" RGB LED animations, a "Mouse Jiggler" that nudges the mouse periodically, and a "Ducky Payload" mode that plays back USB Rubber Ducky-style HID attacks from an editable duckyscript.txt file. Modes are triggered by capacitive touch zones on the board (front brain, nose, mouth).
look:
  colors:
  - black
  - green
  - red
  - multicolor
  shape: circle
  themes:
  - horror
  - skull
  - security
  - ctf
  - puzzle
tech:
  mcu: ATSAMD21E
  leds:
    count: null
    type: RGB
    note: Called "brain LEDs" by the maker; used as binary/progress indicators for each challenge (pulsing red while locked) and for the RGB "Bling Mode" animations. Exact count and LED part number not stated.
  display: none
  connectivity:
  - usb
  - uart
  inputs:
  - touch
  - capacitive
  battery: none
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
  hardware_url: https://github.com/HTHackers/ScryptKeeper/tree/main/ScryptKeeper/Badge%20Source
  firmware_url: https://github.com/HTHackers/ScryptKeeper/tree/main/ScryptKeeper/Firmware
  gerbers_url: https://github.com/HTHackers/ScryptKeeper/tree/main/ScryptKeeper/Gerber%20Fabrication%20Files
  eda_tool: KiCad
links:
- label: github.com/HTHackers/ScryptKeeper
  url: https://github.com/HTHackers/ScryptKeeper
  kind: repo
- label: github.com/syn-ack-zack/ScryptKeeper (original repo)
  url: https://github.com/syn-ack-zack/ScryptKeeper
  kind: repo
- label: Badge Walkthrough wiki
  url: https://github.com/syn-ack-zack/ScryptKeeper/wiki/Badge-Walkthrough
  kind: doc
- label: Hackers Teaching Hackers
  url: https://hthackers.com
  kind: website
images:
- file: assets/images/badges/other/scryptkeeper/f802d11918.jpg
  source: https://github.com/HTHackers/ScryptKeeper
  credit: HTHackers
  caption: The ScryptKeeper badge, lit up, showing its printed monster-face artwork, brain LEDs, and lanyard
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/HTHackers/ScryptKeeper
  title: ScryptKeeper
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://raw.githubusercontent.com/HTHackers/ScryptKeeper/main/README.md
  title: The ScryptKeeper (README)
  accessed: '2026-09-07'
  note: Confirms it was made for the 2021 Hackers Teaching Hackers badge; describes CircuitPython HID features, Bling/Jiggler/Ducky modes, and touch zones; source of the badge photo.
- kind: url
  url: https://github.com/syn-ack-zack/ScryptKeeper/wiki/Badge-Walkthrough
  title: Badge Walkthrough wiki
  accessed: '2026-09-07'
  note: Confirms ATSAMD21E MCU, the four/five challenge steps (binary, crypto, Morse, UART, steganography), brain LEDs, lanyard hole, and touch zones. No price, quantity, or battery info given.
- kind: url
  url: https://hthackers.com
  title: Hackers Teaching Hackers
  accessed: '2026-09-07'
  note: Confirms Hackers Teaching Hackers is an annual infosec conference in Columbus, Ohio (est. 2014, held at BrewDog DogTap); no matching event id exists in events.yml.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: No matching event id in events.yml for "Hackers Teaching Hackers" (a small annual Columbus, OH con, not DEF CON) -- event left as "other"; the con and year are recorded here and in the summary/year field instead. Price, quantity made, and availability were not stated anywhere found. The repo also contains a second item, a "Scouter-SAO" (an SAO-style daughterboard, visible plugged into the badge in the photo), which is a separate item and was not researched further -- see other_items_found.
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/scryptkeeper.glb
  method: gerber
  source_file: ScryptKeeper/Gerber Fabrication Files
  generated: '2026-09-10'
  bytes: 184572
  size_mm:
  - 103.9
  - 114.5
  note: The published files have no board outline, so the model is shown on a rectangular board.
---

The ScryptKeeper is a CircuitPython-powered HID badge that HTHackers (Hackers Teaching Hackers) made for their 2021 conference in Columbus, Ohio. It is printed as a snarling green monster face on a round black PCB, with a set of "brain" LEDs standing in for both decoration and a progress meter: the badge ships locked, pulsing red until its wearer solves a chain of on-board challenges over a 9600-baud serial link -- binary, cryptography, Morse code, a UART protocol puzzle, and steganography.

Once unlocked, the badge exposes a second USB device carrying a live CircuitPython REPL, turning it into a fully scriptable HID platform. Three modes are wired to capacitive touch zones shaped like facial features (front brain, nose, mouth): a "Bling Mode" of RGB LED animations, a "Mouse Jiggler" that nudges the cursor every few seconds, and a "Ducky Payload" mode that plays back a USB Rubber Ducky-style keystroke script from an editable file on the badge.

Hardware (KiCad source and Gerbers), firmware, and a full puzzle walkthrough are published in the maker's GitHub repository, forked from the original by syn-ack-zack. No price, production quantity, or ongoing availability information was found.

## Make your own

KiCad board files, compiled Gerbers for fabrication, and the CircuitPython firmware are all in the repository:

- Board source: https://github.com/HTHackers/ScryptKeeper/tree/main/ScryptKeeper/Badge%20Source
- Firmware: https://github.com/HTHackers/ScryptKeeper/tree/main/ScryptKeeper/Firmware
- Gerbers: https://github.com/HTHackers/ScryptKeeper/tree/main/ScryptKeeper/Gerber%20Fabrication%20Files
