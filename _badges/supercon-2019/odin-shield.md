---
title: Odin Shield
id: supercon-2019-odin-shield
layout: badge
parent: Supercon 2019
grand_parent: Badge Archive
nav_exclude: true
type: other
event: supercon-2019
year: 2019
makers:
- name: Celcyon team
summary: A custom shield built onto the 2019 Hackaday Supercon badge, adding an ESP32-WROOM-32 and an RFM69HCW sub-GHz radio to turn the badge into an FPV control console for a robot.
functions: Controlled a robot over sub-GHz radio and displayed its live video feed on screen, functioning as an FPV (first-person view) ground control station built on top of the badge.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - radio
tech:
  mcu: ESP32-WROOM-32
  leds: null
  display: null
  connectivity:
  - sub-ghz
  - wifi
  battery: null
  sao_version: null
get_one:
  price: ''
  price_usd: null
  quantity: ''
  availability: unknown
  distribution: []
  where: ''
make_your_own:
  open_source: null
  hardware_url: null
  firmware_url: null
  eda_tool: null
links:
- label: hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge
  url: https://hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge/
  kind: article
- label: hackaday.com/badge-hacking-2019-09-odin-shield
  url: https://hackaday.com/badge-hacking-2019-09-odin-shield/
  kind: article
images:
- file: assets/images/badges/supercon-2019/odin-shield/1d6570c24d.jpg
  source: "https://hackaday.com/badge-hacking-2019-09-odin-shield/"
  credit: "Celcyon team / Hackaday"
  caption: "Odin Shield badge hack, shown at Supercon 2019 badge hacking ceremony"
contact: {}
notes:
- An ambitious badge hack adding an ESP32-WROOM-32 and RFM69HCW wireless transceiver to control an FPV robot, shown at the 2019 badge hacking ceremony. Found by the event-year sweep, task supercon-2019.
status: listed
sources:
- kind: url
  url: https://hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge/
  title: Odin Shield
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:supercon-2019); event read as ''supercon-2019''.'
- kind: url
  url: https://hackaday.com/2019/11/29/a-fantastic-frontier-of-fpga-flexibility-found-in-the-2019-supercon-badge/
  title: A Fantastic Frontier Of FPGA Flexibility Found In The 2019 Supercon Badge
  accessed: '2026-09-08'
  note: Confirms the Odin Shield's components (ESP32-WROOM-32, RFM69HCW sub-GHz transceiver) and its goal of turning the badge into an FPV robot control console.
- kind: url
  url: https://hackaday.com/badge-hacking-2019-09-odin-shield/
  title: Badge Hacking 2019 09 - Odin Shield
  accessed: '2026-09-08'
  note: Dedicated Hackaday badge-hacking gallery post for this project; provided the photo of the physical hack, no additional body text.
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-08'
  notes: This is a one-off conference badge hack (built during the Supercon 2019 badge hacking session), not a mass-produced or sold badge/SAO, so pricing, quantity, and availability fields are genuinely not applicable/unknown. No maker project page, GitHub repo, or team member names beyond "Celcyon" were found; both sources are Hackaday coverage of the same badge-hacking ceremony. LED and display details for the shield itself were not specified in either source (the "display" mentioned is the host badge's own screen showing the robot's video feed, not a display added by the shield).
last_modified_date: '2026-09-08'
---

The Odin Shield was a hardware hack built by a team going by "Celcyon" onto the 2019 Hackaday Superconference badge, entered into that year's badge hacking ceremony. Rather than a badge or SAO sold to attendees, it was a custom add-on board carrying an ESP32-WROOM-32 microcontroller and an RFM69HCW sub-GHz wireless transceiver, built with the specific goal of turning the Supercon badge into a first-person-view (FPV) ground control console for a robot — using the badge's own screen to display a live video feed while the sub-GHz radio handled the control link back to the robot.

Coverage is limited to two Hackaday posts from the 2019 badge hacking wrap-up: a general roundup describing the shield's components and purpose, and a dedicated gallery post carrying a photo of the physical hardware. No maker page, repository, or further identifying details for the "Celcyon" team were located.
