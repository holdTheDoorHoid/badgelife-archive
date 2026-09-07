---
title: SAO Digital Multimeter
id: supercon-2024-sao-digital-multimeter-2
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Thomas Flummer
  url: https://hackaday.io/hacker/41938-thomas-flummer
summary: A compact RP2040/CircuitPython digital multimeter in a 3D-printed unibody case with an SAO connector on the back, a detented rotary mode knob, OLED screen and 2mm test-lead sockets, built for the Supercon 8 SAO Contest to measure badge supply voltage, GPIO levels, LEDs, continuity and resistance.
functions: 'Measures SAO/badge supply voltage, GPIO pin voltage, LED/diode forward behavior, continuity (with buzzer) and resistance; an I2C bus tester and GPIO-write mode were planned as future additions.'
look:
  colors: []
  shape: null
  themes: [hardware tool, measurement]
tech:
  mcu: RP2040
  leds: null
  display: 0.96" OLED
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
  open_source: yes
  hardware_url: https://github.com/flummer/dmm-sao
  firmware_url: https://github.com/flummer/circuitpython/tree/hxr-sao-dmm
  eda_tool: KiCad
  license: 'Hardware/3D files: CC BY-SA 4.0. Firmware: MIT (plus third-party CircuitPython library licenses).'
  notes: 'KiCad v8.99 (nightly) source; 3D-printable case, knob, button caps and pogo-pin test probes included; a pre-built firmware.uf2 is provided in the repo.'
links:
- label: hackaday.io/project/198892-sao-digital-multimeter
  url: https://hackaday.io/project/198892-sao-digital-multimeter
  kind: hackaday
- label: github.com/flummer/dmm-sao
  url: https://github.com/flummer/dmm-sao
  kind: repo
- label: github.com/flummer/circuitpython/tree/hxr-sao-dmm
  url: https://github.com/flummer/circuitpython/tree/hxr-sao-dmm
  kind: repo
images:
  - file: assets/images/badges/supercon-2024/sao-digital-multimeter-2/ef06ec4d47.jpg
    source: "https://hackaday.io/project/198892-sao-digital-multimeter"
    credit: "Thomas Flummer"
    caption: "The SAO Digital Multimeter in its 3D-printed unibody case"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198892-sao-digital-multimeter
  title: SAO Digital Multimeter
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/198892-sao-digital-multimeter
  title: SAO Digital Multimeter - Hackaday.io project page
  accessed: '2026-09-07'
  note: 'Confirmed maker, Supercon 8 SAO Contest entry (created Oct 20, 2024), RP2040/CircuitPython, OLED display, rotary mode knob with sub-button, 2mm banana test-lead sockets, buzzer for continuity, unibody 3D-printed case (~41x75mm, over standard SAO size), USB-C/badge dual power with boost circuit, multilingual assembly guide.'
- kind: url
  url: https://github.com/flummer/dmm-sao
  title: flummer/dmm-sao on GitHub
  accessed: '2026-09-07'
  note: 'Confirmed open hardware (KiCad, CC BY-SA 4.0) and firmware (MIT) with pre-built firmware.uf2, 3D-printable probes using P100-B1 pogo pins, and functions list (voltage, GPIO, LED/continuity test, resistance, in-progress I2C tester).'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'This is a one-off contest build for the Supercon 8 SAO Contest, not a sold/distributed product, so price, quantity and availability are not applicable/stated by the maker; left empty rather than guessed. No LED count/type or SAO header version (4-pin vs 6-pin) stated in the sources reviewed. Marked status: released since the device is built and documented (not merely announced).'
last_modified_date: '2026-09-07'
---

Thomas Flummer built the SAO Digital Multimeter as an entry in the Supercon 8 SAO Contest (created October 2024), designing a genuinely useful tool rather than a purely decorative add-on: a pocket-sized meter purpose-built for probing other people's SAOs and badges. It reads the supply voltage coming off a badge's SAO header, checks GPIO pin levels, tests LEDs and diodes, checks continuity with a buzzer, and measures resistance, with an I2C bus tester and a GPIO-write mode noted as planned but not yet finished features.

The electronics are built around a Raspberry Pi Pico-class RP2040 with expanded flash, running a custom CircuitPython build that gives the firmware more readable pin names. Input comes through two 2mm banana test-lead sockets, results show on a 0.96" OLED, and a detented rotary knob (using an embedded steel ball for mechanical click-feel) with a sub-function button handles mode selection. Power can come from USB-C or directly from a host badge's SAO connector, with a boost circuit to handle low badge voltages. The whole thing lives in a 3D-printed unibody case roughly 41x75mm — deliberately larger than the standard SAO footprint, since it is meant to be held and used rather than worn.

Both the hardware and firmware are open source: the KiCad design (v8.99 nightly), 3D-printable case/knob/button-cap files, and pogo-pin test probe designs are on GitHub under CC BY-SA 4.0, with the CircuitPython firmware fork under MIT. A pre-built firmware.uf2 and assembly instructions in English, German and Danish are included in the repo for anyone who wants to build their own.
