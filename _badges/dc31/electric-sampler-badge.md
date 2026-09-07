---
title: Electric Sampler
id: dc31-electric-sampler-badge
layout: badge
parent: DC31
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc31
year: 2023
makers:
- name: DC Zia
  url: https://dczia.net/
summary: A eurorack-format sampler, step sequencer, and MIDI controller badge built around a Raspberry Pi 2040, made to keep working as a small music instrument after the con is over.
functions: 'Multiple modes selected with a rotary encoder and OLED screen: an LED light mode; a sampler mode that loads WAV files from onboard flash and plays them through an 8-key step sequencer with per-step volume; a pre-programmed sequencer mode; a MIDI controller mode (notes/CC editable in the accompanying Python code); and a USB HID keyboard mode where the 8 keys emit digits 0-9.'
look:
  colors:
  - pink
  - multicolor
  shape: rectangle
  themes:
  - music
  - synthwave
  - hardware tool
tech:
  mcu: RP2040
  leds:
    count: null
    type: null
    note: 8 backlit sequence keys (Cherry MX yellow mechanical switches)
  display: 128x32 OLED
  connectivity:
  - usb
  - midi
  battery: external battery pack (soldered on by the builder)
  sao_version: null
get_one:
  price: $110
  price_usd: 110
  quantity: ''
  availability: sold_out
  distribution:
  - purchase
  where: 'Boards (v1.1) were handed out at DEF CON 31 in 2023 partially assembled: surface-mount components came populated, and builders soldered on the keyswitches, audio jacks, screen, rotary encoders, and battery leads themselves. No price or quantity is stated in the maker''s materials.'
  availability_note: Listed sold out on Tindie as of Sep 25, 2023; checked 2026-09-07.
make_your_own:
  open_source: 'yes'
  hardware_url: https://github.com/dczia/Defcon31-Badge/tree/main/Hardware
  firmware_url: https://github.com/dczia/Defcon31-Badge/tree/main/Firmware
  eda_tool: KiCad
  fab_url: null
  bom_url: https://github.com/dczia/Defcon31-Badge/blob/main/Hardware/Final/DCZIA%20DC31%20BADGE%20BOM.xlsx
  license: null
  notes: No LICENSE file found in the repo; hardware (KiCad schematics/PCB, STEP models, BOM) and firmware/software are published but terms aren't stated.
links:
- kind: repo
  label: dczia/Defcon31-Badge on GitHub
  url: https://github.com/dczia/Defcon31-Badge
- kind: website
  label: DC Zia
  url: https://dczia.net/
- kind: article
  label: 'Hackaday: Nostalgic 30-in-ONE Electronics Badge For DEF CON 30 (background on DC Zia)'
  url: https://hackaday.com/2022/12/09/nostalgic-30-in-one-electronics-badge-for-def-con-30/
- label: 'Tindie: DCZia Electric Sampler'
  url: https://www.tindie.com/products/hamster/dczia-electric-sampler/
  kind: store
  archived: https://web.archive.org/web/20260503115706/https://www.tindie.com/products/hamster/dczia-electric-sampler/
- label: 'Tindie: DCZia DEF CON 31 updated front panel'
  url: https://www.tindie.com/products/hamster/dczia-defcon-31-updated-front-panel/
  kind: store
  archived: https://web.archive.org/web/20260503133125/https://www.tindie.com/products/hamster/dczia-defcon-31-updated-front-panel/
images:
- file: assets/images/badges/dc31/electric-sampler-badge/68980a56f4.jpg
  source: https://dczia.net/
  credit: DC Zia
  caption: The Electric Sampler badge, DC Zia's DEF CON 31 (2023) eurorack-format sampler/sequencer badge
- file: assets/images/badges/dc31/electric-sampler-badge/7f5ceab44c.jpg
  source: https://www.tindie.com/products/hamster/dczia-electric-sampler/
  credit: snurkle engineering / DCZia
  caption: DCZia Electric Sampler badge, assembled
  archived: https://web.archive.org/web/20260503115706/https://www.tindie.com/products/hamster/dczia-electric-sampler/
- file: assets/images/badges/dc31/electric-sampler-badge/9e2b3beb0b.jpg
  source: https://www.tindie.com/products/hamster/dczia-electric-sampler/
  credit: snurkle engineering / DCZia
  caption: DCZia Electric Sampler badge, alternate view
  archived: https://web.archive.org/web/20260503115706/https://www.tindie.com/products/hamster/dczia-electric-sampler/
contact: {}
notes:
- Sheet listed this only as "Electric Sampler badge?" with maker "DCZIA" and no other details; title confirmed and details filled in from the maker's own GitHub repo and website.
- Duplicate of dc31-electric-sampler-badge, which already has a fuller writeup; this entry adds the price, sold-out status, and Tindie storefront/photos that the other entry lacked.
status: released
sources:
- kind: sheet
  event: dc31
  row: 36
  updated: '2023-07-28'
- kind: url
  url: https://github.com/dczia/Defcon31-Badge
  title: dczia/Defcon31-Badge - DCZia DC31 Badge
  accessed: '2026-09-06'
  note: Primary source for specs, README/build guide, hardware files (KiCad, BOM), and firmware/software organization.
- kind: url
  url: https://dczia.net/
  title: DC Zia - Badge Creators
  accessed: '2026-09-06'
  note: Confirmed the Electric Sampler is DC Zia's 2023/DEF CON 31 badge, its one-paragraph description, and the source photo.
- kind: url
  url: https://hackaday.com/2022/12/09/nostalgic-30-in-one-electronics-badge-for-def-con-30/
  title: Nostalgic 30-in-ONE Electronics Badge For DEF CON 30
  accessed: '2026-09-06'
  note: Background on DC Zia as a group and led to their GitHub org/website (used to find the DC31 badge, since this article itself covers DC30).
- kind: url
  url: https://www.tindie.com/products/hamster/dczia-electric-sampler/
  title: DCZia Electric Sampler - snurkle engineering
  accessed: '2026-09-07'
  note: Price ($110), sold-out status (since Sep 25, 2023), maker/seller identity, feature list, and product photos.
  archived: https://web.archive.org/web/20260503115706/https://www.tindie.com/products/hamster/dczia-electric-sampler/
- kind: url
  url: https://dczia.net/about.html
  title: About DCZia
  accessed: '2026-09-07'
  note: Confirms DCZia as a group formed around DEF CON 22 with New Mexico roots, and lists Electric Sampler as their DEF CON 31 (2023) badge.
  archived: https://web.archive.org/web/20260514012540/https://dczia.net/about.html
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-06'
  notes: No price, quantity made, or open-source license terms are stated anywhere in the maker's repo or website, so those fields are left empty rather than guessed. Web search was unavailable for this run (session search budget exhausted); research relied on WebFetch against DuckDuckGo/Bing/Hackaday plus GitHub's API, so coverage of secondary press/social mentions (e.g. the "teasers on Twitter" noted on the original sheet) is thinner than usual. LED count/type not found (not itemized in the README; the BOM spreadsheet was not opened). Merged with duplicate entry 'Electric Sampler (DCZia)' (dc31-badge-dczia).
last_modified_date: '2026-09-07'
redirect_from:
- /badges/dc31/badge-dczia/
---

DC Zia is a New-Mexico-rooted hacker collective that has built an independent DEF CON badge nearly every year since around DEF CON 22. For DEF CON 31 in 2023 they moved away from the retro "learn electronics" format of their 2022 30-in-One badge and built the Electric Sampler: a Raspberry Pi RP2040-powered badge shaped around Eurorack modular-synth conventions, with a 3.5mm audio output, 3.5mm MIDI in/out, 3.5mm sync in/out, a microSD slot, and a Eurorack power connector, alongside a 128x32 OLED screen, two rotary encoders, and eight key switches.

The badge is explicitly designed to outlive the con: past its DEF CON 31 debut it works as a small standalone instrument, with firmware modes for an LED light show, a WAV-sample step sequencer with per-step volume control, a pre-programmed sequencer, a MIDI controller, and a USB HID keyboard mode. Units handed out at the con (v1.1 boards) arrived with surface-mount parts pre-assembled; attendees hand-soldered the audio jacks, keyswitches, screen, encoders, and battery leads themselves, and were pointed to updated firmware since the boards shipped with test firmware only.

## Make your own

Hardware (KiCad schematics and PCB files, STEP models for mechanical parts, and a bill of materials) and firmware/software are published in DC Zia's `Defcon31-Badge` GitHub repository, though no license file accompanies them. Firmware can be re-flashed by holding the RP2040's BOOTSEL button while powering the unit over micro-USB to expose it as a mass-storage drive, then dragging on the released `.uf2` file (or the contents of the repo's `Production/Software` folder).

## Notes merged from the duplicate entry "Electric Sampler (DCZia)"

The Electric Sampler is DCZia's badge for DEF CON 31 (2023): a Raspberry Pi RP2040-powered, Eurorack-format drum machine, sampler, and step sequencer with a full-color dye-sublimated PCB front panel. It has a small OLED screen, two rotary encoders, eight backlit Cherry MX-switch sequence keys, 3.5mm audio out, 3.5mm MIDI in/out, 3.5mm sync in/out, a microSD card slot, an SAO port, and both battery power (with a built-in speaker) and a Eurorack power connector, so it keeps working as a small instrument after the con.

It was sold through DCZia member Snurkle Engineering's Tindie store for $110, either as a mostly-assembled kit (surface-mount parts pre-populated, buyer solders on switches, jacks, screen, encoders, and battery) or fully built for an added fee, with an optional 16-character custom text option; it was also handed out at DEF CON 31 itself. The listing sold out by September 25, 2023. Hardware (KiCad schematics/PCB, STEP models, BOM) and firmware are published on GitHub, though no license file is included.

This entry duplicates `dc31-electric-sampler-badge`, which covers the same badge in more depth on functions and the build guide; this one adds the confirmed retail price, sold-out status, and Tindie photos.
