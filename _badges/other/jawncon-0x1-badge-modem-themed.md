---
title: JawnCon 0x1 Badge (modem-themed)
id: other-jawncon-0x1-badge-modem-themed
layout: badge
parent: Other
grand_parent: Badge Archive
nav_exclude: true
type: badge
event: other
year: 2024
makers:
- name: JawnCon organizers
  url: https://jawncon.org
summary: A wearable badge that replicates the Hayes SmartModem 1200 in miniature, built around an ESP32 running the open-source RetroWiFiModem firmware.
functions: Simulates the Hayes AT command set so attendees can dial into early-internet-style services (BBSes) over Wi-Fi from a modern computer; vintage red LEDs light up to show modem activity/status the way the original Hayes modem's did.
look:
  colors: [silver, red]
  shape: rectangle
  themes: [retro computer, wearable]
  form_factor: pcb badge
tech:
  mcu: ESP32
  leds:
    count: null
    type: discrete
    note: Vintage 1980s-era through-hole red LEDs, hand-installed and bent to right angles to mimic the original Hayes SmartModem's indicator lights.
  display: none
  connectivity: [wifi]
  battery: null
  sao_version: none
get_one:
  price: ''
  price_usd: null
  quantity: '~200-250'
  availability: free
  distribution: [free_drop]
  where: Given to attendees of JawnCon 0x1 (Philadelphia-area hacker con, general admission $100, free for students) on October 11-12, 2024.
make_your_own:
  open_source: partial
  hardware_url: null
  firmware_url: https://github.com/mecparts/RetroWiFiModem
  eda_tool: null
links:
- label: hackaday.com/2024/09/16/the-jawncon-0x1-badge-dials-up-a-simpler-time
  url: https://hackaday.com/2024/09/16/the-jawncon-0x1-badge-dials-up-a-simpler-time/
  kind: article
- label: "JawnCon0x1: The Modem Badge"
  url: https://jawncon.org/0x1-modem.html
  kind: website
- label: "RetroWiFiModem firmware (mecparts/RetroWiFiModem)"
  url: https://github.com/mecparts/RetroWiFiModem
  kind: repo
images:
  - file: assets/images/badges/other/jawncon-0x1-badge-modem-themed/d5e8afcb07.jpg
    source: "https://jawncon.org/0x1-modem.html"
    credit: "JawnCon"
    caption: "The JawnCon 0x1 modem badge"
  - file: assets/images/badges/other/jawncon-0x1-badge-modem-themed/9b2c29fc23.jpg
    source: "https://jawncon.org/0x1-modem.html"
    credit: "JawnCon"
    caption: "Isometric CAD view of the badge case"
contact: {}
notes:
- Hayes SmartModem replica wearable, ESP32 + RetroWiFiModem, ~200-250 hand-soldered units.
status: released
sources:
- kind: url
  url: https://hackaday.com/2024/09/16/the-jawncon-0x1-badge-dials-up-a-simpler-time/
  title: JawnCon 0x1 Badge (modem-themed)
  accessed: '2026-09-06'
  note: 'Found by the archive''s discovery sweep (angle: hackaday-press); event read as ''JawnCon 0x1 (Philadelphia, Oct 11-12 2024)''.'
- kind: url
  url: https://jawncon.org/0x1-modem.html
  title: "JawnCon0x1: The Modem Badge"
  accessed: '2026-09-07'
  note: "Maker's own project page: chip (ESP32), LED details, quantity (~200-250), 3D-printed case construction, distribution, and image URLs."
- kind: url
  url: https://github.com/mecparts/RetroWiFiModem
  title: "GitHub - mecparts/RetroWiFiModem"
  accessed: '2026-09-07'
  note: "Confirms the firmware running on the badge is open source; hardware/PCB design files were not found published."
research:
  status: researched
  confidence: high
  last_checked: '2026-09-07'
  notes: 'MCU corrected from ESP8266 (per Hackaday summary) to ESP32, per the maker''s own jawncon.org page, which is more authoritative. LED count not stated by any source. No PCB/hardware design files found published (only the RetroWiFiModem firmware repo, which is a general-purpose project, not JawnCon-specific hardware). Price not disclosed anywhere found; badge was a free con giveaway. No event id exists yet in _data/events.yml for "JawnCon" or "jawncon-0x1" -- event left as "other"; this item was made for JawnCon 0x1, Philadelphia, October 11-12 2024.'
last_modified_date: '2026-09-07'
---

The JawnCon 0x1 badge is a hand-built replica of the classic Hayes SmartModem 1200, shrunk down into a wearable badge. Built by the JawnCon organizers for the inaugural JawnCon security conference in Philadelphia (October 11-12, 2024), the badge houses an ESP32 module running RetroWiFiModem, an open-source firmware project that emulates a Hayes AT-command modem over Wi-Fi. Vintage-style red through-hole LEDs, salvaged in period-correct style and hand-bent to right angles, recreate the blinking status lights of the original SmartModem.

About 200 to 250 badges were made for the roughly 200-250 attendees, each with a hand-soldered PCB and headers seated inside a three-piece, silver silk PLA case that the organizers 3D-printed on a single Prusa MK4 over about six weeks without a failed print. Fronts were individually laser-marked, and a lanyard attaches directly to the PCB rather than the case for durability. The badge let attendees plug in a modern computer and dial into early-internet-style BBS services using genuine AT commands, echoing the dial-up era the Hayes modem represents.

## Make your own

The badge's firmware, RetroWiFiModem, is open source and available on GitHub (mecparts/RetroWiFiModem); it targets ESP8266/ESP32 boards in general and is not JawnCon-specific. No PCB, enclosure, or BOM files for the JawnCon badge itself were found published.
