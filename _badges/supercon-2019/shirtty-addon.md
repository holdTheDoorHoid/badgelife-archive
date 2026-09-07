---
title: shIRtty addon
id: supercon-2019-shirtty-addon
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2019
year: 2019
makers:
- name: Thomas Sarlandie
  url: https://hackaday.io/sarfata
summary: A CircuitPython-compatible "Shitty Addon" for the Supercon 2019 badge that sends and receives infrared signals and carries an RGB LED.
functions: Sends and receives infrared (IR) signals; RGB LED for status/light effects; exposes GPIOs; usable with CircuitPython.
look:
  colors: []
  shape: rectangle
  themes:
  - hardware tool
  - radio
tech:
  mcu: SAMD21E18A
  leds:
    count: 1
    type: RGB
    note: Single RGB LED used for status/light effects; firmware notes mention configuring it to work with the board's specific RGB LED.
  display: none
  connectivity:
  - ir
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/sarfata/shirtty-addon/tree/master/hardware
  firmware_url: https://github.com/sarfata/shirtty-addon/tree/master/firmware
  eda_tool: KiCad
  notes: 'Repo also includes a "shitty-inverser" accessory board to correct a v1 wiring flaw (see notes below), plus bootloader and CircuitPython build instructions and logo assets. No license file is present in the repository.'
links:
- label: hackaday.io/project/168421-shirtty-addon
  url: https://hackaday.io/project/168421-shirtty-addon
  kind: hackaday
- label: github.com/sarfata/shirtty-addon
  url: https://github.com/sarfata/shirtty-addon
  kind: repo
images:
- file: assets/images/badges/supercon-2019/shirtty-addon/c675883d10.jpg
  source: "https://github.com/sarfata/shirtty-addon"
  credit: "Thomas Sarlandie"
  caption: "shIRtty addon board"
- file: assets/images/badges/supercon-2019/shirtty-addon/af232503d2.jpg
  source: "https://github.com/sarfata/shirtty-addon"
  credit: "Thomas Sarlandie"
  caption: "shIRtty addon plugged into Supercon 2019 badge"
contact: {}
notes:
- IR send/receive SAO for Supercon 2019 badge.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/168421-shirtty-addon
  title: shIRtty addon
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-search); event read as ''Supercon 2019''.'
- kind: url
  url: https://hackaday.io/project/168421-shirtty-addon
  title: shIRtty addon | Hackaday.io
  accessed: '2026-09-07'
  note: Confirmed maker (Thomas Sarlandie, hackaday.io/sarfata), project description ("A Shitty Addon (tm) for the Supercon 2019 badge that adds the ability to send and receive infrared signals"), created Nov 12, 2019. No usable hardware photo on this page (og:image is a generic placeholder) and no files attached to the Hackaday.io project itself.
- kind: url
  url: https://github.com/sarfata/shirtty-addon
  title: sarfata/shirtty-addon
  accessed: '2026-09-07'
  note: 'Maker''s GitHub repo. README describes it as "A CircuitPython compatible, SAMD21 shitty addon with IR transmit/receive and RGB LED", MCU SAMD21E18A, SAO connector. Lists known v1 hardware issues (SAO header wired upside down needing a "shitty inverser", insufficient 3V-line capacitance causing brownout on IR transmit, unreliable PCB USB connector, reset button too large to fit the SMD SAO connector). Hardware directory uses KiCad (shirtty.kicad_pcb, fp-lib-table). Repo has no license file/field. Source photos: photo.jpeg, photo-2.jpeg, photo-3.jpeg, pinout.png.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Maker''s own Hackaday.io project and GitHub repo confirm what the addon is, who made it, the event, the MCU, and that hardware/firmware are open source. Price, quantity made, and availability are not stated anywhere found and are left empty. No third-party coverage (press, forum threads) was found beyond the maker''s own pages. Status set to "released" on the basis that the project shipped hardware (photos of an assembled board plugged into a badge exist) rather than remaining a plan.'
last_modified_date: '2026-09-07'
---

The shIRtty addon is a "Shitty Addon" (SAO) built for the Supercon 2019 badge by Thomas Sarlandie. It is built around a SAMD21E18A microcontroller (ARM Cortex-M0+), runs CircuitPython, and adds infrared transmit/receive to the host badge along with a single RGB LED. The board plugs into the badge's SAO header and draws its power from the host badge.

The maker's GitHub README is candid about the addon's rough edges as a "shitty" project: the SAO header on the first version is wired upside down (the repo includes a small "shitty inverser" board, or the addon can simply be plugged in upside down), the 3V rail lacks enough capacitance and can brown out while transmitting IR, the PCB-mount USB connector is unreliable, and the reset button is sized too large to coexist with the SMD SAO connector. Hardware design files (KiCad) and firmware source are published in the repository, along with build notes for a UF2 bootloader and instructions for programming via a Black Magic Probe.

No pricing, production quantity, or distribution details were found on either the Hackaday.io project page or the GitHub repository, so those fields are left empty.
