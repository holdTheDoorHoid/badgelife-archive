---
title: The Floppy
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: sao
event: other
year: 2020
makers:
- name: Uri Shaked
  url: https://github.com/urish
summary: A 3.5"-floppy-disk-shaped SAO that plugs into a conference badge's SAO header and acts as a real 64KB EEPROM "disk" for copying apps, data, and malware between badges.
functions: Exposes a 64KB I2C EEPROM (address 0x51) as removable storage over the SAO bus, usable as a FAT, TAR, or ZIP filesystem (about 47KB usable). A separate 256-byte auxiliary EEPROM stores Badge Add-on ID metadata describing the storage format and layout. Through-hole and full-size variants add an LED that blinks on I2C bus activity, and all variants can be hardware write-protected via solder bridges.
look:
  colors: []
  shape: floppy disk
  themes:
  - retro computer
  - hardware tool
tech:
  mcu: none
  leds:
    count: 1
    type: discrete
    note: Red 0805 LED, I2C bus activity indicator; present on the through-hole and full-size flavors only (not the SMD flavor).
  display: null
  connectivity:
  - i2c
  battery: null
  sao_version: v1.69bis
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: yes
  hardware_url: https://github.com/urish/floppy-disk-sao
  firmware_url: null
  eda_tool: null
  license: MIT
  notes: Repo includes schematics (KiCad-style .sch files), BOM, and PCB variants (through-hole, SMD, full-size 3.5"). No dedicated firmware, since it is a passive EEPROM add-on read by the host badge's own code.
links:
- label: github.com/urish/floppy-disk-sao
  url: https://github.com/urish/floppy-disk-sao
  kind: repo
- label: AraMCon badge floppy driver (aramcon-firmware)
  url: https://github.com/aramcon-badge/aramcon-firmware/blob/master/drivers/floppy.py
  kind: repo
images:
  - file: assets/images/badges/other/floppy-disk-sao/edc4451330.jpg
    source: "https://github.com/urish/floppy-disk-sao"
    credit: "Uri Shaked"
    caption: "Multiple assembled Floppy SAO units"
  - file: assets/images/badges/other/floppy-disk-sao/2af63bebc7.jpg
    source: "https://github.com/urish/floppy-disk-sao"
    credit: "Uri Shaked"
    caption: "Through-hole Floppy SAO showing the write-protect solder bridges"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/urish/floppy-disk-sao
  title: floppy-disk-sao
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://raw.githubusercontent.com/urish/floppy-disk-sao/master/README.md
  title: 'The Floppy — README'
  accessed: '2026-09-07'
  note: Full description, storage layout, BOM, license (MIT, copyright 2020), and image URLs.
- kind: url
  url: https://github.com/aramcon-badge/aramcon-firmware/blob/master/drivers/floppy.py
  title: 'aramcon-firmware: drivers/floppy.py'
  accessed: '2026-09-07'
  note: Driver file header reads "AramCon Badge Floppy Driver", copyright 2020, by Uri Shaked; ties the SAO to the AraMCon badge ecosystem.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Made by Uri Shaked (urish), the designer of the AraMCon badges (a private
    tech event in Israel) and of the "Badge Add-on ID" standard used by this
    SAO's metadata EEPROM. The repo itself is not tied to a specific
    convention in its own text, but the companion driver lives in the
    aramcon-badge/aramcon-firmware repo with a 2020 copyright, so this was
    most likely made for an AraMCon badge (2020 era). No AraMCon event exists
    in this archive's events.yml, so event is left as "other"; if one is
    added later this entry should move to it. Price, quantity made, and
    availability/sale channel were not stated anywhere found and are left
    empty. No SAO connector pin-out beyond "6-pin IDC" was specified as v1 vs
    v1.69bis, so sao_version is a best guess based on the 6-pin IDC connector
    described in the BOM (matches the SAO v1.69bis/v2 6-pin pinout, but
    labeled v1.69bis (6-pin) based on the BOM's "6-pin IDC" connector.
    Title changed from the sheet's slug-like "floppy-disk-sao" to "The
    Floppy", the name used in the project's own README.
last_modified_date: '2026-09-07'
---

The Floppy is a "Shitty Add-on" (SAO) built by Israeli engineer Uri Shaked (urish) in the shape of a 3.5" floppy disk. Rather than being purely decorative, it is a working I2C EEPROM module: a 64KB M24512 EEPROM sits behind the SAO's I2C bus, addressable as a small removable disk that can be formatted FAT, TAR, or ZIP and used to carry roughly 47KB of files, apps, or (as the README puts it) malware between badges at an event. A second, smaller 256-byte EEPROM stores metadata in Shaked's own "Badge Add-on ID" format, telling a host badge how the main EEPROM is laid out so it can be mounted automatically.

The project ships as three PCB variants — through-hole and SMD versions sized like a normal SAO, plus a full-size 3.5" version that actually looks like a floppy disk — and the through-hole and full-size boards add a red activity LED and physical write-protect solder bridges, echoing the write-protect notch of a real floppy. All of it is open source under the MIT license, with schematics and a BOM published in the GitHub repo.

The clearest tie to a specific event is a driver file in the aramcon-badge/aramcon-firmware repository, copyrighted 2020 by Uri Shaked, who separately designed the AraMCon badge (AraMCon is a small private tech event in Israel). That suggests The Floppy was built as an add-on for an AraMCon badge around 2020, though the SAO's own repository doesn't name a specific convention or year, and no price, production quantity, or sale/giveaway details were found.
