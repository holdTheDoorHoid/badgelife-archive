---
title: The GAT Stand - Badge Addon Holder
id: supercon-2024-the-gat-stand-badge-addon-holder
layout: badge
parent: Supercon 2024
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: supercon-2024
year: 2024
makers:
- name: trueControl
  url: https://hackaday.io/true
summary: 'A powered, daisy-chainable acrylic desk stand for displaying GAT/badge addons off the badge itself.'
functions: 'Holds and powers a badge addon on a desk. Supplies the addon over its GAT port, passes USB-C power downstream to a chained unit, has a soft power button with memory, and an ambient-light option to auto power on/off.'
look:
  colors: []
  shape: null
  themes:
  - hardware tool
tech:
  mcu: WCH CH32V203C8T6
  leds: null
  display: none
  connectivity:
  - usb
  battery: 'CR1220 (clock/memory battery; unit itself is USB-C powered)'
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: 'approximately 100'
  availability: limited
  distribution:
  - kit
  - swap
  where: 'Given to attendees at Hackaday Supercon 8 (Nov 2024) as partial-assembly
    kits, with some fully-assembled units given to addon makers; some attendees
    also traded/bartered for them. The maker mentioned plans to later sell assembled
    and kit versions, but no storefront listing was found.'
make_your_own:
  open_source: yes
  hardware_url: https://git.trueserve.org/trueControl/sc8-gat-stand/src/branch/master/hardware
  firmware_url: https://git.trueserve.org/trueControl/sc8-gat-stand/src/branch/master/gat_stand_fw
  eda_tool: null
links:
- label: hackaday.io/project/198570-the-gat-stand-badge-addon-holder
  url: https://hackaday.io/project/198570-the-gat-stand-badge-addon-holder
  kind: hackaday
- label: git.trueserve.org/trueControl/sc8-gat-stand
  url: https://git.trueserve.org/trueControl/sc8-gat-stand
  kind: repo
- label: basic.truecontrol.org (project index)
  url: https://basic.truecontrol.org/database/
  kind: website
images:
  - file: assets/images/badges/supercon-2024/the-gat-stand-badge-addon-holder/9a76484458.jpg
    source: "https://hackaday.io/project/198570-the-gat-stand-badge-addon-holder"
    credit: "trueControl (true)"
    caption: "The GAT Stand, an acrylic-panel desk stand for badge addons"
  - file: assets/images/badges/supercon-2024/the-gat-stand-badge-addon-holder/9b21bb92f9.jpg
    source: "https://hackaday.io/project/198570-the-gat-stand-badge-addon-holder"
    credit: "trueControl (true)"
    caption: "GAT Stand with a badge addon mounted, showing the Type-C daisy-chain port"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 3).
- 'Repo is named "sc8-gat-stand" (sc8 = Hackaday Supercon 8, 2024); the maker''s log also
  says planned future features "may implement at Supercon 8," confirming the event.'
- 'GAT is trueControl''s own badge-addon connector standard (used across their Supercon/DEF
  CON addon boards), distinct from the community SAO v1/v1.69bis header, so sao_version is
  left null.'
status: released
sources:
- kind: url
  url: https://hackaday.io/project/198570-the-gat-stand-badge-addon-holder
  title: The GAT Stand - Badge Addon Holder
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run3-spotted); event read as ''unknown''.'
- kind: url
  url: https://hackaday.io/project/198570-the-gat-stand-badge-addon-holder
  title: The GAT Stand - Badge Addon Holder (project details, files, components)
  accessed: '2026-09-07'
  note: 'Maker''s own description, feature list, schematic file, and BOM (WCH CH32V203C8T6 MCU, CR1220 coin cell); confirms Supercon 8 context and images. Fact-check pass (2026-09-07) re-read the build log and found it states roughly 100 units were built and distributed to attendees at Supercon 8 as partial-assembly kits (some fully assembled units went to addon makers, some were traded/bartered), with a stated intent to sell assembled/kit versions afterward -- corrects the earlier "one-off/personal build" characterization.'
- kind: url
  url: https://git.trueserve.org/trueControl/sc8-gat-stand
  title: trueControl/sc8-gat-stand - trueserve Git
  accessed: '2026-09-07'
  note: 'Repo name and folder layout (hardware/, gat_stand_fw/, binaries/20241114) confirm this was built for Supercon 8 (Nov 2024); hardware folder holds schematic PDF, a STEP file for the 3D-printed holder (REV3d), and a Lightburn (.lbrn2) file for the acrylic panel (laser-cut, not CNC/printed).'
research:
  status: verified
  confidence: medium
  last_checked: '2026-09-07'
  notes: >-
    Maker's own Hackaday.io project page and git repo confirm what the device is, its
    hardware (WCH CH32V203C8T6 MCU, CR1220 backup cell, USB-C powered with switchable
    daisy-chain output, acrylic panel + 3D-printed base), and that it was built for
    Hackaday Supercon 8 (Nov 2024), hence event corrected from "other" to supercon-2024.
    Fact-check pass (2026-09-07) re-read every cited source: confirmed the maker's
    build log ("I think I got roughly 100 boards done for supercon") gives a quantity
    and distribution the earlier pass missed -- roughly 100 units were built and
    handed out at Supercon 8 as partial-assembly kits (some assembled units went to
    addon makers, some were traded/bartered by attendees), with the maker saying they
    planned to sell assembled/kit versions afterward. No completed storefront listing
    or price was found anywhere (trueControl's Tindie/shop.truecontrol.org has other
    GAT-compatible addons but no GAT Stand product page), so price/price_usd stay
    empty and availability is set to "limited" rather than "unknown." The repo's
    hardware/ and gat_stand_fw/ folders both contain real source (schematic PDF, STEP
    file, Lightburn cut file; C firmware source tree), so make_your_own.open_source is
    "yes" per the guide's literal definition, though no license or BOM/build
    instructions file was found in the repo. GAT is trueControl's proprietary
    addon-connector standard, not the community SAO v1/v1.69bis pinout, so
    tech.sao_version is left null rather than guessed. No LED count, colorway, or
    exact form factor dimensions were stated (the addon-facing photo shows a single
    status LED, but no spec for it was given). eda_tool for the acrylic panel could
    not be determined beyond "Lightburn file" (a laser-cutter tool, not a PCB EDA
    tool), so left null. Both images verified against the Hackaday gallery and show
    the actual device.
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/the-gat-stand-badge-addon-holder/
---

The GAT Stand is a small desk accessory built by the hardware maker trueControl (username "true" on Hackaday.io) to hold and power a badge addon off of its host badge, so it can sit on a desk rather than dangling from a lanyard. It plugs in over USB-C and feeds the addon through trueControl's own GAT connector at up to 250 mA sustained (400 mA peak), while a second, switchable Type-C port lets a second stand be daisy-chained downstream off the same USB source (up to 1.5 A total). A soft power button controls the addon port and the downstream port independently, an optional ambient-light sensor can turn the stand on and off automatically with room lighting, and a CR1220 coin cell keeps the power state remembered across a physical power cycle. The enclosure is a slim laser-cut acrylic panel on a 3D-printed base; the electronics run on a WCH CH32V203C8T6 RISC-V microcontroller.

The project's repository, `sc8-gat-stand` on trueControl's self-hosted git, and the maker's own build log ("may implement at Supercon 8") place it squarely at Hackaday Supercon 8 in Pasadena, CA (November 2024) -- the entry's event has been corrected from "other" to `supercon-2024` on that basis. Files in the repo include a REV4 schematic PDF, a STEP file for the printed base (REV3d), and a Lightburn (.lbrn2) cut file for the acrylic panel, alongside the CH32V20x firmware source, so the hardware and firmware are both published, though no BOM, license, or build instructions file was found in the repo. The maker's build log says roughly 100 units were assembled for the conference and handed out to attendees as partial-assembly kits, with some fully-assembled units going to fellow addon makers and some traded or bartered between attendees; the maker mentioned plans to sell assembled and kit versions afterward, but no storefront listing, price, or completed sale could be found.

## Make your own

Hardware files (schematic PDF, 3D-printed base STEP file, laser-cut acrylic panel Lightburn file) are in the `hardware/` folder of the [sc8-gat-stand repo](https://git.trueserve.org/trueControl/sc8-gat-stand/src/branch/master/hardware); firmware source for the WCH CH32V203C8T6 is in `gat_stand_fw/`. No assembly instructions, BOM, or license file were found in the repo, so treat this as reference material rather than a turnkey build.
