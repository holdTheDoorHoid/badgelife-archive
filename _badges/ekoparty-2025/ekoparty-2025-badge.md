---
title: Ekoparty Badge 2025
id: ekoparty-2025-ekoparty-2025-badge
layout: badge
parent: Ekoparty 2025
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: ekoparty-2025
year: 2025
makers:
- name: Lucas Leal
  role: hardware and software development
- name: Jorge Crowe (monstruoMIDI)
  role: concept and project coordination
- name: Nico Restbergs (Fábrica Marciana)
  role: PCB graphic design
summary: A portable sampler and synthesizer badge for Ekoparty 2025 with a resistive touch interface, played by touching exposed copper pads on the PCB.
functions: Built-in sequencer, sample player, synthesizer and audio effects, played via four resistive touch sensors (a "21" numeral, a diamond, and two "ears") that read finger contact through the RP2040's ADCs.
look:
  colors:
  - black
  - gold
  shape: null
  themes:
  - music
  - synthwave
tech:
  mcu: RP2040
  leds:
    count: 10
    type: RGB
    note: NeoPixel backlight on the front of the PCB (specific chip model not stated by the maker)
  display: none
  connectivity:
  - usb
  - audio
  battery: 18650 Li-ion cell, USB-C rechargeable
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: 'Distributed to attendees/participants at Ekoparty 2025 in Buenos Aires, Argentina; no pricing or production-volume figures published.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/lucasleale/Ekoparty_Badge_2025
  firmware_url: https://github.com/lucasleale/Ekoparty_Badge_2025/tree/main/Firmware
  eda_tool: null
links:
- label: github.com/badge-gallery/ekoparty-badge-2025
  url: https://github.com/badge-gallery/ekoparty-badge-2025
  kind: repo
- label: github.com/lucasleale/Ekoparty_Badge_2025
  url: https://github.com/lucasleale/Ekoparty_Badge_2025
  kind: repo
images:
- file: assets/images/badges/ekoparty-2025/ekoparty-2025-badge/b1acb2485e.jpg
  source: "https://github.com/badge-gallery/ekoparty-badge-2025"
  credit: "Lucas Leal"
  caption: "Top view of the Ekoparty 2025 badge PCB"
- file: assets/images/badges/ekoparty-2025/ekoparty-2025-badge/c360f36fdc.png
  source: "https://github.com/badge-gallery/ekoparty-badge-2025"
  credit: "Lucas Leal"
  caption: "Ekoparty 2025 badge in use, showing touch sensors and NeoPixel backlight"
contact: {}
notes:
- 'The discovery sweep imported the title as "Ekoparty 2025 Badge"; the maker''s own README titles it "Ekoparty Badge 2025" (Spanish: "Sampler y sintetizador portatil con interfaz tactil resistiva").'
status: released
sources:
- kind: url
  url: https://github.com/badge-gallery/ekoparty-badge-2025
  title: Ekoparty 2025 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-ekoparty); event read as ''Ekoparty 2025''.'
- kind: url
  url: https://github.com/lucasleale/Ekoparty_Badge_2025
  title: Ekoparty Badge 2025 README
  accessed: '2026-09-08'
  note: 'Maker''s own repo: confirmed creators, RP2040 hardware, PCM5100 DAC/TPA6138/TPA2028 audio chain, 10 NeoPixels, 4 resistive touch sensors, USB-C rechargeable battery, open firmware/hardware, and pulled the two badge photos.'
research:
  status: verified
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Fact-check pass (2026-09-08): re-read both cited sources. Two errors found and corrected: the maker''s README and the annotated PCB-photo diagram (badge-gallery repo) both show a removable 18650 li-ion cell in a holder ("portapilas 18650") with USB-C charge management, not a LiPo pouch cell as the entry previously stated — tech.battery and the body text were corrected. The README calls the backlight "NeoPixel" but never names the chip; "WS2812B" in tech.leds.type and the body was an unsupported specific claim and was changed to the generic "RGB" type with a note. All other fields and body sentences (MCU, DAC/amp chips, touch-pad layout and functions, AMY library, Dr. Dre/SynthDrum firmware, raw2h.py/22050Hz mono, BOOTSEL/UF2 flashing, Spanish manual, open-source status, makers/roles, title) were checked against the maker''s README and confirmed. look.colors (black, gold) filled in from the badge photo, directly visible. No price or production quantity is published anywhere; treated as a con-distributed item rather than a sold product. EDA tool for the PCB is not stated in the README.'
last_modified_date: '2026-09-08'
---

The Ekoparty Badge 2025 is a portable sampler and synthesizer built as the official electronic badge for Ekoparty 2025, Argentina's long-running hacker conference. It was designed by a three-person team: Lucas Leal handled the hardware and firmware, Jorge Crowe (monstruoMIDI) drove the concept and coordinated the project, and Nico Restbergs of Fábrica Marciana did the PCB graphic design. It continues a run of custom electronic badges Ekoparty has produced in recent years.

The badge is built around an RP2040 running Earle Philhower's Arduino core, paired with a PCM5100 I2S DAC (24-bit/96kHz) feeding a TPA6138 headphone amp and a TPA2028 speaker amp, using a modified build of the AMY synth/sample library for low-latency audio. Ten NeoPixel LEDs backlight the PCB, and the badge is played through four resistive touch pads etched directly into the board art — a "21" numeral and a diamond act as buttons, while two ear-shaped pads work as continuous controls (pitch shift and a high-pass filter) by reading finger resistance on the RP2040's ADC inputs. It runs on a rechargeable 18650 lithium-ion cell charged over USB-C, with an onboard charge-management circuit. The stock firmware ships as a sequenced demo built around samples from Dr. Dre's "Still," with an alternate SynthDrum firmware also provided.

## Make your own

Hardware design files and firmware are published on GitHub at lucasleale/Ekoparty_Badge_2025 (mirrored for the archive's sweep at badge-gallery/ekoparty-badge-2025). Prebuilt UF2 firmware images for both the default Dr. Dre demo and the SynthDrum variant are included, so the badge can be reflashed by holding its BOOTSEL button, connecting over USB-C, and dragging the .uf2 file onto the resulting RPI-RP2 drive — no compiler required. Building from source needs the Arduino IDE with the Earle Philhower RP2040 core and the repo's modified AMY library. A Python script (`raw2h.py`) converts custom 22050Hz mono raw audio into the C header format the firmware's sample player expects. A Spanish-language user manual is included in the repo.
