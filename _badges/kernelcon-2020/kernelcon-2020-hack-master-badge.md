---
title: Kernelcon 2020 Hack-Master Badge
id: kernelcon-2020-kernelcon-2020-hack-master-badge
layout: badge
parent: Kernelcon 2020
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: kernelcon-2020
year: 2020
makers:
- name: ZonkSec
  role: badge design (Tyler Rosonke)
- name: Aaron Gunning
  role: co-designer (scotchsec)
summary: A dual-PCB electronic badge built around a mechanical "image reel," styled after childhood vision toys, for the all-virtual Kernelcon 2020.
functions: 'Cycles through ten LED display modes via a button (fade, freeze, reel-only backlight, rave, looping animation, knight-rider, windmill, pseudorandom color, and twinkle), storing the current mode in EEPROM across power cycles. Originally included a serial-port CTF mini-game, which was removed when the conference moved online.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - kit
  - learn to solder
tech:
  mcu: ATmega328P
  leds:
    count: 9
    type: APA102
    note: Two of the nine LEDs serve as backlights for the mechanical image reel rather than general indicators.
  display: custom image reel (mechanical dual-PCB reel, backlit)
  connectivity: []
  battery: 3x AAA
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: partial
  hardware_url: https://github.com/ZonkSec/kernelcon-2020-badge
  firmware_url: https://github.com/ZonkSec/kernelcon-2020-badge
  eda_tool: null
links:
- label: badge.gallery/badges/kernelcon-2020-hack-master-badge
  url: https://badge.gallery/badges/kernelcon-2020-hack-master-badge
  kind: website
- label: github.com/ZonkSec/kernelcon-2020-badge
  url: https://github.com/ZonkSec/kernelcon-2020-badge
  kind: repo
- label: 'Kernelcon 2020 badge talk (YouTube)'
  url: https://youtu.be/VYY81450_RM
  kind: video
images:
- file: assets/images/badges/kernelcon-2020/kernelcon-2020-hack-master-badge/9d972a8899.jpg
  source: "https://github.com/ZonkSec/kernelcon-2020-badge"
  credit: "ZonkSec"
  caption: "Assembled Hack-Master badges"
- file: assets/images/badges/kernelcon-2020/kernelcon-2020-hack-master-badge/f5b5226423.jpg
  source: "https://github.com/ZonkSec/kernelcon-2020-badge"
  credit: "ZonkSec"
  caption: "The custom image reel used by the badge's mechanical display"
contact: {}
notes:
- ATmega328P dual-PCB image-reel badge themed on a childhood toy, with a soldering-based CTF. Found by the event-year sweep, task con-kernelcon.
- 'The sweep''s title matched the maker''s own naming exactly; no correction needed.'
status: listed
sources:
- kind: url
  url: https://badge.gallery/badges/kernelcon-2020-hack-master-badge
  title: Kernelcon 2020 Hack-Master Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kernelcon); event read as ''Kernelcon 2020''.'
- kind: url
  url: https://github.com/ZonkSec/kernelcon-2020-badge
  title: 'ZonkSec/kernelcon-2020-badge'
  accessed: '2026-09-08'
  note: 'Maker repo: confirmed ATmega328P, APA102 LEDs, image-reel mechanism, display modes, EEPROM mode persistence, 3xAAA power, and that the CTF serial game was cut for the virtual event. Also names co-designer Aaron Gunning (scotchsec) and links a conference talk.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Price, quantity, and availability are not stated anywhere in the repo or the gallery page, so those fields are left empty. No storefront or sale listing was found. open_source is set to "partial" because the repo contains hardware documentation and production notes but no explicit firmware source file or license was located in the fetched content. look.colors and look.shape were not stated by any source and are left empty.'
last_modified_date: '2026-09-08'
---

The Hack-Master Badge was Kernelcon 2020's attendee badge, built around an ATmega328P microcontroller and nine APA102 addressable LEDs, two of which backlight a mechanical "image reel" — a rotating dual-PCB display styled after childhood vision-reel toys. A front-panel button cycles through ten LED modes (fade, freeze, reel-only, rave, looping animation, knight-rider, windmill, pseudorandom color, and twinkle), with the active mode saved to EEPROM so it survives a power cycle. The badge runs on three AAA batteries and was designed by Tyler Rosonke (ZonkSec), Kernelcon's badge chair, with Aaron Gunning (scotchsec).

Kernelcon 2020 was forced online by the onset of the COVID-19 pandemic (the event ran virtually March 25-28, 2020), and the badge's original serial-port CTF mini-game was cut as a result, since it depended on in-person badge-to-badge interaction. Assembly used ICSP pogo-pin programming with a clothespin-clamp jig, documented in the project's GitHub repository alongside build notes.

## Make your own

Hardware documentation and production notes are published at github.com/ZonkSec/kernelcon-2020-badge, including the pogo-pin ICSP programming setup used to flash the ATmega328P. No explicit open hardware license or bill of materials was located in the fetched repository content, so treat any reproduction as best-effort from the maker's notes rather than a turnkey build.
