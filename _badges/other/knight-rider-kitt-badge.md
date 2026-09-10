---
title: Knight Rider badge
id: other-knight-rider-kitt-badge
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2017
makers:
- name: davedarko
  url: https://github.com/davedarko
summary: A K.I.T.T. Knight Rider car badge/brooch with a charlieplexed 8-LED scanner animation driven by an ATtiny13, originally on purple PCB with purple LEDs, later also offered in black with red LEDs.
functions: A push-button cycles through 8 LED animation modes, including a K.I.T.T.-style scanning effect, fast/slow chasers, a cross-fade, a police flasher, and a binary counter.
look:
  colors:
  - purple
  - black
  - red
  shape: null
  themes:
  - tv
  - movie
  - retro computer
tech:
  mcu: ATtiny13
  leds:
    count: 8
    type: charlieplexed
    note: 0603 or 0805 SMD LEDs depending on revision; 4 MCU pins drive all 8 via charlieplexing.
  display: null
  connectivity: []
  battery: CR2032 (or two CR2032/CR2016 cells depending on revision)
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: sold_out
  availability_note: 'Tindie listing checked 2026-09-07: "This product is no longer available for sale."'
  distribution:
  - purchase
  - kit
  where: Sold assembled or as a kit via the maker's Tindie store (davedarko); design files also shared on Hackaday.io and GitHub.
make_your_own:
  open_source: true
  hardware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Knight%20Rider%20Badge
  firmware_url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Knight%20Rider%20Badge
  eda_tool: KiCad
  notes: Originally designed in EAGLE (custom PCB outline via SVG-to-DXF conversion), later revisions ported to KiCad 8. Repository includes multiple hardware revisions (REV1 through REV3.1) plus a program-tester variant.
links:
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  kind: repo
- label: hackaday.io/project/25944-kitt-knight-rider-badgebrooch
  url: https://hackaday.io/project/25944-kitt-knight-rider-badgebrooch
  kind: hackaday
  archived: https://web.archive.org/web/20260515101535/https://hackaday.io/project/25944-kitt-knight-rider-badgebrooch
- label: github.com/davedarko/Simple-Add-ons-SAO/tree/main/Knight%20Rider%20Badge
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Knight%20Rider%20Badge
  kind: repo
- label: tindie.com/products/davedarko/kitt-knight-rider-blinky-led-badge
  url: https://www.tindie.com/products/davedarko/kitt-knight-rider-blinky-led-badge/
  kind: store
  archived: https://web.archive.org/web/20260513145035/https://www.tindie.com/products/davedarko/kitt-knight-rider-blinky-led-badge/
images:
- file: assets/images/badges/other/knight-rider-kitt-badge/82ea249c6c.jpg
  source: https://hackaday.io/project/25944-kitt-knight-rider-badgebrooch
  credit: davedarko
  caption: The K.I.T.T. Knight Rider badge/brooch on purple PCB with purple LEDs
  archived: https://web.archive.org/web/20260515101535/https://hackaday.io/project/25944-kitt-knight-rider-badgebrooch
- file: assets/images/badges/other/knight-rider-kitt-badge/5e8ef2ff48.gif
  source: https://hackaday.io/project/25944-kitt-knight-rider-badgebrooch
  credit: davedarko
  caption: K.I.T.T. badge LED scanner animation demo
  archived: https://web.archive.org/web/20260515101535/https://hackaday.io/project/25944-kitt-knight-rider-badgebrooch
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main
  title: davedarko/Simple-Add-ons-SAO — Find all of my simple add-ons in this repository
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/25944-kitt-knight-rider-badgebrooch
  title: K.I.T.T. - KNIGHT RIDER badge/brooch | Hackaday.io
  accessed: '2026-09-07'
  note: 'Project page: ATtiny13/45/85 options, 8 charlieplexed LEDs, CR2032 power, purple PCB/purple LED original with later black-PCB/red-LED variant, started July 2017; source of both saved images.'
  archived: https://web.archive.org/web/20260515101535/https://hackaday.io/project/25944-kitt-knight-rider-badgebrooch
- kind: url
  url: https://github.com/davedarko/Simple-Add-ons-SAO/tree/main/Knight%20Rider%20Badge
  title: Knight Rider Badge directory (Simple-Add-ons-SAO)
  accessed: '2026-09-07'
  note: Confirmed hardware revision folders (REV1-REV3.1, KiCad8) and design-file layout; no README with event/price details found in the directory listing.
- kind: url
  url: https://www.tindie.com/products/davedarko/kitt-knight-rider-blinky-led-badge/
  title: K.I.T.T. Knight Rider Blinky LED Badge from davedarko on Tindie
  accessed: '2026-09-07'
  note: Confirmed sold-out status ("no longer available for sale"), ATtiny13 + 8 LEDs + CR2032 description, badge/brooch form factor (~5x3cm), and that the design was popularized at MakerFaire Zurich (not a hacker-con badge, so event left as other).
  archived: https://web.archive.org/web/20260513145035/https://www.tindie.com/products/davedarko/kitt-knight-rider-blinky-led-badge/
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: No hacker-conference tie-in found; this is a general maker product (Tindie/Hackaday.io/GitHub) rather than a badge made for a specific con, and its Tindie description credits early popularity to MakerFaire Zurich, which is not in events.yml. Exact price and total quantity made were not stated on any source checked, so those fields are left empty. Event remains "other".
last_modified_date: '2026-09-10'
model:
  file: assets/models/other/knight-rider-kitt-badge.glb
  method: kicad
  source_file: Knight Rider Badge/KiCad8/kitt_0805.kicad_pcb
  generated: '2026-09-10'
  bytes: 76188
---

The K.I.T.T. Knight Rider badge is a wearable brooch shaped and lit to evoke the scanning "eye" of the car from the Knight Rider TV series. Designed by davedarko (based in Berlin) starting around July 2017, it uses an ATtiny13 (with ATtiny45/85 as alternate options in later revisions) to charlieplex 8 SMD LEDs across just 4 microcontroller pins, powered by a CR2032 coin cell. A button steps through eight animation modes, including the signature K.I.T.T. scanner sweep, chasers, a cross-fade, a police-light flasher, and a binary counter. The original run was on purple OSH Park PCBs with purple LEDs; a later black-PCB, red-LED variant was also produced.

The badge was sold assembled or as a kit through the maker's Tindie store, where the listing notes it drew early attention at MakerFaire Zurich; it is not tied to a specific hacker convention and is no longer available for purchase. Design files, schematics, and firmware are openly published, with the hardware progressing from an EAGLE-designed custom PCB outline through several revisions (REV1 through REV3.1) and eventually a KiCad 8 port, all hosted in the maker's Simple-Add-ons-SAO repository alongside other similar projects.

## Make your own

The GitHub repository (`Simple-Add-ons-SAO/Knight Rider Badge`) contains multiple hardware revisions, each with its own board files; the KiCad8 folder holds the current schematic, PCB layout, custom footprint library, and production/fabrication-toolkit files needed to order boards. Firmware for the ATtiny is included alongside the hardware; an ISP header on the board allows reprogramming or updating the animation modes.
