---
title: DarkNet DEF CON 24 Badge
id: dc24-dc-darknet-def-con-24-badge
layout: badge
parent: DC24
grand_parent: Badge Archive
nav_exclude: true
type: badge
series: DarkNet
event: dc24
year: 2016
makers:
- name: Krux
  url: https://krux.org/
  role: hardware design
- name: Smitty
  role: firmware
- name: CmdC0dez
  role: firmware
summary: The 2016 DEF CON DarkNet badge kit, a two-board electronic build built around an STM32F103 "blue pill" module. It doubles as a learn-to-solder kit and the physical key to the DarkNet contest's alternate-reality-game puzzles.
functions: 'Runs the DarkNet contest: pairs with other agents'' badges over infrared and a longer-range HopeRF radio link, displays contest text and clues on a small OLED, and is entered via a 13-key T9-style keypad. The badge carries encoded puzzle text (one-time pad and Caesar-shift ciphers) that feeds into the DarkNet casefile/ARG.'
look:
  colors:
  - purple
  - gold
  shape: null
  themes:
  - puzzle
  - ctf
  - security
  - radio
tech:
  mcu: STM32F103
  leds:
    count: 2
    type: discrete
    note: one 5mm green status LED and one 5mm IR LED for infrared transmission; shield board also carries backlight LEDs that light up printed letters
  display: 0.96" OLED
  connectivity:
  - ir
  - uart
  battery: 3x AAA (with reverse-polarity protection diode bridge)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Distributed through the DEF CON DarkNet table/contest at DEF CON 24 (2016); people who solved the pre-con "casefile" challenge could buy in before general sale. Firmware was pre-loaded at the DarkNet table.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/thedarknet/defcon24
  firmware_url: https://github.com/thedarknet/defcon24
  eda_tool: Eagle
links:
- label: github.com/thedarknet/defcon24
  url: https://github.com/thedarknet/defcon24
  kind: repo
- label: DarkNet 2016 Badge Kit (krux.org)
  url: https://krux.org/darknet/2016/index.html
  kind: doc
- label: Darknet Badge Kits created.... (DEF CON Forums)
  url: https://forum.defcon.org/node/221577
  kind: social
images:
- file: assets/images/badges/dc24/dc-darknet-def-con-24-badge/e9fb162487.jpg
  source: https://krux.org/darknet/2016/index.html
  credit: Krux
  caption: 'Full DarkNet DC24 kit of parts: main and shield PCBs, STM32F103 blue pill, HopeRF radio module, OLED, keypad switches, LEDs, and AAA batteries'
- file: assets/images/badges/dc24/dc-darknet-def-con-24-badge/f15146bb37.jpg
  source: https://krux.org/darknet/2016/index.html
  credit: Krux
  caption: Assembled DarkNet DC24 main PCB in OSH Park purple, held during kit assembly
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
status: released
sources:
- kind: url
  url: https://github.com/thedarknet/defcon24
  title: DC Darknet DEF CON 24 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc24''.'
- kind: url
  url: https://krux.org/darknet/2016/index.html
  title: DarkNet 2016 Badge Kit
  accessed: '2026-09-07'
  note: Maker (Krux) assembly-instructions page; source for MCU, LEDs, display, keypad, radio, battery, colors, and distribution details.
- kind: url
  url: https://forum.defcon.org/node/221577
  title: Darknet Badge Kits created....
  accessed: '2026-09-07'
  note: DEF CON forum post confirming the kits were physically assembled and awaiting attendee soldering; used only for confirmation, page required no login for the og:description snippet.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Core specs (MCU, display, radio, battery, distribution) come from Krux''s own DarkNet 2016 build-instructions page, which is the maker''s own documentation. Price and quantity produced were not stated on any source found and are left empty. The GitHub repo (thedarknet/defcon24) contains Eagle schematics and firmware in a Badge/ directory plus a BadgeGen key-generation tool, but no README with specs, so hardware_url/firmware_url point to the repo generally rather than specific files. Series is "DarkNet" per the recurring DEF CON DarkNet badge line (later years: defcon25-badge, Darknet-NG).'
last_modified_date: '2026-09-07'
model:
  file: assets/models/dc24/dc-darknet-def-con-24-badge.glb
  method: kicad
  source_file: DC24-Darknet_Badge.brd
  generated: '2026-09-07'
  bytes: 275420
---

The DarkNet badge was the physical centerpiece of DEF CON DarkNet, a long-running alternate-reality-game contest at DEF CON. The 2016 (DEF CON 24) edition was a two-PCB kit — a purple OSH Park-fabricated main board and a shield board — built around an STM32F103 "blue pill" module, with hardware designed by Krux and firmware by Smitty and CmdC0dez. Attendees assembled it themselves as a soldering exercise, wiring up a 0.96" OLED display, a 13-switch T9-style keypad, a green status LED, an IR LED and receiver for short-range badge-to-badge communication, and a HopeRF RFM69HCW-915S2 radio module for longer-range links, all powered by three AAA batteries.

Functionally, the badge doubled as the key to the DarkNet casefile: it carried encoded text (one-time-pad and Caesar-shift ciphers) that fed into the contest's puzzle chain, and pairing badges over IR or radio was part of solving it. Access followed the DarkNet contest's usual pattern — solving a pre-conference online "casefile" earned early purchase access to the kit at the DarkNet table before it went on sale to the wider con.

The hardware (Eagle schematics) and firmware live in the `thedarknet/defcon24` GitHub repository alongside a `BadgeGen` utility for generating the badges' cryptographic key pairs and radio IDs, though the repo carries no README summarizing specs, price, or production numbers, so those fields could not be confirmed from any source found.
