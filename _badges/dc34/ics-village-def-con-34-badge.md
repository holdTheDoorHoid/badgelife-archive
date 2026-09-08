---
title: ICS Village DEF CON 34 Badge
id: dc34-ics-village-def-con-34-badge
layout: badge
parent: DC34
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: dc34
year: 2026
makers:
- name: FreeWili
  url: https://freewili.com/
summary: A handheld multi-protocol field instrument built by FreeWili for the DEF CON 34 ICS Village, aimed at OT, ICS and automotive security researchers.
functions: Provides hands-on interfaces for RS485/Modbus RTU, CAN/CAN FD, and both 10BASE-T1S and 10BASE-T1L single-pair Ethernet, with an onboard OLED and rotary encoders for on-device control and an SD slot for logging, so a researcher can probe industrial and automotive networks untethered from a laptop.
look:
  colors:
  - blue
  - clear
  - black
  shape: rectangle
  themes:
  - security
  - hardware tool
  - radio
tech:
  mcu: RP2350B-A4
  leds:
    count: 4
    type: RGB
    note: 4 programmable RGB LEDs
  display: I2C OLED
  connectivity:
  - uart
  - usb
  battery: 3.7V LiPo, 1000mAh
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: limited
  distribution:
  - village
  where: Available on-site at the ICS Village or Vendor Village at DEF CON 34 (Aug 6-9, 2026, Las Vegas), while supplies lasted.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/freewili/freewili-firmware
  eda_tool: null
links:
- label: freewili.com/ics-village-defcon-34-badge.html
  url: https://freewili.com/ics-village-defcon-34-badge.html
  kind: website
- label: freewili/freewili-firmware (GitHub)
  url: https://github.com/freewili/freewili-firmware
  kind: repo
- label: FreeWili on LinkedIn - DEF CON 34 ICS Village badge reveal
  url: https://www.linkedin.com/posts/freewili_2026-ics-village-def-con-34-badge-activity-7489365809040130048-22g3
  kind: social
images:
  - file: assets/images/badges/dc34/ics-village-def-con-34-badge/914d07a714.png
    source: "https://freewili.com/ics-village-defcon-34-badge.html"
    credit: "FreeWili"
    caption: "ICS Village DEF CON 34 badge, front view"
  - file: assets/images/badges/dc34/ics-village-def-con-34-badge/c479fe8b94.jpg
    source: "https://freewili.com/ics-village-defcon-34-badge.html"
    credit: "FreeWili"
    caption: "ICS Village DEF CON 34 badge, end view showing DB15 connector"
contact: {}
notes:
- Spotted by a research agent while working on a neighbouring entry (run 4).
- Sheet listed connectivity/RS485/CAN/single-pair Ethernet details are marketing terms for physical-layer interfaces the badge exposes; the `tech.connectivity` controlled vocabulary has no entries for CAN or single-pair Ethernet, so only uart/usb are recorded there. See summary/functions for the full protocol list.
status: listed
sources:
- kind: url
  url: https://freewili.com/ics-village-defcon-34-badge.html
  title: ICS Village DEF CON 34 Badge
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: research-run4-spotted); event read as ''dc34''.'
- kind: url
  url: https://freewili.com/ics-village-defcon-34-badge.html
  title: ICS Village DEF CON 34 Badge — FREE-WiLi
  accessed: '2026-09-08'
  note: Primary source; confirmed maker, MCU, display, LEDs, connectivity, battery, distribution and images.
- kind: url
  url: https://icsvillage.com/defcon-34
  title: DEF CON 34 Schedule | ICS Village
  accessed: '2026-09-08'
  note: Confirms DEF CON 34 dates (Aug 6-9, 2026, Las Vegas) and that ICS Village ran there.
- kind: url
  url: https://www.linkedin.com/posts/freewili_2026-ics-village-def-con-34-badge-activity-7489365809040130048-22g3
  title: DEF CON 34 ICS VILLAGE Field Instrument Badge - LinkedIn
  accessed: '2026-09-08'
  note: FreeWili's own announcement post, corroborates protocol feature list.
- kind: url
  url: https://github.com/freewili/freewili-firmware
  title: freewili/freewili-firmware
  accessed: '2026-09-08'
  note: Firmware repository for the FreeWili platform this badge runs on; no separate hardware/gerbers repo found, so open_source is marked partial.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: Maker's own product page plus FreeWili's LinkedIn/Instagram announcements and the ICS Village DEF CON 34 schedule page all corroborate the item, event and feature list. Price and quantity made were not published anywhere found. Could not confirm whether the hardware design (schematics/gerbers) is published, only the firmware repo; open_source recorded as partial. No exact "SAO" claim was made anywhere - this is a standalone battery-powered badge, not an SAO plug-in, so sao_version is set to none.
last_modified_date: '2026-09-08'
---

The ICS Village DEF CON 34 Badge is a handheld field instrument built by FreeWili for the ICS Village at DEF CON 34, aimed at operational technology (OT), industrial control systems (ICS), and automotive security researchers rather than casual attendees. Housed in a clear molded case around a blue PCB, it runs on an RP2350B-A4 microcontroller and exposes an I2C OLED display, four rotary encoders, four programmable RGB LEDs, and an SD card slot, all powered by an onboard 3.7V/1000mAh LiPo battery for untethered use in the field.

Its headline feature set is the protocol coverage it packs into one pocket-sized device: RS485/Modbus RTU, CAN and CAN FD, and both 10BASE-T1S and 10BASE-T1L single-pair Ethernet, alongside USB-C. FreeWili's own materials describe it less as a conference badge and more as a "field instrument" for auditing industrial and automotive networks on-site.

It was distributed on-site at the ICS Village and Vendor Village at DEF CON 34 (August 6-9, 2026, Las Vegas) while supplies lasted; no price or total quantity made was published in any source found. The badge runs FreeWili's firmware platform (freewili-firmware on GitHub), but no hardware design files (schematics or Gerbers) specific to this badge were located, so its openness is only partially confirmed.
