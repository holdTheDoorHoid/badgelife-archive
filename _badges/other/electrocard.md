---
title: Electrocard
id: other-electrocard
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: other
event: other
year: 2017
makers:
- name: Michael Teeuw
  url: https://michaelteeuw.nl/tag/electrocard/
summary: 'A PCB business card with an embedded OLED display that plays a simple horizontal Tetris game via three push buttons.'
functions: 'Powers up to show Michael Teeuw''s contact details on a 128x32 OLED and to play a homebrew horizontal Tetris game controlled with three SMD push switches.'
look:
  colors: []
  shape: card
  themes:
  - retro computer
  - arcade
  - text
tech:
  mcu: ATtiny85
  leds: null
  display: 0.91" 128x32 OLED (SSD1306)
  connectivity: []
  battery: CR2032
  sao_version: none
get_one:
  price: '$8 (assembled, maker estimate)'
  price_usd: 8
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Given out by Michael Teeuw as his personal business card; unpopulated boards served as the plain version, assembled/populated boards went to select contacts. Not sold commercially.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/MichMich/Electrocard
  eda_tool: KiCad
links:
- label: hackaday.io/project/28909-electrocard
  url: https://hackaday.io/project/28909-electrocard
  kind: hackaday
- label: github.com/MichMich/Electrocard
  url: https://github.com/MichMich/Electrocard
  kind: repo
- label: 'michaelteeuw.nl - Electrocard: The Design'
  url: https://michaelteeuw.nl/post/163129358212/electrocard-part-1-the-design/
  kind: article
- label: 'michaelteeuw.nl - Electrocard tag'
  url: https://michaelteeuw.nl/tag/electrocard/
  kind: article
images:
  - file: assets/images/badges/other/electrocard/05c8acd727.jpg
    source: "https://hackaday.io/project/28909-electrocard"
    credit: "Michael Teeuw"
    caption: "The Electrocard PCB business card with OLED display"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/28909-electrocard
  title: Electrocard
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-list); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/28909-electrocard
  title: Electrocard
  accessed: '2026-09-07'
  note: 'Confirmed maker (Michael Teeuw), MCU (ATtiny85), OLED display, CR2032 battery, price estimate, and that it was a Coin Cell Challenge entry, not a conference badge.'
- kind: url
  url: https://github.com/MichMich/Electrocard
  title: 'MichMich/Electrocard on GitHub'
  accessed: '2026-09-07'
  note: 'Confirmed repo contains only PlatformIO firmware (src/lib/flash.sh), no hardware/Gerber files, so hardware is not published even though firmware is.'
- kind: url
  url: https://michaelteeuw.nl/tag/electrocard/
  title: 'Electrocard tag - michaelteeuw.nl'
  accessed: '2026-09-07'
  note: 'Confirmed the build was documented in a blog series (design, soldering, software) and that KiCad was used for the PCB design.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Not a hacker-conference badge: this is Michael Teeuw''s personal PCB business card, originally built as an entry to Hackaday.io''s "Coin Cell Challenge" contest in 2017. No matching event exists in events.yml, so event is left as "other". Quantity made and PCB color/mask are not stated anywhere found. LED field left null since no LEDs are mentioned in any source (only the OLED). Hardware files (KiCad source, Gerbers) were not found published, only the ATtiny85 firmware, so open_source is "partial".'
last_modified_date: '2026-09-07'
---

The Electrocard is Michael Teeuw's take on the electronic business card: a small PCB that carries his contact details but also functions as a tiny game console. An ATtiny85 drives a 0.91" 128x32 OLED module, powered by a single CR2032 coin cell, and three SMD push buttons let the holder play a homebrew "horizontal Tetris" — a game Teeuw chose specifically because it tolerates the low frame rate the ATtiny85/OLED combination can sustain while still being a fun surprise for whoever receives the card.

Teeuw built the board in KiCad and documented the whole process — design, soldering, and firmware — in a blog series on michaelteeuw.nl, and entered the project into Hackaday.io's 2017 Coin Cell Challenge, where it drew significant attention (recorded at over 8,000 views on the project page). Plain, unpopulated boards served as his everyday business card, while fully assembled, working units went to select contacts. It was never sold; it exists as a one-off personal/promotional item rather than something made for a specific hacker conference.

## Make your own

The ATtiny85 firmware (built with PlatformIO) is published on GitHub at MichMich/Electrocard, including a `flash.sh` script for programming the chip. The PCB itself was designed in KiCad, but no KiCad source files or Gerbers appear to be published in the repository or linked from the blog posts, so only the software side can currently be reproduced from public files.
