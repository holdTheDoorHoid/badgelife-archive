---
title: 2022 SuperCon Badge USB Programing Add-On
id: supercon-2022-supercon-2022-badge-programming-adapter
layout: badge
parent: Supercon 2022
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2022
year: 2022
makers:
- name: brokebit
summary: An open-source expansion board for the 2022 Supercon badge that adds USB programming plus buttons and LEDs for interacting with the badge's I/O pins.
functions: Uploads and downloads programs to the badge over USB, and lets the wearer drive the badge's I/O pins via four buttons and read them via four LEDs. Passes all header pins through so other add-ons can be daisy-chained behind it. DIP switches let the buttons, LEDs, or USB UART each be disabled independently.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: none
  leds:
    count: 4
    type: discrete
    note: One LED per output I/O pin.
  display: none
  connectivity:
  - usb
  - uart
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
  open_source: yes
  hardware_url: https://github.com/brokebit/2022-SuperCon-Badge-Programing-Addon
  firmware_url: null
  eda_tool: KiCad
links:
- label: github.com/brokebit/2022-SuperCon-Badge-Programing-Addon
  url: https://github.com/brokebit/2022-SuperCon-Badge-Programing-Addon
  kind: repo
images:
  - file: assets/images/badges/supercon-2022/supercon-2022-badge-programming-adapter/538081602b.png
    source: "https://github.com/brokebit/2022-SuperCon-Badge-Programing-Addon"
    credit: "brokebit"
    caption: "PCB rendering of the programming add-on board"
  - file: assets/images/badges/supercon-2022/supercon-2022-badge-programming-adapter/e3e15906f3.jpg
    source: "https://github.com/brokebit/2022-SuperCon-Badge-Programing-Addon"
    credit: "brokebit"
    caption: "The add-on board plugged into the 2022 Supercon badge"
contact: {}
notes:
- 'The sweep''s wording was "Supercon 2022 Badge Programming Adapter"; the maker''s repo and README title it "2022 SuperCon Badge USB Programing Add-On" (note the maker''s own spelling "Programing"), which this entry now uses.'
- No price, quantity, or distribution info was found; this appears to be a personal open-source design shared on GitHub rather than something sold, so get_one fields are left empty.
- The sweep's notes mentioned "ten DIP switches" and Hackaday coverage; the README only documents one 4-position and one 2-position DIP switch (6 positions total, used to disable buttons/LEDs/USB independently), and no Hackaday article was found or checked, so that claim was dropped rather than repeated unverified.
status: released
sources:
- kind: url
  url: https://github.com/brokebit/2022-SuperCon-Badge-Programing-Addon
  title: Supercon 2022 Badge Programming Adapter
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2022); event read as ''supercon-2022''.'
- kind: url
  url: https://raw.githubusercontent.com/brokebit/2022-SuperCon-Badge-Programing-Addon/main/README.md
  title: '2022 SuperCon Badge USB Programing Add On Module (README)'
  accessed: '2026-09-08'
  note: Maker's README confirming features (4 buttons, 4 LEDs, CP210x USB UART, DIP-switch disables, passthrough header), 6-layer KiCad PCB, and links to schematic/BOM/gerbers.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Core facts confirmed directly from the maker's GitHub repo and README. No price, quantity, or sale/distribution info exists because this is a shared open-source design rather than a sold item; availability left unknown. Could not confirm the sweep's claim of Hackaday coverage.
last_modified_date: '2026-09-08'
---

The 2022 SuperCon Badge USB Programing Add-On is an open-source expansion board made by brokebit for that year's Hackaday Supercon badge. It plugs into the badge's header and gives the wearer a USB path for uploading and downloading programs, using a CP210x USB-to-UART chip, without needing a separate programmer. It also breaks out four of the badge's I/O pins to four momentary buttons and four LEDs, so those pins can be driven or read by hand, and it passes all header pins straight through so further add-ons can be stacked behind it. Two onboard DIP switch banks (a 4-position and a 2-position switch) let the buttons, LEDs, and USB UART circuitry each be disabled independently when not wanted.

The board is a 6-layer design done in KiCad, with surface-mount parts sourced for JLCPCB assembly and through-hole parts (headers, DIP switches, buttons) from Digikey. The 5V USB supply powers only the USB-UART circuitry, not the rest of the board.

## Make your own

The maker published the full manufacturing package on GitHub: schematic PDF, a BOM spreadsheet, a component position file, and Gerber files, all sized for direct submission to a PCB manufacturer such as JLCPCB. No firmware is involved — the board is a passive I/O breakout and USB-UART bridge, not a programmed device.
