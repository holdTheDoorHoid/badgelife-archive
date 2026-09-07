---
title: Mad Cat Backpack
id: dc26-mad-cat-backpack
layout: badge
parent: DC26
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: dc26
year: 2018
makers:
- name: Peter Shabino
  url: https://github.com/Wireb
summary: An open-source animation upgrade board that piggybacks onto Mr TwinkleTwinkie's Mad Cat SAO, replacing its static LEDs with randomized blinking, talking and sparkle animations.
functions: 'Cycles through eight LED animations (fade in/out, blink/wink, lip licks, "piano teeth," eye bobble, talking, sparkles) on the Mad Cat''s face, waiting a random 0-8 minute interval between each; blinking is weighted to occur most often and sparkles least.'
look:
  colors:
  - purple
  - green
  shape: cat
  themes:
  - animal
  - cat
tech:
  mcu: PIC16F1503-I/SL
  leds:
    count: 8
    type: discrete
    note: White LEDs, reused from the donor Mad Cat kit
  display: none
  connectivity: []
  battery: powered by host badge
  sao_version: v1
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: 'Not sold as a finished product; the PCB can be ordered via the maker''s OSH Park share link and self-assembled/programmed. Requires an existing Mad Cat SAO from Mr TwinkleTwinkie to attach to.'
make_your_own:
  open_source: yes
  hardware_url: https://github.com/Wireb/Mad_Cat_Backpack
  firmware_url: https://github.com/Wireb/Mad_Cat_Backpack
  eda_tool: KiCad
  fab_url: https://www.oshpark.com/shared_projects/GfiURq3q
  license: MIT
  notes: 'KiCad 5.0 hardware project; firmware is MPLAB X 5.05 / assembly (mad_cat_backpack_v0.asm), programmed via PICkit4 or the provided production .hex file.'
links:
- label: github.com/Wireb/Mad_Cat_Backpack
  url: https://github.com/Wireb/Mad_Cat_Backpack
  kind: repo
- label: OSH Park shared project (Mad Cat Backpack PCB)
  url: https://www.oshpark.com/shared_projects/GfiURq3q
  kind: fab
images: []
contact: {}
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- This entry is for the add-on "backpack" board only, not the underlying Mad Cat SAO itself (by Mr TwinkleTwinkie), which is a separate, older item and would warrant its own catalog entry.
status: released
sources:
- kind: url
  url: https://github.com/Wireb/Mad_Cat_Backpack
  title: Mad Cat Backpack
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''dc26''.'
- kind: url
  url: https://raw.githubusercontent.com/Wireb/Mad_Cat_Backpack/master/README.md
  title: Mad_Cat_Backpack README
  accessed: '2026-09-07'
  note: Primary source for features, animations, parts list, MCU, LED count, build steps, license, and maker's name (copyright notice credits Peter Shabino).
- kind: url
  url: https://hackaday.io/project/159523-mad-cat
  title: Mad Cat | Hackaday.io
  accessed: '2026-09-07'
  note: Confirms the underlying Mad Cat SAO (which this backpack attaches to) was made by TwinkleTwinkie for DEF CON 26 (2018), corroborating event/year.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'Maker''s GitHub README is the primary source and is unambiguous about mechanism, parts, and licensing. Price and quantity made are not stated anywhere found and are left blank. No photo of the finished/assembled backpack was found - the only image in the repo (Mad_Cat_modificatons.jpg) is an annotated KiCad PCB render used for mod instructions, not a photo of the item, so no image was saved. Event field was already correct (dc26) and did not need correction.'
last_modified_date: '2026-09-07'
---

The Mad Cat Backpack is a small companion PCB designed by Peter Shabino (GitHub: Wireb) to upgrade Mr TwinkleTwinkie's Mad Cat SAO, a Cheshire Cat-themed add-on from DEF CON 26 (2018). Rather than a standalone badge, it is a "backpack" board that solders onto the back of an existing Mad Cat SAO, reusing that SAO's eight white LEDs but driving them with its own PIC16F1503 microcontroller instead of the original static circuit. Building one requires cutting four traces on the donor Mad Cat PCB and bridging four pads by hand between the two boards, so it is aimed at hobbyists comfortable with fine-pitch soldering rather than a plug-and-play accessory.

Once installed, the backpack runs a firmware loop that waits a randomized interval before playing one of eight animations across the cat's eyes and teeth - fades, blinks, "lip licks," a piano-teeth chase, eye bobbles, a talking effect, and sparkles - with blinking weighted to appear most often. The project is fully open source under the MIT license: KiCad 5.0 source files and a shared OSH Park PCB order link are provided for the hardware, and the PIC firmware (MPLAB X project plus a ready-to-flash .hex) is included for anyone who wants to build or modify their own.

No price, production quantity, or photo of an assembled unit was found in the maker's repository or elsewhere; it appears to have been shared purely as an open build rather than sold as a product.
