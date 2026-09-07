---
title: DrawBot_Badge — A Conference Badge that Draws
id: supercon-2018-drawbot-badge-a-conference-badge-that-draws
layout: badge
parent: Supercon 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: supercon-2018
year: 2018
makers:
- name: bdring
  url: https://github.com/bdring
summary: An ESP32-based CNC controller badge built during a "Getting Started in Small Scale CNC and Robotics" workshop at the 2018 Hackaday Superconference, where it drove a small pantograph pen plotter that drew wiggly line drawings on a stack of Post-it notes.
functions: 'Runs a fork of Grbl_ESP32 to control a small 3-axis (pantograph-style) CNC/drawing mechanism: two servos position the pen and a third lifts the assembly to raise/lower it. Gravity provides pen pressure, so it draws while hanging from a lanyard or resting on a table. The PCB also supports stepper motors, limit switches, a touch probe, laser module control, and a web interface over WiFi.'
look:
  colors: []
  shape: null
  themes:
  - robot
  - hardware tool
  - learn to solder
tech:
  mcu: ESP32
  leds: null
  display: none
  connectivity:
  - wifi
  - bluetooth
  battery: 'battery, USB, or DC barrel jack'
  sao_version: null
get_one:
  price: 'under $12 (BOM, excluding 3D-printed parts)'
  price_usd: 12
  quantity: ''
  availability: unknown
  distribution:
  - kit
  where: Built by attendees during the paid workshop at the 2018 Hackaday Superconference; not sold as a standalone product.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/bdring/DrawBot_Badge
  firmware_url: https://github.com/bdring/DrawBot_Badge
  eda_tool: null
links:
- label: github.com/bdring/DrawBot_Badge
  url: https://github.com/bdring/DrawBot_Badge
  kind: repo
- label: DrawBot Badge Represents The CNC World In Badge Design (Hackaday)
  url: https://hackaday.com/2018/09/16/drawbot-badge-represents-the-cnc-world-in-badge-design/
  kind: article
- label: DrawBot Badge – Preview (Buildlog.Net Blog)
  url: https://www.buildlog.net/blog/2018/09/drawbot-badge-preview/
  kind: article
- label: Assembly Instructions (GitHub wiki)
  url: https://github.com/bdring/DrawBot_Badge/wiki/Assembly-Instructions
  kind: doc
images:
- file: assets/images/badges/supercon-2018/drawbot-badge-a-conference-badge-that-draws/e3c3a75df1.jpg
  source: "https://github.com/bdring/DrawBot_Badge"
  credit: "bdring"
  caption: "The DrawBot Badge PCB controller"
contact: {}
notes:
- 'Sheet title kept as-is ("DrawBot_Badge — A Conference Badge that Draws"), matching the GitHub repo name and tagline.'
status: released
sources:
- kind: url
  url: https://github.com/bdring/DrawBot_Badge
  title: DrawBot_Badge — A Conference Badge that Draws
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: github-topics); event read as ''unknown''.'
- kind: url
  url: https://github.com/bdring/DrawBot_Badge
  title: 'GitHub - bdring/DrawBot_Badge: A Conference Badge that Draws #Badgelife'
  accessed: '2026-09-07'
  note: 'README: ESP32 Grbl_ESP32 fork, feature list, "for the 2018 Hackaday Superconference" workshop, image URL.'
- kind: url
  url: https://hackaday.com/2018/09/16/drawbot-badge-represents-the-cnc-world-in-badge-design/
  title: DrawBot Badge Represents The CNC World In Badge Design
  accessed: '2026-09-07'
  note: 'Confirms maker Bart Dring, mechanism (pantograph, gravity pen pressure), BOM cost under $12 excluding 3D-printed parts.'
- kind: url
  url: https://www.buildlog.net/blog/2018/09/drawbot-badge-preview/
  title: DrawBot Badge – Preview
  accessed: '2026-09-07'
  note: 'Listed as a source; maker''s own blog preview of the badge (page returned rate-limited on fetch, not read in full).'
research:
  status: researched
  confidence: medium
  last_checked: '2026-09-07'
  notes: 'Event corrected from "other" to supercon-2018: the README and Hackaday coverage both state it was built during a "Getting Started in Small Scale CNC and Robotics" workshop (co-taught with Jason Huggins of Tapster Robotics) at the 2018 Hackaday Superconference. No SAO header details, LED count, quantity produced, or a maker-provided price beyond the BOM estimate were found. buildlog.net/blog/2018/11/hackaday-workshop-and-badgelife-experience/ returned HTTP 429 and was not read.'
last_modified_date: '2026-09-07'
redirect_from:
- /badges/other/drawbot-badge-a-conference-badge-that-draws/
---

The DrawBot Badge is an ESP32-powered CNC controller board that Bart Dring (bdring) built as the hands-on centerpiece of a workshop he co-taught with Jason Huggins of Tapster Robotics at the 2018 Hackaday Superconference, titled "Getting Started in Small Scale CNC and Robotics." Rather than blinking LEDs, the badge doubles as a small pantograph plotter: two servos position a pen arm and a third lifts it to raise or lower the tip, with gravity supplying the drawing pressure, so the badge draws while it hangs from its lanyard or sits on a table. It runs a fork of Grbl_ESP32, and the PCB is built to handle far more than the drawing demo alone — stepper motor drivers, limit switches, a touch probe, laser module control, WiFi/Bluetooth, an SD card slot, and a web interface are all present, intended as a general-purpose small-CNC controller that happens to double as a badge.

Workshop attendees assembled and programmed their own badge over the course of the session, using it afterward to draw wiggly line sketches onto a stack of Post-it notes clipped underneath. The bill of materials, not counting the 3D-printed pantograph arms, came in at under $12. Hardware and firmware are both published on GitHub, with assembly instructions on the project's wiki, but no independent sale or public giveaway beyond the workshop build has been found.
