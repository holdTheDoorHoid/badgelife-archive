---
title: TrevorForget
id: other-trevorforget
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2018
makers:
- name: hamster
  role: PCB/hardware design
- name: AND!XOR
  role: firmware (2018 and 2019 revisions)
summary: A memorial PCB badge made for the DerbyCon community in honor of a member named Trevor, who died September 23, 2017. It carries a cartoon cockroach mascot and the hashtag #trevorforget.
functions: ''
look:
  colors:
  - black
  - gold
  - white
  shape: rectangle
  themes:
  - mascot
  - animal
tech:
  mcu: 'ATtiny816 (2018 revision); ATtiny3217 (2019 revision)'
  leds: null
  display: null
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
  hardware_url: https://github.com/hamster/trevorforget
  firmware_url: https://github.com/ANDnXOR/trevorforget
  eda_tool: KiCad
links:
- label: github.com/ANDnXOR/trevorforget
  url: https://github.com/ANDnXOR/trevorforget
  kind: repo
- label: github.com/hamster/trevorforget
  url: https://github.com/hamster/trevorforget
  kind: repo
images:
  - file: assets/images/badges/other/trevorforget/f7fe29952b.jpg
    source: "https://github.com/hamster/trevorforget"
    credit: "hamster"
    caption: "TrevorForget PCB badge, front"
  - file: assets/images/badges/other/trevorforget/f9d3c40906.jpg
    source: "https://github.com/hamster/trevorforget"
    credit: "hamster"
    caption: "TrevorForget PCB badge, back"
contact: {}
notes:
- 'From the user''s ''SAOs to buy'' link list (2026-09-07). Mirror: https://github.com/hamster/trevorforget'
status: released
sources:
- kind: url
  url: https://github.com/ANDnXOR/trevorforget
  title: TrevorForget
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''other''.'
- kind: url
  url: https://github.com/hamster/trevorforget
  title: trevorforget (hamster/trevorforget)
  accessed: '2026-09-07'
  note: 'Original hardware repo. README states the board was made for @grifter801 by @hamster for @derbycon, with front/back renders showing "R.I.P. 9/23/17" and credits to @derbycon, @Grifter801, and @hamster. KiCad source and Gerbers included; license text asks makers not to sell for profit.'
- kind: url
  url: https://raw.githubusercontent.com/ANDnXOR/trevorforget/master/README.md
  title: 'ANDnXOR/trevorforget README'
  accessed: '2026-09-07'
  note: 'Confirms two firmware revisions: ATtiny816 for 2018, ATtiny3217 for 2019, flashed via Atmel Ice/UPDI (2019 adds a Tag Connect 2050 pogo-pin adapter).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Made for DerbyCon (no DerbyCon entry exists in _data/events.yml, so event is left as "other"; the con and approximate year are DerbyCon, 2018-2019). Two related repos exist: hamster/trevorforget (original 2018 KiCad hardware, per its README made "for @grifter801 by @hamster for @derbycon") and ANDnXOR/trevorforget (firmware only, covering a 2018 ATtiny816 build and a 2019 ATtiny3217 revision). Neither repo documents what the firmware actually does, so functions is left empty. The back-of-board render shows a coin-shaped footprint, a single LED/diode symbol, and pads for a small MCU, consistent with a simple blinking memorial badge, but no source spells out the LED count/type or battery type, so tech.leds and tech.battery are left null rather than guessed. Price, quantity made, and how it was distributed are not stated anywhere found; get_one fields are left empty/unknown. No image could be confirmed as an in-hand photo — both saved images are CAD/rendering-tool screenshots of the PCB design from the hamster/trevorforget repo, which is the best material available.'
last_modified_date: '2026-09-07'
---

TrevorForget is a memorial PCB badge made for the DerbyCon community. According to the original hardware repository (github.com/hamster/trevorforget), the boards were "made for @grifter801 by @hamster for @derbycon," and the board itself is marked "R.I.P. 9/23/17" on the back along with the handles @derbycon, @Grifter801, and @hamster — indicating it commemorates a community member named Trevor who died on that date. The front carries a cartoon cockroach mascot in a bowler hat holding a drink cup, with the hashtag #TREVORFORGET printed below it. The hardware design (KiCad source and Gerbers) was released by hamster with the requests "please don't sell these for profit" and "let us know if you are using them."

A separate repository from AND!XOR (github.com/ANDnXOR/trevorforget) hosts firmware for the badge across two builds: a 2018 version targeting the ATtiny816 and a 2019 revision moved to the ATtiny3217, the latter using a Tag Connect 2050 pogo-pin adapter to reach the chip's UPDI programming pins instead of a soldered header. Neither repository documents what the firmware actually makes the badge do, so its on-board behavior (beyond likely lighting the single LED visible in the PCB render) is not confirmed by any source found.

## Make your own

Hardware: KiCad schematic, PCB layout, and Gerber files are in github.com/hamster/trevorforget (custom footprint library `trevor.pretty` included). Firmware: github.com/ANDnXOR/trevorforget, organized into `2018` and `2019` folders; building requires Atmel Studio (set the target to ATtiny816 for the 2018 version or ATtiny3217 for 2019), and flashing needs an Atmel-ICE for the proprietary UPDI protocol (the maintainers note the open-source `pyupdi` tool also worked for them once).
