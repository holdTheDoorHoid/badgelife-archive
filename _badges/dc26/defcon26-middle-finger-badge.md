---
title: The DEFCON26 Middle Finger Badge
id: dc26-defcon26-middle-finger-badge
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc26
year: 2018
makers:
- name: El Jefe de Security
  url: https://hackaday.io/hacker/168331-el-jefe
summary: A DIY soldering-kit badge for DEF CON 26 shaped as a raised middle finger aimed at facial-recognition cameras, built around an Adafruit Trinket M0 driving three 5mm through-hole NeoPixels, with a LiPo backpack shim, breakout pins for sensors, and a DC26 Shitty Add-On connector; sold in white/silver, red/blue and black/gold variants and programmed in CircuitPython.
functions: Programmable RGB LED patterns via CircuitPython; doubles as a soldering/electronics learning kit (LED control and I2C via the SAO connector).
look:
  colors: [white, silver, red, blue, black, gold]
  shape: other
  themes: [meme, pop culture, learn to solder, security, privacy]
tech:
  mcu: Adafruit Trinket M0
  leds:
    count: 3
    type: NeoPixel (5mm through-hole)
    note: Addressable RGB, user-programmable in CircuitPython
  display: none
  connectivity: [i2c]
  battery: LiPo (connector only; battery not included)
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ~300 boards
  availability: sold_out
  availability_note: "Tindie listing checked 2026-09-07: marked retired/sold out; maker noted taking a break."
  distribution: [preorder, purchase, kit]
  where: Sold as a DIY solder kit via Tindie during DEF CON 26 in white/silver, red/blue, and black/gold color variants; all variants sold out.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/ElJefeDSecurIT/DC26fingerbadge
  firmware_url: https://github.com/ElJefeDSecurIT/DC26fingerbadge
  eda_tool: Eagle
links:
- label: hackaday.io/project/160078-the-defcon26-middle-finger-badge
  url: https://hackaday.io/project/160078-the-defcon26-middle-finger-badge
  kind: hackaday
- label: github.com/ElJefeDSecurIT/DC26fingerbadge
  url: https://github.com/ElJefeDSecurIT/DC26fingerbadge
  kind: repo
- label: www.tindie.com/products/336c6614/defcon-26-middle-finger-badge-diy-kit
  url: https://www.tindie.com/products/336c6614/defcon-26-middle-finger-badge-diy-kit/
  kind: store
images:
- file: assets/images/badges/dc26/defcon26-middle-finger-badge/508a0e0a33.jpg
  source: "https://hackaday.io/project/160078-the-defcon26-middle-finger-badge"
  credit: "El Jefe"
  caption: "Assembled DEFCON26 Middle Finger Badge"
- file: assets/images/badges/dc26/defcon26-middle-finger-badge/c2f8b9ad1c.jpg
  source: "https://hackaday.io/project/160078-the-defcon26-middle-finger-badge"
  credit: "El Jefe"
  caption: "DEFCON26 Middle Finger Badge PCB detail"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/160078-the-defcon26-middle-finger-badge
  title: The DEFCON26 Middle Finger Badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/160078-the-defcon26-middle-finger-badge
  title: The DEFCON26 Middle Finger Badge (Hackaday.io project page)
  accessed: '2026-09-07'
  note: "Confirmed maker's stated purpose (satire of facial-recognition surveillance), chip (Trinket M0), LEDs (3 NeoPixels), design files (schematic/board), and creation date (July 30, 2018). Maker said they were 'out of pocket for ~300 boards' and 'not making anything on this.'"
- kind: url
  url: https://github.com/ElJefeDSecurIT/DC26fingerbadge
  title: ElJefeDSecurIT/DC26fingerbadge (GitHub)
  accessed: '2026-09-07'
  note: Confirmed hardware (Eagle schematics/PCB) and CircuitPython firmware are published in the repo; license file present but type not confirmed.
- kind: url
  url: https://www.tindie.com/products/336c6614/defcon-26-middle-finger-badge-diy-kit/
  title: DEFCON 26 Middle Finger Badge DIY Kit (Tindie)
  accessed: '2026-09-07'
  note: "Confirmed kit contents (Trinket M0 pre-loaded with CircuitPython, 3 NeoPixels, LiPo backpack shim board, no battery), the three color variants, and that the listing is now retired/sold out."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: "Maker's own Hackaday.io project, GitHub repo, and Tindie listing all agree on the core facts. Exact retail price was not found on any surviving page (Tindie listing shows only shipping fees, $3.50 first kit + $1.50/additional, U.S. only); left get_one.price empty rather than guess. License type in the GitHub repo's LICENSE file was not confirmed. Quantity (~300 boards) is the maker's own approximate figure from the project page, not an exact count."
last_modified_date: '2026-09-07'
---

The DEFCON26 Middle Finger Badge is a DIY soldering kit sold by El Jefe de Security for DEF CON 26 in 2018. Shaped as an upraised middle finger, the badge was conceived as a pointed, tongue-in-cheek gesture toward facial-recognition cameras and the broader surveillance state — a piece of wearable protest as much as electronics. It is built around an Adafruit Trinket M0 preloaded with CircuitPython, driving three 5mm through-hole NeoPixels that owners can reprogram for their own color patterns, plus a small LiPo backpack shim board and breakout pins for add-on sensors. A DC26 Shitty Add-On (SAO) connector lets it talk I2C to a host badge.

The kit was sold through Tindie in three color schemes — white/silver, red/blue, and black/gold — with the maker stating on the project page that they were personally out roughly 300 boards' worth of cost and were "not making anything on this," framing it as a community give-back rather than a business. All variants are now listed as sold out, and the Tindie shop itself shows as retired.

Both the hardware (Eagle schematic and board files) and the CircuitPython firmware are published on GitHub, making the badge fully reproducible by anyone willing to source and solder the parts themselves.

## Make your own

Hardware (Eagle `.sch`/`.brd`) and CircuitPython firmware are both published at https://github.com/ElJefeDSecurIT/DC26fingerbadge, in the `The_Finger_Board` and `_CircuitPython` folders respectively. The repo notes documentation was still being filled in, so treat it as a reference design rather than a fully written build guide.
