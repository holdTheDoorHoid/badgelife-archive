---
title: Sound to Light for EMF Tildagon Badge
id: emf-camp-2026-sound-to-light-for-emf-tildagon-badge
layout: badge
parent: EMF Camp 2026
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: emf-camp-2026
year: 2026
makers:
- name: Tony Goacher
  url: https://github.com/tonygoacher
summary: A DIY sound-reactive hexpansion for the EMF Camp 2026 Tildagon badge, built around a modified SparkFun sound detector that drives the badge's 12 onboard RGB LEDs in time with ambient audio.
functions: Runs as a Tildagon OS app (upload, start, stop like any other app) that visualizes sound level on the badge's 12 RGB LEDs; includes multiple lighting effects and a potentiometer-free, software-adjustable sensitivity.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - music
tech:
  mcu: null
  leds:
    count: 12
    type: RGB
    note: Uses the Tildagon badge's own 12 onboard surface-mount RGB LEDs; no additional LEDs added.
  display: null
  connectivity:
  - audio
  battery: powered by host badge
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Not sold; a build-it-yourself hexpansion. The Protoboard Hexpansion base (~£3.37 / ~$4.50) plus a SparkFun sound detector module and an LMV324 op-amp are the parts to source.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/tonygoacher/tildagon_soundtolight
  firmware_url: https://github.com/tonygoacher/tildagon_soundtolight
  eda_tool: null
  license: CC BY-SA 4.0
  notes: Code is a MicroPython port of Michael Bartlett's C implementation of the SparkFun RGB LED Music Sound Visualizer. The SparkFun sound detector board is designed to run on 5V, so building it requires a resistor-value change to adapt it to the Tildagon hexpansion's 3.3V supply. Build also includes a 3D-printed diffuser and a two-point lanyard mount.
links:
- label: hackaday.io/project/205329-sound-to-light-for-emf-tildagon-badge
  url: https://hackaday.io/project/205329-sound-to-light-for-emf-tildagon-badge
  kind: hackaday
- label: github.com/tonygoacher/tildagon_soundtolight
  url: https://github.com/tonygoacher/tildagon_soundtolight
  kind: repo
- label: 'Sound to Light for EMF Tildagon Badge (YouTube demo)'
  url: https://youtu.be/Oy822CMz1iM
  kind: video
images:
  - file: assets/images/badges/emf-camp-2026/sound-to-light-for-emf-tildagon-badge/435af6b812.jpg
    source: "https://hackaday.io/project/205329-sound-to-light-for-emf-tildagon-badge"
    credit: "Tony Goacher"
    caption: "Sound-to-light hexpansion mounted on the Tildagon badge"
  - file: assets/images/badges/emf-camp-2026/sound-to-light-for-emf-tildagon-badge/97a509327d.jpg
    source: "https://hackaday.io/project/205329-sound-to-light-for-emf-tildagon-badge"
    credit: "Tony Goacher"
    caption: "3D-printed LED diffuser ring"
contact: {}
notes:
- Sound-reactive hexpansion built from a SparkFun sound detector plus 3D-printed diffuser/lanyard mount, driving the Tildagon's 12 RGB LEDs; documented on Hackaday.io. Found by the event-year sweep, task emf-addons.
status: released
sources:
- kind: url
  url: https://hackaday.io/project/205329-sound-to-light-for-emf-tildagon-badge
  title: Sound to Light for EMF Tildagon Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''EMF Camp 2024'' by the sweep, but the project page states it was created 2026-03-18 and the maker writes "I hope to see others using it in 2026" — this is an EMF Camp 2026 project, corrected below.'
- kind: url
  url: https://github.com/tonygoacher/tildagon_soundtolight
  title: tonygoacher/tildagon_soundtolight
  accessed: '2026-09-08'
  note: Maker's repo; confirms open-source license (CC BY-SA 4.0), MicroPython app for Tildagon OS, build instructions, and hardware modifications needed.
research:
  status: verified
  confidence: high
  last_checked: '2026-09-08'
  notes: "Core facts confirmed on the maker's own Hackaday.io project page and GitHub repo. No pricing beyond the ~£3.37 Protoboard Hexpansion base was published; the project is a DIY build (parts sourced by the builder), not something sold as a finished unit, so get_one.price/quantity are left empty. MCU is the Tildagon badge's own (ESP32-S3, per the Tildagon entry) — left null here since this accessory itself has no separate MCU; it runs as a MicroPython app on the host badge. Fact-check correction: the researcher's draft had event as EMF Camp 2024 and said the sound detector's resistor mod was 'for 5V operation,' but the Hackaday page states the project was created 2026-03-18 with the maker hoping 'to see others using it in 2026,' and the GitHub README says the sound detector board 'was designed to run of 5V so we'll need to change a resistor value' to adapt it to the Tildagon's 3.3V hexpansion supply — the reverse of what was written. Corrected event/year to emf-camp-2026 and fixed the voltage wording; this entry now lives in the wrong folder (_badges/emf-camp-2024/) pending a move, which build_index --check will flag. Also corrected the second image's caption: it is a 3D-printed diffuser ring render, not a 'protoboard hexpansion build.'"
last_modified_date: '2026-09-08'
redirect_from:
- /badges/emf-camp-2024/sound-to-light-for-emf-tildagon-badge/
---

Tony Goacher's Sound to Light project is a build-it-yourself hexpansion for the EMF Camp 2026 Tildagon badge that turns ambient sound into a light show on the badge's 12 onboard RGB LEDs. It plugs a modified SparkFun sound detector module (with an LMV324 op-amp reworked for the badge's voltage) into a Protoboard Hexpansion, and a MicroPython app installed on the Tildagon reads the sensor and drives the LEDs through several visualization modes, adjustable in software rather than with a physical sensitivity dial.

The build includes a 3D-printed diffuser to spread the LED light more evenly and a mount compatible with standard two-point lanyards. Goacher documented the full build — including the soldering changes needed to adapt the sound detector (designed for 5V) to the Tildagon's 3.3V hexpansion supply — on Hackaday.io, with step-by-step instructions and code published on GitHub under a CC BY-SA 4.0 license. The MicroPython app itself is a port of Michael Bartlett's C implementation of the SparkFun RGB LED Music Sound Visualizer.

## Make your own

Everything needed to build one is at Tony Goacher's [tildagon_soundtolight](https://github.com/tonygoacher/tildagon_soundtolight) repository: the MicroPython app (`app.py`), Tildagon app metadata (`tildagon.toml`, `metadata.json`), and a PDF with construction instructions covering the sound-detector rework, wiring into a Protoboard Hexpansion, and 3D-printing the diffuser and lanyard mount.
