---
title: Metamer SAO
id: supercon-2024-metamer-sao
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: supercon-2024
year: 2024
makers:
- name: Reid Sox-Harris
  url: https://reidsoxharris.me
summary: A 16-LED SAO (12 distinct wavelengths from UV to deep red plus four white color temperatures) driven by a TI LP5018 constant-current driver over I2C, built to demonstrate metamerism and spectral color mixing beyond RGB; v1 was made for Open Hardware Summit 2024 in Montreal and v2 (adding a PY32F002B Cortex-M0 to bootstrap I2C) was entered in the Supercon 8 SAO Contest.
functions: Cycles through preset LED combinations to demonstrate metamerism (different spectra that look the same color to the eye); brightness of each of the 16 channels is set over I2C.
look:
  colors:
  - purple
  shape: horseshoe
  themes:
  - science
  - art
  - minimalist
tech:
  mcu: PY32F002B (v2 only; v1 has no onboard MCU)
  leds:
    count: 16
    type: discrete
    note: 12 distinct wavelengths (456-640nm, including a 505nm LED and UV) plus 4 white color temperatures, all driven through a TI LP5018 constant-current I2C LED driver
  display: none
  connectivity:
  - i2c
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - contest
  where: Entered in the Hackaday Supercon 8 (2024) SAO Contest; not established as sold or given away as a general con drop.
make_your_own:
  open_source: true
  hardware_url: https://github.com/eosti/metamer-sao
  firmware_url: https://github.com/eosti/metamer-sao
  eda_tool: KiCad
  notes: v2.1 hardware is designed in KiCad with gerbers and pick-and-place files in the repo; v2 was originally designed in Altium. Firmware for the onboard PY32F002B is MicroPython. Repo also includes Python scripts the maker used to generate LED brightness-normalization data and the graphs from Reid Sox-Harris's "Beyond RGB" talk. Licensed MIT.
links:
- label: hackaday.io/project/198439-metamer-sao
  url: https://hackaday.io/project/198439-metamer-sao
  kind: hackaday
- label: github.com/eosti/metamer-sao
  url: https://github.com/eosti/metamer-sao
  kind: repo
- label: reidsoxharris.me/projects/metamer-sao
  url: https://reidsoxharris.me/projects/metamer-sao
  kind: website
  archived: https://web.archive.org/web/20260508083359/https://reidsoxharris.me/projects/metamer-sao/
images:
- file: assets/images/badges/supercon-2024/metamer-sao/d8bd20a2f1.jpg
  source: https://hackaday.io/project/198439-metamer-sao
  credit: Reid Sox-Harris
  caption: Metamer SAO board
- file: assets/images/badges/supercon-2024/metamer-sao/f9a79d560f.jpg
  source: https://reidsoxharris.me/projects/metamer-sao
  credit: Reid Sox-Harris
  caption: Metamer SAO
  archived: https://web.archive.org/web/20260508083359/https://reidsoxharris.me/projects/metamer-sao/
contact: {}
notes: []
status: released
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Core facts confirmed directly by the maker's own project page, GitHub repo, and Hackaday.io project page, which agree with each other. Price, quantity made, and general availability/distribution are not stated anywhere found, so those fields are left empty; the item is described as an entry in the Supercon 8 SAO Contest rather than a badge sold or distributed at large, so get_one.where reflects that rather than a purchase channel. PCB shape is described as horseshoe-shaped, echoing the CIE 1931 color space diagram.
last_modified_date: '2026-09-07'
---

The Metamer SAO is an educational add-on board built by Reid Sox-Harris (Hackaday.io handle eosti) to demonstrate metamerism: the phenomenon where two different light spectra can look like the same color to the human eye. Rather than mixing red, green, and blue like a typical RGB LED, the board carries 16 individually addressable LED channels covering 12 distinct wavelengths from deep UV through 640nm red, plus four different white color temperatures, all driven through a Texas Instruments LP5018 constant-current I2C LED driver so the whole set can be controlled without overloading a host badge's power budget.

The first version was built for Open Hardware Summit 2024 in Montreal. A second version added an onboard PY32F002B Cortex-M0 microcontroller, running MicroPython, so the SAO could bootstrap its own I2C communication and show a default display pattern without needing the host badge to drive it; this v2 was entered in the Hackaday Supercon 8 (2024) SAO Contest. Sox-Harris also presented the underlying color-science work in a talk titled "Beyond RGB."

Hardware and firmware are fully open source under the MIT license. The current v2.1 board is designed in KiCad with gerbers and pick-and-place files included in the GitHub repository; the original v2 board was designed in Altium. The repo also includes the Python tooling the maker used to normalize LED brightness and to generate the color-space graphs shown in the talk. No information was found on price, quantity produced, or whether units were sold or given away beyond the contest entry.
