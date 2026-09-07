---
title: 30-in-One Badge
id: dc30-30-in-1-badge
layout: badge
parent: DC30
grand_parent: Badge Archive
nav_exclude: true
type: kit
event: dc30
year: 2022
makers:
- name: DCZia
  url: https://dczia.net
summary: A "learn electronics" kit on a single PCB, built and sold as a wearable badge for DEF CON 30.
functions: 'End users solder up to 30 different described circuits onto one board (OLED display, RGB LED, speaker, switches, potentiometer, transformer), using it as a jumping-off point to explore analog electronics; the board includes hidden challenges/puzzles and ships with a printed instruction booklet and a wooden box that doubles as a soldering jig.'
look:
  colors: []
  shape: rectangle
  themes: [learn to solder, kit, electronics]
tech:
  mcu: none
  leds:
    count: 1
    type: RGB
    note: Single RGB LED among the 30 circuits; no microcontroller is used (a passive/analog electronics kit).
  display: 0.96" OLED
  connectivity: []
  battery: not specified (has a battery case)
  sao_version: none
get_one:
  price: $100
  price_usd: 100.0
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing shows "Out of Stock" as of 2026-09-06.
  distribution: [purchase]
  where: Sold via Tindie (seller "hamster" / snurkle engineering, Sandy, UT).
make_your_own:
  open_source: yes
  hardware_url: https://github.com/dczia/thirtyinone
  firmware_url: null
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: Unlicense
  fab_url: null
  notes: OSHWA certified (UID US002134, certified 2022-11-08). Repo includes Hardware and Software folders plus the printed booklet (PDF and source).
links:
- label: www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge
  url: https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/
  kind: store
- label: dczia/thirtyinone (GitHub)
  url: https://github.com/dczia/thirtyinone
  kind: repo
- label: OSHWA certification US002134
  url: https://certification.oshwa.org/us002134.html
  kind: doc
- label: DCZia
  url: https://dczia.net
  kind: website
- label: "DCZia 30 in 1 Electronic Project Kit Badge Overview (YouTube)"
  url: https://www.youtube.com/watch?v=AAD9OO9EeQw
  kind: video
images:
- file: assets/images/badges/dc30/30-in-1-badge/1679846ba4.jpg
  source: "https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/"
  credit: "DCZia / snurkle engineering"
  caption: "The assembled 30-in-One badge PCB with through-hole components"
contact:
  email: contact@dczia.net
notes:
- Blast from the past
status: released
sources:
- kind: sheet
  event: dc30
  row: 11
  updated: '2022-08-04'
- kind: url
  url: https://www.tindie.com/products/hamster/dczia-30-in-one-defcon-30-badge/
  title: DCZia '30-in-One' defcon 30 Badge - Tindie
  accessed: '2026-09-06'
  note: Price, seller (snurkle engineering), features, out-of-stock status, product photo, OSHW mention.
- kind: url
  url: https://certification.oshwa.org/us002134.html
  title: OSHWA Certification US002134 - DCZia 30-in-One Badge
  accessed: '2026-09-06'
  note: Confirms maker name "DCZia", certification date, project description, keywords, and links to GitHub repo and contact email.
- kind: url
  url: https://github.com/dczia/thirtyinone
  title: dczia/thirtyinone - GitHub
  accessed: '2026-09-06'
  note: Repo contents (Hardware/Software folders, booklet PDF), Unlicense, README assembly order listing components (OLED, RGB LED, speaker, switches, battery case, transformer, potentiometer, key cap).
- kind: url
  url: https://dczia.net
  title: DCZia
  accessed: '2026-09-06'
  note: Confirms DCZia as an ongoing badge-making group ("Fueled by Solder & Green Chile"), consistent with their other-year entries in this archive.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-06'
  notes: The community sheet listed the maker as "DCZIA YOLO Badge"; the maker's own name (per Tindie, OSHWA, and GitHub) is "DCZia", sold through Tindie seller "snurkle engineering". No microcontroller is used in this kit - it is a passive/analog electronics teaching board with one RGB LED, an OLED display, a speaker, and other discrete components. Quantity made and battery type/spec are not stated in any source found; left empty/generic accordingly. Retitled from "30-in-1 Badge" to "30-in-One Badge" to match the maker's own naming (Tindie listing, OSHWA record, and GitHub repo all use "30-in-One").
last_modified_date: '2026-09-06'
---

The 30-in-One Badge is a "learn electronics" kit built by DCZia and sold as a badge for DEF CON 30 (2022) through Tindie under seller "snurkle engineering." Rather than running firmware on a microcontroller, it is a single PCB carrying 30 separate analog circuit projects — an OLED screen, an RGB LED, a speaker, switches, a potentiometer, and a transformer among them — that the owner solders together themselves, following a printed instruction booklet. A wooden box doubles as a soldering jig, and the board reportedly hides some challenges/puzzles for people who go looking. It sold for $100 and has since gone out of stock on Tindie.

The project is OSHWA-certified (UID US002134, certified November 2022) and fully open source under the Unlicense, with hardware and software design files, the booklet, and its source available in DCZia's `thirtyinone` GitHub repository. DCZia continued making badges in subsequent years (their DC31, DC32, and DC33 entries are also in this archive), and maintains an ongoing project site at dczia.net.
