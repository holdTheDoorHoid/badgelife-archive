---
title: DCZia Defcon32-Badge (The Ziatron)
id: dc32-dczia-defcon32-badge
layout: badge
parent: DC32
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc32
year: 2024
series: DCZia
makers:
- name: DCZia
  url: https://dczia.net
- name: snurkle engineering (hamster)
  url: https://www.tindie.com/stores/hamster/
summary: The DCZia "Ziatron" is DCZia's 2024 DEF CON 32 badge, an homage to the
  Sony Trinitron TV with a 1.9" full-color LCD, mic-reactive LEDs, and a single
  clickable knob.
functions: Light patterns, a sound-reactive "rave" mode (a knob sets microphone
  sensitivity), and raw image display from an SD card. An SSTV encode/decode
  mode was planned but not finished in time for the con.
look:
  colors: []
  shape: rectangle
  themes: []
  form_factor: pcb badge
tech:
  mcu: RP2040 (Raspberry Pi Pico W)
  leds:
    count: 18
    type: RGB
    note: up to 18 full-color LEDs
  display: 1.9" full-color LCD
  connectivity:
  - wifi
  - audio
  inputs:
  - rotary encoder
  - microphone
  battery: 3x AAA
  sao_version: null
get_one:
  price: $100.00
  price_usd: 100.0
  quantity: ''
  availability: sold_out
  availability_note: Tindie listing showed "Out of Stock" as of 2026-09-07; the maker noted it sold out around 2024-08-05.
  distribution:
  - purchase
  - free_drop
  where: Sold on Tindie by snurkle engineering ("hamster"); also offered as a free pickup at DEF CON 32, with USPS shipping available after the con for those who preordered.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/dczia/Defcon32-Badge/tree/main/Hardware
  firmware_url: https://github.com/dczia/Defcon32-Badge/tree/main/Software
  eda_tool: KiCad
  fab_url: null
  bom_url: https://github.com/dczia/Defcon32-Badge/blob/main/Hardware/DCZIA%20DC32%20BADGE%20BOM.xlsx
  notes: Repo includes KiCad schematics/PCB, a BOM spreadsheet, 3D-printed case
    STLs, and a BuildGuide.md covering assembly and firmware flashing.
links:
- label: github.com/dczia/Defcon32-Badge
  url: https://github.com/dczia/Defcon32-Badge
  kind: repo
- kind: store
  label: 2024 DCZia Badge - The Ziatron (Tindie)
  url: https://www.tindie.com/products/hamster/2024-dczia-badge-the-ziatron/
- kind: website
  label: DCZia badge history
  url: https://dczia.net
images:
- file: assets/images/badges/dc32/dczia-defcon32-badge/f4b2ba85ba.jpg
  source: "https://www.tindie.com/products/hamster/2024-dczia-badge-the-ziatron/"
  credit: "snurkle engineering (hamster)"
  caption: "The DCZia Ziatron, DEF CON 32 badge, product photo from Tindie listing"
contact: {}
notes:
- Marked as a fork of hamster/Defcon32-Badge; "hamster" is the Tindie/GitHub handle of the badge's designer at snurkle engineering.
- 'Duplicate: this is the same badge as the entry dc32-dczia-s-dumb-dc32-badge-winner-for-most-unique-name-lol
  (also "The Ziatron"), imported separately from a different sheet row. Left in
  place per instructions rather than merged; the other entry lacked the Tindie
  price/availability confirmed here ($100, sold out since ~2024-08-05).'
status: released
sources:
- kind: url
  url: https://github.com/dczia/Defcon32-Badge
  title: DCZia Defcon32-Badge
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: maker-groups); event read as ''DEF CON 32''.'
- kind: url
  url: https://github.com/dczia/Defcon32-Badge
  title: dczia/Defcon32-Badge README - GitHub
  accessed: '2026-09-07'
  note: Primary source for badge name ("The Ziatron"), specs (LCD, Pico W, LEDs, mic, speaker, batteries), features, and build guide text.
- kind: url
  url: https://www.tindie.com/products/hamster/2024-dczia-badge-the-ziatron/
  title: 2024 DCZia Badge - The Ziatron
  accessed: '2026-09-07'
  note: Confirms maker (snurkle engineering / hamster), price ($100), sold-out status, DEF CON 32 free-pickup/USPS-shipping distribution, and source of the product photo.
- kind: url
  url: https://dczia.net/about.html
  title: DCZia - About
  accessed: '2026-09-07'
  note: Background on DCZia as a badge-making crew (est. ~2013, formalized 2016), confirming it makes badges annually for DEF CON and its own ZiaCon.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Confirmed via the maker's own GitHub repo README and the Tindie storefront
    listing. This is the "DCZia Ziatron," a Raspberry Pi Pico W badge with a 1.9"
    LCD, up to 18 LEDs, a mic, and a speaker, styled as a Sony Trinitron homage.
    Sold on Tindie for $100 (sold out since ~2024-08-05) with free DEF CON 32
    pickup also offered; exact production quantity not stated anywhere found.
    This is a duplicate of entry dc32-dczia-s-dumb-dc32-badge-winner-for-most-unique-name-lol,
    which covers the same physical badge under a joking sheet title; that entry
    had price listed as an unconfirmed ~$130, while the Tindie listing found here
    gives a confirmed $100 price and sold-out date.
last_modified_date: '2026-09-07'
---

DCZia's 2024 DEF CON 32 badge, "The Ziatron," is an homage to the Sony Trinitron
television: a 1.9" full-color LCD screen sits behind a dye-sublimated, dual-PCB
front panel, backed by up to 18 full-color LEDs. A single clickable rotary
encoder is the only physical control, paired with a micro mechanical microphone
(TDK) and a small 0.3" speaker. It runs on a Raspberry Pi Pico W (RP2040 with
Wi-Fi) and is powered by three AAA batteries.

The badge's stock firmware includes several LED light patterns, a sound-reactive
"rave" mode where the encoder sets microphone sensitivity, and the ability to
display raw formatted images from an SD card. The team had planned an SSTV
(slow-scan television) encode/decode feature to match the TV theme but ran out
of time before the con. Hardware (KiCad schematics and PCB, a BOM, and
3D-printed case files) and firmware source are published on GitHub, along with
a build guide covering rotary-encoder and battery-pack assembly and firmware
flashing via the Pico's USB mass-storage bootloader.

The badge was sold on Tindie by designer "hamster" of snurkle engineering for
$100, and was also offered as a free pickup at DEF CON 32 itself, with USPS
shipping available afterward for those who preordered; the Tindie listing shows
it sold out around August 5, 2024. Production quantity is not stated in any
source found.

## Make your own

Hardware (KiCad schematics/PCB, BOM, 3D-printed case STLs) and firmware source
are in the GitHub repo. The BuildGuide.md there covers soldering the rotary
encoder and battery pack to the board, then flashing firmware by holding the
Pico's BOOTSEL button while plugging it in and dragging a `.uf2` file onto the
resulting USB mass-storage drive.
