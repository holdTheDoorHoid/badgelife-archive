---
title: TiLDA Mk4
id: emf-camp-2018-tilda-mk4-mk
layout: badge
parent: EMF Camp 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: emf-camp-2018
year: 2018
makers:
- name: EMF Camp badge team
summary: 'The official EMF Camp 2018 badge: a fully-hackable, MicroPython-programmable mobile phone with a SIM800 GSM modem for calls and texts on the on-site network.'
functions: 'Phone calls and SMS via the on-site GSM network or a Hologram IoT SIM; MicroPython app store; Wi-Fi; sensors (humidity, dual temperature, ambient light, Hall effect); Neopixel lighting.'
look:
  colors: []
  shape: null
  themes:
  - retro computer
  - radio
  - hardware tool
tech:
  mcu: TI MSP432E401Y (ARM Cortex-M4F @ 120MHz)
  leds:
    count: 2
    type: WS2812B
    note: plus a 3-pin expansion header for more
  display: 240x320 RGB LCD
  connectivity:
  - wifi
  - bluetooth
  battery: 2000mAh
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: 'Given to EMF Camp 2018 attendees as the event badge.'
make_your_own:
  open_source: yes
  hardware_url: null
  firmware_url: https://github.com/emfcamp/TiLDA-MK4
  eda_tool: null
links:
- label: badge.emfcamp.org/TiLDA_MK4
  url: https://badge.emfcamp.org/TiLDA_MK4/
  kind: website
- label: blog.emfcamp.org/2018/08/26/tilda-mk4-the-emf-2018-badge
  url: https://blog.emfcamp.org/2018/08/26/tilda-mk4-the-emf-2018-badge/
  kind: website
- label: blog.adafruit.com/2018/08/31/tilda-mk4-the-emf-2018-cellular-badge-programmable-in-micropython
  url: https://blog.adafruit.com/2018/08/31/tilda-mk4-the-emf-2018-cellular-badge-programmable-in-micropython/
  kind: article
images:
- file: assets/images/badges/emf-camp-2018/tilda-mk4-mk/d48f4d91d0.jpg
  source: "https://badge.emfcamp.org/TiLDA_MK4/"
  credit: "EMF Camp badge team"
  caption: "TiLDA Mk4 badge, front view"
contact: {}
notes:
- Official EMF Camp 2018 badge, a phone-like MicroPython badge with an onboard SIM800 GSM modem, LCD, accelerometer/gyro and LoRa radio; not yet in the archive. Found by the event-year sweep, task emf-badges.
- 'The sweep imported the page title verbatim as "TiLDA Mk4 (Mkδ)"; the maker''s own pages (badge.emfcamp.org, blog.emfcamp.org) just call it "TiLDA Mk4" — the parenthetical does not appear to name a distinct hardware variant, so the title here has been corrected to match the maker''s usage.'
status: released
sources:
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MK4/
  title: TiLDA Mk4 (Mkδ)
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-badges); event read as ''emf-camp-2018''.'
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MK4/
  title: TiLDA MK4 Badge
  accessed: '2026-09-08'
  note: 'Confirmed specs: MSP432E401Y MCU, 240x320 display, 2x WS2812B, GSM/Wi-Fi, 2000mAh battery, open-source firmware repo.'
- kind: url
  url: https://blog.emfcamp.org/2018/08/26/tilda-mk4-the-emf-2018-badge/
  title: 'TiLDA Mk4: the EMF 2018 badge'
  accessed: '2026-09-08'
  note: 'Confirmed the badge is the official EMF 2018 event badge, distributed to attendees; MicroPython app store; Texas Instruments/Seeed Studio sponsorship mentioned.'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'This entry duplicates emf-camp-2018-tilda-mk4 (same badge, same maker, same links) — the sweep appears to have picked it up a second time under the page''s parenthetical subtitle. No PCB color, shape, price, or unit-quantity figures were published on the sources checked, so those fields remain empty. Hardware design files (schematics/Gerbers) were not located, though the firmware repository is public; make_your_own.hardware_url left null pending confirmation.'
last_modified_date: '2026-09-08'
---

The TiLDA Mk4 was the official badge of EMF Camp 2018, built by the EMF Camp badge team as a fully-hackable, pocket-phone-shaped device programmable in MicroPython. At its core is a TI MSP432E401Y (ARM Cortex-M4F at 120MHz) with 256KB of internal RAM, 8MB of external SDRAM, and separate 1MB flash regions for firmware and filesystem, driving a 240x320 RGB LCD behind a T9 keypad and joystick.

What set it apart from a typical badge was a genuine onboard SIM800 GSM modem, letting attendees make calls and send texts over an on-site GSM network EMF Camp operated for the event, or over a Hologram IoT SIM with worldwide data. It also carried a CC3120 Wi-Fi module, Bluetooth, an Ethernet breakout option, Grove headers for UART/I2C expansion, humidity/dual-temperature/ambient-light/Hall-effect sensors, two WS2812B Neopixels with a header for more, and a 2000mAh battery. Attendees could write and share their own MicroPython apps through a community app store.

The sweep that generated this entry pulled it from the same maker page as the archive's existing `emf-camp-2018-tilda-mk4` entry, under the page's parenthetical subtitle "(Mkδ)" rather than the plain "TiLDA Mk4" title used elsewhere on the site — it describes the same hardware, not a separate revision.
