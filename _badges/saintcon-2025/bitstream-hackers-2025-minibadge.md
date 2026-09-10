---
title: Bitstream Hackers 2025 minibadge
id: saintcon-2025-bitstream-hackers-2025-minibadge
layout: badge
parent: Saintcon 2025
grand_parent: Badge Archive
nav_exclude: true
type: minibadge
event: saintcon-2025
year: 2025
makers:
- name: hamster (GitHub) -- maker unconfirmed
  url: https://github.com/hamster
summary: A SAINTCON 2025 'Bitstream Hackers' village minibadge built around an I2C EEPROM chip preloaded with an encoded puzzle fragment.
functions: Carries a Microchip AT24CS01 I2C EEPROM (1Kb, with a unique factory serial number) preloaded with an encoded snippet of text -- one piece of a village puzzle/CTF that attendees read out over I2C and decode. One LED and a solder jumper are also present on the board.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - puzzle
  - ctf
  form_factor: pcb badge
tech:
  mcu: none
  leds:
    count: 1
    type: null
    note: Single generic LED (KiCad 'Device:LED' symbol); exact part not specified in the design files.
  display: none
  connectivity:
  - i2c
  battery: null
  power: powered by host badge
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: true
  hardware_url: https://github.com/hamster/SAINTCON/tree/main/Bitstream%20Hackers/2025
  firmware_url: null
  gerbers_url: https://github.com/hamster/SAINTCON/tree/main/Bitstream%20Hackers/2025/gerber
  eda_tool: KiCad
  notes: No firmware -- the board is a passive EEPROM carrier with no MCU. KiCad schematic, PCB (including a panelized bhc-panel.kicad_pcb), and gerbers are in the repo.
links:
- label: github.com/hamster/SAINTCON/tree/main/Bitstream%20Hackers/2025
  url: https://github.com/hamster/SAINTCON/tree/main/Bitstream%20Hackers/2025
  kind: repo
images:
- file: assets/images/badges/saintcon-2025/bitstream-hackers-2025-minibadge/c9622d748a.jpg
  source: https://github.com/hamster/SAINTCON/tree/main/Bitstream%20Hackers/2025
  credit: hamster (GitHub)
  caption: PCB render of the 2025 Bitstream Hackers minibadge showing full board artwork
- file: assets/images/badges/saintcon-2025/bitstream-hackers-2025-minibadge/61a1d5d469.jpg
  source: https://github.com/hamster/SAINTCON/tree/main/Bitstream%20Hackers/2025
  credit: hamster (GitHub)
  caption: Silkscreen artwork for the 2025 Bitstream Hackers minibadge
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
status: listed
sources:
- kind: url
  url: https://github.com/hamster/SAINTCON/tree/main/Bitstream%20Hackers/2025
  title: Bitstream Hackers 2025 minibadge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''saintcon''.'
- kind: url
  url: https://github.com/hamster/SAINTCON/blob/main/Bitstream%20Hackers/2025/bhc.kicad_sch
  title: bhc.kicad_sch (schematic)
  accessed: '2026-09-07'
  note: Confirmed the AT24CS01 I2C EEPROM chip, single LED, solder jumper, and MiniBadge_Full connector; no MCU present.
- kind: url
  url: https://raw.githubusercontent.com/hamster/SAINTCON/main/Bitstream%20Hackers/2025/EEPROM/01.txt
  title: EEPROM/01.txt sample data
  accessed: '2026-09-07'
  note: Sample of the encoded puzzle text (e.g. 'In the void, I lurk where keys collide') stored per-unit in the EEPROM/ folder, supporting the puzzle/CTF function.
- kind: url
  url: https://github.com/hamster/SAINTCON/commits/main/Bitstream%20Hackers/2025
  title: Commit history for Bitstream Hackers/2025
  accessed: '2026-09-07'
  note: All commits to this folder are authored by GitHub user 'hamster'; no separate maker credit found.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Event corrected from 'other' to saintcon-2025 based on the repo's own folder path (hamster/SAINTCON, 'Bitstream Hackers/2025'). No independent source (Hackaday, forum post, storefront) describing the 'Bitstream Hackers' village or naming a specific designer was found; the repo itself is the only source. Price, quantity, and availability are not stated anywhere in the repo. LED part number and PCB color are not specified in the design files.
last_modified_date: '2026-09-10'
redirect_from:
- /badges/other/bitstream-hackers-2025-minibadge/
model:
  file: assets/models/saintcon-2025/bitstream-hackers-2025-minibadge.glb
  method: kicad
  source_file: Bitstream Hackers/2025/bhc-panel.kicad_pcb
  generated: '2026-09-10'
  bytes: 1042516
---

The Bitstream Hackers 2025 minibadge was made for SAINTCON's "Bitstream Hackers" village, distributed via the `hamster/SAINTCON` GitHub repository rather than a storefront or press writeup. It is a small, MCU-less PCB that plugs into a SAINTCON badge and carries a single Microchip AT24CS01 I2C EEPROM chip -- an 1Kb memory with a built-in unique factory serial number -- along with one LED and a solder jumper.

The EEPROM is the point of the badge: the repository includes a folder of ten `EEPROM/NN.txt` files, each holding a short line of encoded or cipher-flavored text (for example, "In the void, I lurk where keys collide" followed by what looks like base64). This points to a village puzzle or CTF in which attendees read the chip's contents over I2C and decode the hidden message, with different units potentially carrying different fragments or ciphers.

Hardware is fully open: the repo has the KiCad schematic and PCB layout, a panelized production file (`bhc-panel.kicad_pcb`) for manufacturing multiple boards at once, and a gerber folder for fabrication. No firmware is included or needed, since the board has no microcontroller of its own -- it relies entirely on the host badge to talk to it over I2C. No pricing, production quantity, or distribution details were found; the entry should be revisited if the SAINTCON community publishes more about the village or its minibadge run.

## Make your own

The `Bitstream Hackers/2025` folder in the repo has everything needed to reproduce the board: `bhc.kicad_sch` and `bhc.kicad_pcb` for the individual badge, `bhc-panel.kicad_pcb` for panelized production, and a `gerber/` folder with fabrication-ready files. Populate an AT24CS01 SOIC-8 EEPROM, one LED, a resistor, and a solder jumper, then write puzzle data to the EEPROM using the format seen in the repo's `EEPROM/` text files.
