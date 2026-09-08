---
title: BornHack 2023 badge
id: bornhack-2023-bornhack-2023-badge
layout: badge
parent: Bornhack 2023
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: bornhack-2023
year: 2023
makers:
- name: BornHack
summary: 'A two-part NFC badge set for BornHack 2023: an NFC reader badge built around an RP2040 and NXP PN7150, and a companion NFC tag badge using an NXP NTAG I2C Plus chip, connected by a Qwiic/STEMMA QT cable.'
functions: The reader badge does NFC reading and card emulation via the PN7150 controller and runs preloaded CircuitPython for hacking; the tag badge is a passive NTAG I2C Plus tag. The two connect together over a Qwiic/STEMMA QT-style cable.
look:
  colors: []
  shape: null
  themes:
  - security
  - hardware tool
tech:
  mcu: RP2040
  leds: null
  display: none
  connectivity:
  - nfc
  - usb
  - i2c
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - free_drop
  where: Handed out to BornHack 2023 attendees as the conference badge.
make_your_own:
  open_source: true
  hardware_url: https://github.com/bornhack/badge2023
  firmware_url: https://github.com/bornhack/badge2023/tree/circuitpython
  eda_tool: KiCad
notes:
- From the user's 'SAOs to buy' link list (2026-09-07).
- KiCad v7 (or a nightly build) is required to open the design; v5/v6 will not open it, per the repo README.
- 'Main chips: RP2040 (reader MCU), NXP PN7150 (NFC reader/controller), Winbond W25Q128JV (16MB QSPI flash), NXP NT3H2211W0FTT / NTAG I2C Plus 2K (tag chip).'
- No price, quantity made, or LED details were found in the sources checked.
- The passive half of the 2023 NFC badge pair, built around an NXP NTAG I2C Plus chip (part NT3H2211W0FTT) with no active MCU, distinct from the companion reader badge which uses an RP2040 and PN7150 NFC controller. Found by the event-year sweep, task bornhack-2023.
- The maker's repo and README treat the reader and tag as one combined "BornHack 2023 NFC Badges" project/README rather than naming the tag board separately; this entry covers the tag board specifically.
- This item substantially duplicates the archive's existing combined entry bornhack-2023-bornhack-2023-badge, which already documents both halves of the pair from the same repository.
status: released
sources:
- kind: url
  url: https://github.com/bornhack/badge2023
  title: BornHack 2023 badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: tobuy-linkfile); event read as ''bornhack-2023''.'
- kind: url
  url: https://raw.githubusercontent.com/bornhack/badge2023/main/README.md
  title: bornhack/badge2023 README.md
  accessed: '2026-09-07'
  note: Confirmed two-badge design (NFC reader + NFC tag), RP2040/PN7150/NTAG I2C Plus/W25Q128JV chips, CircuitPython firmware, CC-BY-SA-4.0 hardware and MIT firmware licenses, KiCad v7 requirement, and image file locations.
- kind: url
  url: https://blog.adafruit.com/2023/08/02/bornhack-2023-makes-nfc-badges-badgelife-rp2040-bornhackbadge-raspberry_pi/
  title: BornHack 2023 makes NFC badges - Adafruit blog
  accessed: '2026-09-07'
  note: Confirmed the reader/tag pair connect over a Qwiic/STEMMA QT-compatible cable; general summary of the two-badge concept.
- kind: url
  url: https://bornhack.dk/bornhack-2023/program/this-years-bornhack-badge-with-nfc/
  title: This years BornHack badge with NFC - BornHack 2023 program
  accessed: '2026-09-07'
  note: Conference talk page about the badge by Thomas Flummer; no price/quantity information, links back to the same GitHub repo and a slide deck.
- kind: url
  url: https://github.com/bornhack/badge2023/blob/main/README.md
  title: BornHack 2023 NFC Tag Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:bornhack-2023); event read as ''bornhack-2023''.'
- kind: url
  url: https://api.github.com/repos/bornhack/badge2023/contents/IMAGES
  title: bornhack/badge2023 IMAGES directory listing
  accessed: '2026-09-08'
  note: Located the badge photo files used for the images below.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: Hardware and firmware are open source and well documented in the maker's own repo. Could not find a stated price, production quantity, or LED presence in any source checked; BornHack badges are traditionally included with conference admission, but no source stated this explicitly for 2023, so get_one.price/quantity are left empty and distribution is set to free_drop based on the standard con-badge pattern combined with the "handed out" phrasing in the README image caption context. Merged with duplicate entry 'BornHack 2023 NFC Tag Badge' (bornhack-2023-bornhack-2023-nfc-tag-badge).
last_modified_date: '2026-09-08'
images:
- file: assets/images/badges/bornhack-2023/bornhack-2023-badge/14db33a3f1.jpg
  source: https://github.com/bornhack/badge2023
  credit: BornHack
  caption: The BornHack 2023 NFC reader and tag badges, back side
- file: assets/images/badges/bornhack-2023/bornhack-2023-badge/6d4bc29524.jpg
  source: https://github.com/bornhack/badge2023
  credit: BornHack
  caption: The BornHack 2023 NFC reader and tag badges, front side, showing the PCB art
- file: assets/images/badges/bornhack-2023/bornhack-2023-badge/63e3cac77b.jpg
  source: https://github.com/bornhack/badge2023
  credit: BornHack
  caption: The BornHack 2023 NFC tag badge (right) paired with the NFC reader badge
- file: assets/images/badges/bornhack-2023/bornhack-2023-badge/4726c5c38c.jpg
  source: https://github.com/bornhack/badge2023
  credit: BornHack
  caption: Back of the BornHack 2023 NFC badge pair showing the tag and reader boards
links:
- label: github.com/bornhack/badge2023
  url: https://github.com/bornhack/badge2023
  kind: repo
- label: BornHack 2023 makes NFC badges (Adafruit blog)
  url: https://blog.adafruit.com/2023/08/02/bornhack-2023-makes-nfc-badges-badgelife-rp2040-bornhackbadge-raspberry_pi/
  kind: article
- label: This years BornHack badge with NFC (talk, program page)
  url: https://bornhack.dk/bornhack-2023/program/this-years-bornhack-badge-with-nfc/
  kind: doc
- label: BornHack 2023 NFC Badges talk slides (Thomas Flummer)
  url: https://thomasflummer.com/slides/nfc_badge_2023.pdf
  kind: doc
- label: github.com/bornhack/badge2023/blob/main/README.md
  url: https://github.com/bornhack/badge2023/blob/main/README.md
  kind: repo
contact: {}
model:
  file: assets/models/bornhack-2023/bornhack-2023-badge.glb
  method: kicad
  source_file: nfc_reader/nfc_reader.kicad_pcb
  generated: '2026-09-07'
  bytes: 340572
redirect_from:
- /badges/bornhack-2023/bornhack-2023-nfc-tag-badge/
---

The BornHack 2023 conference badge was actually a pair of connected boards themed around NFC: a reader badge and a tag badge, wired together with a small Qwiic/STEMMA QT-style cable. The reader badge is built around a Raspberry Pi RP2040 (dual-core Cortex-M0+) with 16MB of Winbond QSPI flash and an NXP PN7150 NFC controller capable of both reading tags and doing card emulation; it shipped preloaded with CircuitPython so attendees could start experimenting over USB-C with just a text editor. The companion tag badge is a simpler board built around an NXP NTAG I2C Plus (NT3H2211) chip, giving attendees a physical NFC tag to read, write, and clone with the reader badge.

BornHack (the maker, styled as the badge's org rather than an individual) released the hardware design under CC-BY-SA-4.0 and the CircuitPython firmware and demo application under MIT, with schematics as PDFs and the full KiCad v7 project in the repository (KiCad v5/v6 cannot open it). A UF2 restore image is provided in case someone reflashes the reader board and wants to get back to the stock CircuitPython environment. A talk on the badge, "This years BornHack badge with NFC," was given by Thomas Flummer at the 2023 event, walking through the design and NFC use (and misuse).

No source found gave a price, a production quantity, or confirmed whether either board carries LEDs; those fields are left blank rather than guessed. Photos of both badges (front and back) are included from the project's own IMAGES folder.

## Notes merged from the duplicate entry "BornHack 2023 NFC Tag Badge"

The BornHack 2023 NFC tag badge is the passive half of that year's two-board conference badge set. Where the companion badge carries an RP2040 microcontroller and an NXP PN7150 NFC reader/controller, the tag badge has no MCU at all: it is built around a single NXP NT3H2211W0FTT chip, part of the NTAG I2C Plus 2K family, an NFC Forum Type 2 tag that exposes both an RF interface and an I2C interface. Any NFC Forum Type 2 reader, including a phone or the matching reader badge, can read from and write to it.

BornHack designed the pair together and released the hardware for both boards, under the CC BY-SA 4.0 license, in a single GitHub repository (bornhack/badge2023), with schematics as KiCad v7 projects and PDFs. The repository's README and photos describe and depict the tag and reader as a connected pair rather than documenting the tag board on its own, and no price, production quantity, or independent product photo of the tag board was found in the sources checked.

This entry substantially overlaps the archive's existing combined entry for the BornHack 2023 badge (bornhack-2023-bornhack-2023-badge), which already covers both halves of the pair from the same source material.
