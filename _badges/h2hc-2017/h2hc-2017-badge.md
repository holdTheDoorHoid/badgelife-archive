---
title: H2HC 2017 Badge
id: h2hc-2017-h2hc-2017-badge
layout: badge
parent: H2HC 2017
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: h2hc-2017
year: 2017
makers:
- name: Watterott Electronics
  url: https://www.watterott.com/
summary: A two-piece USB-stick badge for H2HC 2017 built around an ATtiny85, meant for USB HID keyboard-injector experiments and Micronucleus bootloader payload development.
functions: Plugs into a USB port as a bare ATtiny85 "USB stick"; runs Micronucleus-bootloader payloads programmed from the Arduino IDE (Digistump/DigiKeyboard workflow) to act as a USB HID keyboard injector. Holding the badge's reset button while inserting it into USB drops it into the bootloader for reflashing.
look:
  colors:
  - white
  shape: rectangle
  themes:
  - hardware tool
  - security
  - learn to solder
tech:
  mcu: ATtiny85
  leds:
    count: 1
    type: discrete
    note: single blue LED wired directly to VCC; lights whenever the stick is powered but is not software-controllable
  display: none
  connectivity:
  - usb
  battery: powered by host USB port
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed to H2HC 2017 attendees; exact distribution method not stated in sources.'
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/micronucleus/micronucleus
  eda_tool: null
  notes: 'The badge ships with the open-source Micronucleus bootloader (used for reflashing over USB), but no source says the badge''s own PCB/schematic files were published.'
links:
- label: badge.gallery/series/h2hc
  url: https://badge.gallery/series/h2hc
  kind: website
- label: 'security-bits.de: H2HC 2017 badge writeup'
  url: https://security-bits.de/electronics/badges/h2hc_17/
  kind: article
- label: Micronucleus bootloader (GitHub)
  url: https://github.com/micronucleus/micronucleus
  kind: repo
images:
- file: assets/images/badges/h2hc-2017/h2hc-2017-badge/dc6ba5e39a.jpg
  source: "https://security-bits.de/electronics/badges/h2hc_17/"
  credit: "security-bits.de (Brian)"
  caption: "H2HC 2017 badge, front (USB-stick PCB)"
- file: assets/images/badges/h2hc-2017/h2hc-2017-badge/d17ccec043.jpg
  source: "https://security-bits.de/electronics/badges/h2hc_17/"
  credit: "security-bits.de (Brian)"
  caption: "H2HC 2017 badge, back"
contact: {}
notes:
- 'Original sweep note: "ATtiny85-based USB HID injector conference badge for H2HC 2017." Confirmed and expanded by a maker/documentation writeup at security-bits.de.'
status: released
sources:
- kind: url
  url: https://badge.gallery/series/h2hc
  title: H2HC 2017 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''H2HC 2017''.'
- kind: url
  url: https://badge.gallery/badges/h2hc-2017-badge
  title: H2HC 2017 Badge - badge.gallery
  accessed: '2026-09-08'
  note: 'Manufacturer attribution (Watterott Electronics / Wattuino Nanite 85 design) and physical two-piece construction.'
- kind: url
  url: https://security-bits.de/electronics/badges/h2hc_17/
  title: 'H2HC 17 badge - security-bits.de'
  accessed: '2026-09-08'
  note: 'Primary writeup: ATtiny85 BitBang-USB HID injector, Micronucleus bootloader, single non-controllable blue LED, two-piece construction, PCB photos.'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: 'Core facts (ATtiny85, USB HID injector, Micronucleus bootloader, two-piece construction) confirmed by a third-party documentation site (security-bits.de) with detailed photos and schematics; no maker-first-party page (e.g. an H2HC or Watterott announcement) was found to corroborate manufacturer attribution independently, so confidence is medium rather than high. Price, quantity, and exact distribution method are not stated anywhere found. Whether the badge''s own hardware files (not just the third-party Micronucleus bootloader) were published is unknown.'
last_modified_date: '2026-09-08'
---

The H2HC 2017 badge is a bare USB-stick board built around an ATtiny85, handed out at Hackers to Hackers Conference (Brazil) in 2017. Rather than being worn, it plugs straight into a USB port; the two-piece design pairs a small microcontroller stick with a separate white baseplate that carries a lanyard loop and a pin-header adapter. A single blue LED lights whenever the stick draws power, but it is wired straight to VCC and can't be driven by code.

Functionally it's a workshop tool as much as a badge: the ATtiny85 ships with the open-source Micronucleus bootloader, so it can be reprogrammed over USB from the Arduino IDE using the Digistump/DigiKeyboard toolchain, no external programmer needed (hold the reset button while plugging it in to force bootloader mode). That makes it well suited to the badge's apparent intended use, USB HID keyboard-injection experiments, the same class of attack demonstrated by devices like the Rubber Ducky or HIDIOT.

Manufacture is attributed to Watterott Electronics, evidently based on their existing Wattuino Nanite 85 design, per a badge.gallery listing; the most detailed account of the hardware and its use comes from a third-party writeup on security-bits.de, which includes schematics and PCB photos but does not give pricing, production numbers, or how badges were distributed to attendees.
