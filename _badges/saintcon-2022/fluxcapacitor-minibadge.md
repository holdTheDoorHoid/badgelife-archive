---
title: FluxCapacitor-Minibadge
id: saintcon-2022-fluxcapacitor-minibadge
layout: badge
parent: Saintcon 2022
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2022
year: 2022
makers:
- name: selftaught
  url: https://github.com/selftaught
summary: A SAINTCON 2022 minibadge shaped like the Back to the Future flux capacitor, with five LEDs that chase in sequence to mimic the movie prop's time-travel flash.
functions: Runs a fixed animation on power-up -- the five LEDs light in sequence with a ramping-then-steady speed, pause, and repeat, echoing the flux capacitor's flash from the film.
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - sci-fi
  - movie
tech:
  mcu: ATtiny85
  leds:
    count: 5
    type: discrete
    note: One center LED plus four others, each on its own ATtiny85 GPIO pin (no addressable driver).
  display: none
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
  open_source: 'yes'
  hardware_url: https://github.com/selftaught/FluxCapacitor-Minibadge/tree/main/kicad
  firmware_url: https://github.com/selftaught/FluxCapacitor-Minibadge/tree/main/src
  eda_tool: KiCad
links:
- label: github.com/selftaught/FluxCapacitor-Minibadge
  url: https://github.com/selftaught/FluxCapacitor-Minibadge
  kind: repo
images:
  - file: assets/images/badges/saintcon-2022/fluxcapacitor-minibadge/3eb51a5573.png
    source: "https://github.com/selftaught/FluxCapacitor-Minibadge"
    credit: "selftaught (Dillan Hildebrand)"
    caption: "3D render of the assembled Flux Capacitor minibadge PCB"
  - file: assets/images/badges/saintcon-2022/fluxcapacitor-minibadge/59d0f91dc8.jpg
    source: "https://github.com/selftaught/FluxCapacitor-Minibadge"
    credit: "selftaught (Dillan Hildebrand)"
    caption: "Assembled Flux Capacitor minibadge on a breadboard programmer"
contact: {}
notes: []
status: listed
sources:
- kind: url
  url: https://github.com/selftaught/FluxCapacitor-Minibadge
  title: FluxCapacitor-Minibadge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''SAINTCON 2022''.'
- kind: url
  url: https://github.com/selftaught/FluxCapacitor-Minibadge
  title: 'selftaught/FluxCapacitor-Minibadge: SaintCon 2022 Flux Capacitor Minibadge'
  accessed: '2026-09-07'
  note: 'Repo description, README, KiCad/Gerber files, and src/fluxcapacitor.c confirmed maker name (Dillan Hildebrand, GitHub handle selftaught), event/year, ATtiny85 MCU, 5-LED chase firmware, SAINTCON minibadge form factor (kicad/saintcon-minibadge.pretty footprints), and that hardware + firmware are both published (no explicit license file found).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    All facts here come from the maker's own GitHub repo (code comments, KiCad
    project, and images folder); no third-party coverage, storefront, or price/quantity
    information was found -- web search budget for this task ran out before a
    broader search could be attempted, so those fields are left empty rather than
    guessed. The repo's README has no body text beyond the title. The firmware
    source header credits "Dillan Hildebrand" as the author, dated 09/21/2022,
    which is presumably the maker behind the GitHub handle "selftaught". No
    LICENSE file is present in the repo despite both hardware and firmware being
    publicly readable, so make_your_own.license is left blank.
last_modified_date: '2026-09-07'
---

The Flux Capacitor Minibadge is a SAINTCON 2022 minibadge built around the movie prop from *Back to the Future*: three photodiode-style LED branches around a center LED, animated to flash and chase the way the film's time-travel effect does. It plugs into the SAINTCON minibadge connector standard (the KiCad project includes the SAINTCON-Minibadge and SAINTCON-Simple footprint library alongside the badge's own custom footprint).

Under the hood it's an ATtiny85 running simple Arduino-framework firmware: five LEDs, each wired to its own GPIO pin, are pulsed in sequence with a speed ramp before settling into a steady chase, then pause for three seconds and repeat. The project was designed in KiCad and programmed via a Bus Pirate over a breadboard header, and the maker has published the full KiCad source, Gerbers, and firmware on GitHub, crediting "Dillan Hildebrand" (GitHub handle selftaught) as the author.

No pricing, quantity, or distribution details were found in the source material -- the repo itself doesn't mention how or whether it was distributed at SAINTCON 2022, and no storefront or press coverage turned up in the research done for this entry.
