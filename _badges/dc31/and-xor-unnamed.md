---
title: 5n4ck3y-7r (Snackey Jr)
id: dc31-and-xor-unnamed
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: AND!XOR
  url: https://andnxor.com/
summary: AND!XOR's DEF CON 31 badge, a screen-less RP2040 board built around the "5n4ck3y" (Snackey) badge-vending mascot and its cumulative CTFd hacking challenge.
functions: Doubles as a USB Rubber Ducky (Ducky 1.0 script subset) and a serial-terminal CTF ("B.E.N.D.E.R.") unlocked by hacker challenges on the 5n4ck3y CTFd site; two rear capacitive touch buttons trigger a default Ducky script; a "jiff" command plays ANSI static/animated art over serial.
look:
  colors: []
  shape: null
  themes:
  - ctf
  - puzzle
  - hardware tool
  - security
tech:
  mcu: RP2040 (Raspberry Pi Pico)
  leds:
    count: null
    type: RGB
    note: '"bling" command selects one of 6 LED modes (0-5); Ducky commands extended with LED_R/LED_G/LED_B/LED_OFF'
  display: none
  connectivity:
  - usb
  inputs:
  - touch
  battery: AAA batteries
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  distribution:
  - free_drop
  - contest
  where: Handed out by "5n4ck3y" in the DEF CON 31 Contest Area to people who solved enough challenges on the 5n4ck3y CTFd site (register, pass IRL physical verification, solve 2 challenges for an SAO or 3 for the badge); a batch also went out early to "Philanthropist" tier supporters starting 24 June 2023.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/ANDnXOR/ANDnXOR_DC31_Badge
  gerbers_url: null
  bom_url: null
  eda_tool: null
  license: MIT
  fab_url: null
  notes: GitHub repo is a "partial dump of source" (per the maintainers) covering the CircuitPython firmware, Ducky scripts, and ANSI art tools; no hardware design files (schematic/PCB/Gerbers) are published.
links:
- label: twitter.com/ANDnXOR
  url: https://twitter.com/ANDnXOR
  kind: social
  archived: https://web.archive.org/web/20260617181253/https://twitter.com/ANDnXOR
- label: 'GitHub: ANDnXOR/ANDnXOR_DC31_Badge'
  url: https://github.com/ANDnXOR/ANDnXOR_DC31_Badge
  kind: repo
- label: 5n4ck3y CTFd Challenge site
  url: https://5n4ck3y.ctfd.io/
  kind: doc
- label: AND!XOR Discord
  url: https://discord.gg/DeXNEydE2r
  kind: social
images: []
contact: {}
notes:
- SOLD OUT!!!!!
- Sheet title was "???"; badge is officially named 5n4ck3y-7r ("Snackey Jr") per the maker's own RTFM.md.
status: released
sources:
- kind: sheet
  event: dc31
  row: 4
  updated: '2023-06-25'
- kind: url
  url: https://github.com/ANDnXOR/ANDnXOR_DC31_Badge
  title: 'ANDnXOR/ANDnXOR_DC31_Badge: AND!XOR DC31 Badge'
  accessed: '2026-09-07'
  note: Repo README confirms scope (partial firmware source dump), MIT license, and CircuitPython/USB troubleshooting details.
- kind: url
  url: https://raw.githubusercontent.com/ANDnXOR/ANDnXOR_DC31_Badge/master/src/RTFM.MD
  title: RTFM.md - AND!XOR DC31 badge documentation
  accessed: '2026-09-07'
  note: Primary source for badge name (5n4ck3y-7r), hardware (RP2040, Winbond flash, PCA9615 I2C mux, TPS2114 power mux, laser-cut acrylic and pine), firmware (CircuitPython 8.0.5, B.E.N.D.E.R. CTF, Ducky, Bling/LED modes, jiff ANSI art), distribution/CTF mechanics, Philanthropist early-access note, and links.
- kind: url
  url: https://andnxor.com/
  title: AND!XOR
  accessed: '2026-09-07'
  note: Confirmed maker site is currently showcasing the DC30 badge; no DC31-specific storefront page found there.
  archived: https://web.archive.org/web/20260821062441/https://www.andnxor.com/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Chip, LEDs, power, distribution mechanism and firmware details all come from the maker''s own RTFM.md and GitHub repo, so those facts are solid. Could not confirm: exact LED count/part number, price, quantity made, PCB/case colors or shape, and could not find or save any photo of the physical badge (WebSearch budget was exhausted this session and X/Twitter, Reddit, and Nitter mirrors all blocked automated fetches; no image URL found on the maker''s GitHub or current storefront). The repo''s own referenced images (img/dc31_logo.png) were not present in the published tree. A future pass should look for photos via Hackaday.io comments, DEF CON forums, or a direct ask to AND!XOR.'
last_modified_date: '2026-09-07'
---

AND!XOR's 2023 DEF CON 31 badge is officially named **5n4ck3y-7r** ("Snackey Jr"), a screen-less badge built around an RP2040 (Raspberry Pi Pico) microcontroller, laser-cut acrylic and pine-wood construction, and AAA battery power. Rather than a display, it leans on RGB LED "bling" modes (six presets, 0-5) and doubles as a USB Rubber Ducky, playing back keystroke-injection scripts through a small subset of Hak5's Ducky language, extended by AND!XOR with LED control commands.

The badge is the physical half of a running CTF built around "5n4ck3y," AND!XOR's badge-vending mascot: a vending machine at DEF CON that hands out badges and SAOs to people who complete hacking challenges on a companion CTFd site (5n4ck3y.ctfd.io), starting with an in-person physical-verification step. Owning the badge unlocks a second layer of challenges, "B.E.N.D.E.R." (Badge Enabled Non Directive Enigma Routine), accessed over a serial terminal and activated with an emoji command sequence. A batch of badges also shipped early, ahead of the general contest-area drops, to backers who supported AND!XOR at the "Philanthropist" tier, with acquisition starting 24 June 2023.

Firmware (CircuitPython 8.0.5) and supporting tools are published on GitHub as a "partial dump" — the maintainers say more was meant to follow — including the Ducky scripts, an ANSI art viewer ("jiff"), and troubleshooting notes, under the MIT license. No hardware design files (schematics, PCB layout, Gerbers) have been published for this badge. As with prior AND!XOR badges, it was distributed free through contest participation rather than sold, and the community sheet marked it sold out.
