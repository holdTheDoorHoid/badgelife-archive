---
title: TiLDA Mk4
id: emf-camp-2018-tilda-mk4
layout: badge
parent: EMF Camp 2018
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: emf-camp-2018
year: 2018
makers:
- name: EMF Camp badge team
summary: The official free badge for EMF Camp 2018, a MicroPython-programmable handheld with a color screen that also works as a working GSM phone via a bundled Hologram SIM.
functions: Runs community-written MicroPython apps loaded over USB, doubles as a phone for on-site calls/SMS using the bundled SIM, and reads onboard temperature/humidity/light sensors; expandable via Grove headers and a Defcon connector.
look:
  colors: []
  shape: null
  themes:
  - hardware tool
  - radio
tech:
  mcu: MSP432E4
  leds:
    count: 2
    type: WS2812B
    note: ''
  display: 240x320 RGB LCD
  connectivity:
  - wifi
  - bluetooth
  - gps
  battery: LiPo 2000 mAh
  sao_version: null
get_one:
  price: free
  price_usd: 0
  quantity: ''
  availability: free
  distribution:
  - free_drop
  where: Given to every attendee of EMF Camp 2018.
make_your_own:
  open_source: yes
  hardware_url: https://github.com/emfcamp/Mk4-Hardware
  firmware_url: https://github.com/emfcamp/Mk4-Apps
  eda_tool: null
links:
- label: blog.emfcamp.org/2018/08/26/tilda-mk4-the-emf-2018-badge
  url: https://blog.emfcamp.org/2018/08/26/tilda-mk4-the-emf-2018-badge/
  kind: website
- label: badge.emfcamp.org/TiLDA_MK4
  url: https://badge.emfcamp.org/TiLDA_MK4/
  kind: doc
- label: github.com/emfcamp/Mk4-Hardware
  url: https://github.com/emfcamp/Mk4-Hardware
  kind: repo
- label: github.com/emfcamp/Mk4-Apps
  url: https://github.com/emfcamp/Mk4-Apps
  kind: repo
images:
- file: assets/images/badges/emf-camp-2018/tilda-mk4/e35b349ede.jpg
  source: "https://blog.emfcamp.org/2018/08/26/tilda-mk4-the-emf-2018-badge/"
  credit: "EMF Camp"
  caption: "Front of the TiLDA Mk4 badge"
- file: assets/images/badges/emf-camp-2018/tilda-mk4/0c8dcc43dc.jpg
  source: "https://blog.emfcamp.org/2018/08/26/tilda-mk4-the-emf-2018-badge/"
  credit: "EMF Camp"
  caption: "Rear of the TiLDA Mk4 badge"
contact: {}
notes:
- Official EMF Camp 2018 badge built around a TI SimpleLink MSP432E4/CC3120, notable as a fully working GSM phone via a supplied Hologram SIM. Found by the event-year sweep, task emf-addons.
status: released
sources:
- kind: url
  url: https://blog.emfcamp.org/2018/08/26/tilda-mk4-the-emf-2018-badge/
  title: TiLDA Mk4
  accessed: '2026-09-07'
  note: 'Found by the archive''s discovery sweep (angle: sweep:emf-addons); event read as ''emf-camp-2018''.'
- kind: url
  url: https://badge.emfcamp.org/TiLDA_MK4/
  title: Index - EMF Badge Documentation
  accessed: '2026-09-08'
  note: Confirms phone functionality via the Hologram SIM and general badge use.
- kind: url
  url: https://github.com/emfcamp/Mk4-Hardware
  title: emfcamp/Mk4-Hardware
  accessed: '2026-09-08'
  note: Open hardware repo for the badge.
- kind: url
  url: https://github.com/emfcamp/Mk4-Apps
  title: emfcamp/Mk4-Apps
  accessed: '2026-09-08'
  note: Open firmware/apps repo (MicroPython) for the badge.
research:
  status: researched
  confidence: high
  last_checked: '2026-09-08'
  notes: 'Core facts confirmed on the maker''s own blog post and documentation site, plus the open hardware/firmware repos on the emfcamp GitHub org. Quantity made (number of attendees who received one) was not stated on the sources checked, so get_one.quantity is left empty. No price/quantity figures found beyond "free, given to attendees."'
last_modified_date: '2026-09-08'
---

The TiLDA Mk4 was the official, free badge given to every attendee of EMF Camp 2018, the UK's outdoor tech and hacker camping festival. Built by the EMF Camp badge team with sponsorship from Texas Instruments, HCD, and Seeed Studio, it centers on a TI SimpleLink MSP432E4 (ARM Cortex-M4F @ 120MHz) paired with a CC3120 Wi-Fi network processor, a 240x320 color LCD, two WS2812B RGB LEDs, a T9 keypad and joystick, and a 2000mAh battery. It is programmed in MicroPython, with apps loaded simply by copying files over USB.

Its standout feature is that it doubles as a working phone: a SIM800 quad-band GSM/GPRS module with Bluetooth, combined with a Hologram SIM card supplied in the box, let attendees make calls and send texts over the on-site cellular network as well as use global IoT data. The badge also carried temperature, humidity, and light sensors, a built-in speaker and microphone, and Grove headers plus a "Defcon connector" for hardware expansion.

Both the hardware design and the firmware/apps were released as open source on the emfcamp GitHub organization, and the badge documentation site has continued to host build and usage instructions. The badge remained popular enough post-event that hobbyists repurposed surplus units for other projects, such as home-automation wall control panels.

## Make your own

Hardware design files are in [emfcamp/Mk4-Hardware](https://github.com/emfcamp/Mk4-Hardware); firmware and MicroPython apps are in [emfcamp/Mk4-Apps](https://github.com/emfcamp/Mk4-Apps). Build instructions for the firmware are documented at [badge.emfcamp.org/TiLDA_MK4/Building_Firmware](https://badge.emfcamp.org/TiLDA_MK4/Building_Firmware/).
