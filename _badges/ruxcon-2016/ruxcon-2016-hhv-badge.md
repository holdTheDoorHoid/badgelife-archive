---
title: RuxBadge (Ruxcon 2016 HHV Badge)
id: ruxcon-2016-ruxcon-2016-hhv-badge
layout: badge
parent: Ruxcon 2016
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: ruxcon-2016
year: 2016
makers:
- name: darkglade (Morgan) / Ruxcon Hardware Hacking Village
summary: A solder-your-own badge kit for the Ruxcon 12 (2016) Hardware Hacking Village, built around an STM32F030 and an IR transceiver so assembled badges can talk to each other.
functions: 'Badge-to-badge communication over IR using a custom "RuxBadge" protocol (a modified Panasonic IR protocol with a 24-bit address field); the firmware also hides a CTF flag for attendees to extract from the code or the running device.'
look:
  colors:
  - red
  shape: null
  themes:
  - village badge
  - learn to solder
  - kit
  - ctf
tech:
  mcu: STM32F030K6T6
  leds:
    count: 8
    type: 0805 SMD (2512-on-3216-footprint)
    note: Green LEDs (D2-D9), driven from the MCU.
  display: none
  connectivity:
  - ir
  battery: 2x CR2032
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - village
  where: Handed out for on-site soldering at the Ruxcon 12 (2016) Hardware Hacking Village.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/darkglade/ruxconhhv2016
  eda_tool: null
links:
- label: github.com/darkglade/ruxconhhv2016
  url: https://github.com/darkglade/ruxconhhv2016
  kind: repo
- label: ruxconhhv.darkglade.com/2016/RuxBadge.pdf
  url: https://ruxconhhv.darkglade.com/2016/RuxBadge.pdf
  kind: doc
images: []
contact: {}
notes:
- 'Sweep found the title as "Ruxcon 2016 HHV Badge"; the badge''s own instruction sheet and repo call it "RuxBadge". Kept both in the title.'
status: released
sources:
- kind: url
  url: https://github.com/darkglade/ruxconhhv2016
  title: Ruxcon 2016 HHV Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:con-kiwicon); event read as ''Ruxcon 2016''.'
- kind: url
  url: https://github.com/darkglade/ruxconhhv2016
  title: darkglade/ruxconhhv2016 (README)
  accessed: '2026-09-08'
  note: Confirms it is the Ruxcon 12 (2016) Hardware Hacking Village firmware repo; contains badge firmware with an embedded CTF flag and a modified Arduino IRRemote library implementing the "RuxBadge" IR protocol (extended-address Panasonic variant).
- kind: url
  url: https://raw.githubusercontent.com/darkglade/ruxconhhv2016/master/badge/README.md
  title: badge/README.md build instructions
  accessed: '2026-09-08'
  note: Confirms firmware targets STM32F030; only firmware source is published, no schematic/PCB/gerber files found in the repo.
- kind: url
  url: https://ruxconhhv.darkglade.com/2016/RuxBadge.pdf
  title: RuxBadge instruction sheet (BOM and soldering guide)
  accessed: '2026-09-08'
  note: 'Maker-published assembly PDF; gives full BOM (STM32F030K6T6 MCU, TSSP58038 IR receiver, 940nm IR emitter, 8x green 0805 LEDs, 2x CR2032 battery holders) and shows the board is a red PCB with a stylised animal-head/lizard silhouette silkscreened "RUXCON 2016 Hardware Hacking Village".'
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Price, quantity made, and availability are not stated anywhere found; only firmware (not schematic/PCB/gerber files) is published, so open_source is set to partial rather than yes. No further photos of the assembled badge were found at a directly linkable image URL (the only board photos live embedded inside the instruction PDF).'
last_modified_date: '2026-09-08'
---

The RuxBadge was the solder-it-yourself badge given out at the Hardware Hacking Village (HHV) of Ruxcon 12, held in 2016, and built by darkglade (Morgan) for the village. Attendees assembled the kit themselves on an STM32F030K6T6-based PCB shaped like a stylised animal head, populating eight green SMD LEDs, an IR receiver/emitter pair, and dual CR2032 battery holders under the guidance of an HHV-authored instruction sheet.

Once built, badges could talk to each other over infrared using "RuxBadge," a custom protocol the maker describes as a modified version of the Panasonic IR protocol with the address field extended to 24 bits and some timing changes. The firmware, released afterward on GitHub along with a matching fork of the Arduino IRRemote library, also embeds a flag for a capture-the-flag style challenge tied to the badge.

Only the firmware source has been published; no schematic, PCB layout, or gerber files were found in the repo, so the hardware itself is not independently reproducible from what is public. Price, production quantity, and post-event availability were not stated in any source found.
