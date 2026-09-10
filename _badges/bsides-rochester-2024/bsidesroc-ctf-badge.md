---
title: BSidesROC CTF Badge
id: bsides-rochester-2024-bsidesroc-ctf-badge
layout: badge
parent: BSides Rochester 2024
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bsides-rochester-2024
year: 2024
makers:
- name: Hackerwares
  url: https://www.hackerwares.com/index.html
summary: A solder-your-own CTF badge for BSidesROC 2024 with a flower-shaped LED cutout that lights up as challenges are solved.
functions: 'Solder-your-own badge whose CTF is played over a micro-USB serial connection: participants connect via Arduino IDE (1.8.x), open the Serial Monitor at 9600 baud, and enter lowercase flags to unlock the badge''s LEDs, working through several challenge levels (one hint involves decoding a Morse-code string) to "unlock all lights forever."'
look:
  colors:
  - black
  - gold
  shape: null
  themes:
  - ctf
  - learn to solder
  - puzzle
tech:
  mcu: null
  leds:
    count: null
    type: reverse-mount
    note: 'Reverse-mount LEDs arranged in a flower-petal cutout (red) plus a separate RGB LED in a gear-shaped cutout; LEDs are solder-it-yourself and unlock progressively as CTF flags are solved.'
  display: null
  connectivity:
  - usb
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
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackerware.io/bsidesroc
  url: https://hackerware.io/bsidesroc
  kind: website
- label: BSidesROC Badge Hacking (PDF instructions)
  url: https://hackerware.io/bsidesroc.pdf
  kind: doc
- label: BSidesROC BadgeCTF Hints
  url: https://hackerware.io/bsidesrochints
  kind: website
- label: Hackerwares - #BadgeLife
  url: https://www.hackerwares.com/index.html
  kind: website
images:
- file: assets/images/badges/bsides-rochester-2024/bsidesroc-ctf-badge/d7a27c77cf.jpg
  source: "https://hackerware.io/bsidesroc"
  credit: "Hackerwares"
  caption: "BSidesROC CTF Badge: black PCB with a red-LED flower cutout and a gear-shaped RGB LED cutout, shown next to the badge's serial CTF terminal"
contact: {}
notes:
- 'Sweep found the item via the maker''s CTF instructions page; entry originally listed the maker as "Hackerware(s)" — the site''s own copyright line and companion site read "Hackerwares."'
- 'Site copyright is dated 2024 and the CTF flag text reads "bsides-roc-n-roll"; exact hardware specs (MCU, LED count, price, quantity, open-source status) are not published anywhere on the maker''s pages.'
status: released
sources:
- kind: url
  url: https://hackerware.io/bsidesroc
  title: BSidesROC CTF Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bsides-bsides-rochester); event read as ''BSides Rochester 2024''.'
- kind: url
  url: https://hackerware.io/bsidesroc.pdf
  title: BSides ROC Badge Hacking
  accessed: '2026-09-10'
  note: 'Confirms CTF mechanics: micro-USB, Arduino IDE 1.8.x, Serial Monitor 9600 baud, lowercase flags.'
- kind: url
  url: https://hackerware.io/bsidesrochints
  title: BSidesROC BadgeCTF Hints
  accessed: '2026-09-10'
  note: 'Hints page confirms a multi-level CTF including a Morse-code-decoding step; page copyright reads "Hackerwares 2024".'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-10'
  notes: 'Maker''s own pages confirm the badge exists, its event/year, and its CTF mechanics; photo (saved) confirms physical appearance (black PCB, flower-shaped red-LED cutout, gear-shaped RGB LED cutout, gold silkscreen). Could not find MCU, LED count/part number, price, quantity made, availability, or open-source/design-file status on any page — left empty rather than guessed. No separate Hackaday, Tindie, or GitHub listing found for this specific badge.'
last_modified_date: '2026-09-10'
---

The BSidesROC CTF Badge is a solder-your-own electronic badge that Hackerwares built for BSides Rochester 2024. Rather than arriving fully assembled, it ships with LEDs the wearer solders on themselves, set into a flower-shaped cutout on the black PCB alongside a separate gear-shaped cutout holding an RGB LED, with "BSidesROC" lettered across the board in gold.

The badge doubles as the event's CTF: it connects to a computer over micro-USB, and players open the Arduino IDE's Serial Monitor (9600 baud, Arduino IDE 1.8.x) to interact with the badge's firmware. Entering the right lowercase flag at each stage unlocks more of the badge's lights, with the goal of solving enough challenges to "unlock all lights forever." A companion hints page walks through at least one puzzle involving decoding a Morse-code string hidden in the challenge output, and the final flag reads "bsides-roc-n-roll."

Beyond the CTF mechanics and its look, the maker's public pages do not disclose the badge's microcontroller, LED part numbers or count, price, production quantity, or whether hardware/firmware files were ever released, so those fields are left blank rather than guessed.
