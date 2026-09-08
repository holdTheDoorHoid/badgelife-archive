---
title: DC225 SAO 2024
id: other-dc225-sao-2024-firmware
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2024
makers:
- name: DC225
  url: https://defcon225.org/
summary: A CTF-style Shitty Add-On built for the DC225 (Baton Rouge, LA) DEF CON group's 2024 meetup, controlled over IR.
functions: Receives IR remote commands to reveal CTF flags, run a "disco" LED animation mode, and switch the onboard LED between preset colors (green, blue, purple, yellow, white).
look:
  colors:
  - black
  shape: null
  themes:
  - ctf
  - puzzle
  - village badge
tech:
  mcu: ATtiny
  leds:
    count: 1
    type: discrete
    note: common-anode RGB LED driven by PWM (analogWrite) on three GPIO pins
  display: null
  connectivity:
  - ir
  battery: null
  sao_version: v2
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/ynots0ups/DC225_SAO_2024/blob/main/DC225-SAO-v2024-3_KiCad.zip
  firmware_url: https://github.com/ynots0ups/DC225_SAO_2024
  eda_tool: KiCad
links:
- label: github.com/ynots0ups/DC225_SAO_2024
  url: https://github.com/ynots0ups/DC225_SAO_2024
  kind: repo
images:
- file: assets/images/badges/other/dc225-sao-2024-firmware/8f67fc6e66.jpg
  source: https://github.com/ynots0ups/DC225_SAO_2024/tree/main/website
  credit: DC225 (s0ups)
  caption: The SAO's SOIC-8 MCU and 6-pin SAO header
- file: assets/images/badges/other/dc225-sao-2024-firmware/72d9f9f61e.jpg
  source: https://github.com/ynots0ups/DC225_SAO_2024/tree/main/website
  credit: DC225 (s0ups)
  caption: IR receiver and RGB LED on the PCB
contact: {}
notes:
- Title on the community sheet was "DC225_SAO_2024 firmware"; the repo README calls the underlying project the "2024 DC225 Shitty Add-on CTF."
status: released
sources:
- kind: url
  url: https://github.com/ynots0ups/DC225_SAO_2024
  title: DC225_SAO_2024 firmware
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''DEF CON 2024''.'
- kind: url
  url: https://github.com/ynots0ups/DC225_SAO_2024
  title: 'ynots0ups/DC225_SAO_2024: Firmware for the 2024 DC225 Shitty Add-on CTF'
  accessed: '2026-09-07'
  note: Repo contents (README, KiCad zip, .ir command list, firmware-special folder) confirm it is an IR-controlled CTF SAO with a KiCad v2024-3 PCB design; no chip/LED part numbers, price, quantity, or hardware photos given.
- kind: url
  url: https://defcon225.org/
  title: DEFCON225 (DC225) | Baton Rouge, LA
  accessed: '2026-09-07'
  note: Confirms DC225 is a local DEF CON group (area code 225, Baton Rouge, LA) rather than the annual DEF CON conference; this SAO was made for the group's own 2024 meetup/CTF, not for DEF CON 32.
  archived: https://web.archive.org/web/20260614133457/https://defcon225.org/
- kind: url
  url: https://raw.githubusercontent.com/ynots0ups/DC225_SAO_2024/main/firmware/firmware.ino
  title: firmware.ino (DC225_SAO_2024)
  accessed: '2026-09-07'
  note: 'Fact-check pass: firmware source confirms the flag/disco/color-change IR commands and colors exactly, includes ATtinySerialOut.hpp and TinyIRReceiver.hpp (ATtiny-family chip), and drives a common-anode RGB LED via PWM on three discrete GPIO pins (controlLeds()) -- corrects tech.mcu and tech.leds from null. Also reveals a Morse-code LED flag and a serial-console flag not mentioned in the summary/body (not added, to keep this a fact-check rather than new research).'
- kind: url
  url: https://github.com/ynots0ups/DC225_SAO_2024/tree/main/website
  title: website/ folder (DC225_SAO_2024)
  accessed: '2026-09-07'
  note: 'Fact-check pass: contains real photos of the assembled PCB (header.jpg, tsop.jpg) not seen in the original research pass, which had said only a generic GitHub social-preview card existed. header.jpg shows an SOIC-8 chip (U1) on a 6-pin SAO header -- consistent with the ATtiny call above and confirms sao_version v2 (6-pin). vcc_gnd.jpg (not saved) is a KiCad schematic screenshot, not a photo, and was not used as an image. Two photos saved to images.'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Original research pass (2026-09-07, low confidence) is superseded by this fact-check pass (medium confidence). All prior factual claims -- DC225 as a Baton Rouge-area DC group (not DEF CON 32), the IR-triggered flag/disco/color-change functions and the five listed colors, the KiCad v2024-3 hardware, and the "no README beyond the IR command table" note -- were re-verified against the same cited sources and hold up. Two corrections made: (1) tech.mcu and tech.leds were wrongly left null; the firmware source (already in this repo) names ATtiny libraries and a discrete common-anode RGB LED, so those are now filled from that same primary source. (2) make_your_own.open_source was "partial" but the single repo publishes both the KiCad hardware and the Arduino firmware, so it is corrected to "yes". Also found two real hardware photos in the repo''s website/ folder that the first pass missed (it only saw the auto-generated social-preview card); both are now saved to images, and the newly-saved
    photos show a black solder mask with white silkscreen, so look.colors is filled with [black]. Still empty/unknown, with no source found: tech.display, tech.battery, look.shape, and all get_one fields (price, quantity, distribution, where) -- no storefront, price, or production-quantity information exists in the repo or on defcon225.org.'
last_modified_date: '2026-09-07'
---

The DC225 SAO 2024 is a Shitty Add-On built by the DC225 DEF CON group -- a Baton Rouge, Louisiana-based local DEF CON group covering the 225 area code and surrounding region -- for their own 2024 meetup. Unlike badges made for the annual DEF CON convention in Las Vegas, this one was designed for the group's own gathering, and its firmware README describes it as built for a "Shitty Add-on CTF."

The SAO is controlled over infrared: sending specific IR codes reveals CTF flags, triggers a "disco" LED animation mode, or switches an onboard LED between five preset colors (green, blue, purple, yellow, white). The hardware itself is a custom KiCad PCB (design revision v2024-3) with a black solder mask, and the GitHub repository publishes both that KiCad design and the firmware, which runs on an ATtiny-family chip and drives a single common-anode RGB LED by PWM.

## Make your own

The maker's GitHub repository (github.com/ynots0ups/DC225_SAO_2024) includes a KiCad PCB design (`DC225-SAO-v2024-3_KiCad.zip`), firmware source, a `firmware-special` variant folder, and an `.ir` file listing the IR command codes for the flag, disco, and color-change modes -- enough to reproduce the hardware and firmware, though no bill of materials or assembly instructions are included.
