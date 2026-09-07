---
title: Ph0xx Bot Jewel
id: fri3d-2018-fri3d-2018-ph0xx-bot-jewel
layout: badge
parent: Fri3d 2018
grand_parent: Badge Archive
nav_exclude: true
type: accessory
event: fri3d-2018
year: 2018
makers:
- name: Fri3d Camp
  url: https://github.com/Fri3dCamp
- name: Wim Van Gool
  url: https://hackaday.io/wim-van-gool
summary: Expansion board (Jewel) for the Ph0xx badge that boosts power to drive four large servos, used as the building block of the Fri3d Camp 2018 bipedal robot kit; the Fri3dBadge library includes servo support for it.
functions: Powers and drives up to four servo motors (ankle and hip joints of a bipedal "Otto"-style robot); charges and boosts a lithium cell to a regulated 5V rail for the servos; controlled from the Fri3d badge via the Fri3dServoJewel library (OneServo / TwoServos examples).
look:
  colors: []
  shape: null
  themes:
  - robot
  - kit
tech:
  mcu: none
  leds: null
  display: null
  connectivity: []
  battery: LiPo (charged via TP4056A)
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Distributed as part of the Fri3d Camp 2018 bipedal robot kit alongside the Ph0xx badge.
make_your_own:
  open_source: partial
  hardware_url: https://github.com/Fri3dCamp/Fri3dBadge
  firmware_url: https://github.com/Fri3dCamp/Fri3dBadge
  eda_tool: null
links:
- label: github.com/Fri3dCamp/Fri3dBadge
  url: https://github.com/Fri3dCamp/Fri3dBadge
  kind: repo
- label: hackaday.io/project/160533-ph0xx-bot-jewel
  url: https://hackaday.io/project/160533-ph0xx-bot-jewel
  kind: hackaday
- label: web.archive.org/web/2019/wiki2018.fri3d.be/index.php?title=Badge
  url: https://web.archive.org/web/2019/http://wiki2018.fri3d.be/index.php?title=Badge
  kind: website
images:
- file: assets/images/badges/fri3d-2018/fri3d-2018-ph0xx-bot-jewel/39304c887c.jpg
  source: "https://hackaday.io/project/160533-ph0xx-bot-jewel"
  credit: "Wim Van Gool / Fri3d Camp"
  caption: "Ph0xx Bot Jewel expansion board / bipedal robot"
contact: {}
notes: []
status: released
sources:
- kind: url
  url: https://github.com/Fri3dCamp/Fri3dBadge
  title: Fri3dCamp/Fri3dBadge - Arduino library for the Fri3d Camp badge
  accessed: '2026-09-06'
  note: Found via the project's link list; intake pass identified this item here.
- kind: url
  url: https://hackaday.io/project/160533-ph0xx-bot-jewel
  title: "Ph0xx Bot Jewel - Hackaday.io"
  accessed: '2026-09-07'
  note: Project page by Wim Van Gool for Fri3d Camp; describes the bipedal Otto-style robot, the Jewel power module (TP4056A lithium charger + two SX1308 boost converters to 5V) driving four servos, and links Arduino/Fri3dcamp library calibration software. Source of the project photo.
- kind: url
  url: https://github.com/Fri3dCamp/Fri3dBadge
  title: "Fri3dServoJewel library and examples (OneServo, TwoServos) - Fri3dCamp/Fri3dBadge"
  accessed: '2026-09-07'
  note: Confirms the Fri3dServoJewel library name, that it "supports servo motors, using the Servo Jewel add-on board that comes with the Fri3d Camp robot kit," and that firmware/hardware live in the same repo.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: Maker's own Hackaday.io project page and the Fri3dBadge GitHub repo confirm the Jewel is a servo power/expansion board (TP4056A lithium charger + dual SX1308 boost converters to 5V) for the Ph0xx bipedal robot kit, driving four servos, with software support in the Fri3dServoJewel Arduino library. Could not find a dedicated hardware repo/gerbers/BOM specific to the Jewel board itself (the Fri3dBadge repo covers the badge firmware/library, not standalone Jewel PCB design files), nor any price, quantity made, or availability/distribution details beyond "came with the robot kit." The wiki2018.fri3d.be archive page could not be fetched (web.archive.org fetch blocked in this environment) to cross-check kit distribution details.
last_modified_date: '2026-09-07'
---

The Ph0xx Bot Jewel is a small expansion board that came with Fri3d Camp's 2018 bipedal robot kit, built around the camp's Ph0xx badge. Rather than a badge or SAO in the usual sense, it is a power module: a TP4056A lithium charging IC paired with two SX1308 boost converters regulate a LiPo cell up to a steady 5V, giving enough current headroom to drive the four servo motors used in the robot's ankle and hip joints. The robot itself is loosely based on the open-source "Otto" bipedal design, adapted into a wooden-bodied kit for the camp.

Software support for the Jewel lives in the Fri3dBadge Arduino library as `Fri3dServoJewel`, with `OneServo` and `TwoServos` example sketches showing how to drive the attached motors from the badge. The project was documented on Hackaday.io by Wim Van Gool for Fri3d Camp, alongside assembly and motor-calibration instructions for builders assembling the robot kit.

No standalone hardware files (schematic/gerbers/BOM) specific to the Jewel board were found separate from the badge firmware repo, and no price, production quantity, or availability details surfaced beyond it being bundled with the robot kit.
