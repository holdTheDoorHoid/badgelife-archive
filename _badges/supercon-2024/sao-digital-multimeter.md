---
title: SAO Digital Multimeter
id: supercon-2024-sao-digital-multimeter
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Thomas Flummer
  url: https://hackaday.io/tf
summary: A compact RP2040/CircuitPython digital multimeter with an SAO connector, OLED screen, rotary mode knob and buzzer, built to measure SAO supply voltage, GPIO levels, resistance, LEDs and continuity, entered in the Supercon 8 (2024) SAO contest.
functions: Measures SAO input voltage, SAO GPIO voltage (read), resistance, and LEDs/diodes; continuity testing with a buzzer; two 2mm banana-socket probe connectors. An I2C tester and GPIO write (digital/PWM) were listed as planned, not-yet-implemented features at submission.
look:
  colors: []
  shape: null
  themes:
  - measurement
  - hardware tool
tech:
  mcu: RP2040
  leds: null
  display: OLED
  connectivity: []
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Entered in the Supercon 8 (2024) SAO badge contest; not described as sold or distributed to attendees generally. Design files are open for anyone to build their own.
make_your_own:
  open_source: true
  hardware_url: https://github.com/flummer/dmm-sao
  firmware_url: https://github.com/flummer/circuitpython/tree/hxr-sao-dmm
  eda_tool: KiCad
  license: 'Hardware/3D files: CC BY-SA 4.0. Firmware: MIT (plus third-party CircuitPython library licenses).'
  notes: KiCad v8.99 (nightly) source; 3D-printable case, knob, button caps and pogo-pin test probes included; a pre-built firmware.uf2 is provided in the repo.
notes: []
links:
- label: github.com/flummer/dmm-sao
  url: https://github.com/flummer/dmm-sao
  kind: repo
- label: hackaday.io/project/198892-sao-digital-multimeter
  url: https://hackaday.io/project/198892-sao-digital-multimeter
  kind: hackaday
  archived: https://web.archive.org/web/20251118041928/https://hackaday.io/project/198892-sao-digital-multimeter
- label: github.com/flummer/circuitpython/tree/hxr-sao-dmm
  url: https://github.com/flummer/circuitpython/tree/hxr-sao-dmm
  kind: repo
images:
- file: assets/images/badges/supercon-2024/sao-digital-multimeter/a8d6abe4d3.jpg
  source: https://github.com/flummer/dmm-sao
  credit: Thomas Flummer
  caption: The assembled SAO Digital Multimeter with OLED display, rotary knob, and probe leads
- file: assets/images/badges/supercon-2024/sao-digital-multimeter/ef06ec4d47.jpg
  source: https://hackaday.io/project/198892-sao-digital-multimeter
  credit: Thomas Flummer
  caption: The SAO Digital Multimeter in its 3D-printed unibody case
  archived: https://web.archive.org/web/20251118041928/https://hackaday.io/project/198892-sao-digital-multimeter
contact: {}
status: released
sources:
- kind: url
  url: https://github.com/flummer/dmm-sao
  title: SAO Digital Multimeter (flummer/dmm-sao)
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://github.com/flummer/dmm-sao
  title: flummer/dmm-sao README
  accessed: '2026-09-07'
  note: Confirmed RP2040/CircuitPython, KiCad hardware (CC BY-SA 4.0), MIT-licensed firmware, features (resistance/LED/continuity/voltage/GPIO read, I2C WIP), 3D-printed case, image URL. No display size, banana-socket, or SAO-extension detail in this README.
- kind: url
  url: https://hackaday.io/project/198892-sao-digital-multimeter
  title: SAO Digital Multimeter project page (hackaday.io)
  accessed: '2026-09-07'
  note: Confirmed maker Thomas Flummer, submission to the Supercon 8 (2024) SAO Contest on 2024-10-20, dimensions (41x75mm), rotary encoder + buttons, pogo-pin PCB stack (3 pogo pins), two 2mm banana sockets, SAO cable extension for recessed connectors, multilingual assembly guide, and the implemented-vs-planned feature split (GPIO read implemented; I2C tester and GPIO write planned). Display size in inches not stated anywhere on the page.
  archived: https://web.archive.org/web/20251118041928/https://hackaday.io/project/198892-sao-digital-multimeter
research:
  status: verified
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Fact-check pass (2026-09-07): re-fetched both cited sources directly. Corrected two invented/imprecise details from the prior research pass: tech.display had specified "0.96\" OLED" but neither the GitHub README nor the Hackaday.io project page states a screen size anywhere, so it is now just "OLED". look.themes included "learn to solder", which is not supported (the build involves QFN reflow/hotplate soldering aimed at an experienced maker, not a beginner soldering exercise), so it was removed. The functions field and body text were reworded slightly: the Hackaday page''s explicit "Features (implemented)" vs "Features (planned)" list shows GPIO reading is already implemented and only an I2C tester and GPIO write are planned, which the prior wording blurred together. The two 2mm banana sockets and the SAO cable extension are both confirmed, but only on the Hackaday.io page, not the GitHub README as the prior source note implied; source notes were corrected accordingly. Image verified
    present on disk and matches the photo shown at the top of the GitHub README. No storefront, price, or production-quantity information found; this appears to be a contest entry/open-source build-your-own project rather than something sold or distributed at scale, so get_one fields are mostly left empty. LED count/type not specified by the maker (the device tests LEDs but does not appear to use addressable LEDs itself, so tech.leds is left null rather than guessed). No SAO connector pin-count (v1 vs v2) stated in sources, so tech.sao_version left null. Everything remaining in the entry is now directly supported by the two cited sources. Merged with duplicate entry ''SAO Digital Multimeter'' (supercon-2024-sao-digital-multimeter-2).'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/supercon-2024/sao-digital-multimeter-2/
---

The SAO Digital Multimeter is a pocket-sized test tool built by Thomas Flummer for the Supercon 8 (2024) SAO Contest. Rather than being a decorative add-on, it is a working instrument: an RP2040 running CircuitPython drives an OLED display, a rotary knob for mode selection, function and system buttons, and a buzzer, letting a badge-hacker check an SAO's supply voltage, GPIO levels (read), resistance, LED/diode condition, and continuity via a pair of 2mm banana-socket probes. The device is slightly larger than a standard SAO at 41x75mm, housed in a 3D-printed unibody case with pogo-pin connections between its front and base PCBs, and the maker also designed a separate SAO cable extension (IDC connectors and ribbon cable) for reaching recessed connectors on badges with an enclosure.

The hardware (KiCad schematics, PCB files, and 3D-printable case and probe parts) is released under CC BY-SA 4.0, and the CircuitPython firmware is MIT-licensed, both published on the maker's GitHub. Assembly and user guides are provided in English, German, and Danish. No sale price, production quantity, or storefront was found; the project reads as an open-source contest build that others can replicate rather than a batch sold to attendees. At last check the maker listed an I2C tester and GPIO-write capability as planned but not yet implemented.

## Make your own

Hardware (KiCad source) and case/probe STL files are at [github.com/flummer/dmm-sao](https://github.com/flummer/dmm-sao); firmware is on a dedicated CircuitPython branch at [github.com/flummer/circuitpython/tree/hxr-sao-dmm](https://github.com/flummer/circuitpython/tree/hxr-sao-dmm). The repo includes a PDF schematic and step-by-step assembly/user manuals in three languages.

## Notes merged from the duplicate entry "SAO Digital Multimeter"

Thomas Flummer built the SAO Digital Multimeter as an entry in the Supercon 8 SAO Contest (created October 2024), designing a genuinely useful tool rather than a purely decorative add-on: a pocket-sized meter purpose-built for probing other people's SAOs and badges. It reads the supply voltage coming off a badge's SAO header, checks GPIO pin levels, tests LEDs and diodes, checks continuity with a buzzer, and measures resistance, with an I2C bus tester and a GPIO-write mode noted as planned but not yet finished features.

The electronics are built around a Raspberry Pi Pico-class RP2040 with expanded flash, running a custom CircuitPython build that gives the firmware more readable pin names. Input comes through two 2mm banana test-lead sockets, results show on a 0.96" OLED, and a detented rotary knob (using an embedded steel ball for mechanical click-feel) with a sub-function button handles mode selection. Power can come from USB-C or directly from a host badge's SAO connector, with a boost circuit to handle low badge voltages. The whole thing lives in a 3D-printed unibody case roughly 41x75mm — deliberately larger than the standard SAO footprint, since it is meant to be held and used rather than worn.

Both the hardware and firmware are open source: the KiCad design (v8.99 nightly), 3D-printable case/knob/button-cap files, and pogo-pin test probe designs are on GitHub under CC BY-SA 4.0, with the CircuitPython firmware fork under MIT. A pre-built firmware.uf2 and assembly instructions in English, German and Danish are included in the repo for anyone who wants to build their own.
